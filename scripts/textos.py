#!/usr/bin/env python3
"""
textos.py - guarda o texto integral dos estudos selecionados, para a fase de elegibilidade.

Abre cada estudo (pelo DOI) no TEU Safari, onde tens sessão do ISEP, e guarda o texto
da página. No IEEE Xplore e na ACM DL a página do artigo mostra o texto integral em HTML.
Vai devagar (pausa entre artigos) para a fonte não bloquear o IP.

Requer: Safari > Programador > "Permitir JavaScript a partir de Apple Events".

Uso:
  python3 textos.py                 # só os prioritários (48)
  python3 textos.py --todos         # todos os incluídos (211)
  python3 textos.py --pausa 30      # segundos entre artigos (por omissão 25)
  python3 textos.py --prefixo 10.1145   # só uma editora (10.1145 ACM, 10.1109 IEEE)

Gera:
  textos/<id>.txt      texto da página do artigo
  textos/indice.csv    id, doi, url final, n.º de caracteres e estado
Volta a correr para continuar: os estudos já guardados com texto integral são saltados.
"""
import argparse
import csv
import random
import time
from pathlib import Path

from exportar import abrir, js, osa

HERE = Path(__file__).parent
PASTA = HERE / "textos"
MIN_INTEGRAL = 15000  # abaixo disto, a página tem provavelmente só o resumo

# remove menus, referências laterais e afins antes de ler o texto
EXTRAIR = r"""
(() => {
  const alvo = document.querySelector('article, .document-main, #article-container, main') || document.body;
  const copia = alvo.cloneNode(true);
  copia.querySelectorAll('nav, header, footer, script, style, aside, .stats-document-footer').forEach(e => e.remove());
  return document.title + '\n' + location.href + '\n\n' + copia.innerText;
})()
"""


def carregar_tudo():
    # o IEEE carrega secções à medida que se desce na página
    for _ in range(8):
        js("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.5)
    js("window.scrollTo(0, 0)")


def esperar_artigo(doi, limite=90):
    # o redirecionamento do DOI pode demorar; sem isto guardava-se a página do artigo anterior
    for _ in range(limite // 3):
        if doi.lower() in js("(location.href + ' ' + document.body.innerText).toLowerCase()"):
            return
        time.sleep(3)
    raise RuntimeError(f"a página do DOI {doi} não carregou")


def esperar_sessao():
    # sem sessão institucional o IEEE só mostra o resumo; espera pelo login e recarrega
    sem = lambda: "Sign In or Purchase" in js("document.body.innerText.slice(0, 3000)")
    if not sem():
        return
    print("   Sem acesso ao texto integral: faz login institucional (ISEP) no Safari; fico à espera...", flush=True)
    osa('display notification "Faz login institucional no Safari" with title "textos.py"')
    while sem():
        time.sleep(10)
        js("location.reload()")
        time.sleep(8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--pausa", type=int, default=25)
    ap.add_argument("--prefixo", default="", help="só DOIs com este prefixo, ex.: 10.1145 (ACM) ou 10.1109 (IEEE)")
    args = ap.parse_args()

    sel = list(csv.DictReader(open(HERE / "selecionados.csv", encoding="utf-8-sig")))
    if not args.todos:
        sel = [s for s in sel if s["prioridade"].startswith("alta")]
    if args.prefixo:
        sel = [s for s in sel if s["doi"].startswith(args.prefixo)]
    PASTA.mkdir(exist_ok=True)
    indice_f = PASTA / "indice.csv"
    indice = {}
    if indice_f.exists():
        indice = {r["id"]: r for r in csv.DictReader(open(indice_f, encoding="utf-8-sig"))}

    for n, s in enumerate(sel, 1):
        feito = indice.get(s["id"])
        if feito and feito["estado"] == "integral":
            continue
        if not s["doi"]:
            indice[s["id"]] = {"id": s["id"], "doi": "", "url": "", "caracteres": 0, "estado": "sem DOI"}
            continue
        print(f"[{n}/{len(sel)}] {s['id']} {s['titulo'][:70]}", flush=True)
        abrir(f"https://doi.org/{s['doi']}", espera=12)
        try:
            esperar_artigo(s["doi"])
            esperar_sessao()
            carregar_tudo()
            texto = js(EXTRAIR)
        except RuntimeError as e:
            print(f"   erro: {e}")
            texto = ""
        estado = "integral" if len(texto) >= MIN_INTEGRAL else "só resumo"
        (PASTA / f"{s['id']}.txt").write_text(texto, encoding="utf-8")
        url = texto.split("\n", 2)[1] if texto.count("\n") >= 2 else ""
        indice[s["id"]] = {"id": s["id"], "doi": s["doi"], "url": url, "caracteres": len(texto), "estado": estado}
        print(f"   {estado} ({len(texto)} caracteres)", flush=True)
        with open(indice_f, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["id", "doi", "url", "caracteres", "estado"])
            w.writeheader()
            w.writerows(indice.values())
        time.sleep(args.pausa + random.uniform(0, 10))

    estados = [r["estado"] for r in indice.values()]
    print({e: estados.count(e) for e in set(estados)})


if __name__ == "__main__":
    main()
