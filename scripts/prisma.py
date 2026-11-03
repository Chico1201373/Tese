#!/usr/bin/env python3
"""
prisma.py - calcula os números do fluxo PRISMA 2020 a partir dos ficheiros da revisão
e gera o diagrama em TikZ para a tese.

Lê: exports/registo_pesquisa.json, exports/funil.md (via juntar.py), triagem.csv
Gera:
  exports/prisma.md                                   números e explicação
  ../tmdei-dissertation-template-main/ch2/assets/prisma.tex   figura TikZ

Uso:
  python3 prisma.py
"""
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
TEX = HERE.parent / "tmdei-dissertation-template-main" / "ch2" / "assets" / "prisma.tex"
FONTES = [("ieee", "IEEE Xplore"), ("acm", "ACM DL"), ("sciencedirect", "Scopus")]


def main():
    registo = json.loads((HERE / "exports" / "registo_pesquisa.json").read_text(encoding="utf-8"))
    total_fonte = {f: sum(v["total"] for k, v in registo.items() if k.startswith(f + "/")) for f, _ in FONTES}
    exportados = {f: sum(v.get("exportados") or 0 for k, v in registo.items() if k.startswith(f + "/")) for f, _ in FONTES}
    identificados = sum(exportados.values())

    triagem = list(csv.DictReader(open(HERE / "triagem.csv", encoding="utf-8-sig")))
    unicos = len(triagem)
    duplicados = identificados - unicos
    auto = [t for t in triagem if t["fase"] == "A"]
    lidos = [t for t in triagem if t["fase"] == "B"]
    excl_lidos = [t for t in lidos if t["decisao"] == "Excluir"]
    incl = [t for t in lidos if t["decisao"] == "Incluir"]
    motivos_auto = Counter(t["motivo"] for t in auto)
    motivos_lidos = Counter(f"{t['criterio']}" for t in excl_lidos)
    # a prioridade está em selecionados.csv (triagem.csv não guarda a coluna)
    sel = list(csv.DictReader(open(HERE / "selecionados.csv", encoding="utf-8-sig")))
    prioridade = sum(1 for s in sel if s["prioridade"].startswith("alta"))
    # elegibilidade (texto integral) dos prioritários: elegibilidade.csv
    eleg = list(csv.DictReader(open(HERE / "elegibilidade.csv", encoding="utf-8-sig")))
    nao_obtidos = [e for e in eleg if e["texto_integral"] == "não"]
    avaliados = [e for e in eleg if e["texto_integral"] == "sim"]
    excl_integral = [e for e in avaliados if e["decisao"] == "Excluir"]
    incl_integral = len(avaliados) - len(excl_integral)
    incluidos = len(incl) - len(excl_integral)
    restantes = len(incl) - len(eleg)

    md = ["# Números PRISMA 2020", "",
          "## Identificação", "",
          "| Fonte | Total indicado pela fonte | Registos exportados |", "|---|---:|---:|"]
    md += [f"| {nome} | {total_fonte[f]} | {exportados[f]} |" for f, nome in FONTES]
    md += [f"| **Total** | **{sum(total_fonte.values())}** | **{identificados}** |", "",
           f"- Duplicados removidos: **{duplicados}**",
           f"- Registos únicos: **{unicos}**", "",
           "## Triagem (título e resumo)", "",
           f"- Excluídos por regras automáticas (fase A): **{len(auto)}**"]
    md += [f"  - {m}: {n}" for m, n in motivos_auto.most_common()]
    md += [f"- Lidos manualmente (fase B): **{len(lidos)}**",
           f"- Excluídos na leitura: **{len(excl_lidos)}** " + ", ".join(f"{k}: {v}" for k, v in sorted(motivos_lidos.items())),
           f"- Incluídos para leitura integral: **{len(incl)}** (prioridade alta: {prioridade})", "",
           "## Elegibilidade (texto integral, estudos prioritários)", "",
           f"- Textos integrais procurados: **{len(eleg)}**; não obtidos: **{len(nao_obtidos)}** (mantidos pelo resumo)",
           f"- Avaliados: **{len(avaliados)}**; excluídos: **{len(excl_integral)}** "
           + ", ".join(f"{e['id']} ({e['criterio']})" for e in excl_integral),
           f"- Estudos incluídos na revisão: **{incluidos}** (prioritários {len(eleg) - len(excl_integral)}: "
           f"{incl_integral} com texto integral e {len(nao_obtidos)} só com resumo; restantes {restantes} por título e resumo)", ""]
    (HERE / "exports" / "prisma.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))

    m = motivos_auto
    tex = rf"""% Gerado por scripts/prisma.py -- não editar à mão
\begin{{tikzpicture}}[
  box/.style={{draw, rectangle, align=left, text width=6.2cm, font=\scriptsize, inner sep=4pt}},
  side/.style={{draw, rectangle, align=left, text width=5.6cm, font=\scriptsize, inner sep=4pt}},
  stage/.style={{font=\scriptsize\bfseries, rotate=90, anchor=south}},
  arr/.style={{-{{Stealth[length=2mm]}}}}]
\node[box, anchor=north west] (id) at (0,0) {{Registos identificados nas bases ($n={identificados}$)\\
  IEEE Xplore ($n={exportados['ieee']}$)\\ ACM DL ($n={exportados['acm']}$)\\ Scopus ($n={exportados['sciencedirect']}$)}};
\node[side, anchor=west] (dup) at ([xshift=0.8cm]id.east) {{Registos removidos antes da triagem:\\ duplicados ($n={duplicados}$)}};
\node[box, anchor=north west] (scr) at ([yshift=-0.7cm]id.south west) {{Registos triados por título e resumo ($n={unicos}$)}};
\node[side, anchor=north west] (auto) at ([xshift=0.8cm]scr.north east) {{Excluídos por regras automáticas ($n={len(auto)}$):\\
  fora de educação/saúde ($n={m['fora do foco (nem educação nem saúde)']}$)\\
  revisão ou survey, E4 ($n={m['revisão ou survey']}$)\\
  não é chatbot/QA ($n={m['não é chatbot, sistema conversacional ou QA']}$)\\
  sem avaliação das respostas ($n={m['sem avaliação das respostas descrita no resumo']}$)\\
  não usa LLM ($n={m['não usa LLM']}$)\\
  sem resumo ou não é artigo, E2 ($n={m['sem resumo ou não é artigo']}$)}};
\node[box, anchor=north west] (man) at ([yshift=-0.6cm]scr.south west |- auto.south) {{Registos lidos manualmente ($n={len(lidos)}$)}};
\node[side, anchor=west] (exm) at ([xshift=0.8cm]man.east) {{Excluídos na leitura ($n={len(excl_lidos)}$):\\
  E3 ($n={motivos_lidos.get('E3', 0)}$), E2 ($n={motivos_lidos.get('E2', 0)}$), E4 ($n={motivos_lidos.get('E4', 0)}$)}};
\node[box, anchor=north west] (ret) at ([yshift=-0.9cm]man.south west) {{Incluídos na triagem ($n={len(incl)}$)\\
  textos integrais procurados (prioritários) ($n={len(eleg)}$)}};
\node[side, anchor=west] (nr) at ([xshift=0.8cm]ret.east) {{Textos integrais não obtidos ($n={len(nao_obtidos)}$):\\
  mantidos com base no resumo}};
\node[box, anchor=north west] (ele) at ([yshift=-0.7cm]ret.south west) {{Textos integrais avaliados ($n={len(avaliados)}$)}};
\node[side, anchor=west] (exe) at ([xshift=0.8cm]ele.east) {{Excluídos no texto integral ($n={len(excl_integral)}$):\\
  I4, sem avaliação das respostas}};
\node[box, anchor=north west] (inc) at ([yshift=-0.7cm]ele.south west) {{Estudos incluídos na revisão ($n={incluidos}$)\\
  prioritários: texto integral ($n={incl_integral}$), só resumo ($n={len(nao_obtidos)}$)\\
  restantes, por título e resumo ($n={restantes}$)}};
\draw[arr] (id) -- (scr); \draw[arr] (id.east) -- (dup.west);
\draw[arr] (scr) -- (man); \draw[arr] (scr.east) -- (scr.east -| auto.west);
\draw[arr] (man) -- (ret); \draw[arr] (man.east) -- (exm.west);
\draw[arr] (ret) -- (ele); \draw[arr] (ret.east) -- (nr.west);
\draw[arr] (ele) -- (inc); \draw[arr] (ele.east) -- (exe.west);
\node[stage] at ([xshift=-0.15cm]id.west) {{Identificação}};
\node[stage] at ([xshift=-0.15cm]man.west) {{Triagem}};
\node[stage] at ([xshift=-0.15cm]ele.west) {{Elegibilidade}};
\node[stage] at ([xshift=-0.15cm]inc.west) {{Incluídos}};
\end{{tikzpicture}}
"""
    TEX.parent.mkdir(parents=True, exist_ok=True)
    TEX.write_text(tex, encoding="utf-8")
    print(f"Figura: {TEX.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
