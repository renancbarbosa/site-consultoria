# -*- coding: utf-8 -*-
"""
Conteudo da pagina /google-meu-negocio-goiania/ (auditoria de 09/11/2026, item 6).

Por que existe: o servico central da RCB (Google Meu Negocio) so tinha paginas nacionais
(/google-perfil-empresa/) ou de clinicas. No Search Console (90 dias ate 06/11/2026) as buscas
"google meu negocio goiania" e parecidas tiveram ZERO impressao: nao havia pagina para elas.

Divisao de termos (nao canibalizar):
  * /google-meu-negocio-goiania/  -> Google Meu Negocio / perfil no Google / Google Maps EM GOIANIA
  * /google-perfil-empresa/       -> o mesmo servico, nacional
  * /seo-local-goiania/           -> SEO local (site + perfil) em Goiania
  * /consultor-seo-goiania/       -> o profissional (PROTEGIDA)

Regras (nao afrouxar):
  * SEM PRECO da RCB. Nenhuma promessa de posicao ou prazo para aparecer.
  * Explica o QUE e o POR QUE, nunca o COMO (decisao do Renan, 29/10/2026). Caixa "ajuda"
    chama para o WhatsApp no meio do texto.
  * Numeros de case so os verificados em /cases/ (Docevidade: 1o no Maps para "macarrons
    Goiania" com 4 avaliacoes, a frente de concorrentes com 47 e 312).
  * Nada de pratica proibida pelo Google: palavra-chave no nome do perfil, avaliacao comprada,
    endereco falso. A pagina diz isso com todas as letras.

Gerador: scripts/gerar-gmn-goiania.py (mesmo invólucro das paginas de servico).
"""

DATA = "2026-11-09"

_A = '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
DIRETRIZES = "https://support.google.com/business/answer/3038177?hl=pt-BR"
RANKING = "https://support.google.com/business/answer/7091?hl=pt-BR"
AVALIACOES = "https://support.google.com/contributionpolicy/answer/7400114?hl=pt-BR"

SLUG = "google-meu-negocio-goiania"

PAGINAS = [
    {
        "slug": SLUG,
        "tipo": "servico",
        "nacional": False,
        "data": DATA,
        "publico": "Empresas, clínicas, escritórios e comércios de Goiânia e região",
        "title": "Google Meu Negócio em Goiânia: Otimização do Perfil | RCB SEO",
        "desc": ("Google Meu Negócio em Goiânia: otimização do perfil para sua empresa aparecer no mapa "
                 "quando o cliente procura perto. Consultor local, orçamento grátis."),
        "trilha": "Google Meu Negócio em Goiânia",
        "servico": "Otimização de Google Meu Negócio (Perfil da Empresa no Google)",
        "eyebrow": "Presencial em Goiânia · Aparecida · região metropolitana",
        "h1": "Google Meu Negócio em Goiânia: sua empresa no mapa quando o cliente procura perto",
        "sub": ("Google Meu Negócio em Goiânia é o perfil gratuito que coloca a sua empresa no mapa do Google "
                "e no Google Maps quando alguém da cidade procura o que você vende. Eu sou consultor em "
                "Goiânia e cuido desse perfil para ele aparecer mais, passar confiança e virar ligação e "
                "mensagem no WhatsApp."),
        "cta_hero": "Quero meu perfil no Google arrumado",
        "botao2": ("#orcamento", "Ver como funciona o orçamento"),
        "msg": "Olá, Renan! Tenho uma empresa em Goiânia e quero arrumar meu perfil no Google Meu Negócio.",
        "pills": ["Consultor em Goiânia", "Orçamento em até 24h", "Sem fidelidade"],
        "painel_h2": "Google Meu Negócio em Goiânia, em uma frase",
        "painel": [
            "Quando alguém em Goiânia busca “dentista perto de mim”, o Google mostra 3 empresas no mapa antes de qualquer site.",
            "Essas 3 levam a maior parte das ligações e mensagens.",
            "O meu trabalho é colocar a sua empresa no jogo por esses 3 lugares, do jeito que o Google permite.",
        ],
        "faq_titulo": "Perguntas frequentes sobre Google Meu Negócio em Goiânia",
        "secoes": [
            ("texto", {
                "tag": "O que é",
                "titulo": "O que é o Google Meu Negócio e por que ele importa em Goiânia?",
                "ps": [
                    "O Google Meu Negócio é a ficha da sua empresa no Google: nome, endereço, telefone, horário, "
                    "fotos, avaliações e o botão de rota. Hoje o Google chama de Perfil da Empresa no Google, mas "
                    "quase todo mundo ainda fala Google Meu Negócio. É essa ficha que aparece no mapa quando "
                    "alguém procura um serviço na cidade.",
                    "Em Goiânia isso pesa muito porque a busca é local de verdade: o cliente do Setor Bueno quer "
                    "alguém perto do Bueno, e o do Jardim Goiás quer alguém perto do Jardim Goiás. O Google "
                    "escolhe quem mostrar olhando a distância, a relevância e a reputação de cada perfil, como "
                    "ele mesmo explica na " + _A % (RANKING, "página oficial sobre o ranking local") + ". Quem "
                    "tem o perfil bem cuidado aparece; quem deixou pela metade fica escondido, mesmo sendo bom "
                    "no que faz.",
                ],
            }),
            ("split", {
                "tag": "O problema",
                "titulo": "Por que a sua empresa não aparece no Google Maps em Goiânia?",
                "ps": [
                    "Na maioria dos casos que eu vejo em Goiânia, a empresa não aparece no mapa por um destes "
                    "motivos: perfil criado e esquecido, categoria errada, poucas fotos, quase nenhuma avaliação, "
                    "horário desatualizado ou nome, endereço e telefone diferentes em cada lugar da internet.",
                    "Nada disso aparece para o dono. Ele só percebe que o concorrente da outra rua recebe as "
                    "ligações e ele não. A boa notícia é que quase sempre dá para arrumar, sem gastar com "
                    "anúncio, porque aparecer no mapa do Google é gratuito.",
                ],
                "card_titulo": "O que mais esconde um perfil no mapa",
                "card": [
                    "Categoria principal errada ou genérica.",
                    "Perfil sem fotos reais da empresa.",
                    "Poucas avaliações, e nenhuma respondida.",
                    "Telefone ou endereço diferente do site.",
                    "Perfil parado há meses, sem novidade.",
                ],
            }),
            ("cards", {
                "tag": "O que é feito",
                "titulo": "O que eu faço no seu Google Meu Negócio em Goiânia",
                "desc": "É um trabalho de consultor, feito à mão, perfil por perfil. Nada de robô, nada de truque.",
                "itens": [
                    ("1. Diagnóstico do perfil e dos concorrentes",
                     "Eu olho o seu perfil e os 3 que aparecem na frente do seu na sua região de Goiânia, e "
                     "mostro, em linguagem simples, o que eles têm que o seu ainda não tem."),
                    ("2. Perfil completo e certo",
                     "Categorias, serviços, descrição, horário, área atendida, fotos e informações conferidas, "
                     "dentro das " + _A % (DIRETRIZES, "regras oficiais do Google") + ". Um item fora da regra "
                     "pode derrubar o perfil, por isso cada detalhe é conferido."),
                    ("3. Avaliações de verdade",
                     "Um jeito simples de pedir avaliação aos seus clientes reais, e respostas para todas, as "
                     "boas e as ruins. Avaliação é um dos sinais que mais pesam no mapa, e também é o que faz o "
                     "cliente escolher você."),
                    ("4. Nome, endereço e telefone iguais em todo lugar",
                     "O Google confere se a sua empresa é a mesma no site, no perfil, nos guias de empresas e "
                     "nas redes. Dado desencontrado tira a confiança dele, e perfil sem confiança cai no mapa."),
                    ("5. Site ligado ao perfil",
                     "Se você tem site, ele passa a confirmar o que o perfil diz: mesma cidade, mesmos serviços, "
                     "mesmo telefone. Se não tem, eu te digo com franqueza se precisa ou não. Às vezes "
                     "<a href=\"/criacao-de-sites-goiania/\">um site simples</a> faz muita diferença, às vezes não."),
                    ("6. Acompanhamento",
                     "O perfil não é coisa de fazer uma vez. Fotos novas, postagens, respostas e conferência "
                     "mensal mantêm a sua empresa viva para o Google, e eu te mostro todo mês quantas ligações, "
                     "rotas e mensagens vieram do perfil."),
                ],
            }),
            ("ajuda", {
                "titulo": "Quer saber o que está escondendo o seu perfil?",
                "texto": "Me manda o nome da sua empresa no WhatsApp. Eu olho o seu perfil e os concorrentes que "
                         "aparecem na sua frente em Goiânia e te digo, sem compromisso, o que está faltando.",
                "msg": "Olá, Renan! Quero que você olhe o meu perfil no Google Meu Negócio. Minha empresa é em Goiânia.",
                "botao": "Quero que você olhe o meu perfil",
            }),
            ("texto", {
                "tag": "Resultado real",
                "titulo": "Um caso real de Google Meu Negócio em Goiânia",
                "ps": [
                    "A Docevidade, uma doceria de Goiânia, chegou ao <strong>1º lugar no Google Maps para "
                    "“macarrons Goiânia”</strong> com apenas 4 avaliações, na frente de concorrentes que tinham "
                    "47 e 312. Isso mostra que o mapa não premia só quem tem mais avaliações: premia o perfil "
                    "mais completo e mais certo para aquela busca.",
                    "Os detalhes, com prints, estão na página de <a href=\"/cases/\">cases</a>. Cada negócio é "
                    "diferente e eu não prometo posição, mas esse é o tipo de trabalho que eu faço.",
                ],
            }),
            ("tabela", {
                "tag": "Quem eu atendo",
                "titulo": "Para quais negócios o Google Meu Negócio mais faz diferença em Goiânia?",
                "desc": "Todo negócio que atende cliente da cidade ganha com um perfil bem cuidado. Estes são os que mais me procuram.",
                "colunas": ["Tipo de negócio", "O que o cliente busca no Google"],
                "linhas": [
                    ["Clínicas e consultórios", "“clínica perto de mim”, “dermatologista Goiânia”"],
                    ["Dentistas", "“dentista no Setor Bueno”, “implante Goiânia”"],
                    ["Estética", "“limpeza de pele Goiânia”, “harmonização perto de mim”"],
                    ["Advogados e contadores", "“advogado trabalhista Goiânia”, “contador perto de mim”"],
                    ["Comércio e serviços", "“pet shop perto de mim”, “dedetizadora Goiânia”"],
                ],
                "nota": "Exemplos de buscas comuns. Cada ramo tem as suas.",
            }),
            ("texto", {
                "tag": "Por ramo",
                "titulo": "Google Meu Negócio para o seu ramo em Goiânia",
                "ps": [
                    "Cada ramo tem regras e buscas próprias. Veja o que muda para "
                    "<a href=\"/google-meu-negocio-para-clinicas/\">clínicas</a>, "
                    "<a href=\"/seo-para-dentistas/\">dentistas</a>, "
                    "<a href=\"/seo-para-clinicas-de-estetica/\">clínicas de estética</a>, "
                    "<a href=\"/marketing-para-advogados/\">advogados</a>, "
                    "<a href=\"/seo-para-contadores/\">contadores</a> e "
                    "<a href=\"/para-comercios-locais/\">comércios locais</a>.",
                ],
            }),
            ("split", {
                "tag": "Com franqueza",
                "titulo": "O que eu não faço no seu perfil",
                "ps": [
                    "Tem muita gente vendendo atalho para o mapa do Google em Goiânia: enfiar palavra-chave no "
                    "nome da empresa, comprar avaliação, usar endereço de outro lugar. Funciona por um tempo e "
                    "depois o Google suspende o perfil, e recuperar um perfil suspenso é muito mais difícil do "
                    "que fazer certo desde o começo.",
                    "As " + _A % (AVALIACOES, "regras do Google sobre avaliações") + " proíbem avaliação falsa "
                    "ou trocada por desconto. Eu trabalho só com o que é permitido, porque o perfil é seu e "
                    "tem que continuar seu.",
                ],
                "card_titulo": "O que eu não faço",
                "card": [
                    "Avaliação comprada ou inventada.",
                    "Palavra-chave no nome da empresa.",
                    "Endereço falso ou de fachada.",
                    "Promessa de 1º lugar ou de prazo.",
                    "Contrato de fidelidade.",
                ],
            }),
            ("texto", {
                "tag": "Prazo",
                "titulo": "Quanto tempo leva para o perfil melhorar no mapa?",
                "ps": [
                    "Os ajustes no perfil ficam prontos em poucos dias. A melhora no mapa costuma aparecer em "
                    "semanas, e depende da sua região de Goiânia, do seu ramo e de quanto os concorrentes já "
                    "cuidam dos perfis deles. Ramo com pouca concorrência anda rápido; ramo disputado leva mais.",
                    "Por isso eu não prometo prazo para o 1º lugar. O que eu prometo, por escrito, é o que vai ser "
                    "feito e quando, e o relatório mensal com ligações, rotas e mensagens que vieram do perfil.",
                ],
            }),
            ("texto", {
                "tag": "Quanto custa",
                "titulo": "Quanto custa a otimização do Google Meu Negócio em Goiânia?",
                "ps": [
                    "Criar e manter o perfil no Google é gratuito. O que tem custo é o trabalho de deixar o perfil "
                    "completo, certo e cuidado. O valor é sob medida: depende de quanto o seu perfil precisa ser "
                    "arrumado, de quantos locais a empresa tem e se você quer acompanhamento mensal.",
                    "Para muita empresa de Goiânia, o perfil sozinho já resolve boa parte do problema, e pode "
                    "sair mais em conta do que você imagina. O orçamento é grátis e chega pelo WhatsApp em até "
                    "24 horas.",
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua empresa quer começar no Google Meu Negócio?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": -1,
                "itens": [
                    ("Arrumar o perfil", "Para quem já tem perfil, mas ele não aparece.",
                     ["Diagnóstico do perfil e dos concorrentes", "Perfil completo dentro das regras",
                      "Plano para conseguir avaliações reais"],
                     "Olá, Renan! Quero arrumar o perfil da minha empresa no Google Meu Negócio. Sou de Goiânia.",
                     "Quero arrumar meu perfil"),
                    ("Criar o perfil do zero", "Para quem ainda não está no mapa.",
                     ["Criação e verificação", "Categorias, serviços e fotos",
                      "Ligação com o site e o WhatsApp"],
                     "Olá, Renan! Minha empresa ainda não está no Google Maps. Quero criar o perfil. Sou de Goiânia.",
                     "Quero aparecer no mapa"),
                    ("Perfil + acompanhamento", "Para quem quer subir e se manter no mapa.",
                     ["Tudo do perfil arrumado", "Postagens, fotos e respostas todo mês",
                      "Relatório mensal de ligações e rotas"],
                     "Olá, Renan! Quero o acompanhamento mensal do meu Google Meu Negócio. Sou de Goiânia.",
                     "Quero o acompanhamento"),
                ],
            }),
            ("texto", {
                "tag": "Onde eu atendo",
                "titulo": "Google Meu Negócio em Goiânia, Aparecida e região",
                "ps": [
                    "Eu atendo presencialmente em Goiânia, em qualquer bairro, e também em "
                    "<a href=\"/consultoria-seo/aparecida-de-goiania/\">Aparecida de Goiânia</a>, Senador "
                    "Canedo, Trindade e <a href=\"/consultoria-seo/anapolis/\">Anápolis</a>. Para empresas de "
                    "outras cidades, o mesmo trabalho é feito online: veja "
                    "<a href=\"/google-perfil-empresa/\">Google Meu Negócio para todo o Brasil</a>.",
                    "Se você também quer o site trabalhando junto com o perfil, o caminho é o "
                    "<a href=\"/seo-local-goiania/\">SEO local em Goiânia</a>. E se quiser saber quem está por "
                    "trás do trabalho, conheça o <a href=\"/consultor-seo-goiania/\">consultor de SEO em Goiânia</a>.",
                ],
            }),
            ("fontes", {"itens": [
                ("Google: como o ranking local é definido (distância, relevância e reputação)", RANKING),
                ("Google: diretrizes para representar a sua empresa no Google", DIRETRIZES),
                ("Google: política de avaliações e conteúdo proibido", AVALIACOES),
            ]}),
        ],
        "faq": [
            ("Google Meu Negócio é a mesma coisa que Perfil da Empresa no Google?",
             "Sim. O Google mudou o nome para Perfil da Empresa no Google, mas é a mesma ficha que aparece no mapa "
             "e no Google Maps, com endereço, telefone, horário, fotos e avaliações."),
            ("Quanto custa ter a empresa no Google Meu Negócio em Goiânia?",
             "Ter o perfil é gratuito. O que tem custo é o trabalho de deixar o perfil completo e cuidado. Na RCB "
             "SEO o valor é sob medida, depende do que o seu perfil precisa, e o orçamento é grátis pelo WhatsApp "
             "em até 24 horas."),
            ("Em quanto tempo a minha empresa aparece no Google Maps?",
             "Os ajustes ficam prontos em poucos dias e a melhora costuma aparecer em semanas. Depende do bairro, "
             "do ramo e dos concorrentes. Eu não prometo posição nem prazo, e desconfie de quem promete."),
            ("Preciso ter site para aparecer no mapa do Google?",
             "Não é obrigatório. Dá para aparecer no mapa só com o perfil. Mas um site que confirma o que o perfil "
             "diz ajuda o Google a confiar na sua empresa. Eu te digo com franqueza se, no seu caso, vale a pena."),
            ("Minha empresa atende em casa ou no cliente. Dá para aparecer no mapa?",
             "Dá. O Google permite perfil de empresa que atende no endereço do cliente, mostrando a área atendida "
             "em vez do endereço. Esse tipo de perfil tem regras próprias, e eu configuro dentro delas."),
            ("Você atende presencialmente em Goiânia?",
             "Sim. Eu sou de Goiânia e atendo presencialmente na cidade e na região metropolitana, com hora "
             "marcada. Também atendo online empresas de todo o Brasil."),
            ("Tem fidelidade?",
             "Não. Para cancelar o acompanhamento basta avisar com 30 dias de antecedência. As condições vão por "
             "escrito junto com o orçamento."),
        ],
        "relacionados_titulo": "Leia também sobre Google Meu Negócio",
        "relacionados": [
            ("/blog/como-aparecer-no-google-maps/", "Como aparecer no Google Maps",
             "O que faz uma empresa aparecer, ou sumir, do mapa do Google."),
            ("/blog/google-meu-negocio-nao-aparece/", "Google Meu Negócio não aparece?",
             "Os motivos mais comuns e o que eles dizem sobre o seu perfil."),
            ("/blog/quanto-custa-otimizar-google-meu-negocio/", "Quanto custa otimizar o Google Meu Negócio",
             "O que é grátis, o que tem custo e como decidir."),
            ("/seo-local-goiania/", "SEO local em Goiânia",
             "Site e perfil no Google trabalhando juntos para a sua empresa ser encontrada na cidade."),
        ],
        "cta_final": ("Quer a sua empresa no mapa do Google em Goiânia?",
                      "Me conte o que a sua empresa faz e em qual bairro atende. Eu olho o seu perfil e os "
                      "concorrentes e te digo, com franqueza, por onde começar."),
    },
]
