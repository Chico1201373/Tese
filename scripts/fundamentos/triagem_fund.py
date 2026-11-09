#!/usr/bin/env python3
"""
triagem_fund.py - triagem da pesquisa de enquadramento (fundamentos sobre LLM, IEEE Xplore).

Fase A (regras objetivas sobre o título, reprodutíveis):
  F1  tipo de registo que não é estudo (prefácio, índice, editorial, programa)
  F2  o título não trata o tema da query de onde o registo veio:
        Q1  survey/overview/review (ou "tutorial") de LLM em geral
        Q2  LLM avaliado em exame médico (exam, USMLE, MedQA, licensing, board)
        Q3  adaptação eficiente: LoRA, PEFT, parameter-efficient, quantização
  F3  survey de uma aplicação específica (Q1): o título refere um domínio de aplicação
Fase B (leitura do título e resumo): decisões em decisoes_fund.csv (id, decisao, motivo).

Gera: triagem_fund.csv (todos) e candidatos_fund.csv (passaram a fase A).
"""
import csv
import re
from pathlib import Path

HERE = Path(__file__).parent
NAO_ESTUDO = re.compile(r"^(front matter|table of contents|preface|editorial|message from|welcome|program|"
                        r"author index|committee|keynote|cover)", re.I)
TEMA = {
    "Q1": re.compile(r"\b(survey|overview|review|tutorial|taxonomy|landscape)\b", re.I),
    "Q2": re.compile(r"\b(exam|exams|examination|usmle|medqa|licens\w*|board)\b", re.I),
    "Q3": re.compile(r"\b(lora|qlora|peft|parameter[- ]efficient|quantiz\w*|low[- ]rank|fine[- ]tun\w*)\b", re.I),
}
LLM = re.compile(r"\b(large language models?|llms?|gpt|chatgpt|foundation models?|language models?)\b", re.I)
# Q1: surveys sobre UMA aplicação (educação, código, finanças, ...) não servem para os fundamentos gerais
APLICACAO = re.compile(r"\b(education\w*|code|software|financ\w*|legal|law|agricult\w*|robot\w*|"
                       r"recommend\w*|cyber\w*|security|medical|medicine|health\w*|clinical|biomedic\w*|"
                       r"chemistry|materials?|manufactur\w*|power|energy|vehic\w*|autonomous|"
                       r"telecom\w*|network\w*|6g|5g|iot|edge|remote sensing|geo\w*|music|game\w*|"
                       r"tabular|graph|time series|vision|multimodal|speech|translation|sentiment)\b", re.I)


def main():
    regs = list(csv.DictReader(open(HERE / "registos.csv", encoding="utf-8-sig")))
    out, cand = [], []
    for r in regs:
        t = r["titulo"]
        qs = re.findall(r"Q\d", r["queries"])
        motivo = ""
        if NAO_ESTUDO.match(t.strip()):
            motivo = "F1 não é estudo"
        elif not LLM.search(t + " " + r["abstract"][:400]):
            motivo = "F2 não trata LLM"
        elif not any(TEMA[q.strip()].search(t) for q in qs if q.strip() in TEMA):
            motivo = "F2 título fora do tema da query"
        elif qs == ["Q1"] and APLICACAO.search(t):
            motivo = "F3 survey de uma aplicação específica"
        r = {**r, "fase_a": "excluir" if motivo else "passa", "motivo_a": motivo}
        out.append(r)
        if not motivo:
            cand.append(r)
    campos = list(out[0].keys())
    for nome, linhas in (("triagem_fund.csv", out), ("candidatos_fund.csv", cand)):
        with open(HERE / nome, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=campos)
            w.writeheader()
            w.writerows(linhas)
    from collections import Counter
    print("Fase A:", Counter(r["motivo_a"] or "passa" for r in out))
    print("Candidatos por query:", Counter(q for r in cand for q in re.findall(r"Q\d", r["queries"])))


if __name__ == "__main__":
    main()
