# -*- coding: utf-8 -*-
"""
Liga /ferramentas/ (28/10/2026) ao resto do site:

1. RODAPÉ: "Ferramentas de diagnóstico" na linha Blog · Cases · Sobre (fonte única:
   rcb_menu.RODAPE_INSTITUCIONAL). Pula /consultor-seo-goiania/ (página protegida:
   rodapé dela só muda com autorização explícita do Renan).
2. ARTIGOS: bloco "Quer testar agora?" no fim do texto dos 4 artigos que as
   "Dicas RCB" da página citam, logo antes de <div class="artigo-cta-wrap">.
   O texto do artigo não muda. Marcador <!--RCB:FERRAMENTAS-->.
3. sitemap.xml, llms.txt e llms-full.txt ganham a URL.

Idempotente: a 2ª execução diz "alterados: 0". Preserva CRLF.
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rcb_menu  # noqa: E402

RAIZ = os.path.dirname(AQUI)
URL = "https://rcbseo.com.br/ferramentas/"
DATA = "2026-10-28"
PULAR = ("scripts/", "docs/", "data/", "node_modules/", "graphify-out/", ".playwright")
PROTEGIDA = "consultor-seo-goiania/index.html"

ARTIGOS = [
    "blog/como-otimizar-google-perfil-empresa/index.html",
    "blog/site-bonito-nao-aparece-no-google/index.html",
    "blog/por-que-meu-site-nao-aparece-no-google/index.html",
    "blog/erros-que-impedem-empresa-aparecer-no-google/index.html",
]
BLOCO = ('<!--RCB:FERRAMENTAS--><div class="dica-rcb artigo-ferramentas">'
         '<h3>Quer testar agora?</h3>'
         '<p>Use a nossa lista de ferramentas gratuitas para fazer um diagnóstico rápido do seu negócio. '
         '<a href="/ferramentas/">Acessar as ferramentas de diagnóstico</a>.</p>'
         '</div><!--/RCB:FERRAMENTAS-->\r\n        ')

LLMS = ("- Ferramentas grátis para ver sua empresa no Google: %s. Cinco ferramentas oficiais e gratuitas "
        "(Perfil da Empresa, PageSpeed Insights, Search Console, Bing Places e teste de pesquisa aprimorada), "
        "com uma dica de uso para cada uma." % URL)
LLMS_FULL = "* Ferramentas grátis para ver sua empresa no Google: %s" % URL
SITEMAP = ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
           "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n" % (URL, DATA))


def ler(p):
    return io.open(p, encoding="utf-8", newline="").read()


def gravar(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def depois_da_linha(s, contem, nova):
    """Insere `nova` numa linha própria logo depois da 1ª linha que contém `contem`."""
    if nova in s:
        return s
    i = s.index(contem)
    fim = s.index("\n", i) + 1
    return s[:fim] + nova + "\r\n" + s[fim:]


def tem_link_no_rodape(h):
    return "/ferramentas/" in h.split("<!--RCB:INSTITUCIONAL-->", 1)[1].split("<!--/RCB:INSTITUCIONAL-->", 1)[0]


def main():
    alterados, sem_rodape = [], []
    for raiz, _, arqs in os.walk(RAIZ):
        for a in arqs:
            if not a.endswith(".html"):
                continue
            p = os.path.join(raiz, a)
            rel = os.path.relpath(p, RAIZ).replace("\\", "/")
            if rel.startswith(PULAR) or rel == PROTEGIDA:
                continue
            h0 = ler(p)
            h = h0
            if "<!--RCB:INSTITUCIONAL-->" in h:
                if not tem_link_no_rodape(h):
                    h = rcb_menu._institucional(h)
            elif 'role="contentinfo"' in h:
                sem_rodape.append(rel)
            if rel in ARTIGOS and "RCB:FERRAMENTAS" not in h:
                alvo = '<div class="artigo-cta-wrap">'
                assert h.count(alvo) == 1, rel
                h = h.replace(alvo, BLOCO + alvo, 1)
            if h != h0:
                assert h.lstrip().startswith("<!DOCTYPE"), rel
                gravar(p, h)
                alterados.append(rel)

    sp = os.path.join(RAIZ, "sitemap.xml")
    s = ler(sp)
    if "<loc>%s</loc>" % URL not in s:
        gravar(sp, s.replace("</urlset>", SITEMAP + "</urlset>", 1))
        alterados.append("sitemap.xml")
    for nome, contem, linha in (("llms.txt", "- Guia de SEO Local (índice editorial)", LLMS),
                                ("llms-full.txt", "* Guia de SEO local:", LLMS_FULL)):
        p = os.path.join(RAIZ, nome)
        s0 = ler(p)
        s = depois_da_linha(s0, contem, linha)
        if s != s0:
            gravar(p, s)
            alterados.append(nome)

    print("alterados:", len(alterados))
    for a in alterados:
        if not a.endswith("index.html") or a in ARTIGOS:
            print("  ", a)
    print("com rodape mas sem a linha Blog/Cases/Sobre:", sem_rodape)


if __name__ == "__main__":
    main()
