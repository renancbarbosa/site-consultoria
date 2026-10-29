# -*- coding: utf-8 -*-
"""
Fase 5 do pilar SEO para IA (29/10/2026): a fonte Inter passa a vir do próprio site.

Medido antes (Lighthouse 13.4.1, celular, 2 rodadas, /criacao-de-sites-goiania/ e /ferramentas/,
que usam o mesmo esqueleto das páginas novas): nota 72 a 74, LCP 4,7 a 4,9 s, CLS 0,113.
Causa: o texto do topo (o maior elemento da tela) era pintado de novo quando a Inter chegava do
Google Fonts, 1,4 s depois; e a troca de fonte mudava a altura das linhas e empurrava os botões.

O que muda:
  1. assets/fonts/inter-latin.woff2: o arquivo oficial do Google Fonts (Inter v20, variável 400 a
     800, só o subconjunto latino, que cobre o português). 48 KB. Licença SIL Open Font.
  2. styles.css: @font-face da Inter local + uma "Inter Fallback" (Arial com as medidas ajustadas
     às da Inter). Enquanto a Inter não chega, o texto já ocupa o mesmo espaço: nada pula.
  3. Em todo HTML e nos 2 geradores com <head> próprio (rcb_base.py, gerar-paginas-cidades.py):
     as 5 linhas do Google Fonts viram 1 linha de preload do arquivo local.

Depois: python scripts/auditoria-2026-09-08.py --css (regera o styles.min.css).
/consultor-seo-goiania/ (protegida) fica de fora: continua carregando do Google Fonts.
Idempotente. Sem argumento só relata; --aplicar grava.
"""
import glob
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
APLICAR = "--aplicar" in sys.argv
PROTEGIDA = os.path.join("consultor-seo-goiania", "index.html")  # continua com o Google Fonts
FORA = ("node_modules", "docs", "scripts", "graphify-out", "Projetos", "reports", "data", ".playwright-mcp")

GF = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
LINHAS = [
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
    '<link rel="preload" as="style" href="%s">' % GF,
    '<link href="%s" rel="stylesheet" media="print" onload="this.media=\'all\'">' % GF,
    '<noscript><link href="%s" rel="stylesheet"></noscript>' % GF,
]
BLOCO = re.compile(r"\r?\n[ \t]*".join(re.escape(x) for x in LINHAS))
PRELOAD = '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>'

CSS_MARCA = "/* RCB:FONTE-LOCAL */"
CSS = CSS_MARCA + """
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400 800;
  font-display: swap;
  src: url(/assets/fonts/inter-latin.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* Arial com as medidas da Inter: o texto ocupa o mesmo espaço antes e depois da troca */
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  ascent-override: 90.2%;
  descent-override: 22.48%;
  line-gap-override: 0%;
  size-adjust: 107.4%;
}
/* /RCB:FONTE-LOCAL */
"""
FONT_VELHO = "--font: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;"
FONT_NOVO = "--font: 'Inter', 'Inter Fallback', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;"


def main():
    os.chdir(RAIZ)
    alterados = []
    alvos = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(FORA) and os.path.normpath(f) != PROTEGIDA]
    alvos += [os.path.join("scripts", "rcb_base.py"), os.path.join("scripts", "gerar-paginas-cidades.py")]
    for f in sorted(alvos):
        t = io.open(f, encoding="utf-8").read()
        novo = BLOCO.sub(PRELOAD, t)
        if "fonts.googleapis.com" in novo and f.endswith(".html"):
            print("  sobrou Google Fonts (formato diferente):", f)
        if novo != t:
            if f.endswith(".html"):
                assert novo.lstrip().lower().startswith("<!doctype"), f
            alterados.append(f)
            if APLICAR:
                io.open(f, "w", encoding="utf-8", newline="").write(novo)
    t = io.open("styles.css", encoding="utf-8").read()
    if CSS_MARCA not in t:
        assert t.count(FONT_VELHO) == 1
        t = CSS + "\n" + t.replace(FONT_VELHO, FONT_NOVO)
        alterados.append("styles.css")
        if APLICAR:
            io.open("styles.css", "w", encoding="utf-8", newline="").write(t)
    print("%s: %d" % ("alterados" if APLICAR else "seriam alterados", len(alterados)))


if __name__ == "__main__":
    main()
