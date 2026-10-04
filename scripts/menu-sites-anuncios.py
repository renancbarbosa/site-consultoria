# -*- coding: utf-8 -*-
"""
Liga a linha "Sites e Anúncios" (28/09/2026) ao site inteiro:

  - MENU: 4 itens no topo do dropdown "Serviços" (criação de sites, landing page,
    tráfego pago, loja virtual). Dentro do dropdown, e não como item novo no topo,
    porque o menu do computador já está no limite de largura (ver rodada de 08/09).
  - RODAPÉ: os mesmos 4 links no começo da coluna "Serviços" (ou "Navegação" nos
    artigos do blog; a home tem formato próprio com <ul><li>).
  - GERADORES (--geradores): rcb_base.py e gerar-paginas-cidades.py aprendem o
    mesmo, para uma regeração futura não desfazer.

Inserção com marcador (<!--RCB:SITES-NAV-->, <!--RCB:SITES-FOOTER-->): idempotente,
a 2ª execução diz "alteradas: 0". Nunca substitui o bloco inteiro de menu/rodapé.
Autorização do Renan para tocar o menu de /consultor-seo-goiania/: 28/09/2026.
"""
import sys as _sys
_sys.exit("DESATIVADO em 04/10/2026: agentes de IA, automacao e recuperacao de vendas sairam do site (Etapa 1, docs/plano-nichos-2026-10.md). O menu e o rodape agora vem de scripts/rcb_menu.py.")
import io
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
PULAR = ("node_modules", ".git", "docs", "data", "scripts", ".playwright-mcp", "graphify-out")

ITENS = [
    ("/criacao-de-sites-goiania/", "Criação de sites"),
    ("/criacao-de-landing-page/", "Landing page"),
    ("/gestao-de-trafego-pago-goiania/", "Tráfego pago (Google e Meta Ads)"),
    ("/criacao-de-loja-virtual-goiania/", "Loja virtual"),
]

NAV = ("<!--RCB:SITES-NAV-->"
       + "".join('<a href="%s" class="nav-dropdown-item" role="menuitem">%s</a>' % i for i in ITENS)
       + "<!--/RCB:SITES-NAV-->")
FOOTER = ("<!--RCB:SITES-FOOTER-->"
          + "".join('<a href="%s">%s</a>' % i for i in ITENS)
          + "<!--/RCB:SITES-FOOTER-->")
FOOTER_LI = ("<!--RCB:SITES-FOOTER-->"
             + "".join('<li><a href="%s">%s</a></li>' % i for i in ITENS)
             + "<!--/RCB:SITES-FOOTER-->")

R_NAV = re.compile(r'(Serviços<svg[^>]*>.*?</svg></button><div class="nav-dropdown-menu" role="menu">)', re.S)
R_FOOT = [
    (re.compile(r'(<h3 class="footer-col-title">Serviços</h3>\s*<nav class="footer-col-nav"[^>]*>)'), FOOTER),
    (re.compile(r'(<h3 class="footer-col-title">Navegação</h3>\s*<nav class="footer-col-nav"[^>]*>)'), FOOTER),
    (re.compile(r'(<h3>Serviços</h3>\s*<ul>)'), FOOTER_LI),     # home (.footer-grid)
]


def aplicar(h):
    feito = []
    if "RCB:SITES-NAV" not in h:
        h, n = R_NAV.subn(lambda m: m.group(1) + NAV, h, count=1)
        if n:
            feito.append("menu")
    if "RCB:SITES-FOOTER" not in h:
        # o ULTIMO rodape do arquivo: a home tem <footer> aninhado nos depoimentos
        for r, bloco in R_FOOT:
            ms = list(r.finditer(h))
            if ms:
                m = ms[-1]
                h = h[:m.end()] + bloco + h[m.end():]
                feito.append("rodape")
                break
    return h, feito


def ensinar_geradores():
    """rcb_base.NAVBAR/rodape e o NAVBAR/rodape das cidades."""
    mudou = []
    for rel in ("rcb_base.py", "gerar-paginas-cidades.py"):
        p = AQUI / rel
        s = io.open(p, encoding="utf-8", newline="").read()
        orig = s
        if "RCB:SITES-NAV" not in s:
            s, n = R_NAV.subn(lambda m: m.group(1) + NAV, s, count=1)
            if not n:
                print("  ! menu nao encontrado em", rel)
        if "RCB:SITES-FOOTER" not in s:
            alvo = '<h3 class="footer-col-title">Serviços</h3><nav class="footer-col-nav">'
            if alvo in s:
                s = s.replace(alvo, alvo + FOOTER, 1)
            else:
                print("  ! rodape nao encontrado em", rel)
        if s != orig:
            io.open(p, "w", encoding="utf-8", newline="").write(s)
            mudou.append(rel)
    return mudou


def main():
    alteradas, sem_menu, sem_rodape = 0, [], []
    for f in sorted(RAIZ.rglob("*.html")):
        rel = f.relative_to(RAIZ).as_posix()
        if rel.startswith(PULAR):
            continue
        h = io.open(f, encoding="utf-8", newline="").read()
        novo, feito = aplicar(h)
        if "RCB:SITES-NAV" not in novo and 'class="nav-dropdown-menu"' in novo:
            sem_menu.append(rel)
        if "RCB:SITES-FOOTER" not in novo and "<footer" in novo:
            sem_rodape.append(rel)
        if novo != h:
            assert novo.lstrip().startswith("<!DOCTYPE"), rel
            io.open(f, "w", encoding="utf-8", newline="").write(novo)
            alteradas += 1
    print("paginas alteradas:", alteradas)
    print("com menu mas sem os itens novos:", sem_menu)
    print("com rodape mas sem os links novos:", sem_rodape)
    if "--geradores" in sys.argv:
        print("geradores ensinados:", ensinar_geradores())


if __name__ == "__main__":
    main()
