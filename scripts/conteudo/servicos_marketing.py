# -*- coding: utf-8 -*-
"""
Conteúdo das páginas de serviço da linha "Sites e Anúncios" (28/09/2026).

  /criacao-de-landing-page/   (nacional desde 04/10/2026; 301 da antiga de Goiania)
  /gestao-de-trafego-pago-goiania/   (Google Ads + Meta Ads)
  /criacao-de-loja-virtual-goiania/

Regras do Renan para estas páginas:
  * SEM PREÇO da RCB. Faixas de mercado são permitidas; o valor sai sob medida no WhatsApp.
  * Copy persuasiva, sempre levando ao WhatsApp com mensagem específica por serviço.
  * Nenhum resultado prometido, nenhuma certificação inventada, nenhum desconto/prazo falso.
  * Social media NÃO é oferecido.

O texto é escrito à mão aqui; o gerador (scripts/gerar-servicos-marketing.py) só monta o invólucro.
Cada seção é uma tupla (tipo, dados) — os tipos estão documentados no gerador.
"""

PAGINAS = [
    # =====================================================================
    # LANDING PAGE
    # =====================================================================
    {
        # Etapa 2 do plano de nichos (04/10/2026): virou pagina NACIONAL, com 301 de
        # /criacao-de-landing-page/ (1 impressao em 28 dias, posicao 104).
        # Regra de honestidade: sem portfolio, cliente ou numero inventado; o exemplo
        # e o modelo demonstrativo de empresa ficticia (/modelos/landing-page-energia-solar/).
        "slug": "criacao-de-landing-page",
        "nacional": True,
        "data": "2026-10-04",
        "publico": "Empresas e profissionais que anunciam ou querem anunciar no Google Ads",
        "title": "Criação de Landing Page para Anúncios (Google Ads) | RCB SEO",
        "desc": ("Criação de landing page para anúncios no Google Ads: rápida no celular, com WhatsApp, "
                 "formulário com LGPD e medição de conversão. Orçamento grátis em 24h."),
        "trilha": "Criação de landing page",
        "servico": "Criação de landing page",
        "eyebrow": "Para empresas de todo o Brasil",
        "h1": "Criação de landing page para anúncios no Google",
        "sub": ("Landing page é uma página única, feita para receber quem clicou no seu anúncio e transformar "
                "esse clique em contato. Eu crio a sua do zero: rápida no celular, com uma oferta só, botão de "
                "WhatsApp, formulário com aviso de LGPD e medição de cada conversão no Google Ads e no GA4. "
                "O orçamento é grátis e sai em até 24 horas pelo WhatsApp."),
        "cta_hero": "Quero orçamento da minha landing page",
        "msg": "Olá, Renan! Quero um orçamento de landing page para anúncio.",
        "pills": ["Orçamento em até 24h", "Feita para Google Ads", "Prazo por escrito"],
        "painel_h2": "O que está incluído",
        "painel": [
            "Página rápida no celular, testada antes da entrega.",
            "Botão de WhatsApp com mensagem pronta.",
            "Formulário com aviso de LGPD.",
            "Medição de conversão no Google Ads e no GA4.",
            "Pixel da Meta, quando você também anuncia lá.",
            "Domínio e hospedagem orientados por mim.",
        ],
        "faq_titulo": "Perguntas frequentes sobre criação de landing page",
        "secoes": [
            ("texto", {
                "tag": "Em palavras simples",
                "titulo": "O que é uma landing page e por que ela não é um site?",
                "ps": [
                    "Um site é como uma loja inteira: tem várias portas, vários corredores e serve para quem "
                    "quer conhecer a empresa com calma. A landing page (em português, “página de destino”) é "
                    "um balcão só, montado para uma pessoa que já chegou interessada numa oferta específica.",
                    "Ela tem um assunto, uma promessa e um convite: falar com você. Não tem menu levando para "
                    "o blog, nem cinco serviços competindo pela atenção. Quem clicou no anúncio de “instalação "
                    "de energia solar” cai numa página que fala só disso — e encontra o botão do WhatsApp sem "
                    "precisar procurar.",
                    "Por isso ela é a peça que fica entre o anúncio e a conversa. O anúncio traz a pessoa; a "
                    "landing page decide se essa visita vira contato ou volta para o Google.",
                ],
            }),
            ("split", {
                "tag": "O desperdício",
                "titulo": "Por que anunciar sem landing page queima dinheiro?",
                "ps": [
                    "No Google Ads, na forma mais comum de anunciar, "
                    "<a href=\"https://support.google.com/google-ads/answer/116495?hl=pt-BR\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">você paga a cada clique no anúncio</a>, segundo a própria ajuda "
                    "do Google. O clique é cobrado mesmo que a pessoa desista três segundos depois, porque a "
                    "página demorou a abrir ou não respondia o que ela procurava.",
                    "Tem um segundo custo, menos visível. O Google dá a cada palavra-chave um "
                    "<a href=\"https://support.google.com/google-ads/answer/6167118?hl=pt-BR\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">Índice de qualidade</a>, que compara o seu anúncio e a sua página "
                    "de destino com os de outros anunciantes. Página fraca puxa esse índice para baixo.",
                    "Mandar o anúncio para a página inicial do site, para o Instagram ou para um link de "
                    "WhatsApp solto costuma ser o caminho mais caro: a pessoa chega sem direção e sai sem falar "
                    "com ninguém.",
                ],
                "card_titulo": "Onde o clique costuma se perder",
                "card": [
                    "Página que demora a abrir no celular.",
                    "Texto genérico, que serve para qualquer empresa.",
                    "Vários caminhos e nenhum convite claro.",
                    "Formulário longo pedindo dado demais.",
                    "Sem medição: ninguém sabe qual anúncio trouxe o cliente.",
                ],
            }),
            ("cards", {
                "tag": "O que vem na página",
                "titulo": "O que está incluído na sua landing page?",
                "desc": "Tudo o que a página precisa para receber o clique do anúncio e devolver um contato.",
                "itens": [
                    ("Página rápida no celular",
                     "Quase todo clique de anúncio vem do celular. Antes de entregar, eu meço a velocidade com o "
                     "<a href=\"https://pagespeed.web.dev/\" target=\"_blank\" rel=\"noopener noreferrer\">PageSpeed "
                     "Insights</a>, a ferramenta gratuita do Google, e corrijo o que estiver pesando."),
                    ("Botão de WhatsApp com mensagem pronta",
                     "A pessoa toca no botão e a conversa já abre com um texto inicial, dizendo de qual anúncio "
                     "ela veio. Você responde sabendo o que ela quer."),
                    ("Formulário com aviso de LGPD",
                     "Para quem prefere deixar o contato. O formulário pede só o necessário e avisa como os dados "
                     "serão usados, como pede a "
                     "<a href=\"https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm\" "
                     "target=\"_blank\" rel=\"noopener noreferrer\">Lei Geral de Proteção de Dados (Lei 13.709/2018)</a>."),
                    ("Medição de conversão no Google Ads e no GA4",
                     "Cada toque no WhatsApp e cada formulário enviado é registrado como conversão — o "
                     "<a href=\"https://support.google.com/google-ads/answer/1722022?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">recurso de medição do próprio Google Ads</a>. Assim dá para saber "
                     "qual anúncio e qual palavra trazem cliente."),
                    ("Pixel da Meta, quando houver",
                     "Se você também anuncia no Instagram ou no Facebook, a página recebe o pixel da Meta para "
                     "medir esses contatos do mesmo jeito."),
                    ("Domínio e hospedagem orientados",
                     "Eu explico o que contratar, em nome de quem fica e como apontar o endereço. A página e o "
                     "domínio ficam no seu nome, não no meu."),
                ],
            }),
            ("texto", {
                "tag": "Prazo",
                "titulo": "Quanto tempo leva para a landing page ficar pronta?",
                "ps": [
                    "A primeira versão da sua landing page fica pronta em até 5 dias úteis depois que eu recebo "
                    "as informações da empresa: os textos (ou as informações para eu escrever), as fotos e o logo. "
                    "O prazo também vai por escrito junto com o orçamento.",
                    "Os 5 dias úteis começam a contar quando tudo chega completo. O que mais atrasa costuma ser a "
                    "espera por fotos, dados e aprovações — por isso eu aviso logo no começo exatamente o que vou "
                    "precisar. Depois da primeira versão, você revisa e eu faço os ajustes antes de a página ir ao ar.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona, do primeiro contato até a página no ar?",
                "itens": [
                    ("Você me conta a oferta",
                     "Pelo WhatsApp: o que você vende, para quem, em que região e se já anuncia ou vai começar."),
                    ("Orçamento e prazo por escrito",
                     "Em até 24 horas você recebe o que entra na página, o prazo e o valor do seu projeto."),
                    ("Texto e montagem",
                     "Com textos, fotos e logo em mãos, a primeira versão fica pronta em até 5 dias úteis para você aprovar."),
                    ("Medição e testes",
                     "Configuro as conversões no Google Ads e no GA4 e testo velocidade, botão e formulário."),
                    ("Página no ar, ligada ao anúncio",
                     "A página entra no ar no seu domínio, pronta para receber o tráfego da campanha."),
                ],
            }),
            ("texto", {
                "tag": "Orçamento",
                "titulo": "Quanto custa uma landing page?",
                "ps": [
                    "Não existe preço de tabela, porque duas landing pages podem ter trabalhos bem diferentes. "
                    "O que define o orçamento é: quantas seções a página precisa ter para explicar a oferta; "
                    "quem escreve o texto; se há fotos prontas ou se é preciso organizar imagens; quantas "
                    "integrações entram (WhatsApp, formulário, planilha ou sistema da empresa); e quanto de "
                    "medição precisa ser configurado.",
                    "Também conta o que acontece depois: se você vai cuidar do anúncio ou se quer que eu cuide "
                    "da campanha no Google Ads junto com a página. O orçamento é individual, grátis e chega "
                    "pelo WhatsApp em até 24 horas.",
                ],
            }),
            ("orcamento", {
                "titulo": "Qual landing page faz sentido para o seu anúncio?",
                "desc": "Escolha o ponto de partida mais parecido com o seu momento. O orçamento é grátis.",
                "destaque": 1,
                "itens": [
                    ("Landing page de captação", "Para quem quer receber contatos pelo WhatsApp e formulário.",
                     ["Uma oferta, texto e montagem", "Botão de WhatsApp e formulário com LGPD",
                      "Teste de velocidade no celular"],
                     "Olá, Renan! Quero orçamento de uma landing page de captação.", "Pedir orçamento"),
                    ("Landing page com medição completa", "Para quem já anuncia e não sabe o que traz cliente.",
                     ["Tudo da landing page de captação", "Conversões no Google Ads e no GA4",
                      "Pixel da Meta, se você anuncia lá"],
                     "Olá, Renan! Já anuncio e quero uma landing page com medição completa.", "Pedir orçamento"),
                    ("Landing page + Google Ads", "Para quem vai começar a anunciar e quer tudo em um lugar só.",
                     ["Landing page com medição completa", "Campanha na pesquisa do Google",
                      "Acompanhamento do que gera contato"],
                     "Olá, Renan! Quero landing page e gestão de Google Ads.", "Pedir orçamento"),
                ],
            }),
            ("chamada", {
                "tag": "Exemplo",
                "titulo": "Quer ver como fica uma landing page pronta?",
                "ps": [
                    "Montei um modelo demonstrativo para uma empresa fictícia de energia solar. Não é cliente "
                    "real: serve para você ver a estrutura, o ritmo do texto e como o botão de WhatsApp aparece "
                    "no celular.",
                ],
                "link": "/modelos/landing-page-energia-solar/",
                "botao": "Ver o modelo demonstrativo",
            }),
            ("texto", {
                "tag": "Landing page ou site",
                "titulo": "Quando faz mais sentido uma landing page do que um site completo?",
                "ps": [
                    "A landing page é a melhor escolha quando você vai anunciar uma oferta específica e quer "
                    "contato rápido: um serviço principal, uma promoção, um lançamento, uma campanha de "
                    "temporada. Ela é focada justamente para não dispersar quem chega pelo anúncio.",
                    "O site completo faz mais sentido quando a empresa quer ser encontrada no Google sem pagar "
                    "por clique, ao longo do tempo, por vários serviços. Muita empresa usa os dois: o site para "
                    "aparecer na busca de graça e a landing page para receber o tráfego pago. Se for o seu caso, "
                    "veja também a <a href=\"/criacao-de-sites-goiania/\">criação de sites</a>.",
                ],
            }),
        ],
        "faq": [
            ("Em quanto tempo a landing page fica pronta?",
             "A primeira versão fica pronta em até 5 dias úteis depois que eu recebo as informações da empresa: "
             "textos, fotos e logo. Depois você revisa e eu ajusto antes de a página ir ao ar."),
            ("Landing page funciona sem anúncio?",
             "Funciona, mas foi feita para receber tráfego que você leva até ela: anúncio, link no WhatsApp, "
             "QR code, e-mail. Sozinha, sem ninguém mandando gente para lá, ela recebe pouca visita, porque não "
             "tem o conteúdo amplo que o Google costuma mostrar na busca gratuita."),
            ("Preciso ter site se eu tiver uma landing page?",
             "Não é obrigatório para anunciar. Mas, se você quer também aparecer no Google sem pagar por clique, "
             "o site com conteúdo é o caminho. Muitas empresas usam a landing page para o anúncio e o site para "
             "a busca gratuita."),
            ("Você também cria e cuida do anúncio no Google Ads?",
             "Sim. Posso entregar só a página ou a página junto com a campanha na pesquisa do Google, com "
             "acompanhamento do que gera contato. O orçamento sai separado para você escolher."),
            ("Posso usar a mesma landing page no Instagram e no Facebook?",
             "Pode. Quando você também anuncia na Meta, eu instalo o pixel da Meta na página para medir esses "
             "contatos. A página continua a mesma; muda só a origem do clique."),
            ("O que é medição de conversão?",
             "É o registro automático de cada contato que veio do anúncio: o toque no botão do WhatsApp ou o "
             "envio do formulário. Com isso dá para ver qual anúncio e qual palavra pesquisada trazem cliente, "
             "e cortar o que só gasta."),
            ("Quanto custa uma landing page?",
             "Depende do número de seções, de quem escreve o texto, das fotos, das integrações e da medição que "
             "precisa ser configurada. O orçamento é individual, grátis e chega pelo WhatsApp em até 24 horas."),
            ("Você tem exemplos de landing page?",
             "Tenho um modelo demonstrativo, feito para uma empresa fictícia de energia solar, para você ver "
             "como a página fica no celular. Ele está marcado como modelo: não é um cliente real."),
            ("A página e o domínio ficam no meu nome?",
             "Sim. Eu oriento a contratação do domínio e da hospedagem em nome da sua empresa. Se um dia você "
             "quiser seguir com outra pessoa, a página continua sendo sua."),
        ],
        "relacionados": [
            ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago",
             "Anúncio na pesquisa do Google para levar gente até a sua landing page."),
            ("/criacao-de-sites-goiania/", "Criação de sites",
             "Quando a empresa quer aparecer no Google de graça, por vários serviços."),
            ("/blog/quanto-investir-em-trafego-pago/", "Quanto investir em tráfego pago?",
             "Como calcular a verba do anúncio a partir do valor do seu cliente."),
        ],
        "cta_final": ("Me conte a sua oferta. Eu te digo como transformar clique em conversa.",
                      "Sem compromisso: você me diz o que vende e onde vai anunciar, e eu te mostro o caminho mais "
                      "curto até o seu WhatsApp."),
    },

    # =====================================================================
    # TRÁFEGO PAGO (Google Ads + Meta Ads)
    # =====================================================================
    {
        "slug": "gestao-de-trafego-pago-goiania",
        "title": "Gestão de Tráfego Pago em Goiânia | Google Ads e Meta Ads",
        "desc": ("Gestão de tráfego pago em Goiânia: Google Ads e Meta Ads para a sua empresa ser encontrada hoje "
                 "por quem procura o que você vende. Orçamento grátis em 24h."),
        "trilha": "Gestão de tráfego pago em Goiânia",
        "servico": "Gestão de tráfego pago",
        "eyebrow": "Google Ads e Meta Ads",
        "h1": "Gestão de tráfego pago em Goiânia",
        "sub": ("Aparecer no Google de graça leva meses. O anúncio coloca a sua empresa na frente do cliente hoje. "
                "Eu monto e acompanho as suas campanhas no Google Ads e no Meta Ads para cada real de anúncio "
                "virar conversa no seu WhatsApp — não só clique."),
        "cta_hero": "Quero anunciar do jeito certo",
        "msg": "Olá, Renan! Quero um orçamento de gestão de tráfego pago.",
        "pills": ["Orçamento em até 24h", "Google Ads e Meta Ads", "Verba no seu cartão"],
        "painel_h2": "O que a gestão de tráfego pago inclui",
        "painel": [
            "Campanhas criadas do zero ou organizadas.",
            "Palavras e públicos escolhidos pelo seu cliente real.",
            "Anúncios escritos para gerar conversa.",
            "Página certa para cada campanha.",
            "Ajustes contínuos: o que não traz contato sai.",
            "Relatório claro de quantas conversas vieram.",
        ],
        "secoes": [
            ("split", {
                "tag": "O problema",
                "titulo": "Anunciar é fácil. Anunciar sem queimar dinheiro, não.",
                "ps": [
                    "O botão \"impulsionar\" do Instagram e a campanha automática do Google foram feitos para "
                    "gastar a sua verba — não para trazer o seu cliente. Sem ajuste, o anúncio aparece para "
                    "curioso, para gente de outra cidade e para quem nunca vai comprar.",
                    "Gestão de tráfego pago é o trabalho de escolher com cuidado quem vê o anúncio, o que ele diz e "
                    "para onde leva — e de cortar toda semana o que está gastando sem trazer conversa.",
                    "O anúncio e o Google orgânico não brigam: o anúncio traz cliente hoje, enquanto o seu "
                    "<a href=\"/google-perfil-empresa/\">Perfil da Empresa</a> e o seu site constroem a parte que "
                    "continua trazendo cliente de graça depois.",
                ],
                "card_titulo": "Sinais de que o anúncio está queimando verba",
                "card": [
                    "<strong>Muito alcance, pouca mensagem.</strong> Gente vendo, ninguém chamando.",
                    "<strong>Anúncio só no \"impulsionar\".</strong> Sem público nem objetivo definidos.",
                    "<strong>Ninguém sabe o que deu certo.</strong> Sem medir, não dá para melhorar.",
                ],
            }),
            ("texto", {
                "tag": "Google Ads",
                "titulo": "Google Ads em Goiânia: apareça para quem já está procurando",
                "ps": [
                    "No Google Ads o seu anúncio aparece para quem digitou exatamente o que você vende: \"dentista "
                    "em Goiânia\", \"energia solar preço\", \"advogado trabalhista perto de mim\". É a pessoa com "
                    "a necessidade na mão — por isso costuma ser o anúncio que mais vira venda para negócio local.",
                    "O trabalho começa pela lista de buscas certas e, tão importante quanto, pela lista das "
                    "buscas que <strong>não</strong> podem acionar o seu anúncio. Sem essa limpeza, você paga "
                    "clique de quem procura emprego, curso grátis ou outra cidade.",
                    "Depois vêm o texto do anúncio, a região de entrega — bairro, raio, cidade — e a "
                    "<a href=\"/criacao-de-landing-page/\">página que recebe o clique</a>. Anúncio bom "
                    "caindo em página ruim continua sendo dinheiro perdido.",
                ],
            }),
            ("texto", {
                "tag": "Meta Ads",
                "titulo": "Meta Ads: anúncios no Instagram e no Facebook",
                "ps": [
                    "No Instagram e no Facebook a pessoa não está procurando você — ela está rolando o feed. O "
                    "anúncio precisa interromper, despertar interesse e mostrar por que vale a pena chamar agora. "
                    "É o canal certo para gerar demanda, apresentar uma oferta nova e alcançar quem mora perto.",
                    "A campanha é montada com objetivo de conversa no WhatsApp, público definido por região, "
                    "idade e interesse, e criativos testados lado a lado. O que não traz mensagem é pausado; o "
                    "que traz ganha mais verba.",
                    "Para deixar claro: eu cuido dos anúncios, não do seu perfil. Postagem diária, stories e "
                    "gestão de redes sociais não fazem parte do serviço.",
                ],
            }),
            ("cards", {
                "tag": "O que está incluído",
                "titulo": "O que entra na gestão de tráfego pago",
                "itens": [
                    ("Diagnóstico da conta", "Se você já anuncia, eu olho o que está gastando sem retorno antes "
                     "de mexer em qualquer coisa."),
                    ("Estrutura das campanhas", "Campanhas separadas por serviço e por objetivo, para saber o que "
                     "funciona e o que não funciona."),
                    ("Anúncios escritos", "Textos e ideias de criativo pensados para gerar conversa, não curtida."),
                    ("Página de destino", "A página certa para cada campanha. Se não existir, a gente cria."),
                    ("Otimização contínua", "Ajuste de palavras, públicos, horários e verba conforme o que os "
                     "números mostram."),
                    ("Relatório que se entende", "Quantas conversas vieram e quanto custou cada uma, sem gráfico "
                     "bonito para esconder resultado."),
                ],
            }),
            ("faixas", {
                "titulo": "Quanto custa a gestão de tráfego pago?",
                "desc": ("São dois valores diferentes, e é bom separar desde o começo. A <strong>verba do "
                         "anúncio</strong> é paga direto ao Google ou ao Meta, no seu cartão — você decide quanto. "
                         "A <strong>gestão</strong> é o trabalho de montar e acompanhar as campanhas, e o valor "
                         "depende de quantas campanhas, canais e serviços entram no projeto."),
                "itens": [
                    ("Verba do anúncio", "Definida por você e paga direto à plataforma. Dá para começar pequeno "
                     "e aumentar conforme as conversas chegam."),
                    ("Gestão de um canal", "Google Ads ou Meta Ads. O mais comum para quem está começando a "
                     "anunciar com um ou dois serviços."),
                    ("Gestão de Google + Meta", "Os dois canais trabalhando juntos: Google para quem procura, "
                     "Instagram para gerar demanda."),
                ],
            }),
            ("orcamento", {
                "titulo": "Seus anúncios sob medida: quanto fica o seu projeto?",
                "desc": ("Escolha por onde quer começar e me chame no WhatsApp. Em até 24 horas você recebe o "
                         "valor da gestão e uma sugestão de verba inicial para o seu caso."),
                "itens": [
                    ("Google Ads", "Para aparecer para quem já está procurando o que você vende.",
                     ["Buscas certas e buscas bloqueadas", "Anúncio por região e bairro", "Contatos medidos"],
                     "Olá, Renan! Quero um orçamento de gestão de Google Ads.", "Orçamento de Google Ads"),
                    ("Meta Ads", "Para anunciar no Instagram e no Facebook para quem mora perto.",
                     ["Campanha de conversa no WhatsApp", "Públicos por região e interesse", "Criativos testados"],
                     "Olá, Renan! Quero um orçamento de anúncios no Instagram e Facebook.", "Orçamento de Meta Ads"),
                    ("Google + Meta", "Para quem quer os dois canais trabalhando juntos.",
                     ["Tudo do Google Ads e do Meta Ads", "Verba distribuída pelo que funciona", "Um relatório só"],
                     "Olá, Renan! Quero um orçamento de Google Ads e Meta Ads juntos.", "Quero os dois canais"),
                    ("Já anuncio e não funciona", "Para quem já investe e não vê o WhatsApp tocar.",
                     ["Diagnóstico da conta atual", "Corte do que gasta sem retorno", "Plano de ajuste"],
                     "Olá, Renan! Já anuncio e não está trazendo cliente. Pode olhar minhas campanhas?", "Olhar meus anúncios"),
                ],
                "destaque": 3,
            }),
            ("passos", {
                "titulo": "Como começa a gestão dos seus anúncios",
                "itens": [
                    ("1. Me conte o negócio", "No WhatsApp: o que você vende, onde atende e se já anuncia."),
                    ("2. Montamos o plano", "Canal, campanhas, verba inicial e a página que recebe o clique."),
                    ("3. Anúncio no ar e acompanhado", "Ajustes contínuos e relatório de quantas conversas vieram."),
                ],
            }),
        ],
        "faq": [
            ("Quanto custa a gestão de tráfego pago?",
             "São dois valores separados: a verba do anúncio, paga direto ao Google ou ao Meta no seu cartão, e a "
             "gestão, que é o trabalho de montar e acompanhar as campanhas. O valor da gestão depende de quantos "
             "canais e serviços entram no projeto. O orçamento é grátis e sai em até 24 horas pelo WhatsApp."),
            ("Quanto eu preciso investir em anúncio para começar?",
             "Dá para começar pequeno e aumentar conforme as conversas chegam. A verba ideal depende da sua cidade, "
             "da concorrência no seu ramo e de quanto vale um cliente para você — é isso que eu olho antes de "
             "sugerir um valor."),
            ("Google Ads ou Meta Ads: qual é melhor para mim?",
             "Google Ads aparece para quem já está procurando o serviço, e costuma converter mais para negócio "
             "local. Meta Ads alcança quem ainda não está procurando, e é bom para gerar demanda e divulgar oferta. "
             "Muitas empresas usam os dois, cada um com o seu papel."),
            ("Vocês garantem resultado?",
             "Ninguém sério garante número de clientes, porque o resultado depende também da oferta, do preço e do "
             "atendimento. O que eu garanto é o trabalho: campanha bem montada, verba cortada onde não dá retorno "
             "e relatório claro do que aconteceu."),
            ("Vocês cuidam do meu Instagram também?",
             "Não. A gestão é dos anúncios. Postagens do dia a dia, stories e gestão de redes sociais não fazem "
             "parte do serviço."),
            ("Tráfego pago substitui aparecer no Google de graça?",
             "Não, eles se completam. O anúncio traz cliente enquanto você paga; o Perfil da Empresa e o site bem "
             "feitos continuam trazendo cliente de graça depois. O ideal é começar pelo anúncio e construir a "
             "parte orgânica ao mesmo tempo."),
        ],
        "relacionados": [
            ("/trafego-pago-para-dentistas/", "Tráfego pago para dentistas", "Google Ads e Meta Ads dentro das regras do CFO."),
            ("/trafego-pago-para-advogados/", "Tráfego pago para advogados", "Google Ads dentro do Provimento 205/2021 da OAB."),
            ("/trafego-pago-para-energia-solar/", "Tráfego pago para energia solar", "Pedidos de orçamento sem clique de curioso."),
            ("/trafego-pago-para-imobiliarias/", "Tráfego pago para imobiliárias", "Leads próprios sem depender de portal."),
            ("/blog/quanto-investir-em-trafego-pago/", "Quanto investir em tráfego pago", "Como calcular a verba a partir do valor do seu cliente."),
            ("/blog/trafego-pago-para-clinicas/", "Tráfego pago para clínicas", "Google Ads e Meta Ads dentro das regras do CFM e do CFO."),
            ("/criacao-de-landing-page/", "Criação de landing page", "A página que transforma o clique do anúncio em conversa."),
            ("/google-perfil-empresa/", "Google Perfil da Empresa", "A parte que traz cliente de graça, sem pagar por clique."),
            ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "O site que sustenta o anúncio e aparece no Google."),
        ],
        "cta_final": ("Me conte o que você vende. Eu te digo por onde começar a anunciar.",
                      "Sem compromisso: se você já anuncia, eu olho as suas campanhas; se ainda não, eu te digo qual canal faz mais sentido."),
    },

    # =====================================================================
    # LOJA VIRTUAL
    # =====================================================================
    {
        "slug": "criacao-de-loja-virtual-goiania",
        "title": "Criação de Loja Virtual em Goiânia | Orçamento Grátis",
        "desc": ("Criação de loja virtual em Goiânia: catálogo, pagamento e frete configurados, páginas de produto "
                 "que aparecem no Google e orçamento grátis em 24h pelo WhatsApp."),
        "trilha": "Criação de loja virtual em Goiânia",
        "servico": "Criação de loja virtual",
        "eyebrow": "Goiânia e todo o Brasil",
        "h1": "Criação de loja virtual em Goiânia",
        "sub": ("Vender só pelo WhatsApp e pelo Instagram tem limite: você responde uma pessoa por vez e o cliente "
                "some quando você demora. A loja virtual vende enquanto você dorme. Eu monto a sua com catálogo, "
                "pagamento e frete funcionando — e com as páginas de produto pensadas para aparecer no Google."),
        "cta_hero": "Quero minha loja virtual",
        "msg": "Olá, Renan! Quero um orçamento de loja virtual.",
        "pills": ["Orçamento em até 24h", "Pagamento e frete prontos", "Prazo por escrito"],
        "painel_h2": "O que vem na sua loja virtual",
        "painel": [
            "Catálogo organizado por categoria.",
            "Pagamento por Pix, cartão e boleto.",
            "Cálculo de frete e retirada na loja.",
            "Páginas de produto pensadas para o Google.",
            "Botão de WhatsApp para quem quer tirar dúvida.",
            "Você aprende a cadastrar produto sozinho.",
        ],
        "secoes": [
            ("split", {
                "tag": "O problema",
                "titulo": "Vender só pelo WhatsApp tem teto",
                "ps": [
                    "Muita loja de Goiânia vende bem pelo Instagram e pelo WhatsApp — até o dia em que não dá mais "
                    "para responder todo mundo. O cliente pergunta o preço, espera, desiste e compra do concorrente "
                    "que tem site.",
                    "A loja virtual resolve isso: o cliente vê o produto, o preço, o frete, paga e pronto. Você "
                    "separa o pedido. E quem ainda tem dúvida continua podendo chamar no WhatsApp.",
                    "O detalhe que quase ninguém cuida: loja virtual também precisa ser encontrada. Página de "
                    "produto com nome certo, descrição própria e foto boa aparece no Google — e cliente que chega "
                    "pela busca não custa clique.",
                ],
                "card_titulo": "Sinais de que chegou a hora da loja",
                "card": [
                    "<strong>Você repete o preço o dia inteiro.</strong> No WhatsApp e no direct.",
                    "<strong>Cliente some enquanto espera resposta.</strong> E compra de quem responde antes.",
                    "<strong>Você quer vender para outras cidades.</strong> Sem estar no balcão.",
                ],
            }),
            ("cards", {
                "tag": "O que está incluído",
                "titulo": "O que entra na criação da sua loja virtual",
                "itens": [
                    ("Catálogo organizado", "Categorias, variações de tamanho e cor, estoque e fotos. O cliente "
                     "acha o que procura em poucos toques."),
                    ("Pagamento configurado", "Pix, cartão e boleto funcionando, com o dinheiro caindo na sua conta."),
                    ("Frete e retirada", "Cálculo de frete por CEP e opção de retirar na loja ou entrega local."),
                    ("Produto que aparece no Google", "Nome, descrição e foto de cada produto pensados para a busca. "
                     "É venda sem pagar anúncio."),
                    ("Rápida no celular", "A maior parte das compras começa no celular. Loja pesada perde venda."),
                    ("Você no controle", "Eu te ensino a cadastrar produto, mudar preço e acompanhar pedido sem "
                     "depender de ninguém."),
                ],
            }),
            ("faixas", {
                "titulo": "Quanto custa uma loja virtual?",
                "desc": ("É o projeto com maior variação de valor, porque uma loja com vinte produtos e uma com dois "
                         "mil são trabalhos completamente diferentes. O que muda o preço é o tamanho do catálogo, "
                         "quem cadastra os produtos, a plataforma e as integrações."),
                "itens": [
                    ("Loja pequena", "Poucos produtos, catálogo simples, pagamento e frete básicos. Ótima para "
                     "começar a vender online sem complicação."),
                    ("Loja com catálogo maior", "Muitas categorias e variações, produtos cadastrados com "
                     "descrição própria e páginas pensadas para o Google."),
                    ("Loja integrada", "Integração com sistema, estoque ou marketplace. Projeto maior, feito sob "
                     "medida para a operação."),
                ],
            }),
            ("orcamento", {
                "titulo": "Sua loja sob medida: quanto fica o seu projeto?",
                "desc": ("Me conte o que você vende e quantos produtos tem. Em até 24 horas você recebe o valor "
                         "exato da sua loja e a plataforma que eu recomendo para o seu tamanho."),
                "itens": [
                    ("Começar a vender online", "Para quem vende no balcão ou no WhatsApp e quer a primeira loja.",
                     ["Catálogo e fotos organizados", "Pagamento e frete configurados", "Botão de WhatsApp"],
                     "Olá, Renan! Quero um orçamento para começar a vender online com uma loja virtual.", "Quero minha primeira loja"),
                    ("Loja que aparece no Google", "Para quem quer vender sem depender só de anúncio.",
                     ["Tudo da primeira loja", "Páginas de produto para a busca", "Categorias pensadas para o Google"],
                     "Olá, Renan! Quero um orçamento de loja virtual que apareça no Google.", "Quero vender pelo Google"),
                    ("Loja + anúncios", "Para quem quer a loja e o tráfego para ela no mesmo lugar.",
                     ["Loja pronta para anúncio", "Google Ads e Meta Ads", "Vendas medidas"],
                     "Olá, Renan! Quero um orçamento de loja virtual com anúncios.", "Quero loja + anúncio"),
                    ("Já tenho loja e não vende", "Para quem tem loja parada e quer saber o motivo.",
                     ["Diagnóstico da loja atual", "Ajustes de produto e página", "Plano para atrair cliente"],
                     "Olá, Renan! Já tenho uma loja virtual e ela não vende. Pode dar uma olhada?", "Olhar minha loja"),
                ],
                "destaque": 1,
            }),
            ("passos", {
                "titulo": "Como é criar a sua loja virtual",
                "itens": [
                    ("1. Me conte o que você vende", "Quantos produtos, como entrega hoje e como recebe."),
                    ("2. Montamos e cadastramos", "Loja, pagamento, frete e os produtos principais no ar."),
                    ("3. Você aprende e vende", "Treinamento para você cuidar da loja e acompanhar os pedidos."),
                ],
            }),
        ],
        "faq": [
            ("Quanto custa criar uma loja virtual?",
             "Depende do tamanho do catálogo, de quem cadastra os produtos, da plataforma e das integrações. Uma "
             "loja com poucos produtos custa bem menos do que uma integrada a sistema e estoque. O orçamento é "
             "grátis e sai em até 24 horas pelo WhatsApp."),
            ("Qual plataforma vocês usam?",
             "A que fizer sentido para o seu tamanho. Para quem está começando, uma plataforma pronta costuma ser "
             "mais barata de manter; para catálogo grande ou integração, pode valer outra. Eu te digo qual e por "
             "quê antes de começar."),
            ("A loja tem mensalidade?",
             "A maioria das plataformas cobra uma mensalidade própria, e os meios de pagamento cobram uma taxa por "
             "venda. Esses custos são da plataforma, não meus — e eu te mostro todos antes de fechar."),
            ("Eu consigo cadastrar produto sozinho depois?",
             "Consegue. A loja é entregue com treinamento para você cadastrar produto, mudar preço e acompanhar "
             "pedido sem depender de ninguém."),
            ("A loja aparece no Google?",
             "Pode aparecer, se as páginas de produto forem bem feitas: nome certo, descrição própria e foto boa. "
             "Esse cuidado faz parte do projeto, mas posição no Google leva tempo e ninguém honesto promete data."),
            ("Vocês fazem anúncio para a loja?",
             "Sim. A RCB faz a gestão de tráfego pago no Google Ads e no Meta Ads, e a loja já sai pronta para "
             "receber anúncio."),
        ],
        "relacionados": [
            ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Google Ads e Meta Ads para levar comprador até a sua loja."),
            ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Quando o que você precisa é de site institucional, não de loja."),
            ("/blog/quanto-custa-um-site/", "Quanto custa um site", "As faixas de preço do mercado, incluindo loja virtual."),
        ],
        "cta_final": ("Me conte o que você vende. Eu te digo como levar isso para a internet.",
                      "Sem compromisso: você me diz quantos produtos tem e como vende hoje, e eu te mostro o caminho."),
    },
]
