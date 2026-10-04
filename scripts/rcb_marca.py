"""Leitor da ficha unica da marca (data/marca.json). Criado em 04/10/2026.

Todo script que escreve nome, contato, coordenadas ou links da marca importa daqui.
Mudou o nome da marca? Edite SO o data/marca.json.

    from rcb_marca import NOME, titulo, texto, no_empresa
"""
import json
import os
import re

_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(_RAIZ, "data", "marca.json"), encoding="utf-8") as _f:
    MARCA = json.load(_f)

NOME = MARCA["nome"]
ALTERNATIVOS = list(MARCA["nomes_alternativos"])
ID_EMPRESA = MARCA["id_empresa"]
ID_SITE = MARCA["id_site"]
URL = MARCA["url"]

# sufixo de titulo antigo -> marca atual ("... | RCB", "... | RCB Consultoria", "... — RCBSEO")
_SUFIXO = re.compile(r'(\s[|—–-]\s)(?:RCB Consultoria de SEO|RCB Consultoria|RCBSEO|RCB SEO|RCB)\s*$')

# nome da marca no meio do texto (nunca o servico generico "consultoria de SEO")
_NO_TEXTO = [
    (re.compile(r'RCB Consultoria de SEO'), NOME),
    (re.compile(r'RCB Consultoria'), NOME),
    (re.compile(r'\bRCBSEO\b'), NOME),
]


def titulo(t):
    """Garante o sufixo da marca atual no titulo. Nao encurta nada."""
    t = t.strip()
    if _SUFIXO.search(t):
        return _SUFIXO.sub(lambda m: m.group(1) + NOME, t)
    return t


def texto(s):
    """Troca o nome antigo da marca pelo atual num texto livre."""
    for rx, novo in _NO_TEXTO:
        s = rx.sub(novo, s)
    return s


_ALTERNATE = re.compile(r'"alternateName":\s*\[[^\]]*\]')


def texto_html(h):
    """texto() numa pagina inteira, sem mexer na lista alternateName do JSON-LD."""
    guardados = []

    def _guarda(m):
        guardados.append(m.group(0))
        return "\x00%d\x00" % (len(guardados) - 1)
    h = _ALTERNATE.sub(_guarda, h)
    h = texto(h)
    return re.sub(r'\x00(\d+)\x00', lambda m: guardados[int(m.group(1))], h)


def referencia(tipo="Organization"):
    """No curto que aponta para a empresa (publisher, provider, author)."""
    return {"@type": tipo, "@id": ID_EMPRESA, "name": NOME, "url": URL}


def site():
    return {"@type": "WebSite", "@id": ID_SITE, "name": NOME, "url": URL}


def extras_empresa():
    """Propriedades que todo no principal da empresa deve carregar."""
    return {
        "name": NOME,
        "alternateName": ALTERNATIVOS,
        "geo": {"@type": "GeoCoordinates",
                "latitude": MARCA["geo"]["latitude"],
                "longitude": MARCA["geo"]["longitude"]},
        "hasMap": MARCA["perfil_google"],
        "sameAs": list(MARCA["sameAs"]) + ([MARCA["linkedin_empresa"]] if MARCA.get("linkedin_empresa") else []),
    }


def no_empresa():
    """No completo da empresa (sem preco, sem garantia, sem CNPJ)."""
    n = {"@type": ["ProfessionalService", "LocalBusiness"], "@id": ID_EMPRESA, "url": URL,
         "telephone": MARCA["telefone"], "email": MARCA["email"],
         "address": dict({"@type": "PostalAddress"}, **MARCA["endereco"]),
         "founder": {"@id": MARCA["fundador"]["id"]}}
    n.update(extras_empresa())
    return n
