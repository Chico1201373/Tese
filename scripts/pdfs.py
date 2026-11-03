#!/usr/bin/env python3
"""
pdfs.py - descarrega o PDF dos estudos selecionados, para a leitura integral.

Abre cada estudo (pelo DOI) no TEU Safari, onde tens sessão do ISEP, e pede o PDF a
partir da própria página do artigo (usa a tua sessão). O PDF é gravado diretamente:
  ../pdfsDownload/<ieee|acm|sciencedirect|outros>/<id>.pdf
Vai devagar (pausa entre artigos) para a fonte não bloquear o IP.

Requer: Safari > Programador > "Permitir JavaScript a partir de Apple Events".

Uso:
  python3 pdfs.py                     # prioritários (48)
  python3 pdfs.py --todos             # todos os incluídos (211)
  python3 pdfs.py --prefixo 10.1145   # só uma editora (10.1145 ACM, 10.1109 IEEE)
  python3 pdfs.py --pausa 40          # segundos entre artigos (por omissão 30)

Gera também ../pdfsDownload/indice.csv (id, fonte, doi, ficheiro, estado).
Volta a correr para continuar: os PDFs já gravados são saltados.
"""
import argparse
import base64
import csv
import random
import re
import time
from pathlib import Path

from exportar import abrir, js, osa

HERE = Path(__file__).parent
DESTINO = HERE.parent / "pdfsDownload"
FONTES = {"10.1109": "ieee", "10.1145": "acm", "10.1016": "sciencedirect"}
PEDACO = 400_000  # caracteres de base64 lidos de cada vez do Safari

PEDIR = r"""
(() => {
  window.__pdf = null;
  fetch(%s, {credentials: 'include'})
    .then(r => r.ok ? r.blob() : Promise.reject('HTTP ' + r.status))
    .then(b => { const f = new FileReader(); f.onload = () => { window.__pdf = f.result; }; f.readAsDataURL(b); })
    .catch(e => { window.__pdf = 'ERRO:' + e; });
  return 'ok';
})()
"""


def url_pdf(fonte, doi):
    if fonte == "acm":
        return f"https://dl.acm.org/doi/pdf/{doi}"
    if fonte == "ieee":
        numero = re.search(r"/document/(\d+)", js("location.href"))
        return f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={numero.group(1)}" if numero else None
    return None


def esperar_artigo(doi, limite=90):
    for _ in range(limite // 3):
        if doi.lower() in js("(location.href + ' ' + document.body.innerText).toLowerCase()"):
            return True
        time.sleep(3)
    return False


def obter_pdf(url, limite=120):
    js(PEDIR % repr(url))
    for _ in range(limite // 2):
        time.sleep(2)
        n = int(float(js("window.__pdf ? window.__pdf.length : 0") or 0))
        if n:
            break
    else:
        raise RuntimeError("tempo esgotado à espera do PDF")
    dados = "".join(js(f"window.__pdf.slice({i}, {i + PEDACO})") for i in range(0, n, PEDACO))
    js("window.__pdf = null")
    if dados.startswith("ERRO:"):
        raise RuntimeError(dados)
    conteudo = base64.b64decode(dados.split(",", 1)[1])
    if not conteudo.startswith(b"%PDF"):
        raise RuntimeError("a resposta não é um PDF (sem acesso ou página de login)")
    return conteudo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--prefixo", default="")
    ap.add_argument("--pausa", type=int, default=30)
    args = ap.parse_args()

    sel = list(csv.DictReader(open(HERE / "selecionados.csv", encoding="utf-8-sig")))
    if not args.todos:
        sel = [s for s in sel if s["prioridade"].startswith("alta")]
    if args.prefixo:
        sel = [s for s in sel if s["doi"].startswith(args.prefixo)]
    indice_f = DESTINO / "indice.csv"
    DESTINO.mkdir(exist_ok=True)
    indice = {}
    if indice_f.exists():
        indice = {r["id"]: r for r in csv.DictReader(open(indice_f, encoding="utf-8-sig"))}

    def gravar_indice():
        with open(indice_f, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["id", "fonte", "doi", "ficheiro", "estado"])
            w.writeheader()
            w.writerows(indice.values())

    for n, s in enumerate(sel, 1):
        fonte = FONTES.get(s["doi"].split("/")[0], "outros")
        ficheiro = DESTINO / fonte / f"{s['id']}.pdf"
        if ficheiro.exists():
            continue
        print(f"[{n}/{len(sel)}] {s['id']} ({fonte}) {s['titulo'][:65]}", flush=True)
        estado = "descarregado"
        if not s["doi"]:
            estado = "sem DOI (descarregar à mão)"
        elif fonte not in ("ieee", "acm"):
            estado = "fonte sem suporte (descarregar à mão)"
        else:
            abrir(f"https://doi.org/{s['doi']}", espera=10)
            try:
                if not esperar_artigo(s["doi"]):
                    raise RuntimeError("a página do artigo não carregou")
                url = url_pdf(fonte, s["doi"])
                if not url:
                    raise RuntimeError("não encontrei o endereço do PDF")
                conteudo = obter_pdf(url)
                ficheiro.parent.mkdir(parents=True, exist_ok=True)
                ficheiro.write_bytes(conteudo)
                print(f"   ok ({len(conteudo) // 1024} KB)", flush=True)
            except RuntimeError as e:
                estado = f"falhou: {e}"
                print(f"   {estado}", flush=True)
                if "sem acesso" in str(e):
                    osa('display notification "Sem acesso ao PDF: confirma o login institucional" with title "pdfs.py"')
            time.sleep(args.pausa + random.uniform(0, 10))
        indice[s["id"]] = {"id": s["id"], "fonte": fonte, "doi": s["doi"],
                           "ficheiro": str(ficheiro.relative_to(DESTINO)) if ficheiro.exists() else "", "estado": estado}
        gravar_indice()

    estados = [r["estado"].split(":")[0] for r in indice.values()]
    print({e: estados.count(e) for e in set(estados)})


if __name__ == "__main__":
    main()
