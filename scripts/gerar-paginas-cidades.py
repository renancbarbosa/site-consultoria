# -*- coding: utf-8 -*-
"""
Gera as páginas de cidade em /consultoria-seo/<slug>/ usando os dados de CNPJ
do projeto SITE-DADOS (C:/Users/renan/SITE-DADOS/data/cidades/*.json).

Cada página recebe dados únicos da cidade (empresas ativas, aberturas recentes,
ramos que mais crescem, bairros) para não ser página repetida.

Uso:  python scripts/gerar-paginas-cidades.py
Goiânia é pulada de propósito: a cidade já tem /seo-local-goiania/ e
/consultor-seo-goiania/ — gerar outra página criaria concorrência interna.
"""
import json
import os
import glob
import hashlib
from urllib.parse import quote

DADOS = r"C:/Users/renan/SITE-DADOS/data/cidades"
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE_URL = "https://rcbseo.com.br"
WHATS = "5562991161040"

ESTADOS = {
    "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas",
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo",
    "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais", "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
    "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul", "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina",
    "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins",
}

# Nomes de CNAE longos/técnicos -> rótulo simples para o leitor leigo
ROTULOS_CNAE = {
    "Promoção de vendas": "Promoção de vendas",
    "Preparação de documentos e serviços especializados de apoio administrativo não especificados anteriormente": "Serviços de apoio administrativo",
    "Comércio varejista de artigos do vestuário e acessórios": "Lojas de roupas e acessórios",
    "Serviços de malote não realizados pelo Correio Nacional": "Serviços de malote e entregas",
    "Cabeleireiros, manicure e pedicure": "Salões de beleza",
    "Fornecimento de alimentos preparados preponderantemente para consumo domiciliar": "Comida por encomenda e delivery",
    "Transporte rodoviário de carga, exceto produtos perigosos e mudanças, municipal.": "Transporte de carga municipal",
    "Transporte rodoviário de carga, exceto produtos perigosos e mudanças, intermunicipal, interestadual e internacional.": "Transporte de carga intermunicipal",
    "Lanchonetes, casas de chá, de sucos e similares": "Lanchonetes e similares",
    "Serviços de entrega rápida": "Entrega rápida (motoboy)",
    "Restaurantes e similares": "Restaurantes",
    "Obras de alvenaria": "Obras e reformas (alvenaria)",
    "Serviços combinados de escritório e apoio administrativo": "Escritórios de apoio administrativo",
    "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - minimercados, mercearias e armazéns": "Minimercados e mercearias",
    "Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica": "Consultoria empresarial",
    "Serviços de organização de feiras, congressos, exposições e festas": "Organização de festas e eventos",
    "Comércio varejista de cosméticos, produtos de perfumaria e de higiene pessoal": "Lojas de cosméticos e perfumaria",
    "Atividades de estética e outros serviços de cuidados com a beleza": "Clínicas e estúdios de estética",
    "Instalação e manutenção elétrica": "Serviços de eletricista",
    "Desenvolvimento de programas de computador sob encomenda": "Desenvolvimento de software",
}


def rotulo_cnae(nome):
    if nome in ROTULOS_CNAE:
        return ROTULOS_CNAE[nome]
    limpo = nome.replace(" não especificados anteriormente", "").replace(" não especificadas anteriormente", "")
    if len(limpo) > 60:
        limpo = limpo.split(",")[0]
    if len(limpo) > 60:
        limpo = limpo[:57].rstrip() + "..."
    return limpo


def n_br(n):
    return f"{n:,}".replace(",", ".")


def variante(slug, n):
    return int(hashlib.md5(slug.encode()).hexdigest(), 16) % n


def limpar_bairro(b):
    b = b.strip()
    b = b.replace("Set ", "Setor ") if b.startswith("Set ") else b
    return b


def carregar_cidades():
    cidades = []
    for arq in sorted(glob.glob(os.path.join(DADOS, "*.json"))):
        if os.path.basename(arq) == "_index.json":
            continue
        with open(arq, encoding="utf-8") as f:
            c = json.load(f)
        if c.get("slug") == "goiania":
            continue  # já coberta por /seo-local-goiania/
        cidades.append(c)
    # resolve slug repetido entre estados
    vistos = {}
    for c in cidades:
        s = c["slug"]
        vistos.setdefault(s, []).append(c)
    for s, lista in vistos.items():
        if len(lista) > 1:
            for c in lista:
                c["slug"] = f"{c['slug']}-{c['uf'].lower()}"
    return sorted(cidades, key=lambda c: -c["empresas_ativas"])


def head_comum(titulo, desc, canonical, schema_json):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K644KXR38G"></script>
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
    gtag('config', 'G-K644KXR38G', {{ 'anonymize_ip': true }});
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#0D1B2A">
  <title>{titulo}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Renan Carvalho Barbosa">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="pt-BR" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="RCB Consultoria">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://rcbseo.com.br/assets/img/logo-rcb-seo-local.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{titulo}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://rcbseo.com.br/assets/img/logo-rcb-seo-local.png">
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
  <script type="application/ld+json">{schema_json}</script>
</head>"""


NAVBAR = """  <a class="skip-link" href="#main-content">Pular para o conteúdo principal</a>
  <nav class="navbar" id="navbar" role="navigation" aria-label="Menu principal"><div class="container nav-container"><a href="/" class="nav-logo" aria-label="Página inicial"><span class="logo-text">RCB</span><span class="logo-sub">SEO Local</span></a><button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="navMenu"><span></span><span></span><span></span></button><ul class="nav-menu" id="navMenu" role="list"><li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Serviços<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></button><div class="nav-dropdown-menu" role="menu"><a href="/consultoria-seo-local/" class="nav-dropdown-item" role="menuitem">Consultoria SEO Local</a><a href="/diagnostico-presenca-digital/" class="nav-dropdown-item" role="menuitem">Diagnóstico de Presença Digital</a><a href="/auditoria-seo/" class="nav-dropdown-item" role="menuitem">Auditoria SEO</a><a href="/google-perfil-empresa/" class="nav-dropdown-item" role="menuitem">Google Perfil da Empresa</a><a href="/site-otimizado-para-seo/" class="nav-dropdown-item" role="menuitem">Site otimizado para SEO</a><a href="/conteudo-para-seo/" class="nav-dropdown-item" role="menuitem">Conteúdo para SEO</a><a href="/acompanhamento-seo/" class="nav-dropdown-item" role="menuitem">Acompanhamento SEO</a></div></li><li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Nichos<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></button><div class="nav-dropdown-menu" role="menu"><a href="/seo-para-clinicas/" class="nav-dropdown-item" role="menuitem">Clínicas</a><a href="/seo-para-dentistas/" class="nav-dropdown-item" role="menuitem">Dentistas</a><a href="/seo-para-clinicas-de-estetica/" class="nav-dropdown-item" role="menuitem">Estética</a><a href="/seo-para-medicos/" class="nav-dropdown-item" role="menuitem">Médicos</a><a href="/seo-para-clinicas-de-emagrecimento/" class="nav-dropdown-item" role="menuitem">Emagrecimento</a><a href="/para-advogados/" class="nav-dropdown-item" role="menuitem">Advogados</a><a href="/para-comercios-locais/" class="nav-dropdown-item" role="menuitem">Comércios locais</a><a href="/para-profissionais-liberais/" class="nav-dropdown-item" role="menuitem">Profissionais liberais</a></div></li><li><a href="/consultor-seo-goiania/" class="nav-link">Consultor SEO</a></li><li><a href="/blog/" class="nav-link">Blog</a></li><li><a href="/cases/" class="nav-link">Cases</a></li><li><a href="/sobre/" class="nav-link">Sobre</a></li><li><a href="/contato/" class="nav-link">Contato</a></li><li><a href="/diagnostico-presenca-digital/" class="nav-link nav-cta">Diagnóstico gratuito</a></li></ul></div></nav>"""


def rodape(pagina):
    return """  <footer class="footer" role="contentinfo"><div class="container footer-cols"><div class="footer-col footer-col-identity"><span class="logo-text">RCB</span><strong class="footer-name">Renan Carvalho Barbosa</strong><span class="footer-cargo">Consultor de SEO Local e Google Meu Negócio</span><p class="footer-bio">Com base em Goiânia e atendimento online para clínicas e negócios locais em todo o Brasil.</p></div><div class="footer-col"><h4 class="footer-col-title">Serviços</h4><nav class="footer-col-nav"><a href="/consultoria-seo-local/">Consultoria SEO Local</a><a href="/consultoria-seo/">Consultoria SEO por cidade</a><a href="/diagnostico-presenca-digital/">Diagnóstico de Presença Digital</a><a href="/auditoria-seo/">Auditoria de SEO</a><a href="/google-perfil-empresa/">Google Perfil da Empresa</a><a href="/site-otimizado-para-seo/">Site otimizado para SEO</a><a href="/acompanhamento-seo/">Acompanhamento de SEO</a></nav></div><div class="footer-col"><h4 class="footer-col-title">Nichos</h4><nav class="footer-col-nav"><a href="/seo-para-clinicas/">Clínicas</a><a href="/seo-para-dentistas/">Dentistas</a><a href="/seo-para-clinicas-de-estetica/">Estética</a><a href="/seo-para-medicos/">Médicos</a><a href="/para-advogados/">Advogados</a></nav></div><div class="footer-col"><h4 class="footer-col-title">Contato</h4><div class="footer-col-contact"><a href="/contato/">Página de contato</a><a href="https://wa.me/""" + WHATS + """\" target="_blank" rel="noopener noreferrer">WhatsApp: (62) 99116-1040</a><a href="mailto:contato@rcbseo.com.br">contato@rcbseo.com.br</a><span>Goiânia - GO</span></div></div></div><div class="footer-bottom"><div class="container footer-bottom-inner"><p>&copy; <span id="anoAtual"></span> Renan Carvalho Barbosa. Todos os direitos reservados.</p><a href="/privacidade/" class="footer-privacy">Política de Privacidade</a><a href="/cookies/" class="footer-privacy" style="margin-left:1rem;">Política de Cookies</a></div></div></footer>
  <script src="/script.js" defer></script>
  <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "958c755428354df69e95c4366389faca"}'></script>
  <script defer src="/assets/js/cookie-consent.js"></script>
  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-labelledby="cookie-banner-title" aria-describedby="cookie-banner-desc" hidden>
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
  </div>
</body>
</html>"""


INTROS = [
    "Seu cliente em {cidade} já pesquisa no Google antes de decidir onde comprar, agendar ou contratar. A pergunta é simples: ele encontra a sua empresa ou encontra um concorrente? A consultoria da RCB organiza sua presença no Google — perfil no Maps, site e conteúdo — para que quem procura o seu serviço em {cidade} encontre você.",
    "Quando alguém em {cidade} precisa de um serviço, o primeiro passo quase sempre é o mesmo: pesquisar no Google. Se a sua empresa não aparece nessa hora, o cliente vai para o concorrente que aparece. O trabalho da RCB é arrumar sua presença no Google — Maps, site e conteúdo — para você ser encontrado.",
    "Em {cidade}, quem aparece no Google leva o cliente. Não adianta ter bom atendimento se, na hora da pesquisa, quem aparece é o concorrente. A consultoria da RCB organiza seu perfil no Google Maps, seu site e seu conteúdo para sua empresa ser encontrada por quem já está procurando.",
]

CTAS = [
    "Quer saber por que sua empresa em {cidade} não aparece no Google — e o que fazer para mudar isso? Peça um diagnóstico gratuito. Você recebe uma análise inicial do seu perfil no Google, do seu site e dos concorrentes que aparecem na sua frente.",
    "O primeiro passo não custa nada: um diagnóstico gratuito da presença da sua empresa em {cidade} no Google. Você descobre o que está travando sua visibilidade e o que priorizar — antes de qualquer proposta.",
]


def pagina_cidade(c, vizinhas):
    cidade = c["cidade"]
    uf = c["uf"]
    estado = ESTADOS.get(uf, uf)
    slug = c["slug"]
    canonical = f"{BASE_URL}/consultoria-seo/{slug}/"
    ativas = n_br(c["empresas_ativas"])
    n90 = n_br(c["abertas_90d"])
    n12 = n_br(c["abertas_12m"])
    nmes = n_br(c["abertas_mes"])
    ref = c.get("data_referencia", c.get("snapshot", ""))

    titulo = f"Consultoria de SEO em {cidade} ({uf}) | Apareça no Google | RCB"
    desc = (f"Sua empresa em {cidade} não aparece no Google? {cidade} tem {ativas} empresas ativas "
            f"e ganhou {n90} novas em 90 dias. Consultoria de SEO online: Google Meu Negócio, site e conteúdo.")

    ramos = [(rotulo_cnae(r["nome"]), r["abertas_90d"]) for r in c.get("ramos_top", [])[:6]]
    bairros = [limpar_bairro(b["bairro"]) for b in c.get("bairros_top", [])[:4]]

    intro = INTROS[variante(slug, len(INTROS))].format(cidade=cidade)
    cta = CTAS[variante(slug + "x", len(CTAS))].format(cidade=cidade)

    whats_msg = quote(f"Olá, Renan. Tenho uma empresa em {cidade}/{uf} e quero aparecer melhor no Google.")
    whats_url = f"https://wa.me/{WHATS}?text={whats_msg}"

    faq = [
        (f"Vocês atendem empresas de {cidade} mesmo estando em Goiânia?",
         f"Sim. O atendimento para {cidade} é 100% online: reuniões por vídeo, análise dos seus dados reais do Google e implementação guiada passo a passo. O método é o mesmo do atendimento presencial — o Google funciona igual em qualquer cidade do Brasil."),
        (f"Minha empresa em {cidade} é pequena. SEO vale a pena para mim?",
         f"Vale, principalmente por isso: a disputa no Google acontece no seu bairro e na sua região, não contra o Brasil inteiro. Mesmo em uma cidade com {ativas} empresas ativas, quem aparece bem no Maps da própria região captura os clientes que estão pesquisando agora."),
        ("Quanto tempo demora para aparecer no Google?",
         "Os primeiros sinais costumam aparecer em semanas (principalmente no Google Maps), mas a melhora consistente leva alguns meses de trabalho, dependendo da concorrência do seu ramo na cidade. Não existe resultado garantido da noite para o dia — desconfie de quem promete isso."),
        ("O que está incluído na consultoria?",
         "Diagnóstico da sua presença atual, otimização do Google Meu Negócio (categorias, fotos, serviços, avaliações), ajustes ou criação de páginas do site voltadas ao que as pessoas pesquisam, conteúdo e acompanhamento com relatórios simples de entender."),
    ]

    faq_schema = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', "'"), a.replace('"', "'"))
        for q, a in faq
    )

    schema = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR"},'
        '{"@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Início","item":"https://rcbseo.com.br/"},'
        '{"@type":"ListItem","position":2,"name":"Consultoria de SEO por cidade","item":"https://rcbseo.com.br/consultoria-seo/"},'
        '{"@type":"ListItem","position":3,"name":"%s","item":"%s"}]},'
        '{"@type":"Service","serviceType":"Consultoria de SEO","name":"Consultoria de SEO em %s","description":"Consultoria online de SEO e Google Meu Negócio para empresas de %s (%s). Diagnóstico, otimização do perfil no Google, site e conteúdo.",'
        '"provider":{"@type":"LocalBusiness","@id":"https://rcbseo.com.br/#business"},'
        '"areaServed":{"@type":"City","name":"%s","containedInPlace":{"@type":"State","name":"%s"}}},'
        '{"@type":"FAQPage","mainEntity":[%s]}]}'
    ) % (canonical, titulo, desc.replace('"', "'"), cidade, canonical, cidade, cidade, uf, cidade, estado, faq_schema)

    ramos_html = "\n".join(
        f'            <li>{nome} — <strong>{n_br(qtd)}</strong> novas em 90 dias</li>' for nome, qtd in ramos
    )
    bairros_html = ""
    if bairros:
        bairros_html = f"""
          <p>Dentro da cidade, a abertura de empresas se concentra em regiões como <strong>{", ".join(bairros)}</strong> — ou seja, é nesses bairros que a disputa pela atenção do cliente no Google Maps tende a ser mais intensa.</p>"""

    vizinhas_html = ""
    if vizinhas:
        links = " · ".join(f'<a href="/consultoria-seo/{v["slug"]}/">{v["cidade"]}</a>' for v in vizinhas)
        vizinhas_html = f"""
    <section class="solution-section" aria-label="Outras cidades atendidas">
      <div class="container">
        <p class="section-desc">Também atendo outras cidades de {estado} e região: {links}. Veja <a href="/consultoria-seo/">todas as cidades atendidas</a>.</p>
      </div>
    </section>"""

    faq_html = "\n".join(
        f"""          <div class="faq-card">
            <h3>{q}</h3>
            <p>{a}</p>
          </div>""" for q, a in faq
    )

    corpo = f"""<body>
{NAVBAR}

  <main id="main-content">

    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><a href="/consultoria-seo/">Cidades</a><span>/</span><span>{cidade}</span></nav>
          <div class="eyebrow">{cidade} · {uf}</div>
          <h1 class="page-title">Consultoria de SEO em {cidade}: faça sua empresa aparecer no Google</h1>
          <p class="page-subtitle">{intro}</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="/diagnostico-presenca-digital/" data-event="cta_click" data-location="hero" data-page="cidade-{slug}">Solicitar diagnóstico gratuito</a>
            <a class="btn btn-outline" href="{whats_url}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero_whatsapp" data-page="cidade-{slug}">Chamar no WhatsApp</a>
          </div>
        </div>
        <aside class="page-hero-panel">
          <h2>O mercado de {cidade} em números</h2>
          <ul class="audit-list">
            <li><strong>{ativas}</strong> empresas ativas na cidade.</li>
            <li><strong>{n90}</strong> novas empresas nos últimos 90 dias.</li>
            <li><strong>{n12}</strong> novas empresas nos últimos 12 meses.</li>
            <li><strong>{nmes}</strong> abriram só no último mês.</li>
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Fonte: dados públicos de CNPJ (Receita Federal), referência {ref}.</p>
        </aside>
      </div>
    </section>

    <section class="solution-section" aria-labelledby="concorrencia-titulo">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Por que agir agora</div>
          <h2 id="concorrencia-titulo" class="section-title">A concorrência em {cidade} cresce todos os meses</h2>
          <p>{cidade} ganhou <strong>{n90} novas empresas nos últimos 90 dias</strong>. Cada uma delas disputa espaço no Google — inclusive no seu ramo. Quando um cliente pesquisa pelo seu serviço e sua empresa não aparece, ele nem fica sabendo que você existe: escolhe entre os que aparecem.</p>{bairros_html}
          <p>A boa notícia: a maioria das empresas da cidade ainda trata o Google como detalhe — perfil incompleto no Maps, site que não explica os serviços, nenhuma estratégia de conteúdo. Quem organiza essa base primeiro sai na frente.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Ramos que mais abriram empresas em {cidade} (90 dias)</h3>
          <ul class="audit-list">
{ramos_html}
          </ul>
        </div>
      </div>
    </section>

    <section class="metodo" aria-labelledby="metodo-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Como funciona</div>
          <h2 id="metodo-titulo" class="section-title">Consultoria online para {cidade}, com método testado</h2>
          <p class="section-desc">Todo o trabalho é feito a distância, por vídeo e com acesso aos seus dados reais do Google. O método é o mesmo aplicado nos atendimentos presenciais.</p>
        </div>
        <div class="metodo-steps">
          <div class="metodo-step"><div class="step-number">1</div><h3>Diagnóstico</h3><p>Analiso como sua empresa aparece hoje no Google e no Maps em {cidade}, e quais concorrentes aparecem na sua frente.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">2</div><h3>Perfil no Google</h3><p>Otimizo o Google Meu Negócio: categorias, serviços, fotos, postagens e estratégia de avaliações.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">3</div><h3>Site e conteúdo</h3><p>Ajusto (ou crio) as páginas do site para responder o que as pessoas de {cidade} pesquisam sobre o seu serviço.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">4</div><h3>Acompanhamento</h3><p>Relatórios simples: quantas pessoas viram, ligaram, pediram rota e chamaram no WhatsApp.</p></div>
        </div>
      </div>
    </section>

    <section class="solution-section" aria-labelledby="nichos-cidade-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Especialidades</div>
          <h2 id="nichos-cidade-titulo" class="section-title">Atendo negócios locais de {cidade} — com especialidade em saúde</h2>
          <p class="section-desc">O nicho mais maduro da RCB é saúde: <a href="/seo-para-clinicas/">clínicas</a>, <a href="/seo-para-dentistas/">dentistas</a>, <a href="/seo-para-clinicas-de-estetica/">estética</a> e <a href="/seo-para-medicos/">médicos</a>. Também atendo <a href="/para-comercios-locais/">comércios locais</a>, <a href="/para-profissionais-liberais/">profissionais liberais</a> e <a href="/para-advogados/">advogados</a>.</p>
        </div>
      </div>
    </section>

    <section class="faq-section" aria-labelledby="faq-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">FAQ</div>
          <h2 id="faq-titulo" class="section-title">Perguntas frequentes de empresas de {cidade}</h2>
        </div>
        <div class="faq-grid">
{faq_html}
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="cta-titulo">
      <div class="container">
        <div class="cta-inner">
          <div class="section-tag">Diagnóstico gratuito</div>
          <h2 id="cta-titulo" class="section-title">Quer aparecer no Google em {cidade}?</h2>
          <p>{cta}</p>
          <a class="btn btn-primary" href="/diagnostico-presenca-digital/" data-event="cta_click" data-location="final" data-page="cidade-{slug}">Solicitar diagnóstico gratuito</a>
        </div>
      </div>
    </section>
{vizinhas_html}
  </main>

"""
    flutuante = f"""  <a href="{whats_url}" class="whatsapp-float" data-event="cta_click" data-location="whatsapp_flutuante" data-page="cidade-{slug}" target="_blank" rel="noopener noreferrer" aria-label="Chamar no WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="white" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
"""
    return head_comum(titulo, desc, canonical, schema) + "\n" + corpo + flutuante + rodape(f"cidade-{slug}")


def pagina_hub(cidades):
    canonical = f"{BASE_URL}/consultoria-seo/"
    titulo = "Consultoria de SEO por Cidade | Atendimento em todo o Brasil | RCB"
    desc = ("Consultoria de SEO e Google Meu Negócio com atendimento online para as maiores cidades do Brasil. "
            "Escolha a sua cidade e veja os dados do mercado local.")

    schema = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR"},'
        '{"@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Início","item":"https://rcbseo.com.br/"},'
        '{"@type":"ListItem","position":2,"name":"Consultoria de SEO por cidade","item":"%s"}]}]}'
    ) % (canonical, titulo, desc, canonical)

    por_regiao = {}
    for c in cidades:
        por_regiao.setdefault(c["regiao"], {}).setdefault(c["uf"], []).append(c)

    ordem_regioes = ["Sudeste", "Sul", "Centro-Oeste", "Nordeste", "Norte"]
    blocos = []
    for reg in ordem_regioes:
        if reg not in por_regiao:
            continue
        estados_html = []
        for uf in sorted(por_regiao[reg]):
            lista = sorted(por_regiao[reg][uf], key=lambda c: -c["empresas_ativas"])
            links = []
            if uf == "GO":
                links.append('<li><a href="/seo-local-goiania/">Goiânia</a> — 322.797 empresas ativas</li>')
            links += [
                f'<li><a href="/consultoria-seo/{c["slug"]}/">{c["cidade"]}</a> — {n_br(c["empresas_ativas"])} empresas ativas</li>'
                for c in lista
            ]
            estados_html.append(f"""          <div class="diagnostic-card">
            <h3>{ESTADOS.get(uf, uf)} ({uf})</h3>
            <ul class="audit-list">
{chr(10).join('            ' + l for l in links)}
            </ul>
          </div>""")
        blocos.append(f"""    <section class="problem-section" aria-label="Região {reg}">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Região {reg}</div>
          <h2 class="section-title">Consultoria de SEO na Região {reg}</h2>
        </div>
        <div class="problem-grid">
{chr(10).join(estados_html)}
        </div>
      </div>
    </section>""")

    corpo = f"""<body>
{NAVBAR}

  <main id="main-content">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><span>Consultoria de SEO por cidade</span></nav>
          <div class="eyebrow">Brasil inteiro, online</div>
          <h1 class="page-title">Consultoria de SEO por cidade: apareça no Google onde seus clientes estão</h1>
          <p class="page-subtitle">A RCB atende empresas de todo o Brasil com consultoria online de SEO e Google Meu Negócio — o mesmo método do atendimento presencial em Goiânia, por vídeo e com acesso aos seus dados reais do Google. Escolha a sua cidade abaixo e veja os números do seu mercado: quantas empresas existem, quantas abriram nos últimos meses e em quais ramos a concorrência mais cresce.</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="/diagnostico-presenca-digital/" data-event="cta_click" data-location="hero" data-page="hub-cidades">Solicitar diagnóstico gratuito</a>
          </div>
        </div>
        <aside class="page-hero-panel">
          <h2>Como funciona o atendimento online</h2>
          <ul class="audit-list">
            <li>Reuniões por vídeo, no seu horário.</li>
            <li>Análise dos seus dados reais do Google.</li>
            <li>Implementação guiada, passo a passo.</li>
            <li>Relatórios simples de entender.</li>
          </ul>
        </aside>
      </div>
    </section>

{chr(10).join(blocos)}

    <section class="cta-band" aria-labelledby="cta-titulo">
      <div class="container">
        <div class="cta-inner">
          <div class="section-tag">Sua cidade não está na lista?</div>
          <h2 id="cta-titulo" class="section-title">Atendo qualquer cidade do Brasil</h2>
          <p>As páginas acima cobrem as 200 maiores cidades do país, mas o atendimento online funciona em qualquer lugar. Fale comigo e conte onde fica a sua empresa.</p>
          <a class="btn btn-primary" href="https://wa.me/{WHATS}?text={quote('Olá, Renan. Quero aparecer melhor no Google. Minha cidade: ')}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="final" data-page="hub-cidades">Chamar no WhatsApp</a>
        </div>
      </div>
    </section>
  </main>

"""
    return head_comum(titulo, desc, canonical, schema) + "\n" + corpo + rodape("hub-cidades")


def main():
    cidades = carregar_cidades()
    print(f"{len(cidades)} cidades carregadas (Goiânia excluída de propósito).")

    por_uf = {}
    for c in cidades:
        por_uf.setdefault(c["uf"], []).append(c)

    urls = []
    for c in cidades:
        mesmas = [v for v in por_uf[c["uf"]] if v["slug"] != c["slug"]][:6]
        html = pagina_cidade(c, mesmas)
        destino = os.path.join(RAIZ, "consultoria-seo", c["slug"])
        os.makedirs(destino, exist_ok=True)
        with open(os.path.join(destino, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        urls.append(f"{BASE_URL}/consultoria-seo/{c['slug']}/")

    hub = pagina_hub(cidades)
    with open(os.path.join(RAIZ, "consultoria-seo", "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(hub)

    print(f"Geradas {len(urls)} páginas de cidade + 1 hub em /consultoria-seo/.")
    return urls


if __name__ == "__main__":
    main()
