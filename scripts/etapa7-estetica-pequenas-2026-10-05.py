# -*- coding: utf-8 -*-
"""
Etapa 7 do plano de nichos (05/10/2026): fortalecer estetica e pequenas empresas.

Sem pagina nova e sem trocar titulo de pagina com trafego (seo-para-clinicas-de-estetica,
seo-para-pequenas-empresas, para-comercios-locais). Unico title trocado: o artigo de
estetica com "Goiania" no titulo, que passa a falar com a dona da clinica (URL mantida).

Cada troca exige que o texto antigo apareca exatamente uma vez; se o texto novo ja estiver
la, a troca e pulada (idempotente). Rode de novo: tem que dizer "alterados: 0".
Respeita a quebra de linha de cada arquivo (alguns misturam CRLF e LF).
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = "2026-10-05"
BYLINE = ('<p class="page-byline">Por <a href="/sobre/">Renan Carvalho Barbosa</a> · '
          'Atualizado em <time datetime="2026-10-05">05/10/2026</time></p>')
FONTE = 'target="_blank" rel="noopener noreferrer nofollow" data-fonte-oficial'
LEI_ESTETICISTA = ('<a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13643.htm" %s>'
                   'Lei nº 13.643/2018</a>' % FONTE)
CFM_2336 = ('<a href="https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2023/2336" %s>'
            'Resolução CFM 2.336/2023</a>' % FONTE)
GOOGLE_LOCAL = ('<a href="https://support.google.com/business/answer/7091?hl=pt-BR" %s>'
                'relevância, distância e destaque</a>' % FONTE)

ART_GYN = "blog/como-aparecer-google-clinica-estetica-goiania/index.html"
ART_GYN_TITULO = "Como atrair clientes para clínica de estética em Goiânia"
ART_GYN_H1 = "Como atrair clientes para sua clínica de estética em Goiânia pelo Google"
ART_GYN_DESC = ("Para a dona de clínica de estética em Goiânia: como atrair clientes pelo Google e "
                "pelo Maps, com perfil forte, avaliações e as regras do conselho em dia.")

TROCAS = {
    # ------------------------------------------------------------ SEO para estética
    "seo-para-clinicas-de-estetica/index.html": [
        ('"dateModified": "2026-09-08",', '"dateModified": "%s",' % HOJE),
        ('''"audience": {
        "@type": "MedicalAudience",
        "audienceType": "Clínicas de estética e profissionais autorizados"
      }''', '''"audience": {
        "@type": "BusinessAudience",
        "audienceType": "Clínicas de estética e profissionais de estética"
      }'''),
        ('data-page="seo-estetica">Ver preços e pacotes</a>', 'data-page="seo-estetica">Ver os pacotes</a>'),
        ('presencial em Goiânia e online no Brasil inteiro.</p>\n',
         'presencial em Goiânia e online no Brasil inteiro.</p>\n          %s\n' % BYLINE),
        ('Os dois cases abaixo são de segmentos diferentes de estética. Eles não garantem',
         'Os dois cases abaixo não são de estética: um é de uma confeitaria e o outro de uma orquestra de '
         'casamentos. Eles não garantem'),
        ('Esteticista (regulada pela Lei nº 13.643/2018) e médico estético (CFM/CRBM)',
         'Esteticista (regulada pela %s) e médico estético (CFM/CRBM)' % LEI_ESTETICISTA),
        ('O conselho competente varia conforme quem executa: CFM para médicos, CRBM para biomédicos, CRO para '
         'dentistas em harmonização orofacial, CRF para farmacêuticos e a Lei nº 13.643/2018 para esteticistas.',
         'O conselho competente varia conforme quem executa: CFM para médicos (a %s trata da publicidade médica), '
         'CRBM para biomédicos, CRO para dentistas em harmonização orofacial, CRF para farmacêuticos e a Lei nº '
         '13.643/2018 para esteticistas.' % CFM_2336),
        ('transmitem mais confiança do que banco de imagens — e o algoritmo do Google valoriza fotos recentes e '
         'frequentes.',
         'transmitem mais confiança do que banco de imagens — e foto recente mostra para quem pesquisa que a '
         'clínica está ativa.'),
        ('<a class="cluster-card" href="/blog/trafego-pago-para-clinicas/"><h3>Tráfego pago para clínicas</h3>'
         '<p>Anúncio no Google e no Instagram dentro das regras.</p></a>\n',
         '<a class="cluster-card" href="/blog/trafego-pago-para-clinicas/"><h3>Tráfego pago para clínicas</h3>'
         '<p>Anúncio no Google e no Instagram dentro das regras.</p></a>\n'
         '          <a class="cluster-card" href="/criacao-de-landing-page/"><h3>Landing page para anúncios</h3>'
         '<p>A página que recebe o clique e vira conversa no WhatsApp.</p></a>\n'
         '          <a class="cluster-card" href="/gestao-de-trafego-pago/"><h3>Gestão de Google Ads</h3>'
         '<p>Anúncio na pesquisa do Google para quem já decidiu fazer o procedimento.</p></a>\n'),
        ('<div class="cluster-grid">\n          <a class="cluster-card" href="/criacao-de-site-para-clinica-de-estetica/">',
         '<div class="cluster-grid cluster-grid-4">\n          <a class="cluster-card" '
         'href="/criacao-de-site-para-clinica-de-estetica/">'),
        ('<p class="section-desc">Aprofunde o tema: <a href="/blog/como-aparecer-google-clinica-estetica-goiania/">'
         'Como aparecer no Google quando alguém procura clínica de estética em Goiânia →</a></p>',
         '<p class="section-desc">Aprofunde o tema: <a href="/blog/como-aparecer-google-clinica-estetica-goiania/">'
         '%s →</a> · <a href="/blog/clinica-de-estetica-nao-aparece-no-google/">Checklist: clínica de estética não '
         'aparece no Google? →</a></p>' % ART_GYN_TITULO),
        # FAQ (ficha e texto visivel): o site agora tambem vende anuncio — resposta equilibrada
        ('"text": "Anúncio no Instagram e no Google traz contato rápido, mas para no dia em que você para de pagar. '
         'O trabalho no Google constrói uma presença que continua trazendo agendamento sem custo por clique. Muitas '
         'clínicas usam os dois, mas, no médio prazo, o SEO reduz a dependência de mídia paga e do algoritmo das '
         'redes sociais."',
         '"text": "O anúncio no Google traz contato rápido, porque aparece para quem já está pesquisando o '
         'procedimento — mas para quando a verba acaba. O SEO demora mais para firmar e continua trazendo paciente '
         'sem custo por clique. Muitas clínicas usam os dois: anúncio para encher a agenda agora e SEO para depender '
         'menos de mídia paga e do algoritmo das redes sociais. Eu faço os dois."'),
        ('<p>Anúncio no Instagram e no Google traz contato rápido, mas para no dia em que você para de pagar. O '
         'trabalho no Google constrói uma presença que continua trazendo agendamento sem custo por clique. Muitas '
         'clínicas usam os dois, mas, no médio prazo, o SEO reduz a dependência de mídia paga e do algoritmo das '
         'redes sociais.</p>',
         '<p>O anúncio no Google traz contato rápido, porque aparece para quem já está pesquisando o procedimento — '
         'mas para quando a verba acaba. O SEO demora mais para firmar e continua trazendo paciente sem custo por '
         'clique. Muitas clínicas usam os dois: anúncio para encher a agenda agora e SEO para depender menos de '
         'mídia paga e do algoritmo das redes sociais. Eu faço os dois — veja a <a href="/gestao-de-trafego-pago/">'
         'gestão de tráfego pago</a>.</p>'),
    ],

    # ------------------------------------------------------- artigo de Goiânia (retitulado)
    ART_GYN: [
        ('<title>Como Aparecer no Google: Clínica de Estética em Goiânia | RCB SEO</title>',
         '<title>Como Atrair Clientes para Clínica de Estética em Goiânia</title>'),
        ('<meta name="description" content="Como aparecer no Google sendo clínica de estética em Goiânia: presença no '
         'Maps, Perfil da Empresa forte e contatos mais qualificados.">',
         '<meta name="description" content="%s">' % ART_GYN_DESC),
        ('<meta property="og:title" content="Como aparecer no Google: clínica de estética em Goiânia | SEO Local">',
         '<meta property="og:title" content="%s">' % ART_GYN_TITULO),
        ('<meta property="og:description" content="O que ajuda uma clínica de estética a melhorar presença no Google '
         'Maps, transmitir confiança e orientar contatos mais qualificados.">',
         '<meta property="og:description" content="%s">' % ART_GYN_DESC),
        ('<meta name="twitter:title" content="Como aparecer no Google: clínica de estética em Goiânia | SEO Local">',
         '<meta name="twitter:title" content="%s">' % ART_GYN_TITULO),
        ('<meta name="twitter:description" content="O que ajuda uma clínica de estética a melhorar presença no Google '
         'Maps, transmitir confiança e orientar contatos mais qualificados.">',
         '<meta name="twitter:description" content="%s">' % ART_GYN_DESC),
        ('"headline": "Como aparecer no Google quando alguém procura clínica de estética em Goiânia",',
         '"headline": "%s",' % ART_GYN_H1),
        ('"description": "Como aparecer no Google sendo clínica de estética em Goiânia: presença no Maps, Perfil da '
         'Empresa forte e contatos mais qualificados.",',
         '"description": "%s",' % ART_GYN_DESC),
        ('"keywords": [\n          "SEO local para clínica de estética",',
         '"keywords": [\n          "como atrair clientes para clínica de estética",\n'
         '          "SEO local para clínica de estética",'),
        ('"dateModified": "2026-05-03T09:00:00-03:00",', '"dateModified": "%sT09:00:00-03:00",' % HOJE),
        ('"name": "Como aparecer no Google: clínica de estética em Goiânia",', '"name": "%s",' % ART_GYN_TITULO),
        ('<h1 id="artigo-h1">Como aparecer no Google quando alguém procura clínica de estética em Goiânia</h1>',
         '<h1 id="artigo-h1">%s</h1>' % ART_GYN_H1),
        ('<time datetime="2026-05-02" class="byline-date">2 de maio de 2026</time>',
         '<time datetime="2026-05-02" class="byline-date">2 de maio de 2026</time>\n'
         '          <span class="byline-separator" aria-hidden="true">·</span>\n'
         '          <span class="byline-date">Atualizado em <time datetime="2026-10-05">5 de outubro de 2026</time></span>'),
        # caixa que expunha nota interna de SEO ("artigo satélite", "cluster") -> leitura para a dona
        ('''<div class="artigo-cluster" aria-label="Cluster de conteúdo sobre SEO para clínicas">
          <strong>Cluster de SEO para clínicas</strong>
          <p>Este guia aprofunda um ponto específico da minha página de <a href="/seo-para-clinicas-de-estetica/" class="artigo-link">SEO local para clínicas de estética</a>: como sua clínica é encontrada quando a paciente pesquisa no Google, compara opções e escolhe quem parece mais confiável.</p>
          <ul>
            <li>Página principal: SEO local para clínicas de estética, saúde e procedimentos.</li>
            <li>Artigo satélite: presença de clínicas de estética no Google Maps e nas buscas locais de Goiânia.</li>
            <li>Próximos temas do cluster: regulamentação de marketing em saúde, avaliações no Google, fotos do perfil e conteúdo que responde dúvidas reais.</li>
          </ul>
        </div>''',
         '''<div class="artigo-cluster" aria-label="Leia junto">
          <strong>Leia junto</strong>
          <ul>
            <li><a href="/seo-para-clinicas-de-estetica/" class="artigo-link">SEO para clínicas de estética</a>: como eu trabalho com a clínica, procedimento por procedimento.</li>
            <li><a href="/blog/clinica-de-estetica-nao-aparece-no-google/" class="artigo-link">Clínica de estética não aparece no Google?</a> O checklist para fazer por conta própria.</li>
            <li><a href="/criacao-de-site-para-clinica-de-estetica/" class="artigo-link">Site para clínica de estética</a>, com uma página para cada procedimento.</li>
          </ul>
        </div>'''),
        ('<h2>Como aparecer no Google: a cliente que você nunca soube que existiu</h2>',
         '<h2>Quanta cliente nova a sua clínica perde sem saber?</h2>'),
        ('<p>O artigo foi pensado para fortalecer buscas como <strong>',
         '<p>As buscas que mais trazem cliente nova costumam ser parecidas com estas — e é nelas que a sua clínica '
         'precisa aparecer: <strong>'),
        ('Os outros conselhos profissionais, CFBM pra biomédicos, COREN pra enfermagem, CFO pra dentistas',
         'Os outros conselhos profissionais, CFBM pra biomédicos, Cofen pra enfermagem, CFO pra dentistas'),
        ('O Conselho Federal de Medicina tem a Resolução CFM 2.336/2023.',
         'O Conselho Federal de Medicina tem a %s, sobre publicidade médica.' % CFM_2336),
        ('<p>Vou tratar disso em profundidade no próximo artigo.</p>',
         '<p>Os cuidados de cada conselho estão resumidos na página de <a href="/seo-para-clinicas-de-estetica/" '
         'class="artigo-link">SEO para clínicas de estética</a>.</p>'),
        ('Salva esse blog nos favoritos e fica de olho. O próximo artigo vai entrar em detalhe sobre a regulamentação '
         'dos conselhos profissionais e como fazer marketing certo sem cair em armadilha jurídica que pode comprometer '
         'seu registro.',
         'Enquanto isso, faz o <a href="/blog/clinica-de-estetica-nao-aparece-no-google/" class="artigo-link">'
         'checklist de SEO local para clínica de estética</a> por conta própria: ele mostra o que dá para arrumar '
         'sozinha ainda essa semana.'),
    ],

    # ------------------------------------------------------- artigo-checklist de estética
    "blog/clinica-de-estetica-nao-aparece-no-google/index.html": [
        ('"dateModified": "2026-06-14T11:00:00-03:00",', '"dateModified": "%sT11:00:00-03:00",' % HOJE),
        ('<time datetime="2026-06-14" class="byline-date">14 de junho de 2026</time>',
         '<time datetime="2026-06-14" class="byline-date">14 de junho de 2026</time>\n'
         '          <span class="byline-separator" aria-hidden="true">·</span>\n'
         '          <span class="byline-date">Atualizado em <time datetime="2026-10-05">5 de outubro de 2026</time></span>'),
        ('''          <ul>
            <li>Página principal: SEO local para clínicas de saúde, estética e procedimentos.</li>
            <li>Este artigo: por que a clínica de estética não aparece e o checklist para mudar isso.</li>
            <li>Artigo irmão: o passo a passo de otimização do Google Meu Negócio da clínica.</li>
          </ul>''',
         '''          <ul>
            <li><a href="/blog/google-meu-negocio-para-clinicas-passo-a-passo/" class="artigo-link">Google Meu Negócio para clínicas, passo a passo</a>.</li>
            <li><a href="/blog/como-aparecer-google-clinica-estetica-goiania/" class="artigo-link">Como atrair clientes para clínica de estética em Goiânia</a>.</li>
            <li><a href="/criacao-de-site-para-clinica-de-estetica/" class="artigo-link">Site para clínica de estética</a>, com uma página para cada procedimento.</li>
          </ul>'''),
    ],

    # ------------------------------------------------------- SEO para pequenas empresas
    "seo-para-pequenas-empresas/index.html": [
        ('"dateModified": "2026-08-15"', '"dateModified": "%s"' % HOJE),
        ('''        {
          "@type": "City",
          "name": "Goiânia"
        }
      ]
    },
    {
      "@type": "FAQPage",''', '''        {
          "@type": "City",
          "name": "Goiânia"
        }
      ],
      "audience": {
        "@type": "BusinessAudience",
        "audienceType": "Pequenas empresas e negócios locais"
      }
    },
    {
      "@type": "FAQPage",'''),
        ('''        <p>É essa organização que eu faço: perfil no Google Maps, site e conteúdo, medindo cada contato que chega.</p>''',
         '''          <p>É essa organização que eu faço: perfil no Google Maps, site e conteúdo, medindo cada contato que chega.</p>
          %s''' % BYLINE),
        ('<a class="btn btn-outline" href="https://wa.me/5562991161040?text=Ol%C3%A1%2C%20Renan.%20Tenho%20uma%20'
         'pequena%20empresa%20e%20quero%20aparecer%20no%20Google." target="_blank" rel="noopener noreferrer" '
         'data-event="cta_click" data-location="hero_whatsapp" data-page="seo-pequenas-empresas">Chamar no WhatsApp</a>',
         '<a class="btn btn-outline" href="#pacotes" data-event="cta_click" data-location="hero_pacotes" '
         'data-page="seo-pequenas-empresas">Ver os pacotes</a>'),
        ('<div class="problem-card"><h3>Anúncio que para quando você para</h3><p>Tráfego pago funciona como aluguel: '
         'parou de pagar, sumiu da vitrine. Sem uma base orgânica, a empresa fica refém do boleto do anúncio para '
         'sempre.</p></div>',
         '<div class="problem-card"><h3>Anúncio que não vira cliente</h3><p>O anúncio traz gente rápido, mas se o '
         'clique cai num site confuso ou num perfil sem avaliação, a verba vai embora sem virar conversa. E sem uma '
         'base no Google, tudo some no dia em que a verba acaba.</p></div>'),
        ('mostra os negócios da região com o perfil mais completo, as melhores avaliações e o site que melhor '
         'responde a pesquisa. Essa é a brecha da empresa pequena.',
         'mostra os negócios da região com o perfil mais completo, as melhores avaliações e o site que melhor '
         'responde a pesquisa. O próprio Google explica que o resultado local depende de %s, e que não dá para pagar '
         'por uma posição melhor no mapa. Essa é a brecha da empresa pequena.' % GOOGLE_LOCAL),
        ('<thead><tr><th>Margem que sobra por cliente</th><th>Investimento de R$ 2 mil (exemplo)</th>'
         '<th>Investimento de R$ 3 mil (exemplo)</th></tr></thead>',
         '<thead><tr><th>Margem que sobra por cliente</th><th>Clientes para cobrir cada R$ 1.000 investidos</th>'
         '</tr></thead>'),
        ('<tr><td>R$ 200</td><td>10 clientes para cobrir</td><td>15 clientes para cobrir</td></tr>',
         '<tr><td>R$ 200</td><td>5 clientes</td></tr>'),
        ('<tr><td>R$ 500</td><td>4 clientes para cobrir</td><td>6 clientes para cobrir</td></tr>',
         '<tr><td>R$ 500</td><td>2 clientes</td></tr>'),
        ('<tr><td>R$ 1.000</td><td>2 clientes para cobrir</td><td>3 clientes para cobrir</td></tr>',
         '<tr><td>R$ 1.000</td><td>1 cliente</td></tr>'),
        ('<tr><td>R$ 2.000</td><td>1 cliente para cobrir</td><td>2 clientes para cobrir</td></tr>',
         '<tr><td>R$ 2.000</td><td>1 cliente (e sobra metade)</td></tr>'),
        ('<p class="case-table-note">Exemplo de ponto de equilíbrio, não projeção de resultado. A conta usa margem',
         '<p class="case-table-note">Exemplo de ponto de equilíbrio, não projeção de resultado nem preço: o valor do '
         'seu projeto sai no orçamento. A conta usa margem'),
        ('Ainda em dúvida se compensa? Leia <a href="/blog/vale-a-pena-seo-para-pequena-empresa/">vale a pena SEO '
         'para pequena empresa?</a></p>',
         'Ainda em dúvida se compensa? Leia <a href="/blog/vale-a-pena-seo-para-pequena-empresa/">vale a pena SEO '
         'para pequena empresa?</a> Quer o passo a passo completo? Veja o <a href="/blog/seo-para-empresas-locais/">'
         'guia de SEO para empresas locais</a>.</p>'),
        # secao nova: os 4 servicos, para o dono escolher por onde comecar
        ('''    <!-- RCB:PACOTES:INICIO -->''', '''    <section class="cluster-section" aria-labelledby="comecar-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Por onde começar</div>
          <h2 id="comecar-titulo" class="section-title">SEO, anúncio no Google ou landing page: por onde a pequena empresa começa?</h2>
          <p class="section-desc">Depende de quanto tempo você pode esperar pelo primeiro cliente. Eles trabalham juntos, mas dá para começar por um só — e eu te digo qual no orçamento.</p>
        </div>
        <div class="cluster-grid cluster-grid-4">
          <a class="cluster-card" href="/gestao-de-trafego-pago/"><h3>Precisa de cliente este mês</h3><p>Anúncio no Google para quem já está pesquisando o seu serviço. A verba é paga direto ao Google, no seu cartão.</p></a>
          <a class="cluster-card" href="/criacao-de-landing-page/"><h3>Vai anunciar</h3><p>Landing page: a página que recebe o clique do anúncio e transforma a visita em conversa no WhatsApp.</p></a>
          <a class="cluster-card" href="/google-perfil-empresa/"><h3>Quer cliente que continua vindo</h3><p>SEO e Google Meu Negócio: demora mais para firmar, mas não some quando a verba acaba.</p></a>
          <a class="cluster-card" href="/criacao-de-sites-goiania/"><h3>Ainda não tem site</h3><p>Site com uma página para cada serviço, pronto para aparecer no Google e receber anúncio.</p></a>
        </div>
        <p class="section-desc">Para pensar a conta antes de decidir, leia <a href="/blog/seo-ou-trafego-pago-empresa-local/">SEO ou tráfego pago para empresa local</a> e <a href="/blog/quanto-investir-em-trafego-pago/">quanto investir em tráfego pago</a>.</p>
      </div>
    </section>

    <!-- RCB:PACOTES:INICIO -->'''),
        ('"text": "Anúncio traz cliente enquanto você paga — parou, sumiu. Para verba pequena, isso vira um aluguel '
         'caro. O SEO é construção: demora mais para engrenar (2 a 6 meses), mas o resultado fica e se acumula. Para '
         'a maioria das pequenas empresas, o melhor caminho é arrumar a base orgânica primeiro; o anúncio, se vier, '
         'rende mais em cima de uma base arrumada."',
         '"text": "Os dois têm papéis diferentes. O anúncio no Google traz contato rápido, porque aparece para quem '
         'já está pesquisando — mas para quando a verba acaba. O SEO demora mais para engrenar (2 a 6 meses), e o '
         'resultado fica e se acumula. Com verba curta, o caminho mais seguro costuma ser arrumar o perfil no Google '
         'e a página que recebe o cliente primeiro; o anúncio rende mais em cima dessa base."'),
        ('<p>Anúncio traz cliente enquanto você paga — parou, sumiu. Para verba pequena, isso vira um aluguel caro. O ',
         '<p>Os dois têm papéis diferentes. O <a href="/gestao-de-trafego-pago/">anúncio no Google</a> traz contato '
         'rápido, porque aparece para quem já está pesquisando — mas para quando a verba acaba. O '),
        ('é construção: demora mais para engrenar (2 a 6 meses), mas o resultado fica e se acumula. Para a maioria das '
         'pequenas empresas, o melhor caminho é arrumar a base orgânica primeiro; o anúncio, se vier, rende mais em '
         'cima de uma base arrumada.</p>',
         'demora mais para engrenar (2 a 6 meses), e o resultado fica e se acumula. Com verba curta, o caminho mais '
         'seguro costuma ser arrumar o perfil no Google e a página que recebe o cliente primeiro; o anúncio rende '
         'mais em cima dessa base.</p>'),
    ],

    # ------------------------------------------------------- comércios locais
    "para-comercios-locais/index.html": [
        ('"dateModified": "2026-09-08",', '"dateModified": "%s",' % HOJE),
        ('<a href="#pacotes" class="btn btn-outline">Ver preços e pacotes</a>',
         '<a href="#pacotes" class="btn btn-outline">Ver os pacotes</a>'),
        ('categorias e avaliações respondidas. Isso melhora a base de visibilidade e confiança.',
         'categorias e avaliações respondidas. Isso melhora a base de visibilidade e confiança. Para ver como isso '
         'se encaixa com anúncio e site, veja <a href="/seo-para-pequenas-empresas/">SEO para pequenas empresas</a>.'),
    ],

    # ------------------------------------------------------- quem cita o título antigo do artigo
    "blog/index.html": [
        ('"headline": "Como aparecer no Google quando alguém procura clínica de estética em Goiânia",\n'
         '        "url": "https://rcbseo.com.br/blog/como-aparecer-google-clinica-estetica-goiania/",\n'
         '        "datePublished": "2026-05-02",\n        "dateModified": "2026-05-03"',
         '"headline": "%s",\n'
         '        "url": "https://rcbseo.com.br/blog/como-aparecer-google-clinica-estetica-goiania/",\n'
         '        "datePublished": "2026-05-02",\n        "dateModified": "%s"' % (ART_GYN_H1, HOJE)),
        ('aria-label="Ler artigo: Como aparecer no Google quando alguém procura clínica de estética em Goiânia"',
         'aria-label="Ler artigo: %s"' % ART_GYN_TITULO),
        ('<span class="blog-card-thumb-title">Como aparecer no Google quando alguém procura clínica de estética em '
         'Goiânia</span>', '<span class="blog-card-thumb-title">%s</span>' % ART_GYN_TITULO),
        ('<h2 class="blog-card-title">Como aparecer no Google quando alguém procura clínica de estética em Goiânia</h2>\n'
         '                          <p class="blog-card-desc">Entenda como uma clínica de estética pode disputar as '
         'primeiras posições no Google Maps, melhorar o ranqueamento local e virar escolha antes da concorrência.</p>',
         '<h2 class="blog-card-title">%s</h2>\n'
         '                          <p class="blog-card-desc">Para a dona de clínica de estética: o que faz a clínica '
         'ser achada no Google e no Maps, e escolhida antes da concorrência.</p>' % ART_GYN_TITULO),
    ],
    "blog/como-divulgar-minha-empresa-em-goiania/index.html": [
        ('<a href="/blog/como-aparecer-google-clinica-estetica-goiania/">Como aparecer no Google quando alguém procura '
         'clínica de estética em Goiânia</a>',
         '<a href="/blog/como-aparecer-google-clinica-estetica-goiania/">%s</a>' % ART_GYN_TITULO),
    ],
    "blog/seo-para-prestadores-de-servico/index.html": [
        ('<a href="/blog/como-aparecer-google-clinica-estetica-goiania/">Como aparecer no Google quando alguém procura '
         'clínica de estética em Goiânia</a>',
         '<a href="/blog/como-aparecer-google-clinica-estetica-goiania/">%s</a>' % ART_GYN_TITULO),
    ],
    "llms.txt": [
        ('- Como aparecer no Google quando alguém procura clínica de estética em Goiânia: '
         'https://rcbseo.com.br/blog/como-aparecer-google-clinica-estetica-goiania/',
         '- %s: https://rcbseo.com.br/blog/como-aparecer-google-clinica-estetica-goiania/' % ART_GYN_TITULO),
        ('- SEO para clínicas de estética: https://rcbseo.com.br/seo-para-clinicas-de-estetica/ — Visibilidade no '
         'Google para clínicas e profissionais de estética.',
         '- SEO para clínicas de estética: https://rcbseo.com.br/seo-para-clinicas-de-estetica/ — Visibilidade no '
         'Google para clínicas e profissionais de estética.\n'
         '  - Site para clínica de estética: https://rcbseo.com.br/criacao-de-site-para-clinica-de-estetica/\n'
         '  - Checklist (clínica de estética não aparece no Google): '
         'https://rcbseo.com.br/blog/clinica-de-estetica-nao-aparece-no-google/\n'
         '  - %s: https://rcbseo.com.br/blog/como-aparecer-google-clinica-estetica-goiania/' % ART_GYN_TITULO),
        ('- SEO para pequenas empresas: https://rcbseo.com.br/seo-para-pequenas-empresas/ — Como pequenas empresas '
         'aparecem no Google sem depender de anúncios.',
         '- SEO para pequenas empresas: https://rcbseo.com.br/seo-para-pequenas-empresas/ — Como pequenas empresas '
         'aparecem no Google e no Maps, e quando vale juntar anúncio e landing page.\n'
         '  - Vale a pena SEO para pequena empresa?: https://rcbseo.com.br/blog/vale-a-pena-seo-para-pequena-empresa/\n'
         '  - Guia de SEO para empresas locais: https://rcbseo.com.br/blog/seo-para-empresas-locais/'),
    ],
}

SITEMAP_URLS = [
    "seo-para-clinicas-de-estetica/", "blog/como-aparecer-google-clinica-estetica-goiania/",
    "blog/clinica-de-estetica-nao-aparece-no-google/", "seo-para-pequenas-empresas/", "para-comercios-locais/",
    "criacao-de-site-para-clinica-de-estetica/", "blog/",
]


def ler(rel):
    with io.open(os.path.join(RAIZ, rel), encoding="utf-8", newline="") as f:
        return f.read()


def gravar(rel, txt):
    with io.open(os.path.join(RAIZ, rel), "w", encoding="utf-8", newline="") as f:
        f.write(txt)


def main():
    erros, alterados = [], 0
    for rel, trocas in TROCAS.items():
        txt = ler(rel)
        orig = txt
        for velho, novo in trocas:
            # ja aplicada? (vale tambem para trocas que so acrescentam: o texto novo contem o velho)
            if novo in txt or novo.replace("\n", "\r\n") in txt:
                continue
            par = None
            for v, n in ((velho, novo), (velho.replace("\n", "\r\n"), novo.replace("\n", "\r\n"))):
                if txt.count(v) == 1:
                    par = (v, n)
                    break
            if par is None:
                erros.append("%s: texto antigo nao encontrado 1 vez: %r" % (rel, velho[:90]))
                continue
            txt = txt.replace(par[0], par[1])
        if txt != orig:
            gravar(rel, txt)
            alterados += 1
            print("alterado:", rel)

    sm = ler("sitemap.xml")
    novo = sm
    for u in SITEMAP_URLS:
        i = novo.find("<loc>https://rcbseo.com.br/%s</loc>" % u)
        if i < 0:
            erros.append("sitemap sem %s" % u)
            continue
        a, fim = novo.find("<lastmod>", i), novo.find("</url>", i)
        if a < 0 or a > fim:
            continue
        b = novo.find("</lastmod>", a)
        novo = novo[:a] + "<lastmod>" + HOJE + novo[b:]
    if novo != sm:
        gravar("sitemap.xml", novo)
        alterados += 1
        print("alterado: sitemap.xml")

    print("alterados:", alterados)
    for e in erros:
        print("ERRO:", e)
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
