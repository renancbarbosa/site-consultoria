"""Copy humana e para leigo no site inteiro (pedido do Renan, 05/10/2026). Idempotente.

Aplica scripts/rcb_copy.py:
  - humanizar() em todas as paginas HTML (sem travessao, sem palavra de IA, termo tecnico explicado
    na primeira vez que aparece no corpo da pagina);
  - texto() no llms.txt e no llms-full.txt.
Os geradores (rcb_base.escrever, gerar-servicos-marketing.py, gerar-paginas-cidades.py) chamam
humanizar() na gravacao, entao uma regeracao nao traz nada de volta.

    python scripts/copy-humana-2026-10-05.py
"""
import glob
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rcb_copy  # noqa: E402

RAIZ = os.path.dirname(AQUI)
FORA = ("node_modules", "graphify-out", "Projetos", "reports", "docs", ".playwright-mcp", "scripts", "data")


def main():
    alterados = 0
    for p in sorted(glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)):
        if os.path.relpath(p, RAIZ).replace("\\", "/").startswith(FORA):
            continue
        s = io.open(p, encoding="utf-8", newline="").read()
        n = rcb_copy.humanizar(s)
        if n != s:
            io.open(p, "w", encoding="utf-8", newline="").write(n)
            alterados += 1
    for nome in ("llms.txt", "llms-full.txt"):
        p = os.path.join(RAIZ, nome)
        s = io.open(p, encoding="utf-8", newline="").read()
        n = rcb_copy.texto(s)
        if n != s:
            io.open(p, "w", encoding="utf-8", newline="").write(n)
            alterados += 1
    print("alterados: %d" % alterados)


if __name__ == "__main__":
    main()
