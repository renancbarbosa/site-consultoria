# -*- coding: utf-8 -*-
"""
Conteúdo das páginas de serviço da linha "Sites e Anúncios" (28/09/2026).

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
]
