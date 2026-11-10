# -*- coding: utf-8 -*-
"""
Conteudo das 2 paginas criadas a partir da pesquisa de palavras-chave de 10/11/2026
(planejador do Google Ads, local Goiania e Brasil, 12 meses, cruzado com o Search Console).

Por que existem:
  * /agencia-de-marketing-digital-goiania/
      "agencia de marketing", "agencia de marketing goiania" e "marketing digital (em) goiania"
      tem 100 a 1 mil buscas/mes cada em Goiania. "consultor de seo" e "consultoria seo" tem
      10 a 100. O site nao tinha pagina para a busca maior: zero impressao no Search Console.
      Decisao do Renan (10/11/2026): usar a palavra "agencia", que e a que o cliente digita.
  * /landing-page-para-advogados/
      "landing page para advogados": 1 mil a 10 mil buscas/mes no Brasil. Nao havia pagina.

Divisao de termos (nao canibalizar):
  * /agencia-de-marketing-digital-goiania/ -> agencia / empresa de marketing (digital) em Goiania
  * /consultor-seo-goiania/                -> consultor de SEO em Goiania (PROTEGIDA)
  * /seo-local-goiania/                    -> SEO local em Goiania
  * /criacao-de-sites-goiania/             -> criacao de sites em Goiania
  * /landing-page-para-advogados/          -> landing page para advogados (nacional)
  * /criacao-de-site-para-advogado/        -> site para advogado
  * /criacao-de-landing-page/              -> landing page em geral

Regras (nao afrouxar):
  * SEM PRECO da RCB. Nenhuma promessa de posicao, de prazo ou de numero de clientes.
  * Explica o QUE e o POR QUE, nunca o COMO. Caixa "ajuda" chama para o WhatsApp no meio.
  * A pagina da agencia diz a verdade sobre o tamanho: quem atende e quem faz e a mesma pessoa.
    E diz o que NAO e feito (redes sociais, publicidade tradicional).
  * Advogados: tudo dentro do Provimento 205/2021 da OAB (publicidade informativa, sem
    captacao, sem promessa de resultado).
  * Case so o verificado em /cases/ (Docevidade).

Gerador: scripts/gerar-paginas-2026-11-10.py
"""

DATA = "2026-11-10"

_A = '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
RANKING = "https://support.google.com/business/answer/7091?hl=pt-BR"
GUIA_SEO = "https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=pt-br"
COMO_BUSCA = "https://www.google.com/intl/pt-BR/search/howsearchworks/"
OAB_205 = "https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021"

AGENCIA = "agencia-de-marketing-digital-goiania"
LP_ADV = "landing-page-para-advogados"

PAGINAS = [
    # ------------------------------------------------------------------------------------
    {
        "slug": AGENCIA,
        "tipo": "servico",
        "nacional": False,
        "data": DATA,
        "publico": "Empresas, clínicas, escritórios, comércios e prestadores de serviço de Goiânia e região",
        "title": "Agência de Marketing Digital em Goiânia | RCB SEO",
        "desc": ("Agência de marketing digital em Goiânia: site, Google, mapa e anúncios para a sua empresa "
                 "ser encontrada. Fale direto com quem faz. Orçamento grátis."),
        "trilha": "Agência de Marketing Digital em Goiânia",
        "servico": "Marketing digital para empresas (Google, site, mapa e anúncios)",
        "alternativos": ["Agência de marketing em Goiânia", "Marketing digital em Goiânia",
                         "Empresa de marketing digital em Goiânia", "Agência digital em Goiânia"],
        "eyebrow": "Presencial em Goiânia · Aparecida · região metropolitana",
        "h1": "Agência de marketing digital em Goiânia para a sua empresa ser encontrada no Google",
        "sub": ("A RCB SEO é uma agência de marketing digital em Goiânia que cuida de quatro coisas: o seu "
                "site, a sua empresa no Google e no mapa, os seus anúncios e a sua presença nas respostas "
                "de inteligência artificial. Você fala direto com quem faz o trabalho, sem atendente no "
                "meio e sem contrato de fidelidade."),
        "cta_hero": "Quero um orçamento grátis",
        "botao2": ("#orcamento", "Ver por onde começar"),
        "msg": "Olá, Renan! Tenho uma empresa em Goiânia e procuro uma agência de marketing digital. Quero um orçamento.",
        "pills": ["Atendimento em Goiânia", "Orçamento em até 24h", "Sem fidelidade"],
        "painel_h2": "Marketing digital em Goiânia, em uma frase",
        "painel": [
            "Quem precisa de um serviço em Goiânia pesquisa no Google antes de ligar para alguém.",
            "Se a sua empresa não aparece nessa hora, o contato vai para o concorrente.",
            "O meu trabalho é fazer a sua empresa aparecer nessa pesquisa e transformar a visita em mensagem no WhatsApp.",
        ],
        "faq_titulo": "Perguntas frequentes sobre agência de marketing digital em Goiânia",
        "secoes": [
            ("texto", {
                "tag": "O que é",
                "titulo": "O que faz uma agência de marketing digital em Goiânia?",
                "ps": [
                    "Uma agência de marketing digital cuida de como a sua empresa é encontrada e escolhida "
                    "na internet. Na prática são quatro frentes: um site que explica o que você vende, o "
                    "perfil da empresa no Google e no mapa, os anúncios pagos e o conteúdo que responde às "
                    "dúvidas de quem está pesquisando.",
                    "Em Goiânia isso pesa porque a busca é local. Quem mora no Setor Bueno procura alguém "
                    "perto do Bueno, e quem está em Aparecida procura em Aparecida. O Google decide quem "
                    "mostrar olhando a distância, a relevância e a reputação de cada empresa, como ele "
                    "explica na " + _A % (RANKING, "página oficial sobre o resultado local") + ". Marketing "
                    "digital bem feito é deixar esses três pontos a favor da sua empresa.",
                ],
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que tanta empresa de Goiânia paga marketing e não vê cliente chegar?",
                "ps": [
                    "Eu escuto a mesma história toda semana: a empresa pagou por um site, por postagens ou "
                    "por anúncio, e o telefone continuou igual. Quase sempre o motivo é o mesmo. O trabalho "
                    "foi feito para ficar bonito, e não para ser encontrado por quem está procurando.",
                    "Site hoje qualquer um faz, tem até de graça. O que separa um site que só existe de um "
                    "site que traz cliente é o que vem antes dele: saber o que o seu cliente digita no "
                    "Google, quem aparece na frente e por quê. Isso é estratégia, e é a parte que eu faço "
                    "antes de mexer em qualquer coisa.",
                ],
                "card_titulo": "Sinais de marketing que não traz cliente",
                "card": [
                    "Site no ar que ninguém encontra no Google.",
                    "Perfil no mapa parado, com poucas avaliações.",
                    "Anúncio rodando sem saber quantos contatos trouxe.",
                    "Relatório cheio de curtidas e nenhum pedido de orçamento.",
                    "Você nunca fala com quem faz o trabalho.",
                ],
            }),
            ("cards", {
                "tag": "Serviços",
                "titulo": "O que a agência faz pela sua empresa em Goiânia",
                "desc": "Você pode contratar uma frente só ou todas juntas. Eu te digo com franqueza por qual começar.",
                "itens": [
                    ("Google e mapa (SEO local)",
                     "A sua empresa aparecendo quando alguém da cidade procura o que você vende. Veja o "
                     "<a href=\"/seo-local-goiania/\">SEO local em Goiânia</a> e o "
                     "<a href=\"/google-meu-negocio-goiania/\">Google Meu Negócio em Goiânia</a>."),
                    ("Criação de sites",
                     "Site feito para ser encontrado e para virar mensagem no WhatsApp, e não só cartão de "
                     "visita. Veja a <a href=\"/criacao-de-sites-goiania/\">criação de sites em Goiânia</a>."),
                    ("Landing page",
                     "Uma página única, direta, para quem clica no seu anúncio e precisa decidir rápido. "
                     "Veja a <a href=\"/criacao-de-landing-page/\">criação de landing page</a>."),
                    ("Tráfego pago (Google Ads)",
                     "Anúncio no Google para aparecer já, enquanto o resultado gratuito amadurece. Veja a "
                     "<a href=\"/gestao-de-trafego-pago/\">gestão de tráfego pago</a>."),
                    ("Aparecer nas respostas de IA",
                     "Cada vez mais gente pergunta ao ChatGPT e ao Gemini quem contratar. Veja o "
                     "<a href=\"/seo-para-ia/\">SEO para IA</a>."),
                    ("Loja virtual e YouTube",
                     "Para quem vende pela internet ou grava vídeo: "
                     "<a href=\"/criacao-de-loja-virtual-goiania/\">loja virtual em Goiânia</a> e "
                     "<a href=\"/seo-para-youtube/\">SEO para YouTube</a>."),
                ],
            }),
            ("ajuda", {
                "titulo": "Quer saber por que a sua empresa não aparece?",
                "texto": "Me manda o nome da sua empresa e o bairro pelo WhatsApp. Eu olho como ela aparece no "
                         "Google hoje, quem está na sua frente em Goiânia, e te digo sem compromisso o que falta.",
                "msg": "Olá, Renan! Quero que você olhe como a minha empresa aparece no Google. Ela fica em Goiânia.",
                "botao": "Quero que você olhe a minha empresa",
            }),
            ("tabela", {
                "tag": "Comparação",
                "titulo": "Agência grande ou agência enxuta: qual serve para a sua empresa?",
                "desc": "As duas existem em Goiânia e as duas têm o seu lugar. A diferença está em quem atende e em quem executa.",
                "colunas": ["O que você quer saber", "Agência grande", "RCB SEO"],
                "linhas": [
                    ["Com quem eu falo?", "Com um atendente de contas", "Com quem faz o trabalho"],
                    ["Quem executa?", "Uma equipe que você não conhece", "A mesma pessoa que te atendeu"],
                    ["Faz redes sociais?", "Normalmente sim", "Não. O foco é Google, site e anúncios"],
                    ["Tem fidelidade?", "É comum ter contrato de 6 a 12 meses", "Não tem"],
                    ["Para quem é melhor?", "Empresa com várias frentes e verba alta", "Empresa local que quer ser encontrada no Google"],
                ],
                "nota": "Comparação geral. Cada agência tem o seu jeito, vale perguntar antes de fechar.",
            }),
            ("texto", {
                "tag": "Com franqueza",
                "titulo": "O que esta agência não faz",
                "ps": [
                    "Eu não faço gestão de redes sociais, não crio campanha de TV, rádio ou outdoor e não "
                    "produzo vídeo. Se é isso que a sua empresa precisa agora, uma agência de publicidade "
                    "completa vai te atender melhor, e eu falo isso sem problema.",
                    "O que eu faço é uma coisa só, bem feita: colocar a sua empresa na frente de quem já está "
                    "procurando o que você vende no Google, no mapa e nas respostas de IA. Se quiser entender "
                    "melhor essa diferença, leia "
                    "<a href=\"/blog/consultor-seo-ou-agencia-de-marketing-digital/\">consultor de SEO ou agência "
                    "de marketing digital</a> e conheça o "
                    "<a href=\"/consultor-seo-goiania/\">consultor de SEO em Goiânia</a> por trás da RCB SEO.",
                ],
            }),
            ("texto", {
                "tag": "Resultado real",
                "titulo": "Um caso real de marketing digital em Goiânia",
                "ps": [
                    "A Docevidade, uma doceria de Goiânia, chegou ao <strong>1º lugar no Google Maps para "
                    "“macarrons Goiânia”</strong> com apenas 4 avaliações, na frente de concorrentes que tinham "
                    "47 e 312. Não foi verba de anúncio. Foi o perfil mais completo e mais certo para aquela busca.",
                    "Os detalhes, com imagens, estão na página de <a href=\"/cases/\">cases</a>. Cada negócio é "
                    "diferente e eu não prometo posição, mas esse é o tipo de trabalho que eu faço.",
                ],
            }),
            ("tabela", {
                "tag": "Quem eu atendo",
                "titulo": "Marketing digital em Goiânia para qual tipo de empresa?",
                "desc": "Todo negócio que depende de cliente da cidade. Estes são os que mais me procuram.",
                "colunas": ["Tipo de negócio", "Página com o que muda para ele"],
                "linhas": [
                    ["Clínicas e consultórios", "<a href=\"/marketing-para-clinicas/\">Marketing para clínicas</a>"],
                    ["Médicos", "<a href=\"/seo-para-medicos/\">Marketing médico</a>"],
                    ["Dentistas", "<a href=\"/seo-para-dentistas/\">Marketing para dentistas</a>"],
                    ["Advogados", "<a href=\"/marketing-para-advogados/\">Marketing para advogados</a>"],
                    ["Imobiliárias e corretores", "<a href=\"/seo-para-imobiliarias/\">Marketing imobiliário</a>"],
                    ["Comércio e prestadores de serviço", "<a href=\"/para-comercios-locais/\">Comércios locais</a>"],
                    ["Pequenas empresas", "<a href=\"/seo-para-pequenas-empresas/\">Pequenas empresas</a>"],
                ],
                "nota": "Veja a lista completa em <a href=\"/nichos/\">todos os nichos atendidos</a>.",
            }),
            ("texto", {
                "tag": "Como escolher",
                "titulo": "Como escolher uma agência de marketing em Goiânia sem errar",
                "ps": [
                    "Antes de fechar com qualquer agência de marketing em Goiânia, inclusive comigo, faça três "
                    "perguntas. Com quem eu vou falar no dia a dia? Como eu vou saber quantos contatos vieram "
                    "do trabalho? O que acontece se eu quiser parar?",
                    "Desconfie de quem promete primeiro lugar no Google ou número certo de clientes. Ninguém "
                    "controla o Google, e o próprio Google avisa isso no "
                    + _A % (GUIA_SEO, "guia oficial para quem contrata esse tipo de serviço") + ". O que uma "
                    "agência séria promete é o que vai ser feito, em que prazo, e como você vai acompanhar.",
                ],
            }),
            ("texto", {
                "tag": "Quanto custa",
                "titulo": "Quanto custa uma agência de marketing digital em Goiânia?",
                "ps": [
                    "Depende do que a sua empresa precisa. Arrumar o perfil no Google é um trabalho pequeno. "
                    "Fazer site, cuidar do Google todo mês e rodar anúncio é um trabalho maior. Por isso o "
                    "valor é sob medida, e não uma tabela igual para todo mundo.",
                    "Como aqui não tem atendente, sala grande nem equipe parada para pagar, costuma sair mais "
                    "em conta do que você imagina. O orçamento é grátis e chega pelo WhatsApp em até 24 horas, "
                    "junto com o que eu vi no Google da sua empresa.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": -1,
                "itens": [
                    ("Aparecer no Google e no mapa", "Para quem quer ser encontrado sem pagar por clique.",
                     ["Perfil da empresa no Google", "Site ajustado para a busca", "Avaliações reais"],
                     "Olá, Renan! Quero que a minha empresa apareça no Google e no mapa. Sou de Goiânia.",
                     "Quero aparecer no Google"),
                    ("Site novo", "Para quem não tem site ou tem um que não traz contato.",
                     ["Site feito para ser encontrado", "Botão de WhatsApp em toda página",
                      "Ligado ao perfil no Google"],
                     "Olá, Renan! Quero um orçamento de site para a minha empresa. Sou de Goiânia.",
                     "Quero um site"),
                    ("Anúncios no Google", "Para quem precisa de contato já.",
                     ["Campanha no Google Ads", "Página própria para o anúncio", "Relatório de contatos"],
                     "Olá, Renan! Quero anunciar a minha empresa no Google. Sou de Goiânia.",
                     "Quero anunciar"),
                    ("Tudo junto", "Para quem quer uma agência cuidando de tudo.",
                     ["Google, site e anúncios", "Um plano só, em ordem de prioridade", "Acompanhamento mensal"],
                     "Olá, Renan! Quero uma agência cuidando do marketing digital da minha empresa em Goiânia.",
                     "Quero o plano completo"),
                ],
            }),
            ("texto", {
                "tag": "Onde eu atendo",
                "titulo": "Agência de marketing digital em Goiânia, Aparecida e região",
                "ps": [
                    "Eu atendo presencialmente em Goiânia, em qualquer bairro, e também em "
                    "<a href=\"/consultoria-seo/aparecida-de-goiania/\">Aparecida de Goiânia</a>, Senador "
                    "Canedo, Trindade e <a href=\"/consultoria-seo/anapolis/\">Anápolis</a>. Para empresas de "
                    "outras cidades o trabalho é o mesmo, feito online: veja a "
                    "<a href=\"/consultoria-seo-local/\">consultoria de SEO para todo o Brasil</a>.",
                    "Se a sua dúvida ainda é mais simples, comece por aqui: "
                    "<a href=\"/blog/como-colocar-minha-empresa-no-google/\">como colocar a minha empresa no "
                    "Google</a> e <a href=\"/como-aparecer-no-google/\">como aparecer no Google</a>.",
                ],
            }),
            ("fontes", {"itens": [
                ("Google: como o resultado local é definido (distância, relevância e reputação)", RANKING),
                ("Google: guia de otimização para a busca, com orientações para quem contrata o serviço", GUIA_SEO),
                ("Google: como a pesquisa funciona", COMO_BUSCA),
            ]}),
        ],
        "faq": [
            ("A RCB SEO é uma agência de marketing digital em Goiânia?",
             "Sim. A RCB SEO fica em Goiânia e faz o trabalho de uma agência de marketing digital voltada para o "
             "Google: site, perfil da empresa no mapa, anúncios e presença nas respostas de IA. A diferença é o "
             "tamanho: quem atende e quem executa é a mesma pessoa, o consultor Renan Carvalho Barbosa."),
            ("Quanto custa contratar uma agência de marketing digital em Goiânia?",
             "O valor depende do que a empresa precisa: só o perfil no Google, site, anúncios ou tudo junto. Na "
             "RCB SEO o orçamento é sob medida, grátis, e chega pelo WhatsApp em até 24 horas."),
            ("Vocês fazem gestão de redes sociais?",
             "Não. O foco é fazer a empresa ser encontrada no Google, no mapa e nas respostas de IA, e transformar "
             "a visita em contato. Para postagens no Instagram, uma agência de redes sociais atende melhor."),
            ("Em quanto tempo o marketing digital dá resultado?",
             "Anúncio no Google começa a trazer visita nos primeiros dias. O resultado gratuito, no Google e no "
             "mapa, costuma levar de semanas a alguns meses e depende do ramo e dos concorrentes. Eu não prometo "
             "posição nem prazo."),
            ("Preciso assinar contrato de fidelidade?",
             "Não. Para encerrar o acompanhamento basta avisar com 30 dias de antecedência. As condições vão por "
             "escrito junto com o orçamento."),
            ("Vocês atendem presencialmente em Goiânia?",
             "Sim, em Goiânia e na região metropolitana, com hora marcada. Empresas de outras cidades são "
             "atendidas online."),
            ("Qual a diferença entre agência de marketing e consultor de SEO?",
             "A agência costuma cuidar de várias frentes com uma equipe, incluindo redes sociais. O consultor de "
             "SEO cuida de uma frente, o Google, e fala direto com o dono. A RCB SEO trabalha do segundo jeito, "
             "com os serviços que mais trazem cliente para empresa local."),
        ],
        "relacionados_titulo": "Leia também sobre marketing digital em Goiânia",
        "relacionados": [
            ("/blog/consultor-seo-ou-agencia-de-marketing-digital/", "Consultor de SEO ou agência de marketing digital?",
             "As diferenças na prática e para quem cada um serve."),
            ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia",
             "Site feito para ser encontrado no Google, com orçamento em 24 horas."),
            ("/google-meu-negocio-goiania/", "Google Meu Negócio em Goiânia",
             "A sua empresa no mapa quando o cliente procura perto."),
            ("/blog/seo-ou-trafego-pago-empresa-local/", "SEO ou tráfego pago para empresa local?",
             "Quando vale anunciar e quando vale investir no resultado gratuito."),
        ],
        "cta_final": ("Procurando uma agência de marketing digital em Goiânia?",
                      "Me conte o que a sua empresa faz e em qual bairro atende. Eu olho o seu Google hoje e "
                      "te digo, com franqueza, por onde começar."),
    },
    # ------------------------------------------------------------------------------------
    {
        "slug": LP_ADV,
        "tipo": "servico",
        "nacional": True,
        "data": DATA,
        "publico": "Advogados e escritórios de advocacia de todo o Brasil",
        "title": "Landing Page para Advogados Dentro das Normas da OAB | RCB SEO",
        "desc": ("Landing page para advogados: página única para quem clica no anúncio do escritório, dentro "
                 "do Provimento 205/2021 da OAB. Orçamento grátis em 24h pelo WhatsApp."),
        "trilha": "Landing Page para Advogados",
        "servico": "Criação de landing page para advogados e escritórios de advocacia",
        "alternativos": ["Landing page para advocacia", "Landing page advogado",
                         "Landing page para escritório de advocacia"],
        "eyebrow": "Online para todo o Brasil · presencial em Goiânia",
        "h1": "Landing page para advogados: a página que recebe quem clicou no anúncio do escritório",
        "sub": ("Landing page para advogados é uma página única, sobre uma área de atuação só, feita para "
                "quem clicou no anúncio do escritório entender em poucos segundos se você atende o caso "
                "dele e mandar mensagem. Eu crio essa página dentro das normas de publicidade da OAB."),
        "cta_hero": "Quero uma landing page para o escritório",
        "botao2": ("#orcamento", "Ver como funciona o orçamento"),
        "msg": "Olá, Renan! Sou advogado e quero uma landing page para o meu escritório.",
        "pills": ["Dentro do Provimento 205/2021", "Orçamento em até 24h", "Sem fidelidade"],
        "painel_h2": "Landing page para advogados, em uma frase",
        "painel": [
            "Quem procura advogado no Google quase sempre está com um problema urgente.",
            "Se o anúncio leva para a página inicial do escritório, a pessoa se perde e sai.",
            "A landing page fala só do problema dela e mostra o caminho para falar com você.",
        ],
        "faq_titulo": "Perguntas frequentes sobre landing page para advogados",
        "secoes": [
            ("texto", {
                "tag": "O que é",
                "titulo": "O que é uma landing page para advogados?",
                "ps": [
                    "É uma página de internet com um assunto só. Em vez de apresentar o escritório inteiro, "
                    "como faz um site, ela trata de uma área de atuação: por exemplo, direito trabalhista "
                    "para quem foi demitido, ou inventário para quem perdeu um familiar.",
                    "Ela existe para receber quem clicou num anúncio. A pessoa pesquisou um problema, viu o "
                    "anúncio do escritório e clicou. O que ela encontra do outro lado decide se ela manda "
                    "mensagem ou volta para o Google e clica no próximo.",
                ],
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que o anúncio do escritório gasta e não traz contato?",
                "ps": [
                    "Na maioria dos casos que eu vejo, o anúncio está certo e a página está errada. O clique "
                    "cai na página inicial do escritório, que fala de dez áreas, da história dos sócios e "
                    "da missão. Quem está preocupado com uma demissão não vai procurar a sua área no menu.",
                    "Cada clique custa dinheiro. Página que não conversa com o problema de quem clicou é "
                    "verba jogada fora, e é por isso que tanto advogado desiste de anunciar achando que "
                    "anúncio não funciona para advocacia.",
                ],
                "card_titulo": "O que faz a pessoa sair sem falar com você",
                "card": [
                    "Página que fala de todas as áreas ao mesmo tempo.",
                    "Texto em linguagem de petição.",
                    "Nenhum botão de contato à vista no celular.",
                    "Página lenta para abrir.",
                    "Nada que mostre quem é o advogado.",
                ],
            }),
            ("cards", {
                "tag": "O que entra",
                "titulo": "O que tem numa landing page para advogados bem feita",
                "desc": "Cada parte existe por um motivo. Nenhuma é enfeite.",
                "itens": [
                    ("Uma área de atuação por página",
                     "Quem pesquisou sobre pensão alimentícia quer ler sobre pensão alimentícia. Uma página "
                     "para cada área conversa melhor com quem chega e aproveita melhor a verba do anúncio."),
                    ("Linguagem de quem tem o problema",
                     "O texto explica a situação com as palavras que o cliente usa, sem juridiquês. Informar "
                     "com clareza é justamente o que a OAB permite."),
                    ("Quem é o advogado",
                     "Nome, número da OAB, foto e formação. A pessoa vai confiar um problema sério a alguém, "
                     "e precisa ver quem é esse alguém."),
                    ("Caminho curto para o contato",
                     "Botão de WhatsApp visível o tempo todo no celular, que é de onde vem a maior parte dos "
                     "cliques em anúncio."),
                    ("Página leve",
                     "Página que demora para abrir perde a visita antes de aparecer. Eu entrego a página leve "
                     "e testada no celular."),
                    ("Medição",
                     "Você fica sabendo quantas pessoas chegaram pelo anúncio e quantas chamaram no WhatsApp. "
                     "Sem isso não dá para saber se o anúncio está pagando."),
                ],
            }),
            ("ajuda", {
                "titulo": "Já anuncia e não está vendo contato chegar?",
                "texto": "Me manda o endereço da página para onde o seu anúncio leva. Eu olho e te digo, sem "
                         "compromisso, o que está fazendo a pessoa sair sem falar com o escritório.",
                "msg": "Olá, Renan! Sou advogado, já anuncio no Google e quero que você olhe a página do meu anúncio.",
                "botao": "Quero que você olhe a minha página",
            }),
            ("split", {
                "tag": "Normas da OAB",
                "titulo": "Landing page para advogados pode? O que a OAB permite",
                "ps": [
                    "Pode. O " + _A % (OAB_205, "Provimento 205/2021 da OAB") + " permite a publicidade "
                    "da advocacia, inclusive com anúncio pago, desde que ela seja informativa, discreta e "
                    "sóbria. O que continua proibido é captar cliente de forma mercantil e prometer resultado.",
                    "Na prática, a página informa: explica a situação, apresenta o advogado e mostra como "
                    "entrar em contato. Ela não promete ganhar a causa, não fala em valor de honorários como "
                    "chamariz e não usa caso de cliente como propaganda. Eu escrevo a página dentro desses "
                    "limites, e a conferência final com o Código de Ética é sempre sua, que é quem assina.",
                ],
                "card_titulo": "O que não entra na página",
                "card": [
                    "Promessa de resultado ou de êxito.",
                    "Preço ou desconto como chamada.",
                    "Depoimento usado para captar cliente.",
                    "Expressões como “o melhor” ou “o número 1”.",
                    "Urgência falsa para forçar o contato.",
                ],
            }),
            ("tabela", {
                "tag": "Comparação",
                "titulo": "Landing page ou site para o escritório de advocacia?",
                "desc": "Não é um ou outro. Cada um resolve uma coisa.",
                "colunas": ["O que muda", "Landing page", "Site do escritório"],
                "linhas": [
                    ["Para que serve", "Receber quem clicou no anúncio", "Apresentar o escritório inteiro"],
                    ["Quantas páginas", "Uma, sobre uma área", "Várias, uma por área e por assunto"],
                    ["De onde vem a visita", "Do anúncio pago", "Da busca gratuita do Google e do mapa"],
                    ["Quando traz contato", "Assim que o anúncio começa", "Com o tempo, conforme o Google conhece o site"],
                ],
                "nota": "Muitos escritórios começam pela landing page com anúncio e depois fazem o site.",
            }),
            ("texto", {
                "tag": "O conjunto",
                "titulo": "A landing page sozinha resolve?",
                "ps": [
                    "Ela resolve uma parte: o que acontece depois do clique. Antes dela vem o anúncio, que "
                    "precisa aparecer para a pessoa certa. Veja o "
                    "<a href=\"/trafego-pago-para-advogados/\">tráfego pago para advogados</a>.",
                    "E para o escritório ser encontrado sem pagar por clique, o caminho é o "
                    "<a href=\"/criacao-de-site-para-advogado/\">site para advogado</a> junto com o perfil no "
                    "Google. O quadro completo está em "
                    "<a href=\"/marketing-para-advogados/\">marketing para advogados</a>. Se o escritório fica "
                    "em Goiânia, eu atendo pessoalmente: conheça a "
                    "<a href=\"/agencia-de-marketing-digital-goiania/\">agência de marketing digital em Goiânia</a>.",
                ],
            }),
            ("texto", {
                "tag": "Quanto custa",
                "titulo": "Quanto custa uma landing page para advogados?",
                "ps": [
                    "O valor é sob medida. Depende de quantas áreas de atuação vão ter página, se o texto "
                    "vai ser escrito do zero e se você quer que eu cuide também do anúncio. Uma página para "
                    "uma área é um trabalho pequeno.",
                    "Para muito escritório, uma única página bem feita já muda o retorno do anúncio, e pode "
                    "sair mais em conta do que você imagina. O orçamento é grátis e chega pelo WhatsApp em "
                    "até 24 horas.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde o escritório quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": -1,
                "itens": [
                    ("Uma landing page", "Para testar uma área de atuação.",
                     ["Página única para uma área", "Texto dentro das normas da OAB", "Botão de WhatsApp e medição"],
                     "Olá, Renan! Sou advogado e quero uma landing page para uma área de atuação.",
                     "Quero uma landing page"),
                    ("Landing page + anúncio", "Para quem quer contato já.",
                     ["Página para a área escolhida", "Campanha no Google Ads", "Relatório de contatos"],
                     "Olá, Renan! Sou advogado e quero landing page com anúncio no Google.",
                     "Quero página e anúncio"),
                    ("Uma página por área", "Para o escritório com várias frentes.",
                     ["Página própria para cada área", "Mesmo padrão visual do escritório", "Medição separada por área"],
                     "Olá, Renan! Quero landing pages para as áreas de atuação do meu escritório.",
                     "Quero várias páginas"),
                ],
            }),
            ("fontes", {"itens": [
                ("OAB: Provimento 205/2021, sobre a publicidade e a informação da advocacia", OAB_205),
                ("Google: guia de otimização para a busca", GUIA_SEO),
            ]}),
        ],
        "faq": [
            ("Advogado pode ter landing page e anunciar no Google?",
             "Pode. O Provimento 205/2021 da OAB permite a publicidade da advocacia, inclusive paga, desde que "
             "seja informativa, discreta e sóbria, sem captação mercantil de clientela e sem promessa de resultado."),
            ("Qual a diferença entre landing page e site para advogado?",
             "A landing page é uma página única sobre uma área de atuação, feita para receber quem clicou no "
             "anúncio. O site apresenta o escritório inteiro e é encontrado pela busca gratuita do Google."),
            ("Quanto custa uma landing page para advogados?",
             "O valor é sob medida e depende do número de áreas e do texto. Na RCB SEO o orçamento é grátis e "
             "chega pelo WhatsApp em até 24 horas."),
            ("Preciso de uma landing page para cada área de atuação?",
             "É o que funciona melhor. Quem pesquisou sobre um problema quer ler sobre aquele problema. Dá para "
             "começar por uma área só e ampliar depois."),
            ("A landing page pode mostrar depoimento de cliente?",
             "A orientação mais segura é não usar depoimento como forma de captar cliente. Na dúvida, vale a "
             "leitura do Provimento 205/2021 e a consulta à seccional da OAB do seu estado."),
            ("Vocês atendem escritórios de qualquer cidade?",
             "Sim. O trabalho é feito online para todo o Brasil, e presencialmente em Goiânia e região."),
        ],
        "relacionados_titulo": "Leia também sobre marketing para advogados",
        "relacionados": [
            ("/marketing-para-advogados/", "Marketing para advogados",
             "O quadro completo: Google, site, perfil e anúncio dentro das normas da OAB."),
            ("/trafego-pago-para-advogados/", "Tráfego pago para advogados",
             "Como o anúncio no Google funciona para a advocacia."),
            ("/criacao-de-site-para-advogado/", "Site para advogado",
             "O site do escritório feito para ser encontrado."),
            ("/blog/advogado-pode-fazer-marketing/", "Advogado pode fazer marketing?",
             "O que a OAB permite e o que continua proibido."),
        ],
        "cta_final": ("Quer uma landing page para o seu escritório?",
                      "Me conte a sua área de atuação e a cidade. Eu te mando o orçamento em até 24 horas, "
                      "com o que eu vi nos anúncios de advocacia da sua região."),
    },
]
