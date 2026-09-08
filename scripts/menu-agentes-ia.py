# -*- coding: utf-8 -*-
"""Liga a linha "Agentes de IA" ao resto do site: item no menu e coluna no rodape.

Complemento de gerar-agentes-ia.py. Sem ele as 3 paginas ficam orfas.

O que faz, em toda pagina com navbar:
  1. Insere o dropdown "Agentes de IA" no menu, logo antes do item "Blog".
  2. Insere a coluna "Agentes de IA" no rodape, logo antes da coluna de contato.

Trabalha por INSERCAO com marcador, nao por substituicao do bloco inteiro:
cada pagina tem seu proprio menu (o data-page do CTA muda) e seu proprio rodape
(bio e nichos mudam). Reescrever o bloco todo apagaria essas diferencas.

Idempotente: se o marcador ja existe, o conteudo dele e atualizado no lugar.
Rodar duas vezes seguidas tem que dizer "alteradas: 0" na segunda.

Tres formatos de rodape convivem no site e os tres sao tratados:
  * footer-cols em linha unica  -> maioria das paginas
  * footer-cols indentado       -> os 72 artigos do blog ("Contato Direto")
  * footer-grid                 -> so a home, com <h4> sem classe e <ul><li>

Uso: python scripts/menu-agentes-ia.py [--aplicar]
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FORA = {
    os.path.join(RAIZ, "404.html"),
    os.path.join(RAIZ, "diagnostico-presenca-digital", "exemplo", "index.html"),
}

PAGINAS = [
    ("/agentes-de-ia/", u"Agentes de IA no WhatsApp", u"O que são agentes de IA"),
    ("/agente-de-ia-para-clinicas/", u"Agente de IA para clínicas", u"Para clínicas"),
    ("/recuperacao-de-vendas-whatsapp/", u"Recuperação de vendas no WhatsApp", u"Recuperar vendas"),
]

CHEVRON = ('<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" '
           'stroke="currentColor" stroke-width="2.5" aria-hidden="true">'
           '<polyline points="6 9 12 15 18 9"/></svg>')

NAV_ABRE, NAV_FECHA = "<!--RCB:AGENTES-NAV-->", "<!--/RCB:AGENTES-NAV-->"
FOOT_ABRE, FOOT_FECHA = "<!--RCB:AGENTES-FOOTER-->", "<!--/RCB:AGENTES-FOOTER-->"

NAV_HTML = (
    NAV_ABRE
    + '<li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" '
      'aria-haspopup="true">Agentes de IA' + CHEVRON + '</button>'
      '<div class="nav-dropdown-menu" role="menu">'
    + "".join('<a href="%s" class="nav-dropdown-item" role="menuitem">%s</a>' % (u, curto)
              for u, _longo, curto in PAGINAS)
    + "</div></li>"
    + NAV_FECHA
)

FOOT_COLS_HTML = (
    FOOT_ABRE
    + '<div class="footer-col"><h4 class="footer-col-title">Agentes de IA</h4>'
      '<nav class="footer-col-nav">'
    + "".join('<a href="%s">%s</a>' % (u, longo) for u, longo, _c in PAGINAS)
    + "</nav></div>"
    + FOOT_FECHA
)

FOOT_GRID_HTML = (
    FOOT_ABRE
    + '<div class="footer-col"><h4>Agentes de IA</h4><ul>'
    + "".join('<li><a href="%s">%s</a></li>' % (u, longo) for u, longo, _c in PAGINAS)
    + "</ul></div>"
    + FOOT_FECHA
)

ANCORA_NAV = '<li><a href="/blog/" class="nav-link">Blog</a></li>'
# coluna de contato do rodape, nos tres formatos (aceita "Contato" e "Contato Direto")
ANCORA_FOOT = re.compile(
    r'<div class="footer-col">\s*<h4(?: class="footer-col-title")?>\s*Contato'
)


def bloco(texto, abre, fecha):
    i = texto.find(abre)
    if i < 0:
        return None
    j = texto.find(fecha, i)
    return (i, j + len(fecha)) if j >= 0 else None


def aplicar_em(texto, foot_html):
    """Devolve (texto_novo, o_que_mudou)."""
    mudou = []

    # ---- menu ----
    pos = bloco(texto, NAV_ABRE, NAV_FECHA)
    if pos:
        if texto[pos[0]:pos[1]] != NAV_HTML:
            texto = texto[:pos[0]] + NAV_HTML + texto[pos[1]:]
            mudou.append("menu(atualizado)")
    elif ANCORA_NAV in texto:
        texto = texto.replace(ANCORA_NAV, NAV_HTML + ANCORA_NAV, 1)
        mudou.append("menu")

    # ---- rodape ----
    pos = bloco(texto, FOOT_ABRE, FOOT_FECHA)
    if pos:
        if texto[pos[0]:pos[1]] != foot_html:
            texto = texto[:pos[0]] + foot_html + texto[pos[1]:]
            mudou.append("rodape(atualizado)")
    else:
        m = ANCORA_FOOT.search(texto)
        if m:
            texto = texto[:m.start()] + foot_html + texto[m.start():]
            mudou.append("rodape")

    return texto, mudou


def main():
    aplicar = "--aplicar" in sys.argv
    alteradas, sem_ancora = [], []

    for root, _dirs, files in os.walk(RAIZ):
        if ".git" in root or "node_modules" in root or "graphify-out" in root:
            continue
        for nome in files:
            if not nome.endswith(".html"):
                continue
            caminho = os.path.join(root, nome)
            if caminho in FORA:
                continue
            texto = io.open(caminho, encoding="utf-8").read()
            if "nav-menu" not in texto:
                continue
            foot_html = FOOT_GRID_HTML if "footer-grid" in texto else FOOT_COLS_HTML
            novo, mudou = aplicar_em(texto, foot_html)
            if NAV_ABRE not in novo or FOOT_ABRE not in novo:
                sem_ancora.append((os.path.relpath(caminho, RAIZ),
                                   "menu" if NAV_ABRE not in novo else "rodape"))
            if mudou:
                alteradas.append((os.path.relpath(caminho, RAIZ), mudou))
                if aplicar:
                    io.open(caminho, "w", encoding="utf-8", newline="").write(novo)

    print("paginas alteradas:", len(alteradas))
    for p, m in alteradas[:5]:
        print("   ", p, m)
    if len(alteradas) > 5:
        print("    ... e mais", len(alteradas) - 5)
    if sem_ancora:
        print("SEM ANCORA (nao receberam):", len(sem_ancora))
        for p, o in sem_ancora[:10]:
            print("   ", p, "->", o)
    if not aplicar:
        print("\n(modo relatorio - rode com --aplicar para gravar)")


if __name__ == "__main__":
    main()
