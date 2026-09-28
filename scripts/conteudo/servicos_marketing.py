# -*- coding: utf-8 -*-
"""
Conteúdo das páginas de serviço da linha "Sites e Anúncios" (28/09/2026).

  /criacao-de-landing-page-goiania/
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
        "slug": "criacao-de-landing-page-goiania",
        "title": "Criação de Landing Page em Goiânia | Orçamento Grátis",
        "desc": ("Criação de landing page em Goiânia que transforma clique de anúncio em conversa no "
                 "WhatsApp. Página rápida, texto que vende e orçamento grátis em 24h."),
        "trilha": "Criação de landing page em Goiânia",
        "servico": "Criação de landing page",
        "eyebrow": "Goiânia e todo o Brasil",
        "h1": "Criação de landing page em Goiânia",
        "sub": ("Você paga por cada clique do anúncio. Se a pessoa cai numa página lenta, confusa ou genérica, "
                "ela volta para o Google e o dinheiro vai junto. Eu crio a landing page que recebe esse clique "
                "e leva a pessoa direto para a conversa com você no WhatsApp."),
        "cta_hero": "Quero minha landing page",
        "msg": "Olá, Renan! Quero um orçamento de landing page.",
        "pills": ["Orçamento em até 24h", "Feita para anúncio", "Garantia de 30 dias"],
        "painel_h2": "O que vem na sua landing page",
        "painel": [
            "Uma oferta só, sem distração.",
            "Texto escrito para convencer quem chega do anúncio.",
            "Botão de WhatsApp com mensagem pronta.",
            "Rápida no celular, onde está quase todo clique.",
            "Pronta para Google Ads e Meta Ads.",
            "Registro de cada contato que chegou.",
        ],
        "secoes": [
            ("split", {
                "tag": "O problema",
                "titulo": "Anúncio bom caindo em página ruim é dinheiro jogado fora",
                "ps": [
                    "A cena é comum em Goiânia: a empresa começa a anunciar, os cliques chegam, o relatório mostra "
                    "gente entrando — e o WhatsApp continua quieto. Quase nunca o culpado é o anúncio. É a página "
                    "que recebe o clique.",
                    "Mandar o anúncio para a página inicial do site é o erro mais caro. Ali a pessoa encontra dez "
                    "assuntos, menu, blog, fotos da equipe — e nenhuma resposta direta para o que ela clicou. Ela "
                    "não procura; ela volta.",
                    "A landing page existe para o contrário: uma página, uma oferta, um próximo passo. Quem clicou "
                    "em \"implante dentário\" lê sobre implante e vê o botão para falar com você. Só isso.",
                ],
                "card_titulo": "Sinais de que a sua página está perdendo gente",
                "card": [
                    "<strong>Muitos cliques, poucas mensagens.</strong> O anúncio funciona; a página não.",
                    "<strong>O anúncio leva para a página inicial.</strong> A pessoa não acha o que clicou.",
                    "<strong>Demora para abrir no celular.</strong> Cada segundo a mais é gente indo embora.",
                ],
            }),
            ("cards", {
                "tag": "O que está incluído",
                "titulo": "O que entra na criação da sua landing page",
                "desc": "Não é um modelo pronto com a sua logo em cima. É uma página pensada para uma oferta e um público.",
                "itens": [
                    ("Texto que vende", "Título que responde ao anúncio, benefícios na língua do seu cliente, "
                     "respostas às dúvidas que travam a decisão e chamada clara para a ação."),
                    ("Uma oferta, um caminho", "Sem menu e sem distração. A pessoa só tem uma coisa para fazer: "
                     "falar com você."),
                    ("WhatsApp com mensagem pronta", "O botão já abre a conversa com o assunto escrito. Você sabe "
                     "de qual campanha a pessoa veio antes de responder."),
                    ("Rápida no celular", "Página leve, sem excesso de efeito. Quase todo clique de anúncio vem do "
                     "celular, muitas vezes com internet ruim."),
                    ("Pronta para anúncio", "Estrutura preparada para Google Ads e Meta Ads, com a página certa "
                     "para cada campanha em vez de uma página para tudo."),
                    ("Contatos medidos", "Cada clique no WhatsApp fica registrado. Você enxerga quanto cada "
                     "campanha trouxe de conversa, e não só de clique."),
                ],
            }),
            ("cards", {
                "tag": "Para quem",
                "titulo": "Quando uma landing page faz mais sentido do que um site",
                "itens": [
                    ("Você vai anunciar", "Campanha no Google ou no Instagram precisa de uma página que converta. "
                     "É o uso mais comum — e o que mais dá retorno."),
                    ("Você tem um serviço carro-chefe", "Implante, harmonização, planejamento tributário, "
                     "energia solar: um serviço que merece página própria e uma oferta clara."),
                    ("Você tem um lançamento ou evento", "Curso, turma nova, promoção de temporada. Página com "
                     "começo, meio e fim, que depois pode ser reaproveitada."),
                ],
            }),
            ("faixas", {
                "titulo": "Quanto custa uma landing page?",
                "desc": ("Depende do tamanho da oferta, de quem escreve o texto e do que a página precisa fazer. "
                         "No mercado, uma landing page vai de algumas centenas de reais a alguns milhares — e a "
                         "diferença costuma estar no texto, que é o que convence."),
                "itens": [
                    ("Modelo pronto", "Algumas centenas de reais. Página montada sobre um modelo, texto genérico. "
                     "Serve para testar, raramente para escalar anúncio."),
                    ("Página sob medida", "Faixa de alguns milhares de reais. Texto escrito para o seu público, "
                     "estrutura pensada para a sua oferta e medição de contatos."),
                    ("Várias páginas para campanhas", "Projeto maior: uma página por serviço ou por público, "
                     "cada campanha com a sua. É o que separa quem anuncia de quem anuncia com lucro."),
                ],
            }),
            ("orcamento", {
                "titulo": "Sua landing page sob medida: quanto fica o seu projeto?",
                "desc": ("Escolha o tipo de página e me chame no WhatsApp. Em até 24 horas você recebe o valor "
                         "exato — e, de brinde, eu olho como estão os anúncios dos seus concorrentes."),
                "itens": [
                    ("Página para anúncio no Google", "Para quem vai aparecer quando o cliente pesquisa o serviço.",
                     ["Texto que responde à busca", "Botão de WhatsApp com mensagem pronta", "Rápida no celular"],
                     "Olá, Renan! Quero um orçamento de landing page para anúncio no Google.", "Orçamento da minha página"),
                    ("Página para Instagram e Facebook", "Para quem anuncia para quem ainda não conhece o serviço.",
                     ["Oferta clara logo no topo", "Prova e respostas às objeções", "Pronta para Meta Ads"],
                     "Olá, Renan! Quero um orçamento de landing page para anúncio no Instagram.", "Quero vender pelo Instagram"),
                    ("Página do serviço carro-chefe", "Para o serviço que mais dá dinheiro ganhar página própria.",
                     ["Uma oferta, um caminho", "Serve para anúncio e para o Google", "Contatos medidos"],
                     "Olá, Renan! Quero uma landing page para o meu serviço principal.", "Orçamento do meu serviço"),
                    ("Página + gestão do anúncio", "Para quem quer a página e a campanha no mesmo lugar.",
                     ["Página e anúncio pensados juntos", "Google Ads ou Meta Ads", "Acompanhamento dos contatos"],
                     "Olá, Renan! Quero um orçamento de landing page com gestão de anúncios.", "Quero página + anúncio"),
                ],
                "destaque": 3,
            }),
            ("passos", {
                "titulo": "Como é criar a sua landing page",
                "itens": [
                    ("1. Me conte a oferta", "No WhatsApp: o que você vende, para quem e onde vai anunciar. Sem formulário longo."),
                    ("2. Eu escrevo e monto", "Texto e página prontos para você conferir antes de publicar."),
                    ("3. Publicamos e medimos", "Página no ar, ligada ao anúncio, com cada contato registrado."),
                ],
            }),
        ],
        "faq": [
            ("Quanto custa criar uma landing page?",
             "Depende do tamanho da oferta, de quem escreve o texto e do que a página precisa fazer. No mercado, "
             "vai de algumas centenas de reais, em modelo pronto, a alguns milhares, em página sob medida. Na RCB "
             "o orçamento é grátis e sai em até 24 horas pelo WhatsApp."),
            ("Qual a diferença entre landing page e site?",
             "O site apresenta a empresa inteira e tem várias páginas. A landing page tem um objetivo só — "
             "geralmente receber quem clicou num anúncio e levar para o contato. Muitas empresas precisam dos "
             "dois: o site para ser encontrado no Google e a landing page para as campanhas."),
            ("Landing page funciona sem anúncio?",
             "Funciona, principalmente quando é a página de um serviço específico e está bem escrita para o Google. "
             "Mas o uso mais comum é com anúncio, porque é onde cada clique custa dinheiro e a conversão pesa mais."),
            ("Em quanto tempo a landing page fica pronta?",
             "Em geral, poucos dias depois de você me mandar as informações da oferta. O que costuma atrasar não é "
             "a montagem, é o material — fotos, depoimentos e detalhes do serviço."),
            ("Vocês cuidam do anúncio também?",
             "Sim. A RCB faz a gestão de tráfego pago no Google Ads e no Meta Ads. Quando a página e o anúncio são "
             "pensados juntos, a mensagem do anúncio continua na página e a conversa chega mais qualificada."),
            ("A página é minha depois de pronta?",
             "É. O domínio e o conteúdo ficam no seu nome. Se um dia você trocar de fornecedor, leva tudo junto."),
        ],
        "relacionados": [
            ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Google Ads e Meta Ads para levar gente até a sua página."),
            ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Quando a empresa precisa do site completo, não só de uma página."),
            ("/blog/quanto-custa-um-site/", "Quanto custa um site", "As faixas de preço do mercado e o que muda o valor."),
        ],
        "cta_final": ("Me conte a sua oferta. Eu te digo como transformar clique em conversa.",
                      "Sem compromisso: você me diz o que vende e onde vai anunciar, e eu te mostro o caminho mais curto até o WhatsApp."),
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
                    "<a href=\"/criacao-de-landing-page-goiania/\">página que recebe o clique</a>. Anúncio bom "
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
            ("/criacao-de-landing-page-goiania/", "Criação de landing page", "A página que transforma o clique do anúncio em conversa."),
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
        "pills": ["Orçamento em até 24h", "Pagamento e frete prontos", "Garantia de 30 dias"],
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
