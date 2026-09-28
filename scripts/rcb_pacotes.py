# -*- coding: utf-8 -*-
"""
Fonte unica dos pacotes (rodada de conversao de 09/08/2026).

DESDE 28/09/2026 O SITE NAO MOSTRA PRECO NENHUM (decisao do Renan). Os pacotes
continuam descrevendo o que cada um entrega, mas o valor sai sob medida no
WhatsApp. Os campos de valor foram removidos de proposito; o
conferir-conversao.py acusa qualquer preco da RCB que reapareca.

Quem usa:
  - aplicar-conversao.py       (aplica nas paginas escritas a mao)
  - gerar-paginas-cidades.py   (embute nas 199 paginas de cidade)

Mexeu no preco ou no que cada pacote inclui? Mude AQUI e rode os dois:
    python scripts/aplicar-conversao.py
    python scripts/gerar-paginas-cidades.py

Mexer direto no HTML de uma pagina de cidade nao adianta: a proxima
regeracao sobrescreve.
"""
from urllib.parse import quote

WHATS = "5562991161040"

MARCA_INI = "<!-- RCB:PACOTES:INICIO -->"
MARCA_FIM = "<!-- RCB:PACOTES:FIM -->"
MARCA_CTA = "<!-- RCB:CTA-MOBILE -->"

# 2a frase da linha de apoio da tabela. Paginas de nicho trocam por uma versao
# na lingua delas (ver FECHOS no aplicar-conversao.py).
FECHO_PADRAO = "Me conte o seu caso no WhatsApp e receba o orçamento em até 24 horas."

PACOTES = [
    {
        "id": "presenca-lite",
        "nome": "Pacote Presença Lite",
        "para": "Para quem já tem site, mas o Google Meu Negócio está largado.",
        "itens": [
            ("Google Meu Negócio configurado e otimizado", False),
            ("10 fotos profissionais publicadas no seu perfil", False),
            ("Avaliações organizadas e respostas configuradas", False),
            ("Perfil entregue em 7 dias úteis", True),
        ],
        "botao": "Quero arrumar meu Google",
    },
    {
        "id": "presenca",
        "nome": "Pacote Presença",
        "para": "Para quem ainda não tem nada no ar, ou tem e está abandonado.",
        "itens": [
            ("Site completo com até 5 páginas: início, serviços, sobre, contato e localização", False),
            ("Google Meu Negócio configurado e otimizado", False),
            ("10 fotos profissionais publicadas no seu perfil", False),
            ("Avaliações organizadas e respostas configuradas", False),
            ("Site entregue em 7 dias úteis", True),
        ],
        "botao": "Quero aparecer no Google",
    },
    {
        "id": "crescimento",
        "nome": "Pacote Crescimento",
        "para": "Para quem já tem o básico e quer subir de posição todo mês.",
        "itens": [
            ("Tudo do Pacote Presença", True),
            ("2 textos novos por mês no seu site", False),
            ("Suas avaliações no Google acompanhadas e respondidas", False),
            ("Relatório mensal: quantas pessoas te encontraram no Google", False),
            ("Ajustes no site todo mês, conforme o que os números mostram", False),
        ],
        "botao": "Quero crescer no Google",
    },
    {
        "id": "dominacao",
        "nome": "Pacote Dominação",
        "para": "Para quem quer ser o primeiro resultado da cidade no seu ramo.",
        "itens": [
            ("Tudo do Pacote Crescimento", True),
            ("4 textos novos por mês", False),
            ("Uma página dedicada para cada serviço que você oferece", False),
            ("3 concorrentes diretos acompanhados todo mês", False),
            ("Prioridade no atendimento: sua mensagem passa na frente", False),
        ],
        "botao": "Quero dominar minha cidade",
    },
]


def wa(texto):
    """Link do WhatsApp com a mensagem ja escrita."""
    return "https://wa.me/%s?text=%s" % (WHATS, quote(texto, safe=""))


def bloco_pacotes(negocio, data_page, onde="", fecho=FECHO_PADRAO):
    """negocio: 'uma clínica' / 'um comércio local' — entra na mensagem do WhatsApp.
    onde: sufixo opcional para o texto de apoio (ex.: ' em Anápolis').
    fecho: 2a frase da linha de apoio. Existe para a pagina falar na lingua do
    nicho dela ('...que a sua clinica pode dar agora') sem que a regeracao
    apague o texto proprio."""
    cards = []
    for p in PACOTES:
        itens = "".join(
            '\n              <li%s>%s</li>' % (' class="destaque-item"' if d else "", t)
            for t, d in p["itens"]
        )
        # A garantia fecha os tres cartoes: e o argumento que derruba o medo de
        # pagar, e antes dela so aparecia la embaixo, longe do preco.
        itens += '\n              <li class="pacote-garantia">Garantia de 30 dias</li>'
        selo = '\n            <span class="pacote-selo">Mais escolhido</span>' if p["id"] == "crescimento" else ""
        destaque = " destaque" if p["id"] == "crescimento" else ""
        msg = ("Olá! Tenho %s%s e quero um orçamento do %s. Pode me explicar como funciona?"
               % (negocio, onde, p["nome"]))
        cards.append(
            '\n          <article class="pacote-card%s">%s'
            '\n            <h3 class="pacote-nome">%s</h3>'
            '\n            <p class="pacote-para">%s</p>'
            '\n            <p class="pacote-condicao">Valor sob medida para o tamanho do seu negócio</p>'
            '\n            <ul class="pacote-lista">%s'
            '\n            </ul>'
            '\n            <a href="%s" class="btn btn-primary btn-full" target="_blank" rel="noopener noreferrer" '
            'data-event="cta_click" data-location="pacote_%s" data-page="%s">%s</a>'
            '\n          </article>\n'
            % (destaque, selo, p["nome"], p["para"],
               itens, wa(msg), p["id"], data_page, p["botao"])
        )

    duvida = ("Olá! Tenho %s%s e quero um orçamento, mas não sei qual pacote escolher. "
              "Pode olhar meu Google e me dizer?" % (negocio, onde))

    return (
        '    %s\n'
        '    <section class="pacotes-section" id="pacotes" aria-labelledby="pacotes-titulo">\n'
        '      <div class="container">\n'
        '        <div class="section-header">\n'
        '          <div class="section-tag">Orçamento grátis</div>\n'
        '          <h2 id="pacotes-titulo" class="section-title">Escolha por onde começar — o valor sai sob medida</h2>\n'
        '          <p class="section-desc">Cada negócio tem um tamanho, e o investimento acompanha: '
        'pode sair bem mais em conta do que você imagina. '
        '%s</p>\n'
        '        </div>\n'
        '        <div class="pacotes-grid">\n%s        </div>\n'
        '        <p class="pacotes-nota"><strong>Não sabe qual escolher?</strong> '
        '<a href="%s" target="_blank" rel="noopener noreferrer" data-event="cta_click" '
        'data-location="pacotes_duvida" data-page="%s">Me chame no WhatsApp</a> e me conte do seu negócio. '
        'Eu olho seu Google antes de você investir qualquer coisa e digo com franqueza qual dos quatro faz '
        'sentido — inclusive se a resposta for o mais simples.</p>\n'
        '      </div>\n'
        '    </section>\n'
        '    %s\n' % (MARCA_INI, fecho, "".join(cards), wa(duvida), data_page, MARCA_FIM)
    )


def bloco_cta_mobile(data_page, ancora="#pacotes"):
    """Barra fixa no rodape do celular. ancora = '#pacotes' na propria pagina,
    ou '/#pacotes' quando a pagina nao tem tabela de precos."""
    msg = "Olá! Vi seu site e quero um orçamento para aparecer no Google."
    return (
        '  %s\n'
        '  <div class="cta-mobile" aria-label="Ações rápidas">\n'
        '    <a href="%s" class="btn btn-outline" data-event="cta_click" '
        'data-location="cta_mobile_precos" data-page="%s">Orçamento grátis</a>\n'
        '    <a href="%s" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer" '
        'data-event="cta_click" data-location="cta_mobile_whatsapp" data-page="%s">Falar no WhatsApp</a>\n'
        '  </div>\n\n' % (MARCA_CTA, ancora, data_page, wa(msg), data_page)
    )


def ofertas():
    """Desde 28/09/2026: nenhuma Offer com preco. Lista vazia; quem monta o
    JSON-LD deve OMITIR a chave "offers"."""
    return []


# Item do menu que substituiu "Diagnostico gratuito".
def nav_ver_precos(data_page, ancora="#pacotes"):
    return ('<li><a href="%s" class="nav-link nav-cta" data-event="cta_click" '
            'data-location="navbar" data-page="%s">Orçamento grátis</a></li>' % (ancora, data_page))
