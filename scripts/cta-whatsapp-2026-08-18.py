# -*- coding: utf-8 -*-
"""Troca o botao principal "diagnostico gratuito" por "Falar no WhatsApp".

Decisao do Renan em 18/08/2026: a oferta de diagnostico gratuito e o botao
principal em dezenas de paginas e nao gerou uma unica mensagem em 3 meses.
O botao passa a levar direto ao WhatsApp, com a mensagem ja escrita.

O QUE ESTE SCRIPT **NAO** FAZ, de proposito:
  * nao apaga /diagnostico-presenca-digital/ - a pagina tem 24 impressoes e
    posicao media 16,7 no Search Console (90d), ou seja, tem valor de busca;
  * nao mexe no link do MENU nem no do RODAPE (sitewide, 313 e 294 ocorrencias).
    Sao eles que impedem a pagina de virar orfa depois da troca dos botoes;
  * nao mexe nos links de texto dentro de artigo (classe artigo-link) - sao
    editoriais, nao sao o botao principal;
  * NAO TOCA em /consultor-seo-goiania/ (pagina protegida, 4a posicao organica)
    nem na propria /diagnostico-presenca-digital/.

Alvo: so o botao de acao - classes "btn", "artigo-cta-btn" e "artigo-cta-btn-inline".
Idempotente: um arquivo ja convertido nao tem mais botao apontando para la.
"""
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rcb_pacotes as P

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALVO_ANTIGO = "/diagnostico-presenca-digital/"

# Paginas que ficam de fora. Caminho relativo, com barra normal.
FORA = {
    "consultor-seo-goiania/index.html",       # PROTEGIDA - 4a posicao organica
    "diagnostico-presenca-digital/index.html",
    "diagnostico-presenca-digital/exemplo/index.html",
}

MSG = (u"Olá, Renan! Vi seu site e quero saber como faço para minha empresa "
       u"aparecer no Google.")
WA = P.wa(MSG)

# Textos de botao que viram "Falar no WhatsApp". Ordem: do mais longo para o
# mais curto, senao o curto casa dentro do longo e sobra texto solto.
TEXTOS = [
    u"Solicitar diagnóstico gratuito da minha presença digital",
    u"Solicitar diagnóstico gratuito do meu consultório",
    u"Solicitar diagnóstico gratuito da minha clínica",
    u"Solicitar diagnóstico gratuito do consultório",
    u"Solicitar diagnóstico do projeto",
    u"Solicitar diagnóstico gratuito",
    u"Solicite um diagnóstico gratuito",
    u"Quero meu diagnóstico gratuito",
    u"Peça um diagnóstico gratuito",
    u"Diagnóstico gratuito",
]

TAG = re.compile(r'<a\b[^>]*href="%s"[^>]*>.*?</a>' % re.escape(ALVO_ANTIGO), re.I | re.S)


def eh_botao(tag):
    m = re.search(r'class="([^"]*)"', tag)
    if not m:
        return False
    classes = m.group(1).split()
    return ("btn" in classes or "artigo-cta-btn" in classes
            or "artigo-cta-btn-inline" in classes)


def converter(tag):
    novo = tag.replace('href="%s"' % ALVO_ANTIGO, 'href="%s"' % WA)
    if "target=" not in novo:
        novo = novo.replace("<a ", '<a target="_blank" rel="noopener noreferrer" ', 1)
    # o botao de contorno vira botao de WhatsApp (verde), preservando o resto
    novo = novo.replace('class="btn btn-outline btn-lg"', 'class="btn btn-whatsapp btn-lg"')
    novo = novo.replace('class="btn btn-outline"', 'class="btn btn-whatsapp"')
    for t in TEXTOS:
        novo = novo.replace(t, u"Falar no WhatsApp")
    novo = re.sub(r'aria-label="[^"]*"', 'aria-label="Falar no WhatsApp"', novo)
    return novo


def main():
    total_botoes, arquivos = 0, 0
    detalhe = []
    for caminho in sorted(glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(caminho, RAIZ).replace(os.sep, "/")
        if any(x in rel for x in ("node_modules/", "graphify-out/", "Projetos/", ".playwright")):
            continue
        if rel in FORA:
            continue
        html = io.open(caminho, encoding="utf-8", newline="").read()
        if ALVO_ANTIGO not in html:
            continue
        n = [0]

        def troca(m):
            if eh_botao(m.group(0)):
                n[0] += 1
                return converter(m.group(0))
            return m.group(0)

        novo = TAG.sub(troca, html)
        if n[0]:
            io.open(caminho, "w", encoding="utf-8", newline="").write(novo)
            total_botoes += n[0]
            arquivos += 1
            detalhe.append((rel, n[0]))

    print("botoes trocados : %d" % total_botoes)
    print("arquivos tocados: %d" % arquivos)
    for rel, n in detalhe[:12]:
        print("   %-62s %d" % (rel, n))
    if len(detalhe) > 12:
        print("   ... e mais %d arquivos" % (len(detalhe) - 12))

    # conferencia: a pagina do diagnostico continua alcancavel?
    menu = outros = 0
    for caminho in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True):
        rel = os.path.relpath(caminho, RAIZ).replace(os.sep, "/")
        if any(x in rel for x in ("node_modules/", "graphify-out/", "Projetos/", ".playwright")):
            continue
        h = io.open(caminho, encoding="utf-8", newline="").read()
        for m in TAG.finditer(h):
            if "nav-dropdown-item" in m.group(0):
                menu += 1
            else:
                outros += 1
    print("\nlinks restantes para /diagnostico-presenca-digital/:")
    print("   menu (sitewide)          : %d" % menu)
    print("   rodape e texto de artigo : %d" % outros)
    print("   (a pagina NAO fica orfa)")

    protegida = io.open(os.path.join(RAIZ, "consultor-seo-goiania", "index.html"),
                        encoding="utf-8", newline="").read()
    print("\npagina protegida ainda com os 2 botoes originais? %s (esperado: True)"
          % (protegida.count('class="btn btn-outline" href="%s"' % ALVO_ANTIGO) == 2))


if __name__ == "__main__":
    main()
