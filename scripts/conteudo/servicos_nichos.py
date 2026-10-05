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
        "pills": ["Orçamento em até 24h", "Feito para %s" % nicho_pl, "Prazo por escrito"],
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
    d = {
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
    return _aplica_extra(d)


def _aplica_extra(d):
    """Etapa 3 (04/10/2026): troca os blocos repetidos pelo texto proprio do nicho (TRAFEGO_EXTRA)."""
    x = TRAFEGO_EXTRA.get(d["slug"])
    if not x:
        return d
    for k in ("title", "desc", "eyebrow", "pills", "faq_titulo", "publico", "relacionados", "cta_hero", "painel_h2"):
        if k in x:
            d[k] = x[k]
    d["nacional"] = True
    d["data"] = "2026-10-04"
    novas = []
    for tipo, s in d["secoes"]:
        s = dict(s)
        if tipo == "split":
            s["card_titulo"] = x.get("card_titulo", s["card_titulo"])
            s["tag"] = x.get("split_tag", s["tag"])
        elif tipo == "texto" and s.get("tag") == "Regras e cuidados":
            s["ps"] = x.get("regras_ps", s["ps"])
            s["titulo"] = x.get("regras_titulo", s["titulo"])
            s["tag"] = x.get("regras_tag", s["tag"])
        elif tipo == "cards":
            s["titulo"] = x.get("entra_titulo", s["titulo"])
            s["tag"] = x.get("entra_tag", s["tag"])
        elif tipo == "faixas" and "quanto_ps" in x:
            tipo, s = "texto", {"tag": "Quanto investir", "titulo": x["quanto_titulo"], "ps": x["quanto_ps"]}
        elif tipo == "orcamento":
            s["titulo"] = x.get("orc_titulo", s["titulo"])
            s["desc"] = x.get("orc_desc", s["desc"])
            s["itens"] = x.get("orc", s["itens"])
        elif tipo == "passos" and "passos" in x:
            s = {"titulo": x["passos_titulo"], "itens": x["passos"]}
        novas.append((tipo, s))
    d["secoes"] = novas
    return d


def _o(nome, para, itens, msg, botao):
    return (nome, para, itens, msg, botao)


# ---------------------------------------------------------------------------
# Etapa 3 do plano de nichos (04/10/2026): texto PROPRIO de cada nicho no lugar
# dos blocos que eram iguais nas 4 paginas (semelhanca medida: 51-56%, meta < 40%).
# Google Ads em primeiro lugar; Meta Ads so como complemento. Fontes oficiais
# conferidas em 04/10/2026. _trafego() usa estas chaves quando existem.
# ---------------------------------------------------------------------------
_OAB = "https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021"
_CFO = "https://website.cfo.org.br/resolucao-cfo-196-2019/"
_COFECI = "https://intranet.cofeci.gov.br/arquivos/legislacao/resolucao_0458_95_nova.pdf"
_L14300 = "https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm"
_CDC = "https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm"


def _a(url, txt):
    return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (url, txt)


TRAFEGO_EXTRA = {
    "trafego-pago-para-dentistas": {
        "title": "Tráfego Pago para Dentistas: Google Ads Dentro do CFO | RCB SEO",
        "desc": ("Tráfego pago para dentistas: Google Ads por tratamento, dentro das regras do CFO, levando o "
                 "paciente para o WhatsApp do consultório. Orçamento grátis em 24h."),
        "publico": "Dentistas, consultórios e clínicas odontológicas",
        "eyebrow": "Google Ads para consultórios odontológicos",
        "pills": ["Orçamento em até 24h", "Campanha por tratamento", "Dentro das regras do CFO"],
        "card_titulo": "Sinais de que a verba do consultório está indo embora",
        "regras_ps": [
            "A " + _a(_CFO, "Resolução CFO-196/2019") + " liberou, com regras, a divulgação de selfies e de imagens "
            "de diagnóstico e de conclusão do tratamento — sempre com autorização escrita do paciente e com o nome "
            "e o número de inscrição do dentista na imagem. A mesma resolução mantém proibidas expressões de "
            "sensacionalismo, autopromoção, mercantilização da odontologia e promessa de resultado.",
            "Na prática, isso muda o texto do anúncio: sai \"sorriso perfeito garantido\" e \"avaliação grátis\" como "
            "isca; entra a informação do tratamento, a região de atendimento e o convite para conversar. Imagem de "
            "antes e depois só do próprio profissional, com o termo assinado; clínica como pessoa jurídica não pode "
            "divulgar esse tipo de imagem, segundo o próprio CFO.",
            "Isso não enfraquece o anúncio. Quem pesquisa implante ou alinhador compara com calma, e confia mais em "
            "quem explica do que em quem promete.",
        ],
        "quanto_titulo": "Quanto um consultório precisa investir em Google Ads?",
        "quanto_ps": [
            "A conta começa pelo tratamento, não pelo anúncio. Um implante ou um tratamento ortodôntico vale muito "
            "mais para o consultório do que uma limpeza, então aguenta um clique mais caro e merece campanha "
            "própria. Por isso a verba é dividida por tratamento: você enxerga quanto custou cada conversa de "
            "implante e cada conversa de aparelho.",
            "São dois valores separados: a verba, que você paga direto ao Google no seu cartão, e a gestão, que é o "
            "trabalho de montar, ajustar e medir. Dá para começar com um ou dois tratamentos e ampliar quando a "
            "agenda responder. O orçamento da gestão é grátis e sai em até 24 horas.",
        ],
        "orc_titulo": "Por qual tratamento o seu consultório quer começar?",
        "orc_desc": "Escolha o ponto de partida. Em até 24 horas você recebe o valor da gestão e uma sugestão de verba por tratamento.",
        "passos_titulo": "Como o anúncio do seu consultório sai do papel",
        "passos": [
            ("Escolha dos tratamentos", "Você me diz quais tratamentos quer encher na agenda e de onde vêm os seus pacientes."),
            ("Revisão das regras do CFO", "Texto e imagens conferidos antes de ir ao ar: sem promessa, sem preço como isca."),
            ("Página do tratamento", "Cada campanha leva para a página daquele tratamento, com o WhatsApp da recepção."),
            ("Medição por tratamento", "Relatório de quantas conversas cada tratamento trouxe e quanto custou cada uma."),
        ],
        "faq_titulo": "Perguntas frequentes sobre Google Ads para dentistas",
        "relacionados": [
            ("/seo-para-dentistas/", "SEO para dentistas", "Aparecer no Google e no Maps sem pagar por clique."),
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago para empresas", "Como funciona a gestão de Google Ads da RCB SEO."),
            ("/criacao-de-site-para-dentista/", "Criação de site para dentista", "O site com página por tratamento."),
        ],
    },
    "trafego-pago-para-advogados": {
        "desc": ("Tráfego pago para advogados: Google Ads por área de atuação, dentro do Provimento 205/2021 da OAB, "
                 "com informação e sem captação. Orçamento grátis em 24h."),
        "publico": "Advogados e escritórios de advocacia",
        "eyebrow": "Google Ads para escritórios de advocacia",
        "pills": ["Orçamento em até 24h", "Campanha por área do Direito", "Dentro do Provimento 205/2021"],
        "card_titulo": "Sinais de que o anúncio do escritório está mal montado",
        "regras_ps": [
            "O " + _a(_OAB, "Provimento 205/2021 do Conselho Federal da OAB") + " admite anúncios, pagos ou não, na "
            "publicidade da advocacia (art. 4º), desde que não haja mercantilização, captação de clientela ou "
            "emprego excessivo de recursos financeiros. O mesmo provimento proíbe a promessa de resultado e o uso de "
            "casos concretos para oferecer serviço (art. 6º).",
            "No Google Ads, isso significa anúncio informativo: a área do Direito, a região, o formato de "
            "atendimento e um convite para tirar dúvidas. Nada de \"ganhe sua causa\", \"indenização garantida\" ou "
            "\"o melhor advogado da cidade\". A página que recebe o clique segue a mesma linha: explica o tema e "
            "identifica o profissional com o número da OAB.",
            "Quem monta a campanha conhece essas regras: o Renan é bacharel em Direito, o que ajuda a separar o que "
            "é informação do que pode ser lido como captação. A conferência final do texto continua sendo do "
            "advogado responsável.",
        ],
        "quanto_titulo": "Quanto um escritório precisa investir em Google Ads?",
        "quanto_ps": [
            "Cada área do Direito tem um custo de clique diferente, e um cliente de direito empresarial costuma "
            "valer mais que uma consulta avulsa. Por isso a verba é separada por área de atuação: você vê quanto "
            "custou cada contato de previdenciário, trabalhista ou família, e decide onde colocar mais.",
            "A verba é paga direto ao Google, no cartão do escritório; a gestão é o trabalho de montar, revisar o "
            "texto dentro das regras da OAB e medir. Dá para começar com uma área e crescer conforme os contatos "
            "chegam. O orçamento da gestão é grátis e sai em até 24 horas.",
        ],
        "orc_titulo": "Por qual área do escritório faz sentido começar a anunciar?",
        "orc_desc": "Escolha o ponto de partida. Em até 24 horas você recebe o valor da gestão e uma sugestão de verba por área.",
        "passos_titulo": "Como o anúncio do escritório é montado dentro das regras",
        "passos": [
            ("Áreas e região", "Você me conta as áreas que quer divulgar e onde o escritório atende."),
            ("Texto informativo", "Anúncio e página escritos para informar, sem promessa de resultado nem caso concreto."),
            ("Revisão do advogado", "Você confere e aprova cada texto antes de a campanha entrar no ar."),
            ("Contatos medidos", "Relatório de quantos contatos cada área trouxe, para ajustar a verba."),
        ],
        "faq_titulo": "Perguntas frequentes sobre Google Ads para advogados",
        "relacionados": [
            ("/marketing-para-advogados/", "Marketing para advogados", "O caminho completo dentro das normas da OAB."),
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago para empresas", "Como funciona a gestão de Google Ads da RCB SEO."),
            ("/criacao-de-site-para-advogado/", "Criação de site para advogado", "O site por área de atuação."),
        ],
    },
    "trafego-pago-para-energia-solar": {
        "title": "Tráfego Pago para Energia Solar: Google Ads | RCB SEO",
        "desc": ("Tráfego pago para empresas de energia solar: Google Ads para quem pesquisa orçamento na sua região, "
                 "com landing page e medição. Orçamento grátis em 24h."),
        "publico": "Empresas integradoras de energia solar",
        "eyebrow": "Google Ads para integradores de energia solar",
        "pills": ["Orçamento em até 24h", "Anúncio por cidade atendida", "Landing page e medição"],
        "card_titulo": "Sinais de que o integrador está pagando clique de curioso",
        "regras_titulo": "Como anunciar energia solar sem prometer o que não pode cumprir?",
        "regras_ps": [
            "A geração de energia em casa e na empresa tem marco legal próprio: a " + _a(_L14300, "Lei 14.300/2022") +
            ", que criou as regras da micro e minigeração distribuída e do sistema de compensação de energia. "
            "Ela é o pano de fundo das dúvidas de quem pesquisa: compensação, conexão com a distribuidora, prazos.",
            "Por isso o anúncio precisa de cuidado com promessa. Frases como \"conta de luz zerada\" ou um percentual "
            "fixo de economia para todo mundo podem virar publicidade enganosa, que o " + _a(_CDC, "Código de Defesa "
            "do Consumidor") + " proíbe no art. 37. A economia real depende do consumo, do telhado e da região de "
            "cada cliente.",
            "O anúncio que funciona fala o que o integrador faz de verdade — análise da conta, visita, projeto, "
            "instalação e acompanhamento da conexão — e leva a pessoa para pedir a simulação pelo WhatsApp.",
        ],
        "quanto_titulo": "Quanto um integrador solar precisa investir em Google Ads?",
        "quanto_ps": [
            "Energia solar é um anúncio disputado e com venda de valor alto, então o que importa é quanto custa "
            "cada pedido de orçamento qualificado — não o clique. A verba é dividida por cidade atendida e por tipo "
            "de cliente (residencial, comercial, rural), porque cada um pesquisa de um jeito e fecha num prazo "
            "diferente.",
            "A verba vai direto para o Google, no seu cartão; a gestão é o trabalho de montar, cortar as buscas que "
            "não viram orçamento e medir. Em geral vale começar pelas cidades onde a equipe já instala e ampliar "
            "depois. O orçamento da gestão é grátis e sai em até 24 horas.",
        ],
        "orc_titulo": "Por onde a sua empresa de energia solar quer começar?",
        "orc_desc": "Escolha o ponto de partida. Em até 24 horas você recebe o valor da gestão e uma sugestão de verba por cidade.",
        "passos_titulo": "Como o anúncio do integrador vira pedido de simulação",
        "passos": [
            ("Cidades e tipo de cliente", "Você me diz onde instala e se o foco é casa, comércio ou propriedade rural."),
            ("Buscas certas", "Campanha para quem pesquisa instalação e orçamento; fora quem procura curso, vaga ou peça."),
            ("Página da simulação", "O clique cai numa landing page que pede a conta de luz e abre o WhatsApp."),
            ("Pedidos medidos", "Relatório de quantas simulações vieram por cidade e quanto custou cada uma."),
        ],
        "faq_titulo": "Perguntas frequentes sobre Google Ads para energia solar",
        "relacionados": [
            ("/blog/como-conseguir-clientes-energia-solar/", "Como conseguir clientes de energia solar", "Maps, site e anúncios juntos."),
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago para empresas", "Como funciona a gestão de Google Ads da RCB SEO."),
            ("/marketing-para-energia-solar/", "Marketing para energia solar", "As quatro frentes: Maps, site, anúncio e landing page."),
        ],
    },
    "trafego-pago-para-imobiliarias": {
        "desc": ("Tráfego pago para imobiliárias: Google Ads por bairro e tipo de imóvel, dentro das regras do COFECI, "
                 "para gerar leads próprios. Orçamento grátis em 24h."),
        "publico": "Imobiliárias e corretores de imóveis",
        "eyebrow": "Google Ads para imobiliárias e corretores",
        "pills": ["Orçamento em até 24h", "Anúncio por bairro e imóvel", "Com o CRECI no anúncio"],
        "card_titulo": "Sinais de que a imobiliária está pagando lead que não vira visita",
        "regras_titulo": "Quais regras do COFECI valem para o anúncio de imóveis?",
        "regras_ps": [
            "A " + _a(_COFECI, "Resolução COFECI nº 458/1995") + " determina que os anúncios tragam o número de "
            "inscrição no CRECI — com a letra \"J\" quando é imobiliária — e que só anuncie publicamente quem tem "
            "contrato escrito de intermediação do imóvel. Em loteamentos e condomínios, o número do registro ou da "
            "incorporação também vai em destaque.",
            "No Google Ads e na página que recebe o clique, isso vira rotina de montagem: CRECI visível, imóvel "
            "anunciado só com autorização e informação verdadeira de preço, metragem e localização — o que também "
            "protege a imobiliária perante o Código de Defesa do Consumidor.",
            "Respeitar essas regras não atrasa a campanha; evita que um anúncio bom seja tirado do ar ou vire "
            "problema com o conselho.",
        ],
        "quanto_titulo": "Quanto uma imobiliária precisa investir em Google Ads?",
        "quanto_ps": [
            "Venda, locação e captação de imóveis são três campanhas diferentes, com custo de clique e valor de "
            "lead diferentes. Uma venda de imóvel de alto padrão justifica um clique caro; uma locação pede verba "
            "mais enxuta e volume. Por isso a verba é separada por objetivo e por região.",
            "A verba é paga direto ao Google, no cartão da imobiliária, sem dividir o lead com portal; a gestão é o "
            "trabalho de montar, ajustar e medir. Dá para começar pelos bairros onde a imobiliária tem mais "
            "carteira. O orçamento da gestão é grátis e sai em até 24 horas.",
        ],
        "orc_titulo": "Qual objetivo a sua imobiliária quer atacar primeiro?",
        "orc_desc": "Escolha o ponto de partida. Em até 24 horas você recebe o valor da gestão e uma sugestão de verba por objetivo.",
        "passos_titulo": "Como a imobiliária passa a gerar lead próprio",
        "passos": [
            ("Objetivo e bairros", "Venda, locação ou captação de imóveis, e as regiões onde a imobiliária atua."),
            ("Anúncio dentro das regras", "CRECI no anúncio e só imóveis com autorização de intermediação."),
            ("Página do imóvel ou da região", "O clique cai na página certa, com WhatsApp do corretor de plantão."),
            ("Leads medidos", "Relatório de quantos contatos vieram por objetivo e por bairro."),
        ],
        "faq_titulo": "Perguntas frequentes sobre Google Ads para imobiliárias",
        "relacionados": [
            ("/seo-para-imobiliarias/", "SEO para imobiliárias", "Leads próprios pelo Google sem pagar por clique."),
            ("/gestao-de-trafego-pago/", "Gestão de tráfego pago para empresas", "Como funciona a gestão de Google Ads da RCB SEO."),
            ("/blog/como-gerar-leads-imobiliaria-sem-portais/", "Leads sem depender de portal", "O caminho completo para a imobiliária."),
        ],
    },
}


# Etapa 3, ajuste fino: rotulos e cartoes de orcamento proprios de cada nicho
# (com eles a semelhanca entre as 4 paginas ficava entre 38% e 42%).
_EXTRA2 = {
    "trafego-pago-para-dentistas": {
        "cta_hero": "Quero pacientes pelo Google Ads",
        "painel_h2": "O que entra nos anúncios do consultório",
        "split_tag": "Agenda e anúncio",
        "regras_tag": "CFO e publicidade",
        "entra_tag": "Na prática",
        "entra_titulo": "Como os anúncios do consultório são montados?",
        "orc": [
            ("Um tratamento no Google", "Para começar pelo tratamento que mais pesa na agenda.",
             ["Campanha só daquele tratamento", "Página do tratamento com WhatsApp", "Conversas medidas"],
             "Olá, Renan! Sou dentista e quero anunciar um tratamento no Google.", "Começar por um tratamento"),
            ("Vários tratamentos separados", "Para o consultório que oferece implante, ortodontia e estética.",
             ["Uma campanha por tratamento", "Verba dividida pelo que dá retorno", "Relatório por tratamento"],
             "Olá, Renan! Sou dentista e quero anunciar vários tratamentos.", "Orçamento por tratamento"),
            ("Revisar o anúncio que já existe", "Para quem já paga o Google e só recebe avaliação que não fecha.",
             ["Leitura da conta atual", "Ajuste de texto às regras do CFO", "Corte de buscas de curioso"],
             "Olá, Renan! Sou dentista, já anuncio e quero revisar a campanha.", "Revisar minha campanha"),
        ],
    },
    "trafego-pago-para-advogados": {
        "cta_hero": "Quero anunciar dentro da OAB",
        "painel_h2": "O que entra nos anúncios do escritório",
        "split_tag": "Captação x informação",
        "regras_tag": "Provimento 205/2021",
        "entra_tag": "Montagem",
        "entra_titulo": "Como a campanha do escritório é organizada?",
        "orc": [
            ("Uma área do Direito", "Para testar o Google Ads com a área que mais traz cliente.",
             ["Campanha informativa da área", "Página explicativa com número da OAB", "Contatos medidos"],
             "Olá, Renan! Sou advogado e quero anunciar uma área de atuação.", "Começar por uma área"),
            ("Escritório com várias áreas", "Para separar trabalhista, família, previdenciário e as demais.",
             ["Campanha por área", "Textos revisados dentro do provimento", "Verba por área"],
             "Olá, Renan! Tenho um escritório com várias áreas e quero anunciar.", "Orçamento por área"),
            ("Conferir anúncio atual", "Para quem já anuncia e tem dúvida se está dentro das regras.",
             ["Leitura dos anúncios ativos", "Ajuste ao Provimento 205/2021", "Plano de melhoria"],
             "Olá, Renan! Sou advogado e quero conferir meus anúncios atuais.", "Conferir meus anúncios"),
        ],
    },
    "trafego-pago-para-energia-solar": {
        "cta_hero": "Quero pedidos de simulação",
        "painel_h2": "O que entra nos anúncios do integrador",
        "split_tag": "Concorrência",
        "regras_tag": "Lei e promessa",
        "entra_tag": "Estrutura",
        "entra_titulo": "Como a campanha do integrador solar é estruturada?",
        "orc": [
            ("Cidades onde já instalo", "Para começar onde a equipe chega sem custo extra de deslocamento.",
             ["Campanha por cidade", "Landing page de simulação", "Pedidos medidos por cidade"],
             "Olá, Renan! Tenho empresa de energia solar e quero anunciar nas cidades onde instalo.", "Começar pelas minhas cidades"),
            ("Residencial e comercial separados", "Para quem atende casa, comércio e propriedade rural.",
             ["Campanha por tipo de cliente", "Texto para cada perfil", "Verba onde fecha mais"],
             "Olá, Renan! Quero anunciar energia solar separando residencial e comercial.", "Separar por tipo de cliente"),
            ("Melhorar o anúncio atual", "Para quem já anuncia e recebe pedido de curioso.",
             ["Leitura da conta", "Negativas para curso, vaga e peças", "Página de simulação revisada"],
             "Olá, Renan! Já anuncio energia solar e recebo muito curioso. Pode olhar?", "Melhorar meu anúncio"),
        ],
    },
    "trafego-pago-para-imobiliarias": {
        "cta_hero": "Quero lead próprio pelo Google",
        "painel_h2": "O que entra nos anúncios da imobiliária",
        "split_tag": "Portal x lead próprio",
        "regras_tag": "COFECI e anúncio",
        "entra_tag": "Funcionamento",
        "entra_titulo": "Como a imobiliária anuncia sem depender de portal?",
        "orc": [
            ("Venda em bairros-chave", "Para os bairros onde a imobiliária tem mais carteira.",
             ["Campanha por bairro", "Página da região com os imóveis", "Leads medidos por bairro"],
             "Olá, Renan! Tenho imobiliária e quero anunciar venda por bairro.", "Anunciar venda por bairro"),
            ("Locação com volume", "Para encher a agenda de visitas de aluguel.",
             ["Campanha de locação", "Página com filtros simples", "Contato direto com o corretor"],
             "Olá, Renan! Quero anunciar imóveis para locação no Google.", "Anunciar locação"),
            ("Captação de proprietários", "Para aumentar a carteira com quem quer vender ou alugar.",
             ["Campanha para proprietários", "Página de avaliação do imóvel", "Pedidos de captação medidos"],
             "Olá, Renan! Quero captar imóveis de proprietários pelo Google.", "Captar proprietários"),
        ],
    },
}
for _slug, _x in _EXTRA2.items():
    TRAFEGO_EXTRA[_slug].update(_x)


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
         ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Google Ads e Meta Ads para captar empresas."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Tenho escritório de contabilidade e quero um orçamento de site.",
        ("Me conte os serviços do seu escritório. Eu te digo como o site deve ser.",
         "Sem compromisso: você me diz o que atende e onde, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página para cada serviço.", "Página de troca de contador.", "Responsável técnico e CRC.",
         "WhatsApp com mensagem pronta.", "Rápido no celular.", "Ligado ao seu Perfil no Google."],
    ),

    # ======================================================= SITE PARA ESTÉTICA
    # Etapa 7 (05/10/2026): autor/data visíveis, público na ficha, FAQ sem "em Goiânia" (a página
    # atende o Brasil) e relacionados com landing page e o checklist de estética.
    dict(_site(
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
          "Sim. A RCB faz a gestão de Google Ads e Meta Ads para clínicas, com cuidado com as políticas de anúncios "
          "de saúde, e monta a landing page que recebe o clique do anúncio.")],
        [("/seo-para-clinicas-de-estetica/", "SEO para clínicas de estética", "Aparecer no Google e no Maps sem pagar por clique."),
         ("/blog/clinica-de-estetica-nao-aparece-no-google/", "Clínica de estética não aparece no Google?",
          "O checklist para conferir o que está travando a clínica."),
         ("/criacao-de-landing-page/", "Landing page para anúncios", "A página que recebe o clique e vira conversa no WhatsApp."),
         ("/blog/trafego-pago-para-clinicas/", "Tráfego pago para clínicas", "Google Ads e Meta Ads dentro das regras."),
         ("/criacao-de-sites-goiania/", "Criação de sites em Goiânia", "Como funciona a criação de sites da RCB.")],
        "Olá, Renan! Tenho uma clínica de estética e quero um orçamento de site.",
        ("Me conte os procedimentos da sua clínica. Eu te digo como o site deve ser.",
         "Sem compromisso: você me diz o que atende e onde, e eu te mostro quem aparece na sua frente hoje."),
        ["Uma página por procedimento.", "Fotos reais do espaço.", "Equipe com registro profissional.",
         "WhatsApp com mensagem pronta.", "Sem promessa de resultado.", "Ligado ao seu Perfil no Google."],
    ), data="2026-10-05", publicado="2026-09-28", publico="Clínicas de estética e profissionais de estética",
        faq_titulo="Perguntas frequentes sobre criação de site para clínica de estética"),

    # ======================================================= TRÁFEGO DENTISTAS
    _trafego(
        "trafego-pago-para-dentistas", "dentistas",
        "Tráfego pago para dentistas",
        "Tráfego Pago para Dentistas: Google Ads e Meta Ads | RCB SEO",
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
         ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
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
        "Tráfego Pago para Advogados: Google Ads Dentro da OAB | RCB SEO",
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
         ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
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
        "Tráfego Pago para Energia Solar: Google Ads e Meta Ads | RCB SEO",
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
         ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
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
         ("/gestao-de-trafego-pago/", "Gestão de tráfego pago", "Como funciona a gestão de anúncios da RCB.")],
        "Olá, Renan! Tenho uma imobiliária e quero um orçamento de tráfego pago.",
        ("Me conte onde a sua imobiliária atua. Eu te digo como gerar lead próprio.",
         "Sem compromisso: se você já anuncia, eu olho as campanhas; se não, te digo por onde começar."),
        ["Campanha por objetivo.", "Captação de proprietários.", "Página por imóvel.",
         "Dentro das regras de habitação.", "Anúncio só na sua região.", "Relatório de leads por objetivo."],
    ),
]
