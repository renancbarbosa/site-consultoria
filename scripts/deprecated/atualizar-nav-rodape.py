# -*- coding: utf-8 -*-
"""
Propaga o menu e o rodapé novos (com a divisão "SEO Nacional") para todas as
páginas HTML já publicadas.

Uso:  python scripts/atualizar-nav-rodape.py

O site é HTML estático escrito à mão: navbar e rodapé são blocos repetidos em
cada arquivo, sem fonte única. Este script faz o papel dessa fonte única —
rcb_base.NAV_MENU e rcb_base.FOOTER_COL_NACIONAL são a definição, e aqui elas
são espalhadas.

Idempotente: rodar duas vezes não duplica nada.
Não toca em node_modules, graphify-out, Projetos nem em docs/.
"""
import os
import re
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from rcb_base import RAIZ, NAV_MENU, FOOTER_COL_NACIONAL  # noqa: E402

IGNORAR = {"node_modules", "graphify-out", "Projetos", ".git", "docs", "scripts"}

# O bloco antigo do menu, em linha única. Existia em uma variante só (confirmado
# na auditoria: 305 arquivos, 1 hash distinto).
RE_NAV = re.compile(r'<ul class="nav-menu" id="navMenu" role="list">.*?</ul>', re.DOTALL)

# Duas variantes de rodapé no site: páginas usam "Contato", artigos do blog usam
# "Contato Direto". Ambas abrem com <div class="footer-col"> imediatamente antes.
RE_FOOTER = re.compile(
    r'(?P<abre><div class="footer-col">)(?P<esp>\s*)'
    r'<h4 class="footer-col-title">(?P<rotulo>Contato Direto|Contato)</h4>'
)


def html_do_site():
    for pasta, subpastas, arquivos in os.walk(RAIZ):
        subpastas[:] = [s for s in subpastas if s not in IGNORAR]
        for nome in arquivos:
            if nome.endswith(".html"):
                yield os.path.join(pasta, nome)


def nova_coluna(m):
    """Insere a coluna 'SEO Nacional' antes da coluna de contato, preservando
    a formatação do arquivo (compacta ou indentada)."""
    abre, esp, rotulo = m.group("abre"), m.group("esp"), m.group("rotulo")

    if "\n" in esp:
        # Rodapé indentado (artigos do blog): reproduz a indentação encontrada.
        ind_h4 = esp.split("\n")[-1]
        ind_div = ind_h4[:-2] if len(ind_h4) >= 2 else ind_h4
        col = FOOTER_COL_NACIONAL.replace(
            '</h4><nav class="footer-col-nav">', f'</h4>\n{ind_h4}<nav class="footer-col-nav">'
        )
        return (f'{abre}{esp}{col}\n{ind_div}</div>\n'
                f'{ind_div}<div class="footer-col">{esp}'
                f'<h4 class="footer-col-title">{rotulo}</h4>')

    # Rodapé compacto (páginas geradas e escritas em linha única).
    return (f'{abre}{FOOTER_COL_NACIONAL}</div>'
            f'<div class="footer-col">{esp}<h4 class="footer-col-title">{rotulo}</h4>')


def escrever_com_retry(caminho, conteudo, tentativas=5):
    """No Windows a escrita falha esporadicamente com EINVAL quando outro
    processo (indexador, antivírus, sincronizador de nuvem) está com o arquivo
    aberto. Reintenta antes de desistir."""
    for i in range(tentativas):
        try:
            with open(caminho, "w", encoding="utf-8", newline="") as f:
                f.write(conteudo)
            return True
        except OSError:
            if i == tentativas - 1:
                return False
            time.sleep(0.3 * (i + 1))
    return False


def main():
    tot = navs = rodapes = ja_ok = sem_nav = 0
    pendentes = []
    falhas = []

    for caminho in html_do_site():
        with open(caminho, encoding="utf-8") as f:
            original = f.read()
        novo = original
        rel = os.path.relpath(caminho, RAIZ).replace("\\", "/")

        # --- navbar ---
        # Substitui o bloco inteiro pelo NAV_MENU atual. Isso torna o script
        # idempotente e permite reaplicar depois de qualquer mudança no menu.
        achado = RE_NAV.search(novo)
        if achado and achado.group(0) == NAV_MENU:
            ja_ok += 1
        elif achado:
            novo = RE_NAV.sub(lambda _: NAV_MENU, novo, count=1)
            navs += 1
        elif 'class="navbar"' in novo:
            sem_nav += 1
            pendentes.append(rel)

        # --- rodapé ---
        if 'footer-col-title">SEO Nacional</h4>' not in novo and RE_FOOTER.search(novo):
            novo = RE_FOOTER.sub(nova_coluna, novo, count=1)
            rodapes += 1

        if novo != original:
            if escrever_com_retry(caminho, novo):
                tot += 1
            else:
                falhas.append(rel)

    print(f"Arquivos alterados : {tot}")
    print(f"Menus atualizados  : {navs}")
    print(f"Rodapés atualizados: {rodapes}")
    print(f"Já estavam corretos: {ja_ok}")
    if falhas:
        print(f"\nFALHA de escrita em {len(falhas)} arquivo(s) — rode o script de novo:")
        for f_ in falhas:
            print(f"  - {f_}")
    if pendentes:
        print(f"\nCom navbar fora do padrão (revisar à mão): {sem_nav}")
        for p in pendentes:
            print(f"  - {p}")


if __name__ == "__main__":
    main()
