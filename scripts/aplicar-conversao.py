# -*- coding: utf-8 -*-
"""
Aplica a refatoracao de conversao (rodada de 09/08/2026) em todo o site.

O que faz, conforme o tipo de pagina:

  COMERCIAL  -> bloco dos 3 pacotes com preco, barra fixa de CTA no celular,
                botao "Ver precos" no menu, precos na ficha do Google (JSON-LD)
                e correcao das frases que diziam "o investimento depende".
  APOIO      -> so o botao do menu e a barra do celular, ambos apontando para
                os precos da home (/#pacotes). Nao repete a tabela de precos em
                artigo de blog: seria repeticao em 68 paginas.
  IGNORADA   -> paginas legais e a demo em JS do diagnostico.

Idempotente: usa marcadores HTML e pode rodar quantas vezes quiser.

Uso:  python scripts/aplicar-conversao.py [--so-comerciais|--so-apoio]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rcb_pacotes import (
    FECHO_PADRAO, MARCA_CTA, MARCA_FIM, MARCA_INI, bloco_cta_mobile, bloco_pacotes,
    nav_ver_precos, ofertas,
)

# Paginas que falam na lingua do nicho no fim da linha de apoio da tabela.
# Fica aqui (e nao no HTML) para sobreviver a regeracao.
FECHOS = {
    "seo-para-dentistas": "Escolha o tamanho do passo que a sua clínica pode dar agora.",
    "seo-para-clinicas": "Escolha o tamanho do passo que a sua clínica pode dar agora.",
    "seo-para-clinicas-de-estetica": "Escolha o tamanho do passo que a sua clínica pode dar agora.",
    "para-comercios-locais": "Escolha o tamanho do passo que o seu comércio pode dar agora.",
}

RAIZ = Path(__file__).resolve().parent.parent
WHATS = "5562991161040"

# ---------------------------------------------------------------------------
# Paginas comerciais: recebem a tabela de precos.
# valor = como o visitante se descreve na mensagem do WhatsApp.
# ---------------------------------------------------------------------------
COMERCIAIS = {
    "seo-para-dentistas": "uma clínica odontológica",
    "seo-para-clinicas-de-estetica": "uma clínica de estética",
    "seo-para-clinicas": "uma clínica",
    "para-comercios-locais": "um comércio local",
    "seo-para-medicos": "um consultório médico",
    "seo-para-clinicas-de-emagrecimento": "uma clínica de emagrecimento",
    "google-meu-negocio-para-clinicas": "uma clínica",
    "site-para-clinica": "uma clínica",
    "marketing-para-clinicas": "uma clínica",
    "como-atrair-mais-pacientes": "uma clínica",
    "para-advogados": "um escritório de advocacia",
    "marketing-para-advogados": "um escritório de advocacia",
    "para-profissionais-liberais": "um negócio",
    "seo-para-contadores": "um escritório de contabilidade",
    "seo-para-psicologos": "um consultório de psicologia",
    "seo-para-veterinarios": "uma clínica veterinária",
    "seo-para-imobiliarias": "uma imobiliária",
    "seo-para-pequenas-empresas": "uma empresa pequena",
    "consultoria-seo-local": "um negócio",
    "consultor-seo-goiania": "um negócio em Goiânia",
    "seo-local-goiania": "um negócio em Goiânia",
    "como-aparecer-no-google": "um negócio",
    "acompanhamento-seo": "um negócio",
    "auditoria-seo": "um negócio",
    "google-perfil-empresa": "um negócio",
    "site-otimizado-para-seo": "um negócio",
    "conteudo-para-seo": "um negócio",
    "consultoria-seo": "um negócio",
    "contato": "um negócio",
    "cases": "um negócio",
    "diagnostico-presenca-digital": "um negócio",
}

# Paginas que nao levam tabela de preco, so o menu e a barra do celular.
APOIO_FIXAS = [
    "blog", "guia-seo-local", "sobre", "automacao-de-processos",
    "privacidade", "cookies",
]

# Nem o menu nem a barra: pagina legal sem navbar, ou demo noindex.
IGNORADAS = {"diagnostico-presenca-digital/exemplo", "404"}

# Frases que contradizem o preco publicado -> texto novo.
CONTRADICOES = [
    ("Em vez de pacote pronto, eu começo com um diagnóstico: avalio a sua presença hoje no Google, mostro o que está travando o resultado e proponho um plano com faixas de investimento compatíveis com a realidade da sua clínica.",
     "O preço está publicado aqui na página: R$ 1.997 ou R$ 2.497 em pagamento único, ou R$ 2.997 e R$ 4.997 por mês. Antes de você pagar qualquer coisa eu olho seu Google de graça e digo com franqueza qual dos quatro faz sentido."),
    ("Para ter uma ideia do investimento no seu caso, <a href=\"/diagnostico-presenca-digital/\">solicite um diagnóstico gratuito</a> e eu te retorno com uma proposta personalizada.",
     "Ficou em dúvida sobre qual pacote escolher? Me chame no WhatsApp que eu olho seu caso e te digo, sem compromisso."),
    ("O investimento depende do momento, da concorrência e do escopo. O diagnóstico gratuito ajuda a entender se faz sentido agora.",
     "Cabe sim, e o preço está publicado nesta página: R$ 1.997 no Presença Lite, R$ 2.497 no Pacote Presença, R$ 2.997 por mês no Crescimento e R$ 4.997 por mês no Dominação."),
    ("não existe preço de tabela — existe escopo",
     "hoje eu trabalho com preço de tabela, publicado no site"),
    ("Não existe preço de tabela — existe escopo",
     "Hoje eu trabalho com preço de tabela, publicado no site"),
]

NAV_ANTIGO = '<li><a href="/diagnostico-presenca-digital/" class="nav-link nav-cta">Diagnóstico gratuito</a></li>'


def aplicar(rel, negocio, comercial):
    """rel = caminho do index.html. Devolve lista do que mudou."""
    caminho = RAIZ / rel
    h = caminho.read_text(encoding="utf-8")
    original = h
    dp = rel.replace("/index.html", "").replace("/", "-") or "home"
    ancora = "#pacotes" if comercial else "/#pacotes"
    feito = []

    # 1. classe no body -------------------------------------------------
    if "tem-cta-mobile" not in h and "<body" in h:
        h = re.sub(r"<body>", '<body class="tem-cta-mobile">', h, count=1)
        h = re.sub(r'<body class="(?!tem-cta-mobile)([^"]*)">',
                   r'<body class="\1 tem-cta-mobile">', h, count=1)
        if "tem-cta-mobile" in h:
            feito.append("body")

    # 2. botao do menu ---------------------------------------------------
    if NAV_ANTIGO in h:
        h = h.replace(NAV_ANTIGO, nav_ver_precos(dp, ancora))
        feito.append("menu")

    # 3. barra fixa no celular -------------------------------------------
    if MARCA_CTA not in h and "whatsapp-float" in h:
        i = h.find('  <a href="https://wa.me/')
        if i == -1:
            i = h.find('<a href="https://wa.me/')
        if i != -1:
            h = h[:i] + bloco_cta_mobile(dp, ancora) + h[i:]
            feito.append("barra mobile")

    # 4. tabela de precos -------------------------------------------------
    # O hub e as 199 cidades sao donos do proprio bloco: o gerador escreve neles
    # o nome da cidade dentro da mensagem do WhatsApp ("...um negocio em Anapolis").
    # Reescrever daqui apagaria isso. Quem atualiza preco la e o gerar-paginas-cidades.py.
    # /consultoria-seo/palmas/ e a excecao: esta no disco mas o gerador nao a
    # produz (residuo de colisao de slug). Se ela ficar de fora dos dois, o
    # preco dela congela. Por isso o bloco dela e atualizado daqui.
    do_gerador = (rel.startswith("consultoria-seo/")
                  and rel != "consultoria-seo/palmas/index.html")

    # 4a. Ja tem a tabela: troca o bloco inteiro pelo atual. Sem isso, mexer no
    # rcb_pacotes.py (preco, itens, garantia) nao chegaria nas paginas que ja
    # foram feitas -- so nas novas.
    # Vale mesmo em pagina de apoio: /blog/quanto-custa-consultoria-seo-local/
    # mostra a tabela e nao esta na lista de comerciais.
    if not do_gerador and MARCA_INI in h:
        novo = bloco_pacotes(negocio, dp, fecho=FECHOS.get(rel.replace("/index.html", ""), FECHO_PADRAO))
        antes = h
        atual = re.compile(r'[ \t]*%s.*?%s\n' % (re.escape(MARCA_INI), re.escape(MARCA_FIM)), re.S)
        h = atual.sub(lambda m: novo, h, count=1)
        if h != antes:
            feito.append("precos (atualizados)")
    if comercial and not do_gerador and MARCA_INI not in h:
        novo = bloco_pacotes(negocio, dp, fecho=FECHOS.get(rel.replace("/index.html", ""), FECHO_PADRAO))
        # 4b. substitui uma secao antiga de "quanto custa", se houver
        padrao = re.compile(
            r'[ \t]*<section class="solution-section section-[a-z-]*precos">.*?</section>\n', re.S)
        h, n = padrao.subn(lambda m: novo, h, count=1)
        if n:
            feito.append("precos (no lugar da secao antiga)")
        else:
            for alvo in ('    <section class="faq-section"',
                         '    <section class="faq"',
                         '<section class="faq-section"',
                         '    <section class="cta-band"',
                         '<section class="cta-band"',
                         '    <section class="cta-final"',
                         "  </main>",
                         "</main>"):
                i = h.find(alvo)
                if i != -1:
                    h = h[:i] + novo + ("\n" if not alvo.strip().startswith("</") else "") + h[i:]
                    feito.append("precos (antes de %s)" % alvo.strip()[:26])
                    break

    # 5. precos na ficha do Google ---------------------------------------
    # Nao basta ser "comercial": /blog/quanto-custa-consultoria-seo-local/ mostra
    # a tabela e e pagina de apoio. Quem mostra preco tem que ter preco no schema.
    if comercial or MARCA_INI in h:
        def injeta(m):
            try:
                dados = json.loads(m.group(1))
            except ValueError:
                return m.group(0)
            nos = dados.get("@graph") if isinstance(dados, dict) and "@graph" in dados else [dados]
            mudou = False
            for no in nos:
                # Sobrescreve sempre: se so inserisse quando falta, mudar preco
                # no rcb_pacotes.py nunca chegaria a quem ja tem "offers".
                if isinstance(no, dict) and no.get("@type") == "Service":
                    novas = ofertas()
                    if no.get("offers") != novas:
                        no["offers"] = novas
                        mudou = True
            # Pagina sem no Service nenhum: cria um, senao o preco aparece para
            # o visitante mas nao para o Google.
            if not mudou and isinstance(dados, dict) and "@graph" in dados:
                tem_service = any(isinstance(n, dict) and n.get("@type") == "Service" for n in nos)
                if not tem_service:
                    nos.append({
                        "@type": "Service",
                        "serviceType": "Consultoria de SEO",
                        "name": "Site e Google Meu Negócio para negócios locais",
                        "provider": {"@type": "LocalBusiness",
                                     "@id": "https://rcbseo.com.br/#business"},
                        "areaServed": {"@type": "Country", "name": "Brasil"},
                        "offers": ofertas(),
                    })
                    mudou = True
            if not mudou:
                return m.group(0)
            return ('<script type="application/ld+json">'
                    + json.dumps(dados, ensure_ascii=False, indent=2) + "</script>")

        antes = h
        h = re.sub(r'<script type="application/ld\+json">(.*?)</script>', injeta, h, flags=re.S)
        if h != antes:
            feito.append("schema")

    # 6. frases que contradizem o preco ----------------------------------
    n_contra = 0
    for velho, novo in CONTRADICOES:
        if velho in h:
            h = h.replace(velho, novo)
            n_contra += 1
    if n_contra:
        feito.append("%d contradicao(oes) de preco" % n_contra)

    if h != original:
        caminho.write_text(h, encoding="utf-8")
    return feito


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    alvos = []

    if arg != "--so-apoio":
        for slug, negocio in COMERCIAIS.items():
            alvos.append((slug + "/index.html", negocio, True))
        # A home NAO entra: ela foi reescrita a mao e ja tem tabela de precos,
        # barra fixa e menu proprios. Injetar aqui criava uma segunda tabela e
        # uma segunda barra de CTA na mesma pagina (corrigido em 09/08/2026).

    if arg != "--so-comerciais":
        for slug in APOIO_FIXAS:
            alvos.append((slug + "/index.html", "um negócio", False))
        for artigo in sorted((RAIZ / "blog").glob("*/index.html")):
            alvos.append(("blog/" + artigo.parent.name + "/index.html", "um negócio", False))
        for cidade in sorted((RAIZ / "consultoria-seo").glob("*/index.html")):
            alvos.append(("consultoria-seo/" + cidade.parent.name + "/index.html",
                          "um negócio", True))

    total_mudadas = 0
    resumo = {}
    for rel, negocio, comercial in alvos:
        if rel.replace("/index.html", "") in IGNORADAS:
            continue
        if not (RAIZ / rel).exists():
            print("  ! nao existe:", rel)
            continue
        feito = aplicar(rel, negocio, comercial)
        if feito:
            total_mudadas += 1
            for f in feito:
                chave = re.sub(r"\d+", "N", f)
                resumo[chave] = resumo.get(chave, 0) + 1

    print("paginas alteradas:", total_mudadas, "de", len(alvos))
    for k, v in sorted(resumo.items(), key=lambda x: -x[1]):
        print("   %-42s %d" % (k, v))


if __name__ == "__main__":
    main()
