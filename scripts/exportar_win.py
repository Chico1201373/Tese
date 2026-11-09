#!/usr/bin/env python3
"""
exportar_win.py - versão Windows do exportar.py: em vez do Safari (AppleScript),
controla o Chrome com o Playwright. Usa as MESMAS classes das fontes do exportar.py
(URL, campos título/resumo/palavras-chave, anos, seleção e exportação de cada página).

Abre uma janela do Chrome com um perfil próprio (../browser_profile). Se aparecer uma
verificação "sou humano" ou um pedido de login, resolve-a nessa janela; o script espera.

Uso:
  python exportar_win.py --pasta fundamentos --so-totais    # só os totais de cada query
  python exportar_win.py --pasta fundamentos                # exporta tudo
  python exportar_win.py --pasta fundamentos --fontes ieee --queries Q2

  --pasta  pasta com queries.json; os exports vão para <pasta>/exports/<fonte>/<Q>/
           (por omissão, a própria pasta scripts, como no exportar.py original)

Requer: pip install playwright   (usa o Chrome instalado; não descarrega browsers)
"""
import argparse
import json
import math
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

import exportar

HERE = Path(__file__).parent
PERFIL = HERE.parent / "browser_profile"
page = None


def js(code):
    """Avalia JS na página e devolve texto, como o osascript do exportar.py."""
    v = page.evaluate(code)
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def osa(script):
    if "display notification" in script:
        print("   >> Resolve a verificação/login na janela do Chrome; fico à espera...", flush=True)
        return ""
    raise RuntimeError("osascript não existe no Windows")


def abrir(url, espera=12):
    page.goto(url, wait_until="domcontentloaded", timeout=120_000)
    time.sleep(espera)
    exportar.verificar_bloqueio()


# As classes do exportar.py chamam js/abrir/osa do próprio módulo: substituímo-los.
exportar.js, exportar.osa, exportar.abrir = js, osa, abrir


def main():
    global page
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", default=".")
    ap.add_argument("--fontes", default="ieee,acm,sciencedirect")
    ap.add_argument("--queries", default=None)
    ap.add_argument("--so-totais", action="store_true")
    args = ap.parse_args()

    base = (HERE / args.pasta).resolve()
    exports = base / "exports"
    exportar.EXPORTS = exports
    queries = json.loads((base / "queries.json").read_text(encoding="utf-8"))
    qids = args.queries.split(",") if args.queries else list(queries)
    exports.mkdir(parents=True, exist_ok=True)
    reg_json = exports / "registo_pesquisa.json"
    registo = json.loads(reg_json.read_text(encoding="utf-8")) if reg_json.exists() else {}

    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            str(PERFIL), channel="chrome", headless=False, accept_downloads=True,
            viewport={"width": 1400, "height": 900})
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        for chave in args.fontes.split(","):
            fonte = exportar.FONTES[chave]
            for qid in qids:
                q = queries[qid]["q"]
                pasta = exports / chave / qid
                pasta.mkdir(parents=True, exist_ok=True)
                print(f"== {fonte.nome} / {qid}", flush=True)
                abrir(fonte.url(q, 1), espera=15)
                total = None
                for _ in range(15):
                    total = fonte.total()
                    if total is not None:
                        break
                    time.sleep(2)
                if total is None:
                    print("   não consegui ler o total; salto esta query", flush=True)
                    continue
                paginas = math.ceil((total or 0) / fonte.por_pagina)
                print(f"   total: {total}; páginas: {paginas}", flush=True)
                r = registo.setdefault(f"{chave}/{qid}", {"fonte": fonte.nome, "qid": qid, "ficheiros": []})
                r.update({"data": f"{datetime.now():%Y-%m-%d %H:%M}", "total": total, "query": fonte.query(q)})
                if not args.so_totais:
                    for p in range(1, paginas + 1):
                        destino = pasta / f"{chave}_{qid}_p{p}.{fonte.ext}"
                        if destino.exists():
                            print(f"   página {p}: já exportada")
                            continue
                        if p > 1:
                            abrir(fonte.url(q, p), espera=15)
                        with page.expect_download(timeout=240_000) as d:
                            fonte.exportar_pagina()
                        d.value.save_as(destino)
                        print(f"   página {p}: {fonte.contar(destino)} registos -> {destino.relative_to(HERE)}", flush=True)
                        time.sleep(4)
                    r["ficheiros"] = sorted(f.name for f in pasta.glob(f"*.{fonte.ext}"))
                    r["exportados"] = sum(fonte.contar(f) for f in pasta.glob(f"*.{fonte.ext}"))
                exportar.gravar_registo(registo)
        ctx.close()
    print(f"Registo: {exports / 'registo_pesquisa.md'}")


if __name__ == "__main__":
    main()
