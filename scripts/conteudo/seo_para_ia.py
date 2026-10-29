# -*- coding: utf-8 -*-
"""
Conteúdo do 5º pilar: SEO para IA (GEO/AEO). Rodada de 28/10/2026.

  /seo-para-ia/                                   pilar comercial
  /como-aparecer-no-chatgpt/                      satélite
  /ai-overviews-e-gemini/                         satélite (Google com IA)
  /o-que-e-geo-e-aeo/                             satélite
  /auditoria-de-seo-para-ia/                      comercial de entrada

Termos e decisões: docs/visibilidade-ia/MAPA-DE-TERMOS.md.

Regras (não afrouxar):
  * SEM PREÇO da RCB e sem faixa de preço inventada (o mercado de GEO não tem referência pública).
  * Nenhuma promessa de ser citado, de posição ou de prazo para aparecer na IA.
  * Serviço novo: NÃO há case de IA. Não inventar cliente, número ou depoimento; não usar o selo
    "Mais pedido" nos cartões de orçamento.
  * Fato técnico só com fonte oficial linkada (OpenAI, Google, Anthropic, Perplexity, Microsoft).
  * Toda página fala de RESPOSTA DE IA; quando encosta em SEO comum, linka a página que já existe.

O texto é escrito à mão aqui; o gerador (scripts/gerar-seo-para-ia.py) só monta o invólucro.
Tipos de seção: os do gerar-servicos-marketing.py + "tabela" e "fontes".
"""

DATA = "2026-10-29"

_A = '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'

# endereços finais conferidos em 29/10/2026 (os antigos redirecionavam para estes)
OPENAI_BOTS = "https://developers.openai.com/api/docs/bots"
GOOGLE_IA = "https://developers.google.com/search/docs/appearance/ai-features"
GOOGLE_CRAWLERS = "https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers"
GOOGLE_UTIL = "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
GOOGLE_SPAM = "https://developers.google.com/search/docs/essentials/spam-policies"
ANTHROPIC_BOTS = ("https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-"
                  "and-how-can-site-owners-block-the-crawler")
PERPLEXITY_BOTS = "https://docs.perplexity.ai/docs/resources/perplexity-crawlers"
PAPER_GEO = "https://arxiv.org/abs/2311.09735"
BING_PLACES = "https://www.bingplaces.com/"
BING_WEBMASTER = "https://www.bing.com/webmasters"

FONTES_BASE = [
    ("OpenAI: robôs da OpenAI (OAI-SearchBot, GPTBot, ChatGPT-User)", OPENAI_BOTS),
    ("Google Search Central: recursos de IA e o seu site", GOOGLE_IA),
    ("Anthropic: como funcionam os robôs do Claude", ANTHROPIC_BOTS),
    ("Perplexity: robôs do Perplexity", PERPLEXITY_BOTS),
]

PILAR = "/seo-para-ia/"
_REL_PILAR = (PILAR, "SEO para IA", "O serviço completo: o que é feito, prazo, como medir e orçamento.")
_REL_CHATGPT = ("/como-aparecer-no-chatgpt/", "Como aparecer no ChatGPT",
                "Por que não existe cadastro e o que o ChatGPT lê para indicar uma empresa.")
_REL_GOOGLE = ("/ai-overviews-e-gemini/", "AI Overviews e Gemini",
               "Como a sua empresa entra na resposta de IA do próprio Google.")
_REL_GEO = ("/o-que-e-geo-e-aeo/", "O que é GEO e AEO",
            "Os nomes novos do SEO para IA, explicados sem complicação.")
_REL_AUDITORIA = ("/auditoria-de-seo-para-ia/", "Auditoria de SEO para IA",
                  "Descubra o que o ChatGPT e o Gemini dizem hoje sobre o seu ramo.")
_REL_SERVICOS = ("/servicos/", "Todos os serviços", "SEO, Google Meu Negócio, sites, anúncios e YouTube.")
_REL_PERFIL = ("/google-perfil-empresa/", "Google Meu Negócio",
               "O perfil no Google é uma das fontes que as IAs mais leem sobre empresas locais.")

PAGINAS = [
    # =====================================================================
    # PILAR
    # =====================================================================
    {
        "slug": "seo-para-ia",
        "tipo": "servico",
        "nacional": False,
        "data": DATA,
        "publico": "Donos de negócio que querem ser indicados pelo ChatGPT, pelo Gemini e pelo Google com IA",
        "title": "SEO para IA: Como Aparecer no ChatGPT e no Gemini | RCB SEO",
        "desc": ("SEO para IA é preparar sua empresa para ser indicada pelo ChatGPT, Gemini e Google com IA. "
                 "Veja o que é feito, prazo e como medir. Orçamento grátis."),
        "trilha": "SEO para IA",
        "servico": "SEO para IA",
        "eyebrow": "Online no Brasil · Presencial em Goiânia",
        "h1": "SEO para IA: como fazer sua empresa aparecer no ChatGPT, no Gemini e no Google",
        "sub": ("SEO para IA é o trabalho de deixar a sua empresa fácil de encontrar, entender e indicar por "
                "assistentes como o ChatGPT e o Gemini. Não existe cadastro para isso: a IA indica quem ela "
                "consegue confirmar em fontes públicas, e é nessas fontes que o trabalho acontece."),
        "cta_hero": "Quero minha empresa na resposta da IA",
        "botao2": ("#orcamento", "Como funciona o orçamento"),
        "msg": "Olá, Renan! Quero que a minha empresa apareça nas respostas do ChatGPT e do Gemini.",
        "pills": ["Orçamento em até 24h", "Prazo por escrito", "Sem fidelidade"],
        "painel_h2": "SEO para IA em uma frase",
        "painel": [
            "Quando o seu cliente pergunta ao ChatGPT “quem indica para…”, a IA monta a resposta com o que acha na internet.",
            "Se a sua empresa não está nessas fontes, ou está com dados confusos, ela fica de fora.",
            "O trabalho é arrumar essas fontes e criar as que faltam.",
        ],
        "faq_titulo": "Perguntas frequentes sobre SEO para IA",
        "secoes": [
            ("texto", {
                "tag": "O que é",
                "titulo": "O que é SEO para IA?",
                "ps": [
                    "SEO para IA é deixar a sua empresa pronta para ser citada nas respostas escritas por "
                    "assistentes de inteligência artificial. O SEO de sempre cuida da lista de links do Google. "
                    "O SEO para IA cuida do texto pronto que o ChatGPT, o Gemini, o Perplexity e o próprio "
                    "Google escrevem quando alguém pergunta “qual é o melhor…” ou “quem faz…”.",
                    "No mercado esse trabalho também é chamado de GEO e AEO, siglas em inglês para "
                    "“otimização para mecanismos generativos” e “otimização para mecanismos de resposta”. "
                    "São nomes diferentes para a mesma ideia. Se quiser entender a diferença, veja "
                    "<a href=\"/o-que-e-geo-e-aeo/\">o que é GEO e AEO</a>.",
                ],
            }),
            ("tabela", {
                "tag": "A diferença",
                "titulo": "Qual a diferença entre aparecer no Google e aparecer na resposta da IA?",
                "desc": "Aparecer na resposta da IA é mais disputado que aparecer na busca comum, porque cabem bem menos empresas.",
                "colunas": ["", "Busca comum do Google", "Resposta de IA (ChatGPT, Gemini)"],
                "linhas": [
                    ["O que a pessoa vê", "Uma lista de links e o mapa", "Um texto pronto, com poucas indicações"],
                    ["Quantas empresas cabem", "Dez links por página, mais o mapa", "Em geral, um punhado de nomes"],
                    ["Existe cadastro?", "Sim, o Perfil da Empresa no Google", "Não. A IA lê fontes públicas"],
                    ["O que pesa", "Site, perfil, avaliações, links", "As mesmas coisas, mais a clareza e a coerência dos dados"],
                    ["Como medir", "Ferramenta grátis do Google mostra buscas e cliques", "Ainda depende de perguntar à IA e anotar"],
                ],
                "nota": "Comparação feita pela RCB SEO a partir da documentação oficial do Google e da OpenAI.",
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que a sua empresa não aparece no ChatGPT?",
                "ps": [
                    "A sua empresa não aparece no ChatGPT porque a IA não encontrou informação suficiente, "
                    "ou encontrou informação desencontrada, sobre ela. A IA não visita a sua loja nem conhece "
                    "a sua fama no bairro. Ela só sabe o que está escrito em algum lugar que ela consegue ler.",
                    "Os motivos mais comuns são simples: site que não explica com clareza o que a empresa faz e "
                    "onde atende; perfil no Google incompleto; nome, telefone e endereço diferentes em cada lugar; "
                    "nenhuma menção da empresa fora do próprio site; ou um site que bloqueia, sem querer, os "
                    "robôs que as IAs usam para ler a internet.",
                ],
                "card_titulo": "O que mais tira uma empresa da resposta",
                "card": [
                    "Site que não diz o que faz, para quem e onde.",
                    "Perfil no Google pela metade.",
                    "Nome e telefone diferentes em cada lugar.",
                    "Ninguém fala da empresa fora do site dela.",
                    "Robô da IA bloqueado no site.",
                ],
            }),
            ("cards", {
                "tag": "O que é feito",
                "titulo": "O que é feito no SEO para IA?",
                "desc": "O trabalho acontece em cinco frentes. Nenhuma delas é truque: é deixar a verdade sobre a sua empresa fácil de achar.",
                "itens": [
                    ("1. Teste do ponto de partida",
                     "Eu faço ao ChatGPT, ao Gemini, ao Perplexity e ao Copilot as perguntas que o seu cliente "
                     "faria, e anoto quem aparece, quem não aparece e de onde a IA tirou a informação. Esse é o "
                     "começo da <a href=\"/auditoria-de-seo-para-ia/\">auditoria de SEO para IA</a>."),
                    ("2. Robôs liberados",
                     "Confiro se o seu site deixa entrar os robôs das IAs. A OpenAI, por exemplo, explica que o "
                     + _A % (OPENAI_BOTS, "robô OAI-SearchBot") + " é o que leva os sites para a busca do ChatGPT. "
                     "Se ele estiver bloqueado, o site some dessa busca."),
                    ("3. Dados iguais em todo lugar",
                     "Nome, endereço, telefone, horário e serviços iguais no site, no "
                     "<a href=\"/google-perfil-empresa/\">Perfil da Empresa no Google</a>, no "
                     + _A % (BING_PLACES, "Bing Places") + " e nas redes. Dado desencontrado deixa a IA em dúvida, "
                     "e IA em dúvida não indica."),
                    ("4. Site que responde",
                     "Páginas que respondem, logo na primeira frase, as perguntas reais do seu cliente: o que você "
                     "faz, quanto tempo leva, onde atende, como funciona. É o formato que a IA consegue copiar e citar."),
                    ("5. Menções fora do site",
                     "Diretórios do seu ramo, associações, imprensa da cidade, vídeos no YouTube, avaliações "
                     "reais. Quanto mais lugares confiáveis confirmam que a sua empresa existe e é boa no que faz, "
                     "mais segura a IA fica para citar você."),
                ],
            }),
            ("texto", {
                "tag": "ChatGPT, Gemini, Perplexity e Copilot",
                "titulo": "Cada IA lê a internet de um jeito?",
                "ps": [
                    "Cada IA lê a internet de um jeito, mas todas dependem das mesmas fontes públicas. O "
                    "<strong>ChatGPT</strong> busca na internet com robôs próprios e mostra os sites de onde "
                    "tirou a resposta (veja <a href=\"/como-aparecer-no-chatgpt/\">como aparecer no ChatGPT</a>). "
                    "O <strong>Gemini</strong> e as respostas de IA do Google usam o índice do próprio Google, "
                    "então um site que já aparece bem no Google sai na frente (veja "
                    "<a href=\"/ai-overviews-e-gemini/\">AI Overviews e Gemini</a>).",
                    "O <strong>Perplexity</strong> mostra as fontes numeradas em cada resposta e tem o próprio robô, "
                    "o " + _A % (PERPLEXITY_BOTS, "PerplexityBot") + ". O <strong>Copilot</strong>, da Microsoft, "
                    "se apoia no Bing: por isso o perfil no " + _A % (BING_PLACES, "Bing Places") + " e o "
                    + _A % (BING_WEBMASTER, "Bing Webmaster Tools") + " entram no trabalho, coisa que quase "
                    "ninguém faz no Brasil.",
                ],
            }),
            ("texto", {
                "tag": "Prazo",
                "titulo": "Quanto tempo leva para aparecer nas respostas da IA?",
                "ps": [
                    "Os ajustes no site e nos perfis levam dias. Aparecer na resposta leva mais, em geral semanas "
                    "ou meses, porque depende de a IA voltar a ler as fontes e de a sua empresa ganhar menções "
                    "fora do próprio site. Ninguém controla quando o ChatGPT ou o Gemini vão citar uma empresa.",
                    "Por isso eu não prometo prazo para aparecer, nem que a sua empresa vai ser citada. O que eu "
                    "prometo, por escrito, é o que vai ser feito e quando. E eu repito as mesmas perguntas à IA "
                    "todo mês, para você ver se mudou alguma coisa.",
                ],
            }),
            ("split", {
                "tag": "Com franqueza",
                "titulo": "O que eu não prometo no SEO para IA",
                "ps": [
                    "SEO para IA é um serviço novo no mundo inteiro. Eu ainda não tenho um case de IA para te "
                    "mostrar, e não vou inventar um. O que eu tenho são "
                    "<a href=\"/cases/\">resultados reais em SEO local e Google Meu Negócio</a>, que são a base "
                    "do que a IA lê, e um método que segue a documentação oficial de quem faz as IAs.",
                    "Desconfie de quem vende pacote para “colocar sua empresa no ChatGPT” com resultado garantido. "
                    "As " + _A % (GOOGLE_SPAM, "políticas contra spam do Google") + " valem também para as "
                    "respostas de IA dele, e truque que funciona hoje costuma virar punição amanhã.",
                ],
                "card_titulo": "O que eu não prometo",
                "card": [
                    "Que a IA vai citar a sua empresa.",
                    "Prazo para aparecer na resposta.",
                    "Primeiro lugar em pergunta nenhuma.",
                    "Avaliação comprada ou inventada.",
                    "Cadastro no ChatGPT (ele não existe).",
                ],
            }),
            ("texto", {
                "tag": "Como medir",
                "titulo": "Como saber se a sua empresa começou a aparecer na IA?",
                "ps": [
                    "Dá para medir de duas formas. A primeira é o "
                    "<a href=\"/ferramentas/\">Search Console</a>: o Google informa que as visitas vindas das "
                    + _A % (GOOGLE_IA, "respostas de IA dele entram no relatório de desempenho") + ", junto "
                    "com a busca comum. A segunda é a mais direta: fazer todo mês as mesmas perguntas ao "
                    "ChatGPT, ao Gemini, ao Perplexity e ao Copilot e anotar se a sua empresa aparece e quem "
                    "aparece no lugar dela.",
                    "Eu faço essa planilha para você: pergunta, assistente, se a sua empresa apareceu, quais "
                    "concorrentes apareceram e a data. Em poucos meses dá para ver a tendência, sem achismo.",
                ],
            }),
            ("texto", {
                "tag": "Quanto custa",
                "titulo": "Quanto custa o SEO para IA?",
                "ps": [
                    "O SEO para IA não tem preço de tabela, nem aqui nem no mercado: o serviço é novo e cada "
                    "empresa monta de um jeito. O que define o valor do seu projeto é o tamanho do ramo e da "
                    "região, quantas páginas o site precisa ganhar ou arrumar, em quantos perfis os dados "
                    "estão desencontrados e se você quer acompanhamento mensal.",
                    "Se a sua empresa já tem o Perfil no Google bem cuidado e um site organizado, o trabalho é "
                    "menor e pode sair bem mais em conta do que você imagina. O orçamento é grátis e chega pelo "
                    "WhatsApp em até 24 horas.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa quer começar no SEO para IA?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": -1,
                "itens": [
                    ("Auditoria de SEO para IA", "Para saber o que a IA diz hoje sobre o seu ramo.",
                     ["Perguntas reais nas 4 IAs e no Google", "Quem aparece e de onde veio",
                      "Lista do que arrumar primeiro"],
                     "Olá, Renan! Quero a auditoria de SEO para IA da minha empresa.", "Pedir orçamento"),
                    ("Preparar a empresa para a IA", "Para quem quer arrumar a casa de uma vez.",
                     ["Auditoria incluída", "Site, Perfil no Google e Bing Places",
                      "Robôs liberados e dados iguais"],
                     "Olá, Renan! Quero preparar a minha empresa para aparecer nas respostas da IA.",
                     "Pedir orçamento"),
                    ("Acompanhamento mensal", "Para quem quer ver a evolução todo mês.",
                     ["Teste mensal nas 4 IAs", "Páginas novas com respostas",
                      "Busca de menções fora do site"],
                     "Olá, Renan! Quero acompanhamento mensal de SEO para IA.", "Pedir orçamento"),
                ],
            }),
            ("texto", {
                "tag": "Onde eu atendo",
                "titulo": "SEO para IA em Goiânia e no Brasil",
                "ps": [
                    "Eu atendo online empresas de todo o Brasil e presencialmente em Goiânia e região. Para "
                    "empresa que atende na cidade, o SEO para IA anda junto com o "
                    "<a href=\"/google-perfil-empresa/\">Google Meu Negócio</a> e com o "
                    "<a href=\"/consultoria-seo-local/\">SEO local</a>: quando alguém pergunta à IA "
                    "“qual dentista indicar em Goiânia”, as fontes que ela usa são quase as mesmas do mapa do Google.",
                ],
            }),
            ("fontes", {"itens": FONTES_BASE + [
                ("Google Search Central: políticas contra spam", GOOGLE_SPAM),
                ("Pesquisa “GEO: Generative Engine Optimization” (Aggarwal e outros, 2023)", PAPER_GEO),
            ]}),
        ],
        "faq": [
            ("Dá para cadastrar a minha empresa no ChatGPT?",
             "Não. O ChatGPT não tem cadastro de empresas, como o Google tem o Perfil da Empresa. Ele indica quem "
             "consegue confirmar em fontes públicas: site, Perfil no Google, Bing, diretórios, avaliações e "
             "notícias. Por isso o trabalho é deixar essas fontes completas e iguais entre si."),
            ("SEO para IA substitui o SEO normal?",
             "Não substitui, depende dele. As respostas de IA do Google usam o índice do próprio Google, e o "
             "ChatGPT também busca páginas na internet. Uma empresa que não aparece na busca comum dificilmente "
             "aparece na resposta da IA. O SEO para IA é uma camada a mais."),
            ("Quanto tempo leva para a minha empresa aparecer na IA?",
             "Os ajustes levam dias, mas aparecer na resposta costuma levar semanas ou meses e não depende só de "
             "mim. A IA precisa voltar a ler as fontes e a empresa precisa ganhar menções. Eu não prometo prazo; "
             "prometo, por escrito, o que vai ser feito e o teste mensal."),
            ("Você garante que a IA vai indicar a minha empresa?",
             "Não. Ninguém controla o que o ChatGPT ou o Gemini respondem, e quem garante isso está prometendo o "
             "que não pode cumprir. O que eu me comprometo a fazer é o trabalho combinado e a medição mensal, com "
             "as mesmas perguntas, para você ver a evolução."),
            ("Funciona para empresa pequena e local?",
             "Funciona, e muitas vezes é onde faz mais diferença. Perguntas como “qual pet shop indicar no meu "
             "bairro” têm poucas empresas bem descritas na internet. Quem arruma o Perfil no Google, o site e as "
             "menções primeiro sai na frente."),
            ("Quanto custa o SEO para IA?",
             "Depende do tamanho do ramo, da região, de quanto o site e os perfis precisam ser arrumados e se há "
             "acompanhamento mensal. Não existe preço de tabela. O orçamento é individual, grátis e chega pelo "
             "WhatsApp em até 24 horas."),
            ("Existe fidelidade?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento."),
        ],
        "relacionados_titulo": "Leia também sobre SEO para IA",
        "relacionados": [_REL_CHATGPT, _REL_GOOGLE, _REL_GEO, _REL_AUDITORIA],
        "cta_final": ("Quer saber o que a IA diz hoje sobre o seu ramo?",
                      "Me conte o que a sua empresa faz e onde atende. Eu faço as perguntas que o seu cliente faria "
                      "e te digo, com franqueza, por onde começar."),
    },

    # =====================================================================
    # COMO APARECER NO CHATGPT
    # =====================================================================
    {
        "slug": "como-aparecer-no-chatgpt",
        "tipo": "artigo",
        "data": DATA,
        "title": "Como Aparecer no ChatGPT: Guia para Empresas | RCB SEO",
        "desc": ("Como aparecer no ChatGPT: não existe cadastro. Veja o que o ChatGPT lê para indicar uma "
                 "empresa e o que fazer no site e nos perfis para entrar na resposta."),
        "trilha": "Como aparecer no ChatGPT",
        "servico": "SEO para IA",
        "eyebrow": "Guia para donos de negócio",
        "h1": "Como aparecer no ChatGPT: o guia para a sua empresa ser indicada",
        "sub": ("Para aparecer no ChatGPT, a sua empresa precisa estar descrita com clareza em fontes que ele "
                "consegue ler: o seu site, o Perfil no Google, o Bing, diretórios e avaliações. Não existe "
                "cadastro nem botão de “colocar minha empresa no ChatGPT”."),
        "cta_hero": "Quero ajuda para aparecer no ChatGPT",
        "botao2": ("/seo-para-ia/#orcamento", "Ver como funciona o serviço"),
        "msg": "Olá, Renan! Li o guia e quero ajuda para a minha empresa aparecer no ChatGPT.",
        "pills": ["Atualizado em outubro de 2026", "Com fontes oficiais"],
        "painel_h2": "Como aparecer no ChatGPT, resumido",
        "painel": [
            "Não existe cadastro de empresa no ChatGPT.",
            "Ele busca na internet e mostra de onde tirou a resposta.",
            "Seu site precisa deixar o robô dele entrar.",
            "Dados iguais em todo lugar dão confiança.",
            "Menções fora do site pesam muito.",
        ],
        "faq_titulo": "Perguntas frequentes sobre como aparecer no ChatGPT",
        "secoes": [
            ("texto", {
                "tag": "A dúvida mais comum",
                "titulo": "Como cadastrar a minha empresa no ChatGPT?",
                "ps": [
                    "Não dá para cadastrar a sua empresa no ChatGPT, porque esse cadastro não existe. Muita gente "
                    "procura por isso pensando no Google Meu Negócio, onde você cria o perfil e preenche os dados. "
                    "No ChatGPT não há perfil, formulário nem área de empresas.",
                    "O que existe é outra coisa: quando alguém pergunta “qual eletricista indicar em Goiânia”, o "
                    "ChatGPT pode buscar na internet, ler algumas páginas e escrever a resposta com base nelas. "
                    "Quem aparece é quem estava bem descrito nessas páginas. Então a pergunta certa não é “como "
                    "me cadastrar”, e sim “onde o ChatGPT vai procurar, e o que ele vai encontrar sobre mim”.",
                ],
            }),
            ("texto", {
                "tag": "Como funciona",
                "titulo": "Como o ChatGPT escolhe quais empresas indicar?",
                "ps": [
                    "O ChatGPT escolhe com base no que encontra e consegue confirmar. Quando a busca dele está "
                    "ligada, ele procura páginas na hora e mostra os links das fontes junto com a resposta. A "
                    "OpenAI explica na " + _A % (OPENAI_BOTS, "página oficial dos robôs dela") + " que o robô "
                    "<strong>OAI-SearchBot</strong> é o que leva os sites para os resultados de busca do ChatGPT, "
                    "e que o <strong>ChatGPT-User</strong> é usado quando uma pessoa pede para ele abrir uma página.",
                    "Na prática, ele tende a indicar empresas que aparecem em mais de um lugar confiável, com as "
                    "mesmas informações, e cujo site responde de forma direta o que a pessoa perguntou. Empresa "
                    "que só existe no Instagram, por exemplo, quase não é lida: boa parte do conteúdo das redes "
                    "sociais fica fechada para robôs.",
                ],
            }),
            ("tabela", {
                "tag": "Onde ele procura",
                "titulo": "O que o ChatGPT lê para indicar uma empresa?",
                "desc": "Estas são as fontes públicas que mais contam e o que conferir em cada uma.",
                "colunas": ["Fonte", "O que conferir"],
                "linhas": [
                    ["Seu site", "Diz o que você faz, para quem e em que cidade, logo no começo da página?"],
                    ["Perfil da Empresa no Google", "Está completo, com categoria certa, horário, fotos e avaliações?"],
                    ["Bing Places", "Existe? Muitas empresas nunca criaram, e o Bing é a base de busca da Microsoft."],
                    ["Diretórios e associações do ramo", "A empresa aparece, com o mesmo nome e telefone do site?"],
                    ["Avaliações", "São reais, recentes e respondidas?"],
                    ["Notícias, vídeos e blogs da cidade", "Alguém além de você fala da sua empresa?"],
                ],
                "nota": "Lista montada pela RCB SEO com base na documentação da OpenAI e na prática de SEO local.",
            }),
            ("cards", {
                "tag": "Passo a passo",
                "titulo": "Como aparecer no ChatGPT em 6 passos",
                "desc": "Faça na ordem. Os três primeiros você mesmo consegue fazer em uma tarde.",
                "itens": [
                    ("1. Pergunte ao ChatGPT como um cliente",
                     "Abra o ChatGPT e pergunte o que o seu cliente perguntaria: “qual [seu serviço] indicar em "
                     "[sua cidade]?”. Anote quem aparece e clique nas fontes. Isso mostra onde ele está procurando."),
                    ("2. Complete o Perfil no Google",
                     "Categoria certa, descrição clara, horário, fotos e avaliações respondidas. Veja o passo a "
                     "passo em <a href=\"/google-perfil-empresa/\">Google Meu Negócio</a>."),
                    ("3. Crie o perfil no Bing Places",
                     "O " + _A % (BING_PLACES, "Bing Places") + " é grátis e deixa importar os dados do perfil do "
                     "Google em poucos cliques."),
                    ("4. Libere os robôs no seu site",
                     "O arquivo robots.txt do site (a lista de quem pode entrar) não pode bloquear o OAI-SearchBot. "
                     "Quem fez o seu site confere isso em minutos."),
                    ("5. Escreva o que você faz, sem rodeio",
                     "Na página inicial e em cada página de serviço, a primeira frase precisa dizer o que é, para "
                     "quem e onde. É essa frase que a IA copia."),
                    ("6. Apareça fora do seu site",
                     "Associação do seu ramo, diretórios da cidade, um vídeo no YouTube explicando o serviço, uma "
                     "entrevista num portal local. Cada menção confiável é uma confirmação a mais."),
                ],
            }),
            ("split", {
                "tag": "Cuidado",
                "titulo": "O que não funciona para aparecer no ChatGPT",
                "ps": [
                    "Tem muita promessa circulando, e a maioria não se sustenta. Encher o site de texto repetindo "
                    "“melhor empresa de Goiânia” não convence a IA: ela cruza com outras fontes. Comprar avaliação "
                    "é proibido pelo Google e pode derrubar o seu perfil. E pagar alguém para “cadastrar no "
                    "ChatGPT” é pagar por algo que não existe.",
                    "O caminho que funciona é mais lento e mais seguro: informação verdadeira, completa e igual "
                    "em todo lugar. Se quiser ajuda para fazer isso direito, é exatamente o serviço de "
                    "<a href=\"/seo-para-ia/\">SEO para IA</a>.",
                ],
                "card_titulo": "Não caia nessa",
                "card": [
                    "“Cadastro no ChatGPT” pago.",
                    "Avaliações compradas.",
                    "Texto repetindo a mesma frase.",
                    "Páginas copiadas trocando o nome da cidade.",
                    "Garantia de ser indicado.",
                ],
            }),
            ("fontes", {"itens": [FONTES_BASE[0], FONTES_BASE[1],
                                  ("Google Search Central: políticas contra spam", GOOGLE_SPAM)]}),
        ],
        "faq": [
            ("Como colocar a minha empresa no ChatGPT?",
             "Não existe um jeito de colocar a empresa direto no ChatGPT. Ele indica o que encontra em fontes "
             "públicas, como o seu site, o Perfil no Google, o Bing e diretórios. O caminho é deixar essas fontes "
             "completas, com os mesmos dados, e liberar o robô dele no seu site."),
            ("O ChatGPT usa o Google Meu Negócio?",
             "A OpenAI não publica a lista completa de fontes que usa. O que se sabe é que o ChatGPT busca páginas "
             "na internet e mostra os links. Um Perfil no Google completo, com avaliações reais, costuma aparecer "
             "nessas buscas e reforça as outras fontes."),
            ("Preciso pagar o ChatGPT para a minha empresa aparecer?",
             "Não. O ChatGPT não vende espaço nas respostas como o Google vende anúncios. Aparecer depende do que "
             "está publicado sobre a sua empresa na internet. Você pode fazer os primeiros passos sozinho, de graça."),
            ("Quanto tempo depois dos ajustes a empresa aparece?",
             "Não há prazo certo. Depende de quando o ChatGPT volta a ler as fontes e de quanta concorrência existe "
             "no seu ramo e na sua cidade. Faça as mesmas perguntas uma vez por mês e anote o resultado para ver a "
             "evolução."),
            ("Como saber se o meu site bloqueia o ChatGPT?",
             "Abra o endereço do seu site seguido de /robots.txt, por exemplo seusite.com.br/robots.txt. Se aparecer "
             "OAI-SearchBot ou GPTBot com a palavra Disallow, existe bloqueio. Na dúvida, mande o print para quem "
             "cuida do site ou para mim."),
        ],
        "relacionados_titulo": "Leia também sobre SEO para IA",
        "relacionados": [_REL_PILAR, _REL_GOOGLE, _REL_AUDITORIA, _REL_PERFIL],
        "cta_final": ("Fez a pergunta ao ChatGPT e a sua empresa não apareceu?",
                      "Me mande o print da resposta no WhatsApp. Eu te digo de onde ele tirou os concorrentes e o "
                      "que falta para a sua empresa entrar nessa lista."),
    },

    # =====================================================================
    # AI OVERVIEWS E GEMINI (Google com IA)
    # =====================================================================
    {
        "slug": "ai-overviews-e-gemini",
        "tipo": "artigo",
        "data": DATA,
        "title": "AI Overviews e Gemini: Como sua Empresa Aparece | RCB SEO",
        "desc": ("AI Overviews é a resposta escrita por IA no topo do Google. Veja como sua empresa entra "
                 "nela e no Gemini, o que o Google recomenda e o que não adianta fazer."),
        "trilha": "AI Overviews e Gemini",
        "servico": "SEO para IA",
        "eyebrow": "Guia para donos de negócio",
        "h1": "AI Overviews e Gemini: como a sua empresa aparece na resposta de IA do Google",
        "sub": ("AI Overviews é o resumo escrito por inteligência artificial que o Google mostra acima dos links. "
                "Para a sua empresa aparecer nele, a página precisa estar no índice do Google e responder bem a "
                "pergunta. O Google diz que não existe otimização especial além do bom SEO."),
        "cta_hero": "Quero minha empresa na resposta do Google",
        "botao2": ("/seo-para-ia/#orcamento", "Ver como funciona o serviço"),
        "msg": "Olá, Renan! Quero que a minha empresa apareça nas respostas de IA do Google.",
        "pills": ["Atualizado em outubro de 2026", "Com fontes oficiais"],
        "painel_h2": "AI Overviews, resumido",
        "painel": [
            "É a resposta de IA no topo da busca do Google.",
            "Usa as páginas que já estão no Google.",
            "Mostra links para as fontes que usou.",
            "Não tem cadastro nem otimização secreta.",
            "Bloquear o Google-Extended não tira você dela.",
        ],
        "faq_titulo": "Perguntas frequentes sobre AI Overviews e Gemini",
        "secoes": [
            ("texto", {
                "tag": "O que é",
                "titulo": "O que é AI Overviews?",
                "ps": [
                    "AI Overviews, ou “Visão geral criada por IA”, é o texto que o Google escreve com "
                    "inteligência artificial e coloca no topo da busca, antes da lista de links. Ele resume a "
                    "resposta e mostra, ao lado, links para as páginas de onde tirou a informação.",
                    "Ser um desses links é o que interessa para a sua empresa. A pessoa lê o resumo, vê o nome "
                    "da sua página como fonte e clica. Em muitas perguntas, quem não está ali fica abaixo de um "
                    "bloco grande de texto e é visto bem menos.",
                ],
            }),
            ("tabela", {
                "tag": "Os nomes",
                "titulo": "Qual a diferença entre AI Overviews, Modo IA e Gemini?",
                "desc": "São três lugares onde a IA do Google responde. Os três dependem do mesmo índice do Google.",
                "colunas": ["Onde aparece", "Como funciona", "O que a sua empresa precisa"],
                "linhas": [
                    ["AI Overviews", "Resumo no topo da busca comum, com links das fontes", "Página guardada pelo Google e resposta clara"],
                    ["Modo IA (AI Mode)", "Aba de conversa dentro do Google, com perguntas em sequência", "O mesmo, mais páginas que cobrem as dúvidas seguintes"],
                    ["Gemini", "O assistente do Google, em app e no navegador", "Estar bem descrita nas fontes que o Google já conhece"],
                ],
                "nota": "Baseado na página oficial do Google sobre recursos de IA na busca.",
            }),
            ("texto", {
                "tag": "O que o Google diz",
                "titulo": "Como aparecer no AI Overviews do Google?",
                "ps": [
                    "Para aparecer no AI Overviews, a sua página precisa estar indexada (guardada pelo Google) e "
                    "poder aparecer com trecho na busca. Na " + _A % (GOOGLE_IA, "página oficial sobre recursos de IA") +
                    ", o Google afirma que não há requisito extra nem otimização especial: valem as mesmas "
                    "práticas de SEO de sempre.",
                    "Na prática, isso quer dizer: página que responde de verdade o que a pessoa pergunta, texto "
                    "escrito para gente e não para robô (o Google chama isso de "
                    + _A % (GOOGLE_UTIL, "conteúdo útil e confiável") + "), informação da empresa organizada "
                    "e um <a href=\"/google-perfil-empresa/\">Perfil da Empresa</a> completo para as buscas locais. "
                    "Se o seu site ainda não aparece no Google, comece por "
                    "<a href=\"/como-aparecer-no-google/\">como aparecer no Google</a>.",
                ],
            }),
            ("split", {
                "tag": "Um engano comum",
                "titulo": "Bloquear o Google-Extended tira o site do AI Overviews?",
                "ps": [
                    "Não. Segundo a " + _A % (GOOGLE_CRAWLERS, "documentação dos robôs do Google") + ", o "
                    "Google-Extended não muda a presença do site na busca do Google, e o AI Overviews faz parte "
                    "da busca. Quem quer sair do AI Overviews precisa de outras marcações, como a que impede o "
                    "Google de mostrar trecho da página, e isso tira a página também dos trechos da busca comum.",
                    "Mas o Google-Extended pesa em outro lugar: ele decide se o conteúdo do seu site pode ser usado "
                    "para treinar os modelos Gemini <strong>e para embasar as respostas do app Gemini</strong>. "
                    "Bloquear o Google-Extended, então, pode tirar o seu site das respostas do Gemini. Para uma "
                    "empresa que quer ser encontrada, a recomendação é deixar tudo liberado. É o que este site faz.",
                ],
                "card_titulo": "Resumo",
                "card": [
                    "Googlebot: busca e AI Overviews.",
                    "Google-Extended: treino do Gemini e respostas do app Gemini.",
                    "Para aparecer nos dois: deixe os dois liberados.",
                ],
            }),
            ("cards", {
                "tag": "O que fazer",
                "titulo": "O que deixa a sua página pronta para a resposta de IA do Google",
                "itens": [
                    ("Resposta na primeira frase",
                     "Cada página abre respondendo a pergunta do título em uma ou duas frases. O resumo da IA "
                     "costuma usar exatamente esse tipo de trecho."),
                    ("Uma pergunta por página",
                     "Página que tenta falar de tudo não responde nada direito. Separe os serviços e as dúvidas "
                     "principais em páginas próprias."),
                    ("Tabelas e listas",
                     "Comparação vira tabela, passo a passo vira lista numerada. É o formato mais fácil de ler, "
                     "para gente e para máquina."),
                    ("Dados estruturados verdadeiros",
                     "Marcação que conta ao Google o nome, o endereço e os serviços da empresa, sempre igual ao "
                     "que está escrito na página. Dá para conferir no "
                     "<a href=\"/ferramentas/\">teste de pesquisa aprimorada</a>."),
                    ("Autor e data",
                     "Quem escreveu, qual a experiência e quando foi atualizado. Ajuda o Google a confiar no texto."),
                    ("Perfil da Empresa completo",
                     "Para perguntas com cidade ou bairro, o perfil no Google é uma das fontes principais."),
                ],
            }),
            ("texto", {
                "tag": "Como medir",
                "titulo": "Como saber se a sua empresa aparece no AI Overviews?",
                "ps": [
                    "O Google informa que os cliques e as impressões vindos das respostas de IA entram no "
                    "relatório de desempenho do Search Console, somados à busca comum. Não existe, até a data "
                    "desta página, um filtro separado só para AI Overviews. Por isso vale também pesquisar no "
                    "Google, uma vez por mês, as perguntas do seu cliente e anotar se a sua página aparece como fonte.",
                ],
            }),
            ("fontes", {"itens": [
                ("Google Search Central: recursos de IA e o seu site", GOOGLE_IA),
                ("Google Search Central: robôs do Google (inclui Google-Extended)", GOOGLE_CRAWLERS),
                ("Google Search Central: como criar conteúdo útil e confiável", GOOGLE_UTIL),
            ]}),
        ],
        "faq": [
            ("Como aparecer no Gemini?",
             "Para uma empresa, aparecer no Gemini é estar bem descrita nas fontes que o Google já conhece: site "
             "indexado, Perfil da Empresa completo, avaliações reais e menções em outros sites. Não existe cadastro "
             "no Gemini. O trabalho é o mesmo das respostas de IA da busca do Google."),
            ("Preciso pagar o Google para aparecer no AI Overviews?",
             "Não. As fontes do AI Overviews não são pagas. Anúncios do Google Ads podem aparecer perto do resumo, "
             "mas em espaço separado e marcado como patrocinado. Aparecer como fonte depende da qualidade e da "
             "relevância da página."),
            ("O AI Overviews diminui as visitas do meu site?",
             "Em algumas perguntas simples, a pessoa lê o resumo e não clica. Em compensação, quem é citado como "
             "fonte ganha destaque no topo. Para empresa local, a decisão de contratar quase sempre leva a pessoa a "
             "clicar, ligar ou chamar no WhatsApp."),
            ("Meu site precisa de algo técnico para o AI Overviews?",
             "Precisa do básico bem feito: estar indexado, abrir rápido, ter o texto no próprio HTML e não bloquear "
             "o Googlebot. O Google afirma que não há marcação especial obrigatória para aparecer nas respostas de IA."),
        ],
        "relacionados_titulo": "Leia também sobre SEO para IA",
        "relacionados": [_REL_PILAR, _REL_CHATGPT, _REL_GEO, ("/como-aparecer-no-google/", "Como aparecer no Google",
                         "O passo a passo para a empresa aparecer na busca comum e no Maps.")],
        "cta_final": ("Quer saber se a sua empresa aparece na resposta do Google?",
                      "Me diga o seu serviço e a sua cidade no WhatsApp. Eu pesquiso as perguntas do seu cliente e "
                      "te mostro quem o Google está citando."),
    },

    # =====================================================================
    # O QUE É GEO E AEO
    # =====================================================================
    {
        "slug": "o-que-e-geo-e-aeo",
        "tipo": "artigo",
        "data": DATA,
        "title": "O que é GEO e AEO? SEO para IA Explicado | RCB SEO",
        "desc": ("GEO e AEO são nomes do SEO feito para respostas de IA, como ChatGPT e Gemini. Entenda a "
                 "diferença para o SEO comum, de onde vieram e o que muda."),
        "trilha": "O que é GEO e AEO",
        "servico": "SEO para IA",
        "eyebrow": "Explicado sem complicação",
        "h1": "O que é GEO e AEO? O SEO para IA explicado para o dono de negócio",
        "sub": ("GEO e AEO são dois nomes para o mesmo esforço: fazer a sua empresa aparecer nas respostas "
                "escritas por inteligência artificial, como as do ChatGPT e do Gemini. Em português, o mais "
                "comum é chamar de SEO para IA."),
        "cta_hero": "Quero entender o meu caso",
        "botao2": ("/seo-para-ia/", "Ver o serviço de SEO para IA"),
        "msg": "Olá, Renan! Li sobre GEO e AEO e quero entender o que faz sentido para a minha empresa.",
        "pills": ["Atualizado em outubro de 2026", "Com fontes oficiais"],
        "painel_h2": "GEO e AEO em uma frase",
        "painel": [
            "SEO: aparecer na lista de links.",
            "AEO: virar a resposta direta.",
            "GEO: ser citado pela IA que escreve a resposta.",
            "Na prática, os três andam juntos.",
        ],
        "faq_titulo": "Perguntas frequentes sobre GEO e AEO",
        "secoes": [
            ("texto", {
                "tag": "GEO",
                "titulo": "O que é GEO?",
                "ps": [
                    "GEO é a sigla em inglês para Generative Engine Optimization, ou “otimização para mecanismos "
                    "generativos”. Mecanismo generativo é a IA que escreve (gera) a resposta, como o ChatGPT, o "
                    "Gemini e o Perplexity. Fazer GEO é preparar o seu conteúdo e a sua empresa para serem "
                    "usados e citados nessas respostas.",
                    "O nome ficou conhecido com uma " + _A % (PAPER_GEO, "pesquisa acadêmica de 2023") + ", que "
                    "testou o que faz um texto ser mais citado por esse tipo de IA. No teste dos autores, "
                    "acrescentar fontes, citações e números verificáveis ao texto ajudou mais do que repetir "
                    "palavras-chave. É uma pista útil, não uma regra garantida para todo caso.",
                ],
            }),
            ("texto", {
                "tag": "AEO",
                "titulo": "O que é AEO?",
                "ps": [
                    "AEO é a sigla para Answer Engine Optimization, ou “otimização para mecanismos de resposta”. "
                    "O termo é mais antigo que o GEO e nasceu com as respostas diretas da busca e dos assistentes "
                    "de voz: aquele quadro que responde a pergunta antes dos links, ou a Alexa lendo uma resposta "
                    "em voz alta. Fazer AEO é escrever para virar essa resposta.",
                ],
            }),
            ("tabela", {
                "tag": "Lado a lado",
                "titulo": "Qual a diferença entre SEO, AEO e GEO?",
                "desc": "Os três se apoiam no mesmo trabalho de base. Muda o lugar onde a empresa quer aparecer.",
                "colunas": ["", "SEO", "AEO", "GEO"],
                "linhas": [
                    ["Onde aparece", "Lista de links e mapa", "Resposta direta, quadro de destaque, voz", "Texto escrito pela IA"],
                    ["Exemplo", "Busca no Google", "Resposta no topo, assistente de voz", "ChatGPT, Gemini, Perplexity, AI Overviews"],
                    ["O que conta", "Página, perfil, links", "Resposta curta e clara", "Fontes confiáveis e dados coerentes"],
                    ["Existe há", "Décadas", "Alguns anos", "Desde 2023, mais ou menos"],
                ],
                "nota": "Quadro da RCB SEO. Os limites entre os três não são oficiais e o mercado usa os nomes de formas diferentes.",
            }),
            ("texto", {
                "tag": "Para a sua empresa",
                "titulo": "GEO e AEO são para a minha empresa?",
                "ps": [
                    "Se o seu cliente pergunta ao ChatGPT ou ao Google “quem indica para…” antes de contratar, "
                    "então sim. E a boa notícia é que você não precisa de três serviços diferentes: o trabalho "
                    "de base é o mesmo. Site claro, Perfil no Google completo, dados iguais em todo lugar, "
                    "respostas diretas e menções fora do site servem para o SEO, para o AEO e para o GEO.",
                    "Cuidado com quem vende GEO como algo mágico e separado de tudo. Sem a base do SEO, quase "
                    "nada acontece. Por isso eu ofereço os dois juntos, com o nome que o dono de negócio entende: "
                    "<a href=\"/seo-para-ia/\">SEO para IA</a>.",
                ],
            }),
            ("texto", {
                "tag": "Os robôs",
                "titulo": "Que robôs as IAs usam para ler o seu site?",
                "ps": [
                    "Cada empresa de IA tem robôs com nomes próprios, e cada uma documenta os seus. A OpenAI usa o "
                    "OAI-SearchBot, o GPTBot e o ChatGPT-User (" + _A % (OPENAI_BOTS, "documentação da OpenAI") + "). "
                    "A Anthropic, dona do Claude, usa o ClaudeBot e outros (" + _A % (ANTHROPIC_BOTS, "documentação da Anthropic") + "). "
                    "O Perplexity usa o PerplexityBot (" + _A % (PERPLEXITY_BOTS, "documentação do Perplexity") + "). "
                    "O Google usa o Googlebot para a busca e para o AI Overviews.",
                    "Todos respeitam o arquivo robots.txt do site, a lista que diz quem pode entrar. Para ser "
                    "citado, o site precisa deixar esses robôs passarem.",
                ],
            }),
            ("fontes", {"itens": [
                ("Pesquisa “GEO: Generative Engine Optimization” (Aggarwal e outros, 2023)", PAPER_GEO),
            ] + FONTES_BASE}),
        ],
        "faq": [
            ("Qual é o nome do SEO para IA?",
             "Os nomes mais usados são GEO, de Generative Engine Optimization, e AEO, de Answer Engine Optimization. "
             "Também aparecem AI SEO, LLMO e SEO para IA. Todos falam do mesmo esforço: fazer a empresa aparecer nas "
             "respostas escritas por inteligência artificial."),
            ("GEO substitui o SEO?",
             "Não. O GEO depende do SEO. As respostas de IA do Google usam o índice do Google, e o ChatGPT busca "
             "páginas na internet. Empresa invisível na busca comum dificilmente vira fonte da IA. O GEO é uma "
             "camada a mais sobre a mesma base."),
            ("Dá para fazer GEO sozinho?",
             "Dá para começar. Completar o Perfil no Google, criar o perfil no Bing Places e escrever no site, sem "
             "rodeio, o que a empresa faz e onde atende são passos que o dono consegue fazer. A parte técnica e a "
             "medição mensal costumam pedir ajuda."),
            ("O que é LLM?",
             "LLM é a sigla em inglês para modelo de linguagem grande, o tipo de inteligência artificial que está "
             "por trás do ChatGPT, do Gemini e do Claude. Otimização para LLM é mais um nome para o mesmo trabalho "
             "de GEO e SEO para IA."),
        ],
        "relacionados_titulo": "Leia também sobre SEO para IA",
        "relacionados": [_REL_PILAR, _REL_CHATGPT, _REL_GOOGLE, _REL_AUDITORIA],
        "cta_final": ("Quer saber o que GEO significa na prática para o seu negócio?",
                      "Me conte o que você faz e onde atende. Eu te explico, sem sigla, o que vale a pena fazer primeiro."),
    },

    # =====================================================================
    # AUDITORIA
    # =====================================================================
    {
        "slug": "auditoria-de-seo-para-ia",
        "tipo": "servico",
        "nacional": False,
        "data": DATA,
        "publico": "Donos de negócio que querem saber o que o ChatGPT e o Gemini dizem sobre o seu ramo",
        "title": "Auditoria de SEO para IA: Sua Empresa no ChatGPT | RCB SEO",
        "desc": ("Auditoria de SEO para IA: descubra se o ChatGPT, o Gemini e o Google com IA indicam sua "
                 "empresa, quem aparece no lugar dela e o que arrumar primeiro."),
        "trilha": "Auditoria de SEO para IA",
        "servico": "Auditoria de SEO para IA",
        "eyebrow": "Online no Brasil · Presencial em Goiânia",
        "h1": "Auditoria de SEO para IA: o que o ChatGPT e o Gemini dizem hoje sobre o seu ramo",
        "sub": ("A auditoria de SEO para IA mostra se as IAs indicam a sua empresa, quem elas indicam no lugar "
                "dela e de onde tiram essa informação. Você recebe a lista do que arrumar primeiro, na ordem "
                "de impacto."),
        "cta_hero": "Quero a auditoria da minha empresa",
        "botao2": ("#orcamento", "Ver o que está incluído"),
        "msg": "Olá, Renan! Quero a auditoria de SEO para IA da minha empresa.",
        "pills": ["Orçamento em até 24h", "Prazo por escrito", "Relatório em português simples"],
        "painel_h2": "O que você descobre",
        "painel": [
            "Se o ChatGPT, o Gemini, o Perplexity e o Copilot citam a sua empresa.",
            "Quais concorrentes eles citam no seu lugar.",
            "De quais sites a IA tirou a resposta.",
            "O que, no seu site e nos seus perfis, está atrapalhando.",
        ],
        "faq_titulo": "Perguntas frequentes sobre a auditoria de SEO para IA",
        "secoes": [
            ("cards", {
                "tag": "Escopo",
                "titulo": "O que a auditoria de SEO para IA analisa?",
                "desc": "Quatro partes, sempre nesta ordem.",
                "itens": [
                    ("1. As perguntas do seu cliente",
                     "Monto com você as perguntas que o seu cliente faz antes de contratar e faço cada uma ao "
                     "ChatGPT, ao Gemini, ao Perplexity, ao Copilot e à busca do Google. Tudo anotado, com print."),
                    ("2. Quem aparece e por quê",
                     "Para cada resposta: se a sua empresa aparece, quais concorrentes aparecem e quais sites a "
                     "IA usou como fonte. É aqui que se descobre onde vale a pena estar."),
                    ("3. A parte técnica do site",
                     "Robôs das IAs liberados, texto visível sem depender de programação, dados estruturados "
                     "corretos e páginas que respondem as perguntas do item 1."),
                    ("4. A sua empresa fora do site",
                     "Perfil no Google, Bing Places, redes e diretórios: se existem, se estão completos e se o "
                     "nome, o telefone e o endereço batem em todos."),
                ],
            }),
            ("tabela", {
                "tag": "Entregáveis",
                "titulo": "O que você recebe na auditoria",
                "colunas": ["Entregável", "Para que serve"],
                "linhas": [
                    ["Planilha das perguntas", "Cada pergunta, cada IA, se a empresa apareceu, quem apareceu e a data. Vira a sua linha de base."],
                    ["Mapa das fontes", "Os sites que as IAs usaram no seu ramo e na sua cidade, para você saber onde precisa estar."],
                    ["Lista de correções", "O que arrumar no site e nos perfis, em ordem de impacto, em português simples."],
                    ["Conversa de entrega", "Uma chamada para explicar o resultado e tirar as suas dúvidas."],
                ],
            }),
            ("split", {
                "tag": "Limites",
                "titulo": "O que não está incluído na auditoria",
                "ps": [
                    "A auditoria é o diagnóstico. Ela mostra onde a sua empresa está e o que fazer, mas não faz "
                    "as correções. Se você quiser que eu faça, isso vira um orçamento à parte, e o trabalho da "
                    "auditoria não se perde: ela é o primeiro passo das correções.",
                    "Também não existe, aqui nem em lugar nenhum, promessa de que a IA vai passar a citar a sua "
                    "empresa. A auditoria te dá clareza para decidir, com dados, e não com achismo.",
                ],
                "card_titulo": "Fica de fora",
                "card": [
                    "Fazer as correções (orçamento à parte).",
                    "Escrever páginas novas.",
                    "Anúncio pago.",
                    "Gestão de redes sociais.",
                    "Promessa de ser citado pela IA.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona a auditoria, do pedido à entrega",
                "itens": [
                    ("Você me conta o seu negócio",
                     "Pelo WhatsApp: o que você faz, onde atende e quem são os concorrentes que você conhece."),
                    ("Orçamento e prazo por escrito",
                     "Em até 24 horas você recebe o que entra na auditoria, o prazo e o valor."),
                    ("Perguntas e análise",
                     "Faço as perguntas nas IAs, analiso as fontes, o site e os perfis."),
                    ("Entrega e conversa",
                     "Você recebe a planilha, o mapa das fontes e a lista de correções, e a gente conversa sobre o resultado."),
                ],
            }),
            ("orcamento", {
                "titulo": "Quer começar pela auditoria ou já ir para o trabalho completo?",
                "desc": "O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": -1,
                "itens": [
                    ("Só a auditoria", "Para saber onde a sua empresa está antes de decidir.",
                     ["Perguntas nas 4 IAs e no Google", "Mapa das fontes", "Lista de correções"],
                     "Olá, Renan! Quero só a auditoria de SEO para IA.", "Pedir orçamento"),
                    ("Auditoria + correções", "Para quem já quer resolver.",
                     ["A auditoria completa", "Correções no site e nos perfis", "Novo teste depois dos ajustes"],
                     "Olá, Renan! Quero a auditoria de SEO para IA e as correções.", "Pedir orçamento"),
                ],
            }),
            ("fontes", {"itens": FONTES_BASE}),
        ],
        "faq": [
            ("Quanto tempo leva a auditoria de SEO para IA?",
             "O prazo vai por escrito no orçamento e depende de quantas perguntas e quantos concorrentes entram na "
             "análise. A entrega inclui a planilha das perguntas, o mapa das fontes, a lista de correções e uma "
             "conversa para explicar o resultado."),
            ("A auditoria serve para empresa que ainda não tem site?",
             "Serve. Nesse caso a auditoria mostra quais fontes as IAs usam no seu ramo e o que precisa existir "
             "para a sua empresa entrar nelas: Perfil no Google, Bing Places, diretórios e, quando fizer sentido, "
             "um site ou uma página simples."),
            ("Eu mesmo não consigo perguntar ao ChatGPT?",
             "Consegue, e eu recomendo que faça. A auditoria vai além: repete as perguntas em várias IAs, registra "
             "as fontes de cada resposta, cruza com o seu site e os seus perfis e transforma isso numa lista de "
             "correções em ordem de impacto."),
            ("Quanto custa a auditoria?",
             "Depende de quantas perguntas, quantas cidades e quantos concorrentes entram. O orçamento é individual, "
             "grátis e chega pelo WhatsApp em até 24 horas, com o prazo por escrito."),
        ],
        "relacionados_titulo": "Leia também sobre SEO para IA",
        "relacionados": [_REL_PILAR, _REL_CHATGPT, _REL_GOOGLE, _REL_SERVICOS],
        "cta_final": ("Quer saber, com dados, o que a IA diz sobre o seu ramo?",
                      "Me conte o que você faz e onde atende. Em até 24 horas você recebe o orçamento da auditoria, "
                      "com o prazo por escrito."),
    },
]
