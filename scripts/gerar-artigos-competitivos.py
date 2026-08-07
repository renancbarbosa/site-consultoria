# -*- coding: utf-8 -*-
"""
Gera os artigos do blog dos clusters "mercados competitivos" e "domínios e autoridade".

Uso:  python scripts/gerar-artigos-competitivos.py

Idempotente. O conteúdo vive em scripts/conteudo/artigos_*.py; aqui só se
percorre, valida e escreve.

Validações que impedem publicar artigo ruim:
  - mínimo de palavras (nada de artigo raso)
  - um único H1
  - sem marcador de rascunho
  - slug único entre todos os módulos
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))

from rcb_base import escrever, contar_palavras  # noqa: E402
from rcb_artigo import render_artigo            # noqa: E402

import artigos_competitivo   # noqa: E402
import artigos_estrategia    # noqa: E402
import artigos_dominios      # noqa: E402
import artigos_backlinks     # noqa: E402
import artigos_iptv          # noqa: E402
import artigos_bets          # noqa: E402
import artigos_iptv_lote2     # noqa: E402
import artigos_dominios_lote2 # noqa: E402
import artigos_bets_lote2     # noqa: E402

MODULOS = [
    ("Mercados competitivos", artigos_competitivo),
    ("Estratégia e decisão", artigos_estrategia),
    ("Domínios e migração", artigos_dominios),
    ("Backlinks e autoridade", artigos_backlinks),
    ("IPTV e streaming", artigos_iptv),
    ("Bets e iGaming", artigos_bets),
    ("IPTV — lote 2", artigos_iptv_lote2),
    ("Domínios — lote 2", artigos_dominios_lote2),
    ("Bets — lote 2", artigos_bets_lote2),
]

# Referência: os artigos já publicados no site têm mediana de ~1.005 palavras
# (medido em 06/08/2026, n=67). O piso abaixo fica um pouco acima do menor
# artigo existente, para impedir texto raso sem exigir enchimento.
MIN_PALAVRAS = 620


def main():
    vistos = set()
    total = 0
    palavras_total = 0
    inventario = []

    print("Gerando artigos dos clusters novos\n")

    for nome, modulo in MODULOS:
        print(f"[{nome}]")
        for a in modulo.ARTIGOS:
            slug = a["slug"]
            assert slug not in vistos, f"slug duplicado: {slug}"
            vistos.add(slug)

            caminho, html = render_artigo(a)

            corpo = html.split('<article class="artigo-body">')[-1].split("</article>")[0]
            n = contar_palavras(corpo)
            assert n >= MIN_PALAVRAS, f"{slug}: raso demais ({n} palavras)"
            assert html.count("<h1") == 1, f"{slug}: deve ter exatamente um H1"
            for proibido in ("TODO", "Lorem ipsum", "PLACEHOLDER", "[[", "XXX"):
                assert proibido not in html, f"{slug}: contém marcador '{proibido}'"

            escrever(caminho, html)
            inventario.append((f"/blog/{slug}/", a["h1"], n, a["cat"]))
            palavras_total += n
            total += 1
            print(f"  ok  {slug[:52]:54s} {n:>5} palavras")
        print()

    print(f"{total} artigos gerados · {palavras_total:,} palavras no total".replace(",", "."))
    return inventario


if __name__ == "__main__":
    main()
