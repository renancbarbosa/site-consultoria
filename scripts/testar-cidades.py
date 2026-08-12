# -*- coding: utf-8 -*-
"""
Guard-rails da poda do cluster de cidades (decisão de 12/08/2026).

Uso:  python scripts/testar-cidades.py
Sai com código 1 se qualquer verificação falhar. Rode antes de publicar.

O que ele impede de acontecer de novo:
  1. página da lista noindex sem a meta robots  -> volta ao índice sem querer
  2. página indexável com noindex               -> some do índice sem querer
  3. página noindex dentro do sitemap           -> sinal contraditório ao Google
  4. página indexável fora do sitemap           -> deixa de ser recomendada
  5. cidade nova indexável sem autorização      -> expansão silenciosa
  6. colisão Palmas/TO x Palmas/PR              -> dado errado na página errada
  7. lista do doc diferente da lista do código  -> duas fontes de verdade
  8. robots.txt bloqueando as podadas           -> Google nunca leria o noindex
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.join(AQUI, "..")

from rcb_cidades import INDEXAVEIS, PILOTO, SLUG_CANONICO, eh_indexavel  # noqa: E402

CIDADES_DIR = os.path.join(RAIZ, "consultoria-seo")
SITEMAP = os.path.join(RAIZ, "sitemap.xml")
DOC = os.path.join(RAIZ, "docs", "decisao-cidades-2026-08-12.md")
PREFIXO = "https://rcbseo.com.br/consultoria-seo/"

erros = []


def falha(msg):
    erros.append(msg)


def publicadas():
    return sorted(
        d for d in os.listdir(CIDADES_DIR)
        if os.path.isdir(os.path.join(CIDADES_DIR, d))
        and os.path.exists(os.path.join(CIDADES_DIR, d, "index.html"))
    )


def html_de(slug):
    with open(os.path.join(CIDADES_DIR, slug, "index.html"), encoding="utf-8") as f:
        return f.read()


def meta_robots(html):
    m = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html, re.I)
    return m.group(1).strip().lower() if m else None


def teste_1_e_2_meta_robots(slugs):
    for slug in slugs:
        robots = meta_robots(html_de(slug))
        if robots is None:
            falha(f"[1] /consultoria-seo/{slug}/ nao tem meta robots nenhuma.")
            continue
        tem_noindex = "noindex" in robots
        if eh_indexavel(slug) and tem_noindex:
            falha(f"[2] /consultoria-seo/{slug}/ e INDEXAVEL mas esta com noindex ({robots}).")
        if not eh_indexavel(slug) and not tem_noindex:
            falha(f"[1] /consultoria-seo/{slug}/ deveria ter noindex e esta como '{robots}'.")
        # nofollow foi decisao explicita de NAO usar: os links continuam valendo
        # e o Google precisa seguir rastreando a pagina para reler a tag.
        if "nofollow" in robots:
            falha(f"[1] /consultoria-seo/{slug}/ usa nofollow — a decisao foi noindex sem nofollow.")


def teste_3_e_4_sitemap(slugs):
    xml = open(SITEMAP, encoding="utf-8").read()
    no_sitemap = {
        u[len(PREFIXO):].rstrip("/")
        for u in re.findall(r"<loc>([^<]+)</loc>", xml)
        if u.startswith(PREFIXO) and u != PREFIXO
    }
    for slug in slugs:
        if not eh_indexavel(slug) and slug in no_sitemap:
            falha(f"[3] /consultoria-seo/{slug}/ tem noindex e MESMO ASSIM esta no sitemap.")
        if eh_indexavel(slug) and slug not in no_sitemap:
            falha(f"[4] /consultoria-seo/{slug}/ e indexavel e esta FORA do sitemap.")
    esperado = len([s for s in slugs if eh_indexavel(s)])
    if len(no_sitemap) != esperado:
        falha(f"[3/4] sitemap tem {len(no_sitemap)} cidades, esperado {esperado}.")


def teste_5_cidade_nova(slugs):
    desconhecidas = [s for s in INDEXAVEIS if s not in slugs]
    if desconhecidas:
        falha(f"[5] INDEXAVEIS aponta para cidade sem pasta publicada: {sorted(desconhecidas)}")
    # Qualquer pasta nova que apareca sem estar em INDEXAVEIS precisa nascer com
    # noindex — o teste 1 ja cobre isso. Aqui o alvo e a expansao silenciosa:
    # o total publicado so muda por decisao editorial.
    if len(slugs) != 199:
        falha(f"[5] o cluster tem {len(slugs)} paginas publicadas; a decisao de 12/08/2026 "
              f"fixou 199. Cidade nova exige decisao editorial e atualizacao de rcb_cidades.py.")


def teste_6_palmas(slugs):
    if SLUG_CANONICO.get(("palmas", "TO")) != "palmas":
        falha("[6] SLUG_CANONICO nao mapeia mais Palmas/TO para o slug `palmas`.")
    if "palmas-pr" in slugs:
        falha("[6] existe /consultoria-seo/palmas-pr/ publicada — Palmas/PR nao deve ter pagina.")
    if "palmas" not in slugs:
        falha("[6] /consultoria-seo/palmas/ sumiu.")
        return
    h = html_de("palmas")
    if "Tocantins" not in h and "(TO)" not in h:
        falha("[6] /consultoria-seo/palmas/ nao identifica o Tocantins — pode ter recebido dados de Palmas/PR.")
    if re.search(r"Palmas.{0,40}Paran[áa]", h) or "(PR)" in h:
        falha("[6] /consultoria-seo/palmas/ contem referencia a Palmas/PR.")


def _bloco(texto, nome):
    m = re.search(rf"<!-- RCB:CIDADES-{nome}:INICIO -->(.*?)<!-- RCB:CIDADES-{nome}:FIM -->",
                  texto, re.S)
    return set(re.findall(r"`([a-z0-9\-]+)`", m.group(1))) if m else None


def teste_7_doc_bate_com_codigo(slugs):
    """O documento e o codigo precisam dizer a MESMA coisa.

    Sem isto, a lista do doc vira uma segunda fonte de verdade e as duas
    divergem em silencio na primeira vez que alguem editar so uma delas.
    """
    if not os.path.exists(DOC):
        falha("[7] docs/decisao-cidades-2026-08-12.md nao existe — a decisao precisa estar registrada.")
        return
    texto = open(DOC, encoding="utf-8").read()

    doc_piloto = _bloco(texto, "PILOTO")
    doc_congeladas = _bloco(texto, "CONGELADAS")
    doc_noindex = _bloco(texto, "NOINDEX")
    for nome, valor in (("PILOTO", doc_piloto), ("CONGELADAS", doc_congeladas),
                        ("NOINDEX", doc_noindex)):
        if valor is None:
            falha(f"[7] bloco RCB:CIDADES-{nome} nao encontrado no documento.")
            return

    if doc_piloto != PILOTO:
        falha(f"[7] piloto: doc={sorted(doc_piloto)} != codigo={sorted(PILOTO)}")
    doc_indexaveis = doc_piloto | doc_congeladas
    if doc_indexaveis != INDEXAVEIS:
        so_doc = sorted(doc_indexaveis - INDEXAVEIS)
        so_cod = sorted(INDEXAVEIS - doc_indexaveis)
        falha(f"[7] indexaveis divergem — so no doc: {so_doc} | so no codigo: {so_cod}")

    noindex_real = {s for s in slugs if not eh_indexavel(s)}
    if doc_noindex != noindex_real:
        so_doc = sorted(doc_noindex - noindex_real)
        so_real = sorted(noindex_real - doc_noindex)
        falha(f"[7] noindex divergem — so no doc: {so_doc} | so no disco: {so_real}")


def teste_8_robots_txt():
    txt = open(os.path.join(RAIZ, "robots.txt"), encoding="utf-8").read()
    if re.search(r"^\s*Disallow:\s*/consultoria-seo", txt, re.M | re.I):
        falha("[8] robots.txt bloqueia /consultoria-seo/ — com Disallow o Google nunca le o "
              "noindex e a URL fica no indice. Remova o bloqueio.")


def main():
    slugs = publicadas()
    print(f"Cidades publicadas    : {len(slugs)}")
    print(f"Indexaveis esperadas  : {len(INDEXAVEIS)} (das quais {len(PILOTO)} piloto)")
    print(f"Com noindex esperadas : {len(slugs) - len(INDEXAVEIS)}")
    print()

    teste_1_e_2_meta_robots(slugs)
    teste_3_e_4_sitemap(slugs)
    teste_5_cidade_nova(slugs)
    teste_6_palmas(slugs)
    teste_7_doc_bate_com_codigo(slugs)
    teste_8_robots_txt()

    if erros:
        print(f"{len(erros)} ERRO(S):")
        for e in erros:
            print(f"  ERRO  {e}")
        return 1
    print("Todos os guard-rails passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
