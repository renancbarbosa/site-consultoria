# -*- coding: utf-8 -*-
"""
Conferencia do site depois da rodada de conversao de 09/08/2026.

Roda sobre TODAS as paginas e checa: HTML balanceado, JSON-LD valido, links
internos e ancoras que existem, preco coerente entre texto e ficha do Google,
barra de CTA no celular, menu novo e ausencia de jargao e de frases que
contradizem o preco publicado.

Uso:  python scripts/conferir-conversao.py
"""
import glob
import json
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
os.chdir(RAIZ)

JARGAO = ["GMB", "on-page", "metadescri", "arquitetura de informa",
          "ticket médio", "métricas de vaidade", "escopo enxuto"]
CONTRADICAO = ["investimento depende", "faixas de investimento",
               "proposta personalizada", "não existe preço de tabela"]

SEM_NAVBAR = {"404.html", "diagnostico-presenca-digital/exemplo/index.html",
              "privacidade/index.html", "cookies/index.html"}

# Demo do relatorio de diagnostico: o HTML dela e montado por JavaScript, entao
# contar tag aberta/fechada no arquivo nao faz sentido. E noindex e fora do
# sitemap de proposito - ver CLAUDE.md.
FORA_DA_CONFERENCIA = {"diagnostico-presenca-digital/exemplo/index.html"}

problemas = []
stats = {"paginas": 0, "com_precos": 0, "com_barra": 0, "com_menu_novo": 0}

paginas = sorted(f.replace(os.sep, "/") for f in glob.glob("**/index.html", recursive=True)
                 if "node_modules" not in f)
paginas.append("404.html")

for rel in paginas:
    if rel in FORA_DA_CONFERENCIA:
        continue
    h = Path(rel).read_text(encoding="utf-8")
    stats["paginas"] += 1

    # HTML balanceado
    for tag in ("section", "div", "article", "ul", "ol", "li", "p", "main", "nav", "footer"):
        a = len(re.findall(r"<" + tag + r"[\s>]", h))
        f_ = len(re.findall(r"</" + tag + r">", h))
        if a != f_:
            problemas.append("%s: <%s> abre %d fecha %d" % (rel, tag, a, f_))

    # JSON-LD valido
    for i, b in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)):
        try:
            json.loads(b)
        except ValueError as e:
            problemas.append("%s: JSON-LD %d invalido (%s)" % (rel, i, str(e)[:50]))

    # ancoras internas existem
    ids = set(re.findall(r'id="([^"]+)"', h))
    orfas = sorted(a for a in set(re.findall(r'href="#([^"]+)"', h)) if a and a not in ids)
    if orfas:
        problemas.append("%s: ancora sem destino: %s" % (rel, orfas))

    # links internos existem
    for l in sorted(set(re.findall(r'href="(/[^"#?]*)"', h))):
        alvo = l.strip("/")
        if not alvo:
            continue
        if not any(Path(c).exists() for c in (alvo, alvo + "/index.html", alvo + ".html")):
            problemas.append("%s: link quebrado -> %s" % (rel, l))

    # preco coerente entre texto e ficha do Google
    # So paginas com a TABELA de pacotes precisam dos tres valores nos dois
    # lugares. Citar "a partir de R$ 997" no meio de um texto e legitimo.
    tem_tabela = "RCB:PACOTES:INICIO" in h
    if tem_tabela:
        stats["com_precos"] += 1
        for v in ("R$ 997", "R$ 1.497", "R$ 2.497", "997.00", "1497.00", "2497.00"):
            if v not in h:
                problemas.append("%s: tem a tabela mas falta o valor %s" % (rel, v))
    elif "997.00" in h and "R$ 997" not in h:
        problemas.append("%s: preco no schema sem preco no texto" % rel)

    # barra do celular e menu novo
    if rel not in SEM_NAVBAR:
        if 'class="cta-mobile"' in h:
            stats["com_barra"] += 1
        else:
            problemas.append("%s: sem barra de CTA no celular" % rel)
        if ">Ver preços<" in h:
            stats["com_menu_novo"] += 1
        elif "nav-cta" in h:
            problemas.append("%s: menu ainda com o botao antigo" % rel)
        if 'class="cta-mobile"' in h and "tem-cta-mobile" not in h:
            problemas.append("%s: barra existe mas o body nao tem a classe" % rel)

    # texto visivel: jargao e contradicao
    corpo = h[h.find("<main"): h.find("</main>")] if "<main" in h else h
    visivel = re.sub(r"<[^>]+>", " ", corpo)
    for j in JARGAO:
        if j.lower() in visivel.lower():
            problemas.append("%s: jargao '%s'" % (rel, j))
    for c in CONTRADICAO:
        if c.lower() in h.lower():
            problemas.append("%s: contradiz o preco ('%s')" % (rel, c))

# llms.txt
llms = Path("llms.txt").read_text(encoding="utf-8")
if "R$ 997" not in llms:
    problemas.append("llms.txt: sem a tabela de precos")

# sitemap x arquivos
mapa = Path("sitemap.xml").read_text(encoding="utf-8")
urls = re.findall(r"<loc>https://rcbseo\.com\.br/(.*?)</loc>", mapa)
for u in urls:
    alvo = u.strip("/")
    if alvo and not any(Path(c).exists() for c in (alvo, alvo + "/index.html", alvo + ".html")):
        problemas.append("sitemap: aponta para pagina que nao existe -> /%s" % u)

print("paginas conferidas      :", stats["paginas"])
print("com tabela de precos    :", stats["com_precos"])
print("com barra no celular    :", stats["com_barra"])
print("com o menu novo         :", stats["com_menu_novo"])
print("URLs no sitemap         :", len(urls))
print()
if problemas:
    print("PROBLEMAS (%d):" % len(problemas))
    for x in problemas[:60]:
        sys.stdout.buffer.write(("  - " + x + "\n").encode("utf-8", "replace"))
    if len(problemas) > 60:
        print("  ... e mais %d" % (len(problemas) - 60))
    sys.exit(1)
print("Nenhum problema encontrado.")
