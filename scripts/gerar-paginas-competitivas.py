# -*- coding: utf-8 -*-
"""
Gera as páginas comerciais da divisão "SEO para mercados competitivos".

Uso:  python scripts/gerar-paginas-competitivas.py

Idempotente: sobrescreve as páginas geradas e não toca em mais nada.
O conteúdo de cada página vive em scripts/conteudo/cluster_*.py — este arquivo
só percorre os módulos, escreve o HTML e confere o resultado.

Arquitetura e matriz de canibalização: docs/seo-mercados-competitivos-plan.md
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))

from rcb_base import escrever, contar_palavras, strip_tags  # noqa: E402

import cluster_central                                       # noqa: E402
import cluster_iptv                                          # noqa: E402
import cluster_bets                                          # noqa: E402
import cluster_dominios                                      # noqa: E402
import pagina_analise                                        # noqa: E402

MODULOS = [
    ("Central", cluster_central),
    ("IPTV e streaming", cluster_iptv),
    ("Bets e iGaming", cluster_bets),
    ("Domínios e autoridade", cluster_dominios),
    ("Conversão", pagina_analise),
]


def main():
    total = 0
    urls = []
    print("Gerando páginas da divisão de mercados competitivos\n")

    for nome_cluster, modulo in MODULOS:
        print(f"[{nome_cluster}]")
        for fabrica in modulo.PAGINAS:
            caminho, html = fabrica()

            # Conferências que impedem publicar página quebrada.
            corpo = html.split('<main id="main-content">')[-1].split("</main>")[0]
            palavras = contar_palavras(corpo)
            assert palavras > 600, f"{caminho}: conteúdo curto demais ({palavras} palavras)"
            for proibido in ("TODO", "Lorem ipsum", "PLACEHOLDER", "XXX"):
                assert proibido not in html, f"{caminho}: contém marcador '{proibido}'"
            assert html.count("<h1") == 1, f"{caminho}: deve ter exatamente um H1"

            escrever(caminho, html)
            url = "/" + caminho.replace("index.html", "")
            urls.append(url)
            total += 1
            print(f"  ok  {url:52s} {palavras:>5} palavras")
        print()

    print(f"{total} páginas geradas.")
    return urls


if __name__ == "__main__":
    main()
