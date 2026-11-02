#!/usr/bin/env python3
"""
triagem.py - triagem por título e resumo dos registos únicos (registos.csv).

Fase A (regras objetivas, reprodutíveis):
  E2  sem resumo ou registo que não é artigo (número completo, livro de resumos, livro)
  E4  revisão / survey
  E3  não usa LLM, ou não é chatbot / sistema conversacional / QA
  E3  fora do foco: nem educação nem saúde (I3)
  E3  o resumo não descreve avaliação das respostas (I4)
Fase B (leitura do título e resumo): decisões em decisoes_manuais.csv
  (id, decisao, criterio, motivo, tema). Registos ainda sem decisão ficam "por ler".

Uso:
  python3 triagem.py              # aplica as fases e grava triagem.csv + selecionados.csv
  python3 triagem.py --listar     # mostra os registos por ler (para a fase B)

Gera:
  triagem.csv       todos os registos com fase, decisão, critério e motivo
  selecionados.csv  só os incluídos, com a query (RQ) a que respondem
"""
import argparse
import csv
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent

REV = (r"\b(systematic (literature )?review|literature review|scoping review|survey|overview|bibliometric|"
       r"mapping study|meta-analysis|narrative review|umbrella review|a review|review of)\b")
REV_ABS = r"\b(this|we|our) (systematic |scoping |literature )?(review|survey)\b|\b(systematic|scoping) review\b"
LLM = (r"\b(llms?|large language models?|gpt[-\w.]*|chatgpt|llama[-\w.]*|gemini|claude|mistral|qwen|deepseek|"
       r"generative ai|genai|foundation models?)\b")
CONV = (r"\b(chat ?bots?|conversational|dialog(ue)?s?|assistants?|question[- ]answering|qa|q&a|tutor(ing|s)?|"
        r"virtual agents?)\b")
DOM = (r"\b(educat\w*|students?|learn(ing|ers?)\b(?! rate)|teach\w*|course\w*|universit\w*|campus|tutor\w*|"
       r"exam\w*|medic\w*|clinic\w*|health\w*|patients?|nurs\w*|hospital|physician\w*|doctors?|biomedic\w*|pharma\w*)")
EVAL = (r"\b(faithful\w*|hallucinat\w*|factual\w*|correctness|accura\w*|groundedness|grounded|"
        r"out[- ]of[- ](scope|domain)|abstain|abstention|refus\w*|guardrails?|prompt injection|jailbreak\w*|ragas|"
        r"llm[- ]as[- ]a[- ]judge|expert evaluat\w*|human evaluat\w*|user stud\w*)")
SEM_ARTIGO = r"^(full issue|pdf of|.*\babstracts\b|informatics$)"


def fase_a(x):
    t, a = x["titulo"], x["abstract"]
    ta = f"{t} {a}"
    if not a or re.search(SEM_ARTIGO, t, re.I) or x["tipo"] == "BOOK":
        return "E2", "sem resumo ou não é artigo"
    if re.search(REV, t, re.I) or re.search(REV_ABS, a[:600], re.I):
        return "E4", "revisão ou survey"
    if not re.search(LLM, ta, re.I):
        return "E3", "não usa LLM"
    if not re.search(CONV, ta, re.I):
        return "E3", "não é chatbot, sistema conversacional ou QA"
    if not re.search(DOM, ta, re.I):
        return "E3", "fora do foco (nem educação nem saúde)"
    if not re.search(EVAL, ta, re.I):
        return "E3", "sem avaliação das respostas descrita no resumo"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--de", type=int, default=0)
    ap.add_argument("--ate", type=int, default=10**6)
    args = ap.parse_args()

    registos = list(csv.DictReader(open(HERE / "registos.csv", encoding="utf-8-sig")))
    manual = {}
    if (HERE / "decisoes_manuais.csv").exists():
        manual = {d["id"]: d for d in csv.DictReader(open(HERE / "decisoes_manuais.csv", encoding="utf-8-sig"))}

    linhas, por_ler = [], []
    for x in registos:
        a = fase_a(x)
        if a:
            linhas.append({**x, "fase": "A", "decisao": "Excluir", "criterio": a[0], "motivo": a[1], "tema": ""})
        elif x["id"] in manual:
            d = manual[x["id"]]
            linhas.append({**x, "fase": "B", "decisao": d["decisao"], "criterio": d["criterio"],
                           "motivo": d["motivo"], "tema": d.get("tema", ""), "prioridade": d.get("prioridade", "")})
        else:
            linhas.append({**x, "fase": "B", "decisao": "por ler", "criterio": "", "motivo": "", "tema": ""})
            por_ler.append(x)

    if args.listar:
        for i, x in enumerate(por_ler):
            if args.de <= i < args.ate:
                qs = ",".join(sorted({q.split(":")[1] for q in x["queries"].split(",")}))
                print(f"{x['id']} [{qs}] {x['ano']} | {x['titulo']}\n   {' '.join(x['abstract'].split())[:420]}\n")
        print(f"por ler: {len(por_ler)}")
        return

    campos = ["id", "decisao", "criterio", "motivo", "tema", "fase", "fontes", "queries", "titulo", "autores",
              "ano", "venue", "tipo", "doi", "abstract"]
    with open(HERE / "triagem.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    incl = sorted((l for l in linhas if l["decisao"] == "Incluir"), key=lambda l: not l["prioridade"].startswith("alta"))
    with open(HERE / "selecionados.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["id", "prioridade", "tema", "queries", "titulo", "autores", "ano", "venue",
                                          "doi", "motivo", "abstract"], extrasaction="ignore")
        w.writeheader()
        w.writerows(incl)

    # melhores por Q: prioridade alta, agrupados pela(s) query(s) onde apareceram
    melhores = []
    for q in ("Q1", "Q2", "Q3", "Q4"):
        for l in incl:
            if l["prioridade"].startswith("alta") and q in {v.split(":")[1] for v in l["queries"].split(",")}:
                melhores.append({"query": q, **l})
    with open(HERE / "melhores_por_q.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["query", "id", "prioridade", "tema", "titulo", "autores", "ano", "venue",
                                          "doi", "abstract"], extrasaction="ignore")
        w.writeheader()
        w.writerows(melhores)
    print(f"melhores por Q: {Counter(m['query'] for m in melhores)}")

    print(Counter((l["fase"], l["decisao"], l["criterio"]) for l in linhas))
    print(Counter(l["motivo"] for l in linhas if l["fase"] == "A"))
    print(f"incluídos: {len(incl)}; por ler: {len(por_ler)}")


if __name__ == "__main__":
    main()
