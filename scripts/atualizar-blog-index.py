# -*- coding: utf-8 -*-
"""
Integra os artigos dos clusters novos ao índice do blog (/blog/).

Uso:  python scripts/atualizar-blog-index.py

Cria dois agrupamentos novos no padrão .blog-cluster já existente:
  #mercados-competitivos   — IPTV, bets, iGaming, projetos nacionais
  #dominios-autoridade     — domínios, migração, backlinks

Decisão do plano (§5): as categorias funcionam como agrupamento no índice e
metadado no artigo. Não existem páginas de categoria indexáveis próprias —
com poucos artigos por categoria, elas seriam páginas fracas.

Idempotente: remove os blocos gerados antes de reinseri-los.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))

from rcb_base import RAIZ  # noqa: E402
from rcb_artigo import data_br  # noqa: E402

import artigos_competitivo, artigos_estrategia, artigos_dominios  # noqa: E402
import artigos_backlinks, artigos_iptv, artigos_bets              # noqa: E402

MARCA_INI = "<!-- RCB:CLUSTERS-NACIONAIS:INICIO -->"
MARCA_FIM = "<!-- RCB:CLUSTERS-NACIONAIS:FIM -->"
MARCA_TOC_INI = "<!-- RCB:TOC-NACIONAIS:INICIO -->"
MARCA_TOC_FIM = "<!-- RCB:TOC-NACIONAIS:FIM -->"

# Ordem editorial dentro de cada agrupamento: do mais comercial para o mais conceitual.
GRUPOS = [
    ("mercados-competitivos", "SEO para mercados competitivos",
     "Projetos nacionais em nichos de alta concorrência: IPTV e streaming, bets e iGaming, "
     "e o que muda quando a disputa deixa de ser local.",
     artigos_iptv.ARTIGOS + artigos_bets.ARTIGOS + artigos_estrategia.ARTIGOS
     + artigos_competitivo.ARTIGOS),
    ("dominios-autoridade", "Domínios, autoridade e link building",
     "Domínio expirado, migração de domínio, backlinks e recuperação de tráfego — as decisões "
     "técnicas que mais impactam projetos competitivos.",
     artigos_dominios.ARTIGOS + artigos_backlinks.ARTIGOS),
]

SVG = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
       'stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>')


def card(a):
    return f"""            <a href="/blog/{a['slug']}/" class="blog-card" aria-label="Ler artigo: {a['h1']}">
                        <div class="blog-card-thumb" aria-hidden="true">
                          <span class="blog-card-thumb-title">{a['h1']}</span>
                        </div>
                        <div class="blog-card-body">
                          <span class="blog-card-cat">{a['cat']}</span>
                          <h2 class="blog-card-title">{a['h1']}</h2>
                          <p class="blog-card-desc">{a['desc']}</p>
                          <div class="blog-card-meta">
                            <time datetime="{a['data']}">{data_br(a['data'])}</time>
                            <span class="blog-card-link">
                              Ler artigo
                              {SVG}
                            </span>
                          </div>
                        </div>
                      </a>"""


def cluster(id_, titulo, desc, artigos):
    cards = "\n".join(card(a) for a in artigos)
    return f"""
        <div class="blog-cluster" id="{id_}">
          <div class="section-header">
            <div class="section-tag">{len(artigos)} artigos</div>
            <h2 class="section-title">{titulo}</h2>
            <p class="section-desc">{desc}</p>
          </div>
          <div class="blog-grid-section">
            <div class="blog-grid">
{cards}
            </div>
          </div>
        </div>
"""


def limpar(html, ini, fim):
    """Remove um bloco marcado, se existir, para o script poder rodar de novo."""
    while ini in html and fim in html:
        a = html.index(ini)
        b = html.index(fim) + len(fim)
        html = html[:a] + html[b:]
    return html


def main():
    caminho = os.path.join(RAIZ, "blog", "index.html")
    html = open(caminho, encoding="utf-8").read()

    html = limpar(html, MARCA_INI, MARCA_FIM)
    html = limpar(html, MARCA_TOC_INI, MARCA_TOC_FIM)

    # --- índice de seções ---
    toc = (MARCA_TOC_INI
           + '\n          <a href="#mercados-competitivos">SEO para mercados competitivos</a>'
           + '\n          <a href="#dominios-autoridade">Domínios, autoridade e link building</a>\n        '
           + MARCA_TOC_FIM)
    ancora_toc = '          <a href="#nichos">Nichos e tipos de negócio</a>\n'
    assert ancora_toc in html, "âncora do índice de seções não encontrada"
    html = html.replace(ancora_toc, ancora_toc + toc + "\n", 1)

    # --- clusters ---
    # A âncora é só o fechamento da <section>, sem o </div> anterior: assim o
    # texto removido por limpar() é exatamente o que foi inserido, e o script
    # pode rodar quantas vezes for preciso sem deslocar a estrutura.
    blocos = MARCA_INI + "".join(cluster(*g) for g in GRUPOS) + MARCA_FIM
    ancora_fim = "\n    </section>\n\n  </main>"
    assert ancora_fim in html, "âncora do fim dos clusters não encontrada"
    html = html.replace(ancora_fim, blocos + ancora_fim, 1)

    with open(caminho, "w", encoding="utf-8", newline="") as f:
        f.write(html)

    total = sum(len(g[3]) for g in GRUPOS)
    print(f"Índice do blog atualizado: {len(GRUPOS)} agrupamentos, {total} artigos listados.")
    for id_, titulo, _, arts in GRUPOS:
        print(f"  #{id_:24s} {len(arts):>2} artigos — {titulo}")


if __name__ == "__main__":
    main()
