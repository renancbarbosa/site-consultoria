# -*- coding: utf-8 -*-
"""
Liga as 8 páginas "serviço + nicho" (28/09/2026) ao resto do site.

  1. sitemap.xml: +8 URLs
  2. Páginas de SEO por nicho (dentistas, advogados, contadores, estética,
     imobiliárias): bloco "Site e anúncios para o seu ramo" antes do FAQ,
     com marcador <!-- RCB:SERVICOS-NICHO --> (idempotente).
  3. /criacao-de-sites-goiania/: cartões dos 4 "site para X" no "Leia também".
  4. Módulos de conteúdo (sobrevivem à regeração):
     - servicos_marketing.py: "Leia também" da página de tráfego pago aponta
       para as 4 versões por nicho;
     - artigos_nichos_anuncios.py: artigos de energia solar e de clínicas
       apontam para as páginas de nicho.
Depois de rodar: python scripts/gerar-servicos-marketing.py
                 python scripts/gerar-artigos-sites.py
"""
import io
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

NOVAS = ["criacao-de-site-para-dentista", "criacao-de-site-para-advogado", "criacao-de-site-para-contador",
         "criacao-de-site-para-clinica-de-estetica", "trafego-pago-para-dentistas", "trafego-pago-para-advogados",
         "trafego-pago-para-energia-solar", "trafego-pago-para-imobiliarias"]

BLOCOS = {
    "seo-para-dentistas": [
        ("/criacao-de-site-para-dentista/", "Site para dentista", "Uma página por tratamento, feita para aparecer no Google."),
        ("/trafego-pago-para-dentistas/", "Tráfego pago para dentistas", "Google Ads e Meta Ads dentro das regras do CFO."),
    ],
    "para-advogados": [
        ("/criacao-de-site-para-advogado/", "Site para advogado", "Uma página por área de atuação, dentro da OAB."),
        ("/trafego-pago-para-advogados/", "Tráfego pago para advogados", "Google Ads dentro do Provimento 205/2021."),
    ],
    "seo-para-contadores": [
        ("/criacao-de-site-para-contador/", "Site para contador", "Página por serviço para captar empresas pelo Google."),
    ],
    "seo-para-clinicas-de-estetica": [
        ("/criacao-de-site-para-clinica-de-estetica/", "Site para clínica de estética", "Uma página por procedimento, com fotos reais."),
        ("/blog/trafego-pago-para-clinicas/", "Tráfego pago para clínicas", "Anúncio no Google e no Instagram dentro das regras."),
    ],
    "seo-para-imobiliarias": [
        ("/trafego-pago-para-imobiliarias/", "Tráfego pago para imobiliárias", "Leads próprios sem depender de portal."),
    ],
}

MARCA = "<!-- RCB:SERVICOS-NICHO -->"


def ler(p):
    return io.open(p, encoding="utf-8", newline="").read()


def gravar(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def troca_unica(p, velho, novo, ja):
    s = ler(p)
    if ja in s:
        return False
    assert s.count(velho) == 1, (p.name, velho[:60], s.count(velho))
    gravar(p, s.replace(velho, novo, 1))
    return True


def main():
    feito = []

    # 1. sitemap
    p = RAIZ / "sitemap.xml"
    s = ler(p)
    nl = "\r\n" if "\r\n" in s else "\n"
    faltam = [u for u in NOVAS if "/%s/</loc>" % u not in s]
    if faltam:
        urls = "".join(("  <url>" + nl + "    <loc>https://rcbseo.com.br/%s/</loc>" + nl
                        + "    <lastmod>2026-09-28</lastmod>" + nl + "    <changefreq>monthly</changefreq>" + nl
                        + "    <priority>0.8</priority>" + nl + "  </url>" + nl) % u for u in faltam)
        ancora = "  <url>" + nl + "    <loc>https://rcbseo.com.br/criacao-de-sites-goiania/</loc>"
        assert s.count(ancora) == 1
        gravar(p, s.replace(ancora, urls + ancora, 1))
        feito.append("sitemap +%d" % len(faltam))

    # 2. paginas de SEO por nicho: bloco antes do FAQ
    for slug, itens in BLOCOS.items():
        p = RAIZ / slug / "index.html"
        s = ler(p)
        if MARCA in s:
            continue
        cards = "".join('\n          <a class="cluster-card" href="%s"><h3>%s</h3><p>%s</p></a>' % i for i in itens)
        bloco = ('%s\n    <section class="cluster-section">\n      <div class="container">\n'
                 '        <div class="section-header">\n          <div class="section-tag">Site e anúncios</div>\n'
                 '          <h2 class="section-title">Site e anúncios para o seu ramo</h2>\n        </div>\n'
                 '        <div class="cluster-grid">%s\n        </div>\n      </div>\n    </section>\n\n    '
                 % (MARCA, cards))
        ancora = '<section class="faq-section"'
        assert s.count(ancora) == 1, (slug, s.count(ancora))
        gravar(p, s.replace(ancora, bloco + ancora, 1))
        feito.append(slug)

    # 3. criacao de sites: cartoes "site para X"
    if troca_unica(RAIZ / "criacao-de-sites-goiania" / "index.html",
                   '          <a class="cluster-card" href="/blog/quanto-custa-um-site/">',
                   '          <a class="cluster-card" href="/criacao-de-site-para-dentista/"><h3>Site para dentista</h3><p>Uma página por tratamento.</p></a>\n'
                   '          <a class="cluster-card" href="/criacao-de-site-para-advogado/"><h3>Site para advogado</h3><p>Por área de atuação, dentro da OAB.</p></a>\n'
                   '          <a class="cluster-card" href="/criacao-de-site-para-contador/"><h3>Site para contador</h3><p>Para captar empresas pelo Google.</p></a>\n'
                   '          <a class="cluster-card" href="/criacao-de-site-para-clinica-de-estetica/"><h3>Site para estética</h3><p>Uma página por procedimento.</p></a>\n'
                   '          <a class="cluster-card" href="/blog/quanto-custa-um-site/">',
                   'href="/criacao-de-site-para-dentista/"><h3>Site para dentista'):
        feito.append("criacao-de-sites-goiania")

    # 4a. pagina de trafego pago: "Leia tambem" com as 4 versoes por nicho
    m = RAIZ / "scripts" / "conteudo" / "servicos_marketing.py"
    if troca_unica(m,
                   '            ("/blog/quanto-investir-em-trafego-pago/", "Quanto investir em tráfego pago",',
                   '            ("/trafego-pago-para-dentistas/", "Tráfego pago para dentistas", "Google Ads e Meta Ads dentro das regras do CFO."),\n'
                   '            ("/trafego-pago-para-advogados/", "Tráfego pago para advogados", "Google Ads dentro do Provimento 205/2021 da OAB."),\n'
                   '            ("/trafego-pago-para-energia-solar/", "Tráfego pago para energia solar", "Pedidos de orçamento sem clique de curioso."),\n'
                   '            ("/trafego-pago-para-imobiliarias/", "Tráfego pago para imobiliárias", "Leads próprios sem depender de portal."),\n'
                   '            ("/blog/quanto-investir-em-trafego-pago/", "Quanto investir em tráfego pago",',
                   '"/trafego-pago-para-dentistas/", "Tráfego pago para dentistas"'):
        feito.append("servicos_marketing.py")

    # 4b. artigos: energia solar e clinicas apontam para as paginas de nicho
    a = RAIZ / "scripts" / "conteudo" / "artigos_nichos_anuncios.py"
    if troca_unica(a,
                   "meses. Se você quer ajuda com a parte dos anúncios, veja como funciona a\n"
                   "        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>",
                   "meses. Se você quer ajuda com a parte dos anúncios, veja como funciona o\n"
                   "        {link('/trafego-pago-para-energia-solar/', 'tráfego pago para energia solar')}.</p>",
                   "{link('/trafego-pago-para-energia-solar/', 'tráfego pago para energia solar')}.</p>"):
        feito.append("artigo energia solar")
    if troca_unica(a,
                   "verba de anúncio com o passar dos meses. Se você quer ajuda com as campanhas, veja como funciona a\n"
                   "        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>",
                   "verba de anúncio com o passar dos meses. Se você quer ajuda com as campanhas, veja como funciona a\n"
                   "        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')} — e, para consultório\n"
                   "        odontológico, o {link('/trafego-pago-para-dentistas/', 'tráfego pago para dentistas')}.</p>",
                   "{link('/trafego-pago-para-dentistas/', 'tráfego pago para dentistas')}.</p>"):
        feito.append("artigo clinicas")

    print("feito:", feito or "nada (ja estava ligado)")


if __name__ == "__main__":
    main()
