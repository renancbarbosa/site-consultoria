# -*- coding: utf-8 -*-
"""
Renderizador dos artigos do blog dos clusters novos.

Segue exatamente o template dos artigos já publicados (artigo-hero, artigo-header,
artigo-body, artigo-faq, artigo-voltar), com uma diferença: não repete o bloco
<style> inline de 4,4 KB que os artigos antigos carregam. Essas regras foram
consolidadas no styles.css em 06/08/2026.

Cada artigo é um dicionário; o corpo é HTML escrito à mão no módulo de conteúdo.
"""
from rcb_base import (
    BASE_URL, WHATS, head_comum, NAVBAR, rodape, grafo, schema_blogposting,
    schema_breadcrumb, schema_faq, tempo_leitura, contar_palavras, esc, whats_link,
)
from rcb_pacotes import bloco_cta_mobile, nav_ver_precos

MESES = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro")


def data_br(iso):
    a, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {a}"


def caixa(html):
    """Caixa de destaque dentro do corpo do artigo (resposta direta, alerta, resumo)."""
    return f'<div class="artigo-cta-box">{html}</div>'


def tabela(cabecalho, linhas, nota=""):
    th = "".join(f"<th>{c}</th>" for c in cabecalho)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in ln) + "</tr>" for ln in linhas)
    n = f'<p class="case-table-note">{nota}</p>' if nota else ""
    return (f'<div class="case-table-wrap"><table class="case-table">'
            f'<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}')


def link(href, texto):
    return f'<a class="artigo-link" href="{href}">{texto}</a>'


def render_artigo(a):
    """
    a = {
      slug, h1, title, desc, cat, data, atualizado (opcional),
      trilha_extra: (href, rotulo) | None,
      corpo: html,
      faq: [(pergunta, resposta_html)],
      cta: (paragrafo, href, rotulo_botao),
    }
    """
    slug = a["slug"]
    canonical = f"{BASE_URL}/blog/{slug}/"
    data_pub = a["data"]
    data_mod = a.get("atualizado", data_pub)

    trilha_schema = [("Início", f"{BASE_URL}/"), ("Blog", f"{BASE_URL}/blog/")]
    trilha_html = ('<a href="/">Início</a><span aria-hidden="true">/</span>'
                   '<a href="/blog/">Blog</a>')
    if a.get("trilha_extra"):
        href, rotulo = a["trilha_extra"]
        trilha_schema.append((rotulo, BASE_URL + href))
        trilha_html += f'<span aria-hidden="true">/</span><a href="{href}">{rotulo}</a>'
    trilha_schema.append((a["h1"], canonical))

    faq = a.get("faq", [])
    imagem = a.get("imagem")
    imagem_abs = BASE_URL + imagem["src"] if imagem else None
    schema = grafo(
        schema_blogposting(canonical, a["h1"], a["desc"], data_pub, data_mod,
                           imagem_abs or "https://rcbseo.com.br/assets/img/og-rcb-1200x628.png"),
        schema_breadcrumb(trilha_schema),
        schema_faq(faq) if faq else "",
    )

    corpo = a["corpo"]
    minutos = tempo_leitura(corpo)

    faq_html = ""
    if faq:
        itens = "\n".join(
            f'            <div class="artigo-faq-item">\n'
            f'              <h3>{q}</h3>\n'
            f'              <p>{r}</p>\n'
            f'            </div>' for q, r in faq
        )
        faq_html = f"""
        <section class="artigo-faq" aria-labelledby="faq-artigo-titulo">
          <h2 id="faq-artigo-titulo">Perguntas frequentes</h2>
          <div class="artigo-faq-list">
{itens}
          </div>
        </section>
"""

    cta_txt, cta_href, cta_label = a["cta"]
    if cta_href.startswith("http"):
        alvo = ' target="_blank" rel="noopener noreferrer"'
        svg = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
               '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')
    else:
        alvo = ""
        svg = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
               'stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>')

    cta_html = f"""
        <div class="artigo-cta-box">
          <p>{cta_txt}</p>
        </div>

        <div class="artigo-cta-wrap">
          <a href="{cta_href}" class="artigo-cta-btn"{alvo} data-event="cta_click" data-location="artigo_cta" data-page="artigo-{slug}" aria-label="{esc(cta_label)}">
            {svg}
            {cta_label}
          </a>
        </div>
"""

    head = head_comum(a["title"], a["desc"], canonical, schema, og_type="article")
    page_id = f"blog-{slug}"
    navbar = NAVBAR.replace(
        '<li><a href="/diagnostico-presenca-digital/" class="nav-link nav-cta">Diagnóstico gratuito</a></li>',
        nav_ver_precos(page_id, "/#pacotes"),
    )
    if imagem:
        capa = (f'<figure class="artigo-capa-media">'
                f'<img src="{imagem["src"]}" alt="{esc(imagem["alt"])}" '
                f'width="{imagem["width"]}" height="{imagem["height"]}" '
                f'fetchpriority="high" decoding="async">'
                f'<figcaption class="artigo-capa-caption">{imagem["legenda"]}</figcaption>'
                f'</figure>')
    else:
        capa = '<div class="artigo-capa-placeholder" aria-hidden="true"></div>'

    html = f"""{head}
<body class="tem-cta-mobile" data-page="artigo-{slug}">
{navbar}

  <main id="main-content">

    <section class="artigo-hero" aria-labelledby="artigo-h1">
      {capa}
      <div class="artigo-header">
        <nav class="artigo-breadcrumb" aria-label="Caminho do artigo">
          {trilha_html}
        </nav>
        <span class="artigo-cat">{a["cat"]}</span>
        <h1 id="artigo-h1">{a["h1"]}</h1>
        <div class="article-byline">
          <span class="byline-author">Por <a href="/sobre/">Renan Carvalho Barbosa</a></span>
          <span class="byline-separator" aria-hidden="true">·</span>
          <time datetime="{data_pub}" class="byline-date">{data_br(data_pub)}</time>
          <span class="byline-separator" aria-hidden="true">·</span>
          <span class="byline-reading-time">{minutos} min de leitura</span>
        </div>
      </div>
    </section>

    <article class="artigo-body">
      <div class="artigo-container">
{corpo}
{cta_html}{faq_html}
      </div>

      <div class="artigo-voltar">
        <a href="/blog/">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Voltar ao blog
        </a>
      </div>
    </article>

  </main>

{rodape(bloco_cta_mobile(page_id, "/#pacotes"))}"""

    return f"blog/{slug}/index.html", html
