"""Exclui as paginas de cidade em noindex (decisao do Renan, 04/10/2026).

Motivo: de 13/08 a 01/10/2026 as 168 cidades em noindex tiveram 0 cliques (e as 31
visiveis tambem 0), e manter as 168 multiplicava o trabalho de qualquer mudanca no
site. As 31 de scripts/rcb_cidades.py INDEXAVEIS (incluindo os 3 pilotos) ficam.
Registro: docs/decisao-cidades-2026-08-12.md, adendo de 04/10/2026.

O que faz:
  1. Confere: as pastas a apagar sao EXATAMENTE as de /consultoria-seo/ que estao
     fora de INDEXAVEIS, todas com noindex, nenhuma indexavel. Se nao bater, para.
  2. Apaga as pastas (so com --aplicar).
  3. Tira todo link interno para elas:
     - hub /consultoria-seo/: o item da lista; estado sem cidade some; regiao sem
       estado some;
     - frase "Tambem atendo outras cidades de ...": tira o link e o separador;
       se nao sobrar cidade, tira a secao inteira (como o gerador faz);
     - qualquer outro link: vira texto simples.
  4. llms.txt: "199 cidades" vira o numero real.

Sem --aplicar so mostra o que faria. Idempotente (depois de apagar, a lista das
excluidas vem do bloco RCB:CIDADES-EXCLUIDAS do documento de decisao).
    python scripts/excluir-cidades-noindex-2026-10-04.py            # relatorio
    python scripts/excluir-cidades-noindex-2026-10-04.py --aplicar  # executa
"""
import glob
import os
import re
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from rcb_cidades import INDEXAVEIS  # noqa: E402

RAIZ = os.path.dirname(AQUI)
PASTA = os.path.join(RAIZ, "consultoria-seo")
DOC = os.path.join(RAIZ, "docs", "decisao-cidades-2026-08-12.md")
S = re.S
ESPERADO = 168


def ler(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def gravar(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def tem_noindex(h):
    return re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', h, re.I) is not None


def tira_links(t, alvo):
    """Remove os links para as cidades de `alvo`. Devolve (texto, links removidos)."""
    if not alvo:
        return t, 0
    slug_rx = "(?:" + "|".join(re.escape(s) for s in sorted(alvo, key=len, reverse=True)) + ")"
    href = r'(?:https://rcbseo\.com\.br)?/consultoria-seo/' + slug_rx + r'/'
    link = r'<a href="' + href + r'">[^<]*</a>'
    n = 0
    # hub: item de lista
    t, k = re.subn(r'\r?\n[ \t]*<li>' + link + r'[^<]*</li>', '', t)
    n += k
    # estado que ficou sem cidade / regiao que ficou sem estado
    t = re.sub(r'\s*<div class="diagnostic-card">\s*<h3>[^<]*</h3>\s*<ul class="audit-list">\s*</ul>\s*</div>', '', t)
    t = re.sub(r'\s*<section class="problem-section" aria-label="Região [^"]*">\s*<div class="container">\s*'
               r'<div class="section-header">(?:(?!</section>).)*?</div>\s*<div class="problem-grid">\s*</div>\s*'
               r'</div>\s*</section>', '', t, flags=S)
    # frase "Tambem atendo outras cidades de ...": link + separador " · "
    t, k1 = re.subn(link + r' · ', '', t)
    t, k2 = re.subn(r' · ' + link, '', t)
    t, k3 = re.subn(r'(e região: )' + link + r'(\. Veja)', r'\1\2', t)
    n += k1 + k2 + k3
    # nao sobrou cidade na frase: a secao inteira sai (o gerador tambem omite)
    t = re.sub(r'\s*<section class="solution-section" aria-label="Outras cidades atendidas">\s*<div class="container">\s*'
               r'<p class="section-desc">Também atendo outras cidades de [^:<]*: \. Veja (?:(?!</section>).)*?</p>\s*'
               r'</div>\s*</section>', '', t, flags=S)
    # qualquer outro link: vira texto
    t, k = re.subn(r'<a [^>]*href="' + href + r'"[^>]*>(.*?)</a>', r'\1', t, flags=S)
    n += k
    return t, n


def main():
    aplicar = "--aplicar" in sys.argv
    pastas = sorted(d for d in os.listdir(PASTA) if os.path.isfile(os.path.join(PASTA, d, "index.html")))
    fora = [d for d in pastas if d not in INDEXAVEIS]
    problemas = []
    sem_noindex = [d for d in fora if not tem_noindex(ler(os.path.join(PASTA, d, "index.html")))]
    idx_noindex = [d for d in pastas if d in INDEXAVEIS and tem_noindex(ler(os.path.join(PASTA, d, "index.html")))]
    faltando = sorted(INDEXAVEIS - set(pastas))
    if sem_noindex:
        problemas.append("fora de INDEXAVEIS mas SEM noindex: %s" % sem_noindex)
    if idx_noindex:
        problemas.append("INDEXAVEIS com noindex: %s" % idx_noindex)
    if faltando:
        problemas.append("indexaveis sem pasta: %s" % faltando)
    if fora and len(fora) != ESPERADO:
        problemas.append("esperado %d pastas a apagar, achei %d" % (ESPERADO, len(fora)))
    print("pastas em /consultoria-seo/   :", len(pastas))
    print("indexaveis (rcb_cidades)     :", len(INDEXAVEIS))
    print("a apagar (fora de INDEXAVEIS):", len(fora))
    if problemas:
        print("PAROU - nada foi apagado:")
        for p in problemas:
            print("   ", p)
        sys.exit(1)

    m = re.search(r"<!-- RCB:CIDADES-EXCLUIDAS:INICIO -->(.*?)<!-- RCB:CIDADES-EXCLUIDAS:FIM -->", ler(DOC), S)
    alvo = (set(fora) | (set(re.findall(r"`([a-z0-9\-]+)`", m.group(1))) if m else set())) - INDEXAVEIS

    arquivos = []
    for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True):
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        if rel.startswith(("scripts/", "docs/", "data/", "node_modules/", ".git/")):
            continue
        if rel.startswith("consultoria-seo/") and rel.count("/") == 2 and rel.split("/")[1] in fora:
            continue  # vai ser apagada
        arquivos.append(p)
    total, mudados = 0, []
    for p in sorted(arquivos):
        t0 = ler(p)
        t, n = tira_links(t0, alvo)
        if t != t0:
            total += n
            mudados.append((os.path.relpath(p, RAIZ), n))
            if aplicar:
                gravar(p, t)
    llms = os.path.join(RAIZ, "llms.txt")
    l0 = ler(llms)
    l1, n = tira_links(l0, alvo)
    l1 = re.sub(r'para \d+ cidades brasileiras', 'para %d cidades brasileiras' % len(INDEXAVEIS), l1)
    if l1 != l0:
        total += n
        mudados.append(("llms.txt", n))
        if aplicar:
            gravar(llms, l1)
    if aplicar:
        for d in fora:
            shutil.rmtree(os.path.join(PASTA, d))
    print("arquivos alterados           :", len(mudados))
    print("links removidos              :", total)
    for rel, n in mudados:
        print("   %4d  %s" % (n, rel))
    print("pastas apagadas              :", len(fora) if aplicar else "0 (relatorio; rode com --aplicar)")


if __name__ == "__main__":
    main()
