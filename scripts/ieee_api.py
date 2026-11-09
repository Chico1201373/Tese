#!/usr/bin/env python3
"""
ieee_api.py - corre as queries no IEEE Xplore através da API oficial (sem browser)
e grava os resultados em RIS, no mesmo formato que o juntar.py lê.

A query é a mesma do exportar.py: cada termo é procurado no título, no resumo e nas
palavras-chave do autor ("Document Title" / "Abstract" / "Author Keywords"), anos 2021-2026.

A chave da API NÃO fica em ficheiros: é lida da variável de ambiente IEEE_API_KEY.
Limite da chave: 10 chamadas/s e 200 chamadas/dia; cada chamada devolve até 200 registos.

Uso:
  IEEE_API_KEY=... python ieee_api.py --pasta fundamentos            # todas as queries
  IEEE_API_KEY=... python ieee_api.py --pasta fundamentos --queries Q2

Gera:
  <pasta>/exports/ieee/<Q>/ieee_<Q>_p<n>.ris
  <pasta>/exports/registo_pesquisa.md / .json   (query exata, data, total, exportados)
"""
import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

import exportar  # reutiliza a conversão da query (IEEE.query), os anos e o registo

HERE = Path(__file__).parent
API = "https://ieeexploreapi.ieee.org/api/v1/search/articles"
POR_CHAMADA = 200


def chamar(chave, querytext, inicio):
    params = {"apikey": chave, "format": "json", "querytext": querytext,
              "start_year": exportar.ANOS[0], "end_year": exportar.ANOS[1],
              "max_records": POR_CHAMADA, "start_record": inicio}
    url = API + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def ris(artigo):
    tipos = {"Journals": "JOUR", "Conferences": "CONF", "Magazines": "MGZN", "Books": "BOOK",
             "Early Access Articles": "JOUR", "Standards": "STAND"}
    linhas = [f"TY  - {tipos.get(artigo.get('content_type', ''), 'GEN')}",
              f"TI  - {' '.join(artigo.get('title', '').split())}"]
    for a in artigo.get("authors", {}).get("authors", []):
        linhas.append(f"AU  - {a.get('full_name', '')}")
    linhas += [f"PY  - {artigo.get('publication_year', '')}",
               f"T2  - {artigo.get('publication_title', '')}",
               f"DO  - {artigo.get('doi', '')}",
               f"AB  - {' '.join(artigo.get('abstract', '').split())}"]
    termos = artigo.get("index_terms", {}).get("author_terms", {}).get("terms", [])
    linhas += [f"KW  - {t}" for t in termos]
    linhas += [f"UR  - {artigo.get('html_url', '')}", "ER  - ", ""]
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", default=".")
    ap.add_argument("--queries", default=None)
    args = ap.parse_args()
    chave = os.environ.get("IEEE_API_KEY")
    if not chave:
        raise SystemExit("Define a variável de ambiente IEEE_API_KEY")

    base = (HERE / args.pasta).resolve()
    exports = base / "exports"
    exportar.EXPORTS = exports
    queries = json.loads((base / "queries.json").read_text(encoding="utf-8"))
    qids = args.queries.split(",") if args.queries else list(queries)
    reg_json = exports / "registo_pesquisa.json"
    registo = json.loads(reg_json.read_text(encoding="utf-8")) if reg_json.exists() else {}
    fonte = exportar.IEEE()

    for qid in qids:
        querytext = fonte.query(queries[qid]["q"])
        pasta = exports / "ieee" / qid
        pasta.mkdir(parents=True, exist_ok=True)
        inicio, pagina, total, exportados = 1, 1, None, 0
        while total is None or inicio <= total:
            dados = chamar(chave, querytext, inicio)
            total = int(dados.get("total_records", 0))
            artigos = dados.get("articles", [])
            if not artigos:
                break
            destino = pasta / f"ieee_{qid}_p{pagina}.ris"
            destino.write_text("\n".join(ris(a) for a in artigos), encoding="utf-8")
            exportados += len(artigos)
            print(f"{qid}: total {total}; página {pagina}: {len(artigos)} registos", flush=True)
            inicio += POR_CHAMADA
            pagina += 1
            time.sleep(1)
        registo[f"ieee/{qid}"] = {"fonte": "IEEE Xplore (API)", "qid": qid,
                                  "data": f"{datetime.now():%Y-%m-%d %H:%M}", "total": total,
                                  "exportados": exportados, "query": querytext,
                                  "ficheiros": sorted(f.name for f in pasta.glob("*.ris"))}
        exportar.gravar_registo(registo)
    print(f"Registo: {exports / 'registo_pesquisa.md'}")


if __name__ == "__main__":
    main()
