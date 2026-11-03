#!/usr/bin/env python3
"""
pdf_texto.py - converte os PDFs de ../pdfsDownload em texto, para leitura e extração.

Corre com o ambiente virtual (tem o pypdf):
  .venv/bin/python pdf_texto.py

Gera ../pdfsDownload/<fonte>/<id>.txt ao lado de cada PDF, sem a lista de referências.
Os PDFs já convertidos são saltados.
"""
import re
from pathlib import Path

import pypdf

DESTINO = Path(__file__).parent.parent / "pdfsDownload"
REFERENCIAS = re.compile(r"\n\s*(REFERENCES|References|Bibliography)\s*\n")


def main():
    for pdf in sorted(DESTINO.glob("*/*.pdf")):
        txt = pdf.with_suffix(".txt")
        if txt.exists():
            continue
        try:
            paginas = [p.extract_text() or "" for p in pypdf.PdfReader(pdf).pages]
        except Exception as e:  # PDF corrompido ou cifrado
            print(f"{pdf.name}: erro ({e})")
            continue
        texto = "\n".join(paginas)
        partes = REFERENCIAS.split(texto)
        if len(partes) > 1:
            texto = "".join(partes[:-2])  # tudo até à última secção de referências
        txt.write_text(texto, encoding="utf-8")
        print(f"{pdf.parent.name}/{txt.name}: {len(paginas)} páginas, {len(texto)} caracteres")


if __name__ == "__main__":
    main()
