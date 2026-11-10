# -*- coding: utf-8 -*-
"""/consultor-seo-goiania/ (PROTEGIDA): ajustes da auditoria de 09/11/2026, item 9.

Autorizacao: o Renan pediu em 09/11/2026 "pode fazer tudo [...] sem me perguntar" sobre a lista
da auditoria, que incluia este item; e avisou que revisa antes de publicar. Por isso fica em
commit proprio: da para desfazer so ele.

O que muda (e SO isto; titulo, H1, textos, canonical e links recebidos ficam como estao):
  1. Fonte: as 5 linhas do Google Fonts viram o preload da fonte do proprio site (igual as outras
     187 paginas desde 29/10/2026). No Lighthouse ela era a pagina mais lenta (LCP 5,1 s).
  2. Ficha tecnica (JSON-LD): a empresa usava o @id ".../consultor-seo-goiania/#business" e a url
     da pagina, como se fosse uma segunda empresa. Passa a ser a mesma do site inteiro
     (data/marca.json: id_empresa, url, sameAs). Nome, endereco, telefone e mapa ja eram iguais.
  3. Rodape local (Ligar, Google Maps, Avaliar, horario) e o item "Google Meu Negocio em Goiania"
     no menu e no rodape, iguais as outras paginas.
Idempotente.
"""
import importlib.util
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import rcb_menu  # noqa: E402


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, os.path.join(AQUI, arq))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


FONTE = _mod("fonte", "fonte-local-2026-10-29.py")
LIGAR = _mod("ligar", "ligar-gmn-goiania-2026-11-09.py")
ARQ = os.path.join(RAIZ, "consultor-seo-goiania", "index.html")
ID_VELHO = "https://rcbseo.com.br/consultor-seo-goiania/#business"


def marca():
    with io.open(os.path.join(RAIZ, "data", "marca.json"), encoding="utf-8") as f:
        return json.load(f)


def schema(h):
    m = marca()

    def troca(bloco):
        txt = bloco.group(1)
        if ID_VELHO not in txt:
            return bloco.group(0)
        j = json.loads(txt)
        for n in j.get("@graph", [j]):
            if n.get("@id") == ID_VELHO:
                n["@id"] = m["id_empresa"]
                n["url"] = m["url"]
                n["sameAs"] = list(dict.fromkeys(list(n.get("sameAs", [])) + m["sameAs"]))
        novo = json.dumps(j, ensure_ascii=False, indent=2).replace(ID_VELHO, m["id_empresa"])
        return bloco.group(0).replace(txt, novo)

    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', troca, h, flags=re.S)


def main():
    raw = io.open(ARQ, encoding="utf-8", newline="").read()
    h = FONTE.BLOCO.sub(FONTE.PRELOAD, raw)
    h = schema(h)
    antes_menu = h
    h, _ok = LIGAR.menu_e_rodape(h)
    # a protegida ficou de fora em 29/10/2026 e nunca recebeu "SEO para IA" no menu e no rodape;
    # entram junto. Trava: fora estes 4 itens, nada pode mudar.
    permitidos = [LIGAR.ITEM_MENU, LIGAR.ITENS_RODAPE[1],
                  '<a href="/seo-para-ia/" class="nav-dropdown-item" role="menuitem">SEO para IA (ChatGPT e Gemini)</a>',
                  '<a href="/seo-para-ia/">SEO para IA</a>']
    conferir = h
    for it in permitidos:
        if it not in antes_menu:
            conferir = conferir.replace(it, "", 1)
    assert conferir == antes_menu, "menu/rodape da protegida difere alem dos itens permitidos"
    h = rcb_menu.rodape_local(h)
    assert h.lstrip().lower().startswith("<!doctype")
    assert "fonts.googleapis.com" not in h, "sobrou Google Fonts"
    assert ID_VELHO not in h
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        json.loads(b)
    if h != raw:
        io.open(ARQ, "w", encoding="utf-8", newline="").write(h)
        print("consultor-seo-goiania: alterada")
    else:
        print("consultor-seo-goiania: sem mudanca")


if __name__ == "__main__":
    main()
