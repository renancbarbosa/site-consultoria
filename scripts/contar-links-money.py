# -*- coding: utf-8 -*-
"""
Conta links internos EDITORIAIS para as money pages, separando por origem.

Uso:  python scripts/contar-links-money.py

Por que separar: depois da poda de 12/08/2026, 168 páginas de cidade carregam
noindex. Elas continuam linkando para as money pages — o link segue útil para
quem lê e o Google continua rastreando —, mas contar esses links como
"autoridade interna" mascara a força estrutural real do site. Este script mostra
os dois números lado a lado.

Editorial = fora da navbar, do rodapé e da barra fixa de CTA. São os blocos que
se repetem em todas as páginas e que não representam escolha editorial.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.join(AQUI, "..")

from rcb_cidades import eh_indexavel  # noqa: E402

ALVOS = [
    "/consultoria-seo-local/",
    "/google-perfil-empresa/",
    "/cases/",
    "/seo-local-goiania/",
    "/consultor-seo-goiania/",
    "/diagnostico-presenca-digital/",
]

IGNORAR_DIRS = {"node_modules", "graphify-out", "Projetos", ".git", "docs", "scripts", "assets"}


def corpo_editorial(html):
    """Remove navbar, rodape, barra de CTA e o botao flutuante."""
    h = re.sub(r"<nav class=\"navbar\".*?</nav>", " ", html, flags=re.S)
    h = re.sub(r"<footer.*?</footer>", " ", h, flags=re.S)
    h = re.sub(r"<div class=\"cta-mobile\".*?</div>\s*</div>", " ", h, flags=re.S)
    h = re.sub(r"<a[^>]*class=\"whatsapp-float\".*?</a>", " ", h, flags=re.S)
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S | re.I)
    return h


def paginas():
    for pasta, subs, arqs in os.walk(RAIZ):
        subs[:] = [s for s in subs if s not in IGNORAR_DIRS]
        for nome in arqs:
            if not nome.endswith(".html"):
                continue
            caminho = os.path.join(pasta, nome)
            rel = os.path.relpath(caminho, RAIZ).replace("\\", "/")
            if rel == "404.html" or "diagnostico-presenca-digital/exemplo" in rel:
                continue
            yield rel, caminho


def origem(rel):
    if rel.startswith("consultoria-seo/") and rel != "consultoria-seo/index.html":
        slug = rel[len("consultoria-seo/"):-len("/index.html")]
        return "cidade_indexavel" if eh_indexavel(slug) else "cidade_noindex"
    return "resto_do_site"


def main():
    contagem = {alvo: {"cidade_indexavel": 0, "cidade_noindex": 0, "resto_do_site": 0}
                for alvo in ALVOS}

    for rel, caminho in paginas():
        with open(caminho, encoding="utf-8") as f:
            h = corpo_editorial(f.read())
        hrefs = re.findall(r'href="([^"]+)"', h)
        o = origem(rel)
        for alvo in ALVOS:
            if rel == alvo.strip("/") + "/index.html":
                continue  # nao conta auto-link
            contagem[alvo][o] += sum(1 for x in hrefs if x == alvo)

    larg = max(len(a) for a in ALVOS)
    print(f"{'money page':<{larg}}  {'indexaveis':>11}  {'noindex':>8}  {'total bruto':>11}")
    print("-" * (larg + 38))
    for alvo in ALVOS:
        c = contagem[alvo]
        real = c["resto_do_site"] + c["cidade_indexavel"]
        total = real + c["cidade_noindex"]
        print(f"{alvo:<{larg}}  {real:>11}  {c['cidade_noindex']:>8}  {total:>11}")
    print()
    print("indexaveis  = resto do site + as 31 cidades que continuam no indice")
    print("noindex     = as 168 cidades podadas (nao contam como autoridade interna)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
