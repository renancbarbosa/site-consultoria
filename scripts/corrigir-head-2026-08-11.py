# -*- coding: utf-8 -*-
"""
Reorganiza o <head> de todas as paginas (auditoria de 11/08/2026, bloco 2.1).

O QUE MUDA
  Antes:  <head>
            <script async src="...gtag/js"></script>   <- externo, baixa da rede
            <script> ...consent default... </script>   <- embutido
            <meta charset="UTF-8">                     <- so aqui, ~640 bytes dentro
            ...
            <link rel="stylesheet" href="/styles.css">

  Depois: <head>
            <meta charset="UTF-8">                     <- 1a tag, como o HTML pede
            <meta name="viewport" ...>
            <script> ...consent default... </script>   <- embutido SOBE
            ...
            <link rel="stylesheet" href="/styles.css">
            <script async src="...gtag/js"></script>   <- externo DESCE

POR QUE SEPARAR O BLOCO EM DOIS
  A auditoria pedia para mover "o gtag" inteiro para depois do CSS. Isso
  quebraria o consentimento de cookies: uma folha de estilo trava a execucao de
  qualquer <script> que venha depois dela, entao o script embutido (que declara
  ad_storage/analytics_storage como 'denied') ficaria esperando o CSS baixar --
  enquanto o script externo, por ser async, executa assim que chega. Numa rede
  em que o CSS demore mais que o gtag, o GA4 dispararia SEM os padroes de
  consentimento. Regressao de LGPD, nao so de performance.

  O embutido nao baixa nada e custa microssegundos: ele sobe. So o externo desce.

SEGURANCA
  - Preserva as quebras de linha de cada arquivo (o site tem 201 em LF e 106 em
    CRLF; reescrever tudo num padrao so sujaria o diff de 306 arquivos).
  - Conferencia por multiconjunto de tokens: o arquivo depois tem exatamente os
    mesmos pedacos de texto de antes, so em outra ordem. Se algo se perder ou
    duplicar, o arquivo NAO e gravado.
  - Idempotente: rodar de novo diz "0 alteradas".

Uso:  python scripts/corrigir-head-2026-08-11.py [--simular]
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)

# graphify-out e artefato local (fora do versionamento); node_modules nao e site.
IGNORAR = ("node_modules", "graphify-out", "Projetos")

RE_GTAG = re.compile(
    r'[ \t]*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+">'
    r'</script>\r?\n'
    r'[ \t]*<script>.*?</script>[ \t]*\r?\n',
    re.S)
RE_VIEWPORT = re.compile(r'[ \t]*<meta name="viewport"[^>]*>[ \t]*\r?\n')
RE_CSS = re.compile(r'[ \t]*<link rel="stylesheet" href="/styles\.css">[ \t]*\r?\n')
RE_CHARSET = re.compile(r'<meta charset=', re.I)


def paginas():
    for f in sorted(glob.glob("**/*.html", recursive=True)):
        f = f.replace(os.sep, "/")
        if any(p in f for p in IGNORAR):
            continue
        yield f


def reorganizar(html):
    """Devolve (novo_html, motivo_se_pulou)."""
    fim = html.find("</head>")
    if fim == -1:
        return None, "sem </head>"
    head, resto = html[:fim], html[fim:]

    m = RE_GTAG.search(head)
    if not m:
        return None, "bloco gtag fora do padrao"

    bloco = m.group(0)
    corte = bloco.index("</script>") + len("</script>")
    externo = bloco[:corte].strip()          # <script async src=...></script>
    embutido = bloco[corte:].strip()         # <script> ...consent... </script>
    if not embutido.startswith("<script>"):
        return None, "nao consegui separar externo de embutido"

    novo = head.replace(bloco, "", 1)

    mv = RE_VIEWPORT.search(novo)
    if not mv:
        return None, "sem <meta name=viewport>"
    if not RE_CSS.search(novo):
        return None, "sem link para /styles.css"

    nl = "\r\n" if mv.group(0).endswith("\r\n") else "\n"

    # embutido logo depois do viewport; externo logo depois do CSS.
    novo = novo[:mv.end()] + "  " + embutido + nl + novo[mv.end():]
    mc = RE_CSS.search(novo)                 # posicao mudou apos a insercao acima
    novo = novo[:mc.end()] + "  " + externo + nl + novo[mc.end():]

    return novo + resto, None


def conferir(antes, depois, rel):
    """Erros que impedem a gravacao."""
    erros = []

    if sorted(antes.split()) != sorted(depois.split()):
        erros.append("o conteudo mudou (nao foi so reordenacao)")

    head = depois[:depois.find("</head>")]
    i_head = head.find("<head>") + len("<head>")
    mch = RE_CHARSET.search(head)
    if not mch:
        erros.append("ficou sem <meta charset>")
    elif head[i_head:mch.start()].strip() != "":
        erros.append("charset nao ficou como 1a tag do <head>")

    i_emb = depois.find("<script>")
    i_ext = depois.find("googletagmanager.com/gtag/js")
    i_css = depois.find('href="/styles.css"')
    if i_emb == -1 or i_ext == -1 or not i_emb < i_ext:
        erros.append("consentimento embutido caiu DEPOIS do script do Google")
    if i_css == -1 or not i_css < i_ext:
        erros.append("script do Google nao ficou depois do CSS")

    return ["%s: %s" % (rel, e) for e in erros]


def main():
    simular = "--simular" in sys.argv[1:]
    alteradas = ja_ok = 0
    pulos, erros = [], []

    for rel in paginas():
        with open(rel, encoding="utf-8", newline="") as f:
            antes = f.read()

        head_antes = antes[:antes.find("</head>")]
        if RE_GTAG.search(head_antes) is None:
            # Ja corrigida (o embutido nao segue mais o externo) ou fora do padrao.
            i_head = head_antes.find("<head>") + len("<head>")
            mch = RE_CHARSET.search(head_antes)
            if mch and head_antes[i_head:mch.start()].strip() == "":
                ja_ok += 1
            else:
                pulos.append((rel, "bloco gtag fora do padrao"))
            continue

        depois, motivo = reorganizar(antes)
        if depois is None:
            pulos.append((rel, motivo))
            continue

        problemas = conferir(antes, depois, rel)
        if problemas:
            erros.extend(problemas)
            continue

        if not simular:
            with open(rel, "w", encoding="utf-8", newline="") as f:
                f.write(depois)
        alteradas += 1

    print("paginas alteradas    :", alteradas, "(simulacao)" if simular else "")
    print("ja estavam corretas  :", ja_ok)
    if pulos:
        print("\nPULADAS (%d) - conferir a mao:" % len(pulos))
        for rel, motivo in pulos:
            print("  - %s: %s" % (rel, motivo))
    if erros:
        print("\nNAO GRAVADAS por falha na conferencia (%d):" % len(erros))
        for e in erros:
            print("  - %s" % e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
