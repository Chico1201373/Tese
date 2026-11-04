#!/usr/bin/env python3
"""
indicadores.py - estatísticas descritivas dos estudos incluídos na revisão (Tabela tab:indicators).

Lê: selecionados.csv (metadados e resumos), elegibilidade.csv (decisão final)
Gera: exports/indicadores.md

Os indicadores contam termos no título e no resumo (não no texto integral), para que todos
os estudos sejam medidos da mesma forma. São indicadores de frequência, não de eficácia.

Uso:
  python3 indicadores.py
"""
import csv
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent

INDICADORES = [
    ("Origem do contexto (RQ1)", [
        ("RAG", r"retrieval[- ]augmented|\bRAG\b|retriev"),
        ("Grafo de conhecimento ou ontologia", r"knowledge graph|ontolog|graphrag|subgraph|triple"),
        ("Fine-tuning", r"fine[- ]?tun|\bLoRA\b|\bSFT\b"),
        ("Contexto no prompt, ICL ou engenharia de prompts", r"in[- ]context|prompt engineering|prompting|few[- ]shot|\bICL\b"),
    ]),
    ("Controlo do âmbito e aspetos operacionais (RQ1)", [
        ("Citações ou rastreabilidade das fontes", r"citation|cite|traceab|source attribution|audit"),
        ("Segurança (injeção, jailbreak, guardrails)", r"injection|jailbreak|guardrail|adversarial|malicious|safeguard"),
        ("Recusa, abstenção ou perguntas fora do âmbito", r"refus|abstain|abstention|out[- ]of[- ](scope|domain)|off[- ]topic|topic restriction"),
        ("Várias línguas ou língua diferente do inglês", r"multilingual|bilingual|trilingual|cross[- ]lingual|arabic|indonesian|italian|german|chinese|vietnamese|language-specific"),
        ("Latência ou tempo de resposta", r"latenc|response time|real[- ]time"),
        ("Custo", r"\bcost"),
    ]),
    ("Avaliação (RQ2)", [
        ("Exatidão (accuracy)", r"accura"),
        ("Métricas automáticas (fidelidade, RAGAS, ROUGE, BLEU, F1)", r"faithful|ragas|rouge|bleu|meteor|bertscore|\bF1\b|exact match"),
        ("Benchmark de escolha múltipla ou de exame", r"multiple[- ]choice|MCQ|MedQA|MedMCQA|USMLE|exam"),
        ("Especialistas, clínicos ou docentes", r"expert|clinician|physician|instructor|teaching assistant|\bTAs?\b|faculty|staff"),
        ("Estudo com utilizadores, questionário ou entrevistas", r"user study|survey(ed)? (of|with)|questionnaire|interview|participants|deploy"),
        ("LLM como juiz", r"llm[- ]as[- ]a[- ]judge|judge"),
    ]),
]


def main():
    eleg = {e["id"]: e for e in csv.DictReader(open(HERE / "elegibilidade.csv", encoding="utf-8-sig"))}
    sel = [s for s in csv.DictReader(open(HERE / "selecionados.csv", encoding="utf-8-sig"))
           if s["id"] in eleg and eleg[s["id"]]["decisao"] == "Incluir"]
    n = len(sel)
    q = Counter(v.split(":")[1] for s in sel for v in s["queries"].split(","))
    fonte = Counter(sorted({v.split(":")[0] for v in s["queries"].split(",")})[0] for s in sel)
    ano = Counter(s["ano"] for s in sel)
    tema = Counter(s["tema"] for s in sel)

    md = [f"# Indicadores dos {n} estudos incluídos", "",
          "Por pesquisa: " + ", ".join(f"{k} {v}" for k, v in sorted(q.items())),
          "Por fonte: " + ", ".join(f"{k} {v}" for k, v in fonte.most_common()),
          "Por ano: " + ", ".join(f"{k} {v}" for k, v in sorted(ano.items(), reverse=True)),
          "Por tema: " + ", ".join(f"{k} {v}" for k, v in tema.most_common()), "",
          "| Aspeto | N.º | % |", "|---|---:|---:|"]
    for grupo, linhas in INDICADORES:
        md.append(f"| *{grupo}* | | |")
        for nome, rx in linhas:
            c = sum(1 for s in sel if re.search(rx, s["titulo"] + " " + s["abstract"], re.I))
            md.append(f"| {nome} | {c} | {round(100 * c / n)} |")
    (HERE / "exports" / "indicadores.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
