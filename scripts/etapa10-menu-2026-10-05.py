"""Etapa 10 do plano de nichos (05/10/2026): paginas-indice /servicos/ e /nichos/ no menu e no rodape.

O conteudo das listas esta em scripts/rcb_menu.py (fonte unica). Este script so reaplica
rcb_menu.aplicar() em todas as paginas HTML do site. Idempotente: a 2a execucao diz "alteradas: 0".

    python scripts/etapa10-menu-2026-10-05.py
"""
import glob
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rcb_menu  # noqa: E402

RAIZ = os.path.dirname(AQUI)
FORA = ("node_modules", "graphify-out", "Projetos", "reports", "docs", ".playwright-mcp", "scripts")


def main():
    total = alteradas = 0
    for p in sorted(glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        if rel.startswith(FORA):
            continue
        total += 1
        h = io.open(p, encoding="utf-8", newline="").read()
        n = rcb_menu.aplicar(h)
        if n != h:
            io.open(p, "w", encoding="utf-8", newline="").write(n)
            alteradas += 1
    print("paginas: %d  alteradas: %d" % (total, alteradas))


if __name__ == "__main__":
    main()
