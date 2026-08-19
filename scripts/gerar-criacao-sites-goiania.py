# -*- coding: utf-8 -*-
"""Gera /criacao-de-sites-goiania/ - pagina comercial de criacao de site em Goiania.

Por que esta pagina existe (evidencia, nao palpite):
  * Keyword Planner: "criacao de site goiania" e "criacao de sites goiania" ~500/mes
    cada, lance alto observado R$ 17,61 - a maior demanda local medida do projeto.
  * Search Console 90d (20/05 a 17/08/2026): ZERO impressoes para qualquer variante
    de "criacao de site". Nao existia URL para isso.
  * SERP conferida em 18/08/2026 (google.com.br, gl=br, sem personalizacao):
    dominada por dominios de correspondencia exata e agencias pequenas - mesmo perfil
    competitivo de "consultor seo goiania", onde a RCB ja e 4a com quase nenhum backlink.
  * E o produto do cliente ideal no 1 do briefing: empresa local SEM site.

O molde (head/nav/rodape) vem de /consultor-seo-goiania/, que e a pagina vencedora do
dominio. O texto e proprio. A pagina vencedora NAO e alterada por este script.
Idempotente: sobrescreve o arquivo de destino.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rcb_pacotes as P

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOADOR = os.path.join(RAIZ, "consultor-seo-goiania", "index.html")
DESTINO = os.path.join(RAIZ, "criacao-de-sites-goiania", "index.html")
SLUG = "criacao-de-sites-goiania"
URL = "https://rcbseo.com.br/%s/" % SLUG

TITLE = u"Criação de Sites em Goiânia | Pronto para Aparecer no Google"
DESC = (u"Criação de sites em Goiânia para empresas e profissionais locais: site que aparece "
        u"no Google, com páginas de serviço, WhatsApp e Perfil da Empresa configurado.")
OG_TITLE = u"Criação de Sites em Goiânia | Pronto para Aparecer no Google"
OG_DESC = (u"Site feito para ser encontrado no Google, não só para ficar bonito. "
           u"Empresas e profissionais de Goiânia. A partir de R$ 1.997.")

FAQ = [
    (u"Quanto custa a criação de um site em Goiânia?",
     u"Na RCB o site entra no pacote Presença, de R$ 2.497 em pagamento único, com até cinco "
     u"páginas, Google Perfil da Empresa configurado, fotos e avaliações organizadas. Quem já "
     u"tem site e só precisa do Google resolvido paga R$ 1.997 no Presença Lite. O preço está "
     u"na tela porque orçamento fechado poupa o tempo dos dois lados."),
    (u"Em quanto tempo o site fica pronto?",
     u"Sete dias úteis a partir do momento em que você me manda os textos, as fotos e os dados "
     u"da empresa. O que costuma atrasar não é a montagem: é o material do cliente."),
    (u"Depois que o site entra no ar, ele já aparece no Google?",
     u"Entrar no Google é rápido — em geral poucos dias. Aparecer bem colocado é outra coisa e "
     u"leva meses, porque depende de concorrência, avaliações e histórico. Ninguém honesto "
     u"promete primeira página com data marcada, e eu não prometo."),
    (u"Você faz o site em WordPress, Wix ou como?",
     u"Faço o site em código próprio, leve e rápido, sem depender de dezenas de plugins. O "
     u"resultado é uma página que carrega rápido no celular e que eu consigo ajustar quando "
     u"for preciso, sem quebrar nada."),
    (u"Já tenho um site, mas ninguém me encontra. Preciso fazer outro?",
     u"Nem sempre. Às vezes o site é razoável e o problema está no Google Perfil da Empresa ou "
     u"na falta de páginas para os serviços que você vende. Eu olho antes de vender: se der "
     u"para arrumar o que existe, eu digo isso."),
    (u"Você atende só Goiânia?",
     u"O atendimento presencial é em Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade e "
     u"Anápolis. Site e Google eu faço para o Brasil inteiro, à distância, e boa parte dos "
     u"clientes nunca precisou de reunião presencial."),
]


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def schema():
    faq = [{"@type": "Question", "name": p,
            "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in FAQ]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": URL + "#webpage", "url": URL, "name": TITLE,
             "description": DESC, "inLanguage": "pt-BR",
             "isPartOf": {"@type": "WebSite", "@id": "https://rcbseo.com.br/#website",
                          "name": "RCB Consultoria", "url": "https://rcbseo.com.br/"},
             "breadcrumb": {"@id": URL + "#breadcrumb"}},
            {"@type": "BreadcrumbList", "@id": URL + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": u"Início",
                 "item": "https://rcbseo.com.br/"},
                {"@type": "ListItem", "position": 2, "name": u"Criação de sites em Goiânia",
                 "item": URL}]},
            {"@type": "Person", "@id": "https://rcbseo.com.br/#renan",
             "name": "Renan Carvalho Barbosa", "jobTitle": "Consultor de SEO local",
             "url": "https://rcbseo.com.br/consultor-seo-goiania/",
             "worksFor": {"@id": "https://rcbseo.com.br/#localbusiness"}},
            {"@type": "LocalBusiness", "@id": "https://rcbseo.com.br/#localbusiness",
             "name": "RCB Consultoria", "url": "https://rcbseo.com.br/",
             "telephone": "+5562991161040", "priceRange": "R$ 1.997 - R$ 4.997",
             "address": {"@type": "PostalAddress", "streetAddress": "Rua 18-A, 256",
                         "addressLocality": u"Goiânia", "addressRegion": "GO",
                         "postalCode": "74070-060", "addressCountry": "BR"},
             "areaServed": [{"@type": "City", "name": u"Goiânia"},
                            {"@type": "City", "name": u"Aparecida de Goiânia"},
                            {"@type": "City", "name": "Senador Canedo"},
                            {"@type": "City", "name": "Trindade"},
                            {"@type": "City", "name": u"Anápolis"}]},
            {"@type": "Service", "@id": URL + "#service",
             "name": u"Criação de sites em Goiânia",
             "serviceType": u"Criação de site profissional otimizado para busca",
             "description": (u"Criação de site para empresas e profissionais de Goiânia, com "
                             u"páginas de serviço, botão de WhatsApp, versão para celular e "
                             u"Google Perfil da Empresa configurado junto."),
             "provider": {"@id": "https://rcbseo.com.br/#localbusiness"},
             "areaServed": {"@type": "City", "name": u"Goiânia", "addressRegion": "GO",
                            "addressCountry": "BR"},
             "offers": P.ofertas()},
            {"@type": "FAQPage", "@id": URL + "#faq", "mainEntity": faq},
        ],
    }


HERO = u"""  <main id="main-content">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><span>Criação de sites em Goiânia</span></nav>
          <div class="eyebrow">Goiânia e região metropolitana</div>
          <h1 class="page-title">Criação de sites em Goiânia</h1>
          <p class="page-subtitle">Seu cliente procura no Google o que você vende. Se a sua empresa não tem site — ou tem um que ninguém encontra — quem aparece é o concorrente. Eu crio o site da sua empresa em Goiânia já pensado para ser achado no Google e para levar a pessoa até o seu WhatsApp.</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="%(wa)s" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero" data-page="%(slug)s">Quero um site que traga clientes</a>
            <a class="btn btn-outline" href="#pacotes" data-event="cta_click" data-location="hero_precos" data-page="%(slug)s">Ver preços</a>
          </div>
          <div class="pill-row"><span class="pill">Pronto em 7 dias úteis</span><span class="pill">Preço fechado na tela</span><span class="pill">Garantia de 30 dias</span></div>
        </div>
        <aside class="page-hero-panel">
          <h2>O que vem junto com o site</h2>
          <ul class="audit-list">
            <li>Site próprio, no seu domínio, rápido no celular.</li>
            <li>Uma página para cada serviço que você vende.</li>
            <li>Botão de WhatsApp em todas as páginas.</li>
            <li>Google Perfil da Empresa configurado e ligado ao site.</li>
            <li>Textos escritos para o cliente entender e para o Google achar.</li>
            <li>Registro de quantas pessoas chamaram você.</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class="solution-section">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">O problema</div>
          <h2 class="section-title">Site bonito não é a mesma coisa que site encontrado</h2>
          <p>A cena se repete em Goiânia toda semana: o empresário paga por um site, acha bonito, coloca no ar — e não acontece nada. Nenhuma mensagem nova, nenhuma ligação nova. Quando ele procura a própria empresa no Google, não encontra.</p>
          <p>O motivo quase nunca é o desenho. É que o site foi feito como um folheto: uma página só, sem dizer com clareza o que a empresa faz, para quem faz e em que cidade. O Google não tem o que mostrar, e o cliente não tem onde clicar.</p>
          <p>Um site que traz cliente é montado ao contrário: primeiro se decide quais buscas ele precisa responder, depois se escreve, depois se desenha. Essa ordem é a diferença entre um site que fica parado e um que trabalha.</p>
        </div>
        <div class="split-visual">
          <div class="visual-card">
            <div class="visual-card-title">Três situações que eu atendo</div>
            <ul class="visual-list">
              <li><strong>Não tenho site.</strong> Só Instagram, ou nada. Começamos do zero e da forma certa.</li>
              <li><strong>Tenho site, mas ninguém acha.</strong> Reconstruo o que precisa e aproveito o que presta.</li>
              <li><strong>Só apareço quando pago anúncio.</strong> Quando o anúncio para, some tudo. Montamos a parte que continua funcionando sem pagar por clique.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">O que está incluído</div>
          <h2 class="section-title">O que entra na criação do site da sua empresa em Goiânia</h2>
          <p class="section-desc">Não é um modelo pronto com o seu logotipo em cima. É a estrutura que faz a sua empresa ser encontrada.</p>
        </div>
        <div class="cards-grid">
          <article class="feature-card">
            <h3>Uma página para cada serviço</h3>
            <p>Quem procura "conserto de ar-condicionado em Goiânia" não quer cair numa página que fala de dez serviços ao mesmo tempo. Cada serviço que você vende ganha a sua própria página, com o nome que o cliente usa.</p>
          </article>
          <article class="feature-card">
            <h3>O nome da cidade onde precisa estar</h3>
            <p>Busca local é decidida por cidade e por bairro. O site diz onde você atende, em texto e nos dados que o Google lê, sem enfeite e sem exagero.</p>
          </article>
          <article class="feature-card">
            <h3>Caminho curto até o WhatsApp</h3>
            <p>Botão visível em toda página, com a mensagem já escrita. Site que obriga a pessoa a procurar o telefone perde a conversa.</p>
          </article>
          <article class="feature-card">
            <h3>Rápido no celular</h3>
            <p>A maior parte das buscas locais é feita no celular, muitas vezes com internet ruim. O site é leve de propósito.</p>
          </article>
          <article class="feature-card">
            <h3>Google Perfil da Empresa junto</h3>
            <p>O site sozinho não coloca você no mapa. O <a href="/google-perfil-empresa/">Perfil da Empresa</a> é configurado junto e apontando para o site — é o par que faz a empresa aparecer nas duas partes da busca.</p>
          </article>
          <article class="feature-card">
            <h3>Espaço para crescer</h3>
            <p>O site nasce pronto para receber mais páginas depois: novos serviços, novas cidades, textos que respondem dúvidas de cliente. Nada precisa ser refeito para isso.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="solution-section alt-bg">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Como funciona</div>
          <h2 class="section-title">Como é criar o site, do primeiro contato até ele no ar</h2>
        </div>
        <ol class="steps-list">
          <li>
            <h3>1. Eu olho antes de vender</h3>
            <p>Você me chama no WhatsApp e me diz o que a empresa faz. Eu procuro no Google como se fosse seu cliente e vejo quem está aparecendo na sua frente. Se eu achar que você não precisa de site novo, eu falo.</p>
          </li>
          <li>
            <h3>2. Decidimos as páginas</h3>
            <p>Listamos os serviços que dão dinheiro e a região onde você quer ser chamado. Isso vira o mapa do site — é aqui que a maioria dos sites erra.</p>
          </li>
          <li>
            <h3>3. Eu monto e escrevo</h3>
            <p>Sete dias úteis depois de receber suas fotos e informações. Você recebe o link para conferir antes de publicar.</p>
          </li>
          <li>
            <h3>4. Publicamos e ligamos ao Google</h3>
            <p>Site no ar, Perfil da Empresa apontando para ele, e o registro de contatos funcionando para você saber quantas pessoas chamaram.</p>
          </li>
        </ol>
      </div>
    </section>

    <section class="solution-section">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Quanto custa</div>
          <h2 class="section-title">Quanto custa criar um site em Goiânia?</h2>
          <p>Em Goiânia é comum ouvir "faço seu site por R$ 500" e também "seu projeto fica R$ 12 mil" — e o cliente não descobre o motivo da diferença. Aqui o preço está na tela logo abaixo, com o que entra em cada faixa.</p>
          <p>O site mais barato do mercado costuma ser uma página só, sem página de serviço, sem cidade, sem Perfil da Empresa. Ele existe, funciona como cartão de visita, e não vai trazer cliente pelo Google — porque não foi feito para isso.</p>
          <p>Se você já tem site e ele até que é razoável, não compre a ideia de refazer tudo: veja antes o <a href="/site-otimizado-para-seo/">que muda quando o site é feito para ranquear</a> e <a href="/blog/melhorar-site-atual-ou-fazer-um-novo/">quando vale melhorar o site atual em vez de fazer outro</a>.</p>
        </div>
        <div class="split-visual">
          <div class="visual-card">
            <div class="visual-card-title">O que empurra o preço para cima</div>
            <ul class="visual-list">
              <li>Quantidade de serviços que precisam de página própria.</li>
              <li>Se você já tem textos e fotos ou se precisa produzir.</li>
              <li>Se o Perfil da Empresa existe, está verificado, ou nem foi criado.</li>
              <li>Se você quer acompanhamento depois ou só o site entregue.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

"""

DEPOIS = u"""    <section class="solution-section alt-bg">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">A diferença</div>
          <h2 class="section-title">Por que eu não me apresento como fábrica de sites</h2>
          <p>Existe muita gente em Goiânia que entrega site rápido e barato. Não é isso que eu faço, e não adianta comparar por preço de página.</p>
          <p>Eu trabalho com <a href="/consultor-seo-goiania/">consultoria de SEO local</a> — ou seja, com o problema de fazer a empresa ser encontrada. O site é a peça central disso, mas é uma peça: sem página de serviço, sem cidade escrita, sem Perfil da Empresa e sem avaliações, um site novo não muda nada.</p>
          <p>Por isso o site sai junto com a parte do Google. É um consultor só, direto com você, sem camada de atendimento no meio. Veja <a href="/cases/">o que aconteceu com clientes reais</a> e decida por resultado, não por promessa.</p>
        </div>
        <div class="split-visual">
          <div class="visual-card">
            <div class="visual-card-title">O que eu não prometo</div>
            <ul class="visual-list">
              <li>Primeiro lugar no Google com data marcada.</li>
              <li>Resultado em uma semana.</li>
              <li>Site que vende sozinho sem você responder mensagem.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="faq-section" aria-labelledby="faq-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Dúvidas</div>
          <h2 id="faq-titulo" class="section-title">Perguntas frequentes sobre criação de sites em Goiânia</h2>
        </div>
        <div class="faq-list">%(faq)s
        </div>
      </div>
    </section>

    <section class="cluster-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Leia também</div>
          <h2 class="section-title">Antes de encomendar um site, vale ler</h2>
        </div>
        <div class="cluster-grid">
          <a class="cluster-card" href="/blog/site-ou-instagram-para-empresa-local/"><h3>Site ou Instagram para empresa local?</h3><p>Onde cada um funciona, e por que o Instagram sozinho deixa dinheiro na mesa.</p></a>
          <a class="cluster-card" href="/blog/site-barato-empresa-local-vale-a-pena/"><h3>Site barato vale a pena?</h3><p>O que costuma faltar no site de R$ 500 — e quando ele até serve.</p></a>
          <a class="cluster-card" href="/blog/paginas-que-empresa-local-precisa-no-site/"><h3>Quais páginas o site precisa ter</h3><p>A lista mínima para uma empresa local ser encontrada.</p></a>
          <a class="cluster-card" href="/blog/site-bonito-nao-aparece-no-google/"><h3>Site bonito que não aparece</h3><p>Por que design não resolve o problema de ser achado.</p></a>
          <a class="cluster-card" href="/seo-local-goiania/"><h3>SEO local em Goiânia</h3><p>Como a empresa aparece no Google e no Maps aqui na cidade.</p></a>
          <a class="cluster-card" href="/blog/como-divulgar-minha-empresa-em-goiania/"><h3>Como divulgar minha empresa em Goiânia</h3><p>Os caminhos que funcionam e os que só gastam dinheiro.</p></a>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="container cta-band-inner">
        <h2>Me conte o que a sua empresa faz. Eu olho o seu Google hoje.</h2>
        <p>Sem formulário longo e sem compromisso. Você me diz o serviço e a região, eu procuro como se fosse seu cliente e te mostro quem está aparecendo no seu lugar.</p>
        <a class="btn btn-whatsapp btn-lg" href="%(wa)s" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="cta_band" data-page="%(slug)s">Falar no WhatsApp</a>
      </div>
    </section>
  </main>
"""


def corpo():
    faq_html = u"".join(
        u'\n          <details class="faq-item">'
        u'\n            <summary><h3>%s</h3></summary>'
        u'\n            <p>%s</p>'
        u'\n          </details>' % (esc(p), esc(r)) for p, r in FAQ)
    wa_hero = P.wa(u"Olá, Renan! Vi a página de criação de sites em Goiânia e quero "
                   u"um site para a minha empresa.")
    pacotes = P.bloco_pacotes(
        u"uma empresa", SLUG, onde=u" em Goiânia",
        fecho=u"É o que a sua empresa em Goiânia paga para começar a aparecer.")
    return (HERO % {"wa": wa_hero, "slug": SLUG}
            + pacotes
            + DEPOIS % {"faq": faq_html, "wa": wa_hero, "slug": SLUG})


def main():
    doador = io.open(DOADOR, encoding="utf-8", newline="").read()
    head = doador[:doador.index("</head>")]
    nav = doador[doador.index("<body"):doador.index("<main id=")]
    rodape = doador[doador.index("</main>") + len("</main>"):]

    def troca(padrao, valor, texto):
        return re.sub(padrao, lambda m: m.group(1) + valor + m.group(2), texto,
                      flags=re.I | re.S)

    head = re.sub(r"(?is)<title>.*?</title>", lambda m: u"<title>%s</title>" % TITLE, head)
    head = troca(r'(<meta name="description" content=")[^"]*(")', DESC, head)
    head = troca(r'(<link rel="canonical" href=")[^"]*(")', URL, head)
    head = troca(r'(<link rel="alternate" hreflang="pt-BR" href=")[^"]*(")', URL, head)
    head = troca(r'(<meta property="og:url" content=")[^"]*(")', URL, head)
    head = troca(r'(<meta property="og:title" content=")[^"]*(")', OG_TITLE, head)
    head = troca(r'(<meta name="twitter:title" content=")[^"]*(")', OG_TITLE, head)
    head = troca(r'(<meta property="og:description" content=")[^"]*(")', OG_DESC, head)
    head = troca(r'(<meta name="twitter:description" content=")[^"]*(")', OG_DESC, head)
    novo_ld = (u'<script type="application/ld+json">\n%s\n  </script>'
               % json.dumps(schema(), ensure_ascii=False, indent=2))
    head = re.sub(r'(?is)<script type="application/ld\+json">.*?</script>',
                  lambda m: novo_ld, head, count=1)

    nav = nav.replace('data-page="consultor-seo-goiania"', 'data-page="%s"' % SLUG)
    rodape = rodape.replace('data-page="consultor-seo-goiania"', 'data-page="%s"' % SLUG)
    rodape = rodape.replace('data-page="consultor-seo"', 'data-page="%s"' % SLUG)
    rodape = re.sub(r"(?s)<!-- RCB:CTA-MOBILE -->.*?</div>\n",
                    lambda m: P.bloco_cta_mobile(SLUG).rstrip("\n") + "\n", rodape, count=1)

    html = head + u"</head>\n" + nav + corpo() + rodape
    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    with io.open(DESTINO, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    print("gerado: %s (%d bytes)" % (DESTINO, len(html)))


if __name__ == "__main__":
    main()
