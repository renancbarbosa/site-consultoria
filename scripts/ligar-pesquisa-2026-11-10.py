# -*- coding: utf-8 -*-
"""Liga as paginas da pesquisa de palavras-chave de 10/11/2026 ao resto do site.

Paginas reforcadas (as que tem procura medida no planejador e estao fracas ou sao novas):
  /agencia-de-marketing-digital-goiania/        (nova)
  /landing-page-para-advogados/                 (nova)
  /criacao-de-sites-goiania/                    (existia, posicao 26 a 52)
  /blog/como-colocar-minha-empresa-no-google/   (existia, so 9 paginas apontavam para ela)

O que faz:
1. Menu (dropdown "SEO e Google") e coluna Servicos do rodape: item novo da agencia em todas
   as paginas com menu. Trava: a pagina so e gravada se a UNICA diferenca for o item novo.
2. Caixa de texto (marcador RCB:PESQUISA-1110) antes das perguntas frequentes em todas as
   paginas escritas a mao e indexaveis, com 2 ou 3 links. Ancoras variadas, tiradas das buscas
   reais ("agencia de marketing em Goiania", "marketing digital em Goiania", "criacao de site
   em Goiania", "cadastrar a empresa no Google"...). Paginas de advocacia e de landing page
   ganham tambem o link para /landing-page-para-advogados/.
3. llms.txt e llms-full.txt: as 2 paginas novas na lista de servicos.

Fora das caixas: cidades (o gerador sobrescreve; elas recebem pelo menu e rodape), paginas
sem indexacao e /consultor-seo-goiania/ (PROTEGIDA). A protegida so entra no passo 1 quando
o script e chamado com --protegida (commit separado).
Idempotente: 2a execucao, 0 alteradas.
    python scripts/ligar-pesquisa-2026-11-10.py [--protegida]
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import rcb_menu  # noqa: E402

AG = "/agencia-de-marketing-digital-goiania/"
LP = "/landing-page-para-advogados/"
SITES = "/criacao-de-sites-goiania/"
COLOCAR = "/blog/como-colocar-minha-empresa-no-google/"
PROTEGIDA = "consultor-seo-goiania/index.html"
INTERNAS = ("docs/", "scripts/", "data/", "reports/", "node_modules/", "graphify-out/",
            "Projetos/", "modelos/", "functions/", "tmp/")
SEM_CAIXA = ("consultoria-seo/", "privacidade/", "cookies/", "404.html", "diagnostico-presenca-digital/exemplo/",
             "index.html", "blog/index.html", "servicos/index.html", "nichos/index.html", "contato/index.html",
             "sobre/index.html", "cases/index.html", "ferramentas/index.html")
NOME_MENU = "Agência de marketing digital em Goiânia"
ITEM_MENU = '<a href="%s" class="nav-dropdown-item" role="menuitem">%s</a>' % (AG, NOME_MENU)
ITENS_RODAPE = ('<li><a href="%s">%s</a></li>' % (AG, NOME_MENU), '<a href="%s">%s</a>' % (AG, NOME_MENU))

A = '<a href="%s">%s</a>'
# (abertura, ancora da agencia, frase de ligacao)
AGENCIA = [
    ("Sua empresa é de Goiânia?", "agência de marketing digital em Goiânia",
     "Conheça a %s que cuida de site, Google e anúncios com atendimento direto."),
    ("Quer alguém para fazer isso por você?", "agência de marketing em Goiânia",
     "A RCB SEO é uma %s em que você fala com quem faz o trabalho."),
    ("Marketing digital em Goiânia:", "marketing digital em Goiânia",
     "veja como a RCB SEO cuida do %s de empresas da cidade, do site ao mapa do Google."),
    ("Precisa de ajuda profissional?", "empresa de marketing digital em Goiânia",
     "Veja o que faz uma %s voltada para o Google."),
    ("Atendimento presencial em Goiânia:", "agência de marketing digital goianiense",
     "conheça a %s que atende com hora marcada, sem fidelidade."),
    ("Tem empresa em Goiânia ou região?", "agência digital em Goiânia",
     "Veja como trabalha a %s que coloca empresas locais no Google."),
]
SEGUNDO = [
    (SITES, "Ainda não tem site? Veja a %s.", "criação de sites em Goiânia"),
    (COLOCAR, "Está começando do zero? Leia %s.", "como colocar a sua empresa no Google"),
    (SITES, "Precisa de um site que traga contato? Veja a %s.", "criação de site em Goiânia"),
    (COLOCAR, "Ainda não está no Google? Veja %s.", "como cadastrar a empresa no Google"),
    (SITES, "Quer um site novo? Conheça a %s.", "criação de sites profissionais em Goiânia"),
    (COLOCAR, "Primeiro passo: %s.", "como colocar minha empresa no Google de graça"),
    (SITES, "Site parado, sem visita? Veja o %s.", "desenvolvimento de sites em Goiânia"),
]
ADV = " É advogado e anuncia no Google? Veja a " + A % (LP, "landing page para advogados") + "."
ADV_ALVOS = ("advog", "advoc", "criacao-de-landing-page", "juridic")

_CAIXA = re.compile(r'<!--RCB:PESQUISA-1110-->.*?<!--/RCB:PESQUISA-1110-->\n', re.S)
_FAQ = re.compile(r'<h2[^>]*>\s*Perguntas frequentes', re.I)
_OUTRAS = ("<!--RCB:GMN-GOIANIA-->", "<!--RCB:REFORCO-->")


def paginas():
    out = subprocess.run(["git", "ls-files", "*.html"], cwd=RAIZ, capture_output=True,
                         text=True, encoding="utf-8").stdout.split()
    return sorted(set(p for p in out if not p.startswith(INTERNAS)))


def menu_e_rodape(h):
    novo = rcb_menu._troca_menu(h)
    novo = rcb_menu._SITES_FOOTER.sub(lambda m: "<!--RCB:SITES-FOOTER-->" + rcb_menu._bloco_servicos(m.group(1))
                                      + "<!--/RCB:SITES-FOOTER-->", novo)
    conferir = novo
    if ITEM_MENU not in h:
        conferir = conferir.replace(ITEM_MENU, "", 1)
    for it in ITENS_RODAPE:
        if it not in h and it in conferir:
            conferir = conferir.replace(it, "", 1)
            break
    return novo, conferir == h


def texto(rel, i):
    url = "/" + rel[:-len("index.html")]
    ab, anc, frase = AGENCIA[i % len(AGENCIA)]
    partes = []
    if url != AG:
        partes.append("<strong>%s</strong> %s" % (ab, frase % (A % (AG, anc))))
    j = i
    while True:
        alvo, f2, anc2 = SEGUNDO[j % len(SEGUNDO)]
        if alvo != url:
            break
        j += 1
    partes.append(f2 % (A % (alvo, anc2)))
    t = " ".join(partes)
    if any(k in rel for k in ADV_ALVOS) and url != LP:
        t += ADV
    return t


def caixa(h, rel, i):
    h = _CAIXA.sub("", h)
    blog = rel.startswith("blog/")
    if blog:
        bloco = '<div class="artigo-cta-box"><p>%s</p></div>' % texto(rel, i)
    else:
        bloco = ('<section class="solution-section"><div class="container"><div class="split-copy" '
                 'style="max-width:860px;margin:0 auto"><p>%s</p></div></div></section>' % texto(rel, i))
    bloco = "<!--RCB:PESQUISA-1110-->" + bloco + "<!--/RCB:PESQUISA-1110-->\n"
    m = _FAQ.search(h)
    pos = -1
    if m:
        pos = h.rfind("<section", 0, m.start())
        if blog or pos < 0:
            pos = h.rfind("\n", 0, m.start()) + 1
    if pos <= 0:
        pos = h.find("</article>") if blog and "</article>" in h else h.find("</main>")
    if pos <= 0:
        return None
    # outras caixas ja ficam coladas no FAQ: esta entra antes da primeira delas
    andou = True
    while andou:
        andou = False
        for marca in _OUTRAS:
            fim_marca = marca.replace("<!--", "<!--/")
            k = h.rfind(marca, 0, pos + 1)
            if k >= 0:
                f = h.find(fim_marca, k)
                if 0 <= f < pos and pos - (f + len(fim_marca)) < 40:
                    pos, andou = k, True
    return h[:pos] + bloco + h[pos:]


def indexavel(h):
    m = re.search(r'<meta name="robots" content="([^"]*)"', h)
    return not (m and "noindex" in m.group(1))


LLMS = [
    ("- Agência de marketing digital em Goiânia: https://rcbseo.com.br/agencia-de-marketing-digital-goiania/. "
     "A RCB SEO atua como agência de marketing digital em Goiânia para empresas locais: site, Google e mapa "
     "(SEO local), anúncios no Google e presença nas respostas de IA. Atendimento direto do consultor Renan "
     "Carvalho Barbosa, presencial em Goiânia e região. Não faz gestão de redes sociais."),
    ("- Landing page para advogados: https://rcbseo.com.br/landing-page-para-advogados/. Página única por área "
     "de atuação para receber quem clica no anúncio do escritório, dentro do Provimento 205/2021 da OAB. "
     "Atendimento online para todo o Brasil."),
]


def llms():
    mudou = []
    for nome in ("llms.txt", "llms-full.txt"):
        p = os.path.join(RAIZ, nome)
        if not os.path.exists(p):
            continue
        s = io.open(p, encoding="utf-8", newline="").read()
        orig = s
        alvo = re.search(r"^- [^\r\n]*https://rcbseo\.com\.br/google-meu-negocio-goiania/[^\r\n]*", s, re.M) or \
            re.search(r"^[-*] [^\r\n]*https://rcbseo\.com\.br/google-perfil-empresa/[^\r\n]*", s, re.M)
        if not alvo:
            print("AVISO: %s sem linha de referencia; nao mexi" % nome)
            continue
        nl = "\r\n" if "\r\n" in s else "\n"
        fim = alvo.end()
        marca = alvo.group(0)[0]  # "-" no llms.txt, "*" no llms-full.txt
        for linha in LLMS:
            if linha.split(": ")[1].split(". ")[0] in s:
                continue
            linha = marca + linha[1:]
            s = s[:fim] + nl + linha + s[fim:]
            fim += len(nl) + len(linha)
        if s != orig:
            io.open(p, "w", encoding="utf-8", newline="").write(s)
            mudou.append(nome)
    return mudou


def main():
    com_protegida = "--protegida" in sys.argv
    alteradas, recusadas, sem_lugar, caixas = [], [], [], 0
    i = 0
    for rel in paginas():
        if rel == PROTEGIDA and not com_protegida:
            continue
        p = os.path.join(RAIZ, rel)
        raw = io.open(p, encoding="utf-8", newline="").read()
        novo, ok = menu_e_rodape(raw)
        if not ok:
            recusadas.append(rel)
            novo = raw
        if (rel != PROTEGIDA and rel.endswith("index.html") and not rel.startswith(SEM_CAIXA)
                and rel not in SEM_CAIXA and indexavel(raw) and "<main" in raw):
            c = caixa(novo, rel, i)
            i += 1
            if c is None:
                sem_lugar.append(rel)
            else:
                novo = c
                caixas += 1
        if novo != raw:
            assert novo.lstrip("﻿").startswith("<!DOCTYPE") or not raw.lstrip("﻿").startswith("<!DOCTYPE"), rel
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            alteradas.append(rel)
    print("alteradas:", len(alteradas))
    print("paginas com caixa:", caixas)
    print("menu/rodape recusado (diferenca alem do item novo):", recusadas)
    print("caixa sem lugar:", sem_lugar)
    print("llms:", llms() or "sem mudanca")


if __name__ == "__main__":
    main()
