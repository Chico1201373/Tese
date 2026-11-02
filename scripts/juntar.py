#!/usr/bin/env python3
"""
juntar.py - lê os exports (RIS/BibTeX) de exports/<fonte>/<Q>/, junta-os e remove duplicados.

Deduplicação: primeiro DOI normalizado, depois título normalizado. Cada registo
guarda a(s) fonte(s) e a(s) query(s) onde apareceu.

Uso:
  python3 juntar.py

Gera:
  registos.csv       um registo único por linha (com resumo), pronto para a triagem
  exports/funil.md   contagens por fonte e query, duplicados e únicos (para o PRISMA)
"""
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
EXPORTS = HERE / "exports"
ORDEM_FONTES = ["ieee", "acm", "sciencedirect"]
NOMES = {"ieee": "IEEE Xplore", "acm": "ACM Digital Library", "sciencedirect": "ScienceDirect"}


def ler_ris(texto):
    registos, atual = [], defaultdict(list)
    for linha in texto.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9])  - ?(.*)$", linha)
        if not m:
            continue
        tag, valor = m.groups()
        if tag == "ER":
            registos.append(atual)
            atual = defaultdict(list)
        else:
            atual[tag].append(valor.strip())
    out = []
    for r in registos:
        out.append({
            "titulo": (r.get("TI") or r.get("T1") or [""])[0],
            "autores": "; ".join(r.get("AU", []) + r.get("A1", [])),
            "ano": (r.get("PY") or r.get("Y1") or [""])[0][:4],
            "venue": (r.get("T2") or r.get("JO") or r.get("JF") or [""])[0],
            "doi": (r.get("DO") or [""])[0],
            "tipo": (r.get("TY") or [""])[0],
            "abstract": " ".join(r.get("AB", [])),
            "keywords": "; ".join(r.get("KW", [])),
        })
    return out


def campo_bib(entrada, nome):
    m = re.search(rf"\b{nome}\s*=\s*\{{", entrada, re.I)
    if not m:
        return ""
    i, nivel = m.end(), 1
    for j in range(i, len(entrada)):
        if entrada[j] == "{":
            nivel += 1
        elif entrada[j] == "}":
            nivel -= 1
            if not nivel:
                return " ".join(entrada[i:j].replace("{", "").replace("}", "").split())
    return ""


def ler_bib(texto):
    out = []
    for entrada in re.split(r"\n(?=@\w+\{)", "\n" + texto):
        m = re.match(r"\s*@(\w+)\{", entrada)
        if not m:
            continue
        out.append({
            "titulo": campo_bib(entrada, "title"),
            "autores": campo_bib(entrada, "author").replace(" and ", "; "),
            "ano": campo_bib(entrada, "year"),
            "venue": campo_bib(entrada, "booktitle") or campo_bib(entrada, "journal"),
            "doi": campo_bib(entrada, "doi"),
            "tipo": m.group(1).lower(),
            "abstract": campo_bib(entrada, "abstract"),
            "keywords": campo_bib(entrada, "keywords"),
        })
    return out


def norm_doi(doi):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip().lower())


def norm_titulo(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def main():
    brutos = []
    for fonte in ORDEM_FONTES:
        for f in sorted((EXPORTS / fonte).glob("Q*/*")):
            texto = f.read_text(encoding="utf-8", errors="ignore")
            regs = ler_ris(texto) if f.suffix == ".ris" else ler_bib(texto) if f.suffix == ".bib" else []
            for r in regs:
                brutos.append({**r, "fonte": fonte, "query": f.parent.name, "ficheiro": f.name})

    por_fonte_query = Counter((r["fonte"], r["query"]) for r in brutos)

    # 1) duplicados dentro da mesma fonte (entre queries); 2) entre fontes
    unicos, chave_de = {}, {}
    dup_intra, dup_inter = Counter(), Counter()
    for r in brutos:
        chaves = [k for k in (("doi", norm_doi(r["doi"])), ("tit", norm_titulo(r["titulo"]))) if k[1]]
        existente = next((chave_de[k] for k in chaves if k in chave_de), None)
        if existente is None:
            uid = len(unicos) + 1
            unicos[uid] = {**r, "fontes": [r["fonte"]], "queries": [f"{r['fonte']}:{r['query']}"]}
            for k in chaves:
                chave_de[k] = uid
            continue
        u = unicos[existente]
        if r["fonte"] in u["fontes"]:
            dup_intra[r["fonte"]] += 1
        else:
            dup_inter[r["fonte"]] += 1
            u["fontes"].append(r["fonte"])
        if f"{r['fonte']}:{r['query']}" not in u["queries"]:
            u["queries"].append(f"{r['fonte']}:{r['query']}")
        for campo in ("abstract", "doi", "keywords", "venue", "ano"):
            if not u[campo] and r[campo]:
                u[campo] = r[campo]
        for k in chaves:
            chave_de.setdefault(k, existente)

    campos = ["id", "fontes", "queries", "titulo", "autores", "ano", "venue", "tipo", "doi", "keywords", "abstract"]
    with open(HERE / "registos.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for uid, u in unicos.items():
            w.writerow({"id": f"R{uid:04d}", "fontes": ",".join(u["fontes"]), "queries": ",".join(u["queries"]),
                        **{c: u[c] for c in campos if c in u and c not in ("id", "fontes", "queries")}})

    linhas = ["# Funil de identificação", "", "| Fonte | Q1 | Q2 | Q3 | Q4 | Total exportado |", "|---|---:|---:|---:|---:|---:|"]
    for fonte in ORDEM_FONTES:
        qs = [por_fonte_query.get((fonte, q), 0) for q in ("Q1", "Q2", "Q3", "Q4")]
        linhas.append(f"| {NOMES[fonte]} | " + " | ".join(map(str, qs)) + f" | {sum(qs)} |")
    sem_abs = sum(1 for u in unicos.values() if not u["abstract"])
    linhas += ["", f"- Registos exportados: **{len(brutos)}**",
               f"- Duplicados entre queries da mesma fonte: **{sum(dup_intra.values())}** " + str(dict(dup_intra)),
               f"- Duplicados entre fontes: **{sum(dup_inter.values())}** " + str(dict(dup_inter)),
               f"- Registos únicos para triagem: **{len(unicos)}** (sem resumo: {sem_abs})"]
    (EXPORTS / "funil.md").write_text("\n".join(linhas), encoding="utf-8")
    print("\n".join(linhas))


if __name__ == "__main__":
    main()
