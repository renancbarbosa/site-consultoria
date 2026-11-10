# -*- coding: utf-8 -*-
"""
Gera as 2 paginas da pesquisa de palavras-chave de 10/11/2026:
  /agencia-de-marketing-digital-goiania/   e   /landing-page-para-advogados/

Conteudo: scripts/conteudo/pesquisa_2026_11_10.py (escrito a mao).
Involucro: o mesmo de /google-meu-negocio-goiania/ (funcoes de secao do gerar-seo-para-ia.py,
que usam o montar() do gerar-servicos-marketing.py: menu, rodape, barra do celular e cookies
copiados da pagina viva /criacao-de-sites-goiania/).

O que este script troca em relacao ao modelo:
  * trilha: Inicio / <pagina>
  * tabela: aceita link dentro da celula (o s_tabela original escapa tudo)
  * fontes: frase de abertura neutra (a original fala de IA)
  * schema: WebPage + BreadcrumbList + Service (com alternateName das variacoes buscadas)
            + a empresa + FAQPage
  * sitemap: insere a URL se faltar

Regras: SEM PRECO da RCB; nenhuma promessa de posicao. Idempotente.
    python scripts/gerar-paginas-2026-11-10.py
"""
import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("seo_ia", os.path.join(AQUI, "gerar-seo-para-ia.py"))
G = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G)
S, M, rcb_copy, e = G.S, G.M, G.rcb_copy, G.e
sys.path.insert(0, os.path.join(AQUI, "conteudo"))
from pesquisa_2026_11_10 import PAGINAS  # noqa: E402

AREAS_GYN = ["Goiânia", "Aparecida de Goiânia", "Senador Canedo", "Trindade", "Anápolis"]


def trilha(p):
    return [(p["trilha"], "/%s/" % p["slug"])]


def _cel(c):
    return c if "<a " in c else e(c)


def s_tabela(d):
    desc = '\n          <p class="section-desc">%s</p>' % e(d["desc"]) if d.get("desc") else ""
    cab = "".join('<th scope="col">%s</th>' % e(c) for c in d["colunas"])
    linhas = "".join("\n              <tr>%s</tr>" % "".join(
        ('<th scope="row">%s</th>' % _cel(c)) if i == 0 else "<td>%s</td>" % _cel(c) for i, c in enumerate(lin))
        for lin in d["linhas"])
    nota = "\n            <caption>%s</caption>" % _cel(d["nota"]) if d.get("nota") else ""
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
          <p>O que esta página afirma sobre regras e funcionamento vem das fontes oficiais:</p>
          <ul class="visual-list">%s
          </ul>
        </div>
      </div>
    </section>
""" % itens


def schema(p):
    url = "%s/%s/" % (S.BASE, p["slug"])
    autor = {"@type": "Person", "@id": "https://rcbseo.com.br/#renan", "name": "Renan Carvalho Barbosa"}
    pagina = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"],
              "description": p["desc"], "inLanguage": "pt-BR", "isPartOf": M.site(),
              "datePublished": p["data"], "dateModified": p["data"], "author": autor,
              "about": {"@id": url + "#service"},
              "breadcrumb": {"@id": url + "#breadcrumb"}}
    migalhas = [{"@type": "ListItem", "position": 1, "name": "Início", "item": S.BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": p["trilha"], "item": url}]
    servico = S.servico_no(p, url)
    if not p.get("nacional"):
        servico["areaServed"] = [{"@type": "City", "name": n, "addressRegion": "GO", "addressCountry": "BR"}
                                 for n in AREAS_GYN]
    servico["alternateName"] = p["alternativos"]
    g = [pagina, {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": migalhas},
         servico, M.no_empresa(),
         {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
             {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
             for q, a in p["faq"]]}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def main():
    G.trilha, G.s_tabela, G.s_fontes = trilha, s_tabela, s_fontes
    S.schema, S.corpo = schema, G.corpo  # montar() chama estes dois
    modelo = io.open(os.path.join(S.RAIZ, S.MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    alteradas = 0
    for p in PAGINAS:
        p = dict(p, title=M.titulo(p["title"]))
        slug = p["slug"]
        assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (slug, len(p["title"]), len(p["desc"]))
        h = S.montar(modelo, p)
        h = rcb_copy.humanizar(M.texto_html(h))
        assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1, slug
        assert "R$" not in h and '"price"' not in h and "priceRange" not in h, slug
        assert "Mais pedido" not in h, slug
        assert 'data-page="%s"' % S.MODELO not in h, slug
        assert "<!--RCB:LOCAL-FOOTER-->" in h, "rodape local sumiu do modelo"
        assert "&lt;a " not in h, "link escapado em " + slug
        for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            json.loads(bloco)
        for href in set(re.findall(r'href="(/[^"#?]*)"', h)):
            alvo = os.path.join(S.RAIZ, href.strip("/"), "index.html") if href.endswith("/") else os.path.join(S.RAIZ, href.strip("/"))
            if href.strip("/") in [q["slug"] for q in PAGINAS]:
                continue
            assert os.path.exists(alvo), ("link interno quebrado", slug, href)
        destino = os.path.join(S.RAIZ, slug, "index.html")
        antes = io.open(destino, encoding="utf-8").read() if os.path.exists(destino) else None
        if antes != h:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            io.open(destino, "w", encoding="utf-8", newline="\n").write(h)
            alteradas += 1
        miolo = h.split('<main id="main-content">')[1].split("</main>")[0]
        print("ok  /%s/  %d palavras  title=%d desc=%d" % (slug, len(re.sub(r"<[^>]+>", " ", miolo).split()),
                                                          len(p["title"]), len(p["desc"])))
    print("páginas alteradas: %d" % alteradas)
    print("sitemap: %d URLs" % G.sitemap(PAGINAS))


if __name__ == "__main__":
    main()
