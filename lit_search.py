#!/usr/bin/env python3
"""
lit_search_v2.py - recolhe títulos para a revisão, deduplica e faz uma pré-triagem. Grava Markdown (+ CSV).

O QUE MUDOU EM RELAÇÃO À v1
  1. Janela temporal exata (por omissão 2021-10-27 a 2026-10-27, o critério registado), com --from-date/--to-date.
  2. Sem limite curto: --max 1000 por (site, query) por omissão; --max 0 = tudo (até 10 000 por segurança).
     O Markdown regista quantos existem na fonte e quantos foram recuperados (regra de paragem).
  3. Deduplicação entre queries (por DOI, ou título normalizado). Cada registo mostra em que RQs apareceu.
  4. Separação automática (heurística) de: revisões/surveys (ficam à parte), trabalhos fora do domínio
     (sem termos de educação/medicina/QA no título ou resumo) e candidatos (o que sobra, por ordem de relevância).
     NADA é apagado: tudo fica listado numa secção com o motivo, para o diagrama PRISMA.
  5. Honestidade da fonte: os registos do modo openalex NÃO vêm da pesquisa nativa dos sites. Para ter
     registos nativos, exporta (RIS) nos próprios sites e junta com --import ficheiro.ris:ieee
     (ou corre o modo browser). Cada registo diz de onde veio.

USO
  pip install requests playwright
  playwright install chromium
  python lit_search.py --mode browser --csv --pages 20 --max 1000
  # Abre as pesquisas nativas; pode ser necessário iniciar sessão em cada site.
  # Recolhe títulos e totais visíveis; não recolhe resumos nem substitui a exportação RIS.
  python lit_search.py --mode openalex --max 1000 --csv  # API OpenAlex, não pesquisa nativa
  python lit_search.py --mode none --import ieee.ris:ieee --import acm.ris:acm
"""
import argparse
import csv
import html
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.parse
from datetime import datetime
from pathlib import Path

import requests

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

QUERIES = {
    "CTX": {
        "title": "Contexto educativo e médico (exemplo do ScienceDirect)",
        "q": '("large language model" OR LLM) AND ("intelligent tutoring system" OR "educational question answering" '
             'OR "medical education" OR "learning platform")',
    },
    "RQ1": {
        "title": "Abordagens para restringir as respostas ao contexto",
        "q": '("large language model" OR LLM) AND (grounding OR "retrieval-augmented generation" OR "context-aware") '
             'AND (chatbot OR "conversational system")',
    },
    "RQ2": {
        "title": "Fidelidade, correção e respostas fora do âmbito",
        "q": '("large language model" OR LLM) AND (faithfulness OR factuality OR correctness OR "scope adherence" '
             'OR abstention) AND (evaluation OR benchmark)',
    },
    "RQ3": {
        "title": "Limitações e compromissos operacionais",
        "q": '("large language model" OR LLM) AND (reliability OR robustness OR security OR "prompt injection" '
             'OR latency OR cost OR integration)',
    },
}

SITES = {
    "sciencedirect": {"label": "ScienceDirect", "prefix": "10.1016"},
    "ieee": {"label": "IEEE Xplore", "prefix": "10.1109"},
    "acm": {"label": "ACM Digital Library", "prefix": "10.1145"},
}

OPENALEX_URL = os.environ.get("OPENALEX_URL", "https://api.openalex.org/works")
HARD_CAP = 10000

# ----------------------------------------------------------------------------
# Pré-triagem (heurística; a decisão de inclusão é SEMPRE manual)
# ----------------------------------------------------------------------------
REVIEW_RE = re.compile(
    r"\b(survey|systematic(?:ally)? review|literature review|scoping review|umbrella review|meta-analysis|"
    r"a review\b|review of|an overview|state[- ]of[- ]the[- ]art review|roadmap|tutorial|mapping study|"
    r"research agenda|taxonomy of|challenges and opportunities)\b", re.I)
EDU_TERMS = ["education", "educational", "student", "students", "tutor", "tutoring", "teaching", "teacher",
             "curriculum", "learner", "learners", "classroom", "e-learning", "exam", "exams", "assessment"]
MED_TERMS = ["medical", "medicine", "clinical", "health", "healthcare", "clinician", "physician", "nurse",
             "nursing", "biomedical", "patient", "patients"]
QA_TERMS = ["multiple-choice", "multiple choice", "mcq", "question answering", "question bank", "question-answering",
            "exam question", "exam questions"]


def term_regex(terms):
    return re.compile(r"(?<![a-z])(" + "|".join(re.escape(t) for t in terms) + r")(?![a-z])", re.I)


EDU_RE, MED_RE, QA_RE = term_regex(EDU_TERMS), term_regex(MED_TERMS), term_regex(QA_TERMS)


def classify(rec):
    text = f"{rec['title']} {rec['abstract']}"
    edu, med, qa = bool(EDU_RE.search(text)), bool(MED_RE.search(text)), bool(QA_RE.search(text))
    if "browser" in rec.get("origins", {rec.get("origin")}) and not rec["abstract"]:
        rec["category"], rec["reason"] = "triagem_manual", "pesquisa nativa recolheu só o título; resumo por verificar"
    elif rec["type"] == "review" or REVIEW_RE.search(rec["title"]):
        rec["category"], rec["reason"] = "revisao", "revisão/survey (secundário; fica à parte da síntese principal)"
    elif edu and (med or qa):
        rec["category"], rec["reason"] = "candidato_A", "educação + medicina/QA no título ou resumo"
    elif edu or med or qa:
        rec["category"], rec["reason"] = "candidato_B", "só um dos eixos (educação, medicina ou QA)"
    else:
        rec["category"] = "fora_dominio"
        rec["reason"] = "sem termos de educação, medicina ou QA" + ("" if rec["abstract"] else " (sem resumo: só título)")
    return rec


def norm_title(t):
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def rec_key(rec):
    return ("doi:" + rec["doi"].lower()) if rec["doi"] else ("t:" + norm_title(rec["title"]))


# ----------------------------------------------------------------------------
# OpenAlex
# ----------------------------------------------------------------------------
def get_json(url, params, retries=5):
    wait = 2.0
    for _ in range(retries):
        try:
            r = requests.get(url, params=params, timeout=60)
        except requests.RequestException as e:
            print(f"   [rede] {e}; a repetir em {wait:.0f}s")
            time.sleep(wait)
            wait *= 2
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429, 500, 502, 503, 504):
            print(f"   [HTTP {r.status_code}] a repetir em {wait:.0f}s")
            time.sleep(wait)
            wait *= 2
            continue
        sys.exit(f"Erro HTTP {r.status_code}: {r.text[:300]}\n"
                 "Se for 401/403, define a chave: export OPENALEX_API_KEY=... (grátis em openalex.org/settings/api)")
    sys.exit("Demasiadas falhas seguidas; tenta mais tarde.")


def abstract_text(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def clean_doi(doi):
    doi = html.unescape(urllib.parse.unquote(str(doi or ""))).strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.rstrip(" .;,\"\'”’)]}>")


def resolve_doi_url(doi):
    """Resolve DOI para a página de destino do editor, sem descarregar o artigo."""
    doi = clean_doi(doi)
    if not doi:
        return ""
    # ACM aceita URL canónico diretamente pelo DOI. Evita páginas de bloqueio do resolver.
    if doi.lower().startswith("10.1145/"):
        return "https://dl.acm.org/doi/" + doi
    try:
        response = requests.get("https://doi.org/" + doi, allow_redirects=True,
                                timeout=25, stream=True, headers={"User-Agent": "Mozilla/5.0 (compatible; thesis-literature-review/1.0)"})
        final_url = response.url
        response.close()
        if final_url and "linkinghub.elsevier.com/retrieve/pii/" in final_url.lower():
            pii = final_url.rstrip("/").rsplit("/", 1)[-1]
            return "https://www.sciencedirect.com/science/article/abs/pii/" + pii
        return final_url if final_url and "doi.org/" not in final_url else "https://doi.org/" + doi
    except requests.RequestException as exc:
        print(f"   [DOI] não resolvido {doi}: {exc}")
        return "https://doi.org/" + doi


def resolve_many_with_log(dois, cache, log_path):
    total = len(dois)
    print(f"A resolver {total} DOI únicos (até 12 em paralelo). Progresso também em: {log_path}", flush=True)
    completed = 0
    with log_path.open("w", encoding="utf-8") as log:
        log.write(f"Início: {datetime.now():%Y-%m-%d %H:%M:%S} | DOI únicos: {total}\n")
        log.flush()
        with ThreadPoolExecutor(max_workers=12) as pool:
            jobs = {pool.submit(resolve_doi_url, doi): doi for doi in dois}
            for future in as_completed(jobs):
                doi = jobs[future]
                try:
                    url = future.result()
                except Exception as exc:
                    print(f"[erro] {doi}: {exc}", flush=True)
                    url = "https://doi.org/" + doi
                cache[doi] = url
                completed += 1
                line = f"[{completed}/{total}] {doi} -> {url}\n"
                log.write(line)
                log.flush()
                if completed == 1 or completed % 25 == 0 or completed == total:
                    print(f"[{completed}/{total}] DOI resolvidos", flush=True)
    print(f"Resolução concluída. Log: {log_path}", flush=True)


def resolve_existing_file(path):
    path = Path(path)
    output = path.with_name(path.stem + "_editor" + path.suffix)
    cache = {}
    log_path = output.with_suffix(output.suffix + ".log")
    if path.suffix.lower() == ".md":
        text = path.read_text(encoding="utf-8")
        pattern = re.compile(r"https?://doi\.org/([^\s)]+)", re.I)
        dois = list(dict.fromkeys(m.group(1).rstrip(".,;") for m in pattern.finditer(text)))
        resolve_many_with_log(dois, cache, log_path)
        text = pattern.sub(lambda m: cache.get(m.group(1).rstrip(".,;"), m.group(0)), text)
        output.write_text(text, encoding="utf-8")
        print(f"Resolvidos {len(dois)} DOI; gravado: {output}", flush=True)
        return
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as src:
            reader = csv.DictReader(src)
            rows = list(reader)
            fields = list(reader.fieldnames or [])
        doi_col = next((c for c in fields if c.lower() in ("doi", "doi_original")), None)
        if not doi_col:
            sys.exit("CSV sem coluna DOI")
        url_col = next((c for c in fields if c.lower() in ("url_editor", "url")), None)
        if not url_col:
            url_col = "url_editor"
            fields.append(url_col)
        dois = list(dict.fromkeys(clean_doi(row.get(doi_col))
                                  for row in rows if clean_doi(row.get(doi_col))))
        resolve_many_with_log(dois, cache, log_path)
        for row in rows:
            doi = (row.get(doi_col) or "").strip().replace("https://doi.org/", "")
            if doi:
                row[doi_col] = doi
                row[url_col] = cache[doi]
                if "doi_original" in row:
                    row["doi_original"] = "https://doi.org/" + doi
        with output.open("w", encoding="utf-8-sig", newline="") as dst:
            writer = csv.DictWriter(dst, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"Resolvidos {len(cache)} DOI; gravado: {output}", flush=True)
        return
    sys.exit("--resolve-file aceita ficheiros .md ou .csv")


def resolve_record_urls(records):
    cache = {}
    for rec in records:
        doi = rec.get("doi") or ""
        if doi:
            if doi not in cache:
                cache[doi] = resolve_doi_url(doi)
                time.sleep(0.15)
            rec["doi_url"] = "https://doi.org/" + doi
            rec["url"] = cache[doi]
    return records


def from_openalex(w, site):
    src = ((w.get("primary_location") or {}).get("source") or {})
    doi = clean_doi(w.get("doi"))
    return {
        "title": " ".join((w.get("display_name") or "(sem título)").split()),
        "year": w.get("publication_year"), "venue": src.get("display_name") or "",
        "cited": w.get("cited_by_count"), "doi": doi,
        "url": (((w.get("primary_location") or {}).get("landing_page_url"))
                or (f"https://doi.org/{doi}" if doi else (w.get("id") or ""))),
        "abstract": abstract_text(w.get("abstract_inverted_index")), "type": w.get("type") or "",
        "site": site, "origin": "openalex",
    }


def openalex_search(query, prefix, d0, d1, max_results, key, mailto, site):
    params = {
        "search": query,
        "filter": f"doi_starts_with:{prefix},from_publication_date:{d0},to_publication_date:{d1},type:!paratext",
        "per_page": 100, "cursor": "*",
        "select": "id,doi,display_name,publication_year,cited_by_count,primary_location,type,abstract_inverted_index",
    }
    if key:
        params["api_key"] = key
    if mailto:
        params["mailto"] = mailto
    limit = HARD_CAP if max_results == 0 else max_results
    out, total, page = [], None, 0
    while len(out) < limit:
        data = get_json(OPENALEX_URL, params)
        meta = data.get("meta", {})
        total = meta.get("count", total)
        results = data.get("results", [])
        page += 1
        if page % 5 == 1 or not results:
            print(f"   página {page}: {len(out) + len(results)} recuperados (total na fonte: {total})")
        if not results:
            break
        out += [from_openalex(w, site) for w in results]
        cursor = meta.get("next_cursor")
        if not cursor:
            break
        params["cursor"] = cursor
        time.sleep(0.2)
    return out[:limit], total


def run_openalex(args, queries, sites, d0, d1):
    key = args.api_key or os.environ.get("OPENALEX_API_KEY")
    if not key:
        print("[aviso] sem chave OpenAlex: quota diária muito pequena. Chave grátis: openalex.org/settings/api\n")
    collected = []
    for s in sites:
        for rq in queries:
            print(f"== {SITES[s]['label']} / {rq}")
            recs, total = openalex_search(queries[rq]["q"], SITES[s]["prefix"], d0, d1, args.max, key,
                                          args.mailto, s)
            collected.append({"site": s, "rq": rq, "total": total, "records": recs, "origin": "openalex"})
    return collected


# ----------------------------------------------------------------------------
# Importação de exportações nativas (RIS)
# ----------------------------------------------------------------------------
def parse_ris(path, site):
    text = Path(path).read_text(encoding="utf-8-sig", errors="replace")
    recs, cur = [], {}
    for line in text.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])\s{2}-\s?(.*)$", line)
        if not m:
            continue
        tag, val = m.group(1), m.group(2).strip()
        if tag == "TY":
            cur = {"title": "", "year": None, "venue": "", "cited": None, "doi": "", "url": "", "abstract": "",
                   "type": "", "site": site, "origin": "export"}
        elif tag == "ER":
            if cur.get("title"):
                recs.append(cur)
            cur = {}
        elif not cur and tag != "TY":
            continue
        elif tag in ("TI", "T1") and not cur["title"]:
            cur["title"] = " ".join(val.split())
        elif tag in ("PY", "Y1", "DA") and cur["year"] is None:
            ym = re.search(r"\d{4}", val)
            cur["year"] = int(ym.group(0)) if ym else None
        elif tag in ("JO", "JF", "T2", "BT", "JA") and not cur["venue"]:
            cur["venue"] = val
        elif tag == "DO":
            cur["doi"] = val.replace("https://doi.org/", "")
        elif tag in ("AB", "N2"):
            cur["abstract"] = val
        elif tag == "UR" and not cur["url"]:
            cur["url"] = val
    for r in recs:
        if not r["url"] and r["doi"]:
            r["url"] = "https://doi.org/" + r["doi"]
    return recs


def run_imports(args, d0, d1):
    collected = []
    y0, y1 = int(d0[:4]), int(d1[:4])
    for spec in args.imports or []:
        path, _, site = spec.rpartition(":") if ":" in spec and spec.rsplit(":", 1)[1] in SITES else (spec, "", "")
        if not site:
            sys.exit(f"--import precisa de ficheiro:site, ex.: ieee.ris:ieee (sites: {list(SITES)})")
        recs = parse_ris(path, site)
        kept = [r for r in recs if r["year"] is None or y0 <= r["year"] <= y1]
        print(f"== import {path} ({SITES[site]['label']}): {len(recs)} registos, {len(kept)} dentro de {y0}-{y1}")
        collected.append({"site": site, "rq": f"export:{Path(path).name}", "total": len(recs), "records": kept,
                          "origin": "export"})
    return collected


# ----------------------------------------------------------------------------
# Browser (opcional; ver v1 para os avisos)
# ----------------------------------------------------------------------------
LINK_PATTERNS = {
    "sciencedirect": re.compile(r"/science/article/(?:abs/)?(?:pii/)?([A-Z0-9]+)", re.I),
    "ieee": re.compile(r"/document/(\d+)"),
    "acm": re.compile(r"dl\.acm\.org/doi/(?:abs/|full/|epdf/|pdf/)?(10\.\d{4,9}/[^\s?#]+)"),
}
RESULT_SELECTORS = {
    "sciencedirect": 'a[href*="/science/article/"]',
    "ieee": 'a[href*="/document/"]',
    "acm": 'a[href*="/doi/10."]',
}
HOMES = {"sciencedirect": "https://www.sciencedirect.com/", "ieee": "https://ieeexplore.ieee.org/",
         "acm": "https://dl.acm.org/"}
BLOCK_HINTS = ("just a moment", "access denied", "captcha", "unusual traffic", "verify you are human",
               "are you a robot", "request blocked")


def build_url(site, query, page_no, y0, y1):
    if site == "sciencedirect":
        return "https://www.sciencedirect.com/search?" + urllib.parse.urlencode({
            "qs": f"TITLE-ABS-KEY({query})", "years": ",".join(str(y) for y in range(y0, y1 + 1)),
            "show": 100, "offset": (page_no - 1) * 100}, quote_via=urllib.parse.quote)
    if site == "ieee":
        return "https://ieeexplore.ieee.org/search/searchresult.jsp?" + urllib.parse.urlencode({
            "queryText": query, "highlight": "true", "returnFacets": "ALL", "returnType": "SEARCH",
            "matchPubs": "true", "ranges": f"{y0}_{y1}_Year", "rowsPerPage": 100, "pageNumber": page_no},
            quote_via=urllib.parse.quote)
    return "https://dl.acm.org/action/doSearch?" + urllib.parse.urlencode({
        "AllField": query, "AfterYear": y0, "BeforeYear": y1, "pageSize": 50, "startPage": page_no - 1},
        quote_via=urllib.parse.quote)


def extract_links(pairs, site):
    found = {}
    for href, text in pairs:
        m = LINK_PATTERNS[site].search(href)
        if not m:
            continue
        title = " ".join((text or "").split())
        if len(title) < 15:
            continue
        key = m.group(1)
        if key not in found or len(title) > len(found[key][1]):
            found[key] = (href, title)
    return list(found.values())


def extract_result_total(text):
    """Tenta ler o total mostrado na página de resultados; devolve None se não o encontrar."""
    text = text.replace("\u00a0", " ")
    patterns = (
        r"(?i)(?:showing\s+)?[\d,.\s]+\s*[-–]\s*[\d,.\s]+\s+(?:of|de)\s+([\d,.\s]+)",
        r"(?i)([\d,\.]+)\s+(?:results|resultados)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            digits = re.sub(r"\D", "", match.group(1))
            if digits:
                return int(digits)
    return None


def run_browser(args, queries, sites, d0, d1):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Falta o Playwright: pip install playwright && playwright install chromium")
    y0, y1 = int(d0[:4]), int(d1[:4])
    limit = HARD_CAP if args.max == 0 else min(args.max, HARD_CAP)
    collected = []
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(str(Path(args.profile).resolve()), headless=False,
                                                   viewport={"width": 1280, "height": 900})
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        for s in sites:
            page.goto(HOMES[s], wait_until="domcontentloaded")
            input(f"\n[{SITES[s]['label']}] Faz login (se necessário), aceita cookies e prime Enter... ")
            for rq in queries:
                print(f"== {SITES[s]['label']} / {rq}")
                seen, records, total = {}, [], None
                for n in range(1, args.pages + 1):
                    if len(records) >= limit:
                        break
                    response = page.goto(build_url(s, queries[rq]["q"], n, y0, y1),
                                         wait_until="domcontentloaded")
                    try:
                        page.wait_for_selector(RESULT_SELECTORS[s], timeout=15000)
                    except Exception:
                        pass
                    page.wait_for_timeout(1500)
                    body = page.inner_text("body") if page.query_selector("body") else ""
                    head = page.title() + " " + body[:1200]
                    status = response.status if response else None
                    if total is None:
                        total = extract_result_total(body)
                    if any(h in head.lower() for h in BLOCK_HINTS):
                        input("   Possível captcha/bloqueio. Resolve no browser e prime Enter (Ctrl+C para parar)... ")
                    pairs = page.eval_on_selector_all(
                        "a[href]", "els => els.map(e => [e.href, (e.innerText || e.textContent || '').trim())]")
                    new = [(h, t) for h, t in extract_links(pairs, s) if h not in seen]
                    for h, t in new:
                        seen[h] = t
                        records.append({"title": t, "year": None, "venue": "", "cited": None, "doi": "", "url": h,
                                        "abstract": "", "type": "", "site": s, "origin": "browser"})
                    print(f"   página {n}: +{len(new)} títulos (total indicado: {total if total is not None else 'n/d'})")
                    if not new:
                        snippet = " ".join(body.split())[:350]
                        print(f"   Sem títulos extraídos. HTTP {status if status is not None else 'n/d'}; "
                              f"página: {page.title()}; URL: {page.url}")
                        if snippet:
                            print(f"   Conteúdo visível: {snippet}")
                        break
                    time.sleep(random.uniform(args.delay_min, args.delay_max))
                collected.append({"site": s, "rq": rq, "total": total, "records": records, "origin": "browser"})
        ctx.close()
    return collected

# ----------------------------------------------------------------------------
# Consolidação, triagem e saída
# ----------------------------------------------------------------------------
def consolidate(collected):
    """Devolve (registos únicos por site, funil por site)."""
    unique = {}  # (site, key) -> rec
    funnel = {}
    for c in collected:
        f = funnel.setdefault(c["site"], {"retrieved": 0, "per_rq": {}})
        f["retrieved"] += len(c["records"])
        f["per_rq"][c["rq"]] = {"total": c["total"], "retrieved": len(c["records"]), "origin": c["origin"]}
        for rec in c["records"]:
            k = (c["site"], rec_key(rec))
            if k in unique:
                unique[k]["rqs"].add(c["rq"])
                unique[k]["origins"].add(c["origin"])
                for fld in ("abstract", "venue", "doi", "doi_url", "year", "cited"):
                    if not unique[k].get(fld) and rec.get(fld):
                        unique[k][fld] = rec[fld]
            else:
                r = dict(rec)
                r["rqs"], r["origins"] = {c["rq"]}, {c["origin"]}
                unique[k] = r
    for rec in unique.values():
        classify(rec)
    for site, f in funnel.items():
        recs = [r for (s, _), r in unique.items() if s == site]
        f["unique"] = len(recs)
        f["duplicates"] = f["retrieved"] - len(recs)
        for cat in ("revisao", "fora_dominio", "candidato_A", "candidato_B", "triagem_manual"):
            f[cat] = sum(1 for r in recs if r["category"] == cat)
    return unique, funnel


def fmt_rec(i, r):
    meta = " · ".join(x for x in [str(r["year"]) if r["year"] else "", r["venue"],
                                  f"{r['cited']} citações" if r["cited"] is not None else ""] if x)
    tags = ",".join(sorted(r["rqs"]))
    src = "+".join(sorted(r["origins"]))
    line = f"{i}. [{r['title']}]({r['url']})" + (f" - {meta}" if meta else "") + f" `[{tags}]` `[{src}]`"
    return line


def write_markdown(path, args, queries, sites, unique, funnel, d0, d1):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    L = [f"# Resultados da pesquisa - {now}", "", "## Registo da pesquisa (para o protocolo)", ""]
    L += [f"- **Janela temporal:** {d0} a {d1}",
          f"- **Data de execução:** {now}",
          f"- **Limite por (site, query):** {'sem limite (até ' + str(HARD_CAP) + ')' if args.max == 0 else args.max}; "
          "ordenado por relevância (a regra de paragem é este limite)",
          "- **Fonte dos registos:**"]
    origins = sorted({o for r in unique.values() for o in r["origins"]})
    if "openalex" in origins:
        L.append("  - `openalex`: OpenAlex (API), filtrado pelo prefixo DOI do editor. **Estes registos NÃO foram obtidos "
                 "na pesquisa nativa de ScienceDirect, IEEE Xplore ou ACM DL** e não devem ser apresentados como tal "
                 "no protocolo nem no PRISMA.")
    if "export" in origins:
        L.append("  - `export`: exportação (RIS) feita pelo utilizador na pesquisa nativa do site.")
    if "browser" in origins:
        L.append("  - `browser`: pesquisa nativa percorrida no browser (só títulos; sem ano nem resumo).")
    L += ["- **Pré-triagem automática:** heurística por palavras-chave no título e resumo. Serve para ordenar e "
          "separar; a inclusão/exclusão final é manual. Revisões e trabalhos fora do domínio não são apagados, "
          "ficam listados à parte com o motivo.", "", "### Queries", ""]
    for k, v in queries.items():
        L += [f"**{k} - {v['title']}**", "", "```", v["q"], "```", ""]

    L += ["### Funil por fonte", "",
          "| Fonte | Recuperados (soma das queries) | Duplicados entre queries | Únicos | Revisões (à parte) | "
          "Fora do domínio | Candidatos A | Candidatos B | Triagem manual |", "|---|---|---|---|---|---|---|---|---|"]
    for s in sites:
        f = funnel.get(s)
        if f:
            L.append(f"| {SITES[s]['label']} | {f['retrieved']} | {f['duplicates']} | {f['unique']} | {f['revisao']} | "
                     f"{f['fora_dominio']} | {f['candidato_A']} | {f['candidato_B']} | {f['triagem_manual']} |")
    L += ["", "### Por query", "", "| Fonte | Query | Total na fonte | Recuperados |", "|---|---|---|---|"]
    for s in sites:
        for rq, v in funnel.get(s, {}).get("per_rq", {}).items():
            tot = v["total"] if v["total"] is not None else "n/d"
            L.append(f"| {SITES[s]['label']} | {rq} | {tot} | {v['retrieved']} |")
    L.append("")

    sections = [("triagem_manual", "Triagem manual (resumo não recolhido)"),
                ("candidato_A", "Candidatos A (educação + medicina/QA)"),
                ("candidato_B", "Candidatos B (um só eixo)"),
                ("revisao", "Revisões e surveys (à parte da síntese principal)"),
                ("fora_dominio", "Fora do domínio (pré-triagem automática)")]
    for s in sites:
        recs = [r for (site, _), r in unique.items() if site == s]
        if not recs:
            continue
        L += [f"## {SITES[s]['label']}", ""]
        for cat, title in sections:
            sel = sorted((r for r in recs if r["category"] == cat),
                         key=lambda r: (-len(r["rqs"]), -(r["cited"] or 0), r["title"]))
            L += [f"### {title} ({len(sel)})", ""]
            if cat in ("revisao", "fora_dominio") and not args.list_all:
                L.append("_Listados no CSV (--csv) ou com --list-all._")
                L.append("")
                continue
            for i, r in enumerate(sel, 1):
                L.append(fmt_rec(i, r))
                if args.abstracts and r["abstract"] and cat in ("candidato_A", "candidato_B"):
                    L.append(f"   > {r['abstract'][:600]}{'...' if len(r['abstract']) > 600 else ''}")
            L.append("")
    Path(path).write_text("\n".join(L), encoding="utf-8")


def write_csv(path, unique):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["site", "categoria", "motivo", "queries", "origem", "titulo", "ano", "venue", "citacoes", "doi",
                    "doi_original", "url_editor", "resumo"])
        for (_, _), r in unique.items():
            w.writerow([r["site"], r["category"], r["reason"], ";".join(sorted(r["rqs"])),
                        "+".join(sorted(r["origins"])), r["title"], r["year"], r["venue"], r["cited"], r["doi"],
                        r.get("doi_url", "https://doi.org/" + r["doi"] if r["doi"] else ""), r["url"], r["abstract"]])


def main():
    ap = argparse.ArgumentParser(description="Recolhe títulos, deduplica e pré-tria (Markdown + CSV)")
    ap.add_argument("--mode", choices=["openalex", "browser", "none"], default="browser",
                    help="browser = pesquisa nativa (padrão); openalex = API por prefixo DOI; none = só usa --import")
    ap.add_argument("--sites", default="sciencedirect,ieee,acm")
    ap.add_argument("--queries", default="RQ1,RQ2,RQ3", help="ex.: CTX,RQ1,RQ2,RQ3")
    ap.add_argument("--queries-file", help="JSON {chave: {title, q}} para substituir/acrescentar queries")
    ap.add_argument("--from-date", default="2021-10-27", help="AAAA-MM-DD (critério registado)")
    ap.add_argument("--to-date", default="2026-10-27", help="AAAA-MM-DD")
    ap.add_argument("--max", type=int, default=1000, help="máx. por (site, query); 0 = tudo (até 10 000)")
    ap.add_argument("--import", dest="imports", action="append", metavar="FICHEIRO.ris:site",
                    help="exportação RIS nativa; repetível. Ex.: ieee.ris:ieee")
    ap.add_argument("--abstracts", action="store_true", help="mostrar o resumo dos candidatos no .md")
    ap.add_argument("--list-all", action="store_true", help="listar também revisões e fora do domínio no .md")
    ap.add_argument("--api-key")
    ap.add_argument("--mailto")
    ap.add_argument("--pages", type=int, default=20, help="browser: máximo de páginas por (site, query); limitado também por --max")
    ap.add_argument("--delay-min", type=float, default=5.0)
    ap.add_argument("--delay-max", type=float, default=9.0)
    ap.add_argument("--profile", default="browser_profile")
    ap.add_argument("--out")
    ap.add_argument("--resolve-file", help="resolve os DOI de um .md/.csv existente e grava *_editor")
    ap.add_argument("--resolve-dois", action="store_true",
                    help="resolve os DOI para o URL final do editor antes de exportar (pode demorar)")
    ap.add_argument("--csv", action="store_true")
    args = ap.parse_args()
    if args.resolve_file:
        resolve_existing_file(args.resolve_file)
        return

    for d in (args.from_date, args.to_date):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            sys.exit("As datas têm de ser AAAA-MM-DD")
    queries = dict(QUERIES)
    if args.queries_file:
        queries.update(json.loads(Path(args.queries_file).read_text(encoding="utf-8")))
    wanted = [q.strip() for q in args.queries.split(",") if q.strip()]
    missing = [q for q in wanted if q not in queries]
    if missing:
        sys.exit(f"Queries desconhecidas: {missing}. Disponíveis: {list(queries)}")
    queries = {k: queries[k] for k in wanted}
    sites = [s.strip() for s in args.sites.split(",") if s.strip()]
    bad = [s for s in sites if s not in SITES]
    if bad:
        sys.exit(f"Sites desconhecidos: {bad}. Disponíveis: {list(SITES)}")

    collected = []
    if args.mode == "openalex":
        collected += run_openalex(args, queries, sites, args.from_date, args.to_date)
    elif args.mode == "browser":
        collected += run_browser(args, queries, sites, args.from_date, args.to_date)
    collected += run_imports(args, args.from_date, args.to_date)
    if not collected:
        sys.exit("Nada a fazer: usa --mode openalex/browser ou --import ficheiro.ris:site")
    sites = [s for s in SITES if any(c["site"] == s for c in collected)]

    if args.resolve_dois:
        flat_records = [rec for group in collected for rec in group["records"]]
        resolve_record_urls(flat_records)
    unique, funnel = consolidate(collected)
    out = Path(args.out or f"resultados_{datetime.now():%Y%m%d_%H%M}.md")
    write_markdown(out, args, queries, sites, unique, funnel, args.from_date, args.to_date)
    print(f"\nGravado: {out}")
    if args.csv:
        write_csv(out.with_suffix(".csv"), unique)
        print(f"Gravado: {out.with_suffix('.csv')}")
    for s in sites:
        f = funnel[s]
        print(f"{SITES[s]['label']}: {f['retrieved']} recuperados -> {f['unique']} únicos | revisões {f['revisao']} | "
              f"fora do domínio {f['fora_dominio']} | candidatos A/B {f['candidato_A']}/{f['candidato_B']}")


if __name__ == "__main__":
    main()