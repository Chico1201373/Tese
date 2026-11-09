#!/usr/bin/env python3
"""
pdfs_win.py - versão Windows do pdfs.py para os estudos escolhidos de uma pesquisa
(decisao = Incluir em <pasta>/decisoes_*.csv). Abre cada artigo pelo DOI no Chrome
(perfil ../browser_profile) e pede o PDF ao IEEE Xplore com a sessão dessa janela.

Os artigos em acesso aberto descarregam logo. Para os restantes, entra no IEEE
com o acesso institucional (Sign In > Access through your organization > ISEP)
na janela do Chrome; o script espera e tenta outra vez.

Uso:
  python pdfs_win.py --pasta fundamentos
Gera:
  ../pdfsDownload/<pasta>/<id>.pdf  e  <id>.txt (texto extraído com pdftotext)
  ../pdfsDownload/<pasta>/indice.csv
"""
import argparse
import csv
import re
import shutil
import subprocess
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
PERFIL = HERE.parent / "browser_profile"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", required=True)
    ap.add_argument("--pausa", type=int, default=20, help="segundos entre artigos")
    ap.add_argument("--espera-login", type=int, default=0,
                    help="abre o IEEE e espera N segundos para o login institucional antes de começar")
    args = ap.parse_args()
    base = (HERE / args.pasta).resolve()
    destino = HERE.parent / "pdfsDownload" / args.pasta
    destino.mkdir(parents=True, exist_ok=True)

    decisoes = {}
    for f in base.glob("decisoes_*.csv"):
        decisoes.update({r["id"]: r for r in csv.DictReader(open(f, encoding="utf-8-sig")) if r["decisao"] == "Incluir"})
    registos = {r["id"]: r for r in csv.DictReader(open(base / "registos.csv", encoding="utf-8-sig"))}
    escolhidos = [registos[i] for i in decisoes]
    indice = []

    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(str(PERFIL), channel="chrome", headless=False,
                                                    viewport={"width": 1400, "height": 900})
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        if args.espera_login:
            page.goto("https://ieeexplore.ieee.org/Xplore/home.jsp", wait_until="domcontentloaded", timeout=120_000)
            print("Entra no IEEE (Institutional Sign In > ISEP). Fico à espera até veres "
                  f"'Access provided by' (máximo {args.espera_login} s)...", flush=True)
            t0 = time.monotonic()
            while time.monotonic() - t0 < args.espera_login:
                time.sleep(5)
                try:
                    if "Access provided by" in page.evaluate("document.body.innerText"):
                        print("Sessão institucional detetada; começo.", flush=True)
                        break
                except Exception:
                    pass  # a página está a mudar durante o login
            else:
                print("Não detetei a sessão institucional; continuo na mesma.", flush=True)
        for s in escolhidos:
            pdf = destino / f"{s['id']}.pdf"
            estado = "já existia"
            if not pdf.exists():
                try:
                    page.goto(f"https://doi.org/{s['doi']}", wait_until="domcontentloaded", timeout=120_000)
                except Exception:
                    pass  # o redirecionamento do doi.org às vezes interrompe o goto; a página continua a abrir
                time.sleep(10)
                numero = re.search(r"/document/(\d+)", page.url)
                if not numero:
                    estado = "sem número do artigo IEEE"
                else:
                    url = f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={numero.group(1)}"
                    for tentativa in range(3):
                        r = ctx.request.get(url, timeout=120_000)
                        if r.ok and r.body()[:4] == b"%PDF":
                            pdf.write_bytes(r.body())
                            estado = "descarregado"
                            break
                        estado = "sem acesso (login institucional?)"
                        if tentativa < 2:
                            print(f"   {s['id']}: sem acesso ao PDF. Entra no IEEE com o acesso do ISEP"
                                  " na janela do Chrome; tento outra vez dentro de 60 s...", flush=True)
                            time.sleep(60)
                time.sleep(args.pausa)
            if pdf.exists() and shutil.which("pdftotext"):
                subprocess.run(["pdftotext", "-layout", str(pdf), str(pdf.with_suffix(".txt"))])
            print(f"{s['id']}: {estado}", flush=True)
            indice.append({"id": s["id"], "doi": s["doi"], "ficheiro": pdf.name if pdf.exists() else "", "estado": estado})
        ctx.close()

    with open(destino / "indice.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["id", "doi", "ficheiro", "estado"])
        w.writeheader()
        w.writerows(indice)
    print(f"Índice: {destino / 'indice.csv'}")


if __name__ == "__main__":
    main()
