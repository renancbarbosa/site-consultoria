# -*- coding: utf-8 -*-
"""
Fonte unica dos pacotes com preco (rodada de conversao de 09/08/2026).

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
FECHO_PADRAO = "Pagamento por Pix pelo WhatsApp."

PACOTES = [
    {
        "id": "presenca-lite",
        "nome": "Pacote Presença Lite",
        "para": "Para quem já tem site, mas o Google Meu Negócio está largado.",
        "valor": "R$ 1.997",
        "periodo": "",
        "condicao": "Pagamento único",
        "itens": [
            ("Google Meu Negócio configurado e otimizado", False),
            ("10 fotos profissionais publicadas no seu perfil", False),
            ("Avaliações organizadas e respostas configuradas", False),
            ("Perfil entregue em 7 dias úteis", True),
        ],
        "botao": "Quero arrumar meu Google",
        "preco": "1997.00",
        "mensal": False,
    },
    {
        "id": "presenca",
        "nome": "Pacote Presença",
        "para": "Para quem ainda não tem nada no ar, ou tem e está abandonado.",
        "valor": "R$ 2.497",
        "periodo": "",
        "condicao": "Pagamento único",
        "itens": [
            ("Site completo com até 5 páginas: início, serviços, sobre, contato e localização", False),
            ("Google Meu Negócio configurado e otimizado", False),
            ("10 fotos profissionais publicadas no seu perfil", False),
            ("Avaliações organizadas e respostas configuradas", False),
            ("Site entregue em 7 dias úteis", True),
        ],
        "botao": "Quero aparecer no Google",
        "preco": "2497.00",
        "mensal": False,
    },
    {
        "id": "crescimento",
        "nome": "Pacote Crescimento",
        "para": "Para quem já tem o básico e quer subir de posição todo mês.",
        "valor": "R$ 2.997",
        "periodo": "/mês",
        "condicao": "Mínimo de 3 meses",
        "itens": [
            ("Tudo do Pacote Presença", True),
            ("2 textos novos por mês no seu site", False),
            ("Suas avaliações no Google acompanhadas e respondidas", False),
            ("Relatório mensal: quantas pessoas te encontraram no Google", False),
            ("Ajustes no site todo mês, conforme o que os números mostram", False),
        ],
        "botao": "Quero crescer no Google",
        "preco": "2997.00",
        "mensal": True,
    },
    {
        "id": "dominacao",
        "nome": "Pacote Dominação",
        "para": "Para quem quer ser o primeiro resultado da cidade no seu ramo.",
        "valor": "R$ 4.997",
        "periodo": "/mês",
        "condicao": "Mínimo de 3 meses",
        "itens": [
            ("Tudo do Pacote Crescimento", True),
            ("4 textos novos por mês", False),
            ("Uma página dedicada para cada serviço que você oferece", False),
            ("3 concorrentes diretos acompanhados todo mês", False),
            ("Prioridade no atendimento: sua mensagem passa na frente", False),
        ],
        "botao": "Quero dominar minha cidade",
        "preco": "4997.00",
        "mensal": True,
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
        periodo = ('<span class="periodo">%s</span>' % p["periodo"]) if p["periodo"] else ""
        selo = '\n            <span class="pacote-selo">Mais escolhido</span>' if p["id"] == "crescimento" else ""
        destaque = " destaque" if p["id"] == "crescimento" else ""
        msg = ("Olá! Tenho %s%s e quero o %s (%s%s). Pode me explicar como funciona?"
               % (negocio, onde, p["nome"], p["valor"], p["periodo"]))
        cards.append(
            '\n          <article class="pacote-card%s">%s'
            '\n            <h3 class="pacote-nome">%s</h3>'
            '\n            <p class="pacote-para">%s</p>'
            '\n            <div class="pacote-preco"><span class="valor">%s</span>%s</div>'
            '\n            <p class="pacote-condicao">%s</p>'
            '\n            <ul class="pacote-lista">%s'
            '\n            </ul>'
            '\n            <a href="%s" class="btn btn-primary btn-full" target="_blank" rel="noopener noreferrer" '
            'data-event="cta_click" data-location="pacote_%s" data-page="%s">%s</a>'
            '\n          </article>\n'
            % (destaque, selo, p["nome"], p["para"], p["valor"], periodo,
               p["condicao"], itens, wa(msg), p["id"], data_page, p["botao"])
        )

    duvida = ("Olá! Tenho %s%s e vi seus pacotes no site, mas não sei qual escolher. "
              "Pode olhar meu Google e me dizer?" % (negocio, onde))

    return (
        '    %s\n'
        '    <section class="pacotes-section" id="pacotes" aria-labelledby="pacotes-titulo">\n'
        '      <div class="container">\n'
        '        <div class="section-header">\n'
        '          <div class="section-tag">Preços</div>\n'
        '          <h2 id="pacotes-titulo" class="section-title">Quanto custa e o que está incluído</h2>\n'
        '          <p class="section-desc">Preço fechado, na tela, sem "solicite um orçamento". '
        '%s</p>\n'
        '        </div>\n'
        '        <div class="pacotes-grid">\n%s        </div>\n'
        '        <p class="pacotes-nota"><strong>Não sabe qual escolher?</strong> '
        '<a href="%s" target="_blank" rel="noopener noreferrer" data-event="cta_click" '
        'data-location="pacotes_duvida" data-page="%s">Me chame no WhatsApp</a> e me conte do seu negócio. '
        'Eu olho seu Google antes de você pagar qualquer coisa e digo com franqueza qual dos quatro faz '
        'sentido — inclusive se a resposta for o mais barato.</p>\n'
        '      </div>\n'
        '    </section>\n'
        '    %s\n' % (MARCA_INI, fecho, "".join(cards), wa(duvida), data_page, MARCA_FIM)
    )


def bloco_cta_mobile(data_page, ancora="#pacotes"):
    """Barra fixa no rodape do celular. ancora = '#pacotes' na propria pagina,
    ou '/#pacotes' quando a pagina nao tem tabela de precos."""
    msg = "Olá! Vi seu site e quero saber como faço para aparecer no Google."
    return (
        '  %s\n'
        '  <div class="cta-mobile" aria-label="Ações rápidas">\n'
        '    <a href="%s" class="btn btn-outline" data-event="cta_click" '
        'data-location="cta_mobile_precos" data-page="%s">Ver preços</a>\n'
        '    <a href="%s" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer" '
        'data-event="cta_click" data-location="cta_mobile_whatsapp" data-page="%s">Falar no WhatsApp</a>\n'
        '  </div>\n\n' % (MARCA_CTA, ancora, data_page, wa(msg), data_page)
    )


def ofertas():
    """Lista de Offer para colar no no Service do JSON-LD."""
    saida = []
    for p in PACOTES:
        o = {
            "@type": "Offer",
            "name": p["nome"],
            "price": p["preco"],
            "priceCurrency": "BRL",
            "availability": "https://schema.org/InStock",
        }
        if p["mensal"]:
            o["priceSpecification"] = {
                "@type": "UnitPriceSpecification",
                "price": p["preco"],
                "priceCurrency": "BRL",
                "unitCode": "MON",
                "billingDuration": 1,
                "billingIncrement": 1,
            }
        saida.append(o)
    return saida


def ofertas_json_compacto():
    """Mesmo conteudo de ofertas(), em texto, para gerador que monta JSON a mao."""
    import json
    return json.dumps(ofertas(), ensure_ascii=False, separators=(",", ":"))


# Item do menu que substituiu "Diagnostico gratuito".
def nav_ver_precos(data_page, ancora="#pacotes"):
    return ('<li><a href="%s" class="nav-link nav-cta" data-event="cta_click" '
            'data-location="navbar" data-page="%s">Ver preços</a></li>' % (ancora, data_page))
