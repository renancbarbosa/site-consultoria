# -*- coding: utf-8 -*-
"""Gera e valida os artigos de intenção leiga sobre visibilidade no Google."""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))

from rcb_base import escrever, contar_palavras  # noqa: E402
from rcb_artigo import render_artigo            # noqa: E402
from artigos_visibilidade_google import ARTIGOS  # noqa: E402

MIN_PALAVRAS = 1000


def remover_navegacao_ainda_nao_publicada(html):
    """Não exibe no lote local a seção nacional cujas páginas ainda não existem."""
    html = re.sub(
        r'<li class="nav-nicho-group"><button[^>]*>SEO Nacional.*?</div></li>',
        "",
        html,
        count=1,
        flags=re.S,
    )
    return re.sub(
        r'<div class="footer-col"><h4 class="footer-col-title">SEO Nacional</h4>.*?</nav></div>',
        "",
        html,
        count=1,
        flags=re.S,
    )


def main():
    vistos = set()
    for artigo in ARTIGOS:
        slug = artigo["slug"]
        assert slug not in vistos, f"slug duplicado: {slug}"
        vistos.add(slug)

        caminho, html = render_artigo(artigo)
        html = remover_navegacao_ainda_nao_publicada(html)
        corpo = html.split('<article class="artigo-body">')[-1].split("</article>")[0]
        palavras = contar_palavras(corpo)
        assert palavras >= MIN_PALAVRAS, f"{slug}: raso demais ({palavras} palavras)"
        assert html.count("<h1") == 1, f"{slug}: deve ter exatamente um H1"
        for proibido in ("TODO", "Lorem ipsum", "PLACEHOLDER", "[[", "XXX"):
            assert proibido not in html, f"{slug}: contém marcador '{proibido}'"

        escrever(caminho, html)
        print(f"ok  {slug}  {palavras} palavras")


if __name__ == "__main__":
    main()
