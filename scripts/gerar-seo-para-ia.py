# -*- coding: utf-8 -*-
"""
Gera o 5º pilar, SEO para IA (28/10/2026):

  /seo-para-ia/  /como-aparecer-no-chatgpt/  /ai-overviews-e-gemini/
  /o-que-e-geo-e-aeo/  /auditoria-de-seo-para-ia/

Conteúdo: scripts/conteudo/seo_para_ia.py (escrito à mão).
Esqueleto: o mesmo montar() do gerar-servicos-marketing.py (copia menu, rodapé, barra do
celular e cookies da página viva /criacao-de-sites-goiania/). Este script só acrescenta:
  * trilha de navegação com o pilar no meio (Início / SEO para IA / página)
  * seções "tabela" (estilo .bench-tabela, já no styles.css) e "fontes"
  * schema Article nos satélites ("tipo": "artigo") e Service nas páginas comerciais
  * as URLs no sitemap.xml (insere se faltar; atualiza o lastmod se já existir)

Regras: SEM PREÇO da RCB; sem selo "Mais pedido"; nenhum resultado prometido.
Idempotente: rodar duas vezes seguidas não muda nada na segunda.
"""
import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("servicos", os.path.join(AQUI, "gerar-servicos-marketing.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)
M, rcb_copy, e, wa, cta = S.M, S.rcb_copy, S.e, S.wa, S.cta
sys.path.insert(0, os.path.join(AQUI, "conteudo"))
from seo_para_ia import PAGINAS, PILAR  # noqa: E402

PILAR_NOME = "SEO para IA"


def trilha(p):
    """Lista (nome, caminho) da trilha de navegação, sem o Início."""
    if "/%s/" % p["slug"] == PILAR:
        return [(p["trilha"], PILAR)]
    return [(PILAR_NOME, PILAR), (p["trilha"], "/%s/" % p["slug"])]


def s_hero(p):
    slug = p["slug"]
    passos = trilha(p)
    migalhas = "".join('<span>/</span><a href="%s">%s</a>' % (h, e(n)) for n, h in passos[:-1])
    migalhas += "<span>/</span><span>%s</span>" % e(passos[-1][0])
    href2, txt2 = p["botao2"]
    return """    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a>%s</nav>
          <div class="eyebrow">%s</div>
          <h1 class="page-title">%s</h1>
          <p class="page-subtitle">%s</p>%s
          <div class="page-actions">
            %s
            <a class="btn btn-outline" href="%s" data-event="cta_click" data-location="hero_secundario" data-page="%s">%s</a>
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
""" % (migalhas, e(p["eyebrow"]), e(p["h1"]), e(p["sub"]), S.autor_data(p),
       cta(S.wa(p["msg"]), e(p["cta_hero"]), "hero", slug), href2, slug, e(txt2),
       "".join('<span class="pill">%s</span>' % e(x) for x in p["pills"]),
       e(p["painel_h2"]), "".join("\n            <li>%s</li>" % e(x) for x in p["painel"]))


def s_tabela(d):
    desc = '\n          <p class="section-desc">%s</p>' % e(d["desc"]) if d.get("desc") else ""
    cab = "".join('<th scope="col">%s</th>' % e(c) for c in d["colunas"])
    linhas = "".join("\n              <tr>%s</tr>" % "".join(
        ('<th scope="row">%s</th>' % e(c)) if i == 0 else "<td>%s</td>" % e(c) for i, c in enumerate(lin))
        for lin in d["linhas"])
    nota = "\n            <caption>%s</caption>" % e(d["nota"]) if d.get("nota") else ""
    return """
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>%s
        </div>
        <div class="bench-tabela-wrap" style="max-width:960px;margin:0 auto">
          <table class="bench-tabela">%s
            <thead><tr>%s</tr></thead>
            <tbody>%s
            </tbody>
          </table>
        </div>
      </div>
    </section>
""" % (e(d["tag"]), e(d["titulo"]), desc, nota, cab, linhas)


def s_fontes(d):
    itens = "".join('\n            <li><a href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>' % (u, e(t))
                    for t, u in d["itens"])
    return """
    <section class="solution-section">
      <div class="container">
        <div class="split-copy" style="max-width:860px;margin:0 auto">
          <div class="section-tag">Fontes</div>
          <h2 class="section-title">De onde vêm as informações desta página</h2>
          <p>Tudo o que esta página afirma sobre como as IAs funcionam vem da documentação oficial de quem as faz:</p>
          <ul class="visual-list">%s
          </ul>
        </div>
      </div>
    </section>
""" % itens


def s_relacionados(p):
    cards = "".join('\n          <a class="cluster-card" href="%s"><h3>%s</h3><p>%s</p></a>' % (h, e(t), e(x))
                    for h, t, x in p["relacionados"])
    return """
    <section class="cluster-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Leia também</div>
          <h2 class="section-title">%s</h2>
        </div>
        <div class="cluster-grid">%s
        </div>
      </div>
    </section>
""" % (e(p["relacionados_titulo"]), cards)


def corpo(p):
    slug, partes, alt = p["slug"], [s_hero(p)], False
    for tipo, d in p["secoes"]:
        if tipo == "tabela":
            partes.append(s_tabela(d))
        elif tipo == "fontes":
            partes.append(s_fontes(d))
        elif tipo == "texto":
            alt = not alt
            partes.append(S.s_texto(d, slug, alt))
        elif tipo == "split":
            partes.append(S.s_split(d, slug))
        elif tipo == "cards":
            partes.append(S.s_cards(d, slug))
        elif tipo == "orcamento":
            partes.append(S.s_orcamento(d, slug))
        elif tipo == "passos":
            partes.append(S.s_passos(d, slug, p["msg"]))
        else:
            raise ValueError("tipo de seção desconhecido: %s" % tipo)
    return "".join(partes + [S.s_faq(p), s_relacionados(p), S.s_cta_final(p)])


def schema(p):
    url = "%s/%s/" % (S.BASE, p["slug"])
    autor = {"@type": "Person", "@id": "https://rcbseo.com.br/#renan", "name": "Renan Carvalho Barbosa"}
    pagina = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"],
              "description": p["desc"], "inLanguage": "pt-BR", "isPartOf": M.site(),
              "datePublished": p["data"], "dateModified": p["data"], "author": autor,
              "breadcrumb": {"@id": url + "#breadcrumb"}}
    migalhas = [{"@type": "ListItem", "position": 1, "name": "Início", "item": S.BASE + "/"}]
    migalhas += [{"@type": "ListItem", "position": i + 2, "name": n, "item": S.BASE + h}
                 for i, (n, h) in enumerate(trilha(p))]
    g = [pagina, {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": migalhas}]
    if p["tipo"] == "artigo":
        g.append({"@type": "Article", "@id": url + "#artigo", "headline": p["h1"], "description": p["desc"],
                  "inLanguage": "pt-BR", "mainEntityOfPage": {"@id": url + "#webpage"},
                  "author": autor, "publisher": {"@id": M.ID_EMPRESA},
                  "datePublished": p["data"], "dateModified": p["data"],
                  "about": {"@type": "Thing", "name": "SEO para IA (GEO e AEO)"},
                  "citation": [u for _, d in p["secoes"] if _ == "fontes" for _t, u in d["itens"]]})
    else:
        n = S.servico_no(p, url)
        n["alternateName"] = ["GEO", "AEO", "Otimização para IA generativa"]
        g.append(n)
    g.append(M.no_empresa())
    g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def sitemap(paginas):
    caminho = os.path.join(S.RAIZ, "sitemap.xml")
    sm = io.open(caminho, encoding="utf-8").read()
    original = sm
    for p in paginas:
        loc = "%s/%s/" % (S.BASE, p["slug"])
        bloco = re.search(r"<url>\s*<loc>%s</loc>.*?</url>" % re.escape(loc), sm, re.S)
        if bloco:
            novo = re.sub(r"<lastmod>[^<]*</lastmod>", "<lastmod>%s</lastmod>" % p["data"], bloco.group(0))
            sm = sm[:bloco.start()] + novo + sm[bloco.end():]
        else:
            sm = sm.replace("</urlset>", "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                            "    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>\n</urlset>"
                            % (loc, p["data"], "0.9" if p["tipo"] == "servico" else "0.7"))
    if sm != original:
        io.open(caminho, "w", encoding="utf-8", newline="\n").write(sm)
    return sm.count("<loc>")


def main():
    S.schema, S.corpo = schema, corpo  # montar() do gerador de serviços chama estes dois
    modelo = io.open(os.path.join(S.RAIZ, S.MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    alteradas = 0
    for p in PAGINAS:
        p = dict(p, title=M.titulo(p["title"]))
        slug = p["slug"]
        assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (slug, len(p["title"]), len(p["desc"]))
        h = S.montar(modelo, p)
        tem_orcamento = any(t == "orcamento" for t, _ in p["secoes"])
        if not tem_orcamento:  # menu e barra do celular herdam "#orcamento" do modelo: mandam para o pilar
            h = h.replace('href="#orcamento"', 'href="%s#orcamento"' % PILAR)
        h = rcb_copy.humanizar(M.texto_html(h))
        assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1, slug
        assert "R$" not in h and '"price"' not in h and "priceRange" not in h, slug
        assert "Mais pedido" not in h, slug  # serviço novo: selo seria falso
        assert 'data-page="%s"' % S.MODELO not in h, slug
        assert tem_orcamento or 'href="#orcamento"' not in h, slug
        for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            json.loads(bloco)
        destino = os.path.join(S.RAIZ, slug, "index.html")
        antes = io.open(destino, encoding="utf-8").read() if os.path.exists(destino) else None
        if antes != h:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            io.open(destino, "w", encoding="utf-8", newline="\n").write(h)
            alteradas += 1
        miolo = h.split('<main id="main-content">')[1].split("</main>")[0]
        print("ok  /%s/  %d palavras" % (slug, len(re.sub(r"<[^>]+>", " ", miolo).split())))
    print("páginas alteradas: %d" % alteradas)
    print("sitemap: %d URLs" % sitemap(PAGINAS))


if __name__ == "__main__":
    main()
