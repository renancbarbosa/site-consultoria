"""Titulos e descricoes novos para as 5 paginas que ja estao na 1a pagina do Google
e quase nao recebem clique (Search Console, 28 dias ate 20/11/2026).

Troca: <title>, meta description, og:title/description, twitter:title/description e,
no JSON-LD, qualquer "name"/"headline"/"description" que fosse igual ao title ou a
description antigos. H1 e URL nao mudam. Idempotente: 2a execucao diz "alteradas: 0".
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

NOVOS = {
    "consultoria-seo-local": (
        "Consultoria de SEO Local: Consultor Direto, Cases Reais | RCB SEO",
        "Consultor de SEO local direto, sem agência: um cliente saiu da 2ª para a 1ª página "
        "do Google e outro teve +180% de aparições. Orçamento grátis em 24h.",
    ),
    "seo-para-clinicas-de-estetica": (
        "SEO para Clínica de Estética: Apareça Quando a Paciente Busca",
        "Consultoria de SEO para clínica de estética: apareça no Google e no Maps quando a "
        "paciente pesquisa o procedimento. Veja cases reais e peça orçamento grátis.",
    ),
    "seo-para-imobiliarias": (
        "Marketing Imobiliário e SEO para Imobiliária: Contato sem Portal",
        "SEO para imobiliária e corretor: seus imóveis aparecem no Google e o contato chega "
        "direto no seu WhatsApp, sem pagar portal por cada contato. Orçamento grátis.",
    ),
    "google-perfil-empresa": (
        "Otimização do Perfil da Empresa no Google: Case 1º no Maps",
        "Otimização do Perfil da Empresa no Google (Google Meu Negócio): uma confeitaria "
        "chegou ao 1º lugar no Maps com 4 avaliações, à frente de quem tinha 312.",
    ),
    "blog/consultor-seo-ou-fazer-sozinho-checklist": (
        "Consultor de SEO ou Fazer Sozinho? Checklist e Sinais de Alerta",
        "Contratou consultor de SEO há meses e não viu resultado? Ou está em dúvida se faz "
        "sozinho? Checklist simples para decidir e os sinais de que algo está errado.",
    ),
}

DASH = re.compile("[–—]")


def meta(html, attr, nome, valor):
    pad = re.compile(r'(<meta\s+' + attr + r'="' + re.escape(nome) + r'"\s+content=")[^"]*(")')
    if not pad.search(html):
        sys.exit(f"meta {nome} nao encontrada")
    return pad.sub(lambda m: m.group(1) + valor + m.group(2), html, count=1)


def main():
    alteradas = 0
    for slug, (titulo, desc) in NOVOS.items():
        assert len(titulo) <= 65, (slug, len(titulo))
        assert len(desc) <= 160, (slug, len(desc))
        assert not DASH.search(titulo + desc), slug
        arq = RAIZ / slug / "index.html"
        html = arq.read_text(encoding="utf-8")
        antes = html
        t_velho = re.search(r"<title>([^<]*)</title>", html).group(1)
        d_velha = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html).group(1)
        html = html.replace(f"<title>{t_velho}</title>", f"<title>{titulo}</title>", 1)
        html = meta(html, "name", "description", desc)
        for nome, valor in (("og:title", titulo), ("og:description", desc)):
            html = meta(html, "property", nome, valor)
        for nome, valor in (("twitter:title", titulo), ("twitter:description", desc)):
            html = meta(html, "name", nome, valor)
        # JSON-LD: so troca campo que era copia exata do title/description antigos
        for velho, novo in ((t_velho, titulo), (d_velha, desc)):
            if velho != novo:
                for chave in ("name", "headline", "description"):
                    html = html.replace(f'"{chave}": "{velho}"', f'"{chave}": "{novo}"')
                    html = html.replace(f'"{chave}":"{velho}"', f'"{chave}":"{novo}"')
        for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            json.loads(bloco)
        if html != antes:
            arq.write_text(html, encoding="utf-8", newline="")
            alteradas += 1
            print(f"{slug}: {len(titulo)} / {len(desc)} caracteres")
    print(f"alteradas: {alteradas}")


if __name__ == "__main__":
    main()
