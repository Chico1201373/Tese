#!/usr/bin/env python3
"""
exportar.py - corre Q1-Q4 em IEEE Xplore, ACM DL e ScienceDirect no TEU Safari,
seleciona todos os resultados de cada página e exporta-os com resumo.

As três fontes pesquisam o mesmo: título, resumo e palavras-chave (equivalente
a TITLE-ABS-KEY), anos 2021-2026, todos os resultados.

Requer: Safari > Programador > "Permitir JavaScript a partir de Apple Events".
Se aparecer uma verificação "sou humano", resolve-a no Safari (sem fechar a
janela); o script espera.

Uso:
  python3 exportar.py                          # todas as fontes e queries
  python3 exportar.py --fontes ieee,acm        # só algumas fontes
  python3 exportar.py --queries Q2             # só algumas queries
  python3 exportar.py --so-totais              # só regista os totais

Gera:
  exports/<fonte>/<Q>/<fonte>_<Q>_p<n>.<ris|bib>
  exports/registo_pesquisa.md    (query exata, data, total, páginas exportadas)
"""
import argparse
import json
import math
import re
import subprocess
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
EXPORTS = HERE / "exports"
DOWNLOADS = Path.home() / "Downloads"
ANOS = (2021, 2026)
BLOCK_HINTS = ("are you a robot", "verify you are human", "just a moment", "captcha",
               "verifying you are human", "there was a problem providing the content you requested")
TERMO = r'("[^"]+"|\b(?!AND\b|OR\b)[A-Za-z][\w-]*)'


# ----------------------------------------------------------------------------
# Safari
# ----------------------------------------------------------------------------
def osa(script):
    out = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if out.returncode:
        raise RuntimeError(out.stderr.strip())
    return out.stdout.strip()


def js(code):
    return osa(f'tell application "Safari" to do JavaScript {json.dumps(code)} in current tab of front window')


def abrir(url, espera=12):
    osa(f'''tell application "Safari"
        if (count of windows) = 0 then make new document
        set URL of current tab of front window to {json.dumps(url)}
    end tell''')
    time.sleep(espera)
    verificar_bloqueio()


def verificar_bloqueio():
    def texto():
        try:
            return js("(document.title + ' ' + document.body.innerText.slice(0,800)).toLowerCase()")
        except RuntimeError:
            return ""
    t = texto()
    if not any(h in t for h in BLOCK_HINTS):
        return
    if "there was a problem providing" in t:
        raise SystemExit("A fonte bloqueou o IP temporariamente. Tenta mais tarde.")
    print("   Verificação no Safari: resolve-a lá (sem fechar a janela); fico à espera...", flush=True)
    osa('display notification "Resolve a verificação no Safari" with title "exportar.py"')
    while any(h in t for h in BLOCK_HINTS):
        time.sleep(5)
        t = texto()
    time.sleep(5)


def clicar(seletor_js):
    """Corre uma expressão JS que devolve o elemento e clica-o; erro se não existir."""
    if js(f"(() => {{ const e = {seletor_js}; if (!e) return 'no'; e.click(); return 'ok'; }})()") != "ok":
        raise RuntimeError(f"Elemento não encontrado: {seletor_js}")


def esperar_download(antes, timeout=240):
    """Espera por um ficheiro novo e completo em ~/Downloads."""
    t0 = time.monotonic()
    while time.monotonic() - t0 < timeout:
        novos = [p for p in DOWNLOADS.iterdir() if p.name not in antes and not p.name.startswith(".")
                 and not p.name.endswith(".download")]
        if novos:
            f = max(novos, key=lambda p: p.stat().st_mtime)
            tamanho = -1
            while tamanho != f.stat().st_size:
                tamanho = f.stat().st_size
                time.sleep(1.5)
            return f
        time.sleep(1)
    raise RuntimeError("O download não apareceu em ~/Downloads")


def so_digitos(texto):
    return int(re.sub(r"\D", "", texto)) if re.search(r"\d", texto or "") else None


# ----------------------------------------------------------------------------
# Fontes: URL da pesquisa, total, seleção e exportação de uma página
# ----------------------------------------------------------------------------
class IEEE:
    nome, ext, por_pagina = "IEEE Xplore", "ris", 100

    def query(self, q):
        return re.sub(TERMO, lambda m: '("Document Title":%s OR "Abstract":%s OR "Author Keywords":%s)'
                      % ((m.group(1),) * 3), q)

    def url(self, q, pagina):
        return "https://ieeexplore.ieee.org/search/searchresult.jsp?" + urllib.parse.urlencode({
            "queryText": self.query(q), "ranges": f"{ANOS[0]}_{ANOS[1]}_Year",
            "rowsPerPage": self.por_pagina, "pageNumber": pagina}, quote_via=urllib.parse.quote)

    def total(self):
        t = js("(document.body.innerText.match(/Showing [\\d,]+\\s*-\\s*[\\d,]+ of ([\\d,]+)/)||['',''])[1]"
               " || (/No results found/.test(document.body.innerText) ? '0' : '')")
        return so_digitos(t)

    def exportar_pagina(self):
        clicar("document.querySelector('label.results-actions-selectall')")
        time.sleep(1)
        clicar("[...document.querySelectorAll('button')].find(b => b.innerText.trim() == 'Export')")
        time.sleep(3)
        clicar("[...document.querySelectorAll('ngb-modal-window a.nav-link')].find(a => a.innerText.trim() == 'Citations')")
        time.sleep(2)
        js("[...document.querySelectorAll('ngb-modal-window input[type=radio]')].forEach(i => {"
           " if (/^(RIS|Citation and Abstract)$/.test((i.closest('label,div') || {}).innerText?.trim())) i.click(); })")
        time.sleep(1)
        clicar("[...document.querySelectorAll('ngb-modal-window button')].filter(b => b.innerText.trim() == 'Download').pop()")

    def contar(self, ficheiro):
        return len(re.findall(r"^ER\s+-", ficheiro.read_text(encoding="utf-8", errors="ignore"), re.M))


class ACM:
    nome, ext, por_pagina = "ACM Digital Library", "bib", 50

    def query(self, q):
        return re.sub(TERMO, lambda m: "(Title:%s OR Abstract:%s OR Keyword:%s)" % ((m.group(1),) * 3), q)

    def url(self, q, pagina):
        return "https://dl.acm.org/action/doSearch?" + urllib.parse.urlencode({
            "AllField": self.query(q), "AfterYear": ANOS[0], "BeforeYear": ANOS[1],
            "pageSize": self.por_pagina, "startPage": pagina - 1}, quote_via=urllib.parse.quote)

    def total(self):
        return so_digitos(js("(document.querySelector('.hitsLength') || {innerText: ''}).innerText"))

    def exportar_pagina(self):
        marcados = "document.querySelectorAll('.search__item input[type=checkbox]:checked').length"
        for _ in range(10):
            js("(() => { const m = document.querySelector('input[name=markall]');"
               " if (m && document.querySelector('.search__item')) { if (m.checked) m.click(); m.click(); } })()")
            time.sleep(2)
            if float(js(marcados) or 0) > 0:
                break
        else:
            raise RuntimeError("Não consegui selecionar os resultados da página")
        clicar("document.querySelector('a.export-citation')")
        time.sleep(4)
        clicar("document.querySelector('a[href=\"#selectedTab\"]')")
        js("(() => { const s = document.querySelector('#selectedTab select, .modal select');"
           " if (s && s.value != 'bibtex') { s.value = 'bibtex'; s.dispatchEvent(new Event('change', {bubbles: true})); } })()")
        for _ in range(20):
            time.sleep(2)
            if (js("((document.querySelector('#selectedTab') || {}).innerText || '').indexOf('@') >= 0") == "true"):
                break
        clicar("document.querySelector('#selectedTab a.download__btn, .modal a.download__btn')")

    def contar(self, ficheiro):
        return len(re.findall(r"^@\w+\{", ficheiro.read_text(encoding="utf-8", errors="ignore"), re.M))


class ScienceDirect:
    nome, ext, por_pagina = "ScienceDirect", "ris", 100

    def query(self, q):
        return f"TITLE-ABS-KEY({q})"

    def url(self, q, pagina):
        return "https://www.sciencedirect.com/search?" + urllib.parse.urlencode({
            "qs": self.query(q), "years": ",".join(str(a) for a in range(ANOS[0], ANOS[1] + 1)),
            "show": self.por_pagina, "offset": (pagina - 1) * self.por_pagina}, quote_via=urllib.parse.quote)

    def total(self):
        t = js("(document.querySelector('.search-body-results-text') || {innerText: ''}).innerText")
        if not t and "no results" in js("document.body.innerText.toLowerCase().slice(0, 3000)"):
            return 0
        return so_digitos(t)

    def exportar_pagina(self):
        js("(() => { const c = document.querySelector('#select-all-results, input[aria-label*=\"Select all\" i]');"
           " if (c && !c.checked) c.click(); })()")
        time.sleep(2)
        clicar("[...document.querySelectorAll('button')].find(b => /^Export$/i.test(b.innerText.trim()))")
        time.sleep(3)
        clicar("[...document.querySelectorAll('button, a')].find(b => /export citation to RIS/i.test(b.innerText))")

    def contar(self, ficheiro):
        return len(re.findall(r"^ER\s+-", ficheiro.read_text(encoding="utf-8", errors="ignore"), re.M))


FONTES = {"ieee": IEEE(), "acm": ACM(), "sciencedirect": ScienceDirect()}


# ----------------------------------------------------------------------------
# Registo
# ----------------------------------------------------------------------------
def gravar_registo(registo):
    linhas = ["# Registo da pesquisa", "",
              f"- **Campos:** título, resumo e palavras-chave (equivalente a TITLE-ABS-KEY) em todas as fontes",
              f"- **Anos:** {ANOS[0]}-{ANOS[1]} (filtro da interface); confirmar 27-10-2021 a 27-10-2026 na triagem",
              "- **Regra de paragem:** todos os resultados", "- **Exportação:** RIS (IEEE, ScienceDirect) e BibTeX (ACM), com resumo", "",
              "| Fonte | Query | Data | Total na fonte | Exportados | Ficheiros |", "|---|---|---|---:|---:|---|"]
    for r in registo.values():
        linhas.append(f"| {r['fonte']} | {r['qid']} | {r['data']} | {r['total']} | {r.get('exportados', '-')} | {len(r['ficheiros'])} |")
    linhas += ["", "## Query executada em cada fonte", ""]
    for r in registo.values():
        linhas += [f"**{r['fonte']} — {r['qid']}**", "", "```", r["query"], "```", ""]
    (EXPORTS / "registo_pesquisa.md").write_text("\n".join(linhas), encoding="utf-8")
    (EXPORTS / "registo_pesquisa.json").write_text(json.dumps(registo, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fontes", default="ieee,acm,sciencedirect")
    ap.add_argument("--queries", default="Q1,Q2,Q3,Q4")
    ap.add_argument("--so-totais", action="store_true")
    args = ap.parse_args()

    queries = json.loads((HERE / "queries.json").read_text(encoding="utf-8"))
    EXPORTS.mkdir(exist_ok=True)
    reg_json = EXPORTS / "registo_pesquisa.json"
    registo = json.loads(reg_json.read_text(encoding="utf-8")) if reg_json.exists() else {}

    for chave in args.fontes.split(","):
        fonte = FONTES[chave]
        for qid in args.queries.split(","):
            q = queries[qid]["q"]
            pasta = EXPORTS / chave / qid
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
                    antes = {f.name for f in DOWNLOADS.iterdir()}
                    fonte.exportar_pagina()
                    ficheiro = esperar_download(antes)
                    ficheiro.rename(destino)
                    print(f"   página {p}: {fonte.contar(destino)} registos -> {destino.relative_to(HERE)}", flush=True)
                    time.sleep(4)
                r["ficheiros"] = sorted(f.name for f in pasta.glob(f"*.{fonte.ext}"))
                r["exportados"] = sum(fonte.contar(f) for f in pasta.glob(f"*.{fonte.ext}"))
            gravar_registo(registo)
    print(f"Registo: {(EXPORTS / 'registo_pesquisa.md').relative_to(HERE)}")


if __name__ == "__main__":
    main()
