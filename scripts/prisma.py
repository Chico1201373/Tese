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
    # fase B, critério I5 (proximidade ao caso): os incluídos em I1-I4 que não são prioritários são excluídos
    excl_i5 = len(incl) - prioridade
    # elegibilidade (texto integral) dos prioritários: elegibilidade.csv
    eleg = list(csv.DictReader(open(HERE / "elegibilidade.csv", encoding="utf-8-sig")))
    nao_obtidos = [e for e in eleg if e["texto_integral"] == "não"]
    avaliados = [e for e in eleg if e["texto_integral"] == "sim"]
    excl_i4 = [e for e in avaliados if e["decisao"] == "Excluir" and e["criterio"] == "I4"]
    excl_qa = [e for e in avaliados if e["decisao"] == "Excluir" and e["criterio"] == "QA"]
    incluidos = sum(1 for e in avaliados if e["decisao"] == "Incluir")
    assert len(eleg) == prioridade, (len(eleg), prioridade)

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
           f"- Excluídos na leitura: **{len(excl_lidos) + excl_i5}** " + ", ".join(f"{k}: {v}" for k, v in sorted(motivos_lidos.items()))
           + f", I5: {excl_i5}",
           f"- Textos integrais procurados: **{prioridade}**", "",
           "## Elegibilidade (texto integral)", "",
           f"- Não obtidos: **{len(nao_obtidos)}** " + ", ".join(e["id"] for e in nao_obtidos),
           f"- Avaliados: **{len(avaliados)}**",
           f"- Excluídos por I4: **{len(excl_i4)}** " + ", ".join(e["id"] for e in excl_i4),
           f"- Excluídos pela qualidade (< 3,5): **{len(excl_qa)}** " + ", ".join(e["id"] for e in excl_qa),
           f"- Estudos incluídos na revisão: **{incluidos}**", ""]
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
\node[side, anchor=north west] (auto) at ([xshift=0.8cm]scr.north east) {{Excluídos por regras ($n={len(auto)}$):\\
  fora de educação/saúde ($n={m['fora do foco (nem educação nem saúde)']}$)\\
  revisão ou survey, E4 ($n={m['revisão ou survey']}$)\\
  não é chatbot/QA ($n={m['não é chatbot, sistema conversacional ou QA']}$)\\
  sem avaliação das respostas ($n={m['sem avaliação das respostas descrita no resumo']}$)\\
  não usa LLM ($n={m['não usa LLM']}$)\\
  sem resumo ou não é artigo, E2 ($n={m['sem resumo ou não é artigo']}$)}};
\node[box, anchor=north west] (man) at ([yshift=-0.6cm]scr.south west |- auto.south) {{Registos lidos manualmente ($n={len(lidos)}$)}};
\node[side, anchor=west] (exm) at ([xshift=0.8cm]man.east) {{Excluídos na leitura ($n={len(excl_lidos) + excl_i5}$):\\
  E3 ($n={motivos_lidos.get('E3', 0)}$), E2 ($n={motivos_lidos.get('E2', 0)}$), E4 ($n={motivos_lidos.get('E4', 0)}$)\\
  I5, sem proximidade ao caso ($n={excl_i5}$)}};
\node[box, anchor=north west] (ret) at ([yshift=-0.9cm]man.south west) {{Textos integrais procurados ($n={prioridade}$)}};
\node[side, anchor=west] (nr) at ([xshift=0.8cm]ret.east) {{Textos integrais não obtidos ($n={len(nao_obtidos)}$)}};
\node[box, anchor=north west] (ele) at ([yshift=-1.0cm]ret.south west) {{Textos integrais avaliados ($n={len(avaliados)}$)}};
\node[side, anchor=west] (exe) at ([xshift=0.8cm]ele.east) {{Excluídos no texto integral ($n={len(excl_i4) + len(excl_qa)}$):\\
  I4, sem avaliação das respostas ($n={len(excl_i4)}$)\\
  qualidade abaixo de 3,5/5 ($n={len(excl_qa)}$)}};
\node[box, anchor=north west] (inc) at ([yshift=-1.5cm]ele.south west) {{Estudos incluídos na revisão ($n={incluidos}$)}};
\draw[arr] (id) -- (scr); \draw[arr] (id.east) -- (dup.west);
\draw[arr] (scr) -- (man); \draw[arr] (scr.east) -- (scr.east -| auto.west);
\draw[arr] (man) -- (ret); \draw[arr] (man.east) -- (exm.west);
\draw[arr] (ret) -- (ele); \draw[arr] (ret.east) -- (nr.west);
\draw[arr] (ele) -- (inc); \draw[arr] (ele.east) -- (exe.west);
\node[stage] at ([xshift=-0.15cm]id.west) {{Identificação}};
\node[stage] at ([xshift=-0.15cm]man.west) {{Triagem}};
\node[stage] at ($(ret.west)!0.5!(ele.west)+(-0.15cm,0)$) {{Elegibilidade}};
\node[stage] at ([xshift=-0.15cm]inc.west) {{Incluídos}};
\end{{tikzpicture}}
"""
    TEX.parent.mkdir(parents=True, exist_ok=True)
    TEX.write_text(tex, encoding="utf-8")
    print(f"Figura: {TEX.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
