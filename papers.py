#!/usr/bin/env python3
"""
Metadados + texto completo (secção a secção) de artigos
(ScienceDirect, ACM DL, IEEE Xplore).

Uso:
  python papers.py -f urls.txt -o resumo.md
  python papers.py URL1 URL2 ...
  python papers.py -f urls.txt --json -o resumo.json
  python papers.py -f urls.txt --no-fulltext        # só metadados + abstract

Cada linha do urls.txt:  URL [DOI]
  Também aceita só o DOI ou um link doi.org.

Texto completo:
  1. Abre a página do editor no Firefox instalado ou no Chromium Playwright
     e extrai o HTML do artigo.
  2. Se a página exigir autenticação, podes iniciar sessão no browser e continuar.
  3. Usa arXiv HTML apenas se não conseguir obter o corpo do artigo no editor.

Deps: pip install requests beautifulsoup4 playwright selenium
     playwright install chromium
"""
import argparse
import configparser
import html
import json
import re
import subprocess
import sys
import time
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import quote, urlparse

import requests
from bs4 import BeautifulSoup

S = requests.Session()
S.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
})

FIELDS = ["title", "authors", "venue", "year", "doi", "abstract", "keywords",
          "tldr", "citations", "pdf", "pdf_urls", "arxiv"]
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", re.I)
LAST = {}  # url -> último estado HTTP / erro (diagnóstico)
BROWSER_LAST = {}  # url -> estado do HTML no browser


class SeleniumFirefoxPage:
    """Adapta o Firefox instalado à pequena interface usada pelo extrator."""
    def __init__(self, driver):
        self.driver = driver

    def goto(self, url, wait_until=None, timeout=60000):
        self.driver.set_page_load_timeout(timeout / 1000)
        self.driver.get(url)
        return None

    @staticmethod
    def wait_for_timeout(milliseconds):
        time.sleep(milliseconds / 1000)

    def title(self):
        return self.driver.title

    def locator(self, selector):
        from selenium.webdriver.common.by import By
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return _SeleniumElement(element)

    def content(self):
        return self.driver.page_source


class _SeleniumElement:
    def __init__(self, element):
        self.element = element

    def inner_text(self, timeout=None):
        return self.element.text


def firefox_default_profile():
    """Resolve o perfil selecionado pela instalação normal do Firefox no macOS."""
    root = Path.home() / "Library/Application Support/Firefox"
    ini = root / "profiles.ini"
    if not ini.exists():
        raise RuntimeError(f"Não encontrei o ficheiro de perfis do Firefox: {ini}")
    config = configparser.ConfigParser()
    config.read(ini)
    # O perfil associado à instalação costuma ser o usado pela app atualmente.
    for section in config.sections():
        if section.startswith("Install") and config.has_option(section, "Default"):
            candidate = root / config.get(section, "Default")
            if candidate.is_dir():
                return candidate
    for section in config.sections():
        if section.startswith("Profile") and config.get(section, "Default", fallback="0") == "1":
            path = config.get(section, "Path")
            candidate = root / path if config.get(section, "IsRelative", fallback="1") == "1" else Path(path)
            if candidate.is_dir():
                return candidate
    raise RuntimeError("Não consegui identificar o perfil predefinido do Firefox.")


def unlock_stale_firefox_profile(profile):
    """Recusa perfil ativo; remove apenas marcadores de lock deixados sem processo Firefox."""
    try:
        proc_list = subprocess.run(
            ["ps", "-axo", "command"], capture_output=True, text=True, check=True
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"Não consegui verificar se o Firefox está ativo: {exc}") from exc
    profile_s = str(profile)
    active = any(
        "/Applications/Firefox.app/Contents/MacOS/firefox" in line and profile_s in line
        for line in proc_list.splitlines()
    )
    if active:
        raise RuntimeError("O teu perfil Firefox está em uso. Sai do Firefox (Firefox > Sair) e volta a executar.")
    for lock_name in (".parentlock", "parent.lock"):
        lock = profile / lock_name
        if lock.exists() or lock.is_symlink():
            try:
                lock.unlink()
            except OSError as exc:
                raise RuntimeError(f"Não consegui limpar o bloqueio antigo {lock}: {exc}") from exc


# ---------- helpers ----------
def get(url, **kw):
    kw.setdefault("timeout", 20)
    try:
        r = S.get(url, **kw)
        LAST[url] = r.status_code
        return r if r.ok else None
    except requests.RequestException as e:
        LAST[url] = type(e).__name__
        return None


def jget(url, **kw):
    r = get(url, **kw)
    try:
        return r.json() if r else None
    except ValueError:
        return None


def clean(t):
    if not t:
        return None
    t = re.sub(r"<[^>]+>", " ", html.unescape(t))
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"^abstract\b[:.\s]*", "", t, flags=re.I)
    return t or None


def norm_doi(d):
    if not d:
        return None
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", d.strip(), flags=re.I) or None


def first(xs):
    return xs[0] if xs else None


def tidy(t):
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\s+([.,;:)\]])", r"\1", t)
    return re.sub(r"([(\[])\s+", r"\1", t)


# ---------- identificar site ----------
def identify(url):
    if re.match(r"^10\.\d{4,9}/\S+$", url) or "doi.org/" in url:
        return "doi", {"doi": norm_doi(url)}
    u = urlparse(url)
    h, p = u.netloc.lower(), u.path
    if "sciencedirect.com" in h:
        m = re.search(r"/pii/([A-Za-z0-9]+)", p)
        return "sciencedirect", {"pii": m.group(1)} if m else {}
    if "dl.acm.org" in h:
        m = re.search(r"/doi/(?:abs/|full/|pdf/|epdf/)?(10\.\d+/[^?#]+)", p)
        return "acm", {"doi": m.group(1)} if m else {}
    if "ieeexplore.ieee.org" in h:
        m = re.search(r"/document/(\d+)", p)
        return "ieee", {"arnumber": m.group(1)} if m else {}
    raise ValueError("site não suportado (usa ScienceDirect, ACM ou IEEE Xplore)")


# ---------- metadados ----------
def from_page(url):
    if "ieeexplore" in url:
        get("https://ieeexplore.ieee.org/")  # cookies
        r = get(url, headers={"Referer": "https://ieeexplore.ieee.org/"})
    else:
        r = get(url)
    if not r:
        return {}
    soup = BeautifulSoup(r.text, "html.parser")

    def meta(*names):
        for n in names:
            v = [m["content"].strip()
                 for m in soup.find_all("meta", attrs={"name": re.compile(f"^{re.escape(n)}$", re.I)})
                 if m.get("content")]
            if v:
                return v
        return []

    date = first(meta("citation_publication_date", "citation_date", "dc.date")) or ""
    ym = re.search(r"\d{4}", date)
    kw = first(meta("citation_keywords")) or ""
    d = {
        "title": first(meta("citation_title", "dc.title")),
        "authors": meta("citation_author", "dc.creator"),
        "venue": first(meta("citation_journal_title", "citation_conference_title")),
        "year": ym.group(0) if ym else None,
        "doi": norm_doi(first(meta("citation_doi", "dc.identifier"))),
        "abstract": clean(first(meta("citation_abstract", "dc.description", "description"))),
        "keywords": [k.strip() for k in re.split(r"[;,]", kw) if k.strip()],
    }

    i = r.text.find("xplGlobal.document.metadata")  # IEEE: JSON embebido
    if i >= 0:
        j = r.text.find("{", i)
        try:
            x, _ = json.JSONDecoder().raw_decode(r.text[j:])
            d.update({k: v for k, v in {
                "title": x.get("title"),
                "abstract": clean(x.get("abstract")),
                "authors": [a["name"] for a in x.get("authors", []) if a.get("name")],
                "doi": norm_doi(x.get("doi")),
                "venue": x.get("publicationTitle"),
                "year": str(x.get("publicationYear") or "")[:4] or None,
                "keywords": [k for kw_ in x.get("keywords", []) for k in kw_.get("kwd", [])],
            }.items() if v})
        except ValueError:
            pass
    return {k: v for k, v in d.items() if v}


def from_crossref(doi=None, pii=None):
    w = None
    if doi:
        j = jget(f"https://api.crossref.org/works/{quote(doi, safe='/')}")
        w = (j or {}).get("message")
    elif pii:  # Elsevier regista o PII como alternative-id
        j = jget("https://api.crossref.org/works",
                 params={"filter": f"alternative-id:{pii}", "rows": 1})
        w = first(((j or {}).get("message") or {}).get("items") or [])
    if not w:
        return {}
    dp = first(first((w.get("issued") or {}).get("date-parts") or []) or [])
    return {k: v for k, v in {
        "title": clean(first(w.get("title") or [])),
        "authors": [" ".join(filter(None, [a.get("given"), a.get("family")]))
                    for a in w.get("author", [])],
        "venue": first(w.get("container-title") or []),
        "year": str(dp) if dp else None,
        "doi": norm_doi(w.get("DOI")),
        "abstract": clean(w.get("abstract")),
        "keywords": w.get("subject") or [],
    }.items() if v}


def uninvert(idx):
    if not idx:
        return None
    return " ".join(w for _, w in sorted((p, w) for w, ps in idx.items() for p in ps))


def from_openalex(doi=None, url=None):
    w = None
    if doi:
        w = jget(f"https://api.openalex.org/works/doi:{quote(doi, safe='/')}")
    elif url:
        j = jget("https://api.openalex.org/works",
                 params={"filter": f"locations.landing_page_url:{url}"})
        w = first((j or {}).get("results") or [])
    if not w or not w.get("title"):
        return {}
    src = (w.get("primary_location") or {}).get("source") or {}
    locs = [w.get("best_oa_location"), w.get("primary_location")] + (w.get("locations") or [])
    pdfs = [l["pdf_url"] for l in locs if l and l.get("pdf_url")]
    oa_url = (w.get("open_access") or {}).get("oa_url")
    if oa_url:
        pdfs.append(oa_url)
    return {k: v for k, v in {
        "title": w.get("title"),
        "authors": [a["author"]["display_name"] for a in w.get("authorships", [])
                    if a.get("author")],
        "venue": src.get("display_name"),
        "year": str(w.get("publication_year") or "") or None,
        "doi": norm_doi(w.get("doi")),
        "abstract": uninvert(w.get("abstract_inverted_index")),
        "keywords": [k["display_name"] for k in w.get("keywords", [])],
        "citations": w.get("cited_by_count"),
        "pdf": oa_url,
        "pdf_urls": list(dict.fromkeys(pdfs)),
    }.items() if v}


def from_s2(doi):
    j = jget(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='/')}",
             params={"fields": "title,abstract,tldr,year,venue,authors,citationCount,"
                               "openAccessPdf,externalIds"})
    if not j:
        return {}
    pdf = (j.get("openAccessPdf") or {}).get("url")
    return {k: v for k, v in {
        "title": j.get("title"),
        "authors": [a["name"] for a in j.get("authors", []) if a.get("name")],
        "venue": j.get("venue"),
        "year": str(j.get("year") or "") or None,
        "abstract": clean(j.get("abstract")),
        "tldr": (j.get("tldr") or {}).get("text"),
        "citations": j.get("citationCount"),
        "pdf": pdf,
        "pdf_urls": [pdf] if pdf else None,
        "arxiv": (j.get("externalIds") or {}).get("ArXiv"),
    }.items() if v}


# ---------- texto completo: HTML do editor ----------
HTML_SELECTORS = (
    "#article-body", ".article__body", ".article-body", ".Body",
    ".document-main", ".document-text", "#full-text", "#body",
    "article", "main",
)
REMOVE_SELECTORS = (
    "script", "style", "noscript", "header", "footer", "nav", "aside",
    "[role=navigation]", ".references", "#references", ".article-tools",
    ".cookie-banner", ".cookie-consent", ".recommendations",
)


def _article_candidate(soup):
    candidates = []
    for rank, selector in enumerate(HTML_SELECTORS):
        for node in soup.select(selector):
            if node.name in ("html", "body"):
                continue
            clone = BeautifulSoup(str(node), "html.parser")
            root = clone.find()
            if not root:
                continue
            for selector_to_remove in REMOVE_SELECTORS:
                for noise in root.select(selector_to_remove):
                    noise.decompose()
            text = tidy(root.get_text(" ", strip=True))
            paragraphs = root.find_all(["p", "li"])
            headings = root.find_all(re.compile(r"^h[1-6]$"))
            if len(text) < 600:
                continue
            score = len(text) + 90 * len(paragraphs) + 180 * len(headings) - 120 * rank
            candidates.append((score, root, len(text), len(paragraphs), len(headings)))
    if not candidates:
        return None, 0, 0, 0
    _, root, size, paragraphs, headings = max(candidates, key=lambda x: x[0])
    return root, size, paragraphs, headings


def html_sections_from_page(page, title=None):
    """Extrai secções e parágrafos do HTML já carregado no browser."""
    try:
        markup = page.content()
    except Exception:
        return None, 0
    soup = BeautifulSoup(markup, "html.parser")
    root, size, paragraph_count, heading_count = _article_candidate(soup)
    if not root or size < 2200 or (paragraph_count < 4 and heading_count < 3):
        return None, size

    sections = []
    current = {"level": 1, "heading": "Article text", "parts": []}
    title_norm = re.sub(r"\W+", " ", (title or "").lower()).strip()

    def flush():
        text = "\n\n".join(x for x in current["parts"] if x)
        if text.strip():
            sections.append({"level": current["level"], "heading": current["heading"], "text": text})

    for node in root.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "table", "figcaption"]):
        if node.find_parent("table") and node.name != "table":
            continue
        text = tidy(node.get_text(" ", strip=True))
        if not text:
            continue
        if re.fullmatch(r"h[1-6]", node.name or ""):
            heading_norm = re.sub(r"\W+", " ", text.lower()).strip()
            if node.name == "h1" and title_norm and heading_norm == title_norm:
                continue
            flush()
            current = {"level": max(1, min(3, int(node.name[1]) - 1)), "heading": text, "parts": []}
        elif node.name == "table":
            rows = []
            for tr in node.find_all("tr"):
                cells = [tidy(c.get_text(" ", strip=True)) for c in tr.find_all(["th", "td"], recursive=False)]
                if cells:
                    rows.append(" | ".join(cells))
            if rows:
                current["parts"].append("\n".join(rows))
        else:
            current["parts"].append(text)
    flush()
    body_chars = sum(len(sec["text"]) for sec in sections)
    if body_chars < 1800:
        return None, body_chars
    return sections, body_chars


def _human_verification_page(page):
    """Identifica páginas de verificação/bloqueio sem interagir com o desafio."""
    try:
        title = page.title()
        body = page.locator("body").inner_text(timeout=3000)
    except Exception:
        title, body = "", ""
    text = (title + " " + body[:5000]).lower()
    markers = (
        "verifying you are human", "verify you are human", "checking your browser",
        "just a moment", "performing security verification", "cf-chl-", "cloudflare",
    )
    return any(marker in text for marker in markers)


def publisher_html_sections(page, url, title=None):
    status = None
    try:
        response = page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)
        status = response.status if response else None
    except Exception as exc:
        print(f"   browser: erro ao abrir HTML ({type(exc).__name__})", file=sys.stderr)

    # Dá tempo à verificação automática normal da página. Se persistir, regista
    # o bloqueio e avança; não pede cliques repetidos nem tenta contornar CAPTCHA.
    if _human_verification_page(page):
        page.wait_for_timeout(4000)
        if _human_verification_page(page):
            BROWSER_LAST[url] = "human_verification"
            print("   editor mantém 'Verifying you are human'; a saltar este HTML e a continuar", file=sys.stderr)
            return None, None

    sections, size = html_sections_from_page(page, title)
    if sections:
        BROWSER_LAST[url] = "html_ok"
        return sections, f"HTML do editor ({urlparse(url).netloc})"

    # Uma tentativa de intervenção manual pode ser útil para login ou para
    # expandir o artigo, mas nunca é usada para clicar/resolver um desafio humano.
    if sys.stdin.isatty():
        print(f"   HTML insuficiente ({size} caracteres; HTTP {status or 'n/d'}). "
              "Se a página tiver um botão normal de acesso ao texto, abre o artigo no browser.", file=sys.stderr)
        input("   Prime Enter depois de o texto integral estar visível; Enter sem alterações continua... ")
        if not _human_verification_page(page):
            sections, size = html_sections_from_page(page, title)
            if sections:
                BROWSER_LAST[url] = "html_ok"
                return sections, f"HTML do editor ({urlparse(url).netloc})"
        else:
            BROWSER_LAST[url] = "human_verification"
            print("   desafio de verificação presente; a saltar este artigo", file=sys.stderr)
            return None, None
    BROWSER_LAST[url] = "html_insufficient"
    return None, None


# ---------- texto completo: arXiv HTML ----------
def arxiv_sections(aid):
    r = get(f"https://arxiv.org/html/{aid}", timeout=40)
    if not r:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    for m in soup.find_all("math"):
        m.replace_with(f" {m.get('alttext', '')} ")
    out = []
    for sec in soup.find_all("section", class_=re.compile(r"^ltx_(sub)*section$|^ltx_appendix$")):
        h = sec.find(re.compile(r"^h[2-6]$"), recursive=False)
        if not h:
            continue
        heading = tidy(h.get_text(" ", strip=True))
        if REFS.match(_core(heading)):
            continue
        paras = [tidy(p.get_text(" ", strip=True))
                 for p in sec.find_all("div", class_="ltx_para", recursive=False)]
        cls = " ".join(sec.get("class", []))
        lvl = 3 if "subsubsection" in cls else 2 if "subsection" in cls else 1
        out.append({"level": lvl, "heading": heading, "text": "\n\n".join(p for p in paras if p)})
    return out if len(out) >= 2 else None


# ---------- texto completo: escolher fonte ----------
def fulltext(p, url, browser_page=None):
    if browser_page is not None:
        sections, source = publisher_html_sections(browser_page, url, p.get("title"))
        if sections:
            return sections, source

    if p.get("arxiv"):
        sections = arxiv_sections(p["arxiv"])
        if sections:
            return sections, f"arXiv HTML ({p['arxiv']})"
    return None, None


# ---------- pipeline ----------
def merge(*srcs):
    out = {}
    for f in FIELDS:
        vals = [s[f] for s in srcs if s.get(f)]
        if not vals:
            continue
        if f == "abstract":
            out[f] = max(vals, key=len)
        elif f == "pdf_urls":
            out[f] = list(dict.fromkeys(u for v in vals for u in v))
        else:
            out[f] = vals[0]
    return out


def process(url, doi_override=None, browser_page=None, full=True):
    kind, ids = identify(url)
    if kind == "doi":
        url, page = f"https://doi.org/{ids['doi']}", {}
    else:
        page = from_page(url)
    doi = norm_doi(doi_override or page.get("doi") or ids.get("doi"))

    cr = from_crossref(doi=doi, pii=None if doi else ids.get("pii"))
    doi = doi or cr.get("doi")
    oa = from_openalex(doi=doi, url=None if doi else url)
    doi = doi or oa.get("doi")
    s2 = from_s2(doi) if doi else {}

    r = merge(page, cr, oa, s2)
    if not r.get("title"):
        raise RuntimeError("sem dados: página bloqueada e DOI não resolvido "
                           "(põe o DOI a seguir ao URL: 'URL 10.xxxx/yyyy')")
    r.update(doi=doi, url=url, source=kind)

    if not r.get("arxiv"):
        for u in (r.get("pdf_urls") or []):
            m = ARXIV.search(u)
            if m:
                r["arxiv"] = m.group(1)
                break

    if full:
        secs, src = fulltext(r, url, browser_page)
        if secs:
            r["sections"], r["fulltext_source"] = secs, src
            print(f"   texto completo: {src} — {len(secs)} secções", file=sys.stderr)
        else:
            if BROWSER_LAST.get(url) == "human_verification":
                r["fulltext_note"] = "O editor apresentou uma página de verificação humana; o texto integral não foi extraído."
            elif not page and kind != "doi":
                r["fulltext_note"] = f"A página não foi lida por requests (HTTP {LAST.get(url)}); o HTML integral não ficou disponível."
                print(f"   página não lida por requests (HTTP {LAST.get(url)}); browser sem corpo HTML suficiente", file=sys.stderr)
            else:
                r["fulltext_note"] = "O browser não encontrou texto integral HTML acessível; foi mantido o resumo/metadados."
            print("   texto integral HTML indisponível; mantido metadados/resumo", file=sys.stderr)
    return r


# ---------- output ----------
def to_md(p):
    au = p.get("authors") or []
    au_s = ", ".join(au[:6]) + (" et al." if len(au) > 6 else "")
    head = " · ".join(filter(None, [p.get("venue"), p.get("year")]))
    L = [f"## {p['title']}", ""]
    if au_s:
        L.append(f"**Autores:** {au_s}  ")
    if head:
        L.append(f"**Publicação:** {head}  ")
    if p.get("doi"):
        L.append(f"**DOI:** https://doi.org/{p['doi']}  ")
    L.append(f"**Fonte:** {p['source']} — {p['url']}  ")
    if p.get("citations") is not None:
        L.append(f"**Citações:** {p['citations']}  ")
    if p.get("keywords"):
        L.append(f"**Keywords:** {', '.join(p['keywords'])}  ")
    if p.get("tldr"):
        L += ["", f"**TL;DR:** {p['tldr']}"]
    if p.get("abstract"):
        L += ["", "**Abstract:**", "", p["abstract"]]
    if p.get("fulltext_note"):
        L += ["", f"**Nota de acesso:** {p['fulltext_note']}"]
    if p.get("sections"):
        L += ["", f"**Texto completo** — {p['fulltext_source']}"]
        for s in p["sections"]:
            L += ["", "#" * (2 + s["level"]) + " " + s["heading"]]
            if s["text"]:
                L += ["", s["text"]]
    elif "sections" not in p:
        pass
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("urls", nargs="*")
    ap.add_argument("-f", "--file", help="ficheiro com um URL por linha")
    ap.add_argument("-o", "--out", help="ficheiro de saída (default: stdout)")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    ap.add_argument("--no-fulltext", action="store_true", help="só metadados + abstract; não abre browser")
    ap.add_argument("--browser", choices=("firefox", "chromium"), default="chromium",
                    help="Firefox instalado ou Chromium Playwright (default: chromium)")
    ap.add_argument("--browser-profile", default=None,
                    help="perfil do browser; Firefox usa por omissão o teu perfil normal")
    a = ap.parse_args()

    urls = list(a.urls)
    if a.file:
        with open(a.file, encoding="utf-8") as fh:
            urls += [line.strip() for line in fh if line.strip() and not line.lstrip().startswith("#")]
    if not urls and not sys.stdin.isatty():
        urls += [line.strip() for line in sys.stdin if line.strip()]
    urls = list(dict.fromkeys(urls))
    if not urls:
        ap.error("indica pelo menos um URL")

    entries = []  # (url, DOI opcional)
    for raw in urls:
        parts = raw.split()
        doi = next((part for part in parts[1:] if part.lower().startswith(("10.", "https://doi.org/", "http://doi.org/"))), None)
        entries.append((parts[0], doi))

    results, errors = [], []
    browser_context = None
    browser_page = None
    playwright_manager = None
    playwright = None
    selenium_driver = None
    if not a.no_fulltext:
        try:
            if a.browser == "firefox":
                from selenium import webdriver
                from selenium.webdriver.firefox.options import Options
                firefox_binary = Path("/Applications/Firefox.app/Contents/MacOS/firefox")
                if not firefox_binary.exists():
                    sys.exit("Não encontrei o Firefox em /Applications/Firefox.app")
                firefox_profile = (Path(a.browser_profile).expanduser().resolve()
                                   if a.browser_profile else firefox_default_profile())
                unlock_stale_firefox_profile(firefox_profile)
                options = Options()
                options.binary_location = str(firefox_binary)
                options.add_argument("-no-remote")
                options.add_argument("-profile")
                options.add_argument(str(firefox_profile))
                selenium_driver = webdriver.Firefox(options=options)
                browser_context = selenium_driver
                browser_page = SeleniumFirefoxPage(selenium_driver)
            else:
                from playwright.sync_api import sync_playwright
                playwright_manager = sync_playwright()
                playwright = playwright_manager.start()
                profile = a.browser_profile or "papers_chromium_profile"
                browser_context = playwright.chromium.launch_persistent_context(
                    str(Path(profile).resolve()), headless=False,
                    viewport={"width": 1400, "height": 1000})
                browser_page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()
        except ImportError as exc:
            sys.exit(f"Falta uma dependência do browser: instala-a com pip. ({exc})")
        except Exception as exc:
            sys.exit(f"Não foi possível abrir {a.browser}: {exc}")

    try:
        for n, (url, doi) in enumerate(entries, 1):
            print(f"[{n}/{len(entries)}] {url}", file=sys.stderr)
            try:
                results.append(process(url, doi, browser_page, not a.no_fulltext))
            except Exception as exc:  # noqa: BLE001
                errors.append({"url": url, "error": str(exc)})
                print(f"   ! {exc}", file=sys.stderr)
            time.sleep(0.5)
    finally:
        if selenium_driver:
            selenium_driver.quit()
        elif browser_context:
            browser_context.close()
        if playwright:
            playwright.stop()

    if a.json:
        text = json.dumps({"papers": results, "errors": errors}, ensure_ascii=False, indent=2)
    else:
        text = "# Resumo de artigos\n\n" + "\n---\n\n".join(to_md(paper) for paper in results)
        if errors:
            text += "\n---\n\n## Falhas\n\n" + "\n".join(f"- {item['url']} — {item['error']}" for item in errors)

    if a.out:
        requested = Path(a.out).expanduser()
        index = 0
        while True:
            if index == 0:
                destination = requested
            else:
                destination = requested.with_name(
                    f"{requested.stem}_{index}{requested.suffix}"
                )
            try:
                # Modo exclusivo: nunca substitui um ficheiro que já exista.
                with destination.open("x", encoding="utf-8") as fh:
                    fh.write(text)
                break
            except FileExistsError:
                index += 1
        print(f"Guardado em {destination}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
