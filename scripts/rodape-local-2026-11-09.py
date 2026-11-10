"""Auditoria de 09/11/2026, itens 3, 4 e 5: rodape local em todas as paginas.

- Telefone clicavel (tel:), link para o perfil no Google Maps, botao "Avaliar no Google"
  e horario, no rodape de todas as paginas que tem rodape (bloco RCB:LOCAL-FOOTER,
  montado por rcb_menu.rodape_local com os dados de data/marca.json).
- Horario unico: 8h as 18h (era 9h no texto da pagina de contato e 8h nas 11 fichas
  tecnicas e no rodape da home).

Idempotente: a 2a execucao diz "alteradas: 0".
/consultor-seo-goiania/ (PROTEGIDA) fica de fora: so com autorizacao, em passo proprio
(use --protegida).

    python scripts/rodape-local-2026-11-09.py              # aplica
    python scripts/rodape-local-2026-11-09.py --protegida  # aplica tambem na protegida
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import rcb_menu  # noqa: E402

INTERNAS = ("docs/", "scripts/", "data/", "reports/", "node_modules/", "graphify-out/",
            "Projetos/", "modelos/", "functions/")
PROTEGIDA = "consultor-seo-goiania/index.html"
HORARIO = [("Segunda a sexta, das 9h às 18h", "Segunda a sexta, das 8h às 18h")]


def paginas():
    out = subprocess.run(["git", "ls-files", "*.html"], cwd=RAIZ, capture_output=True,
                         text=True, encoding="utf-8").stdout.split()
    return [p for p in out if not p.startswith(INTERNAS)]


def main():
    com_protegida = "--protegida" in sys.argv
    alteradas, sem_rodape = [], []
    for rel in paginas():
        if rel == PROTEGIDA and not com_protegida:
            continue
        p = os.path.join(RAIZ, rel)
        raw = io.open(p, encoding="utf-8", newline="").read()
        novo = rcb_menu.rodape_local(raw)
        if rel == "contato/index.html":
            for v, n in HORARIO:
                novo = novo.replace(v, n)
        if "<!--RCB:LOCAL-FOOTER-->" not in novo:
            sem_rodape.append(rel)
        if novo != raw:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            alteradas.append(rel)
    print("alteradas:", len(alteradas))
    print("sem rodape (ficam como estao):", sem_rodape)


if __name__ == "__main__":
    main()
