"""Fonte unica do MENU e dos links de servicos do RODAPE (Etapa 1 do plano de nichos, 04/10/2026).

O site oferece 4 servicos: SEO e Google Meu Negocio | Sites e Landing Pages |
Trafego Pago (Google Ads) | SEO para YouTube. Agentes de IA, automacao e recuperacao
de vendas sairam do site (docs/plano-nichos-2026-10.md).

Item que ainda nao tem pagina propria aponta para a pagina atual mais proxima ate a
etapa dele (ver PROVISORIO). Quando a pagina nova existir, troque SO aqui e rode
    python scripts/foco-etapa1-2026-10-04.py
que reaplica o menu e o rodape em todas as paginas (idempotente).

Uso nos geradores:  import rcb_menu; html = rcb_menu.aplicar(html)
"""
import re

# "SEO para YouTube" fica FORA do menu ate a Etapa 5 criar a pagina (decisao do Renan,
# 04/10/2026). Quando a pagina existir: troque o destino em PROVISORIO e ponha True aqui.
MOSTRAR_YOUTUBE = False

# destino provisorio de itens cuja pagina chega numa etapa futura
PROVISORIO = {
    "seo_youtube": "/conteudo-para-seo/",                 # Etapa 5 cria a pagina propria
    "trafego": "/gestao-de-trafego-pago-goiania/",         # Etapa 3 cria a pagina nacional
    "landing": "/criacao-de-landing-page/",        # Etapa 2 decide a pagina nacional
}

_CHEVRON = ('<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>')

SEO_GMN = [
    ("/consultoria-seo-local/", "Consultoria de SEO"),
    ("/google-perfil-empresa/", "Google Meu Negócio"),
    ("/auditoria-seo/", "Auditoria de SEO"),
    ("/conteudo-para-seo/", "Conteúdo para SEO"),
    ("/acompanhamento-seo/", "Acompanhamento de SEO"),
    ("/diagnostico-presenca-digital/", "Diagnóstico de presença digital"),
    ("/consultor-seo-goiania/", "Consultor de SEO em Goiânia"),
]
SITES = [
    (PROVISORIO["landing"], "Landing page para anúncios"),
    ("/criacao-de-sites-goiania/", "Criação de sites"),
    ("/site-otimizado-para-seo/", "Site otimizado para SEO"),
    ("/criacao-de-loja-virtual-goiania/", "Loja virtual"),
]
NICHOS = [
    ("/seo-para-pequenas-empresas/", "Pequenas empresas"),
    ("/seo-para-clinicas/", "Clínicas"),
    ("/seo-para-dentistas/", "Dentistas"),
    ("/seo-para-clinicas-de-estetica/", "Estética"),
    ("/seo-para-medicos/", "Médicos"),
    ("/para-advogados/", "Advogados"),
    ("/seo-para-imobiliarias/", "Imobiliárias"),
    ("/seo-para-contadores/", "Contadores"),
    ("/seo-para-veterinarios/", "Veterinários"),
    ("/seo-para-psicologos/", "Psicólogos"),
    ("/para-comercios-locais/", "Comércios locais"),
    ("/para-profissionais-liberais/", "Profissionais liberais"),
]
# links de servico do rodape (bloco RCB:SITES-FOOTER); o resto da coluna continua
RODAPE_SERVICOS = [
    (PROVISORIO["landing"], "Landing page para anúncios"),
    ("/criacao-de-sites-goiania/", "Criação de sites"),
    (PROVISORIO["trafego"], "Tráfego pago (Google Ads)"),
    ("/criacao-de-loja-virtual-goiania/", "Loja virtual"),
]
RODAPE_INSTITUCIONAL = [("/blog/", "Blog"), ("/cases/", "Cases"), ("/sobre/", "Sobre")]

REMOVIDAS = ("/agentes-de-ia/", "/agente-de-ia-para-clinicas/",
             "/automacao-de-processos/", "/recuperacao-de-vendas-whatsapp/")


def _dropdown(rotulo, itens):
    links = "".join('<a href="%s" class="nav-dropdown-item" role="menuitem">%s</a>' % (h, t) for h, t in itens)
    return ('<li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" '
            'aria-haspopup="true">%s%s</button><div class="nav-dropdown-menu" role="menu">%s</div></li>'
            % (rotulo, _CHEVRON, links))


def itens_menu(cta_href="/#pacotes", data_page=""):
    """Conteudo do <ul class="nav-menu"> (sem o <ul>)."""
    dp = ' data-page="%s"' % data_page if data_page else ""
    return ("<!--RCB:MENU-->"
            + _dropdown("SEO e Google", SEO_GMN)  # rotulo curto: o completo nao cabe em 1024-1366px
            + _dropdown("Sites e Landing Pages", SITES)
            + '<li><a href="%s" class="nav-link">Tráfego Pago</a></li>' % PROVISORIO["trafego"]
            + ('<li><a href="%s" class="nav-link">SEO para YouTube</a></li>' % PROVISORIO["seo_youtube"]
               if MOSTRAR_YOUTUBE else "")
            + _dropdown("Nichos", NICHOS)
            + '<li><a href="/contato/" class="nav-link">Contato</a></li>'
            + '<li><a href="%s" class="nav-link nav-cta" data-event="cta_click" data-location="navbar"%s>'
              'Orçamento grátis</a></li>' % (cta_href, dp)
            + "<!--/RCB:MENU-->")


_UL = re.compile(r'(<ul class="nav-menu" id="navMenu"[^>]*>)(.*?)(</ul>\s*</div>\s*</nav>)', re.S)
_CTA = re.compile(r'<a href="([^"]*)" class="nav-link nav-cta"[^>]*?(?:data-page="([^"]*)")?[^>]*>')
_AG_FOOTER = re.compile(r'<!--RCB:AGENTES-FOOTER-->.*?<!--/RCB:AGENTES-FOOTER-->', re.S)
_SITES_FOOTER = re.compile(r'<!--RCB:SITES-FOOTER-->(.*?)<!--/RCB:SITES-FOOTER-->', re.S)
_INST = re.compile(r'<!--RCB:INSTITUCIONAL-->.*?<!--/RCB:INSTITUCIONAL-->', re.S)


def _troca_menu(h):
    m = _UL.search(h)
    if not m:
        return h
    cta = _CTA.search(m.group(2))
    href, dp = (cta.group(1), cta.group(2) or "") if cta else ("/#pacotes", "")
    return h[:m.start(2)] + itens_menu(href, dp) + h[m.end(2):]


def _bloco_servicos(antigo):
    if "<li>" in antigo:  # rodape da home: <ul><li>
        return "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in RODAPE_SERVICOS)
    return "".join('<a href="%s">%s</a>' % (h, t) for h, t in RODAPE_SERVICOS)


def _institucional(h):
    """Blog, Cases e Sobre sairam do menu: entram no rodape (coluna de contato)."""
    h = _INST.sub("", h)
    bloco = "".join('<a href="%s">%s</a>' % (u, t) for u, t in RODAPE_INSTITUCIONAL)
    novo, n = re.subn(r'(<div class="footer-col-contact">)',
                      r'\1<!--RCB:INSTITUCIONAL-->' + bloco + '<!--/RCB:INSTITUCIONAL-->', h, count=1)
    if n:
        return novo
    p = ('<p><strong>Conheça:</strong><br>'
         + ' · '.join('<a href="%s">%s</a>' % (u, t) for u, t in RODAPE_INSTITUCIONAL) + '</p>')
    return re.sub(r'(<div class="footer-contact">)', r'\1<!--RCB:INSTITUCIONAL-->' + p + '<!--/RCB:INSTITUCIONAL-->',
                  h, count=1)


def _tira_links_removidos(h):
    for u in REMOVIDAS:
        alvo = r'(?:https://rcbseo\.com\.br)?' + re.escape(u)
        h = re.sub(r'\s*<li>\s*<a [^>]*href="' + alvo + r'"[^>]*>[^<]*</a>\s*</li>', '', h)
        h = re.sub(r'\r?\n[ \t]*<a [^>]*href="' + alvo + r'"[^>]*>[^<]*</a>[ \t]*(?=\r?\n)', '', h)
        h = re.sub(r'<a [^>]*href="' + alvo + r'"[^>]*>([^<]*)</a>', r'\1', h)
    return h


def aplicar(h):
    """Menu novo, rodape sem agentes de IA, servicos do rodape e links removidos."""
    h = _troca_menu(h)
    h = _AG_FOOTER.sub("", h)
    h = _SITES_FOOTER.sub(lambda m: "<!--RCB:SITES-FOOTER-->" + _bloco_servicos(m.group(1))
                          + "<!--/RCB:SITES-FOOTER-->", h)
    if 'role="contentinfo"' in h:
        h = _institucional(h)
    return _tira_links_removidos(h)
