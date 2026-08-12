# -*- coding: utf-8 -*-
"""
Conferencia do site depois da rodada de conversao de 09/08/2026.

Roda sobre TODAS as paginas e checa: HTML balanceado, JSON-LD valido, links
internos e ancoras que existem, preco coerente entre texto e ficha do Google,
barra de CTA no celular, menu novo e ausencia de jargao e de frases que
contradizem o preco publicado.

Uso:  python scripts/conferir-conversao.py
"""
import glob
import json
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
os.chdir(RAIZ)

sys.path.insert(0, str(RAIZ / "scripts"))
from rcb_pacotes import PACOTES, MARCA_INI, MARCA_FIM  # noqa: E402

# Fonte unica: o que a tabela e a ficha do Google TEM que dizer. Mudou o preco
# no rcb_pacotes.py? Esta conferencia acompanha sozinha, sem editar nada aqui.
VALORES_ESPERADOS = {p["valor"] for p in PACOTES}   # "R$ 1.997"
PRECOS_ESPERADOS = {p["preco"] for p in PACOTES}    # "1997.00"

JARGAO = ["GMB", "on-page", "metadescri", "arquitetura de informa",
          "ticket médio", "métricas de vaidade", "escopo enxuto"]
CONTRADICAO = ["investimento depende", "faixas de investimento",
               "proposta personalizada", "não existe preço de tabela"]

SEM_NAVBAR = {"404.html", "diagnostico-presenca-digital/exemplo/index.html",
              "privacidade/index.html", "cookies/index.html"}

# Demo do relatorio de diagnostico: o HTML dela e montado por JavaScript, entao
# contar tag aberta/fechada no arquivo nao faz sentido. E noindex e fora do
# sitemap de proposito - ver CLAUDE.md.
FORA_DA_CONFERENCIA = {"diagnostico-presenca-digital/exemplo/index.html"}

problemas = []
stats = {"paginas": 0, "com_precos": 0, "com_barra": 0, "com_menu_novo": 0}


def precos_do_bloco(html):
    """Preco que o VISITANTE le, extraido so de dentro dos marcadores.

    Procurar 'R$ 1.997' no arquivo inteiro nao serve: o FAQ e a meta description
    tambem citam os valores, entao a tabela podia estar congelada num preco
    velho e a conferencia dizer que estava tudo bem.

    Devolve (valores, erro). Se um dos marcadores faltar, valores e None e erro
    explica qual faltou — nunca silencia.
    """
    i = html.find(MARCA_INI)
    f = html.find(MARCA_FIM)

    if i == -1 and f == -1:
        # A home escreve a tabela a mao, sem marcadores — ela saiu da lista do
        # aplicar-conversao.py em 09/08/2026 justamente porque o script injetava
        # uma segunda copia. Sem marcador, mas a tabela existe: confere pelos
        # limites da secao. Nao da para deixar de fora — foi nela que duplicou.
        s = html.find('id="pacotes"')
        if s == -1:
            return None, None                 # pagina sem tabela: normal
        fim = html.find("</section>", s)
        if fim == -1:
            return None, 'tem id="pacotes" mas a secao nunca fecha'
        valores = set(re.findall(r'<span class="valor">\s*([^<]+?)\s*</span>',
                                 html[s:fim]))
        if not valores:
            return None, 'secao id="pacotes" sem nenhum <span class="valor">'
        return valores, None

    if i == -1:
        return None, "tem o marcador de FIM da tabela mas nao o de INICIO"
    if f == -1:
        return None, "tem o marcador de INICIO da tabela mas nao o de FIM"
    if f < i:
        return None, "marcadores da tabela fora de ordem (FIM antes do INICIO)"

    bloco = html[i:f + len(MARCA_FIM)]
    valores = set(re.findall(r'<span class="valor">\s*([^<]+?)\s*</span>', bloco))
    if not valores:
        return None, "bloco da tabela existe mas nao tem nenhum <span class=\"valor\">"
    return valores, None


def precos_do_schema(html):
    """Preco que o GOOGLE le: todo Offer/price do JSON-LD, em qualquer nivel.

    Devolve (precos, erros). JSON-LD quebrado entra em erros — nao e engolido.
    """
    precos, erros = set(), []

    def caminhar(no):
        if isinstance(no, dict):
            if no.get("@type") == "Offer" and "price" in no:
                precos.add(str(no["price"]))
            for v in no.values():
                caminhar(v)
        elif isinstance(no, list):
            for v in no:
                caminhar(v)

    for i, b in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                                     html, re.S)):
        try:
            caminhar(json.loads(b))
        except ValueError as e:
            erros.append("JSON-LD %d ilegivel ao procurar preco (%s)" % (i, str(e)[:60]))
    return precos, erros

paginas = sorted(f.replace(os.sep, "/") for f in glob.glob("**/index.html", recursive=True)
                 if "node_modules" not in f)
paginas.append("404.html")

for rel in paginas:
    if rel in FORA_DA_CONFERENCIA:
        continue
    h = Path(rel).read_text(encoding="utf-8")
    stats["paginas"] += 1

    # HTML balanceado
    for tag in ("section", "div", "article", "ul", "ol", "li", "p", "main", "nav", "footer"):
        a = len(re.findall(r"<" + tag + r"[\s>]", h))
        f_ = len(re.findall(r"</" + tag + r">", h))
        if a != f_:
            problemas.append("%s: <%s> abre %d fecha %d" % (rel, tag, a, f_))

    # JSON-LD valido
    for i, b in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)):
        try:
            json.loads(b)
        except ValueError as e:
            problemas.append("%s: JSON-LD %d invalido (%s)" % (rel, i, str(e)[:50]))

    # ancoras internas existem
    ids = set(re.findall(r'id="([^"]+)"', h))
    orfas = sorted(a for a in set(re.findall(r'href="#([^"]+)"', h)) if a and a not in ids)
    if orfas:
        problemas.append("%s: ancora sem destino: %s" % (rel, orfas))

    # links internos existem
    for l in sorted(set(re.findall(r'href="(/[^"#?]*)"', h))):
        alvo = l.strip("/")
        if not alvo:
            continue
        if not any(Path(c).exists() for c in (alvo, alvo + "/index.html", alvo + ".html")):
            problemas.append("%s: link quebrado -> %s" % (rel, l))

    # preco coerente entre a TABELA na tela e a ficha do Google (JSON-LD)
    # So paginas com a tabela precisam dos valores nos dois lugares. Citar
    # "a partir de R$ 1.997" no meio de um texto qualquer e legitimo.
    valores_tela, erro_bloco = precos_do_bloco(h)
    precos_schema, erros_schema = precos_do_schema(h)
    tem_tabela = valores_tela is not None or erro_bloco is not None

    if erro_bloco:
        problemas.append("%s: %s" % (rel, erro_bloco))
    for e in erros_schema:
        problemas.append("%s: %s" % (rel, e))

    if valores_tela is not None:
        stats["com_precos"] += 1

        if valores_tela != VALORES_ESPERADOS:
            faltando = sorted(VALORES_ESPERADOS - valores_tela)
            sobrando = sorted(valores_tela - VALORES_ESPERADOS)
            problemas.append(
                "%s: tabela na tela fora do rcb_pacotes.py | esperado: %s | achado: %s%s%s"
                % (rel, sorted(VALORES_ESPERADOS), sorted(valores_tela),
                   " | falta: %s" % faltando if faltando else "",
                   " | sobra (preco velho?): %s" % sobrando if sobrando else ""))

        if not precos_schema:
            problemas.append("%s: tem a tabela na tela mas nenhum Offer/price no JSON-LD"
                             % rel)
        elif precos_schema != PRECOS_ESPERADOS:
            faltando = sorted(PRECOS_ESPERADOS - precos_schema)
            sobrando = sorted(precos_schema - PRECOS_ESPERADOS)
            problemas.append(
                "%s: preco do JSON-LD fora do rcb_pacotes.py | esperado: %s | achado: %s%s%s"
                % (rel, sorted(PRECOS_ESPERADOS), sorted(precos_schema),
                   " | falta: %s" % faltando if faltando else "",
                   " | sobra (preco velho?): %s" % sobrando if sobrando else ""))

    elif precos_schema and not tem_tabela:
        # Preco na ficha do Google sem tabela na tela: o Google mostraria um
        # valor que o visitante nao ve em lugar nenhum.
        problemas.append("%s: preco no JSON-LD (%s) sem tabela de precos na pagina"
                         % (rel, sorted(precos_schema)))

    # barra do celular e menu novo
    if rel not in SEM_NAVBAR:
        if 'class="cta-mobile"' in h:
            stats["com_barra"] += 1
        else:
            problemas.append("%s: sem barra de CTA no celular" % rel)
        if ">Ver preços<" in h:
            stats["com_menu_novo"] += 1
        elif "nav-cta" in h:
            problemas.append("%s: menu ainda com o botao antigo" % rel)
        if 'class="cta-mobile"' in h and "tem-cta-mobile" not in h:
            problemas.append("%s: barra existe mas o body nao tem a classe" % rel)

    # texto visivel: jargao e contradicao
    corpo = h[h.find("<main"): h.find("</main>")] if "<main" in h else h
    visivel = re.sub(r"<[^>]+>", " ", corpo)
    for j in JARGAO:
        if j.lower() in visivel.lower():
            problemas.append("%s: jargao '%s'" % (rel, j))
    for c in CONTRADICAO:
        if c.lower() in h.lower():
            problemas.append("%s: contradiz o preco ('%s')" % (rel, c))

# llms.txt
llms = Path("llms.txt").read_text(encoding="utf-8")
if "R$ 1.997" not in llms:
    problemas.append("llms.txt: sem a tabela de precos")

# sitemap x arquivos
mapa = Path("sitemap.xml").read_text(encoding="utf-8")
urls = re.findall(r"<loc>https://rcbseo\.com\.br/(.*?)</loc>", mapa)
for u in urls:
    alvo = u.strip("/")
    if alvo and not any(Path(c).exists() for c in (alvo, alvo + "/index.html", alvo + ".html")):
        problemas.append("sitemap: aponta para pagina que nao existe -> /%s" % u)

print("paginas conferidas      :", stats["paginas"])
print("com tabela de precos    :", stats["com_precos"])
print("com barra no celular    :", stats["com_barra"])
print("com o menu novo         :", stats["com_menu_novo"])
print("URLs no sitemap         :", len(urls))
print()
if problemas:
    print("PROBLEMAS (%d):" % len(problemas))
    for x in problemas[:60]:
        sys.stdout.buffer.write(("  - " + x + "\n").encode("utf-8", "replace"))
    if len(problemas) > 60:
        print("  ... e mais %d" % (len(problemas) - 60))
    sys.exit(1)
print("Nenhum problema encontrado.")
