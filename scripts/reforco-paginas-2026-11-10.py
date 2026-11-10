# -*- coding: utf-8 -*-
"""
Reforco de 2 paginas que ja existiam, com base no planejador de palavras-chave (10/11/2026).

1. /criacao-de-sites-goiania/  (posicao 26 a 52 para "criacao de site(s) goiania", 100 a 1 mil
   buscas/mes cada variacao em Goiania)
   Secao nova (marcador RCB:SITES-PROF) para as variacoes que a pagina nao cobria:
   "criacao de sites profissionais" (100 a 1 mil em Goiania), "desenvolvimento de sites
   goiania", "empresa de criacao de sites", "agencia de criacao de sites". Entra antes da
   secao "Por que eu nao me apresento como fabrica de sites".

2. /blog/como-colocar-minha-empresa-no-google/
   "como colocar minha empresa no google" e "cadastrar empresa no google": 1 mil a 10 mil
   buscas/mes cada no Brasil. O titulo so tinha "colocar". Entra "cadastrar" no titulo, no H1
   e na descricao. A mesma troca vai para a fonte (conteudo/artigos_visibilidade_google.py),
   para sobreviver a uma regeracao.

Sem preco, sem promessa. Idempotente.
    python scripts/reforco-paginas-2026-11-10.py
"""
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

SECAO = """<!--RCB:SITES-PROF-->    <section class="solution-section">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Site profissional</div>
          <h2 class="section-title">Criação de sites profissionais em Goiânia: o que muda de um site comum</h2>
          <p>Site comum é o que fica pronto, fica bonito, e ninguém acha. Site profissional é o que foi pensado a partir do que o seu cliente digita no Google. A diferença não está no desenho. Está no trabalho que vem antes: descobrir quais buscas trazem cliente para o seu ramo em Goiânia e ter uma página para cada uma.</p>
          <p>Por isso o desenvolvimento de sites aqui começa pela pesquisa e só depois vai para a tela. Vale para site institucional, para <a href="/criacao-de-landing-page/">landing page</a> e para <a href="/criacao-de-loja-virtual-goiania/">loja virtual</a>.</p>
          <p>Procura uma empresa de criação de sites em Goiânia que também cuide do Google, do mapa e dos anúncios? Conheça a <a href="/agencia-de-marketing-digital-goiania/">agência de marketing digital em Goiânia</a>. Ainda não sabe se precisa de site? Leia <a href="/blog/site-ou-instagram-para-empresa-local/">site ou Instagram para empresa local</a>.</p>
        </div>
        <div class="split-visual">
          <div class="visual-card">
            <div class="visual-card-title">O que um site profissional tem</div>
            <ul class="visual-list">
              <li>Uma página para cada serviço que você vende.</li>
              <li>A cidade e os bairros atendidos escritos no texto.</li>
              <li>Botão de WhatsApp sempre à vista no celular.</li>
              <li>Abertura rápida, mesmo em internet ruim.</li>
              <li>Ligação com o perfil da empresa no Google.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
<!--/RCB:SITES-PROF-->
"""
_SECAO = re.compile(r'<!--RCB:SITES-PROF-->.*?<!--/RCB:SITES-PROF-->\r?\n', re.S)
ANCORA = '<h2 class="section-title">Por que eu não me apresento como fábrica de sites</h2>'

T_VELHO = "Como colocar minha empresa no Google: passo a passo | RCB SEO"
T_NOVO = "Como Colocar (Cadastrar) Minha Empresa no Google: Passo a Passo"
BASE_VELHA = "Como colocar minha empresa no Google: passo a passo"
BASE_NOVA = "Como colocar (cadastrar) minha empresa no Google: passo a passo"
H1_NOVO = "Como colocar minha empresa no Google: passo a passo para cadastrar de graça"
D_VELHO = ("Como colocar sua empresa no Google de graça: veja como criar ou reivindicar o perfil, "
           "verificar o negócio e aparecer na Busca e no Maps.")
D_NOVO = ("Como colocar minha empresa no Google de graça: como cadastrar ou reivindicar o perfil, "
          "verificar o negócio e aparecer na busca e no Google Maps.")


def conferir(s, nome):
    assert s.startswith("<!DOCTYPE") and s.count("<h1") == 1, nome
    assert "R$ " not in SECAO
    for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(bloco)


def sites():
    p = RAIZ / "criacao-de-sites-goiania" / "index.html"
    s = io.open(p, encoding="utf-8", newline="").read()
    orig = s
    s = _SECAO.sub("", s)
    k = s.index(ANCORA)
    pos = s.rfind("<section", 0, k)
    pos = s.rfind("\n", 0, pos) + 1
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s[:pos] + SECAO.replace("\n", nl) + s[pos:]
    conferir(s, "sites")
    for href in re.findall(r'href="(/[^"]+/)"', SECAO):
        assert (RAIZ / href.strip("/") / "index.html").exists(), href
    if s != orig:
        io.open(p, "w", encoding="utf-8", newline="").write(s)
        return 1
    return 0


def _troca_artigo(s, html):
    if T_NOVO not in s:
        assert T_VELHO in s, "titulo antigo nao achado"
        s = s.replace(T_VELHO, T_NOVO)
    if html:
        s = s.replace(">%s</h1>" % BASE_VELHA, ">%s</h1>" % H1_NOVO)
        s = s.replace(BASE_VELHA + " |", BASE_NOVA + " |").replace('"%s"' % BASE_VELHA, '"%s"' % BASE_NOVA)
    else:
        s = s.replace('"h1": "%s"' % BASE_VELHA, '"h1": "%s"' % H1_NOVO)
    return s


def artigo():
    n = 0
    p = RAIZ / "blog" / "como-colocar-minha-empresa-no-google" / "index.html"
    s = io.open(p, encoding="utf-8", newline="").read()
    orig = s
    s = _troca_artigo(s, True)
    s = s.replace(D_VELHO, D_NOVO)
    assert D_NOVO in s and len(D_NOVO) <= 160 and len(T_NOVO) <= 65
    assert H1_NOVO in s, "H1 nao trocado"
    conferir(s, "artigo")
    if s != orig:
        io.open(p, "w", encoding="utf-8", newline="").write(s)
        n += 1
    # fonte do artigo (a descricao la esta quebrada em 2 pedacos de string)
    m = RAIZ / "scripts" / "conteudo" / "artigos_visibilidade_google.py"
    f = io.open(m, encoding="utf-8", newline="").read()
    orig = f
    f = _troca_artigo(f, False)
    velho = ('"desc": ("Como colocar sua empresa no Google de graça: veja como criar ou reivindicar o perfil, "')
    if velho in f:
        i = f.index(velho)
        j = f.index("),", i) + 2
        f = f[:i] + '"desc": ("%s"),' % D_NOVO + f[j:]
    assert D_NOVO in f and T_NOVO in f and H1_NOVO in f, "fonte nao atualizada"
    if f != orig:
        io.open(m, "w", encoding="utf-8", newline="").write(f)
        n += 1
    return n


def main():
    print("criacao-de-sites-goiania:", "alterada" if sites() else "sem mudanca")
    print("artigo colocar empresa no google: %d arquivo(s) alterado(s)" % artigo())


if __name__ == "__main__":
    sys.exit(main())
