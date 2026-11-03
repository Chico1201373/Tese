#!/usr/bin/env python3
"""nucleo.py - mostra só o método, resultados e conclusão de um texto em textos/ (para leitura)."""
import re
import sys
from pathlib import Path

SALTAR = re.compile(r"(introduction|related work|literature review|background|acknowledg|references)", re.I)


def nucleo(caminho, limite=9000):
    t = Path(caminho).read_text(encoding="utf-8")
    titulo = t.split("\n", 1)[0].split(" | ")[0]
    partes = re.split(r"(?=SECTION [IVX]+\.|\n\d\.?\s+[A-Z][A-Za-z ]{3,40}\n)", t)
    corpo = [p for p in partes[1:] if not SALTAR.match(re.sub(r"^SECTION [IVX]+\.\s*|^\n\d\.?\s+", "", p))]
    texto = " ".join(" ".join(corpo).split()) if corpo else " ".join(t.split())
    return f"### {Path(caminho).stem} | {titulo}\n{texto[:limite]}\n"


if __name__ == "__main__":
    for c in sys.argv[1:]:
        print(nucleo(c))
