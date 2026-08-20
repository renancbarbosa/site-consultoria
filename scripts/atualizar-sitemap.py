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
from rcb_cidades import eh_indexavel  # noqa: E402

HOJE = "2026-08-20"
SITEMAP = os.path.join(RAIZ, "sitemap.xml")

# URLs cujo conteúdo mudou nesta rodada. Manter a lista explícita evita o erro
# antigo de usar a data do deploy em todas as páginas do site e, ao mesmo tempo,
# impede que uma URL realmente revisada continue com lastmod obsoleto.
ATUALIZADAS = {
    "/blog/como-aparecer-no-google-maps/",
    "/blog/como-divulgar-minha-empresa-em-goiania/",
    "/blog/como-divulgar-minha-empresa-no-google/",
    "/blog/como-receber-orcamentos-whatsapp-site/",
    "/blog/quanto-custa-otimizar-google-meu-negocio/",
    "/blog/quanto-tempo-demora-seo-local/",
    "/blog/quanto-tempo-leva-seo-local-clinicas/",
    "/blog/",
    "/blog/como-aparecer-nas-buscas-perto-de-mim/",
    "/blog/como-aparecer-no-google-sem-pagar/",
    "/blog/dominio-caiu-o-que-fazer/",
    "/blog/por-que-minha-empresa-nao-aparece-no-google/",
    "/blog/seo-para-empresas-locais/",
    "/blog/vale-a-pena-seo-para-pequena-empresa/",
    "/cases/",
    "/como-aparecer-no-google/",
    "/para-comercios-locais/",
    "/google-perfil-empresa/",
    "/seo-local-goiania/",
    "/seo-para-clinicas-de-estetica/",
    "/seo-para-pequenas-empresas/",
    "/sobre/",
}

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

    # Poda de 12/08/2026: as cidades com noindex NAO entram no sitemap. Sem este
    # filtro, este script veria 199 pastas no disco e devolveria as 168 podadas
    # para o sitemap na primeira execucao -- desfazendo a decisao em silencio.
    podadas = {
        u for u in urls
        if u.startswith("/consultoria-seo/") and u != "/consultoria-seo/"
        and not eh_indexavel(u[len("/consultoria-seo/"):].rstrip("/"))
    }
    return urls - EXCLUIR - podadas


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

    atualizados = 0
    for url in ATUALIZADAS:
        absoluta = BASE_URL + url
        padrao = rf"(<loc>{re.escape(absoluta)}</loc>\s*<lastmod>)[^<]+"
        novo_xml, n = re.subn(padrao, lambda m: m.group(1) + HOJE, xml, count=1)
        if n and novo_xml != xml:
            atualizados += 1
        xml = novo_xml

    if not novas and not sumiram and not atualizados:
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
    print(f"Sitemap atualizado: +{len(novas)} URLs, {atualizados} lastmod corrigidos (total: {total}).")
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
