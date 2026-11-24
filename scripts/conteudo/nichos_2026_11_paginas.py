# -*- coding: utf-8 -*-
"""
Páginas de nicho da leva de 23/11/2026 (pedido do Renan: "1 sim").

Motivo, medido no Search Console em 23/11/2026: as páginas de nicho de serviço (guincho,
limpeza, dedetização, estofados, energia solar, reformas) chegam à 1ª página sem link de fora
e deram 17 dos 29 cliques do site em 28 dias. As 5 desta leva vêm do planejador de
palavras-chave puxado em 10/11/2026: "marketing para salão de beleza", "oficina mecânica",
"loja", "construtoras" e "arquitetos", cada uma de 100 a 1 mil buscas por mês, e nenhuma
tinha página no site.

Regras de sempre: o público é o DONO do negócio; sem preço da RCB; nenhum resultado
prometido; social media não é oferecido; fatos só com fonte oficial (conferidas em
23/11/2026: CNAE no IBGE, CNPJ público de nov/2026 com data de referência 15/11/2026,
Lei 12.592/2012, CDC, Lei 4.591/1964, Resoluções CAU/BR 75/2014 e 52/2013, ajuda do Google).

O texto é escrito à mão aqui; o gerador (scripts/gerar-servicos-marketing.py) só monta o
invólucro. Gerar só estas páginas:
    RCB_PAGINA_SLUG=marketing-para-salao-de-beleza,... python scripts/gerar-servicos-marketing.py
"""

DATA = "2026-11-23"


def _a(href, texto):
    return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (href, texto)


def _cnae(codigo, texto):
    return _a("https://cnae.ibge.gov.br/?subclasse=%s&amp;tipo=cnae&amp;versao=10&amp;view=subclasse" % codigo, texto)


CDC_URL = "https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm"
LGPD = _a("https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm", "LGPD (Lei 13.709/2018)")
GBP_HORARIO = _a("https://support.google.com/business/answer/3039617?hl=pt-BR", "horário principal e horário especial")
FIDELIDADE = ("Existe fidelidade?",
              "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "
              "vão por escrito junto com o orçamento.")

PAGINAS = [
    # =====================================================================
    # SALÃO DE BELEZA E BARBEARIA
    # =====================================================================
    {
        # Fontes: CNAE 9602-5/01 no IBGE + CNPJ nov/2026 (954.042 ativas, 45.725 abertas em 90 dias);
        # Lei 12.592/2012 art. 4º (normas sanitárias e esterilização); ajuda do Perfil da Empresa sobre
        # links de agendamento (answer/6218037) e diretrizes de links (answer/13769188); LGPD; CDC art. 37.
        "slug": "marketing-para-salao-de-beleza",
        "nacional": True,
        "data": DATA,
        "publico": "Salões de beleza, barbearias, esmalterias e estúdios de beleza",
        "title": "Marketing para Salão de Beleza e Barbearia | RCB SEO",
        "desc": ("Marketing para salão de beleza e barbearia: Google Meu Negócio com fotos e botão de agendar, "
                 "avaliações e site que enche a agenda. Orçamento em 24h."),
        "trilha": "Marketing para salão de beleza",
        "servico": "Marketing para salões de beleza e barbearias",
        "eyebrow": "Para salões e barbearias de todo o Brasil",
        "h1": "Marketing para salão de beleza e barbearia: agenda cheia pelo Google",
        "sub": ("Marketing para salão de beleza é fazer a cliente que procura \"salão perto de mim\" ver o seu "
                "trabalho, as suas notas e um botão para marcar horário antes de ver o concorrente. Eu cuido do seu "
                "perfil no Google Maps, do site com agendamento e do anúncio no Google, com foco no que enche a "
                "cadeira: horário marcado. Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero a agenda cheia",
        "msg": "Olá, Renan! Tenho um salão de beleza e quero mais clientes pelo Google.",
        "pills": ["Orçamento em até 24h", "Foco em horário marcado", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Perfil no Google Maps com fotos do seu trabalho.",
            "Botão de agendar no perfil e no site.",
            "Rotina de avaliações depois do atendimento.",
            "Site leve com serviços e equipe.",
            "Anúncio no Google para os serviços que dão margem.",
            "Medição de cada mensagem e agendamento.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para salão de beleza",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que o salão de beleza perde cliente para quem aparece primeiro no Google?",
                "ps": [
                    "Quem procura salão novo não abre dez sites. Pesquisa \"salão perto de mim\", \"manicure no "
                    "bairro\" ou \"barbearia aberta agora\", olha as fotos, confere as estrelas e manda mensagem para "
                    "quem parece mais confiável e mais fácil de marcar. A decisão leva poucos minutos e acontece na "
                    "tela do celular.",
                    "E a disputa é enorme. Pelos dados públicos de CNPJ de novembro de 2026, o código "
                    + _cnae("9602501", "9602-5/01 (Cabeleireiros, manicure e pedicure)") +
                    " reunia 954.042 empresas ativas, com 45.725 abertas em apenas 90 dias. É um dos ramos com mais "
                    "empresas no país: quem não aparece bem no próprio bairro some no meio da multidão.",
                ],
                "card_titulo": "Sinais de que falta marketing no salão",
                "card": [
                    "Agenda que depende de indicação e de Instagram.",
                    "Perfil do Google com poucas fotos, ou fotos antigas.",
                    "Avaliações paradas há meses.",
                    "Cliente que pede horário e espera resposta.",
                    "Ninguém sabe de onde veio a cliente nova.",
                ],
            }),
            ("texto", {
                "tag": "Google Meu Negócio",
                "titulo": "Como o salão aparece no Google Maps para quem procura perto de casa?",
                "ps": [
                    "O Google Meu Negócio é a vitrine do salão. É ali que a cliente vê o seu trabalho de verdade: "
                    "fotos dos cortes, das cores, das unhas e das barbas, sempre com autorização de quem foi "
                    "atendido, fotos do espaço e da equipe. Categoria certa, serviços descritos um por um e horário "
                    "real, inclusive o de sábado, completam a ficha.",
                    "O botão de agendar pesa tanto quanto as fotos. Salão de beleza pode ter link de reserva no "
                    "perfil: a ajuda do Google sobre "
                    + _a("https://support.google.com/business/answer/6218037?hl=pt-BR", "links de empresas locais") +
                    " mostra onde ele entra, e as "
                    + _a("https://support.google.com/business/answer/13769188?hl=pt-BR", "diretrizes de links") +
                    " explicam quais tipos de link cada categoria aceita. Cliente que consegue marcar sem esperar "
                    "resposta não vai procurar outro. Veja a "
                    "<a href=\"/google-perfil-empresa/\">otimização do Google Perfil da Empresa</a>.",
                ],
            }),
            ("texto", {
                "tag": "Higiene que vende",
                "titulo": "Biossegurança no salão: a regra que também convence a cliente",
                "ps": [
                    "A " + _a("https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12592.htm",
                              "Lei 12.592/2012") +
                    " reconhece as profissões de cabeleireiro, barbeiro, esteticista, manicure, pedicure, depilador "
                    "e maquiador e determina, no art. 4º, que esses profissionais sigam as normas sanitárias, com "
                    "esterilização de materiais e utensílios. Para a cliente, isso é segurança. Para o seu "
                    "marketing, é prova.",
                    "Mostre o cuidado: o material lacrado aberto na frente da cliente, a bancada limpa, o seu "
                    "processo de esterilização. Uma frase no perfil e no site contando como você cuida disso "
                    "responde a um medo que a cliente quase nunca fala em voz alta, e esse medo decide muita "
                    "escolha de manicure.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de um salão de beleza?",
                "desc": "As frentes que enchem a agenda. Dá para começar por uma e somar as outras.",
                "itens": [
                    ("Perfil no Google Maps",
                     "Categoria, serviços um por um, fotos novas com frequência, horário de sábado e rotina de "
                     "avaliações."),
                    ("Botão de agendar",
                     "Link de agendamento no perfil e no site, para a cliente marcar sem depender de alguém "
                     "responder a mensagem."),
                    ("Site com serviços e equipe",
                     "Cada serviço com foto e explicação, cada profissional com a sua especialidade. Quem procura "
                     "\"luzes\" ou \"barba\" acha direto."),
                    ("Avaliações",
                     "Pedido pelo WhatsApp logo depois do atendimento, com o link direto, e resposta a todas, "
                     "inclusive às críticas."),
                    ("Anúncio no Google",
                     "Só para os serviços que dão margem, como noivas, mechas e tratamentos, e só no raio que a "
                     "cliente aceita ir."),
                    ("Medição",
                     "Cada mensagem e cada agendamento com a origem marcada: mapa, site ou anúncio."),
                ],
            }),
            ("texto", {
                "tag": "Cliente que volta",
                "titulo": "Como fazer a cliente voltar sem depender de promoção?",
                "ps": [
                    "Cabelo cresce, unha cresce, barba cresce: o seu serviço tem retorno natural. Com autorização "
                    "da cliente, guarde o contato e o que foi feito, e mande um lembrete na época certa, com o "
                    "horário da profissional preferida dela. A " + LGPD + " pede que esse uso seja informado e que "
                    "a cliente possa pedir para sair da lista quando quiser.",
                    "Promoção relâmpago enche um dia e ensina a cliente a só voltar com desconto. Lembrete na hora "
                    "certa enche a agenda o mês inteiro, sem baixar o preço do seu trabalho.",
                ],
            }),
            ("texto", {
                "tag": "Promessa",
                "titulo": "Como anunciar o resultado sem prometer o que não depende de você?",
                "ps": [
                    "\"Cabelo liso por seis meses\" e \"unha que não descasca\" atraem e depois viram reclamação, "
                    "porque o resultado depende do fio, da unha e do cuidado em casa. O "
                    + _a(CDC_URL, "Código de Defesa do Consumidor (art. 37)") +
                    " proíbe publicidade que induza o consumidor a erro.",
                    "Prometa o que você controla: horário cumprido, material esterilizado, profissional com "
                    "especialidade e retoque combinado por escrito quando fizer sentido. Foto real do seu trabalho, "
                    "com autorização da cliente, convence mais do que qualquer frase de efeito.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing do seu salão, do diagnóstico à agenda cheia?",
                "itens": [
                    ("Diagnóstico", "Olho o seu perfil no Google, o site e quem aparece antes de você no bairro."),
                    ("Plano por escrito", "Em até 24 horas: as frentes para começar, o que entra e o valor de cada uma."),
                    ("Perfil e agendamento", "Categoria, serviços, fotos e o botão de agendar funcionando."),
                    ("Site e anúncio, se fizer sentido", "Página por serviço e anúncio só no raio do salão."),
                    ("Medição", "Relatório de mensagens e agendamentos por canal."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde o seu salão quer começar?",
                "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa do bairro", "Para quem ainda depende de indicação e de Instagram.",
                     ["Perfil no Google com fotos e serviços", "Botão de agendar no perfil", "Rotina de avaliações"],
                     "Olá, Renan! Tenho um salão e quero aparecer no Google Maps.", "Pedir orçamento"),
                    ("Site com agendamento", "Para a cliente marcar sem esperar resposta.",
                     ["Serviços e equipe", "Agendamento online", "Página por serviço"],
                     "Olá, Renan! Quero um site com agendamento para o meu salão.", "Pedir orçamento"),
                    ("Anúncio no Google", "Para encher os horários vagos dos serviços que dão margem.",
                     ["Anúncio só no raio do salão", "Buscas de curso e emprego bloqueadas", "Medição dos agendamentos"],
                     "Olá, Renan! Quero anunciar o meu salão no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Salão de beleza precisa de site?",
             "Ajuda, principalmente para quem quer agendamento online e quer aparecer para serviços específicos, "
             "como mechas, noivas ou barba. O perfil no Google traz a maior parte das clientes novas; o site é onde "
             "ela confere serviços, equipe e marca o horário."),
            ("Dá para colocar botão de agendar no Google?",
             "Dá: o Perfil da Empresa aceita link de agendamento para salões. Me manda o nome do seu salão no "
             "WhatsApp que eu confiro se o seu perfil já está pronto para isso."),
            ("Vale a pena anunciar salão no Google?",
             "Vale para os serviços de mais valor e para encher horários vagos, desde que o anúncio apareça só no "
             "raio do salão e bloqueie buscas de curso, emprego e compra de produto."),
            ("Só o Instagram não basta?",
             "O Instagram mostra o trabalho para quem já segue você. Quem ainda não conhece o salão procura no "
             "Google e no Maps, e é ali que escolhe entre você e o concorrente. Não faço gestão de redes sociais: o "
             "meu trabalho é o seu salão ser encontrado por quem procura."),
            ("Quanto custa o marketing para salão de beleza?",
             "Depende das frentes que entram e da concorrência no seu bairro. O orçamento é individual, grátis e "
             "sai em até 24 horas pelo WhatsApp. A verba de anúncio, quando houver, é paga direto ao Google."),
            FIDELIDADE,
        ],
        "relacionados": [
            ("/blog/como-atrair-clientes-para-salao-de-beleza/", "Como atrair clientes para salão de beleza",
             "Mapa, botão de agendar, avaliações e a cliente que volta."),
            ("/google-perfil-empresa/", "Google Perfil da Empresa",
             "Fotos, serviços e avaliações para aparecer no mapa."),
            ("/seo-para-clinicas-de-estetica/", "SEO para clínicas de estética",
             "Para quem também faz procedimentos estéticos."),
        ],
        "cta_final": ("Me conte o bairro do seu salão e os serviços que você mais quer vender. Eu te digo por onde "
                      "começar.",
                      "Sem compromisso: eu olho como o seu salão aparece hoje no Google e quem aparece antes de você."),
    },

    # =====================================================================
    # OFICINA MECÂNICA
    # =====================================================================
    {
        # Fontes: CNAE 4520-0/01 no IBGE + CNPJ nov/2026 (286.679 ativas, 13.090 abertas em 90 dias);
        # CDC arts. 21 (peças originais ou com especificação do fabricante), 26 (prazos para reclamar de
        # defeito aparente), 37 (publicidade enganosa), 39 VI (serviço sem orçamento é prática abusiva) e
        # 40 (orçamento prévio discriminado, validade de 10 dias); LGPD.
        "slug": "marketing-para-oficina-mecanica",
        "nacional": True,
        "data": DATA,
        "publico": "Oficinas mecânicas, auto centers e centros automotivos",
        "title": "Marketing para Oficina Mecânica e Auto Center | RCB SEO",
        "desc": ("Marketing para oficina mecânica: Google Meu Negócio com serviços e avaliações, orçamento que passa "
                 "confiança, site e anúncio no Google. Orçamento em 24h."),
        "trilha": "Marketing para oficina mecânica",
        "servico": "Marketing para oficinas mecânicas",
        "eyebrow": "Para oficinas de todo o Brasil",
        "h1": "Marketing para oficina mecânica: o motorista acha você e confia antes de chegar",
        "sub": ("Marketing para oficina mecânica é fazer quem pesquisa \"oficina perto de mim\" achar você, ver as "
                "notas e confiar antes de entrar com o carro. Eu cuido do seu perfil no Google Maps, do site com os "
                "seus serviços e do anúncio no Google, com foco no que paga as contas: carro no elevador. Orçamento "
                "grátis em até 24 horas."),
        "cta_hero": "Quero mais carros na oficina",
        "msg": "Olá, Renan! Tenho uma oficina mecânica e quero mais clientes pelo Google.",
        "pills": ["Orçamento em até 24h", "Foco em carro no elevador", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Perfil no Google Maps com serviços e fotos.",
            "Avaliações pedidas na entrega do carro.",
            "Site com cada serviço explicado.",
            "Anúncio no Google no raio da oficina.",
            "Lembrete de revisão para quem já é cliente.",
            "Medição de ligações e mensagens.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para oficina mecânica",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que a oficina boa perde cliente para a que aparece primeiro?",
                "ps": [
                    "O maior obstáculo de uma oficina não é o preço: é o medo. Quase todo motorista já ouviu uma "
                    "história de serviço que não precisava ser feito. Por isso ele pesquisa antes, lê as avaliações, "
                    "olha as fotos e só liga para quem passa segurança. Quem aparece primeiro e com boas notas leva "
                    "o carro, mesmo que a sua oficina seja melhor.",
                    "Concorrência não falta. Pelos dados públicos de CNPJ de novembro de 2026, o código "
                    + _cnae("4520001", "4520-0/01 (Serviços de manutenção e reparação mecânica de veículos automotores)") +
                    " reunia 286.679 empresas ativas, com 13.090 abertas em 90 dias. O motorista escolhe quem "
                    "transmite mais confiança na tela do celular.",
                ],
                "card_titulo": "Sinais de que falta marketing na oficina",
                "card": [
                    "Cliente que só chega por indicação.",
                    "Perfil do Google sem fotos da oficina por dentro.",
                    "Avaliações sem resposta.",
                    "Orçamento passado só de boca.",
                    "Cliente que some depois do primeiro serviço.",
                ],
            }),
            ("texto", {
                "tag": "Confiança",
                "titulo": "Orçamento por escrito: a obrigação que vira argumento de venda",
                "ps": [
                    "O " + _a(CDC_URL, "Código de Defesa do Consumidor") + " manda entregar orçamento prévio com o "
                    "valor da mão de obra, das peças, as condições de pagamento e as datas de início e de término "
                    "(art. 40), válido por 10 dias salvo combinação diferente, e chama de prática abusiva fazer o "
                    "serviço sem orçamento e sem autorização do cliente (art. 39, VI). Também presume o uso de "
                    "peças originais e novas, ou que mantenham a especificação do fabricante, salvo autorização em "
                    "contrário (art. 21).",
                    "A oficina que transforma isso em rotina ganha a confiança que o motorista desconfiado procura: "
                    "orçamento pelo WhatsApp, foto da peça gasta, explicação simples do que precisa ser feito agora "
                    "e do que pode esperar. Diga isso no perfil e no site. \"Orçamento por escrito antes de qualquer "
                    "serviço\" é uma frase que vende.",
                ],
            }),
            ("texto", {
                "tag": "Google Meu Negócio",
                "titulo": "Como a oficina aparece no Google Maps para quem está perto?",
                "ps": [
                    "O carro quebrado não viaja longe, então o mapa decide. O Google Meu Negócio precisa da categoria "
                    "certa, dos serviços cadastrados um por um (freio, suspensão, injeção, troca de óleo, "
                    "ar-condicionado), do horário real, incluindo o sábado, e de fotos que mostrem a oficina por "
                    "dentro: o pátio organizado, os equipamentos, a equipe. A fachada também entra, para o motorista "
                    "reconhecer o lugar quando chegar.",
                    "Avaliação é o que tira o medo. O melhor momento para pedir é na entrega do carro, com o link "
                    "direto pelo WhatsApp, e toda avaliação merece resposta citando o serviço feito. Veja a "
                    "<a href=\"/google-perfil-empresa/\">otimização do Google Perfil da Empresa</a>.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de uma oficina mecânica?",
                "desc": "O que traz carro para o elevador. Dá para fazer uma frente de cada vez.",
                "itens": [
                    ("Perfil no Google Maps",
                     "Categoria, serviços um por um, fotos da oficina por dentro, horário de sábado e rotina de "
                     "avaliações."),
                    ("Site com serviços",
                     "Cada serviço explicado com os sintomas que o motorista reconhece, como barulho ao frear ou "
                     "luz acesa no painel, e o WhatsApp sempre à vista."),
                    ("Anúncio no Google",
                     "Só no raio da oficina e nos serviços que dão margem, com as buscas de curso, vaga e peça "
                     "avulsa bloqueadas."),
                    ("Página para frotas",
                     "Empresas com carros, locadoras e motoristas de aplicativo precisam de agendamento, prazo e "
                     "nota fiscal. Uma página para eles abre outra porta."),
                    ("Avaliações",
                     "Pedido na entrega do carro, com o link direto, e resposta a todas, inclusive às críticas."),
                    ("Medição",
                     "Cada ligação e cada mensagem registradas, para saber se o cliente veio do mapa, do site ou do "
                     "anúncio."),
                ],
            }),
            ("texto", {
                "tag": "Cliente que volta",
                "titulo": "Como a oficina enche a agenda com quem já é cliente?",
                "ps": [
                    "Revisão, troca de óleo, alinhamento e correia têm prazo. Com autorização do cliente e de acordo "
                    "com a " + LGPD + ", guarde o modelo, a quilometragem e o que foi feito, e mande um lembrete "
                    "quando estiver perto da próxima troca. É o cliente mais barato que existe: ele já confia em você.",
                    "Frotas de empresas, locadoras e motoristas de aplicativo precisam de manutenção constante e de "
                    "carro parado o menor tempo possível. Uma página no site falando com esse público, com "
                    "agendamento, prazo e nota fiscal, traz clientes que voltam todo mês. Guinchos e lojas de "
                    "autopeças da região também indicam oficina de confiança: vale conhecer pessoalmente.",
                ],
            }),
            ("texto", {
                "tag": "Promessa",
                "titulo": "Como anunciar prazo e garantia sem prometer demais?",
                "ps": [
                    "\"Seu carro pronto em duas horas\" e \"garantia total\" atraem e depois viram briga quando a "
                    "peça atrasa. O " + _a(CDC_URL, "Código de Defesa do Consumidor") + " proíbe publicidade "
                    "enganosa (art. 37) e fixa prazos para o cliente reclamar de defeito aparente: 30 dias para "
                    "serviço e produto não durável, 90 dias para serviço e produto durável (art. 26).",
                    "Prometa o que você controla: orçamento antes, aviso se o prazo mudar, peça trocada mostrada ao "
                    "cliente e garantia por escrito, dizendo o prazo e o que ela cobre. Isso vira avaliação boa, e "
                    "avaliação boa traz o próximo carro.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing da sua oficina, do diagnóstico ao pátio cheio?",
                "itens": [
                    ("Diagnóstico", "Olho o seu perfil no Google, o site e quem aparece antes de você na região."),
                    ("Proposta por escrito", "Em até 24 horas você recebe o que eu faria primeiro na oficina e quanto custa cada parte."),
                    ("Perfil e site", "Serviços, fotos, horário e um site que explica cada serviço."),
                    ("Anúncio, se fizer sentido", "Campanha só no raio da oficina, com as buscas erradas bloqueadas."),
                    ("Medição", "Relatório de ligações e mensagens por canal."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua oficina quer começar?",
                "desc": "Diga por onde a oficina quer começar. A resposta vem pelo WhatsApp em até 24 horas, sem custo.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa da região", "Para quem ainda depende de indicação.",
                     ["Perfil no Google com serviços e fotos", "Horário e sábado certos", "Rotina de avaliações"],
                     "Olá, Renan! Tenho uma oficina e quero aparecer no Google Maps.", "Pedir orçamento"),
                    ("Site que passa confiança", "Para o motorista confiar antes de ligar.",
                     ["Página por serviço", "Página para frotas", "WhatsApp sempre à vista"],
                     "Olá, Renan! Quero um site para a minha oficina mecânica.", "Pedir orçamento"),
                    ("Anúncio no Google", "Para quem quer carro no elevador agora.",
                     ["Anúncio só no raio da oficina", "Buscas de curso e vaga bloqueadas", "Medição das ligações"],
                     "Olá, Renan! Quero anunciar a minha oficina no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Oficina mecânica precisa de site?",
             "Ajuda. O perfil no Google traz a maior parte dos clientes de passagem, mas o site é onde o motorista "
             "desconfiado e a empresa com frota conferem os serviços, a garantia e as avaliações antes de ligar."),
            ("Como pedir avaliação para o cliente da oficina?",
             "O melhor momento é na entrega do carro, com o link direto pelo WhatsApp. Me chama no WhatsApp que eu "
             "mostro como deixar isso fácil na rotina da sua equipe."),
            ("Vale a pena anunciar oficina no Google?",
             "Vale, porque quem pesquisa oficina geralmente está com o problema agora. O cuidado é limitar o "
             "anúncio ao raio que o cliente aceita ir e bloquear buscas de curso, vaga e compra de peça."),
            ("A oficina precisa dar orçamento por escrito?",
             "Sim. O Código de Defesa do Consumidor (art. 40) manda entregar orçamento prévio com mão de obra, "
             "peças, pagamento e datas, válido por 10 dias salvo combinação diferente."),
            ("Quanto custa o marketing para oficina mecânica?",
             "Depende do que a oficina já tem e de quantas oficinas disputam a sua região. Eu mando a proposta "
             "pelo WhatsApp em até 24 horas, sem custo. Se houver anúncio, a verba vai direto para o Google."),
            FIDELIDADE,
        ],
        "relacionados": [
            ("/blog/como-atrair-clientes-para-oficina-mecanica/", "Como atrair clientes para oficina mecânica",
             "Avaliações, orçamento claro, lembrete de revisão e frotas."),
            ("/marketing-para-empresa-de-guincho/", "Marketing para empresa de guincho",
             "Guincho e oficina atendem o mesmo motorista."),
            ("/google-perfil-empresa/", "Google Perfil da Empresa",
             "Serviços, fotos e avaliações para aparecer no mapa."),
        ],
        "cta_final": ("Me conte a cidade da sua oficina e os serviços que mais dão margem. Eu te digo por onde "
                      "começar.",
                      "Sem compromisso: eu olho como a sua oficina aparece hoje no Google e quem aparece antes de você."),
    },

    # =====================================================================
    # LOJA (VAREJO FÍSICO E ONLINE)
    # =====================================================================
    {
        # Fontes: CNAE 4781-4/00 no IBGE + CNPJ nov/2026 (1.020.178 ativas, 40.731 abertas em 90 dias);
        # ajuda do Perfil da Empresa: Editor de produtos (answer/9124203), produtos disponíveis na loja
        # (answer/9934993), horário especial (answer/3039617); CDC arts. 30, 37 e 49.
        "slug": "marketing-para-loja",
        "nacional": True,
        "data": DATA,
        "publico": "Lojas de rua, lojas de bairro e lojas com venda online",
        "title": "Marketing para Loja: Mais Clientes na Porta e no Site | RCB SEO",
        "desc": ("Marketing para loja física e online: Google Meu Negócio com produtos, site ou loja virtual e "
                 "anúncio no Google nas datas que vendem. Orçamento grátis em 24h."),
        "trilha": "Marketing para loja",
        "servico": "Marketing para lojas",
        "eyebrow": "Para lojas de todo o Brasil",
        "h1": "Marketing para loja: mais gente entrando pela porta e pelo site",
        "sub": ("Marketing para loja é fazer quem procura um produto perto de casa achar a sua loja, ver o que você "
                "vende e decidir passar aí ou comprar pelo site. Eu cuido do seu perfil no Google Maps com os seus "
                "produtos, do site ou da loja virtual e do anúncio no Google, com foco no que importa: venda. "
                "Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero vender mais",
        "msg": "Olá, Renan! Tenho uma loja e quero vender mais pelo Google.",
        "pills": ["Orçamento em até 24h", "Foco em venda", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Perfil no Google Maps com produtos e fotos.",
            "Horário especial nas datas que vendem.",
            "Site ou loja virtual que vende.",
            "Anúncio no Google no raio da loja.",
            "Avaliações pedidas no caixa.",
            "Medição de rotas, ligações e mensagens.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para loja",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que a loja de rua perde venda para quem aparece primeiro no Google?",
                "ps": [
                    "Hoje a compra começa no celular, mesmo quando termina no balcão. A pessoa pesquisa \"loja de "
                    "roupa infantil perto de mim\" ou \"material de construção aberto agora\", vê quem aparece no "
                    "mapa, confere o horário e as fotos e pede a rota. Se a sua loja não aparece, ou aparece "
                    "\"fechada\" num feriado em que você está aberto, a venda vai para a loja do lado ou para o "
                    "site grande.",
                    "Só no vestuário, o código "
                    + _cnae("4781400", "4781-4/00 (Comércio varejista de artigos do vestuário e acessórios)") +
                    " reunia 1.020.178 empresas ativas em novembro de 2026, com 40.731 abertas em 90 dias, pelos "
                    "dados públicos de CNPJ. Em qualquer ramo do varejo a disputa é grande, e quem não aparece no "
                    "Google depende de quem passa na frente.",
                ],
                "card_titulo": "Sinais de que falta marketing na loja",
                "card": [
                    "Movimento que depende de quem passa na calçada.",
                    "Perfil do Google sem produtos nem fotos novas.",
                    "Cliente que pergunta no WhatsApp e some.",
                    "Site parado, ou só o Instagram.",
                    "Ninguém sabe quantas pessoas pediram a rota.",
                ],
            }),
            ("texto", {
                "tag": "Produtos no Google",
                "titulo": "Como os produtos da sua loja aparecem na busca e no Maps?",
                "ps": [
                    "O Google Meu Negócio tem um "
                    + _a("https://support.google.com/business/answer/9124203?hl=pt-BR", "Editor de produtos") +
                    " para mostrar o que você vende, com foto e descrição, e a ajuda do Google explica como "
                    + _a("https://support.google.com/business/answer/9934993?hl=pt-BR",
                         "mostrar os produtos disponíveis na loja") +
                    " na Pesquisa e no Maps. Quem procura um produto e vê que ele está na sua loja, a dez minutos "
                    "de casa, vai até aí.",
                    "Horário também é venda. Datas comemorativas, feriados e o horário estendido de fim de ano "
                    "precisam estar no perfil: o Google permite definir o " + GBP_HORARIO + ", e sem isso ele "
                    "mostra \"fechado\" justo no dia de mais movimento. Veja a "
                    "<a href=\"/google-perfil-empresa/\">otimização do Google Perfil da Empresa</a>.",
                ],
            }),
            ("texto", {
                "tag": "Site ou loja virtual",
                "titulo": "Loja física precisa de site ou de loja virtual?",
                "ps": [
                    "Não precisa começar com um grande e-commerce. Para muita loja, um site com as categorias, os "
                    "produtos principais, o endereço, o horário e o WhatsApp já resolve: o cliente confere antes de "
                    "sair de casa e chega sabendo o que quer. Quem quer vender para outras cidades precisa de loja "
                    "virtual de verdade, com pagamento e frete. Veja a "
                    "<a href=\"/criacao-de-loja-virtual-goiania/\">criação de loja virtual</a>.",
                    "Vendeu fora da loja, pelo site ou pelo WhatsApp? O "
                    + _a(CDC_URL, "Código de Defesa do Consumidor (art. 49)") +
                    " dá ao cliente 7 dias para desistir da compra feita fora do estabelecimento. Deixar a troca e "
                    "a devolução claras no site evita reclamação e aumenta a confiança de quem compra pela primeira "
                    "vez.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de uma loja?",
                "desc": "As frentes que trazem cliente para a porta e para o site. Dá para começar por uma.",
                "itens": [
                    ("Perfil no Google Maps",
                     "Produtos, fotos da vitrine e de dentro da loja, horário especial e rotina de avaliações."),
                    ("Produtos no Google",
                     "Catálogo no perfil com foto e descrição, para quem pesquisa o produto achar a sua loja."),
                    ("Site ou loja virtual",
                     "Categorias, produtos principais, endereço e WhatsApp, ou a loja virtual completa para vender "
                     "para fora."),
                    ("Anúncio no Google",
                     "No raio da loja e nas datas que vendem, com as buscas de atacado, vaga e \"grátis\" "
                     "bloqueadas."),
                    ("Avaliações",
                     "Pedido no caixa ou na entrega, com o link direto, e resposta a todas."),
                    ("Medição",
                     "Rotas, ligações, mensagens e vendas do site separadas por origem."),
                ],
            }),
            ("texto", {
                "tag": "Datas que vendem",
                "titulo": "Como a loja aproveita as datas comemorativas?",
                "ps": [
                    "Dia das Mães, Dia dos Namorados, Dia das Crianças, Black Friday e Natal costumam concentrar a "
                    "procura, e a procura começa antes da data. Atualizar produtos e fotos, ajustar o horário "
                    "especial e ligar o anúncio com antecedência coloca a sua loja na frente de quem está "
                    "pesquisando presente.",
                    "Fora das datas, o que sustenta o movimento é o básico bem feito: perfil completo, avaliações "
                    "recentes e o cliente que volta porque foi bem atendido. Com autorização, e de acordo com a "
                    + LGPD + ", uma lista de clientes para avisar das novidades vale mais do que qualquer panfleto.",
                ],
            }),
            ("texto", {
                "tag": "Promessa",
                "titulo": "Como anunciar promoção sem virar dor de cabeça?",
                "ps": [
                    "\"Tudo pela metade do preço\" e \"o mais barato da cidade\" atraem e viram reclamação quando o "
                    "cliente não encontra a oferta. O " + _a(CDC_URL, "Código de Defesa do Consumidor") + " diz que "
                    "a oferta anunciada obriga a loja a cumprir (art. 30) e proíbe publicidade enganosa (art. 37).",
                    "Anuncie o que você tem em estoque, com a condição clara e o prazo da promoção. Cliente que "
                    "encontra exatamente o que viu no anúncio compra, volta e indica.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing da sua loja, do diagnóstico às vendas?",
                "itens": [
                    ("Diagnóstico", "Olho o seu perfil no Google, o site e quem aparece antes de você na região."),
                    ("Plano no papel", "Em até 24 horas: por onde a loja começa, o que cada frente inclui e o valor de cada uma."),
                    ("Perfil e produtos", "Fotos, produtos, horário especial e rotina de avaliações."),
                    ("Site e anúncio, se fizer sentido", "Site ou loja virtual e anúncio nas datas que vendem."),
                    ("Medição", "Relatório de rotas, ligações, mensagens e vendas por canal."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua loja quer começar?",
                "desc": "Escolha o primeiro passo da loja. Eu respondo pelo WhatsApp em até 24 horas, sem cobrar nada.",
                "destaque": 1,
                "itens": [
                    ("Aparecer no mapa da região", "Para quem depende de quem passa na frente.",
                     ["Perfil no Google com produtos", "Horário especial nas datas", "Rotina de avaliações"],
                     "Olá, Renan! Tenho uma loja e quero aparecer no Google Maps.", "Pedir orçamento"),
                    ("Site ou loja virtual", "Para vender também fora do balcão.",
                     ["Catálogo com os produtos principais", "WhatsApp e rota à vista", "Troca e devolução claras"],
                     "Olá, Renan! Quero um site ou uma loja virtual para a minha loja.", "Pedir orçamento"),
                    ("Anúncio nas datas que vendem", "Para encher a loja na época certa.",
                     ["Anúncio só no raio da loja", "Buscas de atacado e vaga bloqueadas", "Medição das vendas"],
                     "Olá, Renan! Quero anunciar a minha loja no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Loja física precisa estar no Google?",
             "Precisa. É no Google e no Maps que o cliente confere se a loja existe, se está aberta e se tem o que "
             "ele procura antes de sair de casa."),
            ("Dá para mostrar os meus produtos no Google de graça?",
             "Dá: o Perfil da Empresa tem um espaço para produtos com foto e descrição. Me manda o nome da sua loja "
             "no WhatsApp que eu confiro o que já dá para ligar no seu perfil."),
            ("Vale a pena anunciar loja no Google?",
             "Vale, principalmente nas datas que vendem e para produtos que o cliente pesquisa pelo nome. O cuidado "
             "é limitar o anúncio ao raio da loja e bloquear buscas de atacado, vaga e \"grátis\"."),
            ("Preciso de loja virtual ou só de site?",
             "Quem vende só no bairro costuma resolver com um site com catálogo e WhatsApp. Quem quer vender para "
             "outras cidades precisa de loja virtual com pagamento e frete."),
            ("Quanto custa o marketing para loja?",
             "Depende do tamanho do catálogo e de quantas frentes a loja quer. A proposta sai sem custo, em até "
             "24 horas, pelo WhatsApp. Quando houver anúncio, a verba é paga direto ao Google."),
            FIDELIDADE,
        ],
        "relacionados": [
            ("/blog/como-atrair-clientes-para-loja/", "Como atrair clientes para loja",
             "Mapa, produtos no Google, vitrine, datas e cliente que volta."),
            ("/criacao-de-loja-virtual-goiania/", "Criação de loja virtual",
             "Para vender também para outras cidades."),
            ("/para-comercios-locais/", "SEO para comércio local",
             "Para aparecer no mapa do bairro."),
        ],
        "cta_final": ("Me conte o que a sua loja vende e onde ela fica. Eu te digo por onde começar.",
                      "Sem compromisso: eu olho como a sua loja aparece hoje no Google e quem aparece antes de você."),
    },

    # =====================================================================
    # CONSTRUTORAS E INCORPORADORAS
    # =====================================================================
    {
        # Fontes: CNAE 4120-4/00 no IBGE + CNPJ nov/2026 (183.307 ativas, 3.515 abertas em 90 dias; o código
        # inclui reformas, dito no texto); Lei 4.591/1964 art. 32 e § 3º (registro da incorporação nos
        # anúncios, salvo classificados), lido no Planalto em 23/11/2026; CDC arts. 30 e 37; Lei 6.496/1977
        # (ART); LGPD.
        "slug": "marketing-para-construtoras",
        "nacional": True,
        "data": DATA,
        "publico": "Construtoras, incorporadoras e empresas de construção",
        "title": "Marketing para Construtoras e Incorporadoras | RCB SEO",
        "desc": ("Marketing para construtoras: landing page por empreendimento, Google Ads com contatos "
                 "qualificados e site que passa confiança. Orçamento grátis em 24h."),
        "trilha": "Marketing para construtoras",
        "servico": "Marketing para construtoras e incorporadoras",
        "eyebrow": "Para construtoras de todo o Brasil",
        "h1": "Marketing para construtoras: o contato certo para cada empreendimento",
        "sub": ("Marketing para construtora é colocar cada empreendimento na frente de quem procura imóvel na "
                "região, com uma página que mostra o projeto, passa confiança e entrega o contato na hora para o "
                "corretor. Eu cuido da página de cada empreendimento, do anúncio no Google e do site da "
                "construtora, dentro das regras do anúncio imobiliário. Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero contatos que compram",
        "msg": "Olá, Renan! Tenho uma construtora e quero mais contatos para os meus empreendimentos.",
        "pills": ["Orçamento em até 24h", "Foco em contato qualificado", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Uma página para cada empreendimento.",
            "Anúncio no Google na região do imóvel.",
            "Site com as obras entregues.",
            "Contato que chega na hora para o corretor.",
            "Registro da incorporação no anúncio.",
            "Medição de cada contato por canal.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para construtoras",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que a construtora anuncia e recebe contato que não compra?",
                "ps": [
                    "O problema raramente é falta de contato. É contato errado: gente procurando aluguel, emprego "
                    "ou um imóvel em outra faixa. Isso acontece quando o anúncio leva para a página inicial do site "
                    "ou para um portal genérico, em vez de uma página do empreendimento que mostra o imóvel certo e "
                    "filtra quem não é o público.",
                    "Pelos dados públicos de CNPJ de novembro de 2026, o código "
                    + _cnae("4120400", "4120-4/00 (Construção de edifícios)") +
                    " reunia 183.307 empresas ativas, com 3.515 abertas em 90 dias. O código inclui também "
                    "empresas de reforma, mas mostra o tamanho da disputa pela atenção de quem vai comprar ou "
                    "construir.",
                ],
                "card_titulo": "Sinais de que falta marketing na construtora",
                "card": [
                    "Anúncio que leva para a página inicial do site.",
                    "Contatos que nunca atendem o corretor.",
                    "Empreendimento sem página própria.",
                    "Site sem obras entregues nem prazos cumpridos.",
                    "Ninguém sabe qual anúncio trouxe a visita ao decorado.",
                ],
            }),
            ("texto", {
                "tag": "Landing page",
                "titulo": "Por que cada empreendimento precisa da sua própria landing page?",
                "ps": [
                    "Para a construtora, a landing page é a página do empreendimento: localização, plantas, áreas "
                    "comuns, estágio da obra e um formulário curto que pergunta o que o corretor precisa saber. Quem "
                    "clica num anúncio de \"apartamento de 2 quartos no bairro\" cai direto no imóvel que procurou, "
                    "e não na lista de todos os lançamentos.",
                    "Ela também é onde se mede o resultado: cada contato chega com a origem marcada, e dá para saber "
                    "qual anúncio traz quem visita o decorado. Veja a "
                    "<a href=\"/criacao-de-landing-page/\">criação de landing page para anúncios</a>.",
                    "E ela precisa abrir rápido no celular. Veja como os sites das construtoras de Goiânia se saem "
                    "no <a href=\"/blog/velocidade-sites-construtoras-goiania/\">teste de velocidade que fizemos "
                    "com eles</a>.",
                ],
            }),
            ("texto", {
                "tag": "Regra do anúncio",
                "titulo": "O que o anúncio de lançamento precisa mostrar por lei?",
                "ps": [
                    "A " + _a("https://www.planalto.gov.br/ccivil_03/leis/l4591.htm", "Lei 4.591/1964") +
                    " diz que o incorporador só pode vender as futuras unidades depois do registro do memorial de "
                    "incorporação no cartório de imóveis (art. 32), e que o número desse registro, com a indicação "
                    "do cartório, deve constar dos anúncios, impressos, publicações, propostas e contratos, salvo "
                    "nos classificados (art. 32, § 3º).",
                    "O " + _a(CDC_URL, "Código de Defesa do Consumidor") + " completa: a oferta anunciada obriga a "
                    "empresa (art. 30), e a publicidade não pode induzir o comprador a erro (art. 37). Na prática, "
                    "vale conferir se imagens, metragens e prazos do anúncio batem com o projeto registrado. Uma "
                    "página de empreendimento bem feita já nasce com esses cuidados, e isso protege a venda depois.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de uma construtora?",
                "desc": "As frentes que trazem o contato certo. Dá para começar por um empreendimento.",
                "itens": [
                    ("Página por empreendimento",
                     "Plantas, localização, estágio da obra, registro da incorporação e formulário que qualifica o "
                     "contato."),
                    ("Anúncio no Google na região",
                     "Anúncio por bairro e por tipo de imóvel, com as buscas de aluguel, emprego e leilão "
                     "bloqueadas."),
                    ("Site institucional",
                     "Obras entregues, prazos cumpridos e a história da construtora, que é o que o comprador "
                     "confere antes de visitar."),
                    ("Contato direto ao corretor",
                     "Formulário e WhatsApp que chegam na hora para quem vai atender, com o empreendimento e a "
                     "origem."),
                    ("Perfil no Google Maps",
                     "Perfil da construtora com fotos das obras e avaliações de quem já comprou ou construiu."),
                    ("Medição",
                     "Cada contato com a origem marcada, para saber qual anúncio e qual página trazem visita."),
                ],
            }),
            ("texto", {
                "tag": "Obra por contrato",
                "titulo": "E a construtora que constrói por encomenda?",
                "ps": [
                    "Nem toda construtora vende lançamento. Quem constrói casa sob medida, galpão ou obra para "
                    "empresa vive de outra busca, como \"construtora de casas\" ou \"construção de galpão\" na "
                    "cidade. Para esse público, o que vende é portfólio com obras entregues, prazo cumprido e o "
                    "perfil do Google com avaliações de quem já construiu com você.",
                    "Arquitetos e engenheiros que projetam e precisam de quem execute também são uma porta. Uma "
                    "página no site falando com eles, com prazo, acompanhamento da obra, "
                    + _a("https://www.planalto.gov.br/ccivil_03/leis/l6496.htm", "ART (Lei 6.496/1977)") +
                    " e padrão de acabamento, abre parcerias que nenhum anúncio substitui.",
                ],
            }),
            ("texto", {
                "tag": "Contato",
                "titulo": "Como tratar o contato que chega pelo anúncio?",
                "ps": [
                    "Contato de imóvel esfria em horas. Formulário que cai num e-mail que ninguém olha é verba "
                    "jogada fora. O contato precisa chegar na hora para o corretor, com o empreendimento e a "
                    "origem, e a primeira resposta precisa sair rápido.",
                    "Quem deixou o contato também tem direitos: a " + LGPD + " pede que a pessoa saiba para que o "
                    "dado será usado. Um aviso simples no formulário resolve e passa seriedade.",
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing da sua construtora, do diagnóstico ao contato certo?",
                "itens": [
                    ("Diagnóstico", "Olho o site, os anúncios, as páginas dos empreendimentos e quem aparece antes de você."),
                    ("Proposta por lançamento", "Em até 24 horas: o que cada empreendimento precisa, o que entra e o valor de cada parte."),
                    ("Página do empreendimento", "Uma página por empreendimento, com o registro da incorporação e formulário curto."),
                    ("Anúncio, se fizer sentido", "Campanha por bairro e tipo de imóvel, com as buscas erradas bloqueadas."),
                    ("Medição", "Relatório de contatos e visitas por anúncio e por página."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde a sua construtora quer começar?",
                "desc": "Comece por um lançamento ou pelo site da construtora. Orçamento sem custo em até 24 horas.",
                "destaque": 0,
                "itens": [
                    ("Página de lançamento", "Para vender um empreendimento específico.",
                     ["Página do empreendimento", "Formulário que qualifica", "Registro da incorporação à vista"],
                     "Olá, Renan! Quero uma landing page para um empreendimento da minha construtora.", "Pedir orçamento"),
                    ("Anúncio de imóveis no Google", "Para ter contato certo agora.",
                     ["Anúncio por bairro e tipo", "Buscas de aluguel bloqueadas", "Custo de cada contato medido"],
                     "Olá, Renan! Quero anunciar os imóveis da minha construtora no Google.", "Pedir orçamento"),
                    ("Site da construtora", "Para o comprador confiar antes de visitar.",
                     ["Obras entregues", "Prazos e história", "Página por empreendimento"],
                     "Olá, Renan! Quero um site novo para a minha construtora.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Construtora precisa de landing page para cada empreendimento?",
             "Para anunciar, sim: a página do empreendimento mostra o imóvel certo, filtra quem não é o público e "
             "mede cada contato. O site institucional continua sendo o lugar da história e das obras entregues."),
            ("O anúncio de lançamento precisa ter o número do registro?",
             "Pela Lei 4.591/1964 (art. 32, § 3º), o número do registro da incorporação e o cartório devem constar "
             "dos anúncios, impressos e publicações da incorporação, salvo nos classificados."),
            ("Vale a pena anunciar imóvel no Google?",
             "Vale para quem tem página por empreendimento e corretor respondendo rápido. Sem isso, o anúncio "
             "traz contato que esfria antes do retorno."),
            ("Construtora de obra por encomenda também precisa de marketing?",
             "Precisa, com outro foco: portfólio, obras entregues, perfil no Google com avaliações e parceria com "
             "arquitetos e engenheiros."),
            ("Quanto custa o marketing para construtora?",
             "Varia com o número de lançamentos e com a região. A proposta é feita para a sua construtora, sem "
             "custo, em até 24 horas pelo WhatsApp. A verba de anúncio vai direto para o Google."),
            FIDELIDADE,
        ],
        "relacionados": [
            ("/blog/landing-page-para-construtora/", "Landing page para construtora",
             "O que a página de cada empreendimento precisa ter."),
            ("/criacao-de-landing-page/", "Criação de landing page",
             "A página certa para cada anúncio."),
            ("/seo-para-imobiliarias/", "Marketing para imobiliárias",
             "Para quem vende imóveis de terceiros."),
        ],
        "cta_final": ("Me conte o empreendimento que você quer vender e a região. Eu te digo por onde começar.",
                      "Sem compromisso: eu olho os seus anúncios e o seu site e te digo onde o contato está se perdendo."),
    },

    # =====================================================================
    # ARQUITETOS E ESCRITÓRIOS DE ARQUITETURA
    # =====================================================================
    {
        # Fontes: CNAE 7111-1/00 no IBGE + CNPJ nov/2026 (45.584 ativas, 1.429 abertas em 90 dias; não conta
        # quem atua como pessoa física); Resolução CAU/BR 75/2014 arts. 11 e 12 (responsável técnico, título,
        # registro e atividade em toda divulgação ao público); Código de Ética e Disciplina do CAU/BR
        # (Resolução 52/2013), regra 3.2.16 (proibição de vantagem de fornecedores, a "reserva técnica").
        # Textos lidos no portal da transparência do CAU/BR em 23/11/2026.
        "slug": "marketing-para-arquitetos",
        "nacional": True,
        "data": DATA,
        "publico": "Arquitetos, urbanistas e escritórios de arquitetura e interiores",
        "title": "Marketing para Arquitetos e Escritórios de Arquitetura | RCB SEO",
        "desc": ("Marketing para arquitetos: site com portfólio que vende, Google Meu Negócio e Google Ads dentro "
                 "das regras do CAU, para não depender só de indicação."),
        "trilha": "Marketing para arquitetos",
        "servico": "Marketing para arquitetos e escritórios de arquitetura",
        "eyebrow": "Para arquitetos de todo o Brasil",
        "h1": "Marketing para arquitetos: projeto novo sem depender só de indicação",
        "sub": ("Marketing para arquiteto é fazer quem vai construir ou reformar achar o seu trabalho, entender o "
                "seu estilo e chamar você para conversar antes de fechar com quem apareceu primeiro. Eu cuido do "
                "site com portfólio, do seu perfil no Google Maps e do anúncio no Google, dentro das regras do CAU. "
                "Orçamento grátis em até 24 horas."),
        "cta_hero": "Quero mais projetos",
        "msg": "Olá, Renan! Tenho um escritório de arquitetura e quero mais clientes pelo Google.",
        "pills": ["Orçamento em até 24h", "Dentro das regras do CAU", "Prazo por escrito"],
        "painel_h2": "O que entra no marketing",
        "painel": [
            "Site com portfólio organizado por tipo.",
            "Perfil do escritório no Google Maps.",
            "Página por serviço: casa, reforma, interiores.",
            "Anúncio no Google para quem vai construir.",
            "Responsável técnico e registro no anúncio.",
            "Medição de cada contato.",
        ],
        "faq_titulo": "Perguntas frequentes sobre marketing para arquitetos",
        "secoes": [
            ("split", {
                "tag": "O cenário",
                "titulo": "Por que o arquiteto bom fica refém da indicação?",
                "ps": [
                    "Indicação traz o melhor cliente, mas não tem hora para chegar. Enquanto isso, quem vai "
                    "construir ou reformar pesquisa \"arquiteto na cidade\", \"projeto de casa\" ou \"design de "
                    "interiores\", olha os primeiros portfólios e chama para conversar quem passou confiança.",
                    "Pelos dados públicos de CNPJ de novembro de 2026, o código "
                    + _cnae("7111100", "7111-1/00 (Serviços de arquitetura)") +
                    " reunia 45.584 empresas ativas, com 1.429 abertas em 90 dias, sem contar quem trabalha como "
                    "pessoa física. A disputa é pelo cliente que está decidindo agora.",
                ],
                "card_titulo": "Sinais de que falta marketing no escritório",
                "card": [
                    "Projetos que só chegam por indicação.",
                    "Portfólio só no Instagram.",
                    "Site sem página por tipo de projeto.",
                    "Perfil do Google inexistente ou sem fotos.",
                    "Cliente que pede orçamento e some.",
                ],
            }),
            ("texto", {
                "tag": "Portfólio",
                "titulo": "Como o portfólio vira cliente, e não só elogio?",
                "ps": [
                    "Portfólio que vende conta uma história: qual era o problema, o que foi feito e como ficou. "
                    "Organize por tipo de projeto (casa nova, reforma, interiores, comercial), com fotos de "
                    "qualidade e o contexto de cada um. Quem procura reforma de apartamento quer ver reforma de "
                    "apartamento, não a casa de campo mais bonita que você já fez.",
                    "Mostrar o projeto de um cliente pede autorização por escrito, e as fotos da obra pronta também. "
                    "Isso respeita quem confiou em você e evita problema quando o projeto fizer sucesso.",
                ],
            }),
            ("texto", {
                "tag": "Regra do CAU",
                "titulo": "O que o CAU exige no anúncio do arquiteto?",
                "ps": [
                    "A " + _a("https://transparencia.caubr.gov.br/resolucao75/", "Resolução CAU/BR nº 75/2014") +
                    " determina que a divulgação de projeto, obra ou serviço de arquitetura em qualquer meio "
                    "dirigido ao público traga o responsável técnico, o título profissional, o número de registro "
                    "no CAU e a atividade desenvolvida (art. 11), com letras no mínimo do mesmo tamanho das usadas "
                    "para os demais profissionais da peça (art. 12).",
                    "E o " + _a("https://transparencia.caubr.gov.br/resolucao52/",
                                "Código de Ética e Disciplina do CAU/BR") +
                    " proíbe receber comissão, vantagem ou presente de fornecedores dos seus clientes (regra "
                    "3.2.16), a chamada reserva técnica. Isso muda o marketing: parceria com loja ou fornecedor não "
                    "pode ser troca de comissão. O caminho limpo é portfólio, conteúdo e a indicação de quem já foi "
                    "bem atendido.",
                ],
            }),
            ("texto", {
                "tag": "Google",
                "titulo": "Como o escritório aparece no Google para quem vai construir?",
                "ps": [
                    "O Google Meu Negócio funciona para escritório que atende clientes. Fotos dos projetos, serviços "
                    "cadastrados e avaliações de quem já contratou fazem o escritório aparecer no mapa da cidade, "
                    "que é onde muita gente começa a procura. Veja a "
                    "<a href=\"/google-perfil-empresa/\">otimização do Google Perfil da Empresa</a>.",
                    "No site, uma página por serviço (projeto residencial, reforma, interiores, comercial) faz o "
                    "Google mostrar você para buscas específicas e responde às dúvidas que o cliente tem antes da "
                    "primeira reunião: como funciona, quanto tempo leva o projeto e o que entra em cada etapa. Veja "
                    "o <a href=\"/site-otimizado-para-seo/\">site otimizado para o Google</a>.",
                ],
            }),
            ("cards", {
                "tag": "As frentes",
                "titulo": "O que entra no marketing de um escritório de arquitetura?",
                "desc": "As frentes que trazem projeto novo, na ordem que fizer sentido para o escritório.",
                "itens": [
                    ("Site com portfólio",
                     "Projetos por tipo, com problema, solução e fotos autorizadas."),
                    ("Página por serviço",
                     "Casa nova, reforma, interiores e comercial, cada uma respondendo às dúvidas do cliente."),
                    ("Perfil no Google Maps",
                     "Perfil do escritório com fotos dos projetos, serviços e rotina de avaliações."),
                    ("Google Ads",
                     "Anúncio para quem pesquisa projeto agora, só na sua região, com buscas de curso, vaga e "
                     "\"grátis\" bloqueadas."),
                    ("Dentro das regras",
                     "Responsável técnico, título e registro no CAU em toda divulgação, como pede a Resolução "
                     "75/2014."),
                    ("Medição",
                     "Cada contato com a origem marcada, para saber se veio do mapa, do site ou do anúncio."),
                ],
            }),
            ("passos", {
                "titulo": "Como funciona o marketing do seu escritório, do diagnóstico ao projeto novo?",
                "itens": [
                    ("Diagnóstico", "Olho o seu site, o perfil no Google e quem aparece antes de você na cidade."),
                    ("Proposta para o escritório", "Em até 24 horas: o que falta primeiro, o que entra e quanto custa cada frente."),
                    ("Portfólio e páginas", "Projetos organizados por tipo e uma página para cada serviço."),
                    ("Anúncio, se fizer sentido", "Campanha na sua região, com o registro no CAU e as buscas erradas bloqueadas."),
                    ("Medição", "Relatório de contatos por canal."),
                ],
            }),
            ("orcamento", {
                "titulo": "Por onde o seu escritório quer começar?",
                "desc": "Comece pelo que mais falta no escritório. Orçamento sem custo, respondido em até 24 horas.",
                "destaque": 0,
                "itens": [
                    ("Site com portfólio", "Para o cliente entender o seu estilo antes de ligar.",
                     ["Projetos por tipo", "Página por serviço", "WhatsApp à vista"],
                     "Olá, Renan! Quero um site com portfólio para o meu escritório de arquitetura.", "Pedir orçamento"),
                    ("Aparecer no Google da cidade", "Para não depender só de indicação.",
                     ["Perfil do escritório no Google", "Fotos e serviços", "Rotina de avaliações"],
                     "Olá, Renan! Quero que o meu escritório de arquitetura apareça no Google Maps.", "Pedir orçamento"),
                    ("Anúncio para projeto", "Para ter conversa nova agora.",
                     ["Anúncio só na sua região", "Buscas de curso bloqueadas", "Registro do CAU no anúncio"],
                     "Olá, Renan! Quero anunciar o meu escritório de arquitetura no Google.", "Pedir orçamento"),
                ],
            }),
        ],
        "faq": [
            ("Arquiteto pode fazer anúncio no Google?",
             "Pode. A Resolução CAU/BR nº 75/2014 pede que a divulgação traga o responsável técnico, o título "
             "profissional, o registro no CAU e a atividade desenvolvida."),
            ("Arquiteto pode receber comissão de loja?",
             "Não. O Código de Ética e Disciplina do CAU/BR (regra 3.2.16) proíbe receber comissão ou vantagem de "
             "fornecedores dos seus clientes, a chamada reserva técnica."),
            ("Portfólio no Instagram não basta?",
             "O Instagram mostra o trabalho para quem já segue você. Quem vai construir pesquisa no Google, e é ali "
             "que compara escritórios. Não faço gestão de redes sociais: o meu trabalho é o seu escritório ser "
             "encontrado por quem procura."),
            ("Vale a pena anunciar projeto de arquitetura no Google?",
             "Vale para quem tem página por serviço e responde rápido. O cuidado é anunciar só na sua região e "
             "bloquear buscas de curso, vaga e planta grátis."),
            ("Quanto custa o marketing para arquitetos?",
             "Varia com o que o escritório já tem e com a cidade. Você recebe a proposta sem custo, em até 24 horas, "
             "pelo WhatsApp. Se houver anúncio, a verba é paga direto ao Google."),
            FIDELIDADE,
        ],
        "relacionados": [
            ("/blog/google-ads-para-arquitetos/", "Google Ads para arquitetos",
             "Que buscas anunciar e o que o CAU exige no anúncio."),
            ("/marketing-para-empresa-de-reformas/", "Marketing para empresa de reformas",
             "Para quem executa a obra."),
            ("/site-otimizado-para-seo/", "Site otimizado para SEO",
             "Portfólio que o Google entende."),
        ],
        "cta_final": ("Me conte a sua cidade e o tipo de projeto que você mais quer fazer. Eu te digo por onde "
                      "começar.",
                      "Sem compromisso: eu olho como o seu escritório aparece hoje no Google e quem aparece antes de "
                      "você."),
    },
]
