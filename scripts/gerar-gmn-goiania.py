# -*- coding: utf-8 -*-
"""
Gera /google-meu-negocio-goiania/ (auditoria de 09/11/2026, item 6).

Conteudo: scripts/conteudo/gmn_goiania.py (escrito a mao).
Involucro: as funcoes de secao do gerar-seo-para-ia.py, que por sua vez usam o montar() do
gerar-servicos-marketing.py (copia menu, rodape, barra do celular e cookies da pagina viva
/criacao-de-sites-goiania/). Este script troca so a trilha e o schema:
  * trilha: Inicio / Google Meu Negocio em Goiania
  * schema: WebPage + BreadcrumbList + Service (areaServed Goiania e regiao, provider #business)
            + a empresa + FAQPage
  * sitemap: insere a URL se faltar

Regras: SEM PRECO da RCB; nenhuma promessa de posicao. Idempotente.
    python scripts/gerar-gmn-goiania.py
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
S, M, rcb_copy = G.S, G.M, G.rcb_copy
sys.path.insert(0, os.path.join(AQUI, "conteudo"))
from gmn_goiania import PAGINAS, SLUG  # noqa: E402

G.PILAR = "/%s/" % SLUG  # a pagina e o proprio "pilar": trilha Inicio / Google Meu Negocio em Goiania

AREAS = [("City", "Goiânia"), ("City", "Aparecida de Goiânia"), ("City", "Senador Canedo"),
         ("City", "Trindade"), ("City", "Anápolis")]


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
    servico["areaServed"] = [{"@type": t, "name": n, "addressRegion": "GO", "addressCountry": "BR"}
                             for t, n in AREAS]
    servico["alternateName"] = ["Otimização de Google Meu Negócio em Goiânia",
                                "Perfil da Empresa no Google em Goiânia",
                                "Google Maps para empresas em Goiânia"]
    servico["isRelatedTo"] = {"@type": "Service", "name": "Google Meu Negócio (Brasil)",
                              "url": S.BASE + "/google-perfil-empresa/"}
    g = [pagina, {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": migalhas},
         servico, M.no_empresa(),
         {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
             {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
             for q, a in p["faq"]]}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def main():
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
        for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            json.loads(bloco)
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
