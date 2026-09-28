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
from rcb_pacotes import MARCA_INI, MARCA_FIM  # noqa: E402

# Desde 28/09/2026 o site NAO mostra preco da RCB (decisao do Renan). A regra
# se inverteu: antes esta conferencia exigia os valores na tabela e na ficha do
# Google; agora ela ACUSA qualquer valor da RCB que apareca. Faixas de mercado
# ("site custa de R$ 100/mes a R$ 10 mil") sao permitidas e nao casam aqui.
# Mesmo padrao do scripts/remover-precos-2026-09-28.py.
PRECO_RCB = re.compile(
    r'R\$\s?(?:1\.997|2\.497|2\.997|4\.997|997|1\.497)(?![\d.,])'
    r'|(?<![\d.])(?:1997|2497|2997|4997)\.00'
    r'|a partir de R\$'
    r'|"priceRange"|"offers"\s*:'
    r'|(?<!um )[Pp]reço (?:fechado|publicado|está (?:na tela|publicado))'
    r'|[Pp]agamento por Pix pelo WhatsApp\.<'
    r'|class="valor"'
)

JARGAO = ["GMB", "on-page", "metadescri", "arquitetura de informa",
          "ticket médio", "métricas de vaidade", "escopo enxuto"]
# Ate 28/09/2026 estas frases "contradiziam o preco publicado". Hoje o site e
# sem preco e elas sao o discurso certo: lista vazia de proposito.
CONTRADICAO = []

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
        return valores, None                  # vazio = certo (sem preco)

    if i == -1:
        return None, "tem o marcador de FIM da tabela mas nao o de INICIO"
    if f == -1:
        return None, "tem o marcador de INICIO da tabela mas nao o de FIM"
    if f < i:
        return None, "marcadores da tabela fora de ordem (FIM antes do INICIO)"

    bloco = html[i:f + len(MARCA_FIM)]
    valores = set(re.findall(r'<span class="valor">\s*([^<]+?)\s*</span>', bloco))
    return valores, None                      # vazio = certo (sem preco)


def precos_do_schema(html):
    """Preco que o GOOGLE le: todo Offer/price do JSON-LD, em qualquer nivel.

    Devolve (precos, erros). JSON-LD quebrado entra em erros — nao e engolido.
    """
    precos, erros = set(), []

    def caminhar(no):
        if isinstance(no, dict):
            if "price" in no:
                precos.add(str(no["price"]))
            if "priceRange" in no:
                precos.add("priceRange " + str(no["priceRange"]))
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

    # SEM PRECO (desde 28/09/2026): tabela sem valor, ficha do Google sem
    # price/priceRange e nenhuma mencao a preco da RCB na pagina.
    valores_tela, erro_bloco = precos_do_bloco(h)
    precos_schema, erros_schema = precos_do_schema(h)

    if erro_bloco:
        problemas.append("%s: %s" % (rel, erro_bloco))
    for e in erros_schema:
        problemas.append("%s: %s" % (rel, e))

    if valores_tela is not None:
        stats["com_precos"] += 1
        if valores_tela:
            problemas.append("%s: tabela de pacotes mostrando preco %s"
                             % (rel, sorted(valores_tela)))
    if precos_schema:
        problemas.append("%s: preco na ficha do Google (JSON-LD): %s"
                         % (rel, sorted(precos_schema)))
    m_preco = PRECO_RCB.search(h)
    if m_preco:
        problemas.append("%s: preco da RCB no texto ('%s')" % (rel, m_preco.group(0)))

    # barra do celular e menu novo
    if rel not in SEM_NAVBAR:
        if 'class="cta-mobile"' in h:
            stats["com_barra"] += 1
        else:
            problemas.append("%s: sem barra de CTA no celular" % rel)
        if ">Orçamento grátis<" in h:
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
if PRECO_RCB.search(llms):
    problemas.append("llms.txt: cita preco da RCB ('%s')" % PRECO_RCB.search(llms).group(0))

# CSS minificado em dia?
# styles.css e a FONTE que se edita; styles.min.css e o que o site serve.
# Se alguem editar a fonte e esquecer de regerar, o site continua servindo o CSS
# velho e ninguem percebe. Este check existe para isso nao passar batido.
if Path("styles.min.css").exists():
    import importlib.util as _il
    _spec = _il.spec_from_file_location("_aud", "scripts/auditoria-2026-09-08.py")
    _aud = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_aud)
    if _aud.minificar(Path("styles.css").read_text(encoding="utf-8")) != \
            Path("styles.min.css").read_text(encoding="utf-8"):
        problemas.append(
            "styles.min.css DESATUALIZADO em relacao ao styles.css "
            "-> rode: python scripts/auditoria-2026-09-08.py --css")

# sitemap x arquivos
mapa = Path("sitemap.xml").read_text(encoding="utf-8")
urls = re.findall(r"<loc>https://rcbseo\.com\.br/(.*?)</loc>", mapa)
for u in urls:
    alvo = u.strip("/")
    if alvo and not any(Path(c).exists() for c in (alvo, alvo + "/index.html", alvo + ".html")):
        problemas.append("sitemap: aponta para pagina que nao existe -> /%s" % u)

print("paginas conferidas      :", stats["paginas"])
print("com tabela de pacotes   :", stats["com_precos"])
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
