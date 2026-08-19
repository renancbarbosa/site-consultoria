# -*- coding: utf-8 -*-
"""
Gera as páginas de cidade em /consultoria-seo/<slug>/ usando os dados de CNPJ
do projeto SITE-DADOS (C:/Users/renan/SITE-DADOS/data/cidades/*.json).

Cada página recebe dados únicos da cidade (empresas ativas, aberturas recentes,
ramos que mais crescem, bairros) para não ser página repetida.

Uso:  python scripts/gerar-paginas-cidades.py
Goiânia é pulada de propósito: a cidade já tem /seo-local-goiania/ e
/consultor-seo-goiania/ — gerar outra página criaria concorrência interna.

╔══════════════════════════════════════════════════════════════════════════╗
║  EXPANSÃO SUSPENSA — decisão estratégica de 12/08/2026                    ║
╚══════════════════════════════════════════════════════════════════════════╝
NÃO gere cidade nova até a revisão estratégica das 199 já publicadas.

Motivo (medido em 11/08/2026, relatório completo no raio-X comercial):
  - duas cidades quaisquer são ~89,5% idênticas palavra a palavra;
  - 63% do texto de uma página se repete em 90%+ das outras;
  - o que muda entre uma cidade e outra é o nome, a sigla do estado e
    quatro números.
Isso já se encaixa na definição de página-porta do Google, e as 199 são dois
terços do site. Publicar mais cidades agrava exatamente esse problema.

Este script continua funcionando normalmente para ATUALIZAR as 199 existentes
(preço, links, texto) — é isso que ele faz por padrão. A trava é a variável
EXPANDIR_CIDADES: sem RCB_EXPANDIR_CIDADES=1, cidade que ainda não tem pasta
publicada é ignorada. Não remova essa trava sem decisão editorial.

Triagem das 199 para manter/reescrever/noindex: docs/triagem-cidades.md
"""
import json
import os
import sys
import glob
import hashlib
import re
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rcb_pacotes import bloco_cta_mobile, bloco_pacotes, ofertas_json_compacto
from rcb_cidades import INDEXAVEIS, PILOTO, SLUG_CANONICO, eh_indexavel
from conteudo.cidades_piloto import PILOTOS

DADOS = r"C:/Users/renan/SITE-DADOS/data/cidades"
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE_URL = "https://rcbseo.com.br"
WHATS = "5562991161040"
EXPANDIR_CIDADES = os.environ.get("RCB_EXPANDIR_CIDADES") == "1"
ATUALIZADO_INDEXAVEIS = "2026-08-15"

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


# ---------------------------------------------------------------------------
# Anchors dos links internos para as money pages (arquitetura de 12/08/2026).
#
# Por que variar: 199 paginas com o MESMO anchor exato viram padrao obvio de
# geracao automatica. A variacao e deterministica (hash do slug), entao a
# regeracao devolve sempre o mesmo texto para a mesma cidade -- o anchor nao
# fica trocando a cada build.
#
# Por que Goiania NAO entra aqui: linkar "consultor de SEO em Goiania" de uma
# pagina de Recife e incoerente para o leitor e reforca o footprint. Goiania so
# aparece nas cidades do proprio entorno (ver GO_PROXIMAS).
# ---------------------------------------------------------------------------
ANCHOR_VARIANTES = {
    "/google-perfil-empresa/": [
        "otimização do Google Perfil da Empresa",
        "trabalho no Google Perfil da Empresa",
        "Google Perfil da Empresa (o antigo Google Meu Negócio)",
        "otimização do perfil no Google Meu Negócio",
    ],
    # ATENCAO: estas variantes entram na frase "E a mesma ___ aplicada nos
    # atendimentos presenciais". Todas precisam ser substantivos FEMININOS, ou
    # a concordancia quebra ("a mesma trabalho ... aplicada"). Ja aconteceu.
    "/consultoria-seo-local/": [
        "consultoria de SEO local",
        "estratégia de SEO local",
        "metodologia de SEO local",
        "consultoria de SEO local para quem atende por região",
    ],
    "/cases/": [
        "resultados reais de clientes",
        "resultados que já entreguei",
        "cases de clientes reais",
        "resultados de clientes atendidos",
    ],
}

# Cidades onde citar Goiania faz sentido geografico: Goias e o entorno do DF.
# Fora daqui, nenhuma pagina de cidade linka para as paginas de Goiania.
GO_PROXIMAS = {"GO", "DF"}


def anchor(slug, destino):
    """Texto do link para `destino`, escolhido de forma estavel pelo slug."""
    op = ANCHOR_VARIANTES[destino]
    return op[variante(slug + destino, len(op))]


def link(slug, destino):
    return f'<a href="{destino}">{anchor(slug, destino)}</a>'


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
                # Colisao entre estados. Por padrao vira `slug-uf`, MAS quando a
                # URL ja publicada pertence comprovadamente a uma das cidades, o
                # mapa SLUG_CANONICO manda. Caso real: /consultoria-seo/palmas/
                # sempre foi Palmas/TO (titulo, schema e numeros publicados sao
                # de TO); sem este mapa as duas viravam palmas-to e palmas-pr,
                # nenhuma casava com a pasta publicada e a pagina ficava orfa da
                # geracao, congelada no conteudo de 15/07/2026.
                fixo = SLUG_CANONICO.get((s, c["uf"]))
                c["slug"] = fixo if fixo else f"{c['slug']}-{c['uf'].lower()}"

    # Por padrão, atualiza apenas URLs já publicadas. Isso impede que uma nova
    # carga de dados coloque centenas de páginas no ar sem revisão editorial.
    if not EXPANDIR_CIDADES:
        pasta_publicada = os.path.join(RAIZ, "consultoria-seo")
        publicados = {
            nome for nome in os.listdir(pasta_publicada)
            if os.path.isfile(os.path.join(pasta_publicada, nome, "index.html"))
        }
        antes = len(cidades)
        cidades = [c for c in cidades if c["slug"] in publicados]
        print(f"Expansão protegida: {antes - len(cidades)} cidades novas ficaram fora da geração.")
    return sorted(cidades, key=lambda c: -c["empresas_ativas"])


def head_comum(titulo, desc, canonical, schema_json, indexavel=True):
    # Poda de 12/08/2026: as cidades fora de rcb_cidades.INDEXAVEIS saem do
    # indice por meta robots. NAO usar nofollow (os links continuam valendo
    # para o leitor e para o rastreamento), NAO bloquear no robots.txt e NAO
    # redirecionar: o Google precisa RASTREAR a pagina para ver o noindex.
    # Bloquear no robots.txt faria o efeito contrario -- a URL ficaria no
    # indice sem o Google nunca ler a tag.
    robots = "index, follow" if indexavel else "noindex, follow"
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
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="pt-BR" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="RCB Consultoria">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://rcbseo.com.br/assets/img/og-rcb-1200x628.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="628">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{titulo}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://rcbseo.com.br/assets/img/og-rcb-1200x628.png">
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
  <nav class="navbar" id="navbar" role="navigation" aria-label="Menu principal"><div class="container nav-container"><a href="/" class="nav-logo" aria-label="Página inicial"><span class="logo-text">RCB</span><span class="logo-sub">SEO Local</span></a><button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="navMenu"><span></span><span></span><span></span></button><ul class="nav-menu" id="navMenu" role="list"><li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Serviços<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></button><div class="nav-dropdown-menu" role="menu"><a href="/consultoria-seo-local/" class="nav-dropdown-item" role="menuitem">Consultoria SEO Local</a><a href="/diagnostico-presenca-digital/" class="nav-dropdown-item" role="menuitem">Diagnóstico de Presença Digital</a><a href="/auditoria-seo/" class="nav-dropdown-item" role="menuitem">Auditoria SEO</a><a href="/google-perfil-empresa/" class="nav-dropdown-item" role="menuitem">Google Perfil da Empresa</a><a href="/site-otimizado-para-seo/" class="nav-dropdown-item" role="menuitem">Site otimizado para SEO</a><a href="/conteudo-para-seo/" class="nav-dropdown-item" role="menuitem">Conteúdo para SEO</a><a href="/acompanhamento-seo/" class="nav-dropdown-item" role="menuitem">Acompanhamento SEO</a></div></li><li class="nav-nicho-group"><button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Nichos<svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg></button><div class="nav-dropdown-menu" role="menu"><a href="/seo-para-clinicas/" class="nav-dropdown-item" role="menuitem">Clínicas</a><a href="/seo-para-dentistas/" class="nav-dropdown-item" role="menuitem">Dentistas</a><a href="/seo-para-clinicas-de-estetica/" class="nav-dropdown-item" role="menuitem">Estética</a><a href="/seo-para-medicos/" class="nav-dropdown-item" role="menuitem">Médicos</a><a href="/seo-para-clinicas-de-emagrecimento/" class="nav-dropdown-item" role="menuitem">Emagrecimento</a><a href="/para-advogados/" class="nav-dropdown-item" role="menuitem">Advogados</a><a href="/para-comercios-locais/" class="nav-dropdown-item" role="menuitem">Comércios locais</a><a href="/para-profissionais-liberais/" class="nav-dropdown-item" role="menuitem">Profissionais liberais</a></div></li><li><a href="/consultor-seo-goiania/" class="nav-link">Consultor SEO</a></li><li><a href="/blog/" class="nav-link">Blog</a></li><li><a href="/cases/" class="nav-link">Cases</a></li><li><a href="/sobre/" class="nav-link">Sobre</a></li><li><a href="/contato/" class="nav-link">Contato</a></li><li><a href="#pacotes" class="nav-link nav-cta" data-event="cta_click" data-location="navbar" data-page="cidade">Ver preços</a></li></ul></div></nav>"""


def rodape(pagina):
    return """  <footer class="footer" role="contentinfo"><div class="container footer-cols"><div class="footer-col footer-col-identity"><span class="logo-text">RCB</span><strong class="footer-name">Renan Carvalho Barbosa</strong><span class="footer-cargo">Consultor de SEO Local e Google Meu Negócio</span><p class="footer-bio">Com base em Goiânia e atendimento online para clínicas e negócios locais em todo o Brasil.</p></div><div class="footer-col"><h4 class="footer-col-title">Serviços</h4><nav class="footer-col-nav"><a href="/consultoria-seo-local/">Consultoria SEO Local</a><a href="/consultoria-seo/">Consultoria SEO por cidade</a><a href="/diagnostico-presenca-digital/">Diagnóstico de Presença Digital</a><a href="/auditoria-seo/">Auditoria de SEO</a><a href="/google-perfil-empresa/">Google Perfil da Empresa</a><a href="/site-otimizado-para-seo/">Site otimizado para SEO</a><a href="/acompanhamento-seo/">Acompanhamento de SEO</a></nav></div><div class="footer-col"><h4 class="footer-col-title">Nichos</h4><nav class="footer-col-nav"><a href="/seo-para-clinicas/">Clínicas</a><a href="/seo-para-dentistas/">Dentistas</a><a href="/seo-para-clinicas-de-estetica/">Estética</a><a href="/seo-para-medicos/">Médicos</a><a href="/para-advogados/">Advogados</a></nav></div><div class="footer-col"><h4 class="footer-col-title">Contato</h4><div class="footer-col-contact"><a href="/contato/">Página de contato</a><a href="https://wa.me/""" + WHATS + """\" target="_blank" rel="noopener noreferrer">WhatsApp: (62) 99116-1040</a><a href="mailto:contato@rcbseo.com.br">contato@rcbseo.com.br</a><span>Rua 18-A, nº 256 — Goiânia - GO, CEP 74070-060</span></div></div></div><div class="footer-bottom"><div class="container footer-bottom-inner"><p>&copy; <span id="anoAtual"></span> Renan Carvalho Barbosa. Todos os direitos reservados.</p><a href="/privacidade/" class="footer-privacy">Política de Privacidade</a><a href="/cookies/" class="footer-privacy" style="margin-left:1rem;">Política de Cookies</a></div></div></footer>
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
    "Quer saber por que sua empresa em {cidade} não aparece no Google — e o que fazer para mudar isso? Me chame no WhatsApp e me diga o que você vende. Eu procuro como se fosse seu cliente e te mostro quem está aparecendo no seu lugar.",
    "Me mande uma mensagem contando o que a sua empresa faz em {cidade}. Eu olho seu perfil no Google, seu site e os concorrentes que aparecem na sua frente, e digo com franqueza o que priorizar — antes de qualquer proposta.",
]


TITULOS_LEITURA_LOCAL = [
    "O retrato de {cidade} antes de escolher palavras-chave",
    "O que os números locais mudam na estratégia",
    "Uma leitura prática do mercado de {cidade}",
    "Onde a disputa local começa em {cidade}",
    "Dados de {cidade} que merecem virar decisão",
    "Antes do conteúdo: o contexto comercial de {cidade}",
    "Como transformar dados de {cidade} em prioridade",
    "O recorte local que uma página genérica não mostra",
]


def bloco_leitura_indexavel(c):
    """Cria ganho de informação verificável apenas nas 28 antigas congeladas.

    A camada usa exclusivamente o snapshot de CNPJ que já alimenta a página.
    Não presume demanda de busca, escritório local, clientes ou equipe na cidade.
    """
    slug = c["slug"]
    if slug not in INDEXAVEIS or slug in PILOTO:
        return ""

    cidade = c["cidade"]
    ativas = int(c.get("empresas_ativas", 0) or 0)
    abertas_90d = int(c.get("abertas_90d", 0) or 0)
    abertas_12m = int(c.get("abertas_12m", 0) or 0)
    abertas_mes = int(c.get("abertas_mes", 0) or 0)
    variacao = float(c.get("variacao_mes_anterior_pct", 0) or 0)
    ramos = c.get("ramos_top", [])
    bairros = c.get("bairros_top", [])
    ramo1 = ramos[0] if ramos else {"nome": "serviços locais", "abertas_90d": 0}
    ramo2 = ramos[1] if len(ramos) > 1 else ramo1
    bairro1 = bairros[0] if bairros else {"bairro": "área central", "abertas_90d": 0}
    bairro2 = bairros[1] if len(bairros) > 1 else bairro1
    taxa_mil = round((abertas_90d / ativas * 1000), 1) if ativas else 0
    fatia_lider = round((int(ramo1.get("abertas_90d", 0)) / abertas_90d * 100), 1) if abertas_90d else 0

    nome_ramo1 = rotulo_cnae(ramo1.get("nome", "serviços locais"))
    nome_ramo2 = rotulo_cnae(ramo2.get("nome", "serviços locais"))
    nome_bairro1 = limpar_bairro(bairro1.get("bairro", "área central"))
    nome_bairro2 = limpar_bairro(bairro2.get("bairro", "área central"))
    modo = variante(slug + "-leitura-local", 8)
    titulo = TITULOS_LEITURA_LOCAL[modo].format(cidade=cidade)

    r1 = n_br(ramo1.get("abertas_90d", 0))
    r2 = n_br(ramo2.get("abertas_90d", 0))
    b1 = n_br(bairro1.get("abertas_90d", 0))
    b2 = n_br(bairro2.get("abertas_90d", 0))

    # Oito leituras escritas com estruturas diferentes. Não é rotação de
    # adjetivo: cada modo ensina uma forma distinta de transformar os mesmos
    # dados verificáveis em hipótese de SEO a ser confirmada no projeto.
    narrativas = [
        [
            f"{cidade} tem {n_br(ativas)} empresas ativas no recorte. Em 90 dias surgiram <strong>{n_br(abertas_90d)}</strong> novos registros — {n_br(taxa_mil)} para cada mil empresas já abertas. O número dá escala ao mercado cadastral, mas ainda não diz quantas pessoas pesquisam um serviço no Google.",
            f"A liderança ficou com {nome_ramo1}: {r1} aberturas, ou {n_br(fatia_lider)}% do total recente. {nome_ramo2} veio depois, com {r2}. Para uma estratégia, isso vira uma lista de segmentos a investigar, não uma autorização para criar páginas sem cliente, oferta ou prova.",
            f"A distribuição também merece lupa. {nome_bairro1} aparece com {b1} registros e {nome_bairro2} com {b2}. O teste útil é medir a visibilidade a partir desses pontos e comparar a composição do mapa; repetir os bairros no texto não altera a distância real.",
            f"O mês fechou com {n_br(abertas_mes)} aberturas, variação de {n_br(variacao)}% sobre o anterior. Em 12 meses foram {n_br(abertas_12m)}. A página registra esse contexto e deixa a promessa de lado: demanda, clique e contato só entram depois de medidos.",
        ],
        [
            f"Começo pelo segmento, porque uma cidade grande demais vira uma abstração. Em {cidade}, {nome_ramo1} somou <strong>{r1} novos CNPJs</strong> em 90 dias; {nome_ramo2}, {r2}. O primeiro representa {n_br(fatia_lider)}% das {n_br(abertas_90d)} aberturas registradas.",
            f"Esse dado ajuda a formular perguntas. Há mais concorrentes publicando? O pacote local é dominado por redes, profissionais ou empresas antigas? Quais serviços aparecem nas consultas? A resposta vem do Maps e do Search Console do negócio — não da tabela de CNPJ sozinha.",
            f"No território, {nome_bairro1} concentrou {b1} aberturas informadas e {nome_bairro2}, {b2}. São pontos de observação para uma grade de busca. Só devem aparecer como área atendida quando a operação realmente chega até lá.",
            f"A base inteira reúne {n_br(ativas)} empresas. O ritmo recente foi de {n_br(taxa_mil)} aberturas por mil ativas em 90 dias, com {n_br(abertas_mes)} no último mês. É contexto competitivo mensurável; posição orgânica continua sendo outra medição.",
        ],
        [
            f"Uma estratégia local para {cidade} não deveria começar com uma lista de palavras-chave. Deveria começar com um mapa. Os cadastros recentes apontam {nome_bairro1} ({b1} aberturas) e {nome_bairro2} ({b2}) como dois pontos que merecem observação.",
            f"Observar não é criar uma falsa unidade. É pesquisar o serviço a partir de locais reais, anotar quais empresas entram no mapa e conferir se distância, categoria e reputação mudam o cenário. A página não afirma atendimento em bairro que não foi confirmado pelo negócio.",
            f"No recorte econômico, foram {n_br(abertas_90d)} aberturas em 90 dias diante de {n_br(ativas)} empresas ativas. A razão de {n_br(taxa_mil)} por mil ajuda a dimensionar renovação cadastral, sem confundir abertura de empresa com procura no Google.",
            f"{nome_ramo1} liderou com {r1} registros; {nome_ramo2} teve {r2}. Junto ao total anual de {n_br(abertas_12m)}, esses dados dizem onde vale investigar primeiro. Quem decide a página final são oferta, evidência e intenção de busca.",
        ],
        [
            f"O dado mais recente de {cidade} é {n_br(abertas_mes)} novas empresas no mês. A variação foi de <strong>{n_br(variacao)}%</strong> em relação ao anterior. Oscilação mensal pede cautela; por isso a leitura também olha {n_br(abertas_90d)} aberturas no trimestre e {n_br(abertas_12m)} no ano.",
            f"Quando esse volume é comparado às {n_br(ativas)} empresas ativas, chega-se a {n_br(taxa_mil)} novos cadastros por mil em 90 dias. É uma métrica de ritmo da base, não uma previsão de tráfego e muito menos de vendas.",
            f"Nos ramos, {nome_ramo1} registrou {r1} aberturas e {nome_ramo2}, {r2}. A concentração do líder foi de {n_br(fatia_lider)}%. Uma consultoria pode usar isso para selecionar amostras de concorrentes; produzir conteúdo antes dessa checagem seria inverter a ordem.",
            f"{nome_bairro1} e {nome_bairro2} aparecem com {b1} e {b2} cadastros. Se o negócio atende esses locais, vale medir; se não atende, os nomes ficam fora da oferta. SEO local não transforma alcance desejado em presença física.",
        ],
        [
            f"Nos últimos 90 dias, a base de {cidade} ganhou {n_br(abertas_90d)} registros. Diante das {n_br(ativas)} empresas ativas, são {n_br(taxa_mil)} aberturas por mil. Para quem já está no mercado, o dado sugere renovação competitiva que precisa ser acompanhada, não temida.",
            f"Dois grupos ajudam a montar a amostra: {nome_ramo1}, com {r1} aberturas, e {nome_ramo2}, com {r2}. O líder responde por {n_br(fatia_lider)}% do total recente. A análise seguinte é manual: títulos, páginas, avaliações, categorias e facilidade de contato dos resultados visíveis.",
            f"O componente geográfico começa em {nome_bairro1} ({b1}) e {nome_bairro2} ({b2}). Esses números mostram onde empresas foram cadastradas; não mostram onde o cliente estava nem qual resultado ele clicou.",
            f"Com {n_br(abertas_mes)} aberturas no mês e {n_br(abertas_12m)} no ano, há dados suficientes para evitar uma página vazia. Ainda faltam os dados decisivos do projeto: consultas, impressões, posição por região e conversões.",
        ],
        [
            f"A melhor utilidade dos dados de {cidade} é desenhar uma medição. A cidade reúne {n_br(ativas)} empresas ativas e recebeu {n_br(abertas_90d)} registros em 90 dias. Isso equivale a {n_br(taxa_mil)} por mil — uma linha de base objetiva para o contexto cadastral.",
            f"Para o recorte por atividade, começaria com {nome_ramo1} ({r1} aberturas) e {nome_ramo2} ({r2}). O primeiro concentra {n_br(fatia_lider)}% das aberturas. Depois, separaria buscas de marca, serviço, problema e preço para não misturar intenções.",
            f"Na leitura espacial, {nome_bairro1} tem {b1} registros recentes e {nome_bairro2}, {b2}. Uma grade local pode comparar os resultados nesses pontos, desde que a empresa confirme que atende a região. Nome de bairro não é palavra para espalhar; é coordenada para testar.",
            f"O movimento mensal foi de {n_br(abertas_mes)}, com variação de {n_br(variacao)}%. O acumulado de 12 meses chegou a {n_br(abertas_12m)}. A estratégia só avança quando esse contexto encontra os dados do próprio negócio.",
        ],
        [
            f"Em {cidade}, o mapa de conteúdo deve nascer da oferta, mas os dados ajudam a escolher a ordem. Foram {n_br(abertas_90d)} aberturas em 90 dias e {n_br(abertas_12m)} em 12 meses, sobre uma base de {n_br(ativas)} empresas ativas.",
            f"{nome_ramo1} aparece na frente, com {r1} registros; {nome_ramo2} soma {r2}. A fatia do primeiro é de {n_br(fatia_lider)}%. Se a empresa vende para um desses mercados, vale cruzar a informação com as consultas existentes antes de escrever uma nova landing page.",
            f"{nome_bairro1}, com {b1} aberturas, e {nome_bairro2}, com {b2}, podem orientar exemplos e testes de cobertura. Eles não devem gerar duas cópias da mesma página. Uma URL forte por intenção é preferível a uma coleção de portas de entrada quase iguais.",
            f"O último mês adicionou {n_br(abertas_mes)} cadastros e variou {n_br(variacao)}%. Esse ritmo é informação de apoio. O conteúdo principal continua precisando responder serviço, processo, prova, atendimento e próxima ação em linguagem direta.",
        ],
        [
            f"A pergunta comercial em {cidade} não é “quantas vezes repetir a cidade?”. É “qual combinação de perfil, página e reputação vence em cada ponto?”. A base traz {n_br(ativas)} empresas ativas e {n_br(abertas_90d)} novas em 90 dias para enquadrar a concorrência.",
            f"O ritmo equivale a {n_br(taxa_mil)} cadastros por mil empresas. No mês foram {n_br(abertas_mes)}, com variação de {n_br(variacao)}%; em 12 meses, {n_br(abertas_12m)}. Nenhum desses números substitui uma consulta de busca, mas todos tornam o diagnóstico menos genérico.",
            f"{nome_ramo1} liderou as aberturas com {r1} ({n_br(fatia_lider)}% do período), seguido por {nome_ramo2}, com {r2}. Esses segmentos servem para observar padrões de página e perfil, não para afirmar que são os mais pesquisados.",
            f"Na camada geográfica, {nome_bairro1} registra {b1} aberturas e {nome_bairro2}, {b2}. A empresa só disputa esses pontos de forma legítima quando existe atendimento real; o restante é medição e planejamento, não alegação de presença.",
        ],
    ]
    paragrafos = "\n          ".join(f"<p>{p}</p>" for p in narrativas[modo])

    enfoques = [
        "validar quais serviços realmente geram impressão no Search Console antes de abrir outra URL",
        "comparar categoria, avaliações, páginas e conversão dos concorrentes que aparecem no mapa",
        "dar uma página própria somente aos serviços que têm oferta, prova e capacidade de atendimento",
        "medir separadamente busca pela marca, busca pelo serviço e ações de contato",
        "ligar o Perfil da Empresa à página mais específica para cada serviço prioritário",
        "revisar o que o cliente encontra no celular antes de ampliar a produção de conteúdo",
        "usar bairros como recorte de medição, nunca como endereço ou unidade inventada",
        "concentrar autoridade nas páginas que já recebem sinais antes de multiplicar variações",
    ]
    plano = enfoques[modo]

    return f"""
    <section class="solution-section" aria-labelledby="leitura-local-{slug}">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Leitura local verificável</div>
          <h2 id="leitura-local-{slug}" class="section-title">{titulo}</h2>
          {paragrafos}
        </div>
        <aside class="diagnostic-card">
          <h3>Primeira decisão para {cidade}</h3>
          <p>{plano.capitalize()}.</p>
          <ul class="check-list">
            <li><strong>Dado disponível:</strong> empresas, aberturas, ramos e bairros do CNPJ.</li>
            <li><strong>Dado ainda necessário:</strong> consultas, posição, cliques e contatos do negócio.</li>
            <li><strong>Limite da leitura:</strong> abertura de CNPJ não comprova procura no Google.</li>
          </ul>
        </aside>
      </div>
    </section>"""


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
    gerado_em = ATUALIZADO_INDEXAVEIS if eh_indexavel(slug) else c.get("gerado_em", ref)
    variacao = float(c.get("variacao_mes_anterior_pct", 0) or 0)
    porte = c.get("porte", {})

    titulo = f"Consultoria de SEO em {cidade} ({uf}) | Apareça no Google | RCB"
    if len(titulo) > 65:
        titulo = f"Consultoria de SEO em {cidade} ({uf}) | RCB"
    desc = (f"Sua empresa em {cidade} não aparece no Google? Consultoria online de SEO: "
            f"Google Meu Negócio, site e conteúdo. Diagnóstico gratuito.")

    ramos = [(rotulo_cnae(r["nome"]), r["abertas_90d"]) for r in c.get("ramos_top", [])[:6]]
    bairros = [(limpar_bairro(b["bairro"]), b["abertas_90d"]) for b in c.get("bairros_top", [])[:4]]

    if variacao > 5:
        leitura_ritmo = f"O ritmo de abertura acelerou <strong>{n_br(abs(variacao))}%</strong> em relação ao mês anterior."
    elif variacao < -5:
        leitura_ritmo = f"O ritmo de abertura recuou <strong>{n_br(abs(variacao))}%</strong> em relação ao mês anterior, mas {n90} negócios ainda abriram em 90 dias."
    else:
        leitura_ritmo = f"O ritmo de abertura ficou relativamente estável: variação de <strong>{n_br(variacao)}%</strong> em relação ao mês anterior."

    ramo_lider = ramos[0] if ramos else ("serviços locais", 0)
    leitura_mercado = (
        f"Entre as novas empresas, <strong>{ramo_lider[0]}</strong> liderou a lista, "
        f"com {n_br(ramo_lider[1])} aberturas em 90 dias. Isso não prova demanda de busca, "
        "mas sinaliza onde novos concorrentes podem disputar visibilidade local."
    )

    intro = INTROS[variante(slug, len(INTROS))].format(cidade=cidade)
    cta = CTAS[variante(slug + "x", len(CTAS))].format(cidade=cidade)
    leitura_indexavel = bloco_leitura_indexavel(c)

    whats_msg = quote(f"Olá, Renan. Tenho uma empresa em {cidade}/{uf} e quero saber como faço para aparecer melhor no Google.")
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
        '{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR","dateModified":"%s"},'
        '{"@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Início","item":"https://rcbseo.com.br/"},'
        '{"@type":"ListItem","position":2,"name":"Consultoria de SEO por cidade","item":"https://rcbseo.com.br/consultoria-seo/"},'
        '{"@type":"ListItem","position":3,"name":"%s","item":"%s"}]},'
        '{"@type":"Service","serviceType":"Consultoria de SEO","name":"Consultoria de SEO em %s","description":"Consultoria online de SEO e Google Meu Negócio para empresas de %s (%s). Diagnóstico, otimização do perfil no Google, site e conteúdo.",'
        '"provider":{"@type":"LocalBusiness","@id":"https://rcbseo.com.br/#business"},'
        '"areaServed":{"@type":"City","name":"%s","containedInPlace":{"@type":"State","name":"%s"}},'
        '"offers":' + ofertas_json_compacto() + '},'
        '{"@type":"FAQPage","mainEntity":[%s]}]}'
    ) % (canonical, titulo, desc.replace('"', "'"), gerado_em, cidade, canonical, cidade, cidade, uf, cidade, estado, faq_schema)

    ramos_html = "\n".join(
        f'            <li>{nome} — <strong>{n_br(qtd)}</strong> novas em 90 dias</li>' for nome, qtd in ramos
    )
    bairros_html = ""
    if bairros:
        bairros_itens = "".join(
            f"<li><strong>{nome}</strong>: {n_br(qtd)} novas empresas em 90 dias</li>"
            for nome, qtd in bairros
        )
        bairros_html = f"""
          <h3>Bairros com mais aberturas recentes</h3>
          <ul class="audit-list">{bairros_itens}</ul>
          <p>Esses números mostram concentração de novas empresas, não posição no Google. A concorrência de busca precisa ser confirmada no diagnóstico do seu segmento.</p>"""

    porte_itens = "".join(
        f"<li><strong>{rotulo}</strong>: {n_br(porte.get(chave, 0))} aberturas em 90 dias</li>"
        for chave, rotulo in (("MEI", "MEI"), ("ME", "Microempresa"), ("EPP", "Empresa de pequeno porte"))
        if porte.get(chave) is not None
    )

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

    # Pacotes e barra de CTA vem do rcb_pacotes.py (fonte unica do preco).
    bloco_precos = bloco_pacotes("um negócio", f"cidade-{slug}", f" em {cidade}")
    barra_mobile = bloco_cta_mobile(f"cidade-{slug}")

    # Links internos para as money pages, em slots que ja existiam no texto.
    # Nenhum link novo foi acrescentado ao template: os tres abaixo entram em
    # frases que ja estavam la, e o CTA secundario do hero deixou de apontar
    # para /diagnostico-presenca-digital/ (289 links internos, rebaixada a
    # passo 2 do funil em 09/08) e passou a apontar para /cases/ (tinha 6).
    link_gmn = link(slug, "/google-perfil-empresa/")
    link_consultoria = link(slug, "/consultoria-seo-local/")
    # /cases/ entra UMA vez por pagina, pelo botao do hero. Ele ja e o link mais
    # visivel da pagina; repetir no texto do metodo criava duas ancoras para a
    # mesma URL sem ganho -- o Google costuma considerar so a primeira.

    # Goiania so aparece nas cidades do proprio entorno (GO e DF). Em Recife ou
    # Blumenau, esse link seria incoerente para o leitor e so engrossaria o
    # padrao programatico.
    goiania_html = ""
    if uf in GO_PROXIMAS:
        goiania_html = (
            f' Como {cidade} fica perto da minha base, o atendimento pode ser presencial:'
            f' veja o trabalho de <a href="/seo-local-goiania/">SEO local em Goiânia</a>'
            f' e quem é o <a href="/consultor-seo-goiania/">consultor de SEO em Goiânia</a>'
            f' por trás dele.'
        )

    corpo = f"""<body class="tem-cta-mobile">
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
            <a class="btn btn-primary" href="{whats_url}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero_whatsapp" data-page="cidade-{slug}">Quero analisar minha empresa em {cidade}</a>
            <a class="btn btn-outline" href="/cases/" data-event="cta_click" data-location="hero_secundario" data-page="cidade-{slug}">Ver resultados de clientes reais</a>
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
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Fonte: <a href="https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj" target="_blank" rel="noopener noreferrer">dados públicos de CNPJ da Receita Federal</a>, referência {ref}. Página atualizada em {gerado_em}.</p>
        </aside>
      </div>
    </section>{leitura_indexavel}

    <section class="solution-section" aria-labelledby="concorrencia-titulo">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Por que agir agora</div>
          <h2 id="concorrencia-titulo" class="section-title">O que os dados de {cidade} dizem — e o que ainda precisa ser medido</h2>
          <p>{cidade} ganhou <strong>{n90} novas empresas nos últimos 90 dias</strong>. {leitura_ritmo}</p>
          <p>{leitura_mercado}</p>{bairros_html}
          <p>Esses dados dimensionam o mercado, mas não substituem a análise do Google. No diagnóstico, eu verifico as buscas do seu serviço, o Maps, seu site e os concorrentes que realmente aparecem na sua frente.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Ramos que mais abriram empresas em {cidade} (90 dias)</h3>
          <ul class="audit-list">
{ramos_html}
          </ul>
          <h3 style="margin-top:1.25rem;">Porte das empresas abertas</h3>
          <ul class="audit-list">{porte_itens}</ul>
        </div>
      </div>
    </section>

    <section class="metodo" aria-labelledby="metodo-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Como funciona</div>
          <h2 id="metodo-titulo" class="section-title">Consultoria online para {cidade}, com método testado</h2>
          <p class="section-desc">Todo o trabalho é feito a distância, por vídeo e com acesso aos seus dados reais do Google. É a mesma {link_consultoria} aplicada nos atendimentos presenciais.</p>
        </div>
        <div class="metodo-steps">
          <div class="metodo-step"><div class="step-number">1</div><h3>Diagnóstico</h3><p>Analiso como sua empresa aparece hoje no Google e no Maps em {cidade}, e quais concorrentes aparecem na sua frente.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">2</div><h3>Perfil no Google</h3><p>Faço a {link_gmn}: categorias, serviços, fotos, postagens e estratégia de avaliações.</p></div>
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
          <p class="section-desc">O nicho mais maduro da RCB é saúde: <a href="/seo-para-clinicas/">clínicas</a>, <a href="/seo-para-dentistas/">dentistas</a>, <a href="/seo-para-clinicas-de-estetica/">estética</a> e <a href="/seo-para-medicos/">médicos</a>. Também atendo <a href="/para-comercios-locais/">comércios locais</a>, <a href="/para-profissionais-liberais/">profissionais liberais</a> e <a href="/para-advogados/">advogados</a>.{goiania_html}</p>
        </div>
      </div>
    </section>

{bloco_precos}
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
          <div class="section-tag">Fale comigo</div>
          <h2 id="cta-titulo" class="section-title">Quer aparecer no Google em {cidade}?</h2>
          <p>{cta}</p>
          <a class="btn btn-primary" href="{whats_url}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="final_whatsapp" data-page="cidade-{slug}">Falar no WhatsApp</a>
        </div>
      </div>
    </section>
{vizinhas_html}
  </main>

"""
    flutuante = f"""{barra_mobile}  <a href="{whats_url}" class="whatsapp-float" data-event="cta_click" data-location="whatsapp_flutuante" data-page="cidade-{slug}" target="_blank" rel="noopener noreferrer" aria-label="Chamar no WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="white" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
"""
    return (head_comum(titulo, desc, canonical, schema, eh_indexavel(slug))
            + "\n" + corpo + flutuante + rodape(f"cidade-{slug}"))


def pagina_cidade_piloto(c, vizinhas):
    """Pagina de cidade com conteudo local proprio (Rio, Campinas, Palmas).

    Estrutura DIFERENTE do template das demais: hero proprio, secoes escritas
    para a praca, FAQ propria. So o involucro (head, navbar, precos, rodape) e
    compartilhado -- e isso e proposital: preco e navegacao precisam ser iguais
    no site inteiro.
    """
    slug = c["slug"]
    cidade = c["cidade"]
    uf = c["uf"]
    estado = ESTADOS.get(uf, uf)
    canonical = f"{BASE_URL}/consultoria-seo/{slug}/"
    ref = c.get("data_referencia", c.get("snapshot", ""))
    gerado_em = ATUALIZADO_INDEXAVEIS

    ramos = [(rotulo_cnae(r["nome"]), r["abertas_90d"]) for r in c.get("ramos_top", [])[:6]]
    bairros = [(limpar_bairro(b["bairro"]), b["abertas_90d"]) for b in c.get("bairros_top", [])[:4]]
    bairros_lista = "<ul class=\"audit-list\">" + "".join(
        f"<li><strong>{nome}</strong>: {n_br(qtd)} novas empresas em 90 dias</li>"
        for nome, qtd in bairros
    ) + "</ul>" if bairros else ""

    ctx = {
        "cidade": cidade,
        "uf": uf,
        "estado": estado,
        "ativas": n_br(c["empresas_ativas"]),
        "n90": n_br(c["abertas_90d"]),
        "n12": n_br(c["abertas_12m"]),
        "ref": ref,
        "ramos_html": "\n".join(
            f'            <li>{nome} — <strong>{n_br(qtd)}</strong> novas em 90 dias</li>'
            for nome, qtd in ramos
        ),
        "bairros_lista": bairros_lista,
        "link_gmn": link(slug, "/google-perfil-empresa/"),
        "link_consultoria": link(slug, "/consultoria-seo-local/"),
        "link_cases": link(slug, "/cases/"),
    }

    p = PILOTOS[slug](ctx)

    whats_url = f"https://wa.me/{WHATS}?text={quote(p['whats'])}"

    faq_schema = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (q.replace('"', "'"), a.replace('"', "'"))
        for q, a in p["faq"]
    )

    schema = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR","dateModified":"%s"},'
        '{"@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Início","item":"https://rcbseo.com.br/"},'
        '{"@type":"ListItem","position":2,"name":"Consultoria de SEO por cidade","item":"https://rcbseo.com.br/consultoria-seo/"},'
        '{"@type":"ListItem","position":3,"name":"%s","item":"%s"}]},'
        '{"@type":"Service","serviceType":"Consultoria de SEO","name":"%s","description":"%s",'
        '"provider":{"@type":"LocalBusiness","@id":"https://rcbseo.com.br/#business"},'
        '"areaServed":{"@type":"City","name":"%s","containedInPlace":{"@type":"State","name":"%s"}},'
        '"offers":' + ofertas_json_compacto() + '},'
        '{"@type":"FAQPage","mainEntity":[%s]}]}'
    ) % (canonical, p["titulo"], p["desc"].replace('"', "'"), gerado_em, cidade, canonical,
         p["titulo"].split(" | ")[0], p["desc"].replace('"', "'"), cidade, estado, faq_schema)

    faq_html = "\n".join(
        f"""          <div class="faq-card">
            <h3>{q}</h3>
            <p>{a}</p>
          </div>""" for q, a in p["faq"]
    )

    vizinhas_html = ""
    if vizinhas:
        links = " · ".join(f'<a href="/consultoria-seo/{v["slug"]}/">{v["cidade"]}</a>' for v in vizinhas)
        vizinhas_html = f"""
    <section class="solution-section" aria-label="Outras cidades atendidas">
      <div class="container">
        <p class="section-desc">Também atendo outras cidades de {estado} e região: {links}. Veja <a href="/consultoria-seo/">todas as cidades atendidas</a>.</p>
      </div>
    </section>"""

    bloco_precos = bloco_pacotes("um negócio", f"cidade-{slug}", f" em {cidade}")
    barra_mobile = bloco_cta_mobile(f"cidade-{slug}")

    corpo = f"""<body class="tem-cta-mobile">
{NAVBAR}

  <main id="main-content">

    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><a href="/consultoria-seo/">Cidades</a><span>/</span><span>{cidade}</span></nav>
          <div class="eyebrow">{p['eyebrow']}</div>
          <h1 class="page-title">{p['h1']}</h1>
          <p class="page-subtitle">{p['subtitulo']}</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="{whats_url}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero_whatsapp" data-page="cidade-{slug}">Quero analisar minha empresa em {cidade}</a>
            <a class="btn btn-outline" href="/cases/" data-event="cta_click" data-location="hero_secundario" data-page="cidade-{slug}">Ver resultados de clientes reais</a>
          </div>
        </div>
        <aside class="page-hero-panel">
          <h2>{p['painel_titulo']}</h2>{p['painel_html']}
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Números de empresas: <a href="https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj" target="_blank" rel="noopener noreferrer">dados públicos de CNPJ</a>, referência {ref}. Página atualizada em {gerado_em}.</p>
        </aside>
      </div>
    </section>
{chr(10).join(p['secoes'])}

{bloco_precos}
    <section class="faq-section" aria-labelledby="faq-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">FAQ</div>
          <h2 id="faq-titulo" class="section-title">Perguntas frequentes sobre SEO em {cidade}</h2>
        </div>
        <div class="faq-grid">
{faq_html}
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="cta-titulo">
      <div class="container">
        <div class="cta-inner">
          <div class="section-tag">Fale comigo</div>
          <h2 id="cta-titulo" class="section-title">{p['cta_titulo']}</h2>
          <p>{p['cta_texto']}</p>
          <a class="btn btn-primary" href="{whats_url}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="final_whatsapp" data-page="cidade-{slug}">Falar no WhatsApp</a>
        </div>
      </div>
    </section>
{vizinhas_html}
  </main>

"""
    flutuante = f"""{barra_mobile}  <a href="{whats_url}" class="whatsapp-float" data-event="cta_click" data-location="whatsapp_flutuante" data-page="cidade-{slug}" target="_blank" rel="noopener noreferrer" aria-label="Chamar no WhatsApp"><svg width="30" height="30" viewBox="0 0 24 24" fill="white" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
"""
    return (head_comum(p["titulo"], p["desc"], canonical, schema, True)
            + "\n" + corpo + flutuante + rodape(f"cidade-{slug}"))


def pagina_hub(cidades):
    canonical = f"{BASE_URL}/consultoria-seo/"
    titulo = "Consultoria de SEO por Cidade | Todo o Brasil | RCB"
    desc = ("Consultoria de SEO e Google Meu Negócio com atendimento online para as maiores cidades do Brasil. "
            "Escolha a sua cidade e veja os dados do mercado local.")

    schema = (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebPage","url":"%s","name":"%s","description":"%s","inLanguage":"pt-BR"},'
        '{"@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"Início","item":"https://rcbseo.com.br/"},'
        '{"@type":"ListItem","position":2,"name":"Consultoria de SEO por cidade","item":"%s"}]},'
        '{"@type":"Service","serviceType":"Consultoria de SEO","name":"Site e Google Meu Neg\u00f3cio para neg\u00f3cios locais",'
        '"provider":{"@type":"LocalBusiness","@id":"https://rcbseo.com.br/#business"},'
        '"areaServed":{"@type":"Country","name":"Brasil"},'
        '"offers":' + ofertas_json_compacto() + '}]}'
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

    # Mesmos pacotes das paginas de cidade (fonte: rcb_pacotes.py).
    bloco_precos_hub = bloco_pacotes("um negócio", "hub-cidades")
    barra_mobile_hub = bloco_cta_mobile("hub-cidades")

    corpo = f"""<body class="tem-cta-mobile">
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
            <a class="btn btn-primary" href="https://wa.me/{WHATS}?text={quote('Olá, Renan! Vi seu site e quero saber como faço para minha empresa aparecer no Google.')}" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero" data-page="hub-cidades">Falar no WhatsApp</a>
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

{bloco_precos_hub}
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
    return head_comum(titulo, desc, canonical, schema) + "\n" + corpo + barra_mobile_hub + rodape("hub-cidades")


def atualizar_sitemap(cidades):
    """Sincroniza o sitemap com a decisao de 12/08/2026.

    Regra: so entram no sitemap as cidades de rcb_cidades.INDEXAVEIS (mais o
    hub). As demais sao REMOVIDAS -- pedir indexacao de pagina que carrega
    noindex e sinal contraditorio. Elas continuam no ar, com HTTP 200 e
    linkadas pelo hub, para que o Google as rastreie e leia a tag.

    Idempotente: rodar duas vezes seguidas nao muda mais nada.
    """
    caminho = os.path.join(RAIZ, "sitemap.xml")
    with open(caminho, encoding="utf-8") as f:
        conteudo = f.read()

    prefixo = f"{BASE_URL}/consultoria-seo/"
    datas = {
        f"{prefixo}{c['slug']}/": c.get("gerado_em", c.get("data_referencia", ""))
        for c in cidades
    }
    hub_data = max(datas.values()) if datas else ""

    # 1. remove do sitemap toda URL de cidade que nao e indexavel
    def manter(bloco):
        m = re.search(r"<loc>([^<]+)</loc>", bloco)
        if not m:
            return True
        url = m.group(1)
        if not url.startswith(prefixo) or url == prefixo:
            return True  # nao e pagina de cidade (ou e o hub): nao mexe
        slug = url[len(prefixo):].rstrip("/")
        return eh_indexavel(slug)

    blocos = re.findall(r"[ \t]*<url>.*?</url>\n?", conteudo, flags=re.S)
    removidos = 0
    for bloco in blocos:
        if not manter(bloco):
            conteudo = conteudo.replace(bloco, "", 1)
            removidos += 1

    # 2. atualiza lastmod das que ficaram
    for url, data in list(datas.items()) + [(prefixo, hub_data)]:
        if not data:
            continue
        slug = url[len(prefixo):].rstrip("/")
        if slug and not eh_indexavel(slug):
            continue
        padrao = rf"(<loc>{re.escape(url)}</loc>\s*<lastmod>)[^<]+"
        conteudo = re.sub(padrao, lambda m: m.group(1) + data, conteudo, count=1)

    # 3. garante que toda cidade indexavel esteja presente
    presentes = set(re.findall(r"<loc>([^<]+)</loc>", conteudo))
    faltando = []
    for c in cidades:
        url = f"{prefixo}{c['slug']}/"
        if eh_indexavel(c["slug"]) and url not in presentes:
            data = c.get("gerado_em", c.get("data_referencia", "")) or hub_data
            faltando.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{data}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>""")
    if faltando:
        conteudo = conteudo.replace("</urlset>", "\n".join(faltando) + "\n</urlset>")

    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(conteudo)

    total = len(re.findall(r"<loc>", conteudo))
    print(f"Sitemap: {removidos} URLs de cidade removidas (noindex), "
          f"{len(faltando)} acrescentadas. Total agora: {total}.")


def main():
    cidades = carregar_cidades()
    print(f"{len(cidades)} cidades carregadas (Goiânia excluída de propósito).")

    por_uf = {}
    for c in cidades:
        por_uf.setdefault(c["uf"], []).append(c)

    urls = []
    n_piloto = n_noindex = 0
    for c in cidades:
        mesmas = [v for v in por_uf[c["uf"]] if v["slug"] != c["slug"]][:6]
        if c["slug"] in PILOTO:
            html = pagina_cidade_piloto(c, mesmas)
            n_piloto += 1
        else:
            html = pagina_cidade(c, mesmas)
        if not eh_indexavel(c["slug"]):
            n_noindex += 1
        destino = os.path.join(RAIZ, "consultoria-seo", c["slug"])
        os.makedirs(destino, exist_ok=True)
        with open(os.path.join(destino, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        urls.append(f"{BASE_URL}/consultoria-seo/{c['slug']}/")

    hub = pagina_hub(cidades)
    with open(os.path.join(RAIZ, "consultoria-seo", "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(hub)

    atualizar_sitemap(cidades)

    print(f"Geradas {len(urls)} páginas de cidade + 1 hub em /consultoria-seo/.")
    print(f"  piloto (conteúdo local próprio): {n_piloto}")
    print(f"  com noindex                     : {n_noindex}")
    print(f"  indexáveis                      : {len(urls) - n_noindex}")
    return urls


if __name__ == "__main__":
    main()
