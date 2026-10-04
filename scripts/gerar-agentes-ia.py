# -*- coding: utf-8 -*-
"""Gera as 3 paginas comerciais da linha "Agentes de IA".

  /agentes-de-ia/                     -> a vitrine da linha
  /agente-de-ia-para-clinicas/        -> clinicas e consultorios
  /recuperacao-de-vendas-whatsapp/    -> infoprodutores e lojas online

O que ESTA pagina vende e o servico. O produto (n8n, banco, painel) NAO foi
construido - decisao do Renan em 08/09/2026: primeiro a vitrine, com simulacao
fiel, para medir procura antes de investir na fabrica.

Decisoes desta rodada, tomadas com o Renan:
  * SEM preco na tela. Linha nova, cada projeto e diferente -> orcamento.
  * Depoimentos REAIS de clientes de consultoria, com legenda dizendo que sao
    de consultoria e nao de automacao. Nada inventado.
  * Nenhum numero de resultado prometido. A calculadora usa numeros do proprio
    visitante; o "1 em cada 10" e declarado como conta de exemplo.

Idempotente: sobrescreve os tres arquivos a cada execucao.
Depois de rodar: python scripts/menu-agentes-ia.py (propaga menu e rodape)
                 python scripts/atualizar-sitemap.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rcb_agentes as A
import rcb_pacotes as P
import rcb_marca as M  # ficha unica da marca (data/marca.json)

RAIZ = A.RAIZ
BASE = "https://rcbseo.com.br"


def hero(slug, trilha, eyebrow, h1, subtitulo, acoes_wa, pills, painel_h2, painel_itens):
    """Topo da pagina. O H2 do painel e o PRIMEIRO H2 do documento - por isso
    ele carrega o termo da pagina (regra da auditoria semantica de 08/08/2026)."""
    return u"""  <main id="main-content">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span>%(trilha)s</nav>
          <div class="eyebrow">%(eyebrow)s</div>
          <h1 class="page-title">%(h1)s</h1>
          <p class="page-subtitle">%(sub)s</p>
          <div class="page-actions">
            <a class="btn btn-primary" href="#demonstracao" data-event="cta_click" data-location="hero_demo" data-page="%(slug)s">Ver funcionando</a>
            <a class="btn btn-outline" href="%(wa)s" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="hero_whatsapp" data-page="%(slug)s">Pedir um orçamento</a>
          </div>
          <div class="pill-row">%(pills)s</div>
        </div>
        <aside class="page-hero-panel">
          <h2>%(ph2)s</h2>
          <ul class="audit-list">%(pitens)s
          </ul>
        </aside>
      </div>
    </section>
""" % {
        "trilha": trilha, "eyebrow": A.esc(eyebrow), "h1": A.esc(h1),
        "sub": A.esc(subtitulo), "slug": slug, "wa": acoes_wa,
        "pills": u"".join(u'<span class="pill">%s</span>' % A.esc(p) for p in pills),
        "ph2": A.esc(painel_h2),
        "pitens": u"".join(u"\n            <li>%s</li>" % i for i in painel_itens),
    }


def secao_texto(tag, titulo, paragrafos, id_secao=None):
    return u"""
    <section class="solution-section"%(id)s>
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">%(tag)s</div>
          <h2 class="section-title">%(titulo)s</h2>%(ps)s
        </div>
      </div>
    </section>
""" % {"id": (u' id="%s"' % id_secao) if id_secao else u"",
       "tag": A.esc(tag), "titulo": A.esc(titulo),
       "ps": u"".join(u"\n          <p>%s</p>" % p for p in paragrafos)}


def secao_cards(tag, titulo, intro, cards):
    """cards = [(h3, html_do_paragrafo)]"""
    html = u"".join(
        u'\n          <article class="feature-card"><h3>%s</h3><p>%s</p></article>'
        % (A.esc(t), p) for t, p in cards)
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="cards-grid">%s
        </div>
      </div>
    </section>
""" % (A.esc(tag), A.esc(titulo), A.esc(intro), html)


NOTA_DEPO = (u"Estes depoimentos são de clientes de consultoria de SEO e Google Perfil "
             u"da Empresa — não de automação, que é serviço novo e ainda não tem cliente "
             u"para depor. Ficam aqui porque falam de como eu trabalho, e é isso que "
             u"você está contratando.")


# ===========================================================================
# PÁGINA 1 — /agentes-de-ia/
# ===========================================================================

SLUG1 = "agentes-de-ia"
URL1 = BASE + "/agentes-de-ia/"
TITLE1 = M.titulo(u"Agentes de IA no WhatsApp para Empresas | RCB")
DESC1 = (u"Agentes de IA no WhatsApp respondem, agendam e recuperam vendas 24 horas "
         u"por dia. Veja uma conversa simulada e entenda o que dá para automatizar "
         u"no seu negócio.")

ROTEIRO1 = {
    "contato": {"nome": u"Clínica Sorriso Odontologia", "iniciais": u"CS",
                "status": u"responde na hora, 24 horas por dia"},
    "dia": u"Ontem",
    "cenarios": [
        {"id": "clinica", "rotulo": u"Uma clínica de noite",
         "nota": (u"<strong>23h47.</strong> A clínica está fechada há quatro horas. "
                  u"Hoje, essa mensagem esperaria até de manhã — e boa parte dessas "
                  u"pessoas já marcou em outro lugar antes disso."),
         "mensagens": [
             {"de": "cliente", "hora": "23:47",
              "texto": u"Boa noite. Vocês estão atendendo? Preciso marcar uma limpeza."},
             {"de": "agente", "hora": "23:47", "espera": 700,
              "texto": u"Boa noite! A clínica está fechada agora, mas eu consigo já deixar seu horário marcado.\nLimpeza é com a Dra. Camila. Estes são os horários livres:",
              "opcoes": [u"Quinta, 12/09, às 14:30", u"Quinta, 12/09, às 16:00",
                         u"Sexta, 13/09, às 09:00"]},
             {"de": "cliente", "hora": "23:48", "texto": u"Quinta 14:30 pode ser"},
             {"de": "agente", "hora": "23:48",
              "texto": u"Fechado. Só me diga seu nome completo, por favor?"},
             {"de": "cliente", "hora": "23:49", "texto": u"Marcos Antônio Ribeiro"},
             {"de": "agente", "hora": "23:49",
              "texto": u"Pronto, Marcos! Limpeza marcada para quinta-feira, dia 12, às 14:30, com a Dra. Camila.\nEndereço: Rua T-55, 1210 — Setor Bueno.\nEu te lembro um dia antes. Precisa de mais alguma coisa?"},
             {"de": "cliente", "hora": "23:49", "texto": u"Só isso. Obrigado!"},
             {"de": "agente", "hora": "23:50",
              "texto": u"Boa noite, Marcos. Até quinta."},
         ]},
        {"id": "loja", "rotulo": u"Uma venda que ia se perder",
         "nota": (u"<strong>Ela chegou até o pagamento e parou.</strong> Sem ninguém "
                  u"para puxar a conversa, essa venda simplesmente não acontece. "
                  u"A mensagem sai sozinha, meia hora depois."),
         "mensagens": [
             {"de": "agente", "hora": "20:14", "espera": 400,
              "texto": u"Oi, Juliana! Vi que você começou a compra do curso e não finalizou. Ficou alguma dúvida? Posso ajudar."},
             {"de": "cliente", "hora": "20:31",
              "texto": u"oi! é que fiquei na dúvida se dá pra pagar parcelado"},
             {"de": "agente", "hora": "20:31",
              "texto": u"Dá sim: até 12x no cartão, ou à vista no Pix.\nE o acesso é liberado na hora, mesmo no parcelado."},
             {"de": "cliente", "hora": "20:32", "texto": u"ah, então tá. me manda o link"},
             {"de": "agente", "hora": "20:32",
              "texto": u"Aqui está, é o mesmo carrinho que você já tinha montado:\npay.exemplo.com.br/curso\nQualquer coisa é só me chamar por aqui."},
             {"de": "cliente", "hora": "20:41", "texto": u"comprei! obrigada 🙌"},
             {"de": "agente", "hora": "20:41",
              "texto": u"Que bom, Juliana! Seu acesso já foi para o seu e-mail. Bons estudos."},
         ]},
    ],
}

FAQ1 = [
    (u"O que é um agente de IA no WhatsApp?",
     u"É um atendente automático que lê a mensagem do cliente, entende o que ele quer e "
     u"responde com texto escrito na hora — não é aquele menu de \"digite 1, digite 2\". "
     u"Ele consegue marcar horário na agenda, responder dúvidas que você autorizou, avisar "
     u"você quando o assunto é sério e mandar lembretes sozinho."),
    (u"É o mesmo que um robô de menu numerado?",
     u"Não. O menu numerado obriga o cliente a se encaixar em opções prontas e trava quando "
     u"ele escreve qualquer coisa fora do script. O agente entende a frase como ela foi "
     u"escrita, com erro de digitação e tudo, e responde no assunto."),
    (u"O cliente vai perceber que está falando com um robô?",
     u"Provavelmente sim, em algum momento — e tudo bem. Eu configuro o agente para não fingir "
     u"ser humano: ele se apresenta como atendimento automático quando faz sentido e passa a "
     u"conversa para uma pessoa quando o assunto pede. Cliente enganado vira cliente irritado."),
    (u"Ele vai responder besteira e me dar prejuízo?",
     u"O risco existe e é por isso que o agente trabalha com limites escritos: ele só fala do "
     u"que foi autorizado, e o que está fora dessa lista vira \"vou passar para a equipe\". "
     u"Preço de tratamento, promessa de resultado e assunto delicado ficam de fora por padrão."),
    (u"Preciso instalar alguma coisa na minha empresa?",
     u"Não. Roda tudo fora do seu computador. Você precisa de um número de WhatsApp para o "
     u"negócio e, no caso de agendamento, de uma agenda digital. O resto é comigo."),
    (u"Quanto custa?",
     u"Depende do tamanho do atendimento e de quantas coisas o agente precisa fazer. Como é "
     u"serviço novo e cada negócio é diferente, eu não coloco preço fixo na tela: você me "
     u"conta o que precisa pelo WhatsApp e eu te mando um orçamento fechado, sem enrolação."),
    (u"Você já fez isso para alguém?",
     u"Serviço de agente de IA é linha nova aqui, aberta em 2026 — então não, ainda não tenho "
     u"um cliente de automação para mostrar, e prefiro dizer isso do que inventar caso de "
     u"sucesso. O que eu tenho são clientes de consultoria que assinam embaixo do jeito como "
     u"eu trabalho, e a demonstração desta página, que mostra exatamente o que será entregue."),
]


def pagina1():
    wa = P.wa(u"Olá, Renan! Vi a página de agentes de IA no site e quero entender "
              u"o que dá para automatizar no meu negócio.")

    corpo = hero(
        SLUG1,
        u"<span>Agentes de IA</span>",
        u"Atendimento automático — Brasil inteiro",
        u"Agentes de IA que atendem no seu WhatsApp 24 horas por dia",
        u"Seu cliente manda mensagem às onze da noite, no domingo, no feriado. "
        u"Se ninguém responde, ele procura outro. Um agente de IA responde na hora, "
        u"marca o horário, tira a dúvida e chama você quando o assunto é sério.",
        wa,
        [u"Responde em segundos", u"Funciona fora do horário", u"Você continua no controle"],
        u"O que um agente de IA faz sozinho",
        [u"Responde qualquer mensagem em segundos, a qualquer hora.",
         u"Marca, confirma e remarca horário direto na sua agenda.",
         u"Responde as dúvidas que se repetem todo dia.",
         u"Chama você na hora quando o assunto é urgente.",
         u"Puxa de volta a venda que ficou pela metade.",
         u"Registra tudo o que aconteceu, para você conferir depois."])

    corpo += secao_texto(
        u"Em uma frase",
        u"Agentes de IA são atendentes que não dormem",
        [u"<strong>Um agente de IA é um atendente digital que trabalha dentro do seu "
         u"WhatsApp.</strong> Ele lê a mensagem que o cliente escreveu, entende o que a "
         u"pessoa quer e responde na hora — de madrugada, no domingo, no meio do "
         u"atendimento. Quando o assunto é marcar horário, ele marca. Quando é dúvida "
         u"repetida, ele responde. Quando é sério, ele chama você.",
         u"Não é um robô de \"digite 1 para vendas\". Aquilo obriga o cliente a se "
         u"encaixar num menu e trava assim que ele escreve qualquer coisa diferente. "
         u"O agente entende frase escrita do jeito que as pessoas escrevem de verdade, "
         u"com pressa e com erro de digitação.",
         u"E não é você sendo substituído. É o contrário: o trabalho chato — repetir "
         u"o endereço, repetir o horário, correr atrás de confirmação — sai da sua mão. "
         u"O que exige gente continua com gente."])

    corpo += A.bloco_whatsapp(
        u"Veja um agente de IA trabalhando, agora",
        u"Demonstração",
        u"Não é vídeo nem foto de tela. É a conversa acontecendo aqui, do jeito que "
        u"acontece no celular do seu cliente. Troque o cenário nos botões ao lado.",
        ROTEIRO1,
        paragrafos=[
            u"Escolha uma situação e acompanhe o celular ao lado. As mensagens vão "
            u"aparecendo no ritmo real de uma conversa.",
            u"<strong>Repare no horário.</strong> É esse detalhe que separa quem "
            u"fecha de quem perde o cliente para o concorrente que respondeu antes.",
        ])

    corpo += A.bloco_fluxo(
        u"O que acontece quando a mensagem chega",
        u"Como funciona",
        u"Sem palavra difícil: são quatro passos, e todos acontecem em menos tempo do "
        u"que você levou para ler esta frase.",
        [(u"A mensagem chega",
          u"O cliente escreve no seu WhatsApp de sempre, o mesmo número que você já "
          u"divulga. Nada muda para ele.", u"Instantâneo"),
         (u"O agente entende o pedido",
          u"Ele separa o que a pessoa quer: marcar horário, tirar dúvida, reclamar, "
          u"pedir preço ou algo urgente.", u"1 a 2 segundos"),
         (u"Ele faz o que foi combinado",
          u"Consulta sua agenda e oferece horários livres, responde com a informação "
          u"que você autorizou, ou registra o pedido.", u"Poucos segundos"),
         (u"Você fica sabendo",
          u"Assunto sério cai no seu celular na hora. O resto entra no resumo, para "
          u"você olhar quando puder.", None)])

    corpo += secao_cards(
        u"Duas frentes",
        u"Dois agentes prontos para começar",
        u"São os dois casos em que a automação paga a conta mais rápido. "
        u"Se o seu negócio não é nenhum dos dois, me chame assim mesmo — o que muda "
        u"é o roteiro, não a ferramenta.",
        [(u"Clínicas e consultórios",
          u"Agendamento pelo WhatsApp a qualquer hora, confirmação um dia antes para "
          u"a cadeira não ficar vazia, resposta às dúvidas de sempre e aviso na hora "
          u"quando alguém chega com urgência. "
          u"<a href=\"/agente-de-ia-para-clinicas/\">Ver a página de clínicas →</a>"),
         (u"Quem vende pela internet",
          u"A pessoa chega no pagamento e some. O agente puxa a conversa de volta, "
          u"resolve a dúvida que travou a compra e devolve o link. "
          u"<a href=\"/recuperacao-de-vendas-whatsapp/\">Ver a página de recuperação de vendas →</a>"),
         (u"Comércio e prestador de serviço",
          u"Horário de funcionamento, endereço, orçamento inicial, agendamento de "
          u"visita. É o mesmo agente, com outro roteiro — e conversa com o trabalho "
          u"de <a href=\"/automacao-de-processos/\">automação de processos</a> que "
          u"eu já faço.")])

    corpo += A.bloco_antes_depois(
        u"O que muda no dia a dia",
        u"Antes e depois",
        u"Nada aqui é promessa de faturamento. É a mudança de rotina que a automação "
        u"provoca — o resultado em dinheiro depende do seu negócio.",
        u"Como é hoje",
        [u"A mensagem da noite só é lida de manhã.",
         u"Alguém para o que está fazendo para responder \"qual o endereço?\".",
         u"Confirmação de horário é feita na correria, quando dá.",
         u"Quem desistiu no meio da compra vai embora calado.",
         u"Ninguém sabe quantas conversas foram perdidas."],
        u"Como fica",
        [u"A mensagem da noite é respondida na noite.",
         u"As perguntas repetidas são respondidas sem tirar ninguém do trabalho.",
         u"A confirmação sai sozinha, sempre, no mesmo horário.",
         u"Quem parou no meio recebe uma mensagem e muitos voltam.",
         u"Todo atendimento fica registrado e vira relatório."])

    corpo += secao_texto(
        u"Honestidade",
        u"O que um agente de IA não faz — e eu não vou prometer",
        [u"<strong>Não substitui você nem sua equipe.</strong> Ele tira da frente o "
         u"trabalho repetido. Fechar venda grande, acalmar cliente irritado e cuidar "
         u"do que é delicado continua sendo trabalho de gente.",
         u"<strong>Não garante aumento de faturamento.</strong> Você vai ver na "
         u"internet números como \"reduza 40% das faltas\" e \"aumente 70% das vendas\". "
         u"Eu não vou repetir isso, porque não tenho como garantir o seu caso. O que eu "
         u"garanto é o que está sendo entregue: o agente funcionando do jeito que você "
         u"viu na demonstração.",
         u"<strong>Não inventa resposta.</strong> Se a pergunta está fora do que você "
         u"autorizou, ele passa para uma pessoa em vez de chutar. Preço que depende de "
         u"avaliação, promessa de resultado e assunto de saúde ficam fora por padrão.",
         u"<strong>Não some com a sua responsabilidade.</strong> A conversa é do seu "
         u"negócio, com o seu nome. Por isso tudo fica registrado e você aprova o "
         u"roteiro antes de entrar no ar."])

    corpo += A.bloco_depoimentos(NOTA_DEPO)
    corpo += A.bloco_faq(u"Perguntas frequentes sobre agentes de IA", FAQ1)
    corpo += A.bloco_cta(
        u"Me conte como é o seu atendimento hoje",
        u"Você me diz quantas mensagens chegam por dia e o que mais se repete. "
        u"Eu te digo o que dá para automatizar, o que não vale a pena e quanto custa. "
        u"Sem compromisso.",
        wa, SLUG1)
    corpo += u"  </main>\n"

    servico = {
        "@type": "Service", "@id": URL1 + "#service",
        "name": u"Agentes de IA para WhatsApp",
        "serviceType": u"Automação de atendimento com inteligência artificial",
        "description": (u"Implantação de agentes de inteligência artificial no WhatsApp "
                        u"para atendimento, agendamento e recuperação de vendas, com "
                        u"passagem para atendimento humano quando o assunto exige."),
        "provider": {"@id": M.ID_EMPRESA},
        "areaServed": {"@type": "Country", "name": "Brasil"},
    }
    schema = A.schema_pagina(URL1, TITLE1, DESC1,
                             [(u"Início", BASE + "/"), (u"Agentes de IA", URL1)],
                             servico=servico, faq=FAQ1)
    return A.montar_pagina(
        os.path.join(RAIZ, SLUG1, "index.html"), SLUG1, URL1, TITLE1, DESC1,
        u"Agentes de IA no WhatsApp que atendem 24 horas por dia",
        u"Veja uma conversa simulada de um agente marcando consulta às 23h47 "
        u"e recuperando uma venda abandonada.",
        schema, corpo)


# ===========================================================================
# PÁGINA 2 — /agente-de-ia-para-clinicas/
# ===========================================================================

SLUG2 = "agente-de-ia-para-clinicas"
URL2 = BASE + "/agente-de-ia-para-clinicas/"
TITLE2 = u"Agente de IA para Clínicas: Agendamento 24h no WhatsApp"
DESC2 = (u"Agente de IA para clínicas marca consulta no WhatsApp a qualquer hora, "
         u"confirma na véspera para reduzir faltas e avisa a equipe quando é urgência. "
         u"Veja funcionando.")

ROTEIRO2 = {
    "contato": {"nome": u"Clínica Sorriso Odontologia", "iniciais": u"CS",
                "status": u"responde na hora, 24 horas por dia"},
    "dia": u"Ontem",
    "cenarios": [
        {"id": "agendar", "rotulo": u"Quer marcar consulta",
         "nota": (u"<strong>23h47, clínica fechada.</strong> Hoje essa mensagem espera "
                  u"até de manhã. Aqui ela virou horário marcado antes de a pessoa "
                  u"pensar em procurar outra clínica."),
         "mensagens": [
             {"de": "cliente", "hora": "23:47",
              "texto": u"Boa noite. Vocês estão atendendo? Preciso marcar uma limpeza."},
             {"de": "agente", "hora": "23:47", "espera": 700,
              "texto": u"Boa noite! A clínica está fechada agora, mas eu consigo já deixar seu horário marcado.\nLimpeza é com a Dra. Camila. Estes são os horários livres:",
              "opcoes": [u"Quinta, 12/09, às 14:30", u"Quinta, 12/09, às 16:00",
                         u"Sexta, 13/09, às 09:00"]},
             {"de": "cliente", "hora": "23:48", "texto": u"Quinta 14:30 pode ser"},
             {"de": "agente", "hora": "23:48",
              "texto": u"Fechado. Só me diga seu nome completo, por favor?"},
             {"de": "cliente", "hora": "23:49", "texto": u"Marcos Antônio Ribeiro"},
             {"de": "agente", "hora": "23:49",
              "texto": u"Pronto, Marcos! Limpeza marcada para quinta-feira, dia 12, às 14:30, com a Dra. Camila.\nEndereço: Rua T-55, 1210 — Setor Bueno.\nEu te lembro um dia antes."},
             {"de": "cliente", "hora": "23:50", "texto": u"Perfeito, obrigado!"},
         ]},
        {"id": "duvida", "rotulo": u"Pergunta preço e convênio",
         "nota": (u"<strong>O agente não chuta preço de tratamento.</strong> Ele responde "
                  u"o que a clínica autorizou responder e leva para a avaliação o que "
                  u"só pode ser dito depois de examinar. Isso protege a clínica diante "
                  u"das regras do conselho e evita cobrança depois."),
         "mensagens": [
             {"de": "cliente", "hora": "12:10",
              "texto": u"Bom dia! Vocês atendem Unimed? E quanto custa clareamento?"},
             {"de": "agente", "hora": "12:10", "espera": 600,
              "texto": u"Bom dia! Atendemos Unimed, Bradesco Saúde e SulAmérica, e também particular."},
             {"de": "agente", "hora": "12:10",
              "texto": u"Sobre o clareamento: o valor só é fechado depois da avaliação, porque muda conforme o caso de cada pessoa. A avaliação custa R$ 150 e, se você fizer o tratamento aqui, esse valor entra como desconto."},
             {"de": "agente", "hora": "12:11",
              "texto": u"Quer que eu já reserve um horário de avaliação?",
              "opcoes": [u"Sim, quero avaliar", u"Só queria saber o valor"]},
             {"de": "cliente", "hora": "12:14", "texto": u"pode reservar sim"},
             {"de": "agente", "hora": "12:14",
              "texto": u"Tenho terça, 10/09, às 10:00, ou quarta, 11/09, às 15:30. Qual fica melhor para você?"},
         ]},
        {"id": "urgencia", "rotulo": u"Chegou com dor",
         "nota": (u"<strong>Aqui é a linha que o agente não cruza.</strong> Ele não dá "
                  u"diagnóstico, não receita e não diz que \"não é grave\". Acolhe, dá "
                  u"a orientação básica de segurança e chama gente de verdade na hora."),
         "mensagens": [
             {"de": "cliente", "hora": "21:32",
              "texto": u"socorro, meu dente quebrou e tá doendo muito, meu rosto tá inchado"},
             {"de": "agente", "hora": "21:32", "espera": 500,
              "texto": u"Sinto muito que você esteja passando por isso. Isso não vai ficar para amanhã: estou avisando a equipe agora."},
             {"de": "agente", "hora": "21:32",
              "texto": u"Enquanto alguém te retorna: evite mastigar desse lado e não coloque nada quente no rosto. Se a dor ficar muito forte, se o inchaço aumentar rápido ou se você tiver febre, procure um pronto-socorro sem esperar."},
             {"de": "agente", "hora": "21:33",
              "texto": u"Aviso enviado para o celular da Dra. Camila. Alguém fala com você em minutos."},
             {"de": "cliente", "hora": "21:33", "texto": u"obrigado"},
             {"de": "agente", "hora": "21:35",
              "texto": u"A Dra. Camila assumiu a conversa a partir daqui."},
         ]},
        {"id": "confirmar", "rotulo": u"Confirmação da véspera",
         "nota": (u"<strong>É esta mensagem que evita a cadeira vazia.</strong> Quem ia "
                  u"faltar avisa antes, e o horário volta para a agenda em vez de virar "
                  u"prejuízo. Ela sai sozinha, todo dia, sem ninguém lembrar."),
         "mensagens": [
             {"de": "agente", "hora": "09:00", "espera": 400,
              "texto": u"Bom dia, Marcos! Passando para lembrar: sua limpeza é amanhã, quinta, dia 12, às 14:30, com a Dra. Camila.\nPosso confirmar?",
              "opcoes": [u"1 — Confirmo que vou", u"2 — Preciso remarcar"]},
             {"de": "cliente", "hora": "09:14", "texto": u"2"},
             {"de": "agente", "hora": "09:14",
              "texto": u"Sem problema. Estes são os horários livres da semana que vem:",
              "opcoes": [u"Segunda, 16/09, às 11:00", u"Terça, 17/09, às 14:30",
                         u"Quinta, 19/09, às 16:00"]},
             {"de": "cliente", "hora": "09:16", "texto": u"terça 14:30"},
             {"de": "agente", "hora": "09:16",
              "texto": u"Remarcado para terça, dia 17, às 14:30.\nO horário de amanhã já foi liberado para outra pessoa. Obrigado por avisar, Marcos."},
         ]},
    ],
}

FAQ2 = [
    (u"O agente de IA para clínicas pode falar preço de tratamento?",
     u"Só o que a clínica autorizar. Por padrão eu configuro o agente para informar valor de "
     u"avaliação e formas de pagamento, e para levar o resto à avaliação presencial — que é "
     u"como funciona de verdade e é o que respeita as regras de publicidade dos conselhos "
     u"de odontologia e medicina. Se a clínica quiser divulgar algum valor fixo, isso é "
     u"decisão dela e fica escrito no roteiro."),
    (u"E se o paciente chegar com uma emergência?",
     u"O agente reconhece palavras de urgência — dor forte, sangramento, inchaço, acidente — "
     u"e faz três coisas: acolhe, dá orientação básica de segurança (incluindo procurar um "
     u"pronto-socorro se piorar) e dispara um aviso imediato para o celular de quem estiver "
     u"de plantão. Ele não dá diagnóstico e não diz se é grave ou não."),
    (u"Ele mexe na minha agenda sozinho?",
     u"Ele consulta os horários livres e marca dentro das regras que você definir: quais "
     u"procedimentos, com qual profissional, em que dias, com quanto tempo cada um. Nada de "
     u"encaixe fora da regra. Você pode pedir que certos procedimentos só sejam pré-agendados, "
     u"esperando a confirmação da recepção."),
    (u"A confirmação da véspera realmente diminui as faltas?",
     u"Lembrete de consulta é prática antiga em clínica justamente porque ajuda — mas eu não "
     u"vou te dar uma porcentagem, porque o número varia demais entre especialidades e "
     u"públicos. O que a automação garante é que o lembrete sai todos os dias, no mesmo "
     u"horário, sem depender de alguém lembrar de fazer."),
    (u"E os dados dos pacientes? Isso está dentro da LGPD?",
     u"Dado de saúde é dado sensível e recebe tratamento próprio na Lei Geral de Proteção de "
     u"Dados. Na prática: o agente coleta só o necessário para agendar, a conversa fica "
     u"guardada em ambiente controlado, ninguém de fora tem acesso, e a clínica continua "
     u"sendo a responsável pelos dados dos seus pacientes. Isso é combinado por escrito "
     u"antes de começar."),
    (u"Minha recepcionista vai perder o emprego?",
     u"A conta não costuma ser essa. O que sai da mão dela é a parte repetida: informar "
     u"endereço, repetir horário, correr atrás de confirmação. O que sobra é o que exige "
     u"gente — receber bem quem chega, resolver caso difícil, cuidar de quem está com medo."),
    (u"Funciona no meu WhatsApp atual?",
     u"Funciona com o WhatsApp do negócio. Em alguns casos é preciso migrar o número para a "
     u"versão de empresa antes, o que não faz você perder as conversas. Eu verifico isso "
     u"junto com você antes de fechar qualquer coisa."),
    (u"Em quanto tempo fica pronto?",
     u"Depende de quantos procedimentos e profissionais a agenda tem, e de quanto tempo a "
     u"clínica leva para revisar o roteiro de respostas. O roteiro é sempre aprovado pela "
     u"clínica antes de entrar no ar — essa é a etapa que mais varia, porque envolve decisão "
     u"de quem manda na clínica, não trabalho técnico."),
]


def pagina2():
    wa = P.wa(u"Olá, Renan! Vi a página do agente de IA para clínicas e quero um "
              u"orçamento para a minha clínica.")

    corpo = hero(
        SLUG2,
        u'<a href="/agentes-de-ia/">Agentes de IA</a><span>/</span><span>Para clínicas</span>',
        u"Clínicas, consultórios e centros de estética",
        u"Agente de IA para clínicas: marca consulta até de madrugada",
        u"Boa parte das mensagens de paciente chega fora do horário — de noite, no fim de "
        u"semana, no meio do expediente em que ninguém pode parar. Um agente de IA "
        u"responde na hora, marca o horário na sua agenda e confirma na véspera para "
        u"a cadeira não ficar vazia.",
        wa,
        [u"Marca a qualquer hora", u"Confirma na véspera", u"Urgência vai para gente"],
        u"O que o agente de IA para clínicas faz",
        [u"Marca, confirma e remarca consulta direto na sua agenda.",
         u"Responde convênio, endereço, horário e formas de pagamento.",
         u"Manda o lembrete da véspera todos os dias, sozinho.",
         u"Reconhece urgência e chama a equipe no mesmo minuto.",
         u"Nunca chuta preço de tratamento nem dá diagnóstico.",
         u"Entrega um relatório do mês com tudo o que aconteceu."])

    corpo += secao_texto(
        u"O problema",
        u"Duas cadeiras vazias por semana pagam a automação inteira",
        [u"<strong>A clínica não perde paciente na hora do atendimento. Perde antes.</strong> "
         u"Perde na mensagem de sábado que só foi lida na segunda. Perde no paciente que "
         u"perguntou o preço e ninguém respondeu. Perde na consulta marcada há três semanas "
         u"que virou uma cadeira vazia numa quinta-feira à tarde.",
         u"O buraco mais caro é a falta. O horário vago não volta: o profissional ficou "
         u"parado, a sala ficou parada, e havia gente na fila que teria ocupado aquele "
         u"lugar se soubesse que ele existia.",
         u"E o buraco mais silencioso é a mensagem sem resposta. Quem procura clínica "
         u"raramente manda mensagem para uma só. Manda para três — e marca com a primeira "
         u"que responder."])

    corpo += A.bloco_whatsapp(
        u"Veja o agente de IA para clínicas atendendo",
        u"Demonstração",
        u"Quatro situações que acontecem em toda clínica. Clique nos botões para trocar "
        u"de cenário e acompanhe a conversa no celular.",
        ROTEIRO2,
        paragrafos=[
            u"Estas quatro conversas cobrem a maior parte do que chega no WhatsApp de "
            u"uma clínica: quem quer marcar, quem quer saber preço, quem está com dor "
            u"e a confirmação do dia anterior.",
            u"<strong>Preste atenção no que o agente não faz.</strong> Ele não dá "
            u"diagnóstico, não promete resultado e não inventa valor de tratamento. "
            u"É isso que mantém a clínica dentro das regras do conselho.",
        ])

    corpo += A.bloco_calculadora(
        "faltas",
        u"Quanto as faltas custam para a sua clínica por mês",
        u"Faça a conta",
        u"Arraste as barrinhas com os números da sua clínica. A conta é simples: "
        u"quantos horários vagos por mês, vezes o valor de cada atendimento.",
        [("atendimentos", u"Atendimentos marcados por mês", 20, 600, 10, 200, "num",
          u"", u"20", u"600"),
         ("faltas", u"Quantos por cento faltam ou desmarcam em cima da hora", 2, 40, 1,
          12, "num", u"%", u"2%", u"40%"),
         ("ticket", u"Valor médio de cada atendimento", 50, 1500, 10, 250, "reais",
          u"", u"R$ 50", u"R$ 1.500")],
        u"Fica parado por mês, aproximadamente",
        u"Esta conta usa <strong>os seus números</strong>, não uma média inventada. "
        u"Ela mostra o tamanho do buraco — não promete que a automação vai fechar o "
        u"buraco inteiro. Nenhum lembrete recupera todas as faltas.")

    corpo += A.bloco_fluxo(
        u"Como o agente de IA para clínicas trabalha no seu dia",
        u"Como funciona",
        u"O paciente continua mandando mensagem para o mesmo número de sempre. "
        u"O que muda é o que acontece depois.",
        [(u"Chega a mensagem",
          u"No WhatsApp da clínica, o mesmo que está no Google e no cartãozinho. "
          u"O paciente não precisa baixar nem aprender nada.", u"Qualquer hora"),
         (u"O agente entende",
          u"Marcar, remarcar, perguntar convênio, perguntar preço, urgência ou "
          u"confirmação — cada um segue um caminho diferente.", u"Segundos"),
         (u"Resolve ou passa adiante",
          u"O que está no roteiro, ele resolve. O que não está, e tudo o que for "
          u"urgência, vai para uma pessoa da equipe imediatamente.", None),
         (u"Lembra e confirma sozinho",
          u"Um dia antes de cada consulta, o lembrete sai automaticamente. "
          u"Quem não pode vir remarca ali mesmo, e o horário é liberado.", u"Todo dia")])

    corpo += A.bloco_painel(
        u"No fim do mês, você recebe isto",
        u"Relatório",
        u"Um resumo em linguagem de gente, sem gráfico complicado: quantos pacientes "
        u"foram atendidos pelo agente, quantos horários foram marcados e quantos "
        u"foram confirmados.",
        u"Relatório do mês — Clínica Sorriso (exemplo)",
        [(u"318", u"mensagens respondidas no mês", False),
         (u"74", u"consultas marcadas pelo agente", False),
         (u"41", u"delas fora do horário de atendimento", True),
         (u"12", u"remarcadas na véspera em vez de virar falta", True),
         (u"9", u"urgências passadas para a equipe", False)],
        [34, 52, 41, 68, 57, 79, 62, 88, 71, 94, 83, 100],
        u"Gráfico ilustrativo de mensagens atendidas ao longo do mês",
    )

    corpo += secao_cards(
        u"Limites combinados",
        u"O que o agente de IA para clínicas nunca vai fazer",
        u"Estes limites não são detalhe técnico: são o que mantém a clínica segura "
        u"diante do paciente e do conselho profissional.",
        [(u"Não dá diagnóstico",
          u"Nenhuma hipótese, nenhuma opinião clínica, nenhum \"provavelmente é...\". "
          u"Sintoma sempre vira encaminhamento para profissional."),
         (u"Não promete resultado",
          u"Não diz que o tratamento vai funcionar, em quanto tempo, nem mostra "
          u"antes e depois. As regras de publicidade dos conselhos de "
          u"<a href=\"https://website.cfo.org.br/\" target=\"_blank\" rel=\"noopener nofollow\">odontologia</a> "
          u"e <a href=\"https://portal.cfm.org.br/\" target=\"_blank\" rel=\"noopener nofollow\">medicina</a> "
          u"são claras nisso."),
         (u"Não inventa preço",
          u"Só repete valores que a clínica escreveu e autorizou. O que depende de "
          u"avaliação vira convite para avaliação."),
         (u"Não finge ser humano",
          u"Se o paciente perguntar, o agente diz que é atendimento automático. "
          u"Enganar paciente destrói confiança e não vale o atalho."),
         (u"Não segura urgência",
          u"Palavra de urgência interrompe o roteiro e chama a equipe na hora. "
          u"Nunca fica esperando alguém abrir o computador."),
         (u"Não some com o registro",
          u"Toda conversa fica guardada e disponível para a clínica conferir, "
          u"como manda o cuidado com dado de paciente.")])

    corpo += A.bloco_depoimentos(NOTA_DEPO)
    corpo += A.bloco_faq(u"Perguntas frequentes sobre agente de IA para clínicas", FAQ2)
    corpo += secao_texto(
        u"Antes da automação",
        u"Se a sua clínica ainda não aparece no Google, comece por ali",
        [u"Automatizar o atendimento resolve o que fazer com a mensagem que chega. "
         u"Não resolve o problema de <strong>não chegar mensagem nenhuma</strong>.",
         u"Se hoje o seu telefone é silencioso, o gargalo está antes: a clínica "
         u"não está sendo encontrada. Nesse caso o caminho é "
         u"<a href=\"/seo-para-clinicas/\">aparecer no Google para quem procura seu "
         u"serviço</a> e organizar o "
         u"<a href=\"/google-perfil-empresa/\">Perfil da Empresa no Google</a> — que é "
         u"o meu trabalho principal. Eu falo isso antes de vender automação, e não "
         u"depois.",
         u"Cheio de mensagem e sem conseguir dar conta? Aí sim o agente é a peça "
         u"que falta."])
    corpo += A.bloco_cta(
        u"Me conte como funciona o atendimento da sua clínica",
        u"Quantas mensagens chegam por dia, quantas consultas viram falta, quem "
        u"responde hoje. Com isso eu te digo o que dá para automatizar e quanto custa.",
        wa, SLUG2)
    corpo += u"  </main>\n"

    servico = {
        "@type": "Service", "@id": URL2 + "#service",
        "name": u"Agente de IA para clínicas no WhatsApp",
        "serviceType": u"Automação de agendamento e atendimento para clínicas",
        "description": (u"Agente de inteligência artificial que atende no WhatsApp da "
                        u"clínica, agenda e remarca consultas, envia confirmação de "
                        u"véspera e encaminha urgências para a equipe humana."),
        "provider": {"@id": M.ID_EMPRESA},
        "audience": {"@type": "Audience", "audienceType": u"Clínicas e consultórios"},
        "areaServed": {"@type": "Country", "name": "Brasil"},
    }
    schema = A.schema_pagina(URL2, TITLE2, DESC2,
                             [(u"Início", BASE + "/"),
                              (u"Agentes de IA", URL1),
                              (u"Para clínicas", URL2)],
                             servico=servico, faq=FAQ2)
    return A.montar_pagina(
        os.path.join(RAIZ, SLUG2, "index.html"), SLUG2, URL2, TITLE2, DESC2,
        u"Agente de IA para clínicas: agendamento 24h no WhatsApp",
        u"Marca consulta de madrugada, confirma na véspera e chama a equipe quando "
        u"é urgência. Veja a conversa simulada.",
        schema, corpo)


# ===========================================================================
# PÁGINA 3 — /recuperacao-de-vendas-whatsapp/
# ===========================================================================

SLUG3 = "recuperacao-de-vendas-whatsapp"
URL3 = BASE + "/recuperacao-de-vendas-whatsapp/"
TITLE3 = M.titulo(u"Recuperação de Carrinho Abandonado no WhatsApp | RCB")
DESC3 = (u"Recuperação de carrinho abandonado no WhatsApp: quem chegou no pagamento e "
         u"desistiu recebe uma mensagem, tira a dúvida e volta para a compra. "
         u"Veja a conversa funcionando.")

ROTEIRO3 = {
    "contato": {"nome": u"Método Vender Mais — Suporte", "iniciais": u"MV",
                "status": u"responde na hora"},
    "dia": u"Ontem",
    "cenarios": [
        {"id": "duvida", "rotulo": u"Travou numa dúvida",
         "nota": (u"<strong>A venda não caiu por falta de interesse.</strong> Caiu porque "
                  u"surgiu uma dúvida boba na hora de pagar e não tinha ninguém para "
                  u"responder. Trinta minutos depois, o agente puxa a conversa."),
         "mensagens": [
             {"de": "agente", "hora": "20:14", "espera": 500,
              "texto": u"Oi, Juliana! Vi que você começou a compra do Método Vender Mais e não finalizou. Ficou alguma dúvida? Posso ajudar."},
             {"de": "cliente", "hora": "20:31",
              "texto": u"oi! é que fiquei na dúvida se dá pra pagar parcelado"},
             {"de": "agente", "hora": "20:31",
              "texto": u"Dá sim: até 12x no cartão, ou à vista no Pix.\nE o acesso é liberado na hora, mesmo no parcelado."},
             {"de": "cliente", "hora": "20:32", "texto": u"ah, então tá. me manda o link"},
             {"de": "agente", "hora": "20:32",
              "texto": u"Aqui está, é o mesmo carrinho que você já tinha montado:\npay.exemplo.com.br/metodo\nQualquer coisa é só me chamar por aqui."},
             {"de": "cliente", "hora": "20:41", "texto": u"comprei! obrigada 🙌"},
             {"de": "agente", "hora": "20:41",
              "texto": u"Que bom, Juliana! Seu acesso já foi para o seu e-mail. Bons estudos."},
         ]},
        {"id": "preco", "rotulo": u"Achou caro",
         "nota": (u"<strong>Desconto só se você autorizar, e só do jeito que você "
                  u"autorizar.</strong> O agente não inventa condição para fechar venda "
                  u"— isso destrói o preço do seu produto e gera confusão com quem "
                  u"pagou o valor cheio."),
         "mensagens": [
             {"de": "agente", "hora": "19:40", "espera": 500,
              "texto": u"Oi, Rodrigo! Vi que você não finalizou a compra do Método Vender Mais. Posso ajudar com alguma coisa?"},
             {"de": "cliente", "hora": "19:52",
              "texto": u"tô achando meio caro pra mim agora"},
             {"de": "agente", "hora": "19:52",
              "texto": u"Entendo. Duas coisas que talvez ajudem:\n1) dá para parcelar em até 12x, o que deixa a parcela bem menor;\n2) no Pix à vista tem 5% de desconto."},
             {"de": "agente", "hora": "19:53",
              "texto": u"E se agora não for a hora, tudo bem também. Quer que eu te avise quando abrir uma condição nova?",
              "opcoes": [u"Quero o link do Pix", u"Me avisa depois"]},
             {"de": "cliente", "hora": "19:55", "texto": u"manda o pix"},
             {"de": "agente", "hora": "19:55",
              "texto": u"Aqui: pay.exemplo.com.br/metodo-pix\nO desconto já está aplicado."},
         ]},
        {"id": "nao", "rotulo": u"Não quer mais",
         "nota": (u"<strong>Insistir é o que transforma recuperação em perseguição.</strong> "
                  u"Um \"não\" encerra a sequência na hora e a pessoa entra na lista de "
                  u"quem não recebe mais mensagem. Isso é exigência da LGPD e é o que "
                  u"impede o seu número de ser bloqueado."),
         "mensagens": [
             {"de": "agente", "hora": "14:20", "espera": 500,
              "texto": u"Oi, Camila! Vi que você não finalizou a compra do Método Vender Mais. Ficou alguma dúvida?"},
             {"de": "cliente", "hora": "14:26",
              "texto": u"não quero mais, desisti. não me manda mais mensagem"},
             {"de": "agente", "hora": "14:26",
              "texto": u"Sem problema, Camila. Já removi você desta lista e não vou mais te procurar sobre isso.\nSe mudar de ideia um dia, é só chamar aqui. Obrigado pelo seu tempo."},
         ]},
        {"id": "aluno", "rotulo": u"Aluno com problema",
         "nota": (u"<strong>Depois da venda o mesmo agente vira suporte.</strong> "
                  u"As dúvidas de acesso são quase sempre as mesmas cinco — e são "
                  u"justamente as que geram pedido de reembolso quando ninguém responde."),
         "mensagens": [
             {"de": "cliente", "hora": "07:12",
              "texto": u"bom dia, comprei ontem e não consigo entrar na plataforma"},
             {"de": "agente", "hora": "07:12", "espera": 500,
              "texto": u"Bom dia! Vamos resolver. O acesso vai para o mesmo e-mail usado na compra — e às vezes cai no lixo eletrônico ou na aba de promoções."},
             {"de": "agente", "hora": "07:12",
              "texto": u"Me confirma o e-mail que você usou?"},
             {"de": "cliente", "hora": "07:15", "texto": u"juliana.costa@exemplo.com"},
             {"de": "agente", "hora": "07:15",
              "texto": u"Achei sua compra. Reenviei o acesso agora para esse e-mail.\nSe em cinco minutos não chegar, me avisa que eu chamo uma pessoa do suporte."},
             {"de": "cliente", "hora": "07:19", "texto": u"chegou! valeu"},
         ]},
    ],
}

FAQ3 = [
    (u"Como funciona a recuperação de carrinho abandonado no WhatsApp?",
     u"Quando alguém preenche os dados no checkout e não conclui o pagamento, a plataforma "
     u"avisa o sistema. Passados cerca de 30 minutos — tempo de a pessoa voltar sozinha — "
     u"o agente manda uma mensagem no WhatsApp perguntando se ficou alguma dúvida. Se a "
     u"pessoa responde, ele conversa, resolve o que travou e devolve o link do carrinho."),
    (u"Com quais plataformas isso funciona?",
     u"Com as que avisam quando um carrinho é abandonado — Hotmart, Kiwify e Eduzz, entre "
     u"outras, além de lojas próprias. Antes de fechar qualquer coisa eu confiro na sua "
     u"conta se esse aviso existe e está ligado, porque sem ele não há o que automatizar."),
    (u"Mandar mensagem para quem abandonou o carrinho é permitido pela LGPD?",
     u"É preciso ter uma base legal para o contato, e o momento de garantir isso é no "
     u"checkout: a pessoa informou o telefone e foi avisada de que poderia ser contatada "
     u"sobre a compra. Além disso, todo pedido de parar tem que ser respeitado na hora, e "
     u"a pessoa precisa conseguir sair a qualquer momento. Se o seu checkout hoje não deixa "
     u"isso claro, o primeiro passo é ajustar o checkout — não automatizar em cima de um "
     u"problema. Eu falo isso antes de vender."),
    (u"Quanto eu vou recuperar?",
     u"Não tem como eu responder isso com honestidade. Depende do seu produto, do preço, de "
     u"quanto a pessoa já conhecia você e de por que ela parou. Você vai ver por aí promessas "
     u"de aumento garantido nas vendas — eu não repito esse tipo de número porque não posso "
     u"garanti-lo. O que dá para garantir é que hoje, sem a mensagem, a taxa de recuperação "
     u"dessas pessoas é praticamente zero."),
    (u"O agente vai ficar insistindo e queimar minha marca?",
     u"Não, porque a insistência é limitada de propósito: uma mensagem depois de meia hora e, "
     u"no máximo, uma segunda no dia seguinte. Qualquer sinal de \"não quero\" encerra tudo "
     u"na hora. Além de ser o certo, é o que evita bloqueio em massa do seu número."),
    (u"Posso oferecer desconto automático?",
     u"Pode, se você quiser — e só nas condições que você definir por escrito. O agente nunca "
     u"cria desconto por conta própria. Muita gente prefere não dar desconto nenhum na "
     u"primeira mensagem, para não ensinar o cliente a abandonar o carrinho de propósito."),
    (u"Serve também para loja de produto físico?",
     u"Serve, com o mesmo princípio: carrinho abandonado, dúvida antes da compra, aviso de "
     u"envio e pós-venda. O que muda é o roteiro e a integração com a plataforma da loja."),
]


def pagina3():
    wa = P.wa(u"Olá, Renan! Vi a página de recuperação de vendas no WhatsApp e quero "
              u"um orçamento.")

    corpo = hero(
        SLUG3,
        u'<a href="/agentes-de-ia/">Agentes de IA</a><span>/</span><span>Recuperação de vendas</span>',
        u"Infoprodutores e lojas online — Brasil inteiro",
        u"Recuperação de vendas no WhatsApp: o carrinho abandonado volta",
        u"A pessoa entrou no checkout, preencheu os dados e parou. Muitas vezes não foi "
        u"falta de interesse — foi uma dúvida que ninguém respondeu. Um agente de IA puxa "
        u"essa conversa de volta meia hora depois, resolve o que travou e devolve o link.",
        wa,
        [u"Mensagem em 30 minutos", u"Para na primeira recusa", u"Vira suporte depois da venda"],
        u"O que a recuperação de vendas no WhatsApp faz",
        [u"Detecta quem chegou no pagamento e não concluiu.",
         u"Manda uma mensagem escrita na hora, com o nome da pessoa.",
         u"Responde a dúvida que travou a compra e devolve o link.",
         u"Encerra na hora se a pessoa disser que não quer.",
         u"Vira suporte de aluno depois que a venda acontece.",
         u"Mostra quantas conversas viraram compra."])

    corpo += secao_texto(
        u"O problema",
        u"A venda que você já pagou para conseguir e deixou escapar no último passo",
        [u"<strong>Chegar no checkout é a parte cara.</strong> Você pagou anúncio, "
         u"produziu conteúdo, construiu confiança durante semanas. Quando a pessoa "
         u"preenche o nome e o telefone na tela de pagamento, todo esse investimento já "
         u"foi feito.",
         u"E é exatamente aí que a maior parte some. Muitas vezes não por desinteresse: "
         u"some porque apareceu uma dúvida boba — \"dá para parcelar?\", \"o acesso é na "
         u"hora?\", \"tem garantia mesmo?\" — e não tinha ninguém do outro lado para "
         u"responder naquele minuto.",
         u"O e-mail de recuperação ajuda pouco: cai na aba de promoções, é aberto no dia "
         u"seguinte, quando a vontade já passou. O WhatsApp é lido em minutos. É a chance "
         u"real de falar com a pessoa enquanto ela ainda está pensando no assunto."])

    corpo += A.bloco_linha_tempo(
        u"O que acontece minuto a minuto",
        u"A sequência",
        u"Do abandono até a compra recuperada. Tudo automático, e tudo com limite: "
        u"no máximo duas mensagens, e nenhuma se a pessoa pedir para parar.",
        [(u"20h02", u"A pessoa desiste no pagamento",
          u"Ela preencheu nome, e-mail e telefone no checkout, chegou na tela de "
          u"pagamento e fechou. A plataforma registra o carrinho abandonado."),
         (u"20h02 às 20h32", u"Meia hora de silêncio, de propósito",
          u"Boa parte das pessoas volta sozinha nesse intervalo. Mandar mensagem antes "
          u"disso é atrapalhar quem já ia comprar."),
         (u"20h32", u"Chega a primeira mensagem",
          u"Escrita na hora, com o nome da pessoa e o nome do produto. Sem link de "
          u"desconto, sem pressão: só uma pergunta sobre o que ficou faltando."),
         (u"20h33", u"A conversa acontece de verdade",
          u"A pessoa responde e o agente conversa: tira a dúvida sobre parcelamento, "
          u"acesso, garantia ou conteúdo, e devolve o link do mesmo carrinho."),
         (u"Dia seguinte", u"Uma segunda mensagem, no máximo",
          u"Só para quem não respondeu nada. Depois disso, silêncio: insistir mais que "
          u"isso queima a marca e faz seu número ser bloqueado."),
         (u"Depois da compra", u"O mesmo agente vira suporte",
          u"\"Não recebi o acesso\", \"não consigo entrar\", \"onde fica a aula 3\". "
          u"São as dúvidas que viram pedido de reembolso quando ninguém responde.")])

    corpo += A.bloco_whatsapp(
        u"Veja a recuperação de vendas no WhatsApp acontecendo",
        u"Demonstração",
        u"Quatro situações comuns de quem abandona o carrinho. Troque o cenário nos "
        u"botões e acompanhe a conversa no celular.",
        ROTEIRO3,
        paragrafos=[
            u"Repare que em nenhuma delas o agente empurra a venda. Ele pergunta o que "
            u"faltou, responde, e deixa a pessoa decidir.",
            u"<strong>O cenário mais importante é o terceiro.</strong> Saber parar "
            u"quando a pessoa diz não é o que separa recuperação de vendas de "
            u"perseguição — e é o que mantém o seu número funcionando.",
        ])

    corpo += A.bloco_calculadora(
        "carrinho",
        u"Quanto está parado no seu carrinho abandonado",
        u"Faça a conta",
        u"Arraste as barrinhas com os números do seu produto. É o valor que passou "
        u"pelo checkout e não virou venda.",
        [("carrinhos", u"Carrinhos abandonados por mês", 5, 500, 5, 60, "num",
          u"", u"5", u"500"),
         ("ticket", u"Preço do seu produto", 47, 3000, 10, 497, "reais",
          u"", u"R$ 47", u"R$ 3.000")],
        u"Passou pelo checkout e não virou venda",
        u"Ninguém recupera tudo isso — nem perto. O \"1 em cada 10\" acima é "
        u"<strong>uma conta de exemplo para dar ordem de grandeza</strong>, não uma "
        u"previsão do seu resultado. O ponto é outro: hoje, sem nenhuma mensagem, "
        u"a recuperação dessas pessoas é praticamente zero.")

    corpo += secao_cards(
        u"Onde funciona",
        u"Plataformas e o que precisa estar ligado",
        u"O agente não conversa com a sua plataforma por mágica: ela precisa avisar "
        u"quando um carrinho é abandonado. Eu confiro isso na sua conta antes de "
        u"fechar qualquer coisa.",
        [(u"Hotmart, Kiwify e Eduzz",
          u"As três avisam sobre carrinho abandonado e sobre compra aprovada. É o "
          u"cenário mais comum e o mais simples de ligar."),
         (u"Loja própria ou outra plataforma",
          u"Funciona sempre que houver um aviso automático de carrinho abandonado. "
          u"Se a sua não tiver, eu te digo isso na primeira conversa em vez de "
          u"empurrar um serviço que não vai funcionar."),
         (u"Um número de WhatsApp para o negócio",
          u"De preferência não o seu pessoal. Volume alto de mensagem em número "
          u"pessoal é o caminho mais rápido para bloqueio."),
         (u"Um checkout que avisa sobre o contato",
          u"A pessoa precisa saber, no momento em que informa o telefone, que pode "
          u"ser contatada sobre a compra. Isso é base legal, e é o primeiro item "
          u"que eu verifico."),
         (u"Suas respostas, escritas por você",
          u"Parcelamento, garantia, conteúdo, prazo de acesso. O agente só fala o "
          u"que você autorizou — ele não estuda seu produto sozinho."),
         (u"Uma lista de quem não quer contato",
          u"Mantida automaticamente. Quem pediu para parar, para de receber, "
          u"para sempre.")])

    corpo += secao_texto(
        u"Honestidade",
        u"O que eu não vou prometer sobre recuperação de vendas",
        [u"<strong>Não existe porcentagem garantida.</strong> Você vai ver muita gente "
         u"vendendo aumento certo de faturamento. Eu não sei quanto o seu produto vai "
         u"recuperar, e quem diz que sabe está chutando com a sua expectativa.",
         u"<strong>Não é para consertar produto que não vende.</strong> Se as pessoas "
         u"abandonam porque o preço não faz sentido ou a oferta não convence, mensagem "
         u"nenhuma resolve. Automação amplifica o que existe: se a oferta é boa, ajuda "
         u"muito; se é ruim, só faz mais gente dizer não mais rápido.",
         u"<strong>Não é lista fria disfarçada.</strong> Isto aqui é para quem chegou "
         u"até o seu checkout e deixou o telefone. Não é para disparo em massa, não é "
         u"para lista comprada, e eu não faço esse tipo de trabalho."])

    corpo += A.bloco_depoimentos(NOTA_DEPO)
    corpo += A.bloco_faq(u"Perguntas frequentes sobre recuperação de vendas no WhatsApp",
                         FAQ3)
    corpo += A.bloco_cta(
        u"Me diga quantos carrinhos você abandona por mês",
        u"Com esse número e o preço do seu produto, eu te digo se vale a pena "
        u"automatizar, o que precisa estar ligado na sua plataforma e quanto custa.",
        wa, SLUG3)
    corpo += u"  </main>\n"

    servico = {
        "@type": "Service", "@id": URL3 + "#service",
        "name": u"Recuperação de carrinho abandonado no WhatsApp",
        "serviceType": u"Automação de recuperação de vendas com inteligência artificial",
        "description": (u"Agente de inteligência artificial que entra em contato pelo "
                        u"WhatsApp com quem abandonou o checkout, responde a dúvida que "
                        u"travou a compra, devolve o link do carrinho e atua como suporte "
                        u"depois da venda."),
        "provider": {"@id": M.ID_EMPRESA},
        "audience": {"@type": "Audience",
                     "audienceType": u"Infoprodutores e lojas online"},
        "areaServed": {"@type": "Country", "name": "Brasil"},
    }
    schema = A.schema_pagina(URL3, TITLE3, DESC3,
                             [(u"Início", BASE + "/"),
                              (u"Agentes de IA", URL1),
                              (u"Recuperação de vendas", URL3)],
                             servico=servico, faq=FAQ3)
    return A.montar_pagina(
        os.path.join(RAIZ, SLUG3, "index.html"), SLUG3, URL3, TITLE3, DESC3,
        u"Recuperação de carrinho abandonado no WhatsApp",
        u"Quem parou no pagamento recebe mensagem em 30 minutos, tira a dúvida e "
        u"volta. Veja a conversa simulada.",
        schema, corpo)


def main():
    for nome, fn in ((SLUG1, pagina1), (SLUG2, pagina2), (SLUG3, pagina3)):
        tamanho = fn()
        print(u"gerado: /%s/  (%d bytes)" % (nome, tamanho))


if __name__ == "__main__":
    main()
