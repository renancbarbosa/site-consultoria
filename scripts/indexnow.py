# -*- coding: utf-8 -*-
"""
Envia URLs ao IndexNow (Bing e mecanismos parceiros).

Uso:
  python scripts/indexnow.py --novas     # só as URLs da divisão de mercados competitivos
  python scripts/indexnow.py --sitemap   # todas as URLs do sitemap.xml
  python scripts/indexnow.py URL [URL…]  # URLs avulsas

IMPORTANTE: a chave abaixo já está publicada em
https://rcbseo.com.br/19341b29c6054af601879d85a34d62c5.txt desde 23/07/2026.
**Reutilizar sempre esta chave — não gerar outra.** Gerar uma nova exigiria
publicar outro arquivo e invalidaria o histórico de envios.

Envie somente depois de confirmar que as URLs estão no ar (HTTP 200). Avisar o
Bing sobre URL que ainda não subiu faz ele rastrear e encontrar 404.
"""
import json
import os
import re
import sys
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.path.insert(0, os.path.join(AQUI, "conteudo"))

from rcb_base import RAIZ, BASE_URL  # noqa: E402

CHAVE = "19341b29c6054af601879d85a34d62c5"
KEY_LOCATION = f"{BASE_URL}/{CHAVE}.txt"
HOST = "rcbseo.com.br"
ENDPOINT = "https://www.bing.com/indexnow"


def urls_da_divisao():
    import cluster_central, cluster_iptv, cluster_bets, cluster_dominios, pagina_analise
    import artigos_competitivo, artigos_estrategia, artigos_dominios
    import artigos_backlinks, artigos_iptv, artigos_bets

    urls = []
    for m in (cluster_central, cluster_iptv, cluster_bets, cluster_dominios, pagina_analise):
        for f in m.PAGINAS:
            urls.append(f"{BASE_URL}/" + f()[0].replace("index.html", ""))
    for m in (artigos_competitivo, artigos_estrategia, artigos_dominios,
              artigos_backlinks, artigos_iptv, artigos_bets):
        for a in m.ARTIGOS:
            urls.append(f"{BASE_URL}/blog/{a['slug']}/")
    return urls


def urls_do_sitemap():
    xml = open(os.path.join(RAIZ, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def enviar(urls):
    corpo = json.dumps({
        "host": HOST,
        "key": CHAVE,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT, data=corpo, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "RCB-IndexNow/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read().decode("utf-8", "replace")[:400]


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1

    if args[0] == "--novas":
        urls = urls_da_divisao()
        rotulo = "URLs da divisão de mercados competitivos"
    elif args[0] == "--sitemap":
        urls = urls_do_sitemap()
        rotulo = "URLs do sitemap"
    else:
        urls = args
        rotulo = "URLs informadas na linha de comando"

    print(f"{len(urls)} {rotulo}")
    print(f"Chave: {CHAVE} (publicada em {KEY_LOCATION})")
    print(f"Endpoint: {ENDPOINT}\n")

    status, resposta = enviar(urls)
    print(f"HTTP {status}")
    if resposta.strip():
        print(f"Resposta: {resposta}")
    if status in (200, 202):
        print("\nEnvio aceito. O Bing decide quando e se rastreia — não é indexação imediata.")
        return 0
    print("\nEnvio NÃO aceito. Conferir chave, keyLocation e formato das URLs.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
