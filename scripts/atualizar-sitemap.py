# -*- coding: utf-8 -*-
"""
Atualiza o sitemap.xml com as URLs da divisão nova.

Uso:  python scripts/atualizar-sitemap.py

Preserva as entradas existentes exatamente como estão (lastmod, changefreq e
priority já ajustados em rodadas anteriores) e só acrescenta o que falta,
mantendo a ordem: primeiro o que já existia, depois as URLs novas agrupadas.

Não inclui 404.html nem páginas de exemplo.
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from rcb_base import RAIZ, BASE_URL  # noqa: E402

HOJE = "2026-08-06"
SITEMAP = os.path.join(RAIZ, "sitemap.xml")

EXCLUIR = {"/404.html", "/diagnostico-presenca-digital/exemplo/"}

# Prioridade por tipo de URL nova. Os pilares de cluster recebem o mesmo peso
# das páginas de nicho já consolidadas (0.95).
PILARES = {
    "/seo-para-mercados-competitivos/",
    "/seo-nacional/",
    "/seo-para-iptv/",
    "/seo-para-bets/",
}


def paginas_do_site():
    urls = set()
    ignorar = {"node_modules", "graphify-out", "Projetos", ".git", "docs", "scripts"}
    for pasta, subs, arqs in os.walk(RAIZ):
        subs[:] = [s for s in subs if s not in ignorar]
        for nome in arqs:
            if not nome.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(pasta, nome), RAIZ).replace("\\", "/")
            if rel == "index.html":
                urls.add("/")
            elif rel.endswith("/index.html"):
                urls.add("/" + rel[: -len("index.html")])
            else:
                urls.add("/" + rel)
    return urls - EXCLUIR


def prioridade(url):
    if url in PILARES:
        return "0.95", "monthly"
    if url.startswith("/blog/"):
        return "0.7", "monthly"
    return "0.9", "monthly"


def main():
    xml = open(SITEMAP, encoding="utf-8").read()
    existentes = set(re.findall(r"<loc>([^<]+)</loc>", xml))
    existentes_rel = {u[len(BASE_URL):] or "/" for u in existentes}

    do_site = paginas_do_site()
    novas = sorted(do_site - existentes_rel)
    sumiram = sorted(existentes_rel - do_site)

    if not novas and not sumiram:
        print("Sitemap já está em dia.")
        return

    blocos = []
    for url in novas:
        pri, freq = prioridade(url)
        blocos.append(f"""  <url>
    <loc>{BASE_URL}{url}</loc>
    <lastmod>{HOJE}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""")

    if blocos:
        xml = xml.replace("</urlset>", "\n".join(blocos) + "\n</urlset>")

    with open(SITEMAP, "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)

    total = len(re.findall(r"<loc>", xml))
    print(f"Sitemap atualizado: +{len(novas)} URLs (total: {total}).")
    comerciais = [u for u in novas if not u.startswith("/blog/")]
    artigos = [u for u in novas if u.startswith("/blog/")]
    print(f"  páginas comerciais: {len(comerciais)}")
    print(f"  artigos do blog   : {len(artigos)}")
    if sumiram:
        print(f"\n  ATENÇÃO — no sitemap mas sem arquivo no site ({len(sumiram)}):")
        for u in sumiram:
            print(f"    {u}")


if __name__ == "__main__":
    main()
