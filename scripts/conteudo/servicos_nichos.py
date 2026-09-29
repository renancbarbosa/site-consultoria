# -*- coding: utf-8 -*-
"""
Páginas "serviço + nicho" (28/09/2026) — buscas de quem quer COMPRAR um serviço
para o seu ramo: "site para dentista", "tráfego pago para advogados" etc.

Mesmo formato de servicos_marketing.py (o gerador gerar-servicos-marketing.py monta
as duas listas). Regras: sem preço da RCB, sem resultado prometido, normas de
conselho citadas com cuidado, todo CTA para o WhatsApp com mensagem própria.

Canibalização evitada de propósito:
  - "site para clínica" já existe em /site-para-clinica/ -> não criado aqui.
  - "site para energia solar" é o artigo /blog/site-para-empresa-de-energia-solar/.
  - As páginas /seo-para-dentistas/ etc. disputam "SEO para X"; estas disputam
    "site para X" e "tráfego pago para X" (outra intenção de compra).
"""


def _site(slug, nicho, nicho_pl, h1, desc, sub, dor_titulo, dor_ps, dor_card, entra, orc, faq, rel, msg, cta_final,
          painel):
    return {
        "slug": slug,
        "title": "%s | Orçamento Grátis" % h1,
        "desc": desc,
        "trilha": h1,
        "servico": h1,
        "eyebrow": "Goiânia e todo o Brasil",
        "h1": h1,
        "sub": sub,
        "cta_hero": "Quero o orçamento do meu site",
        "msg": msg,
        "pills": ["Orçamento em até 24h", "Feito para %s" % nicho_pl, "Garantia de 30 dias"],
        "painel_h2": "O que vem no site para %s" % nicho,
        "painel": painel,
        "secoes": [
            ("split", {"tag": "O problema", "titulo": dor_titulo, "ps": dor_ps,
                       "card_titulo": "Sinais de que o seu site está perdendo cliente", "card": dor_card}),
            ("cards", {"tag": "O que está incluído", "titulo": "O que entra no site para %s" % nicho, "itens": entra}),
            ("faixas", {"titulo": "Quanto custa um site para %s?" % nicho,
                        "desc": ("Depende de quantos serviços precisam de página própria, de quem escreve os textos e "
                                 "de quantas cidades você quer disputar. Um site de uma página custa pouco e quase não "
                                 "traz cliente pelo Google; um site com página para cada serviço é um projeto maior — e "
                                 "é o que aparece quando o cliente pesquisa."),
                        "itens": [
                            ("Site de apresentação", "Poucas páginas, texto enxuto. Serve como cartão de visita e "
                             "para mandar o link no WhatsApp."),
                            ("Site com página por serviço", "Uma página para cada serviço que dá dinheiro, textos "
                             "escritos para a busca e Perfil da Empresa ligado."),
                            ("Site + acompanhamento", "Novas páginas e ajustes todo mês, conforme o que os números "
                             "do Google mostram."),
                        ]}),
            ("orcamento", {"titulo": "Seu site sob medida: quanto fica o seu projeto?",
                           "desc": ("Escolha por onde começar e me chame no WhatsApp. Em até 24 horas você recebe o "
                                    "valor exato — e uma olhada em quem aparece na sua frente no Google hoje."),
                           "itens": orc, "destaque": 1}),
            ("passos", {"titulo": "Como é criar o seu site",
                        "itens": [
                            ("1. Me conte o seu trabalho", "No WhatsApp: serviços, região e o que já existe hoje."),
                            ("2. Eu escrevo e monto", "Páginas, textos e botão de WhatsApp prontos para você conferir."),
                            ("3. No ar e no Google", "Site publicado e ligado ao seu Perfil da Empresa."),
                        ]}),
        ],
        "faq": faq,
        "relacionados": rel,
        "cta_final": cta_final,
    }


def _trafego(slug, nicho, h1, title, desc, sub, dor_titulo, dor_ps, dor_card, regras_titulo, regras_ps, entra, orc,
             faq, rel, msg, cta_final, painel):
    return {
        "slug": slug,
        "title": title,
        "desc": desc,
        "trilha": h1,
        "servico": h1,
        "eyebrow": "Google Ads e Meta Ads",
        "h1": h1,
        "sub": sub,
        "cta_hero": "Quero anunciar do jeito certo",
        "msg": msg,
        "pills": ["Orçamento em até 24h", "Google Ads e Meta Ads", "Verba no seu cartão"],
        "painel_h2": "O que a gestão de tráfego pago para %s inclui" % nicho,
        "painel": painel,
        "secoes": [
            ("split", {"tag": "O problema", "titulo": dor_titulo, "ps": dor_ps,
                       "card_titulo": "Sinais de que o anúncio está queimando verba", "card": dor_card}),
            ("texto", {"tag": "Regras e cuidados", "titulo": regras_titulo, "ps": regras_ps}),
            ("cards", {"tag": "O que está incluído", "titulo": "O que entra na gestão de tráfego pago para %s" % nicho,
                       "itens": entra}),
            ("faixas", {"titulo": "Quanto custa o tráfego pago para %s?" % nicho,
                        "desc": ("São dois valores: a <strong>verba do anúncio</strong>, paga direto ao Google ou ao "
                                 "Meta no seu cartão, e a <strong>gestão</strong>, que é o trabalho de montar e "
                                 "acompanhar as campanhas. A verba certa depende de quanto vale um cliente para você e "
                                 "de quanto custa o clique no seu ramo e na sua cidade."),
                        "itens": [
                            ("Verba do anúncio", "Definida por você e paga à plataforma. Dá para começar pequeno e "
                             "aumentar conforme as conversas chegam."),
                            ("Gestão de um canal", "Google Ads ou Meta Ads, com um ou dois serviços principais."),
                            ("Google + Meta", "Os dois canais juntos: Google para quem procura, Instagram para gerar "
                             "demanda na sua região."),
                        ]}),
            ("orcamento", {"titulo": "Seus anúncios sob medida: quanto fica o seu projeto?",
                           "desc": ("Escolha por onde começar e me chame no WhatsApp. Em até 24 horas você recebe o "
                                    "valor da gestão e uma sugestão de verba inicial para o seu caso."),
                           "itens": orc, "destaque": 0}),
            ("passos", {"titulo": "Como começa a gestão dos seus anúncios",
                        "itens": [
                            ("1. Me conte o seu negócio", "No WhatsApp: serviços, região e se você já anuncia."),
                            ("2. Montamos o plano", "Canal, campanhas, verba inicial e a página que recebe o clique."),
                            ("3. Anúncio no ar e acompanhado", "Ajustes contínuos e relatório de quantas conversas vieram."),
                        ]}),
        ],
        "faq": faq,
        "relacionados": rel,
        "cta_final": cta_final,
    }


def _o(nome, para, itens, msg, botao):
    return (nome, para, itens, msg, botao)


PAGINAS = [
    # ======================================================= SITE PARA DENTISTA
    _site(
        "criacao-de-site-para-dentista", "dentista", "dentistas",
        "Criação de site para dentista",
        ("Criação de site para dentista: uma página por tratamento, WhatsApp em todas as páginas e site feito para aparecer no Google. Orçamento grátis em 24h."),
        ("O paciente pesquisa \"implante dentário\" ou \"aparelho invisível\" antes de marcar. Se o seu site tem uma "
         "página só, genérica, ele cai no concorrente. Eu crio o site do seu consultório com uma página para cada "
         "tratamento, pensado para aparecer no Google e levar o paciente direto para o seu WhatsApp."),
        "Site de dentista com uma página só não aparece para ninguém",
        ["Implante, lente, clareamento, ortodontia, harmonização: cada tratamento é uma busca diferente no Google. "
         "Site com uma página falando de tudo não responde a nenhuma delas — e quem responde é a clínica do lado.",
         "O paciente de tratamento de valor alto pesquisa muito antes de ligar. Ele quer saber como funciona, quanto "
         "tempo leva, quem é o dentista e onde fica o consultório. O site que responde isso com clareza marca a "
         "avaliação; o que não responde perde o paciente sem nem saber.",
         "Tudo dentro das regras de publicidade do CFO: sem promessa de resultado e com o cuidado que o conselho "
         "exige na divulgação."],
        ["<strong>Site com uma página só.</strong> Nenhum tratamento tem página própria.",
         "<strong>O paciente não acha o WhatsApp.</strong> Só um telefone no rodapé.",
         "<strong>Você não aparece quando pesquisa o tratamento.</strong> Só quando pesquisa o seu nome."],
        [("Uma página por tratamento", "Implante, ortodontia, lente, clareamento, prótese: cada um com o que é, para "
          "quem é indicado e como funciona."),
         ("WhatsApp com mensagem pronta", "O paciente já chega dizendo qual tratamento quer. A recepção responde mais rápido."),
         ("Equipe e estrutura", "Dentistas com CRO, fotos reais do consultório e da equipe. É o que passa confiança."),
         ("Dentro das regras do CFO", "Textos sem promessa de resultado e divulgação dentro do que o conselho permite."),
         ("Rápido no celular", "Quase todo paciente pesquisa pelo celular. Site leve não perde ninguém no carregamento."),
         ("Ligado ao Google Maps", "Site e Perfil da Empresa apontando um para o outro — o par que coloca o consultório no mapa.")],
        [_o("Site de apresentação", "Para o consultório que ainda não tem site.",
            ["Páginas principais", "WhatsApp em todas as páginas", "Rápido no celular"],
            "Olá, Renan! Sou dentista e quero um orçamento de site.", "Orçamento do meu site"),
         _o("Site com página por tratamento", "Para aparecer quando o paciente pesquisa o tratamento.",
            ["Uma página por tratamento", "Textos dentro das regras do CFO", "Perfil da Empresa ligado"],
            "Olá, Renan! Sou dentista e quero um site com página para cada tratamento.", "Quero aparecer no Google"),
         _o("Site + anúncio", "Para encher a agenda enquanto o site sobe no Google.",
            ["Site com página por tratamento", "Google Ads para os tratamentos principais", "Contatos medidos"],
            "Olá, Renan! Sou dentista e quero site e anúncio no Google.", "Quero site + anúncio"),
         _o("Já tenho site e não aparece", "Para quem tem site parado.",
            ["Diagnóstico do site atual", "Plano de páginas por tratamento", "O que dá para aproveitar"],
            "Olá, Renan! Sou dentista, tenho site e ele não aparece no Google. Pode olhar?", "Olhar meu site")],
        [("Quanto custa um site para dentista?",
          "Depende de quantos tratamentos precisam de página própria e de quem escreve os textos. Um site de "
          "apresentação custa bem menos que um site com página para cada tratamento. O orçamento é grátis e sai em "
          "até 24 horas pelo WhatsApp."),
         ("Site de dentista pode mostrar antes e depois?",
          "Depende das regras do CFO em vigor e do contexto. Na dúvida, o site pode mostrar casos de forma educativa, "
          "sem promessa de resultado, e sempre com autorização do paciente."),
         ("O site vai aparecer no Google?",
          "O site é feito para isso: uma página por tratamento, textos escritos para a busca e ligação com o Perfil "
          "da Empresa. Entrar no Google é rápido; subir de posição leva meses, conforme a concorrência na sua região."),
         ("Vocês fazem anúncio para dentista também?",
          "Sim. A RCB faz a gestão de Google Ads e Meta Ads para consultórios, dentro das regras do CFO.")],
        [("/trafego-pago-para-dentistas/", "Tráfego pago para dentistas", "Google Ads e Meta Ads para encher a agenda."),
         ("/seo-para-dentistas/", "SEO para dentistas", "Aparecer no Google e no Maps sem pagar por clique."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Sou dentista e quero um orçamento de site.",
        ("Me conte os tratamentos do seu consultório. Eu te digo como o site deve ser.",
         "Sem compromisso: você me diz o que atende e onde, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página para cada tratamento.", "WhatsApp com mensagem pronta.", "Equipe com CRO e fotos reais.",
         "Textos dentro das regras do CFO.", "Rápido no celular.", "Ligado ao seu Perfil no Google."],
    ),

    # ======================================================= SITE PARA ADVOGADO
    _site(
        "criacao-de-site-para-advogado", "advogado", "advogados",
        "Criação de site para advogado",
        ("Criação de site para advogado e escritório de advocacia dentro das regras da OAB: página por área de "
         "atuação, conteúdo informativo e orçamento grátis em 24h."),
        ("Quem precisa de advogado pesquisa o problema antes de pesquisar o escritório: \"direito trabalhista\", "
         "\"divórcio consensual\", \"revisão de aposentadoria\". Eu crio o site do seu escritório com uma página por "
         "área de atuação e conteúdo informativo, dentro do Provimento 205/2021 da OAB — com consultor formado em Direito."),
        "Site de escritório genérico não é encontrado por quem tem o problema",
        ["A maioria dos sites de advocacia fala do escritório: missão, valores, foto da fachada. O cliente, porém, "
         "pesquisa o problema dele. Sem página para cada área de atuação, o site não aparece para essas buscas.",
         "A OAB permite marketing jurídico informativo, com sobriedade e sem captação de clientela. Um site com "
         "conteúdo que explica direitos e caminhos é exatamente o que o Provimento 205/2021 admite — e é o que o "
         "Google mostra para quem procura.",
         "Eu sou bacharel em Direito: os textos saem com o cuidado técnico e ético que a advocacia exige."],
        ["<strong>Uma página só para todas as áreas.</strong> Nenhuma aparece no Google.",
         "<strong>Site só fala do escritório.</strong> Não responde a dúvida do cliente.",
         "<strong>Medo de ferir a OAB.</strong> E por isso o site fica parado."],
        [("Uma página por área de atuação", "Trabalhista, família, previdenciário, empresarial: cada área com "
          "conteúdo próprio e informativo."),
         ("Dentro do Provimento 205/2021", "Conteúdo informativo, sóbrio e sem captação — o que a OAB permite."),
         ("Consultor formado em Direito", "Textos revisados por quem entende a linguagem e a ética da advocacia."),
         ("Contato discreto e direto", "WhatsApp e formulário para o cliente explicar o caso, sem exposição."),
         ("Perfil dos advogados", "Formação, OAB e áreas de cada profissional — a autoridade que o cliente procura."),
         ("Ligado ao Google Maps", "Site e Perfil da Empresa do escritório apontando um para o outro.")],
        [_o("Site do escritório", "Para o escritório que ainda não tem site.",
            ["Páginas principais", "Perfil dos advogados", "Contato por WhatsApp"],
            "Olá, Renan! Sou advogado e quero um orçamento de site.", "Orçamento do meu site"),
         _o("Site por área de atuação", "Para aparecer para quem pesquisa o problema.",
            ["Uma página por área", "Conteúdo dentro da OAB", "Perfil da Empresa ligado"],
            "Olá, Renan! Sou advogado e quero um site com página por área de atuação.", "Quero aparecer no Google"),
         _o("Site + artigos", "Para construir autoridade com conteúdo informativo.",
            ["Site por área de atuação", "Artigos que respondem dúvidas", "Acompanhamento mensal"],
            "Olá, Renan! Sou advogado e quero site com artigos informativos.", "Quero site + conteúdo"),
         _o("Já tenho site e não aparece", "Para quem tem site parado.",
            ["Diagnóstico do site atual", "Plano de páginas por área", "O que dá para aproveitar"],
            "Olá, Renan! Sou advogado, tenho site e ele não aparece no Google. Pode olhar?", "Olhar meu site")],
        [("Quanto custa um site para advogado?",
          "Depende de quantas áreas de atuação precisam de página própria e se o site terá artigos. O orçamento é "
          "grátis e sai em até 24 horas pelo WhatsApp."),
         ("Site de advogado pode fazer propaganda?",
          "Pode fazer marketing jurídico informativo, com sobriedade e sem captação de clientela, como permite o "
          "Provimento 205/2021 da OAB. Não pode prometer resultado nem mercantilizar a profissão."),
         ("O site vai aparecer no Google?",
          "É feito para isso: página por área de atuação e conteúdo que responde dúvidas reais. Subir de posição "
          "leva meses, conforme a concorrência na sua cidade e área."),
         ("Vocês fazem anúncio para advogado?",
          "Sim, dentro das regras da OAB. Veja a página de tráfego pago para advogados.")],
        [("/trafego-pago-para-advogados/", "Tráfego pago para advogados", "Google Ads dentro do Provimento 205/2021."),
         ("/para-advogados/", "SEO para advogados", "Aparecer no Google e no Maps dentro das normas."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Sou advogado e quero um orçamento de site.",
        ("Me conte as áreas do seu escritório. Eu te digo como o site deve ser.",
         "Sem compromisso e com sigilo: você me diz onde atua, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página por área de atuação.", "Conteúdo dentro do Provimento 205/2021.", "Revisão de quem é formado em Direito.",
         "Perfil dos advogados com OAB.", "Contato discreto pelo WhatsApp.", "Ligado ao Perfil no Google."],
    ),

    # ======================================================= SITE PARA CONTADOR
    _site(
        "criacao-de-site-para-contador", "contador", "contadores",
        "Criação de site para contador",
        ("Criação de site para contador: página por serviço, captação de empresas pelo Google e WhatsApp em todas as páginas. Orçamento grátis em 24h."),
        ("O empresário que vai abrir empresa ou trocar de contador pesquisa no Google: \"abrir empresa em Goiânia\", "
         "\"contador para MEI\", \"trocar de contador\". Eu crio o site do seu escritório com uma página para cada "
         "serviço, pronto para aparecer nessas buscas e levar o empresário para o seu WhatsApp."),
        "Escritório de contabilidade que depende só de indicação cresce devagar",
        ["Indicação continua sendo o principal canal de muitos escritórios — e é justamente por isso que quem "
         "aparece no Google cresce mais rápido. O empresário que está abrindo CNPJ não tem indicação: ele pesquisa.",
         "Abertura de empresa, MEI, Simples Nacional, folha de pagamento, troca de contador: cada serviço é uma busca "
         "diferente. Com página própria para cada um, o seu escritório disputa todas.",
         "Site de contabilidade também precisa passar segurança: quem é o responsável, CRC, há quanto tempo atua e "
         "como funciona a migração de outro contador."],
        ["<strong>Site sem página por serviço.</strong> Não aparece para \"abrir empresa\".",
         "<strong>Não explica como trocar de contador.</strong> E o empresário desiste.",
         "<strong>Contato só por formulário.</strong> O empresário quer resposta rápida."],
        [("Uma página por serviço", "Abertura de empresa, MEI, Simples Nacional, folha, troca de contador: cada um "
          "com o que inclui e para quem é."),
         ("Página de troca de contador", "Explica como é a migração, sem dor de cabeça — a dúvida que mais trava o cliente."),
         ("WhatsApp com mensagem pronta", "O empresário já chega dizendo o que precisa."),
         ("Responsável técnico e CRC", "Quem responde pelo escritório, com registro. É o que passa segurança."),
         ("Rápido no celular", "O empresário pesquisa entre um compromisso e outro, pelo celular."),
         ("Ligado ao Google Maps", "Para aparecer quando pesquisam \"contador perto de mim\".")],
        [_o("Site do escritório", "Para o escritório que ainda não tem site.",
            ["Páginas principais", "Responsável técnico e CRC", "WhatsApp em todas as páginas"],
            "Olá, Renan! Tenho escritório de contabilidade e quero um orçamento de site.", "Orçamento do meu site"),
         _o("Site por serviço", "Para captar empresas pelo Google.",
            ["Uma página por serviço", "Página de troca de contador", "Perfil da Empresa ligado"],
            "Olá, Renan! Tenho escritório de contabilidade e quero um site com página por serviço.", "Quero captar pelo Google"),
         _o("Site + anúncio", "Para captar empresas enquanto o site sobe.",
            ["Site por serviço", "Google Ads para abertura de empresa", "Contatos medidos"],
            "Olá, Renan! Tenho escritório de contabilidade e quero site e anúncio.", "Quero site + anúncio"),
         _o("Já tenho site e não aparece", "Para quem tem site parado.",
            ["Diagnóstico do site atual", "Plano de páginas por serviço", "O que dá para aproveitar"],
            "Olá, Renan! Tenho escritório de contabilidade e o site não aparece no Google. Pode olhar?", "Olhar meu site")],
        [("Quanto custa um site para contador?",
          "Depende de quantos serviços precisam de página própria e de quem escreve os textos. O orçamento é grátis "
          "e sai em até 24 horas pelo WhatsApp."),
         ("Site de contabilidade traz cliente mesmo?",
          "Traz quando tem página para cada serviço que o empresário pesquisa — abrir empresa, MEI, trocar de "
          "contador — e está ligado ao Perfil da Empresa no Google."),
         ("Posso atender clientes de outras cidades pelo site?",
          "Pode. Contabilidade online atende o Brasil inteiro, e o site pode ter páginas para as cidades que você "
          "quer disputar."),
         ("Vocês fazem anúncio para contabilidade?",
          "Sim. A RCB faz a gestão de Google Ads e Meta Ads, com foco em buscas como abertura de empresa e troca de contador.")],
        [("/seo-para-contadores/", "SEO para contadores", "Aparecer no Google e no Maps sem pagar por clique."),
         ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Google Ads e Meta Ads para captar empresas."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Tenho escritório de contabilidade e quero um orçamento de site.",
        ("Me conte os serviços do seu escritório. Eu te digo como o site deve ser.",
         "Sem compromisso: você me diz o que atende e onde, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página para cada serviço.", "Página de troca de contador.", "Responsável técnico e CRC.",
         "WhatsApp com mensagem pronta.", "Rápido no celular.", "Ligado ao seu Perfil no Google."],
    ),

    # ======================================================= SITE PARA ESTÉTICA
    _site(
        "criacao-de-site-para-clinica-de-estetica", "clínica de estética", "estética",
        "Criação de site para clínica de estética",
        ("Criação de site para clínica de estética: página por procedimento, fotos reais e WhatsApp em todas as páginas. Feito para o Google. Orçamento em 24h."),
        ("A paciente pesquisa o procedimento antes de escolher a clínica: \"harmonização facial\", \"depilação a laser\", "
         "\"limpeza de pele\". Eu crio o site da sua clínica com uma página para cada procedimento, fotos reais do "
         "espaço e o botão de WhatsApp sempre à mão — pensado para aparecer no Google."),
        "Clínica de estética que vive só do Instagram fica refém do algoritmo",
        ["O Instagram mostra o seu trabalho, mas quem pesquisa \"botox em Goiânia\" no Google não cai no seu perfil — "
         "cai no site de quem tem página para aquele procedimento.",
         "Site de estética precisa responder o que a paciente quer saber antes de marcar: como é o procedimento, "
         "quem faz, quanto tempo dura, qual o cuidado depois. Com clareza e sem promessa de resultado.",
         "Com página por procedimento e ligação com o Perfil da Empresa, a clínica passa a receber paciente do Google "
         "sem depender só do alcance das postagens."],
        ["<strong>Só Instagram, sem site.</strong> Não aparece na busca do Google.",
         "<strong>Site com lista de procedimentos.</strong> Nenhum tem página própria.",
         "<strong>Paciente não sabe quem faz.</strong> Falta equipe e registro profissional."],
        [("Uma página por procedimento", "Harmonização, laser, limpeza de pele, protocolos corporais: cada um com "
          "o que é, como funciona e cuidados."),
         ("Fotos reais do espaço", "A paciente quer ver onde vai ser atendida. Foto de banco de imagem não convence."),
         ("Equipe e registro profissional", "Quem faz cada procedimento, com formação e registro no conselho."),
         ("WhatsApp com mensagem pronta", "A paciente já chega dizendo qual procedimento quer."),
         ("Sem promessa de resultado", "Textos informativos, dentro das regras de publicidade em saúde."),
         ("Ligado ao Google Maps", "Para aparecer quando a paciente pesquisa perto de casa.")],
        [_o("Site da clínica", "Para a clínica que ainda não tem site.",
            ["Páginas principais", "Fotos reais do espaço", "WhatsApp em todas as páginas"],
            "Olá, Renan! Tenho uma clínica de estética e quero um orçamento de site.", "Orçamento do meu site"),
         _o("Site por procedimento", "Para aparecer quando a paciente pesquisa o procedimento.",
            ["Uma página por procedimento", "Equipe com registro", "Perfil da Empresa ligado"],
            "Olá, Renan! Tenho uma clínica de estética e quero um site com página por procedimento.", "Quero aparecer no Google"),
         _o("Site + anúncio", "Para encher a agenda enquanto o site sobe.",
            ["Site por procedimento", "Anúncio no Google e no Instagram", "Contatos medidos"],
            "Olá, Renan! Tenho uma clínica de estética e quero site e anúncio.", "Quero site + anúncio"),
         _o("Já tenho site e não aparece", "Para quem tem site parado.",
            ["Diagnóstico do site atual", "Plano de páginas por procedimento", "O que dá para aproveitar"],
            "Olá, Renan! Tenho clínica de estética e o site não aparece no Google. Pode olhar?", "Olhar meu site")],
        [("Quanto custa um site para clínica de estética?",
          "Depende de quantos procedimentos precisam de página própria, das fotos e de quem escreve os textos. O "
          "orçamento é grátis e sai em até 24 horas pelo WhatsApp."),
         ("Instagram não basta para clínica de estética?",
          "O Instagram mostra o trabalho, mas não aparece para quem pesquisa o procedimento no Google. O site com "
          "página por procedimento pega essa paciente, que já está decidida a marcar."),
         ("Posso mostrar antes e depois no site?",
          "Depende das regras do conselho do profissional responsável. Na dúvida, prefira conteúdo educativo e sempre "
          "com autorização da paciente."),
         ("Vocês fazem anúncio para estética?",
          "Sim. A RCB faz a gestão de Google Ads e Meta Ads para clínicas, com cuidado com as políticas de anúncios de saúde.")],
        [("/seo-para-clinicas-de-estetica/", "SEO para clínicas de estética", "Aparecer no Google e no Maps sem pagar por clique."),
         ("/blog/trafego-pago-para-clinicas/", "Tráfego pago para clínicas", "Google Ads e Meta Ads dentro das regras."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Tenho uma clínica de estética e quero um orçamento de site.",
        ("Me conte os procedimentos da sua clínica. Eu te digo como o site deve ser.",
         "Sem compromisso: você me diz o que atende e onde, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página por procedimento.", "Fotos reais do espaço.", "Equipe com registro profissional.",
         "WhatsApp com mensagem pronta.", "Sem promessa de resultado.", "Ligado ao seu Perfil no Google."],
    ),

    # ======================================================= TRÁFEGO DENTISTAS
    _trafego(
        "trafego-pago-para-dentistas", "dentistas",
        "Tráfego pago para dentistas",
        "Tráfego Pago para Dentistas: Google Ads e Meta Ads | RCB",
        ("Tráfego pago para dentistas: Google Ads e Meta Ads para encher a agenda de implante e ortodontia, dentro das regras do CFO. Orçamento grátis em 24h."),
        ("O paciente de implante, lente ou aparelho pesquisa no Google e decide em poucos cliques. Eu monto e acompanho "
         "os anúncios do seu consultório no Google e no Instagram para que esse paciente chame você no WhatsApp — "
         "dentro das regras do CFO e sem queimar verba com curioso."),
        "Anúncio de dentista mal feito atrai curioso e irrita o conselho",
        ["\"Implante grátis\", \"avaliação gratuita\", \"sorriso perfeito\": o anúncio agressivo atrai quem procura "
         "preço baixo e ainda pode ferir as regras do CFO. O resultado é agenda cheia de avaliação que não fecha.",
         "O anúncio certo de odontologia aparece para quem pesquisa o tratamento na sua região, leva para a página "
         "daquele tratamento e deixa a recepção pronta para responder rápido.",
         "Cada tratamento tem sua campanha — implante, ortodontia, estética — para você saber qual traz paciente e "
         "colocar a verba onde dá retorno."],
        ["<strong>Muita avaliação, pouco tratamento fechado.</strong> O anúncio atrai o paciente errado.",
         "<strong>Campanha única para tudo.</strong> Ninguém sabe qual tratamento dá retorno.",
         "<strong>Anúncio leva para a página inicial.</strong> O paciente não acha o que clicou."],
        "Anúncio de odontologia dentro das regras do CFO",
        ["O Código de Ética Odontológica e as resoluções do <a href=\"https://website.cfo.org.br/\" target=\"_blank\" "
         "rel=\"noopener noreferrer\">CFO</a> definem o que pode e o que não pode na divulgação. Os pontos mais "
         "sensíveis em anúncio são promessa de resultado, preço como chamariz e o uso de imagens de pacientes.",
         "A campanha já nasce dentro dessas regras e das políticas de anúncios de saúde do Google e do Meta: texto "
         "informativo, identificação do responsável técnico e nada de \"garantia\" de resultado.",
         "Isso não deixa o anúncio fraco. O paciente de tratamento de valor alto confia mais em quem informa do que "
         "em quem promete."],
        [("Campanha por tratamento", "Implante, ortodontia, estética dental e clínica geral separados, com verba própria."),
         ("Buscas bloqueadas", "\"Grátis\", \"SUS\", \"curso\", \"vaga\": fora do anúncio para não queimar verba."),
         ("Raio certo", "Anúncio só para a região de onde o paciente realmente vem."),
         ("Página por tratamento", "O clique cai na página do tratamento, com WhatsApp. Se não existir, a gente cria."),
         ("Instagram para gerar demanda", "Vídeos educativos e apresentação do dentista para quem mora perto."),
         ("Relatório claro", "Quantas conversas vieram por tratamento e quanto custou cada uma.")],
        [_o("Google Ads para dentistas", "Para quem já pesquisa o tratamento na sua região.",
            ["Campanha por tratamento", "Buscas bloqueadas", "Raio certo"],
            "Olá, Renan! Sou dentista e quero um orçamento de Google Ads.", "Orçamento de Google Ads"),
         _o("Instagram e Facebook", "Para apresentar o consultório a quem mora perto.",
            ["Conteúdo educativo", "Conversa no WhatsApp", "Dentro das regras do CFO"],
            "Olá, Renan! Sou dentista e quero anunciar no Instagram.", "Orçamento de Meta Ads"),
         _o("Anúncio + página do tratamento", "Para quem anuncia e não converte.",
            ["Landing page por tratamento", "Google Ads ou Meta Ads", "Contatos medidos"],
            "Olá, Renan! Sou dentista e quero anúncio com página do tratamento.", "Quero anúncio + página"),
         _o("Já anuncio e não funciona", "Para quem já investe e não vê o WhatsApp tocar.",
            ["Diagnóstico da conta", "Corte do que gasta sem retorno", "Plano de ajuste"],
            "Olá, Renan! Sou dentista, já anuncio e não está trazendo paciente. Pode olhar?", "Olhar meus anúncios")],
        [("Quanto custa o tráfego pago para dentista?",
          "São dois valores: a verba do anúncio, paga direto ao Google ou ao Meta, e a gestão. O valor da gestão "
          "depende de quantos tratamentos e canais entram. O orçamento é grátis e sai em até 24 horas."),
         ("Dentista pode anunciar no Google?",
          "Pode, dentro das regras do CFO e das políticas de saúde do Google: sem promessa de resultado, sem preço como "
          "chamariz e com identificação do responsável técnico."),
         ("Qual tratamento vale mais a pena anunciar?",
          "Em geral, os de valor mais alto — implante, ortodontia, estética dental —, porque suportam o custo do clique. "
          "A campanha separada por tratamento mostra na prática qual dá retorno no seu consultório."),
         ("Em quanto tempo o anúncio traz paciente?",
          "Os primeiros contatos podem vir nos primeiros dias, mas as primeiras semanas são de ajuste. O que dá para "
          "cobrar desde o começo é medição: quantas conversas e de qual tratamento.")],
        [("/criacao-de-site-para-dentista/", "Criação de site para dentista", "O site com página por tratamento."),
         ("/blog/trafego-pago-para-clinicas/", "Tráfego pago para clínicas", "As regras e os cuidados em detalhe."),
         ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
        "Olá, Renan! Sou dentista e quero um orçamento de tráfego pago.",
        ("Me conte os tratamentos que você quer encher na agenda.",
         "Sem compromisso: se você já anuncia, eu olho as campanhas; se não, te digo por onde começar."),
        ["Campanha separada por tratamento.", "Buscas erradas bloqueadas.", "Anúncio só na sua região.",
         "Página certa para cada clique.", "Dentro das regras do CFO.", "Relatório de conversas por tratamento."],
    ),

    # ======================================================= TRÁFEGO ADVOGADOS
    _trafego(
        "trafego-pago-para-advogados", "advogados",
        "Tráfego pago para advogados",
        "Tráfego Pago para Advogados: Google Ads Dentro da OAB | RCB",
        ("Tráfego pago para advogados: Google Ads e Meta Ads dentro do Provimento 205/2021 da OAB, com consultor "
         "formado em Direito. Orçamento grátis em 24h."),
        ("Quem tem um problema jurídico pesquisa no Google: \"advogado trabalhista\", \"divórcio\", \"aposentadoria "
         "negada\". O anúncio coloca o seu escritório nessa busca hoje. Eu monto e acompanho as campanhas dentro do "
         "Provimento 205/2021 da OAB — com o cuidado de quem é formado em Direito."),
        "Advogado que anuncia sem conhecer a OAB corre risco duas vezes",
        ["O anúncio jurídico feito por agência genérica costuma cometer os mesmos erros: promessa de êxito, "
         "linguagem de captação, apelo emocional. Além de ferir a OAB, atrai o cliente errado.",
         "O Provimento 205/2021 permite o impulsionamento e o anúncio pago, desde que informativo, sóbrio e sem "
         "captação de clientela. Dentro dessas regras, o anúncio no Google é um dos canais mais eficientes para "
         "o escritório.",
         "Eu sou bacharel em Direito: cada anúncio sai revisado com o cuidado técnico e ético da advocacia."],
        ["<strong>Cliques de quem procura \"advogado grátis\".</strong> Sem filtro de busca.",
         "<strong>Anúncio com promessa de resultado.</strong> Risco ético.",
         "<strong>Contato não qualificado.</strong> Muita conversa, pouco caso bom."],
        "Anúncio jurídico dentro do Provimento 205/2021 da OAB",
        ["O Provimento 205/2021 do <a href=\"https://www.oab.org.br/\" target=\"_blank\" rel=\"noopener noreferrer\">"
         "Conselho Federal da OAB</a> trata da publicidade na advocacia. Em resumo: o marketing jurídico deve ser "
         "informativo e sóbrio; é vedada a captação de clientela, a mercantilização da profissão e a promessa de resultado.",
         "Na prática, o anúncio fala da área de atuação e do direito do cliente, leva para uma página informativa e "
         "abre um canal de contato. Nada de \"ganhe sua causa\", nada de valores de honorários no anúncio.",
         "Cada seccional pode ter orientações próprias. Na dúvida, a campanha é ajustada para o lado conservador."],
        [("Campanha por área de atuação", "Trabalhista, família, previdenciário, empresarial: cada área com sua verba."),
         ("Buscas bloqueadas", "\"Grátis\", \"defensoria\", \"modelo de petição\", \"curso\": fora do anúncio."),
         ("Texto dentro da OAB", "Anúncios informativos, revisados por quem é formado em Direito."),
         ("Página informativa", "O clique cai numa página que explica o direito, com contato discreto."),
         ("Região certa", "Anúncio para as cidades e comarcas que o escritório atende."),
         ("Relatório claro", "Quantos contatos vieram por área e quanto custou cada um.")],
        [_o("Google Ads para advogados", "Para quem pesquisa a área de atuação.",
            ["Campanha por área", "Buscas bloqueadas", "Texto dentro da OAB"],
            "Olá, Renan! Sou advogado e quero um orçamento de Google Ads.", "Orçamento de Google Ads"),
         _o("Anúncio + página informativa", "Para transformar clique em contato qualificado.",
            ["Landing page por área", "Conteúdo informativo", "Contato discreto"],
            "Olá, Renan! Sou advogado e quero anúncio com página informativa.", "Quero anúncio + página"),
         _o("Meta Ads informativo", "Para conteúdo educativo sobre direitos na sua região.",
            ["Conteúdo informativo", "Público por região", "Dentro da OAB"],
            "Olá, Renan! Sou advogado e quero anunciar conteúdo no Instagram.", "Orçamento de Meta Ads"),
         _o("Já anuncio e não funciona", "Para quem já investe e só recebe contato ruim.",
            ["Diagnóstico da conta", "Filtro de buscas", "Plano de ajuste"],
            "Olá, Renan! Sou advogado, já anuncio e os contatos não são bons. Pode olhar?", "Olhar meus anúncios")],
        [("Quanto custa o tráfego pago para advogado?",
          "São dois valores: a verba do anúncio, paga direto ao Google ou ao Meta, e a gestão. O clique jurídico "
          "costuma ser mais caro que o de outros ramos, por isso o filtro de buscas pesa tanto. O orçamento é grátis "
          "e sai em até 24 horas."),
         ("Advogado pode anunciar no Google?",
          "Pode. O Provimento 205/2021 da OAB admite o anúncio pago, desde que informativo, sóbrio e sem captação de "
          "clientela, sem promessa de resultado e sem mercantilização."),
         ("Posso colocar valor de honorários no anúncio?",
          "Não é recomendado. A divulgação de valores como chamariz é vista como mercantilização. O anúncio deve "
          "falar da área e do direito, e o valor é tratado na consulta."),
         ("Qual área jurídica vale anunciar?",
          "Depende da sua cidade e da concorrência. Áreas com muita busca e casos de valor — trabalhista, "
          "previdenciário, família — costumam responder bem, mas a campanha separada por área mostra na prática.")],
        [("/criacao-de-site-para-advogado/", "Criação de site para advogado", "O site por área de atuação."),
         ("/marketing-para-advogados/", "Marketing para advogados", "O caminho completo dentro das normas da OAB."),
         ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
        "Olá, Renan! Sou advogado e quero um orçamento de tráfego pago.",
        ("Me conte as áreas do seu escritório. Eu te digo como anunciar dentro da OAB.",
         "Sem compromisso e com sigilo: se você já anuncia, eu olho as campanhas; se não, te digo por onde começar."),
        ["Campanha por área de atuação.", "Buscas erradas bloqueadas.", "Texto dentro do Provimento 205/2021.",
         "Página informativa para o clique.", "Anúncio só nas comarcas atendidas.", "Relatório de contatos por área."],
    ),

    # ======================================================= TRÁFEGO ENERGIA SOLAR
    _trafego(
        "trafego-pago-para-energia-solar", "energia solar",
        "Tráfego pago para energia solar",
        "Tráfego Pago para Energia Solar: Google Ads e Meta Ads | RCB",
        ("Tráfego pago para energia solar: Google Ads e Meta Ads para gerar pedidos de orçamento na sua região, sem pagar clique de curioso. Orçamento em 24h."),
        ("Quem pesquisa \"orçamento energia solar\" já decidiu instalar — só falta escolher quem. Eu monto e "
         "acompanho os anúncios da sua integradora no Google e no Instagram para que esse cliente peça orçamento "
         "para você, e não para as outras cinco empresas da cidade."),
        "Energia solar é o anúncio mais disputado do bairro",
        ["Em muitas cidades há dezenas de integradoras anunciando o mesmo kit. Sem filtro, o anúncio paga clique de "
         "quem quer curso, vaga de instalador ou \"energia solar grátis\" — e a verba acaba antes do cliente certo chegar.",
         "O anúncio que funciona separa residencial, comercial e rural, fala para a região que você atende e leva para "
         "uma página que pede a informação certa: o valor da conta de luz.",
         "Sem promessa de economia exata. Economia depende do consumo e da tarifa — a simulação acontece na conversa."],
        ["<strong>Muito clique, pouco orçamento pedido.</strong> Sem filtro de busca.",
         "<strong>Anúncio promete economia fixa.</strong> Atrai curioso e gera desconfiança.",
         "<strong>Mesmo anúncio para casa e fazenda.</strong> Cliente e mensagem diferentes."],
        "Como anunciar energia solar sem queimar verba",
        ["O primeiro trabalho é a lista de buscas bloqueadas: curso, vaga, \"como fazer placa solar\", \"energia "
         "solar grátis\", kits para instalar sozinho. Cada busca bloqueada é verba que sobra para quem vai comprar.",
         "Depois, campanhas separadas por tipo de cliente — residencial, comercial e rural — com mensagem e página "
         "próprias. O produtor rural que pesquisa bombeamento solar não quer ler sobre telhado de casa.",
         "No Instagram, obras reais da sua região e a conta de luz antes e depois (com autorização) geram mais "
         "confiança do que qualquer arte com \"economize 95%\"."],
        [("Campanha por tipo de cliente", "Residencial, comercial e rural separados, cada um com mensagem própria."),
         ("Buscas bloqueadas", "Curso, vaga, \"grátis\" e \"como fazer\" fora do anúncio."),
         ("Região que você atende", "Anúncio só nas cidades onde você instala."),
         ("Página que pede a conta de luz", "O clique cai numa página que qualifica o pedido. Se não existir, a gente cria."),
         ("Instagram com obras reais", "Criativos com instalações da sua região para gerar demanda."),
         ("Relatório de orçamentos", "Quantos pedidos vieram por tipo de cliente e quanto custou cada um.")],
        [_o("Google Ads para energia solar", "Para quem já pesquisa orçamento na sua região.",
            ["Campanha por tipo de cliente", "Buscas bloqueadas", "Região certa"],
            "Olá, Renan! Tenho empresa de energia solar e quero um orçamento de Google Ads.", "Orçamento de Google Ads"),
         _o("Instagram e Facebook", "Para gerar demanda com obras reais.",
            ["Criativos com obras da região", "Conversa no WhatsApp", "Público por região"],
            "Olá, Renan! Tenho empresa de energia solar e quero anunciar no Instagram.", "Orçamento de Meta Ads"),
         _o("Anúncio + página de orçamento", "Para transformar clique em pedido qualificado.",
            ["Landing page por tipo de cliente", "Pergunta da conta de luz", "Contatos medidos"],
            "Olá, Renan! Tenho empresa de energia solar e quero anúncio com página de orçamento.", "Quero anúncio + página"),
         _o("Já anuncio e não funciona", "Para quem já investe e recebe pouco pedido.",
            ["Diagnóstico da conta", "Filtro de buscas", "Plano de ajuste"],
            "Olá, Renan! Tenho empresa de energia solar, já anuncio e não está funcionando. Pode olhar?", "Olhar meus anúncios")],
        [("Quanto custa o tráfego pago para energia solar?",
          "São dois valores: a verba do anúncio, paga direto ao Google ou ao Meta, e a gestão. O valor da gestão "
          "depende de quantos tipos de cliente e canais entram. O orçamento é grátis e sai em até 24 horas."),
         ("Google Ads ou Instagram para energia solar?",
          "O Google traz quem já está pedindo orçamento; o Instagram gera demanda mostrando obras. Para pedidos no "
          "curto prazo, o Google costuma vir primeiro."),
         ("Posso prometer economia no anúncio?",
          "Evite número exato. A economia depende do consumo e da tarifa de cada cliente. Casos reais com autorização "
          "funcionam melhor e não geram frustração."),
         ("Por que recebo contato de gente que não compra?",
          "Normalmente por falta de buscas bloqueadas e de uma página que peça o valor da conta de luz. Os dois "
          "filtram o curioso antes da conversa.")],
        [("/blog/como-conseguir-clientes-energia-solar/", "Como conseguir clientes de energia solar", "Maps, site e anúncios juntos."),
         ("/blog/site-para-empresa-de-energia-solar/", "Site para empresa de energia solar", "O que o site precisa ter."),
         ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
        "Olá, Renan! Tenho empresa de energia solar e quero um orçamento de tráfego pago.",
        ("Me conte as cidades onde você instala. Eu te digo como encher a agenda de visitas.",
         "Sem compromisso: se você já anuncia, eu olho as campanhas; se não, te digo por onde começar."),
        ["Campanha por tipo de cliente.", "Buscas de curso e vaga bloqueadas.", "Anúncio só onde você instala.",
         "Página que pede a conta de luz.", "Instagram com obras reais.", "Relatório de pedidos de orçamento."],
    ),

    # ======================================================= TRÁFEGO IMOBILIÁRIAS
    _trafego(
        "trafego-pago-para-imobiliarias", "imobiliárias",
        "Tráfego pago para imobiliárias",
        "Tráfego Pago para Imobiliárias: Leads Sem Depender de Portal",
        ("Tráfego pago para imobiliárias: Google Ads e Meta Ads para gerar leads próprios de compra, venda e locação, sem depender de portal. Orçamento em 24h."),
        ("Portal imobiliário cobra caro e entrega o mesmo lead para cinco imobiliárias. Com anúncio próprio no Google "
         "e no Instagram, o interessado chama direto você. Eu monto e acompanho as campanhas da sua imobiliária para "
         "gerar leads de compra, venda e locação na sua região."),
        "Depender de portal é dividir cada lead com a concorrência",
        ["No portal, o interessado vê o imóvel de várias imobiliárias lado a lado — e o lead chega disputado. Com "
         "anúncio próprio, o contato chega exclusivo, direto no seu WhatsApp.",
         "O anúncio imobiliário funciona melhor quando separa objetivos: quem quer comprar, quem quer alugar e — o "
         "mais valioso — quem quer vender ou colocar o imóvel para alugar.",
         "Anúncios de imóveis também têm regras nas plataformas, como as políticas de habitação do Google e do Meta. "
         "A campanha já nasce respeitando essas regras."],
        ["<strong>Todo lead vem do portal.</strong> E chega disputado.",
         "<strong>Poucos imóveis para captar.</strong> Ninguém anuncia para proprietário.",
         "<strong>Anúncio leva para a lista de imóveis.</strong> O interessado se perde."],
        "Como anunciar imóveis dentro das regras das plataformas",
        ["O Google e o Meta tratam anúncio de imóvel como categoria especial: há limites de segmentação por idade, "
         "gênero e CEP para evitar discriminação. Campanha montada sem esse cuidado pode ser reprovada.",
         "Dentro dessas regras, o que funciona é segmentar por região e interesse, anunciar lançamentos e imóveis "
         "de destaque com página própria e criar campanhas para captar proprietários que querem vender ou alugar.",
         "O corretor também precisa exibir o CRECI na divulgação, como exige a regulamentação da profissão."],
        [("Campanha por objetivo", "Compra, locação e captação de imóveis separadas, cada uma com sua verba."),
         ("Captação de proprietários", "Anúncio para quem quer vender ou alugar — o lead que mais vale."),
         ("Página por imóvel ou lançamento", "O clique cai na página do imóvel, com WhatsApp e fotos."),
         ("Dentro das regras das plataformas", "Segmentação permitida para anúncios de habitação."),
         ("Região certa", "Anúncio nos bairros e cidades onde a imobiliária atua."),
         ("Relatório de leads", "Quantos contatos por objetivo e quanto custou cada um.")],
        [_o("Google Ads para imobiliárias", "Para quem pesquisa imóvel na sua região.",
            ["Campanha por objetivo", "Buscas bloqueadas", "Região certa"],
            "Olá, Renan! Tenho uma imobiliária e quero um orçamento de Google Ads.", "Orçamento de Google Ads"),
         _o("Instagram e Facebook", "Para lançamentos e imóveis de destaque.",
            ["Criativos por imóvel", "Conversa no WhatsApp", "Dentro das regras de habitação"],
            "Olá, Renan! Tenho uma imobiliária e quero anunciar no Instagram.", "Orçamento de Meta Ads"),
         _o("Captação de imóveis", "Para aumentar a carteira com proprietários.",
            ["Campanha para quem quer vender", "Campanha para quem quer alugar", "Página de captação"],
            "Olá, Renan! Tenho uma imobiliária e quero captar mais imóveis.", "Quero captar imóveis"),
         _o("Já anuncio e não funciona", "Para quem já investe e recebe lead ruim.",
            ["Diagnóstico da conta", "Filtro de públicos", "Plano de ajuste"],
            "Olá, Renan! Tenho uma imobiliária, já anuncio e os leads não são bons. Pode olhar?", "Olhar meus anúncios")],
        [("Quanto custa o tráfego pago para imobiliária?",
          "São dois valores: a verba do anúncio, paga direto ao Google ou ao Meta, e a gestão. O valor da gestão "
          "depende de quantos objetivos e canais entram. O orçamento é grátis e sai em até 24 horas."),
         ("Anúncio próprio substitui o portal?",
          "Pode reduzir muito a dependência. O lead do anúncio próprio chega exclusivo, enquanto o do portal chega "
          "disputado. Muitas imobiliárias usam os dois e cortam o portal aos poucos."),
         ("Dá para captar imóveis com anúncio?",
          "Dá. Campanhas para proprietários que querem vender ou alugar costumam ser as mais valiosas, porque "
          "aumentam a carteira da imobiliária."),
         ("Por que meu anúncio de imóvel foi reprovado?",
          "Anúncio de imóvel é categoria especial no Google e no Meta, com limites de segmentação. Campanha montada "
          "sem esse cuidado costuma ser reprovada ou limitada.")],
        [("/blog/como-gerar-leads-imobiliaria-sem-portais/", "Leads sem depender de portal", "O caminho completo para a imobiliária."),
         ("/seo-para-imobiliarias/", "SEO para imobiliárias", "Aparecer no Google e no Maps sem pagar por clique."),
         ("/gestao-de-trafego-pago-goiania/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
        "Olá, Renan! Tenho uma imobiliária e quero um orçamento de tráfego pago.",
        ("Me conte onde a sua imobiliária atua. Eu te digo como gerar lead próprio.",
         "Sem compromisso: se você já anuncia, eu olho as campanhas; se não, te digo por onde começar."),
        ["Campanha por objetivo.", "Captação de proprietários.", "Página por imóvel.",
         "Dentro das regras de habitação.", "Anúncio só na sua região.", "Relatório de leads por objetivo."],
    ),
]
