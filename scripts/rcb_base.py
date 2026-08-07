# -*- coding: utf-8 -*-
"""
Módulo base compartilhado dos geradores de página da RCB.

Centraliza o invólucro que se repete em toda página do site — <head>, navbar,
rodapé, schema, blocos de seção — para que os geradores de conteúdo cuidem
apenas do texto, que é único em cada página.

Usado por:
  - scripts/gerar-paginas-competitivas.py   (páginas comerciais da divisão nacional)
  - scripts/gerar-artigos-competitivos.py   (artigos do blog dos novos clusters)
  - scripts/atualizar-nav-rodape.py         (propaga navbar/rodapé para o site inteiro)

Nada aqui é específico de uma página: se um texto só serve para uma URL, ele
mora no gerador de conteúdo, não neste arquivo.
"""
import json
import os
import re
from urllib.parse import quote

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
BASE_URL = "https://rcbseo.com.br"
WHATS = "5562991161040"
OG_IMG = "https://rcbseo.com.br/assets/img/og-rcb-1200x628.png"
GA_ID = "G-K644KXR38G"


# ============================================================
# Utilidades
# ============================================================

def esc(txt):
    """Escapa texto para uso dentro de atributo HTML."""
    return (txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
               .replace('"', "&quot;"))


def sesc(txt):
    """Escapa texto para dentro de string JSON do schema (sem quebrar o JSON-LD)."""
    return json.dumps(txt, ensure_ascii=False)[1:-1]


def strip_tags(html):
    return re.sub(r"<[^>]+>", "", html)


def whats_link(mensagem):
    return f"https://wa.me/{WHATS}?text={quote(mensagem)}"


def tempo_leitura(html):
    """Estimativa de minutos de leitura a partir do HTML do corpo."""
    palavras = len(strip_tags(html).split())
    return max(3, round(palavras / 220))


def contar_palavras(html):
    return len(strip_tags(html).split())


# ============================================================
# <head>
# ============================================================

def head_comum(titulo, desc, canonical, schema_json, og_type="website", extra_head=""):
    """
    Cabeçalho idêntico ao padrão do site: gtag com consent mode, metas sociais,
    favicons, fontes com carregamento diferido, styles.css e schema JSON-LD.
    """
    assert len(titulo) <= 65, f"Title longo demais ({len(titulo)}): {titulo}"
    assert len(desc) <= 160, f"Description longa demais ({len(desc)}): {desc}"
    t, d = esc(titulo), esc(desc)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('consent', 'default', {{
      'ad_storage': 'denied',
      'ad_user_data': 'denied',
      'ad_personalization': 'denied',
      'analytics_storage': 'denied',
      'functionality_storage': 'granted',
      'security_storage': 'granted',
      'wait_for_update': 500
    }});
    gtag('js', new Date());
    gtag('config', '{GA_ID}', {{ 'anonymize_ip': true }});
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#0D1B2A">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <meta name="author" content="Renan Carvalho Barbosa">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="pt-BR" href="{canonical}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="RCB Consultoria">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{OG_IMG}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="628">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{OG_IMG}">
  <meta name="twitter:domain" content="rcbseo.com.br">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"></noscript>
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">{schema_json}</script>{extra_head}
</head>"""


# ============================================================
# Navbar — bloco <ul class="nav-menu"> em linha única.
# É a ÚNICA fonte deste bloco no projeto: atualizar-nav-rodape.py substitui
# a versão antiga por esta em todas as páginas já publicadas.
# ============================================================

_CHEVRON = ('<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>')

NAV_NACIONAL_ITENS = [
    ("/seo-para-mercados-competitivos/", "SEO para mercados competitivos"),
    ("/seo-nacional/", "SEO nacional"),
    ("/seo-para-iptv/", "SEO para IPTV"),
    ("/seo-para-bets/", "SEO para bets e iGaming"),
    ("/seo-para-afiliados-de-apostas/", "SEO para afiliados"),
    ("/link-building-para-nichos-competitivos/", "Link building"),
    ("/analise-de-dominios-expirados/", "Domínios expirados"),
    ("/migracao-de-dominio-seo/", "Migração de domínio"),
]

_nav_nacional = "".join(
    f'<a href="{u}" class="nav-dropdown-item" role="menuitem">{t}</a>' for u, t in NAV_NACIONAL_ITENS
)

NAV_MENU = (
    '<ul class="nav-menu" id="navMenu" role="list">'
    '<li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Serviços'
    + _CHEVRON +
    '</button><div class="nav-dropdown-menu" role="menu">'
    '<a href="/consultoria-seo-local/" class="nav-dropdown-item" role="menuitem">Consultoria SEO Local</a>'
    '<a href="/diagnostico-presenca-digital/" class="nav-dropdown-item" role="menuitem">Diagnóstico de Presença Digital</a>'
    '<a href="/auditoria-seo/" class="nav-dropdown-item" role="menuitem">Auditoria SEO</a>'
    '<a href="/google-perfil-empresa/" class="nav-dropdown-item" role="menuitem">Google Perfil da Empresa</a>'
    '<a href="/site-otimizado-para-seo/" class="nav-dropdown-item" role="menuitem">Site otimizado para SEO</a>'
    '<a href="/conteudo-para-seo/" class="nav-dropdown-item" role="menuitem">Conteúdo para SEO</a>'
    '<a href="/acompanhamento-seo/" class="nav-dropdown-item" role="menuitem">Acompanhamento SEO</a>'
    # Estava no topo do menu antes desta rodada. Foi movido para cá — e não
    # removido — porque a entrada "SEO Nacional" ocupou o espaço do topo e
    # /consultor-seo-goiania/ é uma das páginas locais mais importantes do site.
    '<a href="/consultor-seo-goiania/" class="nav-dropdown-item" role="menuitem">Consultor SEO em Goiânia</a>'
    '</div></li>'
    '<li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">SEO Nacional'
    + _CHEVRON +
    '</button><div class="nav-dropdown-menu nav-dropdown-wide" role="menu">' + _nav_nacional + '</div></li>'
    '<li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Nichos'
    + _CHEVRON +
    '</button><div class="nav-dropdown-menu" role="menu">'
    '<a href="/seo-para-clinicas/" class="nav-dropdown-item" role="menuitem">Clínicas</a>'
    '<a href="/seo-para-dentistas/" class="nav-dropdown-item" role="menuitem">Dentistas</a>'
    '<a href="/seo-para-clinicas-de-estetica/" class="nav-dropdown-item" role="menuitem">Estética</a>'
    '<a href="/seo-para-medicos/" class="nav-dropdown-item" role="menuitem">Médicos</a>'
    '<a href="/seo-para-clinicas-de-emagrecimento/" class="nav-dropdown-item" role="menuitem">Emagrecimento</a>'
    '<a href="/para-advogados/" class="nav-dropdown-item" role="menuitem">Advogados</a>'
    '<a href="/para-comercios-locais/" class="nav-dropdown-item" role="menuitem">Comércios locais</a>'
    '<a href="/para-profissionais-liberais/" class="nav-dropdown-item" role="menuitem">Profissionais liberais</a>'
    '</div></li>'
    '<li><a href="/blog/" class="nav-link">Blog</a></li>'
    '<li><a href="/cases/" class="nav-link">Cases</a></li>'
    '<li><a href="/sobre/" class="nav-link">Sobre</a></li>'
    '<li><a href="/contato/" class="nav-link">Contato</a></li>'
    '<li><a href="/diagnostico-presenca-digital/" class="nav-link nav-cta">Diagnóstico gratuito</a></li>'
    '</ul>'
)

NAVBAR = ('  <a class="skip-link" href="#main-content">Pular para o conteúdo principal</a>\n'
          '  <nav class="navbar" id="navbar" role="navigation" aria-label="Menu principal">'
          '<div class="container nav-container">'
          '<a href="/" class="nav-logo" aria-label="Página inicial">'
          '<span class="logo-text">RCB</span><span class="logo-sub">SEO Local</span></a>'
          '<button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="navMenu">'
          '<span></span><span></span><span></span></button>'
          + NAV_MENU + '</div></nav>')


# ============================================================
# Rodapé — coluna nova "SEO Nacional" (6 a 10 URLs prioritárias, conforme briefing)
# ============================================================

FOOTER_NACIONAL_ITENS = [
    ("/seo-para-mercados-competitivos/", "Mercados competitivos"),
    ("/seo-nacional/", "SEO nacional"),
    ("/seo-para-iptv/", "SEO para IPTV"),
    ("/seo-para-bets/", "SEO para bets"),
    ("/seo-para-afiliados-de-apostas/", "SEO para afiliados"),
    ("/link-building-para-nichos-competitivos/", "Link building"),
    ("/analise-de-dominios-expirados/", "Domínios expirados"),
    ("/recuperacao-de-trafego-organico/", "Recuperação de tráfego"),
]

FOOTER_COL_NACIONAL = (
    '<h4 class="footer-col-title">SEO Nacional</h4><nav class="footer-col-nav">'
    + "".join(f'<a href="{u}">{t}</a>' for u, t in FOOTER_NACIONAL_ITENS)
    + '</nav>'
)

_COOKIE_BANNER = """  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-labelledby="cookie-banner-title" aria-describedby="cookie-banner-desc" hidden>
    <div class="cookie-banner-content">
      <div class="cookie-banner-text">
        <strong id="cookie-banner-title">Este site usa cookies</strong>
        <p id="cookie-banner-desc">Utilizamos cookies do Google Analytics para entender como o site é usado e melhorar a experiência. Você pode aceitar ou recusar. <a href="/cookies/">Saiba mais</a>.</p>
      </div>
      <div class="cookie-banner-actions">
        <button type="button" class="btn btn-secondary cookie-btn-reject" data-cookie-action="reject">Recusar</button>
        <button type="button" class="btn btn-primary cookie-btn-accept" data-cookie-action="accept">Aceitar</button>
      </div>
    </div>
  </div>"""


def rodape(scripts_extra=""):
    return ('  <footer class="footer" role="contentinfo"><div class="container footer-cols">'
            '<div class="footer-col footer-col-identity"><span class="logo-text">RCB</span>'
            '<strong class="footer-name">Renan Carvalho Barbosa</strong>'
            '<span class="footer-cargo">Consultor de SEO Local e Google Meu Negócio</span>'
            '<p class="footer-bio">Com base em Goiânia e atendimento online para clínicas e negócios locais em todo o Brasil.</p></div>'
            '<div class="footer-col"><h4 class="footer-col-title">Serviços</h4><nav class="footer-col-nav">'
            '<a href="/consultoria-seo-local/">Consultoria SEO Local</a>'
            '<a href="/consultoria-seo/">Consultoria SEO por cidade</a>'
            '<a href="/diagnostico-presenca-digital/">Diagnóstico de Presença Digital</a>'
            '<a href="/auditoria-seo/">Auditoria de SEO</a>'
            '<a href="/google-perfil-empresa/">Google Perfil da Empresa</a>'
            '<a href="/site-otimizado-para-seo/">Site otimizado para SEO</a>'
            '<a href="/acompanhamento-seo/">Acompanhamento de SEO</a></nav></div>'
            '<div class="footer-col">' + FOOTER_COL_NACIONAL + '</div>'
            '<div class="footer-col"><h4 class="footer-col-title">Nichos</h4><nav class="footer-col-nav">'
            '<a href="/seo-para-clinicas/">Clínicas</a><a href="/seo-para-dentistas/">Dentistas</a>'
            '<a href="/seo-para-clinicas-de-estetica/">Estética</a><a href="/seo-para-medicos/">Médicos</a>'
            '<a href="/para-advogados/">Advogados</a></nav></div>'
            '<div class="footer-col"><h4 class="footer-col-title">Contato</h4><div class="footer-col-contact">'
            '<a href="/contato/">Página de contato</a>'
            f'<a href="https://wa.me/{WHATS}" target="_blank" rel="noopener noreferrer">WhatsApp: (62) 99116-1040</a>'
            '<a href="mailto:contato@rcbseo.com.br">contato@rcbseo.com.br</a>'
            '<span>Rua 18-A, nº 256 — Goiânia - GO, CEP 74070-060</span></div></div></div>'
            '<div class="footer-bottom"><div class="container footer-bottom-inner">'
            '<p>&copy; <span id="anoAtual"></span> Renan Carvalho Barbosa. Todos os direitos reservados.</p>'
            '<a href="/privacidade/" class="footer-privacy">Política de Privacidade</a>'
            '<a href="/cookies/" class="footer-privacy" style="margin-left:1rem;">Política de Cookies</a>'
            '</div></div></footer>\n'
            '  <script src="/script.js" defer></script>\n'
            '  <script defer src=\'https://static.cloudflareinsights.com/beacon.min.js\' '
            'data-cf-beacon=\'{"token": "958c755428354df69e95c4366389faca"}\'></script>\n'
            '  <script defer src="/assets/js/cookie-consent.js"></script>\n'
            + _COOKIE_BANNER + scripts_extra + "\n</body>\n</html>")


# ============================================================
# Blocos de schema
# ============================================================

def schema_breadcrumb(trilha):
    """trilha: lista de (nome, url_absoluta)."""
    itens = ",".join(
        '{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}' % (i + 1, sesc(n), u)
        for i, (n, u) in enumerate(trilha)
    )
    return '{"@type":"BreadcrumbList","itemListElement":[%s]}' % itens


def schema_faq(faq):
    """faq: lista de (pergunta, resposta_em_texto)."""
    itens = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (sesc(q), sesc(strip_tags(a)))
        for q, a in faq
    )
    return '{"@type":"FAQPage","mainEntity":[%s]}' % itens


def schema_service(nome, descricao, canonical, tipo="Consultoria de SEO"):
    return ('{"@type":"Service","serviceType":"%s","name":"%s","description":"%s","url":"%s",'
            '"provider":{"@type":"ProfessionalService","@id":"https://rcbseo.com.br/#business",'
            '"name":"RCB Consultoria","url":"https://rcbseo.com.br/"},'
            '"areaServed":{"@type":"Country","name":"Brasil"}}'
            % (sesc(tipo), sesc(nome), sesc(descricao), canonical))


def schema_webpage(canonical, nome, desc, data_mod):
    return ('{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR",'
            '"dateModified":"%s","isPartOf":{"@type":"WebSite","url":"https://rcbseo.com.br/",'
            '"name":"RCB Consultoria"}}' % (canonical, sesc(nome), sesc(desc), data_mod))


def schema_blogposting(canonical, titulo, desc, data_pub, data_mod):
    return ('{"@type":"BlogPosting","mainEntityOfPage":{"@type":"WebPage","@id":"%s"},'
            '"headline":"%s","description":"%s","image":"%s","datePublished":"%s","dateModified":"%s",'
            '"inLanguage":"pt-BR",'
            '"author":{"@type":"Person","name":"Renan Carvalho Barbosa","url":"https://rcbseo.com.br/sobre/"},'
            '"publisher":{"@type":"Organization","name":"RCB Consultoria","url":"https://rcbseo.com.br/"}}'
            % (canonical, sesc(titulo), sesc(desc), OG_IMG, data_pub, data_mod))


def grafo(*blocos):
    return '{"@context":"https://schema.org","@graph":[%s]}' % ",".join(b for b in blocos if b)


# ============================================================
# Blocos de seção — compostos livremente por cada página.
# A ordem e a escolha das seções variam de página para página de propósito:
# repetir a mesma sequência em 22 URLs criaria páginas-molde.
# ============================================================

def hero(trilha_html, eyebrow, h1, subtitulo, cta_primario, cta_secundario, painel_html="", page_id=""):
    p1_url, p1_txt = cta_primario
    p2_url, p2_txt = cta_secundario
    alvo = ' target="_blank" rel="noopener noreferrer"' if p1_url.startswith("http") else ""
    painel = f'\n        <aside class="page-hero-panel">{painel_html}</aside>' if painel_html else ""
    grid = "page-hero-grid" if painel_html else "page-hero-grid"
    return f"""
    <section class="page-hero">
      <div class="container {grid}">
        <div>
          {trilha_html}
          <div class="eyebrow">{eyebrow}</div>
          <h1 class="page-title">{h1}</h1>
          <p class="page-subtitle">{subtitulo}</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="{p1_url}"{alvo} data-event="cta_click" data-location="hero_principal" data-page="{page_id}">{p1_txt}</a>
            <a class="btn btn-outline" href="{p2_url}" data-event="cta_click" data-location="hero_secundario" data-page="{page_id}">{p2_txt}</a>
          </div>
        </div>{painel}
      </div>
    </section>"""


def breadcrumb_html(trilha):
    """trilha: lista de (nome, href) — último item sem link."""
    partes = []
    for i, (nome, href) in enumerate(trilha):
        if i == len(trilha) - 1:
            partes.append(f"<span>{nome}</span>")
        else:
            partes.append(f'<a href="{href}">{nome}</a>')
    return ('<nav class="breadcrumb" aria-label="Breadcrumb">'
            + '<span>/</span>'.join(partes) + '</nav>')


def sec_split(tag, titulo, corpo_html, lateral_html, tid, classe="solution-section"):
    """Seção em duas colunas: texto + cartão lateral."""
    return f"""
    <section class="{classe}" aria-labelledby="{tid}">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">{tag}</div>
          <h2 id="{tid}" class="section-title">{titulo}</h2>
{corpo_html}
        </div>
        <div class="diagnostic-card">{lateral_html}</div>
      </div>
    </section>"""


def sec_texto(tag, titulo, corpo_html, tid, classe="solution-section", desc=""):
    """Seção de largura total."""
    d = f'\n          <p class="section-desc">{desc}</p>' if desc else ""
    return f"""
    <section class="{classe}" aria-labelledby="{tid}">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">{tag}</div>
          <h2 id="{tid}" class="section-title">{titulo}</h2>{d}
        </div>
{corpo_html}
      </div>
    </section>"""


def cards(itens):
    """itens: lista de (href|None, titulo, texto, link_txt|None)."""
    out = []
    for href, tit, txt, link in itens:
        if href:
            lk = f'<span class="cluster-card-link">{link}</span>' if link else ""
            out.append(f'<a class="cluster-card" href="{href}"><h3>{tit}</h3><p>{txt}</p>{lk}</a>')
        else:
            out.append(f'<div class="cluster-card"><h3>{tit}</h3><p>{txt}</p></div>')
    return '        <div class="cluster-grid">\n          ' + "\n          ".join(out) + '\n        </div>'


def problem_cards(itens):
    """itens: lista de (titulo, texto)."""
    out = "\n          ".join(
        f'<div class="problem-card"><h3>{t}</h3><p>{x}</p></div>' for t, x in itens
    )
    return f'        <div class="problem-grid">\n          {out}\n        </div>'


def passos(itens):
    """itens: lista de (titulo, texto). Renderiza a esteira numerada do site."""
    seta = ('<div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>')
    blocos = []
    for i, (t, x) in enumerate(itens):
        if i:
            blocos.append(seta)
        blocos.append(f'<div class="metodo-step"><div class="step-number">{i+1}</div><h3>{t}</h3><p>{x}</p></div>')
    return '        <div class="metodo-steps">\n          ' + "\n          ".join(blocos) + '\n        </div>'


def lista(itens, classe="audit-list"):
    return (f'          <ul class="{classe}">\n'
            + "\n".join(f"            <li>{i}</li>" for i in itens)
            + "\n          </ul>")


def tabela(cabecalho, linhas, nota=""):
    """Tabela comparativa responsiva, no padrão .case-table do site."""
    th = "".join(f"<th>{c}</th>" for c in cabecalho)
    tr = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in linha) + "</tr>" for linha in linhas
    )
    n = f'\n        <p class="case-table-note">{nota}</p>' if nota else ""
    return (f'        <div class="case-table-wrap">\n'
            f'          <table class="case-table">\n'
            f'            <thead><tr>{th}</tr></thead>\n'
            f'            <tbody>{tr}</tbody>\n'
            f'          </table>\n        </div>{n}')


def pills(itens):
    return ('        <div class="pill-row">'
            + "".join(f'<span class="pill">{i}</span>' for i in itens)
            + '</div>')


def sec_faq(faq, titulo, tid="faq-titulo", tag="Perguntas frequentes"):
    """faq: lista de (pergunta, resposta_html). Renderizado visível — condição para o FAQPage."""
    cards_html = "\n".join(
        f'          <div class="faq-card">\n            <h3>{q}</h3>\n            <p>{a}</p>\n          </div>'
        for q, a in faq
    )
    return f"""
    <section class="faq-section" aria-labelledby="{tid}">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">{tag}</div>
          <h2 id="{tid}" class="section-title">{titulo}</h2>
        </div>
        <div class="faq-grid">
{cards_html}
        </div>
      </div>
    </section>"""


def cta_final(titulo, texto, cta_url, cta_txt, page_id, secundario=None, tag="Análise de projeto"):
    sec = ""
    if secundario:
        s_url, s_txt = secundario
        sec = (f'\n            <a class="btn btn-outline" href="{s_url}" data-event="cta_click" '
               f'data-location="cta_final_secundario" data-page="{page_id}">{s_txt}</a>')
    alvo = ' target="_blank" rel="noopener noreferrer"' if cta_url.startswith("http") else ""
    return f"""
    <section class="cta-band" aria-labelledby="cta-final-titulo">
      <div class="container">
        <div class="cta-inner">
          <div class="section-tag">{tag}</div>
          <h2 id="cta-final-titulo" class="section-title">{titulo}</h2>
          <p class="section-desc">{texto}</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="{cta_url}"{alvo} data-event="cta_click" data-location="cta_final" data-page="{page_id}">{cta_txt}</a>{sec}
          </div>
        </div>
      </div>
    </section>"""


def relacionados(titulo, itens, tid="relacionados-titulo"):
    """itens: lista de (href, texto)."""
    links = "\n          ".join(
        f'<a class="cluster-card" href="{h}"><h3>{t}</h3><p>{d}</p></a>' for h, t, d in itens
    )
    return f"""
    <section class="solution-section" aria-labelledby="{tid}">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Continue por aqui</div>
          <h2 id="{tid}" class="section-title">{titulo}</h2>
        </div>
        <div class="cluster-grid">
          {links}
        </div>
      </div>
    </section>"""


def whatsapp_float(mensagem, page_id, aria):
    svg = ('<svg width="30" height="30" viewBox="0 0 24 24" fill="white" aria-hidden="true">'
           '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 '
           '1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 '
           '0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 '
           '4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 '
           '7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 '
           '4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 '
           '9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 '
           '5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 '
           '11.821 0 00-3.48-8.413Z"/></svg>')
    return (f'\n  <a href="{whats_link(mensagem)}" class="whatsapp-float" data-event="cta_click" '
            f'data-location="whatsapp_flutuante" data-page="{page_id}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="{esc(aria)}">{svg}</a>')


# ============================================================
# Montagem final e escrita
# ============================================================

def montar(head, corpo, page_id="", float_msg=None, float_aria="", scripts_extra=""):
    body_attr = f' data-page="{page_id}"' if page_id else ""
    flutuante = whatsapp_float(float_msg, page_id, float_aria) if float_msg else ""
    return (head + f"\n<body{body_attr}>\n" + NAVBAR + "\n\n  <main id=\"main-content\">\n"
            + corpo + "\n\n  </main>\n" + flutuante + "\n\n" + rodape(scripts_extra))


def escrever(caminho_rel, html):
    """Escreve garantindo a pasta. caminho_rel é relativo à raiz do site."""
    destino = os.path.join(RAIZ, caminho_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return destino
