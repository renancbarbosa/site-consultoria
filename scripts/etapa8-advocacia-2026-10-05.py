# -*- coding: utf-8 -*-
"""
Etapa 8 do plano de nichos (05/10/2026): advocacia.

/marketing-para-advogados/ vira a principal (gerada por gerar-servicos-marketing.py) e
/para-advogados/ sai do ar com 301 para ela (decisao do Renan na Etapa 0). Este script:
  1. troca todo link href="/para-advogados/" pela principal (menu, rodape, texto) no site e
     nos geradores, para nenhum link interno passar pelo 301;
  2. apaga a pasta para-advogados/ e grava o 301 no _redirects;
  3. sitemap (sai /para-advogados/, entram os 2 artigos), llms.txt e indice do blog.

Idempotente: rode de novo e tem que dizer "alterados: 0".
"""
import glob
import io
import os
import shutil
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = "2026-10-05"
VELHO, NOVO = "/para-advogados/", "/marketing-para-advogados/"
GERADORES = ["scripts/rcb_base.py", "scripts/rcb_menu.py", "scripts/gerar-paginas-cidades.py"]
ARTIGOS = [
    ("como-conseguir-clientes-na-advocacia", "Como conseguir clientes na advocacia sem ferir as regras da OAB",
     "Como conseguir clientes na advocacia",
     "Perfil no Google, página por área de atuação, conteúdo e anúncio — dentro do Provimento 205/2021."),
    ("advogado-pode-fazer-marketing",
     "Advogado pode fazer marketing? O que o Provimento 205/2021 da OAB permite e proíbe",
     "Advogado pode fazer marketing?",
     "O que é permitido, o que é vedado e como ficam o Google, o Instagram e o anúncio."),
]


def ler(rel):
    with io.open(os.path.join(RAIZ, rel), encoding="utf-8", newline="") as f:
        return f.read()


def gravar(rel, txt):
    with io.open(os.path.join(RAIZ, rel), "w", encoding="utf-8", newline="") as f:
        f.write(txt)


def nl(txt):
    return "\r\n" if "\r\n" in txt else "\n"


def card(slug, h, thumb, desc, n):
    return (n.join([
        '            <a href="/blog/%s/" class="blog-card" aria-label="Ler artigo: %s">' % (slug, h),
        '                        <div class="blog-card-thumb" aria-hidden="true">',
        '                          <span class="blog-card-thumb-title">%s</span>' % thumb,
        '                        </div>',
        '                        <div class="blog-card-body">',
        '                          <span class="blog-card-cat">Advocacia</span>',
        '                          <h2 class="blog-card-title">%s</h2>' % h,
        '                          <p class="blog-card-desc">%s</p>' % desc,
        '                          <div class="blog-card-meta">',
        '                            <time datetime="2026-10-05">5 de outubro de 2026</time>',
        '                            <span class="blog-card-link">',
        '                              Ler artigo',
        '                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
        '                            </span>',
        '                          </div>',
        '                        </div>',
        '                      </a>']) + n)


def main():
    alterados, erros = [], []

    # 1. links no site inteiro e nos geradores
    paginas = [os.path.relpath(p, RAIZ).replace(os.sep, "/")
               for p in glob.glob(os.path.join(RAIZ, "**", "index.html"), recursive=True)]
    alvo = [p for p in paginas if not p.startswith(("para-advogados/", "scripts/", "node_modules/"))]
    for rel in alvo + GERADORES:
        t = ler(rel)
        novo = t.replace('href="%s' % VELHO, 'href="%s' % NOVO)
        if rel == "scripts/rcb_menu.py":
            novo = novo.replace('("%s", "Advogados")' % VELHO, '("%s", "Advogados")' % NOVO)
        if novo != t:
            gravar(rel, novo)
            alterados.append(rel)

    # 2. pagina antiga fora do ar + 301
    pasta = os.path.join(RAIZ, "para-advogados")
    if os.path.isdir(pasta):
        shutil.rmtree(pasta)
        alterados.append("para-advogados/ (apagada)")
    r = ler("_redirects")
    n = nl(r)
    r2 = r.replace("/para-advogados.html /para-advogados/ 301", "/para-advogados.html /marketing-para-advogados/ 301")
    bloco = ("# Etapa 8 (05/10/2026): advocacia juntou em /marketing-para-advogados/" + n +
             "/para-advogados/ /marketing-para-advogados/ 301" + n +
             "/para-advogados /marketing-para-advogados/ 301" + n)
    if "/para-advogados/ /marketing-para-advogados/ 301" not in r2:
        r2 = r2.rstrip("\r\n") + n + bloco
    if r2 != r:
        gravar("_redirects", r2)
        alterados.append("_redirects")

    # 3a. sitemap
    sm = ler("sitemap.xml")
    n = nl(sm)
    s2 = sm
    i = s2.find("<loc>https://rcbseo.com.br/para-advogados/</loc>")
    if i >= 0:
        a = s2.rfind("<url>", 0, i)
        a = s2.rfind(n, 0, a)
        b = s2.find("</url>", i) + len("</url>")
        s2 = s2[:a] + s2[b:]
    ancora = "<loc>https://rcbseo.com.br/blog/como-divulgar-empresa-de-limpeza/</loc>"
    for slug, *_ in reversed(ARTIGOS):
        loc = "<loc>https://rcbseo.com.br/blog/%s/</loc>" % slug
        if loc in s2:
            continue
        j = s2.find("</url>", s2.find(ancora)) + len("</url>")
        s2 = s2[:j] + n + n.join(["  <url>", "    " + loc, "    <lastmod>%s</lastmod>" % HOJE,
                                  "    <changefreq>monthly</changefreq>", "    <priority>0.75</priority>",
                                  "  </url>"]) + s2[j:]
    for u in ("marketing-para-advogados/", "trafego-pago-para-advogados/", "criacao-de-site-para-advogado/", "blog/"):
        k = s2.find("<loc>https://rcbseo.com.br/%s</loc>" % u)
        a = s2.find("<lastmod>", k)
        if k < 0 or a > s2.find("</url>", k):
            erros.append("sitemap sem lastmod para %s" % u)
            continue
        b = s2.find("</lastmod>", a)
        s2 = s2[:a] + "<lastmod>" + HOJE + s2[b:]
    if s2 != sm:
        gravar("sitemap.xml", s2)
        alterados.append("sitemap.xml")

    # 3b. llms.txt
    ll = ler("llms.txt")
    n = nl(ll)
    l2 = ll.replace("- SEO para advogados: https://rcbseo.com.br/para-advogados/ — SEO local e presença digital para "
                    "advogados e escritórios, dentro das normas da OAB." + n, "")
    l2 = l2.replace("- Marketing para advogados: https://rcbseo.com.br/marketing-para-advogados/ — Explicação em "
                    "linguagem simples de como advogados são encontrados no Google dentro das normas da OAB.",
                    "- Marketing e SEO para advogados: https://rcbseo.com.br/marketing-para-advogados/ — Google Meu "
                    "Negócio, site por área de atuação e Google Ads para escritórios, dentro do Provimento 205/2021 "
                    "da OAB.")
    secao = n.join([
        "## Advocacia",
        "Marketing e SEO para advogados e escritórios de advocacia (o público é o advogado, não quem procura um "
        "advogado). Escrito com base no Provimento 205/2021 da OAB; o consultor é bacharel em Direito, não advogado.",
        "- Marketing e SEO para advogados (página principal): https://rcbseo.com.br/marketing-para-advogados/ — perfil "
        "do escritório no Google, página por área de atuação, conteúdo informativo e Google Ads para quem já pesquisa.",
        "- Tráfego pago para advogados: https://rcbseo.com.br/trafego-pago-para-advogados/ — Google Ads por área de "
        "atuação, como permite o Anexo Único do Provimento 205/2021.",
        "- Criação de site para advogado: https://rcbseo.com.br/criacao-de-site-para-advogado/ — uma página por área "
        "de atuação, sem promessa de resultado.",
        "- Como conseguir clientes na advocacia: https://rcbseo.com.br/blog/como-conseguir-clientes-na-advocacia/ — "
        "os caminhos permitidos, do perfil no Google à indicação.",
        "- Advogado pode fazer marketing?: https://rcbseo.com.br/blog/advogado-pode-fazer-marketing/ — o que o "
        "Provimento 205/2021 permite e o que proíbe.",
    ]) + n + n
    if "## Advocacia" not in l2:
        k = l2.find("## Conteúdo")
        if k < 0:
            erros.append("llms.txt sem a seção ## Conteúdo")
        else:
            l2 = l2[:k] + secao + l2[k:]
    if "rcbseo.com.br/para-advogados/" in l2:
        erros.append("llms.txt ainda cita /para-advogados/")
    if l2 != ll:
        gravar("llms.txt", l2)
        alterados.append("llms.txt")

    # 3c. índice do blog
    bi = ler("blog/index.html")
    n = nl(bi)
    b2 = bi
    ancora = '<a href="/blog/trafego-pago-para-clinicas/" class="blog-card"'
    for slug, h, thumb, desc in ARTIGOS:
        if 'href="/blog/%s/" class="blog-card"' % slug in b2:
            continue
        k = b2.find(ancora)
        k = b2.rfind(n, 0, k) + len(n)
        b2 = b2[:k] + card(slug, h, thumb, desc, n) + b2[k:]
    if b2 != bi:
        gravar("blog/index.html", b2)
        alterados.append("blog/index.html")

    sobra = [p for p in paginas if os.path.exists(os.path.join(RAIZ, p)) and 'href="%s' % VELHO in ler(p)]
    if sobra:
        erros.append("ainda linkam %s: %s" % (VELHO, sobra[:5]))

    for a in alterados[:8]:
        print("alterado:", a)
    if len(alterados) > 8:
        print("... e mais", len(alterados) - 8)
    print("alterados:", len(alterados))
    for e in erros:
        print("ERRO:", e)
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
