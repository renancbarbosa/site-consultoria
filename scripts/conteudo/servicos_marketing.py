# -*- coding: utf-8 -*-
"""
Conteúdo das páginas de serviço da linha "Sites e Anúncios" (28/09/2026).

  /marketing-para-energia-solar/   (Etapa 4, 04/10/2026: pagina principal do nicho)
  /criacao-de-landing-page/   (nacional desde 04/10/2026; 301 da antiga de Goiania)
  /gestao-de-trafego-pago/   (nacional desde 04/10/2026; 301 da antiga de Goiania)
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
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago",
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
        # Etapa 3 do plano de nichos (04/10/2026): pagina NACIONAL, com 301 de
        # /gestao-de-trafego-pago/ (0 impressao em 28 dias). Google Ads (rede de
        # pesquisa) em primeiro lugar; Meta Ads so como complemento; sempre com landing page
        # e medicao. Regra de honestidade: sem case, cliente ou numero inventado.
        "slug": "gestao-de-trafego-pago",
        "nacional": True,
        "data": "2026-10-04",
        "publico": "Empresas e profissionais que querem clientes pelo Google Ads",
        "title": "Gestão de Tráfego Pago para Empresas (Google Ads) | RCB SEO",
        "desc": ("Gestão de tráfego pago para empresas: anúncio na pesquisa do Google para quem já procura o seu "
                 "serviço, com landing page e medição. Orçamento grátis em 24h."),
        "trilha": "Gestão de tráfego pago",
        "servico": "Gestão de tráfego pago",
        "eyebrow": "Google Ads para empresas de todo o Brasil",
        "h1": "Gestão de tráfego pago para empresas no Google Ads",
        "sub": ("Gestão de tráfego pago é o trabalho de montar, acompanhar e ajustar os seus anúncios no Google para "
                "que eles tragam contatos — e não só cliques. Eu cuido da campanha na pesquisa do Google, da página "
                "que recebe o clique e da medição de cada conversa. A verba é paga direto ao Google, no seu cartão; "
                "o orçamento da gestão é grátis e sai em até 24 horas pelo WhatsApp."),
        "cta_hero": "Quero orçamento de Google Ads",
        "msg": "Olá, Renan! Quero um orçamento de gestão de Google Ads para a minha empresa.",
        "pills": ["Orçamento em até 24h", "Anúncio na pesquisa do Google", "Verba no seu cartão"],
        "painel_h2": "O que a gestão inclui",
        "painel": [
            "Pesquisa do que o seu cliente digita no Google.",
            "Campanha na rede de pesquisa, separada por serviço.",
            "Palavras negativas para não pagar clique errado.",
            "Landing page ligada a cada anúncio.",
            "Conversões medidas no Google Ads e no GA4.",
            "Relatório simples de contatos e custo por contato.",
        ],
        "faq_titulo": "Perguntas frequentes sobre gestão de tráfego pago",
        "secoes": [
            ("texto", {
                "tag": "Pesquisa x impulsionar",
                "titulo": "Qual a diferença entre anunciar no Google e impulsionar post no Instagram?",
                "ps": [
                    "Quando alguém digita no Google \"desentupidora 24 horas\" ou \"contador para MEI\", essa pessoa já "
                    "está procurando o serviço. Na "
                    "<a href=\"https://support.google.com/google-ads/answer/1722047?hl=pt-BR\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">rede de pesquisa do Google</a>, o seu anúncio aparece perto dos "
                    "resultados exatamente nesse momento — é o cliente que vai atrás de você.",
                    "Impulsionar um post funciona ao contrário: interrompe quem está rolando o feed, pensando em outra "
                    "coisa. Serve para tornar a marca conhecida, mas raramente traz o cliente que precisa resolver "
                    "algo hoje. Por isso o foco aqui é o anúncio na pesquisa; Instagram e Facebook entram como "
                    "complemento, quando fazem sentido para o seu negócio.",
                ],
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que tanta empresa anuncia no Google e o WhatsApp não toca?",
                "ps": [
                    "Quase sempre o problema não é o Google Ads em si, mas a montagem. Campanha aberta para qualquer "
                    "busca parecida, anúncio que leva para a página inicial do site e ninguém medindo o que vira "
                    "contato: o dinheiro sai todo dia e ninguém sabe dizer o que trouxe cliente.",
                    "No Google Ads, na forma mais comum, "
                    "<a href=\"https://support.google.com/google-ads/answer/116495?hl=pt-BR\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">você paga a cada clique</a>. Então cada clique de quem procurava "
                    "emprego, curso ou algo de graça é verba jogada fora — e isso dá para cortar.",
                ],
                "card_titulo": "Sinais de que a campanha precisa de gestão",
                "card": [
                    "Muitos cliques e poucas conversas.",
                    "Anúncio aparecendo para buscas que não têm nada a ver.",
                    "Clique caindo na página inicial do site.",
                    "Nenhum relatório de quantos contatos vieram.",
                    "Campanha ligada no automático há meses.",
                ],
            }),
            ("cards", {
                "tag": "O que está incluído",
                "titulo": "O que entra na gestão de Google Ads?",
                "desc": "Tudo o que separa um anúncio que gasta de um anúncio que traz contato.",
                "itens": [
                    ("Pesquisa de palavras",
                     "Levantamento do que o seu cliente realmente digita no Google, serviço por serviço, e na sua "
                     "região de atendimento."),
                    ("Palavras negativas",
                     "Bloqueio das buscas que não interessam — \"grátis\", \"curso\", \"vaga\" —, usando as "
                     "<a href=\"https://support.google.com/google-ads/answer/2453972?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">palavras-chave negativas</a> do próprio Google Ads."),
                    ("Anúncios escritos para a sua oferta",
                     "Textos que falam do seu serviço e da sua região, sem promessa que você não pode cumprir."),
                    ("Landing page para cada campanha",
                     "O clique cai numa página feita para aquele serviço, com WhatsApp. Se você ainda não tem, eu "
                     "crio a <a href=\"/criacao-de-landing-page/\">landing page para anúncios</a>."),
                    ("Medição de conversões",
                     "Cada toque no WhatsApp e cada formulário registrado como conversão, com a "
                     "<a href=\"https://support.google.com/google-ads/answer/1722022?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">medição do próprio Google Ads</a> e o GA4."),
                    ("Relatório que você entende",
                     "Quantos contatos vieram, quanto custou cada um e o que vou ajustar no mês seguinte."),
                ],
            }),
            ("texto", {
                "tag": "Anúncio + SEO",
                "titulo": "Por que anúncio no Google e SEO funcionam melhor juntos?",
                "ps": [
                    "O anúncio é a torneira: abre hoje e traz cliente enquanto você paga. O SEO é a construção: leva "
                    "meses, mas depois traz contato sem custo por clique. Quem usa só anúncio fica refém da verba; "
                    "quem usa só SEO espera demais pelo primeiro resultado.",
                    "Juntos, um ajuda o outro. O anúncio mostra rápido quais buscas trazem cliente de verdade, e essas "
                    "buscas viram as páginas que o "
                    "<a href=\"/consultoria-seo-local/\">trabalho de SEO e Google Meu Negócio</a> vai fortalecer. "
                    "Com o tempo, você depende menos do anúncio para encher a agenda.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona a gestão, do diagnóstico ao relatório?",
                "itens": [
                    ("Conversa e diagnóstico",
                     "Você me conta o que vende e onde atende. Se já anuncia, eu olho a conta antes de propor algo."),
                    ("Plano por escrito",
                     "Em até 24 horas: campanhas, serviços, sugestão de verba e o valor da gestão."),
                    ("Montagem",
                     "Palavras, negativas, anúncios, landing page e medição configurados antes de gastar o primeiro real."),
                    ("Ajuste contínuo",
                     "Corte do que gasta sem trazer contato e reforço do que funciona."),
                    ("Relatório mensal",
                     "Contatos, custo por contato e os próximos passos, em linguagem simples."),
                ],
            }),
            ("texto", {
                "tag": "Verba e gestão",
                "titulo": "Quanto investir em Google Ads e quanto custa a gestão?",
                "ps": [
                    "São dois valores diferentes. A verba é o que você paga ao Google pelos cliques, direto no seu "
                    "cartão, sem passar por mim. A gestão é o meu trabalho de montar, ajustar e medir as campanhas.",
                    "A verba certa depende de quanto vale um cliente para a sua empresa e de quanto custa o clique no "
                    "seu ramo e na sua região. Dá para começar com um ou dois serviços e aumentar quando os contatos "
                    "chegarem. Para fazer essa conta com calma, veja o guia "
                    "<a href=\"/blog/quanto-investir-em-trafego-pago/\">quanto investir em tráfego pago</a>. O "
                    "orçamento da gestão é individual, grátis e sai em até 24 horas.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa quer começar no Google Ads?",
                "desc": "Escolha o ponto de partida. Em até 24 horas você recebe o plano e o valor da gestão.",
                "destaque": 0,
                "itens": [
                    ("Começar a anunciar no Google", "Para quem nunca anunciou ou quer começar do jeito certo.",
                     ["Pesquisa de palavras e negativas", "Campanha na rede de pesquisa", "Conversões medidas"],
                     "Olá, Renan! Quero começar a anunciar no Google Ads.", "Pedir orçamento"),
                    ("Já anuncio e não funciona", "Para quem gasta todo mês e não vê o WhatsApp tocar.",
                     ["Diagnóstico da conta", "Corte do que gasta sem retorno", "Plano de ajuste"],
                     "Olá, Renan! Já anuncio no Google e não está trazendo cliente. Pode olhar?", "Olhar meus anúncios"),
                    ("Anúncio + landing page", "Para quem não tem uma página certa para receber o clique.",
                     ["Gestão de Google Ads", "Landing page para o anúncio", "Medição de ponta a ponta"],
                     "Olá, Renan! Quero gestão de Google Ads com landing page.", "Pedir orçamento"),
                ],
            }),
            ("texto", {
                "tag": "Para quem",
                "titulo": "Para quais empresas a gestão de tráfego pago faz sentido?",
                "ps": [
                    "Faz sentido para quem vende um serviço que as pessoas procuram no Google quando precisam: "
                    "empresas de serviço local, profissionais liberais, clínicas, escritórios, comércio que vende "
                    "na região. Cada ramo tem suas regras e seus cuidados — veja como funciona para "
                    "<a href=\"/trafego-pago-para-energia-solar/\">empresas de energia solar</a>, "
                    "<a href=\"/trafego-pago-para-dentistas/\">dentistas</a>, "
                    "<a href=\"/trafego-pago-para-advogados/\">advogados</a> e "
                    "<a href=\"/trafego-pago-para-imobiliarias/\">imobiliárias</a>.",
                    "Faz menos sentido quando a margem de cada venda é tão pequena que não paga o clique, ou quando "
                    "ninguém pesquisa o que você vende. Nesses casos eu digo isso no diagnóstico, antes de você "
                    "investir.",
                ],
            }),
        ],
        "faq": [
            ("O que faz um gestor de tráfego pago?",
             "Monta as campanhas, escolhe as palavras e as negativas, escreve os anúncios, liga cada anúncio à "
             "página certa, configura a medição de conversões e ajusta tudo com base no que traz contato."),
            ("A verba do anúncio fica com você?",
             "Não. A verba é paga direto ao Google, no cartão da sua empresa. Eu cobro só a gestão, que é o "
             "trabalho de montar e acompanhar as campanhas."),
            ("Vocês anunciam no Instagram e no Facebook também?",
             "Sim, como complemento. O foco é o anúncio na pesquisa do Google, que pega quem já procura o seu "
             "serviço. Meta Ads entra quando faz sentido para o seu negócio, sempre com página e medição."),
            ("Preciso ter site para anunciar no Google?",
             "Precisa de uma página para receber o clique. Pode ser o site, se ele tiver a página do serviço, ou "
             "uma landing page feita para o anúncio — que eu também crio."),
            ("Em quanto tempo os anúncios trazem contato?",
             "Os primeiros contatos podem vir logo que a campanha entra no ar, mas as primeiras semanas são de "
             "ajuste. O que dá para garantir desde o começo é a medição: você vê quantos contatos vieram e quanto "
             "custou cada um."),
            ("Quanto custa a gestão de tráfego pago?",
             "Depende de quantos serviços e campanhas entram e do que precisa ser montado, como landing page e "
             "medição. O orçamento é individual, grátis e sai em até 24 horas pelo WhatsApp."),
            ("Vocês atendem empresas de outras cidades?",
             "Sim. A gestão de Google Ads é feita online para empresas de todo o Brasil. Em Goiânia também dá para "
             "conversar pessoalmente."),
            ("Existe fidelidade ou contrato longo?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento. A conta do Google Ads fica no nome da sua empresa."),
        ],
        "relacionados": [
            ("/criacao-de-landing-page/", "Landing page para anúncios",
             "A página que transforma o clique do anúncio em conversa."),
            ("/blog/quanto-investir-em-trafego-pago/", "Quanto investir em tráfego pago?",
             "Como calcular a verba a partir do valor do seu cliente."),
            ("/blog/seo-ou-trafego-pago-empresa-local/", "SEO ou tráfego pago?",
             "O que faz mais sentido para a empresa local em cada momento."),
        ],
        "cta_final": ("Me conte o que você vende. Eu te digo se o Google Ads faz sentido para você.",
                      "Sem compromisso: se você já anuncia, eu olho a conta; se não, te mostro por onde começar sem "
                      "queimar verba."),
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
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Google Ads e Meta Ads para levar comprador até a sua loja."),
            ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Quando o que você precisa é de site institucional, não de loja."),
            ("/blog/quanto-custa-um-site/", "Quanto custa um site", "As faixas de preço do mercado, incluindo loja virtual."),
        ],
        "cta_final": ("Me conte o que você vende. Eu te digo como levar isso para a internet.",
                      "Sem compromisso: você me diz quantos produtos tem e como vende hoje, e eu te mostro o caminho."),
    },
    {
        # Etapa 4 do plano de nichos (04/10/2026): pagina principal do nicho ENERGIA SOLAR.
        # Publico: o DONO da integradora (regra de ouro). Buscas do cliente final so no meio,
        # entre aspas, como argumento. Fontes conferidas: Lei 14.300/2022, CDC art. 37,
        # ANEEL (bandeiras tarifarias), IBGE/Concla (CNAE 4321-5/00) e CNPJ publico (jun/2026).
        "slug": "marketing-para-energia-solar",
        "nacional": True,
        "data": "2026-10-04",
        "publico": "Empresas integradoras de energia solar",
        "title": "Marketing para Energia Solar: SEO, Google e Anúncios | RCB SEO",
        "desc": ("Marketing para empresas de energia solar: Google Meu Negócio, site, SEO e Google Ads para o "
                 "integrador receber pedidos de orçamento. Orçamento grátis em 24h."),
        "trilha": "Marketing para energia solar",
        "servico": "Marketing para empresas de energia solar",
        "eyebrow": "Para integradores de energia solar de todo o Brasil",
        "h1": "Marketing e SEO para empresas de energia solar",
        "sub": ("Marketing para energia solar é fazer a sua empresa aparecer quando alguém da sua região pesquisa como "
                "reduzir a conta de luz — e transformar essa busca em pedido de simulação no seu WhatsApp. Eu cuido "
                "das quatro frentes que trazem esse cliente: Google Meu Negócio, site com SEO, anúncio no Google e "
                "landing page. O orçamento é grátis e sai em até 24 horas."),
        "cta_hero": "Quero mais pedidos de orçamento",
        "msg": "Olá, Renan! Tenho uma empresa de energia solar e quero mais pedidos de orçamento pelo Google.",
        "pills": ["Orçamento em até 24h", "Feito para integradores", "Prazo por escrito"],
        "painel_h2": "As quatro frentes",
        "painel": [
            "Google Meu Negócio para aparecer no mapa da sua região.",
            "Site com uma página por tipo de cliente e cidade.",
            "Google Ads para quem já pesquisa instalação.",
            "Landing page que pede a conta de luz e abre o WhatsApp.",
            "Medição de cada pedido de simulação.",
            "Texto dentro do que a lei e o consumidor permitem.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para energia solar",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que tanta empresa de energia solar depende só de indicação?",
                "ps": [
                    "Muita integradora começou vendendo para conhecidos e cresceu na base da indicação. Funciona — até "
                    "a agenda esvaziar num mês e não haver nenhum outro canal trazendo cliente. Enquanto isso, o "
                    "concorrente que aparece no Google recebe o pedido de quem nunca ouviu falar de nenhum dos dois.",
                    "E a concorrência é grande. O IBGE classifica a instalação de painéis solares fotovoltaicos em "
                    "prédios dentro do "
                    "<a href=\"https://cnae.ibge.gov.br/?subclasse=4321500&amp;tipo=cnae&amp;versao=10&amp;view=subclasse\" "
                    "target=\"_blank\" rel=\"noopener noreferrer\">CNAE 4321-5/00 (Instalação e manutenção elétrica)</a>. "
                    "Pelos dados públicos de CNPJ de junho de 2026, esse código reúne 328.524 empresas ativas e teve "
                    "17.358 aberturas em 90 dias. Nem todas são de energia solar — o código inclui eletricistas em geral "
                    "—, mas o número mostra com quanta gente o integrador disputa a atenção de quem procura.",
                ],
                "card_titulo": "Sinais de que falta marketing na integradora",
                "card": [
                    "Mês bom e mês fraco sem explicação.",
                    "Perfil do Google sem fotos de obra nem avaliações.",
                    "Site com uma página só, igual a todos.",
                    "Anúncio que traz curioso e pedido de peça avulsa.",
                    "Ninguém sabe de onde veio o último cliente.",
                ],
            }),
            ("texto", {
                "tag": "Como o cliente procura",
                "titulo": "O que o cliente do integrador pesquisa no Google antes de pedir orçamento?",
                "ps": [
                    "O seu cliente quase nunca começa digitando o nome técnico do serviço. Ele pesquisa a dor: "
                    "\"como diminuir a conta de luz\", \"energia solar vale a pena\", \"quanto custa energia solar para "
                    "casa\" e, mais perto da decisão, \"energia solar perto de mim\" ou o nome da cidade.",
                    "Por isso o marketing do integrador precisa estar nos dois momentos: no começo, com conteúdo que "
                    "explica economia, conexão com a distribuidora e prazos, sem prometer conta zerada; e no fim, com o "
                    "perfil no mapa, a página da cidade e o anúncio aparecendo para quem já quer a simulação.",
                    "Esse conteúdo educativo também responde às dúvidas que o próprio cliente traz para a visita — o "
                    "que poupa tempo do vendedor e aumenta a confiança antes do orçamento.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de uma empresa de energia solar?",
                "desc": "Quatro frentes que se ajudam. Dá para começar por uma e somar as outras depois.",
                "itens": [
                    ("Google Meu Negócio",
                     "Perfil completo, com fotos de obras feitas (com autorização do cliente), serviços, cidades "
                     "atendidas e avaliações respondidas. É o que aparece no mapa quando alguém procura instalador "
                     "na região. Veja como funciona a <a href=\"/google-perfil-empresa/\">otimização do Google "
                     "Perfil da Empresa</a>."),
                    ("Site com SEO",
                     "Uma página para cada tipo de cliente — residencial, comercial, rural — e para as cidades que "
                     "você atende, com respostas para as dúvidas reais. Detalhes em "
                     "<a href=\"/blog/site-para-empresa-de-energia-solar/\">site para empresa de energia solar</a>."),
                    ("Google Ads",
                     "Anúncio na pesquisa do Google para quem já procura instalação na sua região, com as buscas de "
                     "curso, vaga e peça bloqueadas. Veja o "
                     "<a href=\"/trafego-pago-para-energia-solar/\">tráfego pago para energia solar</a>."),
                    ("Landing page de simulação",
                     "A página que recebe o clique do anúncio, pede a conta de luz e abre o WhatsApp. Existe um "
                     "<a href=\"/modelos/landing-page-energia-solar/\">modelo demonstrativo</a> para você ver como fica."),
                    ("Medição dos pedidos",
                     "Cada pedido de simulação registrado, por cidade e por canal, para você saber o que traz cliente."),
                    ("Conteúdo que educa",
                     "Textos que explicam economia, prazos e conexão sem promessa exagerada — e que viram argumento "
                     "de venda na visita."),
                ],
            }),
            ("texto", {
                "tag": "Lei e promessa",
                "titulo": "O que a lei muda no marketing de energia solar?",
                "ps": [
                    "A geração de energia em casa e na empresa tem marco legal próprio: a "
                    "<a href=\"https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm\" "
                    "target=\"_blank\" rel=\"noopener noreferrer\">Lei 14.300/2022</a>, que instituiu as regras da "
                    "micro e minigeração distribuída e do sistema de compensação de energia. É ela que está por trás das "
                    "perguntas que o seu cliente faz sobre compensação e conexão com a distribuidora — e um bom "
                    "conteúdo explica isso em palavras simples.",
                    "O outro cuidado é a promessa. Frases como \"conta de luz zerada\" ou um percentual fixo de economia "
                    "para todo mundo podem ser lidas como publicidade enganosa, que o "
                    "<a href=\"https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">Código de Defesa do Consumidor</a> proíbe no art. 37. O marketing que "
                    "funciona mostra o processo, as obras reais e convida para a simulação — que é onde a economia de "
                    "cada cliente aparece de verdade.",
                ],
            }),
            ("texto", {
                "tag": "Sazonalidade",
                "titulo": "Existe época melhor para divulgar energia solar?",
                "ps": [
                    "A dúvida sobre energia solar costuma aparecer quando a conta de luz pesa. A ANEEL define todo mês a "
                    "<a href=\"https://www.gov.br/aneel/pt-br/assuntos/tarifas/bandeiras-tarifarias\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">bandeira tarifária</a> — verde, amarela ou vermelha —, que indica se a "
                    "energia vai custar mais ou menos naquele período. Meses de bandeira mais cara e de calor, com "
                    "ar-condicionado ligado, tendem a ser justamente quando muita gente para para fazer a conta — é uma "
                    "observação de mercado, não um dado medido de buscas.",
                    "Na prática, isso pede duas coisas: estar no Google o ano inteiro (SEO e Google Meu Negócio "
                    "trabalham em segundo plano) e ter o anúncio pronto para aumentar a verba quando a procura subir. "
                    "Quem só começa a divulgar quando a conta já está cara chega depois do concorrente.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing da sua integradora, do diagnóstico aos pedidos?",
                "itens": [
                    ("Diagnóstico", "Olho o seu perfil no Google, o site e quem aparece antes de você nas suas cidades."),
                    ("Plano por escrito", "Em até 24 horas: as frentes para começar, o que entra e o valor de cada uma."),
                    ("Base no Google", "Perfil do Google Meu Negócio e páginas do site por tipo de cliente e cidade."),
                    ("Anúncio e landing page", "Quando fizer sentido, campanha no Google com página de simulação."),
                    ("Medição", "Relatório de pedidos de simulação por canal e por cidade."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa de energia solar quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa", "Para quem ainda depende de indicação e não aparece no Google.",
                     ["Google Meu Negócio completo", "Fotos de obras e serviços", "Rotina de avaliações"],
                     "Olá, Renan! Tenho empresa de energia solar e quero aparecer no Google Maps.", "Pedir orçamento"),
                    ("Site + Google Meu Negócio", "Para ser encontrado nas buscas da sua região o ano inteiro.",
                     ["Páginas por tipo de cliente e cidade", "SEO e Google Meu Negócio", "Pedidos medidos"],
                     "Olá, Renan! Quero site e Google Meu Negócio para a minha empresa de energia solar.", "Pedir orçamento"),
                    ("Anúncio + landing page", "Para encher a agenda de simulações agora.",
                     ["Google Ads por cidade", "Landing page de simulação", "Medição de cada pedido"],
                     "Olá, Renan! Quero Google Ads com landing page para energia solar.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Marketing para energia solar funciona para empresa pequena?",
             "Funciona, e costuma pesar mais para a pequena, porque o cliente decide por quem aparece e passa "
             "confiança na região dele. Dá para começar pelo Google Meu Negócio e somar site e anúncio depois."),
            ("O que traz cliente mais rápido: SEO ou anúncio?",
             "O anúncio no Google traz pedidos mais rápido, enquanto você paga. O SEO e o Google Meu Negócio levam "
             "meses para firmar, mas depois trazem pedido sem custo por clique. O ideal é usar os dois juntos."),
            ("Posso prometer economia na conta de luz no anúncio?",
             "Com cuidado. Prometer conta zerada ou um percentual igual para todo mundo pode ser publicidade enganosa. "
             "O mais seguro é convidar para a simulação, onde a economia de cada cliente é calculada."),
            ("Vale a pena ter uma página para cada cidade que atendo?",
             "Vale, desde que cada página tenha conteúdo próprio: obras feitas ali, particularidades da região e "
             "como funciona o atendimento. Página igual trocando só o nome da cidade não ajuda."),
            ("Vocês fazem as fotos das obras?",
             "Eu oriento como fotografar e organizar as fotos das obras, sempre com autorização do cliente. As "
             "fotos reais da sua equipe valem mais do que imagem de banco."),
            ("Quanto custa o marketing para empresa de energia solar?",
             "Depende das frentes que entram e de quantas cidades você atende. O orçamento é individual, grátis e "
             "sai em até 24 horas pelo WhatsApp. A verba de anúncio, quando houver, é paga direto ao Google."),
            ("Existe fidelidade?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento."),
        ],
        "relacionados": [
            ("/blog/como-conseguir-clientes-energia-solar/", "Como conseguir clientes de energia solar",
             "Os canais que trazem pedido de orçamento, um por um."),
            ("/blog/como-divulgar-empresa-de-energia-solar/", "Como divulgar empresa de energia solar",
             "Ideias práticas de divulgação para integradores."),
            ("/trafego-pago-para-energia-solar/", "Tráfego pago para energia solar",
             "Google Ads por cidade, com landing page e medição."),
        ],
        "cta_final": ("Me conte as cidades onde você instala. Eu te digo por onde começar.",
                      "Sem compromisso: eu olho como a sua empresa aparece hoje no Google e quem aparece antes de você."),
    },
    {
        # Etapa 5 do plano de nichos (04/10/2026): servico SEO PARA YOUTUBE. Publico: empresas e
        # profissionais que querem crescer o canal. Sem prometer inscritos/visualizacoes.
        # Fontes conferidas: "Como funciona a busca do YouTube", ajuda do YouTube (capitulos,
        # transcricao automatica, miniatura personalizada) e Google (SEO para video).
        "slug": "seo-para-youtube",
        "nacional": True,
        "data": "2026-10-04",
        "publico": "Empresas e profissionais que usam ou querem usar o YouTube para atrair clientes",
        "title": "SEO para YouTube: Como Fazer Seu Canal Crescer | RCB SEO",
        "desc": ("SEO para YouTube: título, descrição, capítulos, transcrição e miniatura para o vídeo da sua "
                 "empresa aparecer no YouTube e no Google. Orçamento grátis em 24h."),
        "trilha": "SEO para YouTube",
        "servico": "SEO para YouTube",
        "eyebrow": "Para empresas e profissionais de todo o Brasil",
        "h1": "SEO para YouTube: como fazer o canal da sua empresa crescer",
        "sub": ("SEO para YouTube é preparar cada vídeo para ser encontrado por quem pesquisa o assunto — no próprio "
                "YouTube e no Google. Na prática: escolher o tema pelo que o seu cliente pergunta, escrever o título e "
                "a descrição, organizar capítulos, revisar a transcrição e acertar a miniatura. Sem promessa de "
                "número de inscritos: o trabalho é deixar o vídeo fácil de achar e de entender. Orçamento grátis em "
                "até 24 horas."),
        "cta_hero": "Quero orçamento de SEO para YouTube",
        "msg": "Olá, Renan! Quero um orçamento de SEO para o canal do YouTube da minha empresa.",
        "pills": ["Orçamento em até 24h", "Sem promessa de inscritos", "Prazo por escrito"],
        "painel_h2": "O que entra em cada vídeo",
        "painel": [
            "Tema escolhido pelo que o seu cliente pesquisa.",
            "Título claro, com o assunto na frente.",
            "Descrição com resumo, links e contato.",
            "Capítulos para cada parte do vídeo.",
            "Transcrição revisada, sem os erros da automática.",
            "Miniatura que diz do que o vídeo trata.",
        ],
        "faq_titulo": "Perguntas frequentes sobre SEO para YouTube",
        "secoes": [
            ("texto", {
                "tag": "Como funciona",
                "titulo": "Como o YouTube decide quais vídeos mostrar na busca?",
                "ps": [
                    "Segundo a página oficial "
                    "<a href=\"https://www.youtube.com/intl/pt-BR/howyoutubeworks/product-features/search/\" "
                    "target=\"_blank\" rel=\"noopener noreferrer\">Como funciona a busca do YouTube</a>, o sistema olha "
                    "três coisas: relevância (o quanto o título, as tags, a descrição e o conteúdo do vídeo combinam com "
                    "o que foi pesquisado), engajamento (por exemplo, o tempo que as pessoas passam assistindo àquele "
                    "vídeo para aquela busca) e qualidade (sinais de que o canal mostra experiência, autoridade e "
                    "confiança no assunto).",
                    "Ou seja: não existe truque. O que dá para trabalhar é deixar claro, em texto, do que o vídeo trata, "
                    "planejar o tema para o vídeo responder de verdade o que a pessoa procurou e manter o canal coerente num "
                    "assunto. O YouTube também afirma que não aceita pagamento por posição na busca orgânica.",
                ],
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que o canal da empresa não cresce mesmo postando vídeo?",
                "ps": [
                    "O motivo mais comum é que o vídeo foi feito para quem já conhece a empresa, não para quem está "
                    "pesquisando. Título com o nome do evento, descrição vazia, nenhuma pista do assunto: o YouTube não "
                    "tem como saber para quem mostrar.",
                    "O outro motivo é falta de foco. Um vídeo sobre promoção, outro sobre a festa da equipe, outro sobre "
                    "um serviço: o canal não firma em nenhum assunto. Quando os vídeos respondem às perguntas que o "
                    "cliente faz antes de comprar, cada um vira uma porta de entrada.",
                ],
                "card_titulo": "Sinais de vídeo difícil de encontrar",
                "card": [
                    "Título que só faz sentido para quem é da empresa.",
                    "Descrição em branco ou com uma linha.",
                    "Vídeo longo sem capítulos.",
                    "Transcrição automática cheia de erros.",
                    "Miniatura que não mostra o assunto.",
                ],
            }),
            ("cards", {
                "tag": "O que está incluído",
                "titulo": "O que entra no SEO para YouTube?",
                "desc": "Cada item ajuda o YouTube, o Google e quem assiste a entender do que o vídeo trata.",
                "itens": [
                    ("Pesquisa de temas",
                     "Levantamento das perguntas que o seu cliente faz antes de contratar, para cada vídeo responder "
                     "uma delas."),
                    ("Título e descrição",
                     "O assunto na frente do título e uma descrição que resume o vídeo, com links para o site e para o "
                     "seu WhatsApp."),
                    ("Capítulos",
                     "O vídeo dividido em partes, com título em cada uma. Os "
                     "<a href=\"https://support.google.com/youtube/answer/9884579?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">capítulos</a>, segundo o YouTube, facilitam encontrar e rever cada "
                     "trecho."),
                    ("Transcrição revisada",
                     "O YouTube gera "
                     "<a href=\"https://support.google.com/youtube/answer/6373554?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">transcrição automática</a>, mas avisa que ela pode errar com sotaque, "
                     "ruído e termos técnicos. A revisão corrige nomes, serviços e termos do seu ramo."),
                    ("Miniatura",
                     "Uma imagem que diz do que o vídeo trata. A "
                     "<a href=\"https://support.google.com/youtube/answer/72431?hl=pt-BR\" target=\"_blank\" "
                     "rel=\"noopener noreferrer\">miniatura personalizada</a> exige conta verificada — eu oriento esse passo."),
                    ("Organização do canal",
                     "Playlists por assunto, descrição do canal e links, para quem chega por um vídeo assistir ao próximo."),
                ],
            }),
            ("texto", {
                "tag": "Google e IA",
                "titulo": "O vídeo também precisa ser entendido pelo Google e pelas ferramentas de IA?",
                "ps": [
                    "Precisa. Vídeo aparece também no Google — na página de resultados, na aba de vídeos e no Discover, "
                    "como explica o guia de "
                    "<a href=\"https://developers.google.com/search/docs/appearance/video?hl=pt-br\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">práticas recomendadas de SEO para vídeo</a> do próprio Google.",
                    "Na prática, buscadores e assistentes de inteligência artificial dependem muito do texto que "
                    "acompanha o vídeo — título, descrição, capítulos e transcrição — para entender o assunto e decidir "
                    "quando mostrar ou citar aquele conteúdo. Um vídeo excelente com texto pobre é um vídeo difícil de "
                    "encontrar. Por isso a transcrição revisada e a descrição bem escrita valem tanto quanto a gravação.",
                ],
            }),
            ("texto", {
                "tag": "Empresa local",
                "titulo": "Como o YouTube ajuda uma empresa local a conseguir clientes?",
                "ps": [
                    "Para a empresa local, o YouTube funciona como vitrine e como resposta pronta. Um vídeo explicando "
                    "como funciona o serviço, quanto tempo leva, como é a primeira consulta ou a visita técnica tira "
                    "dúvidas antes de o cliente chamar no WhatsApp — e ele chega mais decidido.",
                    "O mesmo vídeo pode ir para o site, numa página do serviço, e ajudar o "
                    "<a href=\"/google-perfil-empresa/\">Google Perfil da Empresa</a> a mostrar quem você é. Assim o "
                    "YouTube trabalha junto com o <a href=\"/consultoria-seo-local/\">SEO e o Google Meu Negócio</a>, em "
                    "vez de ser um canal solto.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o SEO do seu canal, do diagnóstico aos vídeos novos?",
                "itens": [
                    ("Diagnóstico do canal", "Olho os vídeos que já existem, os títulos, as descrições e o que dá para aproveitar."),
                    ("Mapa de temas", "Lista das perguntas do seu cliente que viram vídeo, na ordem de prioridade."),
                    ("Otimização dos vídeos antigos", "Títulos, descrições, capítulos e transcrições revistos nos que já estão no ar."),
                    ("Cada vídeo novo", "Antes de publicar: título, descrição, capítulos, transcrição e miniatura prontos."),
                    ("Acompanhamento", "Relatório do que as pessoas pesquisam para chegar ao canal e quais vídeos levam ao contato."),
                ],
            }),
            ("texto", {
                "tag": "Expectativa",
                "titulo": "Quanto tempo leva e o que dá para esperar do SEO para YouTube?",
                "ps": [
                    "O canal cresce com constância: vídeos que respondem a perguntas reais, publicados com regularidade, "
                    "vão sendo encontrados ao longo de meses. Um vídeo bem preparado pode continuar trazendo visita por "
                    "muito tempo depois de publicado.",
                    "O que não dá para prometer é número de inscritos ou de visualizações — isso depende do assunto, da "
                    "concorrência e do próprio vídeo. O que eu entrego é cada vídeo preparado para ser encontrado — título, "
                    "descrição, capítulos, transcrição e miniatura — e um relatório honesto do que está trazendo gente até você.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde o seu canal quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": 0,
                "itens": [
                    ("Arrumar o canal que já existe", "Para quem já tem vídeos que ninguém encontra.",
                     ["Diagnóstico do canal", "Títulos, descrições e capítulos revistos", "Transcrições corrigidas"],
                     "Olá, Renan! Quero arrumar o SEO do canal do YouTube que já tenho.", "Pedir orçamento"),
                    ("Otimização de cada vídeo novo", "Para quem vai publicar com frequência.",
                     ["Tema pelo que o cliente pesquisa", "Título, descrição e capítulos", "Miniatura orientada"],
                     "Olá, Renan! Quero otimização para cada vídeo novo do meu canal.", "Pedir orçamento"),
                    ("Canal + site + Google Meu Negócio", "Para usar o YouTube junto com o resto da presença no Google.",
                     ["SEO do canal", "Vídeos nas páginas do site", "Ligação com o Google Meu Negócio"],
                     "Olá, Renan! Quero integrar meu canal do YouTube com o site e o Google Meu Negócio.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("O que é SEO para YouTube?",
             "É preparar cada vídeo para ser encontrado por quem pesquisa o assunto: tema escolhido pelo que o "
             "cliente pergunta, título, descrição, capítulos, transcrição revisada e miniatura."),
            ("Vocês garantem um número de inscritos ou visualizações?",
             "Não. Ninguém controla quantas pessoas vão assistir. O trabalho é deixar o vídeo fácil de encontrar e de "
             "entender, e mostrar em relatório o que está trazendo gente até você."),
            ("O serviço inclui gravar e editar os vídeos?",
             "Este serviço cuida de o seu vídeo ser encontrado: tema, título, descrição, capítulos, transcrição e "
             "miniatura. A gravação e a edição ficam com você ou com um editor de sua confiança."),
            ("Preciso ter muitos vídeos para começar?",
             "Não. Dá para começar arrumando os vídeos que já existem e planejando os próximos a partir das perguntas "
             "que o seu cliente faz."),
            ("Preciso de conta verificada no YouTube?",
             "Para usar miniatura personalizada, sim — é uma exigência do YouTube. Eu oriento como fazer a verificação."),
            ("Quanto custa o SEO para YouTube?",
             "Depende de quantos vídeos entram e se é arrumação do canal ou acompanhamento dos vídeos novos. O "
             "orçamento é individual, grátis e sai em até 24 horas pelo WhatsApp."),
            ("Existe fidelidade?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento."),
        ],
        "relacionados": [
            ("/consultoria-seo-local/", "SEO e Google Meu Negócio",
             "Aparecer no Google e no mapa, junto com o canal."),
            ("/google-perfil-empresa/", "Google Perfil da Empresa",
             "O perfil que mostra a sua empresa no Google Maps."),
            ("/conteudo-para-seo/", "Conteúdo para SEO",
             "Textos que respondem às dúvidas do cliente e ajudam a escolher os temas dos vídeos."),
        ],
        "cta_final": ("Me mande o link do seu canal. Eu te digo o que dá para melhorar primeiro.",
                      "Sem compromisso: eu olho os títulos, as descrições e os temas, e te mostro por onde começar."),
    },
    {
        # Etapa 6 do plano de nichos (04/10/2026): pagina principal do nicho LIMPEZA EMPRESARIAL E
        # TERCEIRIZACAO. Publico: o DONO da empresa de limpeza (regra de ouro). Fontes conferidas:
        # ajuda do Perfil da Empresa (area de cobertura), Lei 6.019/1974 (redacao da Lei 13.429/2017),
        # IBGE/Concla CNAE 8121-4/00 e CNPJ publico (jun/2026).
        "slug": "marketing-para-empresa-de-limpeza",
        "nacional": True,
        "data": "2026-10-04",
        "publico": "Empresas de limpeza, conservação e terceirização de serviços",
        "title": "Marketing para Empresa de Limpeza e Terceirização | RCB SEO",
        "desc": ("Marketing para empresas de limpeza e terceirização: Google Meu Negócio, site e Google Ads para "
                 "fechar contratos com condomínios e empresas. Orçamento em 24h."),
        "trilha": "Marketing para empresa de limpeza",
        "servico": "Marketing para empresas de limpeza e terceirização",
        "eyebrow": "Para empresas de limpeza de todo o Brasil",
        "h1": "Marketing e SEO para empresas de limpeza e terceirização",
        "sub": ("Marketing para empresa de limpeza é fazer o síndico, o gestor de condomínio e o dono de empresa "
                "encontrarem você quando procuram quem cuide da limpeza — e transformar essa busca num pedido de "
                "proposta. Eu cuido do Google Meu Negócio, do site com páginas por serviço e do anúncio no Google, "
                "com foco no que sustenta a empresa: o contrato mensal. Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero mais pedidos de proposta",
        "msg": "Olá, Renan! Tenho uma empresa de limpeza e quero fechar mais contratos pelo Google.",
        "pills": ["Orçamento em até 24h", "Foco em contrato mensal", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Google Meu Negócio com área de atendimento.",
            "Site com página para cada tipo de serviço.",
            "Página para condomínios e outra para empresas.",
            "Google Ads para quem procura terceirizar.",
            "Formulário de pedido de proposta e WhatsApp.",
            "Medição de cada pedido recebido.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para empresa de limpeza",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que a empresa de limpeza vive de indicação e perde contrato para o concorrente?",
                "ps": [
                    "A maioria dos contratos de limpeza começa com alguém da administração pesquisando no Google ou "
                    "pedindo indicação a um conhecido. Quem depende só da indicação fica sem chance quando o síndico "
                    "novo ou o gerente de outra empresa vai direto ao Google — e encontra o concorrente.",
                    "O mercado é disputado. Pelos dados públicos de CNPJ de junho de 2026, o código "
                    "<a href=\"https://cnae.ibge.gov.br/?subclasse=8121400&amp;tipo=cnae&amp;versao=10&amp;view=subclasse\" "
                    "target=\"_blank\" rel=\"noopener noreferrer\">8121-4/00 (Limpeza em prédios e em domicílios)</a> "
                    "reunia 15.874 empresas ativas, e o de serviços combinados de apoio a edifícios (8111-7/00), mais "
                    "18.169. Quem aparece primeiro e passa confiança chega antes à mesa de negociação.",
                ],
                "card_titulo": "Sinais de que falta marketing na empresa de limpeza",
                "card": [
                    "Contratos que entram só por indicação.",
                    "Perfil do Google com endereço errado ou sem avaliações.",
                    "Site com uma página só, sem separar serviços.",
                    "Nenhum material para mandar junto com a proposta.",
                    "Ninguém sabe de onde veio o último contrato.",
                ],
            }),
            ("texto", {
                "tag": "Contrato mensal",
                "titulo": "Por que o marketing da empresa de limpeza precisa mirar o contrato mensal?",
                "ps": [
                    "Faxina avulsa paga a semana; contrato mensal paga a empresa. Um condomínio ou um escritório que "
                    "fecha com você costuma ficar por muito tempo, se o serviço for bom — e cada contrato desses vale "
                    "dezenas de faxinas. Por isso o marketing precisa falar com quem decide esse contrato: síndico, "
                    "administradora de condomínio, gerente administrativo, dono de empresa.",
                    "Isso muda tudo: as páginas do site, as palavras do anúncio e até o texto do perfil no Google. Em "
                    "vez de \"faxina barata\", a comunicação fala de rotina, equipe uniformizada, supervisão, "
                    "reposição de faltas e relatório — o que um gestor quer ler antes de pedir proposta.",
                ],
            }),
            ("texto", {
                "tag": "Google Meu Negócio",
                "titulo": "Como a empresa de limpeza aparece no Google Maps se atende no endereço do cliente?",
                "ps": [
                    "Empresa de limpeza é o exemplo que o próprio Google usa: na ajuda do Perfil da Empresa sobre "
                    "<a href=\"https://support.google.com/business/answer/9157481?hl=pt-BR\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">áreas de cobertura</a>, os \"prestadores de serviços de limpeza\" "
                    "aparecem como empresa de serviço local — que vai até o cliente. Nesse caso, o perfil mostra a "
                    "área atendida, e o Google orienta remover o endereço se você não recebe clientes nele.",
                    "Configurar isso certo evita dois problemas: aparecer num endereço onde ninguém atende e ficar "
                    "fora das buscas dos bairros e cidades que você realmente cobre. Com o perfil completo — serviços, "
                    "fotos da equipe em ação (com autorização dos clientes) e avaliações respondidas — a empresa passa "
                    "a aparecer para quem procura na região. Veja a "
                    "<a href=\"/google-perfil-empresa/\">otimização do Google Perfil da Empresa</a>.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de uma empresa de limpeza?",
                "desc": "As frentes que trazem pedido de proposta. Dá para começar por uma e somar as outras.",
                "itens": [
                    ("Google Meu Negócio",
                     "Área de atendimento configurada, serviços, fotos da equipe e rotina de avaliações de clientes "
                     "satisfeitos."),
                    ("Site com páginas por serviço",
                     "Limpeza de condomínio, de escritório, pós-obra, terceirização de equipe: cada serviço com a sua "
                     "página, respondendo o que o gestor quer saber."),
                    ("Página para condomínios",
                     "O síndico decide em assembleia e compara propostas. A página explica rotina, supervisão e como "
                     "funciona a reposição quando alguém falta."),
                    ("Google Ads",
                     "Anúncio na pesquisa do Google para quem já procura terceirizar a limpeza, com as buscas de vaga "
                     "de emprego bloqueadas. Veja a <a href=\"/gestao-de-trafego-pago/\">gestão de tráfego pago</a>."),
                    ("Pedido de proposta",
                     "Formulário curto (com aviso de LGPD) e WhatsApp, pedindo o que você precisa para calcular: "
                     "metragem, frequência, número de pessoas."),
                    ("Medição",
                     "Cada pedido de proposta registrado, para saber qual canal traz contrato."),
                ],
            }),
            ("texto", {
                "tag": "Terceirização",
                "titulo": "Como falar de terceirização de limpeza sem assustar o cliente?",
                "ps": [
                    "Quem contrata terceirização quer segurança: saber que a empresa cumpre as obrigações com a equipe e "
                    "que o problema trabalhista não vai cair no colo dele. A relação entre a empresa de prestação de "
                    "serviços e quem contrata é regulada pela "
                    "<a href=\"https://www.planalto.gov.br/ccivil_03/leis/l6019.htm\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">Lei 6.019/1974</a>, com a redação dada pela Lei 13.429/2017.",
                    "O marketing não substitui o contrato nem a orientação jurídica, mas pode mostrar com clareza como "
                    "a sua empresa trabalha: registro da equipe, supervisão, substituição de faltas e documentação "
                    "disponível para o contratante conferir. Esse tipo de transparência pesa mais na decisão do gestor "
                    "do que qualquer promessa de preço baixo.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing da sua empresa de limpeza, do diagnóstico aos contratos?",
                "itens": [
                    ("Diagnóstico", "Olho seu perfil no Google, o site e quem aparece antes de você nas suas cidades."),
                    ("Plano por escrito", "Em até 24 horas: as frentes para começar, o que entra e o valor de cada uma."),
                    ("Perfil e site", "Área de atendimento, páginas por serviço e a página para condomínios e empresas."),
                    ("Anúncio, se fizer sentido", "Campanha no Google para quem procura terceirizar a limpeza."),
                    ("Medição", "Relatório de pedidos de proposta por canal."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa de limpeza quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa da região", "Para quem ainda depende só de indicação.",
                     ["Google Meu Negócio com área de atendimento", "Serviços e fotos", "Rotina de avaliações"],
                     "Olá, Renan! Tenho empresa de limpeza e quero aparecer no Google Maps.", "Pedir orçamento"),
                    ("Site para fechar contrato", "Para ser encontrado por síndicos e empresas.",
                     ["Páginas por serviço", "Página para condomínios", "Pedido de proposta"],
                     "Olá, Renan! Quero um site para a minha empresa de limpeza fechar contratos.", "Pedir orçamento"),
                    ("Anúncio no Google", "Para quem quer pedidos de proposta agora.",
                     ["Google Ads para terceirização", "Página de pedido de proposta", "Medição dos pedidos"],
                     "Olá, Renan! Quero anunciar a minha empresa de limpeza no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Empresa de limpeza precisa de site?",
             "Para fechar contrato com condomínio e empresa, ajuda muito. O gestor costuma pesquisar antes de pedir "
             "proposta, e um site com os serviços explicados passa a segurança que a indicação sozinha não passa."),
            ("Devo colocar meu endereço no Google Meu Negócio?",
             "Só se você recebe clientes nele. Para quem vai até o cliente, o Google orienta usar a área de cobertura e "
             "remover o endereço do perfil."),
            ("Vale a pena anunciar limpeza no Google Ads?",
             "Vale para buscas de quem quer terceirizar ou contratar limpeza de condomínio e escritório. O cuidado é "
             "bloquear as buscas de vaga de emprego, que são muitas nesse ramo."),
            ("Como conseguir contrato com condomínio?",
             "Estar no Google quando o síndico pesquisa, ter uma página que explique a rotina e a supervisão, e mandar "
             "uma proposta clara. Os detalhes estão no artigo sobre como conseguir clientes para empresa de limpeza."),
            ("Quanto custa o marketing para empresa de limpeza?",
             "Depende das frentes que entram e de quantas cidades você atende. O orçamento é individual, grátis e sai "
             "em até 24 horas pelo WhatsApp. A verba de anúncio, quando houver, é paga direto ao Google."),
            ("Existe fidelidade?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento."),
        ],
        "relacionados": [
            ("/blog/como-conseguir-clientes-para-empresa-de-limpeza/", "Como conseguir clientes para empresa de limpeza",
             "Condomínios, empresas e a proposta que fecha contrato."),
            ("/blog/como-divulgar-empresa-de-limpeza/", "Como divulgar empresa de limpeza",
             "Ideias práticas de divulgação para o dono da empresa."),
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago",
             "Anúncio no Google para quem procura terceirizar a limpeza."),
        ],
        "cta_final": ("Me conte as cidades que você atende e o tipo de cliente. Eu te digo por onde começar.",
                      "Sem compromisso: eu olho como a sua empresa aparece hoje no Google e quem aparece antes de você."),
    },
    {
        # Etapa 8 do plano de nichos (05/10/2026): pagina principal de ADVOCACIA. Substitui a antiga
        # /marketing-para-advogados/ (escrita a mao, criada em 15/07/2026) e recebe o 301 de
        # /para-advogados/, que era quem aparecia para "seo para advogados" — por isso o termo SEO fica
        # no title, no H1 e num H2. Fonte dos fatos: Provimento 205/2021 do CFOAB (texto oficial no site
        # da OAB), lido em 05/10/2026. O Renan e bacharel em Direito, NAO advogado: nunca escrever o contrario.
        "slug": "marketing-para-advogados",
        "nacional": True,
        "data": "2026-10-05",
        "publicado": "2026-07-15",
        "publico": "Advogados e escritórios de advocacia",
        "title": "Marketing e SEO para Advogados nas Normas da OAB | RCB SEO",
        "desc": ("Marketing e SEO para advogados dentro do Provimento 205/2021 da OAB: Google Meu Negócio, site por "
                 "área de atuação e Google Ads. Orçamento grátis em 24h."),
        "trilha": "Marketing para advogados",
        "servico": "Marketing jurídico e SEO para advogados",
        "eyebrow": "Para advogados de todo o Brasil",
        "h1": "Marketing e SEO para advogados: seja encontrado por quem procura, dentro da OAB",
        "sub": ("Marketing para advogados é fazer o escritório aparecer quando alguém pesquisa o próprio problema no "
                "Google — \"advogado trabalhista\", \"divórcio consensual\", \"aposentadoria negada\" — com "
                "informação sóbria, do jeito que o Provimento 205/2021 da OAB permite. Eu cuido do Google Meu "
                "Negócio, do site com uma página por área de atuação e, quando faz sentido, do anúncio no Google. "
                "Sou bacharel em Direito. Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero ser encontrado no Google",
        "msg": "Olá, Renan! Sou advogado(a) e quero que o meu escritório seja encontrado no Google dentro das normas da OAB.",
        "pills": ["Orçamento em até 24h", "Dentro do Provimento 205/2021", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing do escritório",
        "painel": [
            "Google Meu Negócio do escritório completo.",
            "Site com uma página por área de atuação.",
            "Artigos que explicam direitos, sem captação.",
            "Google Ads para quem já pesquisa o problema.",
            "WhatsApp e formulário com aviso de LGPD.",
            "Medição de cada contato recebido.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing e SEO para advogados",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que é tão difícil conseguir clientes novos na advocacia?",
                "ps": [
                    "Loja faz promoção e clínica faz campanha; o advogado não pode. A publicidade da advocacia tem "
                    "regra própria, e muito escritório conclui que não há nada a fazer — e fica só na indicação. "
                    "Quando o boca a boca para de crescer, a carteira para junto.",
                    "Enquanto isso, a pessoa com um problema jurídico pesquisa no Google antes de ligar para qualquer "
                    "um. Até o cliente indicado procura o nome do escritório antes da primeira conversa. O que ele "
                    "encontra — ou não encontra — pesa na decisão.",
                ],
                "card_titulo": "Sinais de que o escritório está invisível no Google",
                "card": [
                    "Clientes novos chegam só por indicação.",
                    "Perfil no Google sem fotos, horário ou avaliações.",
                    "Site com uma página só, \"atuação em todas as áreas\".",
                    "Instagram com curtidas de colegas, não de clientes.",
                    "Ninguém sabe de onde veio o último cliente.",
                ],
            }),
            ("texto", {
                "tag": "O que a OAB permite",
                "titulo": "O que o Provimento 205/2021 da OAB permite no marketing jurídico?",
                "ps": [
                    "O <a href=\"https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021\" target=\"_blank\" "
                    "rel=\"noopener noreferrer\">Provimento 205/2021</a> do Conselho Federal da OAB começa dizendo que "
                    "o marketing jurídico é permitido (art. 1º), desde que compatível com o Código de Ética. Ele "
                    "também define o marketing de conteúdos jurídicos: criar e divulgar conteúdo para informar o "
                    "público e consolidar o nome do advogado ou do escritório (art. 2º, II).",
                    "Um ponto ajuda muito quem quer aparecer no Google: o Provimento chama de publicidade passiva a "
                    "divulgação que atinge \"somente público certo que tenha buscado informações\" sobre o anunciante "
                    "ou o tema (art. 2º, VII). É exatamente o que acontece quando alguém pesquisa o próprio problema "
                    "e encontra a página do seu escritório.",
                    "O limite também está escrito: a publicidade profissional deve ser informativa, discreta e sóbria, "
                    "sem captação de clientela nem mercantilização. O art. 3º veda, entre outras coisas, falar de "
                    "honorários, gratuidade ou descontos como forma de captar cliente, anunciar especialidade sem "
                    "título e usar expressões persuasivas, de autoengrandecimento ou de comparação. E o art. 6º "
                    "proíbe prometer resultado ou usar casos concretos para oferecer serviço.",
                    "Uma observação honesta: sou bacharel em Direito, não advogado. Este resumo não substitui a "
                    "leitura do Provimento nem a orientação da sua seccional — mas é com ele aberto que cada página "
                    "do escritório é escrita.",
                ],
            }),
            ("texto", {
                "tag": "SEO para advogados",
                "titulo": "Como o SEO para advogados faz o escritório aparecer quando o cliente pesquisa?",
                "ps": [
                    "SEO é o trabalho de organizar o escritório no Google para que ele apareça de graça, sem pagar por "
                    "clique, nas buscas de quem tem o problema que você resolve. Para advocacia, são três peças.",
                    "A primeira é o <a href=\"/google-perfil-empresa/\">Google Meu Negócio</a> do escritório: nome, "
                    "endereço, horário, fotos e áreas de atuação completos — é ele que aparece no mapa quando alguém "
                    "procura advogado na região. A segunda é o site com uma página para cada área: trabalhista, "
                    "família, previdenciário, cada uma respondendo o que as pessoas perguntam sobre o tema. A terceira "
                    "é o conteúdo informativo, que o próprio Provimento chama de marketing de conteúdos jurídicos.",
                    "O resultado não é imediato: costuma levar alguns meses para firmar, e depende da concorrência na "
                    "sua cidade e na sua área. Em troca, não some no dia em que a verba de anúncio acaba.",
                ],
            }),
            ("texto", {
                "tag": "Anúncio",
                "titulo": "Advogado pode anunciar no Google Ads?",
                "ps": [
                    "Pode, com regra. O Anexo Único do Provimento 205/2021 permite a \"aquisição de palavra-chave a "
                    "exemplo do Google Ads\" quando o anúncio responde a uma busca iniciada pelo potencial cliente e "
                    "as palavras escolhidas respeitam a ética — e proíbe anúncios ostensivos em plataformas de vídeo.",
                    "Na prática, o anúncio aparece para quem pesquisou \"advogado previdenciário\" e leva para a página "
                    "daquela área, com texto informativo e sem promessa. Já o impulsionamento nas redes sociais é "
                    "permitido pelo mesmo Anexo desde que não contenha oferta de serviços jurídicos. Os detalhes estão "
                    "em <a href=\"/trafego-pago-para-advogados/\">tráfego pago para advogados</a>.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing e no SEO do escritório?",
                "desc": "As frentes que fazem o escritório ser encontrado. Dá para começar por uma e somar as outras.",
                "itens": [
                    ("Google Meu Negócio",
                     "Perfil completo do escritório, com fotos (permitidas pelo art. 5º, § 2º), horário e áreas de "
                     "atuação, para aparecer no mapa da região."),
                    ("Site por área de atuação",
                     "Uma página para cada área, com o que a pessoa precisa saber antes de procurar um advogado. Veja "
                     "a <a href=\"/criacao-de-site-para-advogado/\">criação de site para advogado</a>."),
                    ("Conteúdo informativo",
                     "Artigos que explicam direitos e prazos em linguagem simples, sem caso concreto, valor ou "
                     "promessa de resultado."),
                    ("Google Ads",
                     "Anúncio na pesquisa do Google para quem já procura a sua área, levando para a página certa."),
                    ("Contato e LGPD",
                     "WhatsApp e formulário curto com aviso de privacidade, para o primeiro contato chegar organizado."),
                    ("Medição",
                     "Cada contato registrado, para saber qual área e qual canal trazem cliente."),
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing do seu escritório, do diagnóstico ao relatório?",
                "itens": [
                    ("Diagnóstico", "Olho o perfil do escritório no Google, o site e quem aparece antes de você."),
                    ("Plano por escrito", "Em até 24 horas: as frentes para começar, o que entra e o valor de cada uma."),
                    ("Perfil e site", "Perfil completo e páginas por área de atuação, revisadas com o Provimento aberto."),
                    ("Anúncio, se fizer sentido", "Campanha no Google para as áreas que você quer fazer crescer."),
                    ("Relatório", "Contatos recebidos por área e por canal, todo mês."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde o seu escritório quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa da região", "Para quem depende só de indicação.",
                     ["Google Meu Negócio completo", "Fotos e áreas de atuação", "Rotina de avaliações"],
                     "Olá, Renan! Sou advogado(a) e quero que o escritório apareça no Google Maps.", "Pedir orçamento"),
                    ("Site por área de atuação", "Para ser encontrado por quem pesquisa o problema.",
                     ["Uma página por área", "Conteúdo informativo", "WhatsApp e formulário"],
                     "Olá, Renan! Quero um site para o meu escritório de advocacia.", "Pedir orçamento"),
                    ("Anúncio no Google", "Para quem quer contatos de uma área agora.",
                     ["Google Ads por área", "Página da área de atuação", "Medição dos contatos"],
                     "Olá, Renan! Quero anunciar o meu escritório de advocacia no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Advogado pode fazer marketing?",
             "Pode. O art. 1º do Provimento 205/2021 da OAB permite o marketing jurídico, desde que compatível com o "
             "Código de Ética: informativo, discreto e sóbrio, sem captação de clientela nem mercantilização."),
            ("Posso divulgar que a primeira consulta é gratuita?",
             "O art. 3º, I, do Provimento veda a referência a valores de honorários, forma de pagamento, gratuidade ou "
             "descontos como forma de captar clientes. Por isso as páginas do escritório não falam de preço nem de "
             "consulta grátis."),
            ("Posso me apresentar como especialista no site?",
             "Só se tiver título certificado ou notória especialização: o art. 3º, III, veda anunciar especialidade "
             "sem isso. Sem título, a página fala em área de atuação."),
            ("Funciona para advogado solo ou recém-formado?",
             "Funciona, porque a disputa no Google acontece por área de atuação e por região, não pelo tamanho do "
             "escritório. Um perfil completo e páginas claras por área já colocam o advogado na disputa."),
            ("Você é advogado?",
             "Não. Sou bacharel em Direito e consultor de SEO. Conheço o Provimento e escrevo com ele aberto, mas a "
             "responsabilidade pela publicidade é de quem está inscrito na OAB, como diz o próprio art. 1º, § 1º."),
            ("Quanto custa o marketing para advogados?",
             "Depende das frentes que entram, das áreas de atuação e da concorrência na sua cidade. O orçamento é "
             "individual, grátis e sai em até 24 horas pelo WhatsApp. A verba de anúncio, quando houver, é paga direto "
             "ao Google."),
            ("Existe fidelidade?",
             "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
             "vão por escrito junto com o orçamento."),
        ],
        "relacionados": [
            ("/blog/como-conseguir-clientes-na-advocacia/", "Como conseguir clientes na advocacia",
             "Os caminhos permitidos, do perfil no Google à indicação."),
            ("/blog/advogado-pode-fazer-marketing/", "Advogado pode fazer marketing?",
             "O que o Provimento 205/2021 permite e o que proíbe."),
            ("/trafego-pago-para-advogados/", "Tráfego pago para advogados",
             "Google Ads por área de atuação, dentro da OAB."),
            ("/criacao-de-site-para-advogado/", "Site para advogado",
             "Uma página para cada área de atuação."),
        ],
        "cta_final": ("Me conte as áreas do seu escritório e a cidade. Eu te digo por onde começar.",
                      "Sem compromisso: eu olho como o escritório aparece hoje no Google e quem aparece antes de você."),
    },
]
