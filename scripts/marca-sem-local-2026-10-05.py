"""Marca so "RCB SEO", sem "Local" (pedido do Renan, 05/10/2026). Idempotente: 2a execucao = 0 alterados.

1. Nome alternativo da empresa (JSON-LD, marca.json, llms.txt): fica SO "RCB Consultoria", porque o perfil
   no Google Maps ainda se chama "RCB Consultoria - SEO Local e Google Meu Negocio" e o alternateName liga
   o site a esse perfil. Saem "RCB SEO Local" e "RCBSEO". Se o perfil for renomeado, tirar tambem.
2. Cargo do Renan (rodape, jobTitle e geradores): "Consultor de SEO Local e Google Meu Negocio" ->
   "Consultor de SEO e Google Meu Negocio"; o jobTitle "Consultor de SEO Local" do /sobre/ idem.
3. /sobre/: twitter:title "| RCB SEO Local" -> "| RCB SEO".
4. site.webmanifest: "RCB Consultoria de SEO" -> "RCB SEO".
O logo ("SEO Local" -> "SEO") foi trocado antes, na mesma rodada.

NAO mexe: "Consultor de SEO Local em Goiania" (termo de busca de /consultor-seo-goiania/, /sobre/ e
/contato/) e os campos ocultos do formulario da home (assunto do e-mail, decisao do Renan).

    python scripts/marca-sem-local-2026-10-05.py
"""
import glob
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORA = ("node_modules", "graphify-out", "Projetos", "reports", "docs", ".playwright-mcp")

CARGO_VELHO = "Consultor de SEO Local e Google Meu Negócio"
CARGO_NOVO = "Consultor de SEO e Google Meu Negócio"
ALT = re.compile(r'"alternateName":(\s*)\[\s*"RCB Consultoria",\s*"RCB SEO Local",\s*"RCBSEO"\s*\]')


def ler(p):
    return io.open(p, encoding="utf-8", newline="").read()


def gravar(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def html(s):
    s = ALT.sub(lambda m: '"alternateName":%s["RCB Consultoria"]' % m.group(1), s)
    s = s.replace(CARGO_VELHO, CARGO_NOVO)
    s = s.replace('"jobTitle": "Consultor de SEO Local"', '"jobTitle": "%s"' % CARGO_NOVO)
    s = s.replace('content="Sobre Renan Carvalho Barbosa | RCB SEO Local"',
                  'content="Sobre Renan Carvalho Barbosa | RCB SEO"')
    return s


def main():
    alterados = []
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)
             if not os.path.relpath(p, RAIZ).replace("\\", "/").startswith(FORA)]
    alvos += [os.path.join(RAIZ, "scripts", f) for f in ("rcb_base.py", "gerar-paginas-cidades.py")]
    for p in alvos:
        s = ler(p)
        n = html(s)
        if n != s:
            gravar(p, n)
            alterados.append(p)

    # marca.json (fonte unica lida por scripts/rcb_marca.py)
    p = os.path.join(RAIZ, "data", "marca.json")
    s = ler(p)
    d = json.loads(s)
    if d["nomes_alternativos"] != ["RCB Consultoria"]:
        n = s.replace('"nomes_alternativos": ["RCB Consultoria", "RCB SEO Local", "RCBSEO"]',
                      '"nomes_alternativos": ["RCB Consultoria"]')
        assert n != s, "marca.json: formato inesperado"
        gravar(p, n)
        alterados.append(p)

    # llms.txt
    p = os.path.join(RAIZ, "llms.txt")
    s = ler(p)
    n = s.replace("Também conhecida como: RCB Consultoria, RCB SEO Local, RCBSEO.",
                  "Também aparece como RCB Consultoria (nome atual do perfil no Google Maps).")
    n = n.replace("consultor de SEO Local e Google Meu Negócio", "consultor de SEO e Google Meu Negócio")
    if n != s:
        gravar(p, n)
        alterados.append(p)

    # site.webmanifest
    p = os.path.join(RAIZ, "site.webmanifest")
    s = ler(p)
    n = s.replace('"name": "RCB Consultoria de SEO"', '"name": "RCB SEO"')
    if n != s:
        gravar(p, n)
        alterados.append(p)

    print("alterados: %d" % len(alterados))


if __name__ == "__main__":
    main()
