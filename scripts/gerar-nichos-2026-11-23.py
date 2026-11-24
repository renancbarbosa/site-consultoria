# -*- coding: utf-8 -*-
"""
Gera os 5 nichos de 23/11/2026: 5 páginas principais + 5 artigos de apoio. Idempotente.

  Páginas : scripts/conteudo/nichos_2026_11_paginas.py  (montadas pelo montar() do
            gerar-servicos-marketing.py, que copia menu, rodapé, barra do celular e cookies
            da página viva /criacao-de-sites-goiania/)
  Artigos : scripts/conteudo/nichos_2026_11_artigos.py  (render_artigo + o mesmo acabamento
            que os artigos de outubro receberam depois: menu atual, rodapé do artigo vivo do
            guincho e sameAs da empresa no publisher)

Por que um gerador próprio: gerar-servicos-marketing.py e gerar-artigos-sites.py regravam
TODAS as páginas deles, e várias foram alteradas depois por outros scripts.

Também cuida, de forma idempotente, de: a página-índice /nichos/ (cartões novos vêm de
servicos_marketing.py), sitemap.xml, cartões no blog/index.html (seção "Nichos e tipos de
negócio") e entradas no llms.txt / llms-full.txt.

Rodar de novo NÃO apaga as caixas e os links que os scripts de ligação puseram depois: a página só
é regravada se o texto dos módulos de conteúdo mudou (ver gravar_gerada).

Uso:
    python scripts/gerar-nichos-2026-11-23.py          # gera e grava
    python scripts/gerar-nichos-2026-11-23.py --teste  # só confere o caminho de montagem:
        remonta a página e o artigo do guincho (outubro) e exige que saiam iguais aos do ar,
        fora as caixas que outros scripts põem depois.

Depois de gerar, rode (nessa ordem): ligar-nichos-2026-11-23.py (menu + caixas), ligar-pesquisa-2026-11-10.py,
cases-nichos-2026-11-21.py, ligar-leigas-2026-11-21.py e conferir-conversao.py. O --teste só passa
com o menu já atualizado (ligar-nichos), porque o artigo é montado com o rcb_menu atual.
"""
import difflib
import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))


def _modulo(nome, arquivo):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arquivo))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S = _modulo("servicos", "gerar-servicos-marketing.py")
A = _modulo("artigos_sites", "gerar-artigos-sites.py")
import rcb_copy  # noqa: E402
import rcb_marca as M  # noqa: E402
import rcb_menu  # noqa: E402
from rcb_base import contar_palavras  # noqa: E402
from rcb_artigo import render_artigo, data_br  # noqa: E402
from nichos_2026_11_paginas import PAGINAS  # noqa: E402
from nichos_2026_11_artigos import ARTIGOS  # noqa: E402

BASE = "https://rcbseo.com.br"
MODELO_ARTIGO = "blog/como-conseguir-clientes-para-guincho/index.html"
RODAPE = re.compile(r'<footer class="footer" role="contentinfo">.*?</footer>', re.S)
SAMEAS = list(M.MARCA["sameAs"]) + ([M.MARCA["linkedin_empresa"]] if M.MARCA.get("linkedin_empresa") else [])
NOVOS = {p["slug"] for p in PAGINAS} | {"blog/" + a["slug"] for a in ARTIGOS}

# cartão do índice do blog: (título curto da capa, descrição curta)
CARTOES = {
    "como-atrair-clientes-para-salao-de-beleza": (
        "Como atrair clientes para salão de beleza",
        "Fotos reais, serviços no Google, botão de agendar, avaliações e a cliente que volta no tempo certo."),
    "como-atrair-clientes-para-oficina-mecanica": (
        "Como atrair clientes para oficina mecânica",
        "Orçamento por escrito, peça trocada à vista, avaliações na entrega, revisão e frotas."),
    "como-atrair-clientes-para-loja": (
        "Como atrair clientes para loja",
        "Produtos no Google, vitrine, horário de feriado, datas que vendem e lista de clientes."),
    "landing-page-para-construtora": (
        "Landing page para construtora",
        "O que a página de cada empreendimento precisa ter, do topo ao registro da incorporação."),
    "google-ads-para-arquitetos": (
        "Google Ads para arquitetos",
        "Que buscas anunciar, quais bloquear, a página certa e o que o CAU exige na divulgação."),
}

# llms.txt: (título da seção, página, artigo, abertura, resumo da página, resumo do artigo)
LLMS = [
    ("Salão de beleza e barbearia", "marketing-para-salao-de-beleza", "como-atrair-clientes-para-salao-de-beleza",
     "Marketing para salões de beleza, barbearias e esmalterias (o público é o dono do salão, não a cliente). "
     "Escrito com base na Lei 12.592/2012, que reconhece as profissões do setor e exige esterilização de "
     "materiais (art. 4º).",
     "perfil no Google Maps com fotos e botão de agendar, avaliações, site com serviços e equipe e anúncio só no "
     "raio do salão.",
     "10 caminhos: fotos reais, serviços no Google, agendamento, avaliações, a cliente que volta e parcerias no "
     "bairro."),
    ("Oficina mecânica", "marketing-para-oficina-mecanica", "como-atrair-clientes-para-oficina-mecanica",
     "Marketing para oficinas mecânicas e auto centers (o público é o dono da oficina, não o motorista). Escrito "
     "com base no Código de Defesa do Consumidor: orçamento prévio (art. 40), serviço sem orçamento como prática "
     "abusiva (art. 39, VI) e peças de reposição (art. 21).",
     "perfil no Google Maps com serviços e fotos de dentro, orçamento por escrito, site por serviço, página para "
     "frotas e anúncio no raio da oficina.",
     "confiança antes do orçamento: fotos de dentro, peça trocada à vista, avaliações na entrega, lembrete de "
     "revisão, frotas e parcerias."),
    ("Lojas", "marketing-para-loja", "como-atrair-clientes-para-loja",
     "Marketing para lojas de rua, lojas de bairro e lojas com venda online (o público é o dono da loja).",
     "perfil no Google Maps com produtos, horário especial, site ou loja virtual e anúncio nas datas que vendem.",
     "10 ideias: produtos no Google, vitrine, horário de feriado, datas comemorativas, eventos, lista de clientes "
     "e promoção dentro do Código de Defesa do Consumidor."),
    ("Construtoras e incorporadoras", "marketing-para-construtoras", "landing-page-para-construtora",
     "Marketing para construtoras e incorporadoras (o público é a construtora, não o comprador). Escrito com base "
     "na Lei 4.591/1964, que exige o número do registro da incorporação nos anúncios (art. 32, § 3º).",
     "landing page por empreendimento, anúncio no Google por bairro e tipo de imóvel, site com obras entregues e "
     "contato direto ao corretor.",
     "o que a página de cada empreendimento precisa ter: topo, plantas, registro da incorporação, formulário e "
     "contato rápido."),
    ("Arquitetura", "marketing-para-arquitetos", "google-ads-para-arquitetos",
     "Marketing para arquitetos e escritórios de arquitetura (o público é o arquiteto). Escrito com base na "
     "Resolução CAU/BR 75/2014 (divulgação com responsável técnico, título e registro) e no Código de Ética do "
     "CAU/BR (proibição da reserva técnica).",
     "site com portfólio, página por serviço, perfil do escritório no Google Maps e anúncio dentro das regras "
     "do CAU.",
     "quando vale anunciar, que buscas anunciar e bloquear, a página certa e o que o CAU exige."),
]

LLMS_FULL_ANTES = "* **Comércio:** pequenas empresas e comércios locais."
LLMS_FULL_DEPOIS = (
    "* **Comércio:** pequenas empresas, comércios locais e lojas.\n"
    "* **Beleza:** salões de beleza e barbearias (Lei 12.592/2012).\n"
    "* **Automotivo:** oficinas mecânicas (orçamento prévio do art. 40 do Código de Defesa do Consumidor).\n"
    "* **Construção:** construtoras e incorporadoras (registro da incorporação, Lei 4.591/1964) e arquitetos "
    "(Resolução CAU/BR 75/2014).")


def ler(rel):
    return io.open(os.path.join(RAIZ, rel), encoding="utf-8", newline="").read()


def gravar(rel, texto):
    caminho = os.path.join(RAIZ, rel)
    antes = io.open(caminho, encoding="utf-8", newline="").read() if os.path.exists(caminho) else None
    if antes == texto:
        return False
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    io.open(caminho, "w", encoding="utf-8", newline="").write(texto)
    return True


def gravar_gerada(rel, h):
    """Grava a página gerada, a não ser que a do disco só difira pelo que os scripts de ligação puseram
    depois (caixas e links no texto). Assim, rodar o gerador de novo não apaga essas ligações; só um
    texto novo nos módulos de conteúdo regrava a página (e aí é preciso rodar as ligações de novo)."""
    if os.path.exists(os.path.join(RAIZ, rel)) and _normaliza(ler(rel)) == _normaliza(h):
        return False
    return gravar(rel, h)


# ------------------------------------------------------------------ montagem
def montar_pagina(modelo, p):
    p = dict(p, title=M.titulo(p["title"]))
    assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (p["slug"], len(p["title"]), len(p["desc"]))
    return rcb_copy.humanizar(M.texto_html(S.montar(modelo, p)))


def montar_artigo(a, rodape_modelo):
    assert len(a["title"]) <= 65 and len(a["desc"]) <= 160, (a["slug"], len(a["title"]), len(a["desc"]))
    caminho, h = render_artigo(a)
    h = A.remover_navegacao_ainda_nao_publicada(h)
    h = rcb_copy.humanizar(rcb_menu.aplicar(M.texto_html(h)))  # o mesmo que rcb_base.escrever() faz
    rodapes = RODAPE.findall(h)
    assert len(rodapes) == 1, (a["slug"], "rodapé")
    h = h.replace(rodapes[0], rodape_modelo)  # rodapé dos artigos vivos (com o YouTube)
    h, n = re.subn(r'("@id":"https://rcbseo\.com\.br/#business","name":"RCB SEO","url":"https://rcbseo\.com\.br/")\}',
                   lambda m: m.group(1) + ',"sameAs":' + json.dumps(SAMEAS, ensure_ascii=False, separators=(",", ":")) + "}",
                   h)
    assert n >= 1, (a["slug"], "publisher sem sameAs")
    return caminho.replace("\\", "/"), h


def conferir(rel, h):
    assert h.startswith("<!DOCTYPE"), rel
    assert h.count("<h1") == 1, (rel, "h1")
    assert "R$" not in h and '"price"' not in h and "priceRange" not in h, (rel, "preço")
    assert 'data-page="%s"' % S.MODELO not in h, (rel, "GA4 herdou o modelo")
    assert "&lt;a " not in h, (rel, "link escapado")
    assert "<!--RCB:LOCAL-FOOTER-->" in h, (rel, "rodapé local")
    for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        json.loads(bloco)
    for href in set(re.findall(r'href="(/[^"#?]*)"', h)):
        alvo = href.strip("/")
        if alvo in NOVOS:
            continue
        caminho = os.path.join(RAIZ, alvo, "index.html") if href.endswith("/") else os.path.join(RAIZ, alvo)
        assert os.path.exists(caminho), (rel, "link interno quebrado", href)
    miolo = h.split('<main id="main-content">')[1].split("</main>")[0] if '<main id="main-content">' in h else h
    texto = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", miolo, flags=re.S))
    assert "—" not in texto and "–" not in texto, (rel, "travessão no texto")
    return len(texto.split())


# ------------------------------------------------------------------ integração
def sitemap():
    sm = ler("sitemap.xml")
    original = sm
    nl = "\r\n" if "\r\n" in sm else "\n"
    itens = ([(p["slug"], p["data"], "0.8") for p in PAGINAS]
             + [("blog/" + a["slug"], a["data"], "0.75") for a in ARTIGOS])
    for slug, data, prioridade in itens:
        loc = "%s/%s/" % (BASE, slug)
        if "<loc>%s</loc>" % loc in sm:
            continue
        bloco = nl.join(["  <url>", "    <loc>%s</loc>" % loc, "    <lastmod>%s</lastmod>" % data,
                         "    <changefreq>monthly</changefreq>", "    <priority>%s</priority>" % prioridade,
                         "  </url>", "</urlset>"])
        sm = sm.replace("</urlset>", bloco, 1)
    gravar("sitemap.xml", sm)
    return sm.count("<loc>"), sm != original


def cartao(a):
    capa, desc = CARTOES[a["slug"]]
    return """            <a href="/blog/%s/" class="blog-card" aria-label="Ler artigo: %s">
                        <div class="blog-card-thumb" aria-hidden="true">
                          <span class="blog-card-thumb-title">%s</span>
                        </div>
                        <div class="blog-card-body">
                          <span class="blog-card-cat">%s</span>
                          <h2 class="blog-card-title">%s</h2>
                          <p class="blog-card-desc">%s</p>
                          <div class="blog-card-meta">
                            <time datetime="%s">%s</time>
                            <span class="blog-card-link">
                              Ler artigo
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </span>
                          </div>
                        </div>
                      </a>
""" % (a["slug"], S.e(a["h1"]), S.e(capa), S.e(a["cat"]), S.e(a["h1"]), S.e(desc), a["data"], data_br(a["data"]))


def blog_index():
    h = ler("blog/index.html")
    faltam = [a for a in ARTIGOS if 'href="/blog/%s/" class="blog-card"' % a["slug"] not in h]
    if not faltam:
        return 0
    nl = "\r\n" if "\r\n" in h else "\n"
    m = re.search(r'<div class="blog-cluster" id="nichos">.*?<div class="blog-grid">\r?\n', h, re.S)
    assert m, "seção de nichos do blog não encontrada"
    h = h[:m.end()] + "".join(cartao(a) for a in faltam).replace("\n", nl) + h[m.end():]
    gravar("blog/index.html", h)
    return len(faltam)


def llms():
    mudou = []
    t = ler("llms.txt")
    if "%s/marketing-para-salao-de-beleza/" % BASE not in t:
        nl = "\r\n" if "\r\n" in t else "\n"
        bloco = ""
        for titulo, pag, art, abertura, r_pag, r_art in LLMS:
            p = [x for x in PAGINAS if x["slug"] == pag][0]
            bloco += nl.join([
                "## " + titulo, abertura,
                "- %s (página principal): %s/%s/. %s" % (p["trilha"], BASE, pag, r_pag[0].upper() + r_pag[1:]),
                "- %s: %s/blog/%s/. %s" % (CARTOES[art][0], BASE, art, r_art[0].upper() + r_art[1:]),
            ]) + nl + nl
        assert (nl + "## Conteúdo" + nl) in t, "llms.txt sem a seção Conteúdo"
        t = t.replace(nl + "## Conteúdo" + nl, nl + bloco + "## Conteúdo" + nl, 1)
        gravar("llms.txt", t)
        mudou.append("llms.txt")
    f = ler("llms-full.txt")
    if LLMS_FULL_ANTES in f:
        nl = "\r\n" if "\r\n" in f else "\n"
        f = f.replace(LLMS_FULL_ANTES, LLMS_FULL_DEPOIS.replace("\n", nl), 1)
        gravar("llms-full.txt", f)
        mudou.append("llms-full.txt")
    return mudou


def hub(modelo):
    """Regera só /nichos/ (cartões novos vêm de servicos_marketing.py) e devolve, no mesmo lugar,
    a caixa RCB:REFORCO que o reforco-links-2026-11-09.py tinha posto antes do FAQ."""
    p = [x for x in S.PAGINAS if x["slug"] == "nichos"][0]
    vivo = ler("nichos/index.html")
    novo = montar_pagina(modelo, p)
    ancora = '<section class="faq-section"'
    for bloco in re.findall(r'<!--RCB:REFORCO-->.*?<!--/RCB:REFORCO-->\r?\n', vivo, re.S):
        assert novo.count(ancora) == 1, "FAQ do /nichos/"
        novo = novo.replace(ancora, bloco.replace("\r\n", "\n") + ancora, 1)
    for x in [q for q in PAGINAS]:
        assert 'href="/%s/"' % x["slug"] in novo, ("/nichos/ sem o cartão", x["slug"])
    conferir("nichos/index.html", novo)
    if _normaliza(vivo) == _normaliza(novo):
        return False
    gravar("nichos/index.html", novo)
    sm = ler("sitemap.xml")  # data de atualização do índice no sitemap
    sm2 = re.sub(r"(<loc>%s/nichos/</loc>\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(BASE),
                 lambda m: m.group(1) + p["data"] + m.group(2), sm)
    gravar("sitemap.xml", sm2)
    return True


# ------------------------------------------------------------------ teste do caminho
# o que os scripts de ligação põem DEPOIS do gerador (caixas e links no texto) fica fora da comparação
_DEPOIS = re.compile(r'<!--RCB:(PESQUISA-1110|NICHOS-1123)-->.*?<!--/RCB:\1-->'
                     r'|<!-- RCB:CASE-NICHO -->.*?<!-- /RCB:CASE-NICHO -->', re.S)
_LEIGAS = re.compile(r'<a href="(?:/como-aparecer-no-google/|/blog/por-que-minha-empresa-nao-aparece-no-google/'
                     r'|/como-aparecer-no-chatgpt/)">(.*?)</a>', re.S)  # links do ligar-leigas-2026-11-21.py


def _normaliza(h):
    h = _LEIGAS.sub(r"\1", _DEPOIS.sub("", h))
    h = re.sub(r'"alternateName": \[\s*"RCB Consultoria"\s*\]', '"alternateName": ["RCB Consultoria"]', h)
    return [x.strip() for x in h.splitlines() if x.strip()]


def teste(modelo, rodape_modelo):
    """Remonta a página e o artigo do guincho (outubro) e compara com o que está no ar."""
    from servicos_marketing import PAGINAS as GERAIS
    from artigos_nichos_anuncios import ARTIGOS as OUTUBRO
    casos = [("marketing-para-empresa-de-guincho/index.html",
              montar_pagina(modelo, [p for p in GERAIS if p["slug"] == "marketing-para-empresa-de-guincho"][0])),
             (MODELO_ARTIGO,
              montar_artigo([a for a in OUTUBRO if a["slug"] == "como-conseguir-clientes-para-guincho"][0],
                            rodape_modelo)[1])]
    falhou = False
    for rel, gerado in casos:
        dif = [x for x in difflib.unified_diff(_normaliza(ler(rel)), _normaliza(gerado), lineterm="", n=0)
               if x[:1] in "+-" and not x.startswith(("+++", "---"))]
        print("%s  %s  (%d linhas diferentes)" % ("ok   " if not dif else "FALHA", rel, len(dif)))
        for x in dif[:6]:
            print("    " + x[:160])
        falhou = falhou or bool(dif)
    if falhou:
        raise SystemExit("o caminho de montagem não reproduz o que está no ar: nada foi gravado")


def main():
    modelo = ler(os.path.join(S.MODELO, "index.html"))
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    rodape_modelo = RODAPE.findall(ler(MODELO_ARTIGO))[-1]
    teste(modelo, rodape_modelo)
    if "--teste" in sys.argv:
        return
    alteradas = 0
    for p in PAGINAS:
        h = montar_pagina(modelo, p)
        rel = p["slug"] + "/index.html"
        n = conferir(rel, h)
        alteradas += gravar_gerada(rel, h)
        print("ok  /%s/  %d palavras" % (p["slug"], n))
    for a in ARTIGOS:
        rel, h = montar_artigo(a, rodape_modelo)
        conferir(rel, h)
        corpo = h.split('<article class="artigo-body">')[-1].split("</article>")[0]
        n = contar_palavras(corpo)
        assert n >= A.MIN_PALAVRAS, (rel, "raso demais", n)
        alteradas += gravar_gerada(rel, h)
        print("ok  /blog/%s/  %d palavras no artigo" % (a["slug"], n))
    print("arquivos de página alterados: %d" % alteradas)
    print("/nichos/: %s" % ("regerado com os cartões novos" if hub(modelo) else "sem mudança"))
    n, mudou = sitemap()
    print("sitemap: %d URLs (%s)" % (n, "alterado" if mudou else "sem mudança"))
    print("cartões novos no índice do blog: %d" % blog_index())
    print("llms: %s" % (", ".join(llms()) or "sem mudança"))


if __name__ == "__main__":
    main()
