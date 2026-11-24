# -*- coding: utf-8 -*-
"""Liga os 5 nichos de 23/11/2026 (salão, oficina, loja, construtoras, arquitetos) ao resto do site.

1. Menu: os 5 itens novos do dropdown "Nichos" (rcb_menu.NICHOS) em todas as páginas com menu.
   Trava: a página só é gravada se a ÚNICA diferença for os itens novos (o mesmo cuidado do
   ligar-gmn-goiania-2026-11-09.py). /consultor-seo-goiania/ (PROTEGIDA) só com --protegida,
   e em commit próprio.
2. Caixa de texto (marcador RCB:NICHOS-1123) antes das perguntas frequentes nas páginas do mesmo
   assunto, com link para a página ou o artigo do nicho novo. Âncoras descritivas e variadas.
   Se a caixa já existe, é trocada no mesmo lugar (não troca de posição com as outras caixas).

Idempotente: 2ª execução, 0 alteradas.
    python scripts/ligar-nichos-2026-11-23.py
    python scripts/ligar-nichos-2026-11-23.py --protegida   # só o menu da página protegida
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import rcb_menu  # noqa: E402

PROTEGIDA = "consultor-seo-goiania/index.html"
INTERNAS = ("docs/", "scripts/", "data/", "reports/", "node_modules/", "graphify-out/",
            "Projetos/", "modelos/", "functions/", "tmp/")

SAL, OFI, LOJ, CON, ARQ = ("/marketing-para-salao-de-beleza/", "/marketing-para-oficina-mecanica/",
                           "/marketing-para-loja/", "/marketing-para-construtoras/",
                           "/marketing-para-arquitetos/")
B = "/blog/"
A_SAL = B + "como-atrair-clientes-para-salao-de-beleza/"
A_OFI = B + "como-atrair-clientes-para-oficina-mecanica/"
A_LOJ = B + "como-atrair-clientes-para-loja/"
A_CON = B + "landing-page-para-construtora/"
A_ARQ = B + "google-ads-para-arquitetos/"

NOVOS = (SAL, OFI, LOJ, CON, ARQ)
ITENS_MENU = ['<a href="%s" class="nav-dropdown-item" role="menuitem">%s</a>' % (h, t)
              for h, t in rcb_menu.NICHOS if h in NOVOS]
assert len(ITENS_MENU) == 5, "rcb_menu.NICHOS sem os 5 nichos novos"

A = '<a href="%s">%s</a>'
# página que recebe a caixa -> texto (com os links)
CAIXAS = {
    "marketing-para-empresa-de-guincho/index.html":
        "<strong>Guincho e oficina andam juntos.</strong> Se você tem oficina ou trabalha com uma, veja o "
        + A % (OFI, "marketing para oficina mecânica") + ": o motorista confia na oficina antes de chegar.",
    "blog/como-conseguir-clientes-para-guincho/index.html":
        "<strong>Leia também:</strong> " + A % (A_OFI, "como atrair clientes para oficina mecânica")
        + ", o lugar para onde vai boa parte dos carros que o guincho leva.",
    "marketing-para-empresa-de-reformas/index.html":
        "<strong>Faz obra maior ou trabalha junto com projeto?</strong> Veja o "
        + A % (CON, "marketing para construtoras e incorporadoras") + " e o "
        + A % (ARQ, "marketing para arquitetos") + ", ramos que atendem o mesmo cliente de quem vai reformar.",
    "blog/como-conseguir-clientes-para-reformas/index.html":
        "<strong>Leia também:</strong> " + A % (A_CON, "o que a landing page de uma construtora precisa ter")
        + " e " + A % (A_ARQ, "quando o Google Ads vale a pena para arquitetos") + ".",
    "seo-para-clinicas-de-estetica/index.html":
        "<strong>Tem salão de beleza ou barbearia?</strong> O caminho é parecido, mas o cliente e as regras "
        "mudam. Veja o " + A % (SAL, "marketing para salão de beleza e barbearia") + " e "
        + A % (A_SAL, "10 caminhos para atrair clientes para o salão") + ".",
    "para-comercios-locais/index.html":
        "<strong>Tem loja de rua ou de bairro?</strong> Veja o " + A % (LOJ, "marketing para loja")
        + ", com produtos no Google e as datas que mais vendem, e "
        + A % (A_LOJ, "10 ideias para atrair clientes para a loja") + ".",
    "criacao-de-landing-page/index.html":
        "<strong>É construtora ou incorporadora?</strong> Veja "
        + A % (A_CON, "o que a landing page de cada empreendimento precisa ter")
        + ", do topo ao número do registro da incorporação.",
    "criacao-de-loja-virtual-goiania/index.html":
        "<strong>Também tem loja física?</strong> Veja o "
        + A % (LOJ, "marketing para loja de rua e de bairro") + ", para levar gente até a porta, não só ao site.",
    "seo-para-imobiliarias/index.html":
        "<strong>Trabalha com lançamento?</strong> Para a construtora e a incorporadora, veja o "
        + A % (CON, "marketing para construtoras") + ", com uma página para cada empreendimento.",
}

INI, FIM = "<!--RCB:NICHOS-1123-->", "<!--/RCB:NICHOS-1123-->"
_CAIXA = re.compile(re.escape(INI) + r".*?" + re.escape(FIM) + r"\r?\n?", re.S)


def paginas():
    """Páginas do git, incluindo as novas que ainda não foram commitadas."""
    out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.html"],
                         cwd=RAIZ, capture_output=True, text=True, encoding="utf-8").stdout.split()
    return sorted(set(p for p in out if not p.startswith(INTERNAS)))


def menu(h):
    """Menu atual do rcb_menu. Devolve (novo, ok): ok só se a única diferença forem os itens novos."""
    novo = rcb_menu._troca_menu(h)
    conferir = novo
    for item in ITENS_MENU:
        if item not in h:
            conferir = conferir.replace(item, "", 1)
    return novo, conferir == h


def caixa(h, rel, texto):
    artigo = rel.startswith("blog/")
    if artigo:
        bloco = '<div class="artigo-cta-box"><p>%s</p></div>' % texto
    else:
        bloco = ('<section class="solution-section"><div class="container"><div class="split-copy" '
                 'style="max-width:860px;margin:0 auto"><p>%s</p></div></div></section>' % texto)
    bloco = INI + bloco + FIM + ("\r\n" if "\r\n" in h else "\n")  # a quebra de linha do próprio arquivo
    if INI in h:
        return _CAIXA.sub(lambda _: bloco, h, count=1)
    ancora = '<section class="artigo-faq"' if artigo else '<section class="faq-section"'
    if h.count(ancora) != 1:
        return None
    pos = h.rfind("\n", 0, h.find(ancora)) + 1  # começo da linha do FAQ: a caixa fica numa linha própria
    return h[:pos] + bloco + h[pos:]


def main():
    com_protegida = "--protegida" in sys.argv
    for rel in CAIXAS:  # trava: todo link da caixa precisa existir
        for href in re.findall(r'href="([^"]+)"', CAIXAS[rel]):
            assert os.path.exists(os.path.join(RAIZ, href.strip("/"), "index.html")), (rel, href)
    alteradas, recusadas, sem_lugar, menus, caixas = [], [], [], 0, 0
    for rel in paginas():
        if (rel == PROTEGIDA) != com_protegida:
            continue  # sem a flag, pula a protegida; com a flag, só ela
        p = os.path.join(RAIZ, rel)
        raw = io.open(p, encoding="utf-8", newline="").read()
        novo, ok = menu(raw)
        if not ok:
            recusadas.append(rel)
            novo = raw
        elif novo != raw:
            menus += 1
        if rel in CAIXAS and rel != PROTEGIDA:
            c = caixa(novo, rel, CAIXAS[rel])
            if c is None:
                sem_lugar.append(rel)
            else:
                caixas += c != novo
                novo = c
        if novo != raw:
            assert novo.startswith("<!DOCTYPE") or not raw.startswith("<!DOCTYPE"), rel
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            alteradas.append(rel)
    print("alteradas:", len(alteradas))
    print("menu atualizado:", menus)
    print("caixas novas ou trocadas:", caixas)
    print("menu recusado (diferença além dos itens novos):", recusadas)
    print("caixa sem lugar:", sem_lugar)


if __name__ == "__main__":
    main()
