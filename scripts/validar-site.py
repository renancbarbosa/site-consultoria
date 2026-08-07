# -*- coding: utf-8 -*-
"""
Validação do site estático.

Uso:  python scripts/validar-site.py

Verifica:
  1. links internos quebrados (href que não resolve para arquivo existente)
  2. títulos e descrições duplicados ou fora do limite
  3. páginas sem canonical, sem H1 ou com mais de um H1
  4. marcadores de rascunho esquecidos
  5. páginas órfãs (nenhuma outra página aponta para elas)
  6. URLs do sitemap que não existem, e páginas fora do sitemap
"""
import os
import re
import sys
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from rcb_base import RAIZ  # noqa: E402

IGNORAR = {"node_modules", "graphify-out", "Projetos", ".git", "docs", "scripts"}
BASE = "https://rcbseo.com.br"

RE_HREF = re.compile(r'href="([^"]+)"')
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
RE_DESC = re.compile(r'<meta name="description" content="([^"]*)"')
RE_CANON = re.compile(r'<link rel="canonical" href="([^"]+)"')


def paginas():
    for pasta, subs, arqs in os.walk(RAIZ):
        subs[:] = [s for s in subs if s not in IGNORAR]
        for nome in arqs:
            if nome.endswith(".html"):
                caminho = os.path.join(pasta, nome)
                rel = os.path.relpath(caminho, RAIZ).replace("\\", "/")
                yield rel, caminho


def url_de(rel):
    """Converte caminho de arquivo em URL do site."""
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    if rel == "index.html":
        return "/"
    return "/" + rel


def resolve(href):
    """Converte href interno em caminho de arquivo esperado. None = externo/âncora."""
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        if href.startswith(BASE):
            href = href[len(BASE):] or "/"
        else:
            return None
    href = href.split("#")[0].split("?")[0]
    if not href.startswith("/"):
        return None
    if href.endswith("/"):
        return os.path.join(RAIZ, href.strip("/"), "index.html")
    if "." in os.path.basename(href):
        return os.path.join(RAIZ, href.strip("/"))
    return os.path.join(RAIZ, href.strip("/"), "index.html")


def main():
    todas = dict(paginas())
    urls_existentes = {url_de(r) for r in todas}

    quebrados = defaultdict(list)
    titulos = defaultdict(list)
    descricoes = defaultdict(list)
    problemas = []
    apontadas = set()

    for rel, caminho in todas.items():
        html = open(caminho, encoding="utf-8").read()
        corpo = html.split("<body", 1)[-1]

        # 1. links internos
        for href in set(RE_HREF.findall(corpo)):
            alvo = resolve(href)
            if alvo is None:
                continue
            if not os.path.exists(alvo):
                quebrados[href].append(rel)
            else:
                destino = os.path.relpath(alvo, RAIZ).replace("\\", "/")
                if destino != rel:
                    apontadas.add(url_de(destino))

        # 2. title / description
        m = RE_TITLE.search(html)
        if not m:
            problemas.append(f"{rel}: sem <title>")
        else:
            t = m.group(1).strip()
            titulos[t].append(rel)
            if len(t) > 65:
                problemas.append(f"{rel}: title com {len(t)} caracteres")

        m = RE_DESC.search(html)
        if not m:
            problemas.append(f"{rel}: sem meta description")
        else:
            d = m.group(1).strip()
            descricoes[d].append(rel)
            if len(d) > 160:
                problemas.append(f"{rel}: description com {len(d)} caracteres")

        # 3. canonical e H1
        if not RE_CANON.search(html):
            problemas.append(f"{rel}: sem canonical")
        n_h1 = len(re.findall(r"<h1[\s>]", corpo))
        if n_h1 != 1:
            problemas.append(f"{rel}: {n_h1} H1 (esperado 1)")

        # 4. marcadores de rascunho
        for marca in ("Lorem ipsum", "PLACEHOLDER", "TODO:", "FIXME"):
            if marca in corpo:
                problemas.append(f"{rel}: contém '{marca}'")

    print("=" * 66)
    print("1. LINKS INTERNOS QUEBRADOS")
    print("=" * 66)
    if quebrados:
        for href in sorted(quebrados):
            origens = quebrados[href]
            print(f"  {href}")
            print(f"     citado em {len(origens)} página(s): {', '.join(origens[:3])}"
                  + (" ..." if len(origens) > 3 else ""))
    else:
        print("  nenhum")

    print()
    print("=" * 66)
    print("2. TITLES / DESCRIPTIONS DUPLICADOS")
    print("=" * 66)
    dup = False
    for t, arqs in titulos.items():
        if len(arqs) > 1:
            dup = True
            print(f"  TITLE repetido em {len(arqs)}: {t[:60]}")
            print(f"     {', '.join(arqs[:4])}")
    for d, arqs in descricoes.items():
        if len(arqs) > 1:
            dup = True
            print(f"  DESC repetida em {len(arqs)}: {d[:60]}")
            print(f"     {', '.join(arqs[:4])}")
    if not dup:
        print("  nenhum")

    print()
    print("=" * 66)
    print("3. OUTROS PROBLEMAS DE PÁGINA")
    print("=" * 66)
    print("\n".join(f"  {p}" for p in problemas) if problemas else "  nenhum")

    print()
    print("=" * 66)
    print("4. PÁGINAS ÓRFÃS (ninguém aponta para elas)")
    print("=" * 66)
    orfas = sorted(urls_existentes - apontadas - {"/"})
    print("\n".join(f"  {u}" for u in orfas) if orfas else "  nenhuma")

    print()
    print("=" * 66)
    print("5. SITEMAP")
    print("=" * 66)
    sm = os.path.join(RAIZ, "sitemap.xml")
    if os.path.exists(sm):
        locs = set(re.findall(r"<loc>([^<]+)</loc>", open(sm, encoding="utf-8").read()))
        urls_sm = {u[len(BASE):] or "/" for u in locs}
        faltando = sorted(urls_existentes - urls_sm)
        sobrando = sorted(urls_sm - urls_existentes)
        print(f"  URLs no sitemap: {len(urls_sm)} | páginas no site: {len(urls_existentes)}")
        if faltando:
            print(f"  FORA do sitemap ({len(faltando)}):")
            for u in faltando[:40]:
                print(f"    {u}")
        if sobrando:
            print(f"  no sitemap mas SEM arquivo ({len(sobrando)}):")
            for u in sobrando[:20]:
                print(f"    {u}")
        if not faltando and not sobrando:
            print("  sitemap em dia")

    print()
    total_problemas = len(quebrados) + len(problemas)
    print(f"RESUMO: {len(todas)} páginas | {len(quebrados)} links quebrados | "
          f"{len(problemas)} problemas de página")
    return 1 if total_problemas else 0


if __name__ == "__main__":
    sys.exit(main())
