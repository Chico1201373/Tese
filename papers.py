#!/usr/bin/env python3
"""
Resumo de artigos (ScienceDirect, ACM DL, IEEE Xplore).

Uso:
  python papers.py URL1 URL2 ...
  python papers.py -f urls.txt -o resumo.md
  python papers.py -f urls.txt --json -o resumo.json

Formato de cada linha do urls.txt:  URL [DOI]
  O DOI é opcional e serve de fallback quando o site bloqueia a página.
  Também aceita só o DOI (10.xxxx/yyyy) ou um link doi.org.

Deps: pip install requests beautifulsoup4

Estratégia por URL:
  1. Tenta ler a página (meta tags / JSON embebido do IEEE).
  2. Esses sites bloqueiam bots com frequência, por isso resolve o DOI e
     completa com Crossref -> OpenAlex -> Semantic Scholar (APIs abertas).
"""
import argparse
import html
import json
import re
import sys
import time
from urllib.parse import quote, urlparse

import requests
from bs4 import BeautifulSoup

S = requests.Session()
S.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
})

FIELDS = ["title", "authors", "venue", "year", "doi", "abstract",
          "keywords", "tldr", "citations", "pdf"]


# ---------- helpers ----------
LAST = {}  # url -> último estado HTTP / erro (para diagnóstico)


def get(url, **kw):
    try:
        r = S.get(url, timeout=20, **kw)
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


# ---------- fontes ----------
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

    # IEEE Xplore: JSON embebido na página
    i = r.text.find("xplGlobal.document.metadata")
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
    src = ((w.get("primary_location") or {}).get("source") or {})
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
        "pdf": (w.get("open_access") or {}).get("oa_url"),
    }.items() if v}


def from_s2(doi):
    j = jget(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='/')}",
             params={"fields": "title,abstract,tldr,year,venue,authors,citationCount,openAccessPdf"})
    if not j:
        return {}
    return {k: v for k, v in {
        "title": j.get("title"),
        "authors": [a["name"] for a in j.get("authors", []) if a.get("name")],
        "venue": j.get("venue"),
        "year": str(j.get("year") or "") or None,
        "abstract": clean(j.get("abstract")),
        "tldr": (j.get("tldr") or {}).get("text"),
        "citations": j.get("citationCount"),
        "pdf": (j.get("openAccessPdf") or {}).get("url"),
    }.items() if v}


# ---------- pipeline ----------
def merge(*srcs):
    out = {}
    for f in FIELDS:
        vals = [s[f] for s in srcs if s.get(f)]
        if vals:
            out[f] = max(vals, key=len) if f == "abstract" else vals[0]
    return out


def process(url, doi_override=None):
    kind, ids = identify(url)
    if kind == "doi":
        url, page = f"https://doi.org/{ids['doi']}", {}
    else:
        page = from_page(url)
        if not page:
            print(f"   página não lida (HTTP {LAST.get(url)})", file=sys.stderr)
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
    if p.get("pdf"):
        L.append(f"**PDF (open access):** {p['pdf']}  ")
    if p.get("keywords"):
        L.append(f"**Keywords:** {', '.join(p['keywords'])}  ")
    if p.get("tldr"):
        L += ["", f"**TL;DR:** {p['tldr']}"]
    if p.get("abstract"):
        L += ["", "**Abstract:**", "", p["abstract"]]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("urls", nargs="*")
    ap.add_argument("-f", "--file", help="ficheiro com um URL por linha")
    ap.add_argument("-o", "--out", help="ficheiro de saída (default: stdout)")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    a = ap.parse_args()

    urls = list(a.urls)
    if a.file:
        with open(a.file, encoding="utf-8") as fh:
            urls += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not urls and not sys.stdin.isatty():
        urls += [l.strip() for l in sys.stdin if l.strip()]
    urls = list(dict.fromkeys(urls))
    if not urls:
        ap.error("indica pelo menos um URL")
    entries = []  # (url, doi_opcional) — formato por linha: "URL [DOI]"
    for raw in urls:
        p = raw.split()
        entries.append((p[0], p[1] if len(p) > 1 else None))

    results, errors = [], []
    for n, (u, d) in enumerate(entries, 1):
        print(f"[{n}/{len(entries)}] {u}", file=sys.stderr)
        try:
            results.append(process(u, d))
        except Exception as e:  # noqa: BLE001
            errors.append({"url": u, "error": str(e)})
            print(f"   ! {e}", file=sys.stderr)
        time.sleep(1)

    if a.json:
        text = json.dumps({"papers": results, "errors": errors}, ensure_ascii=False, indent=2)
    else:
        text = "# Resumo de artigos\n\n" + "\n---\n\n".join(to_md(p) for p in results)
        if errors:
            text += "\n---\n\n## Falhas\n\n" + "\n".join(f"- {e['url']} — {e['error']}" for e in errors)

    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"Guardado em {a.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()