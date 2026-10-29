# -*- coding: utf-8 -*-
"""
Fase 3 do pilar SEO para IA (29/10/2026): a ficha do Renan (Person #renan) igual em todo o site.

  1. knowsAbout: a lista única de data/marca.json (fundador.knowsAbout) em toda página que já
     descreve o Renan com knowsAbout (home, /sobre/ e 9 páginas de nicho). Antes eram 3 listas
     diferentes; agora entram GEO, AEO e otimização para IA generativa.
  2. sameAs do Renan: o de data/marca.json (fundador.sameAs). Nas páginas que não tinham, entra;
     no /sobre/, sai o Instagram (é da empresa, já está no nó #business).
  3. Home: o OfferCatalog #pacotes ganha a oferta "SEO para IA" (sem preço), apontando para o pilar.
  4. Publisher dos artigos do blog: sameAs completo da empresa onde só havia o YouTube.

Edita só o trecho do JSON-LD, sem regravar o bloco inteiro: o resto da formatação de cada página
fica como está. /consultor-seo-goiania/ fica de fora (protegida). Idempotente.
Sem argumento só relata; --aplicar grava.
"""
import glob
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
APLICAR = "--aplicar" in sys.argv
PROTEGIDA = os.path.join("consultor-seo-goiania", "index.html")
FORA = ("node_modules", "docs", "scripts", "graphify-out", "Projetos", "reports", "data", ".playwright-mcp")

MARCA = json.load(io.open(os.path.join(RAIZ, "data", "marca.json"), encoding="utf-8"))
SABE = MARCA["fundador"]["knowsAbout"]
SAME = MARCA["fundador"]["sameAs"]
ID = MARCA["fundador"]["id"]

OFERTA_IA = {
    "@type": "Offer",
    "name": "SEO para IA (ChatGPT, Gemini e Google com IA)",
    "description": "Deixar a empresa fácil de achar, entender e indicar nas respostas escritas por inteligência "
                   "artificial, começando por uma auditoria pronta em 1 a 3 dias úteis. Sem promessa de ser citado.",
    "availability": "https://schema.org/InStock",
    "url": "https://rcbseo.com.br/seo-para-ia/",
    "itemOffered": {"@type": "Service", "name": "SEO para IA (GEO e AEO)",
                    "provider": {"@id": MARCA["id_empresa"]}},
}


def fecha(t, i):
    """Índice logo depois do ] que fecha o [ em t[i] (os textos das listas não têm colchete)."""
    n = 0
    for j in range(i, len(t)):
        n += {"[": 1, "]": -1}.get(t[j], 0)
        if n == 0:
            return j + 1
    raise ValueError("colchete sem par")


def lista(valor, recuo, multilinha):
    """Lista JSON no mesmo estilo (uma linha só ou um item por linha) do trecho que substitui."""
    if not multilinha:
        return json.dumps(valor, ensure_ascii=False)
    linhas = json.dumps(valor, ensure_ascii=False, indent=2).split("\n")
    return "\n".join(linhas[:1] + [recuo + x for x in linhas[1:]])


def troca_lista(b, ini, valor, recuo):
    """Troca a lista JSON da chave que começa em b[ini]."""
    a = b.index("[", ini)
    f = fecha(b, a)
    return b[:a] + lista(valor, recuo, "\n" in b[a:f]) + b[f:]


def pessoa(b):
    """knowsAbout e sameAs do nó #renan. As chaves do nó são as linhas com o mesmo recuo do knowsAbout."""
    k = b.find('"knowsAbout"')  # só o nó do Renan tem knowsAbout nestes blocos
    if k == -1:
        return b
    linha = b.rfind("\n", 0, k) + 1
    recuo = b[linha:k]
    assert recuo.strip() == "", "knowsAbout fora do padrão: " + b[linha:k + 40]
    b = troca_lista(b, k, SABE, recuo)
    # o nó vai da { até a } com um nível a menos de recuo; o sameAs pode vir antes ou depois do knowsAbout
    ini_no = b.rfind("\n" + recuo[:-2] + "{", 0, k)
    fim_no = b.find("\n" + recuo[:-2] + "}", k)
    s = b.find("\n" + recuo + '"sameAs"', ini_no, fim_no)
    if s != -1:
        return troca_lista(b, s + 1 + len(recuo), SAME, recuo)
    fim_k = fecha(b, b.index("[", k))
    return b[:fim_k] + ",\n" + recuo + '"sameAs": ' + lista(SAME, recuo, True) + b[fim_k:]


def catalogo(b):
    if '"@id": "https://rcbseo.com.br/#pacotes"' not in b or OFERTA_IA["url"] in b:
        return b
    c = b.index('"@id": "https://rcbseo.com.br/#pacotes"')
    i = b.index('"itemListElement"', c)
    f = fecha(b, b.index("[", i))
    recuo = b[b.rfind("\n", 0, i) + 1:i]
    item = json.dumps(OFERTA_IA, ensure_ascii=False, indent=2).split("\n")
    item = "\n".join(recuo + "  " + x for x in item)
    return b[:f - 1].rstrip() + ",\n" + item + "\n" + recuo + b[f - 1:]


def publisher(b):
    """21 artigos do blog ficaram com o publisher RCB SEO só com o YouTube no sameAs (commit 28601dae
    criou a lista onde não havia). Vira a lista completa do marca.json."""
    so_yt = '"url":"%s","sameAs":["%s"]}' % (MARCA["url"], MARCA["sameAs"][-1])
    return b.replace(so_yt, '"url":"%s","sameAs":%s}' % (MARCA["url"], json.dumps(MARCA["sameAs"], separators=(",", ":"))))


BLOCO = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)


def main():
    os.chdir(RAIZ)
    alteradas = []
    for f in sorted(glob.glob("**/index.html", recursive=True)):
        if f.startswith(FORA) or os.path.normpath(f) == PROTEGIDA:
            continue
        h = io.open(f, encoding="utf-8").read()
        if ID not in h:
            continue

        def um(m):
            b = publisher(m.group(2))
            if ID in b and "knowsAbout" in b:
                b = pessoa(b)
            if f == "index.html":
                b = catalogo(b)
            json.loads(b)  # JSON quebrado para aqui
            return m.group(1) + b + m.group(3)

        novo = BLOCO.sub(um, h)
        if novo != h:
            assert novo.lstrip().lower().startswith("<!doctype"), f
            alteradas.append(f)
            if APLICAR:
                io.open(f, "w", encoding="utf-8", newline="").write(novo)
    print("%s: %d" % ("alteradas" if APLICAR else "seriam alteradas", len(alteradas)))
    for f in alteradas:
        print("  ", f)


if __name__ == "__main__":
    main()
