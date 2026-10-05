# -*- coding: utf-8 -*-
"""
Gera as páginas de serviço da linha "Sites e Anúncios" (28/09/2026):

  /criacao-de-landing-page/
  /gestao-de-trafego-pago/
  /criacao-de-loja-virtual-goiania/

Conteúdo: scripts/conteudo/servicos_marketing.py (escrito à mão).

ESQUELETO: copiado em tempo de execução de /criacao-de-sites-goiania/index.html
(head técnico, menu, rodapé, barra do celular, aviso de cookies). Motivo: o
rcb_base.py está defasado em relação ao site no ar (menu com "Diagnóstico
gratuito", coluna "SEO Nacional" da divisão revertida, sem barra do celular).
Copiar da página viva garante que as páginas novas saiam iguais ao resto.

Regras: SEM PREÇO da RCB; todo CTA vai para o WhatsApp com mensagem própria.

Idempotente: sobrescreve os três arquivos. Tipos de seção aceitos:
  split     texto + cartão lateral         texto   texto corrido com H2
  cards     grade de cartões                faixas  "quanto custa" (faixas de mercado)
  orcamento cartões de orçamento -> WhatsApp passos  3 passos + botão
"""
import html as H
import io
import json
import os
import re
import sys
from urllib.parse import quote

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "conteudo"))
sys.path.insert(0, AQUI)
import rcb_marca as M  # ficha unica da marca (data/marca.json)
from servicos_marketing import PAGINAS as _GERAIS  # noqa: E402
from servicos_nichos import PAGINAS as _NICHOS  # noqa: E402  (serviço + nicho, 28/09/2026)

PAGINAS = _GERAIS + _NICHOS

RAIZ = os.path.dirname(AQUI)
BASE = "https://rcbseo.com.br"
MODELO = "criacao-de-sites-goiania"
WHATS = "5562991161040"
DATA = "2026-09-28"


def wa(msg):
    return "https://wa.me/%s?text=%s" % (WHATS, quote(msg, safe=""))


def e(t):
    return H.escape(t, quote=True)


def cta(href, txt, loc, slug, classe="btn btn-primary"):
    return ('<a class="%s" href="%s" target="_blank" rel="noopener noreferrer" data-event="cta_click" '
            'data-location="%s" data-page="%s">%s</a>' % (classe, href, loc, slug, txt))


# ---------------------------------------------------------------- seções
def autor_data(p):
    """Linha 'Por Renan ... | Atualizado em ...' (opcional: so quem tem p['data'])."""
    if not p.get("data"):
        return ""
    a, m, d = p["data"].split("-")
    return ('\n          <p class="page-byline">Por <a href="/sobre/">Renan Carvalho Barbosa</a> · '
            'Atualizado em <time datetime="%s">%s/%s/%s</time></p>' % (p["data"], d, m, a))


def s_chamada(d, slug):
    """Faixa com um link de destaque (ex.: modelo demonstrativo)."""
    return """
    <section class="solution-section alt-bg">
      <div class="container">
        <div class="split-copy" style="max-width:860px;margin:0 auto;text-align:center">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>%s
          <div class="page-actions" style="justify-content:center;margin-top:1.5rem">
            <a class="btn btn-outline" href="%s" data-event="cta_click" data-location="chamada" data-page="%s">%s</a>
          </div>
        </div>
      </div>
    </section>
""" % (e(d["tag"]), e(d["titulo"]), "".join("\n          <p>%s</p>" % x for x in d["ps"]), d["link"], slug, e(d["botao"]))


def s_hero(p):
    slug = p["slug"]
    return """    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><span>%s</span></nav>
          <div class="eyebrow">%s</div>
          <h1 class="page-title">%s</h1>
          <p class="page-subtitle">%s</p>%s
          <div class="page-actions">
            %s
            <a class="btn btn-outline" href="#orcamento" data-event="cta_click" data-location="hero_orcamento" data-page="%s">Quanto custa?</a>
          </div>
          <div class="pill-row">%s</div>
        </div>
        <aside class="page-hero-panel">
          <h2>%s</h2>
          <ul class="audit-list">%s
          </ul>
        </aside>
      </div>
    </section>
""" % (e(p["trilha"]), e(p["eyebrow"]), e(p["h1"]), e(p["sub"]), autor_data(p),
       cta(wa(p["msg"]), e(p["cta_hero"]), "hero", slug), slug,
       "".join('<span class="pill">%s</span>' % e(x) for x in p["pills"]),
       e(p["painel_h2"]), "".join("\n            <li>%s</li>" % e(x) for x in p["painel"]))


def s_split(d, slug):
    return """
    <section class="solution-section">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>%s
        </div>
        <div class="split-visual">
          <div class="visual-card">
            <div class="visual-card-title">%s</div>
            <ul class="visual-list">%s
            </ul>
          </div>
        </div>
      </div>
    </section>
""" % (e(d["tag"]), e(d["titulo"]), "".join("\n          <p>%s</p>" % x for x in d["ps"]),
       e(d["card_titulo"]), "".join("\n              <li>%s</li>" % x for x in d["card"]))


def s_texto(d, slug, alt):
    return """
    <section class="solution-section%s">
      <div class="container">
        <div class="split-copy" style="max-width:860px;margin:0 auto">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>%s
        </div>
      </div>
    </section>
""" % (" alt-bg" if alt else "", e(d["tag"]), e(d["titulo"]),
       "".join("\n          <p>%s</p>" % x for x in d["ps"]))


def grade(itens):
    # item = (titulo, texto) ou (titulo, texto, link) — com link, o titulo do cartao vira link (paginas-indice)
    def titulo(it):
        return '<a href="%s">%s</a>' % (it[2], e(it[0])) if len(it) > 2 else e(it[0])
    return "".join('\n          <article class="feature-card">\n            <h3>%s</h3>\n            <p>%s</p>\n'
                   '          </article>' % (titulo(it), it[1]) for it in itens)


def s_cards(d, slug):
    desc = '\n          <p class="section-desc">%s</p>' % e(d["desc"]) if d.get("desc") else ""
    return """
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>%s
        </div>
        <div class="cards-grid">%s
        </div>
      </div>
    </section>
""" % (e(d["tag"]), e(d["titulo"]), desc, grade(d["itens"]))


def s_faixas(d, slug):
    return """
    <section class="solution-section alt-bg">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Quanto custa</div>
          <h2 class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="cards-grid">%s
        </div>
      </div>
    </section>
""" % (e(d["titulo"]), d["desc"], grade(d["itens"]))


def s_orcamento(d, slug):
    cards = []
    for i, (nome, para, itens, msg, botao) in enumerate(d["itens"]):
        dest = i == d.get("destaque", -1)
        cards.append("""
          <article class="pacote-card%s">%s
            <h3 class="pacote-nome">%s</h3>
            <p class="pacote-para">%s</p>
            <p class="pacote-condicao">Valor sob medida para o tamanho do seu projeto</p>
            <ul class="pacote-lista">%s
            </ul>
            %s
          </article>
""" % (" destaque" if dest else "", '\n            <span class="pacote-selo">Mais pedido</span>' if dest else "",
       e(nome), e(para), "".join("\n              <li>%s</li>" % e(x) for x in itens),
       cta(wa(msg), e(botao), "orcamento_%d" % (i + 1), slug, "btn btn-primary btn-full")))
    duvida = ('<a href="%s" target="_blank" rel="noopener noreferrer" data-event="cta_click" '
              'data-location="orcamento_duvida" data-page="%s">Me chame no WhatsApp</a>'
              % (wa("Olá, Renan! Quero um orçamento, mas não sei por onde começar."), slug))
    return """
    <section class="pacotes-section" id="orcamento" aria-labelledby="orcamento-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Orçamento grátis</div>
          <h2 id="orcamento-titulo" class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="pacotes-grid">%s        </div>
        <p class="pacotes-nota"><strong>Não sabe por onde começar?</strong> %s. Eu olho o seu caso antes de você investir qualquer coisa e digo com franqueza o que faz sentido — inclusive se for o mais simples.</p>
      </div>
    </section>
""" % (e(d["titulo"]), e(d["desc"]), "".join(cards), duvida)


def s_passos(d, slug, msg):
    return """
    <section class="solution-section alt-bg">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Como funciona</div>
          <h2 class="section-title">%s</h2>
        </div>
        <ol class="steps-list">%s
        </ol>
        <div class="page-actions" style="justify-content:center;margin-top:2rem">
          %s
        </div>
      </div>
    </section>
""" % (e(d["titulo"]),
       "".join("\n          <li>\n            <h3>%s</h3>\n            <p>%s</p>\n          </li>" % (e(t), e(x))
               for t, x in d["itens"]),
       cta(wa(msg), "Pedir meu orçamento grátis", "passos", slug, "btn btn-whatsapp btn-lg"))


def s_faq(p):
    itens = "".join("""
          <details class="faq-item">
            <summary><h3>%s</h3></summary>
            <p>%s</p>
          </details>""" % (e(q), e(a)) for q, a in p["faq"])
    return """
    <section class="faq-section" aria-labelledby="faq-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Dúvidas</div>
          <h2 id="faq-titulo" class="section-title">%s</h2>
        </div>
        <div class="faq-list">%s
        </div>
      </div>
    </section>
""" % (e(p.get("faq_titulo") or "Perguntas frequentes sobre %s em Goiânia" % p["servico"].lower()), itens)


def s_relacionados(p):
    cards = "".join('\n          <a class="cluster-card" href="%s"><h3>%s</h3><p>%s</p></a>' % (h, e(t), e(x))
                    for h, t, x in p["relacionados"])
    return """
    <section class="cluster-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Leia também</div>
          <h2 class="section-title">Outros serviços que andam junto</h2>
        </div>
        <div class="cluster-grid">%s
        </div>
      </div>
    </section>
""" % cards


def s_cta_final(p):
    t, x = p["cta_final"]
    return """
    <section class="cta-band">
      <div class="container cta-band-inner">
        <h2>%s</h2>
        <p>%s</p>
        %s
      </div>
    </section>
""" % (e(t), e(x), cta(wa(p["msg"]), "Falar no WhatsApp", "cta_band", p["slug"], "btn btn-whatsapp btn-lg"))


def corpo(p):
    slug, partes, alt = p["slug"], [s_hero(p)], False
    for tipo, d in p["secoes"]:
        if tipo == "split":
            partes.append(s_split(d, slug))
        elif tipo == "texto":
            alt = not alt
            partes.append(s_texto(d, slug, alt))
        elif tipo == "cards":
            partes.append(s_cards(d, slug))
        elif tipo == "faixas":
            partes.append(s_faixas(d, slug))
        elif tipo == "orcamento":
            partes.append(s_orcamento(d, slug))
        elif tipo == "passos":
            partes.append(s_passos(d, slug, p["msg"]))
        elif tipo == "chamada":
            partes.append(s_chamada(d, slug))
        else:
            raise ValueError("tipo de seção desconhecido: %s" % tipo)
    partes += [s_faq(p), s_relacionados(p), s_cta_final(p)]
    return "".join(partes)


# ---------------------------------------------------------------- schema
def servico_no(p, url):
    n = {"@type": "Service", "@id": url + "#service", "name": p["trilha"], "serviceType": p["servico"],
         "description": p["desc"], "provider": {"@id": M.ID_EMPRESA},
         "areaServed": ([{"@type": "Country", "name": "Brasil"}] if p.get("nacional") else
                        [{"@type": "City", "name": "Goiânia", "addressRegion": "GO", "addressCountry": "BR"},
                         {"@type": "Country", "name": "Brasil"}])}
    if p.get("publico"):
        n["audience"] = {"@type": "BusinessAudience", "audienceType": p["publico"]}
    return n


def schema(p):
    url = "%s/%s/" % (BASE, p["slug"])
    hub = p.get("hub")  # pagina-indice (Etapa 10): CollectionPage com a lista de links, sem no Service
    g = [
        {"@type": "CollectionPage" if hub else "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"],
         "description": p["desc"],
         "dateModified": p.get("data", DATA), "inLanguage": "pt-BR",
         "isPartOf": M.site(),
         **({"author": {"@type": "Person", "@id": "https://rcbseo.com.br/#renan", "name": "Renan Carvalho Barbosa"},
             "datePublished": p.get("publicado", p["data"])} if p.get("data") else {}),
         "breadcrumb": {"@id": url + "#breadcrumb"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["trilha"], "item": url}]},
        ({"@type": "ItemList", "@id": url + "#lista", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": it[0], "url": BASE + it[2]}
            for i, it in enumerate(it for tipo, d in p["secoes"] if tipo == "cards"
                                   for it in d["itens"] if len(it) > 2)]}
         if hub else servico_no(p, url)),
        M.no_empresa(),
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------- montagem
def montar(modelo, p):
    slug, url = p["slug"], "%s/%s/" % (BASE, p["slug"])
    h = modelo

    def troca(padrao, novo):
        nonlocal h
        h2, k = re.subn(padrao, lambda _: novo, h, count=1, flags=re.S)
        assert k == 1, (slug, padrao, k)
        h = h2

    troca(r"<title>.*?</title>", "<title>%s</title>" % e(p["title"]))
    troca(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % e(p["desc"]))
    troca(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url)
    troca(r'<link rel="alternate" hreflang="pt-BR" href="[^"]*">', '<link rel="alternate" hreflang="pt-BR" href="%s">' % url)
    troca(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % e(p["title"]))
    troca(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % e(p["desc"]))
    troca(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url)
    troca(r'<meta name="twitter:title" content="[^"]*">', '<meta name="twitter:title" content="%s">' % e(p["title"]))
    troca(r'<meta name="twitter:description" content="[^"]*">', '<meta name="twitter:description" content="%s">' % e(p["desc"]))
    troca(r'<script type="application/ld\+json">.*?</script>',
          '<script type="application/ld+json">\n%s\n  </script>' % schema(p))
    troca(r'<main id="main-content">.*?</main>', '<main id="main-content">\n%s  </main>' % corpo(p))

    # barra do celular e botao flutuante: mensagem do servico desta pagina
    novo = wa(p["msg"])
    h, n1 = re.subn(r'(<div class="cta-mobile".*?<a href=")https://wa\.me/[^"]*(")',
                    lambda m: m.group(1) + novo + m.group(2), h, count=1, flags=re.S)
    h, n2 = re.subn(r'<a href="https://wa\.me/[^"]*"( class="whatsapp-float")',
                    lambda m: '<a href="%s"%s' % (novo, m.group(1)), h, count=1)
    assert n1 == 1 and n2 == 1, (slug, n1, n2)
    h = h.replace('aria-label="Pedir orçamento de site pelo WhatsApp"',
                  'aria-label="Pedir orçamento de %s pelo WhatsApp"' % e(p["servico"].lower()))
    return h.replace('data-page="%s"' % MODELO, 'data-page="%s"' % slug)


def main():
    modelo = io.open(os.path.join(RAIZ, MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    for p in PAGINAS:
        p = dict(p, title=M.titulo(p["title"]))
        h = montar(modelo, p)
        assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1, p["slug"]
        assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (p["slug"], len(p["title"]), len(p["desc"]))
        assert "R$ 1.997" not in h and '"price"' not in h and "priceRange" not in h, p["slug"]
        assert 'data-page="%s"' % MODELO not in h, p["slug"]  # medicao do GA4 nao pode herdar o modelo
        destino = os.path.join(RAIZ, p["slug"], "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        h = M.texto_html(h)
        io.open(destino, "w", encoding="utf-8", newline="\n").write(h)
        miolo = h.split('<main id="main-content">')[1].split("</main>")[0]
        print("ok  /%s/  %d palavras" % (p["slug"], len(re.sub(r"<[^>]+>", " ", miolo).split())))


if __name__ == "__main__":
    main()
