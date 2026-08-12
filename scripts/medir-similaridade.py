# -*- coding: utf-8 -*-
"""
Mede similaridade palavra a palavra entre páginas de cidade.

Uso:  python scripts/medir-similaridade.py

Mesma metodologia do raio-X de 11/08/2026 que apurou 89,5% entre Aracaju e
Botucatu: extrai o texto visível (sem script/style/tags), tokeniza em palavras e
compara com difflib.SequenceMatcher.

O par Aracaju x Botucatu é recalculado a cada execução como controle — se ele
sair muito longe de 89,5%, a metodologia mudou e os demais números não são
comparáveis com o histórico.
"""
import difflib
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.join(AQUI, "..")
CIDADES = os.path.join(RAIZ, "consultoria-seo")


def texto_visivel(slug):
    with open(os.path.join(CIDADES, slug, "index.html"), encoding="utf-8") as f:
        h = f.read()
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<svg.*?</svg>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    h = re.sub(r"&[a-z]+;|&#\d+;", " ", h)
    return h


def palavras(slug):
    return re.findall(r"\w+", texto_visivel(slug).lower(), flags=re.UNICODE)


def similaridade(a, b):
    pa, pb = palavras(a), palavras(b)
    return difflib.SequenceMatcher(None, pa, pb).ratio() * 100


def main():
    pares_piloto = [
        ("rio-de-janeiro", "campinas"),
        ("rio-de-janeiro", "palmas"),
        ("campinas", "palmas"),
    ]
    # cada piloto contra uma cidade antiga que ficou no grupo noindex
    pares_contra_antiga = [
        ("rio-de-janeiro", "aracaju"),
        ("campinas", "botucatu"),
        ("palmas", "araguaina"),
    ]
    controle = ("aracaju", "botucatu")

    print("CONTROLE — duas cidades do template antigo")
    r = similaridade(*controle)
    print(f"  {controle[0]:<18} x {controle[1]:<18} {r:6.1f}%")
    if not (80 <= r <= 95):
        print("  ATENCAO: fora da faixa esperada (~89,5%). Metodologia pode ter mudado.")
    print()

    print("PILOTO x PILOTO")
    for a, b in pares_piloto:
        print(f"  {a:<18} x {b:<18} {similaridade(a, b):6.1f}%")
    print()

    print("PILOTO x CIDADE ANTIGA (noindex)")
    for a, b in pares_contra_antiga:
        print(f"  {a:<18} x {b:<18} {similaridade(a, b):6.1f}%")
    print()

    n = {s: len(palavras(s)) for s in
         ["rio-de-janeiro", "campinas", "palmas", "aracaju", "botucatu"]}
    print("PALAVRAS POR PAGINA (texto visivel, inclui navbar/rodape/precos)")
    for s, q in n.items():
        print(f"  {s:<18} {q:>6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
