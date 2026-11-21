"""Links internos no texto corrido para as paginas leigas de maior procura.

/como-aparecer-no-google/ (251 aparicoes, pos 50), /blog/por-que-minha-empresa-nao-aparece-no-google/
(176, pos 64) e /como-aparecer-no-chatgpt/ (109, pos 57) recebiam poucos links internos.

Regra: so a 1a ocorrencia da frase, so em <p> sem atributo (texto corrido), fora de <a>, fora
de blocos com marcador RCB: (seriam apagados na regeracao), fora da pagina protegida e das
paginas de cidade. No maximo 1 link novo por alvo por pagina e LIMITE paginas por alvo.
Idempotente: pagina que ja linka o alvo e pulada. Rodar de novo depois de regerar paginas.
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LIMITE = 30
PULAR = {"consultor-seo-goiania", "404.html", "diagnostico-presenca-digital/exemplo", "cases"}

ALVOS = [
    ("/como-aparecer-no-google/", re.compile(r"\b(aparecer no Google)\b(?! Maps)", re.I)),
    ("/blog/por-que-minha-empresa-nao-aparece-no-google/",
     re.compile(r"\b(n[ãa]o aparece no Google)\b(?! Maps)", re.I)),
    ("/como-aparecer-no-chatgpt/", re.compile(r"\b(ChatGPT)\b")),
]

MARCADOR = re.compile(r"<!-- ?RCB:([A-Z0-9-]+) ?-->.*?<!-- ?/RCB:\1 ?-->", re.S)
PARAGRAFO = re.compile(r"<p>(.*?)</p>", re.S)
LINK = re.compile(r"<a\b.*?</a>", re.S)


def paginas():
    for arq in sorted(RAIZ.rglob("index.html")):
        rel = arq.parent.relative_to(RAIZ).as_posix()
        if rel in PULAR or rel.startswith(("consultoria-seo/", "scripts", "docs", "data", "node_modules", ".")):
            continue
        yield rel, arq


def ligar(s, url, pad):
    proibido = [m.span() for m in MARCADOR.finditer(s)]
    ini_main = s.find("<main")
    for m in PARAGRAFO.finditer(s):
        a, b = m.span()
        if a < ini_main or any(x < b and a < y for x, y in proibido):  # encosta num bloco RCB: pula
            continue
        interno = m.group(1)
        pedacos, pos, feito = [], 0, False
        for lk in LINK.finditer(interno):
            pedacos.append((interno[pos:lk.start()], True))
            pedacos.append((lk.group(0), False))
            pos = lk.end()
        pedacos.append((interno[pos:], True))
        novo = []
        for txt, livre in pedacos:
            if livre and not feito:
                txt, n = pad.subn(lambda x: f'<a href="{url}">{x.group(1)}</a>', txt, count=1)
                feito = n == 1
            novo.append(txt)
        if feito:
            return s[:m.start(1)] + "".join(novo) + s[m.end(1):]
    return None


def main():
    contagem = {u: 0 for u, _ in ALVOS}
    alteradas = set()
    for rel, arq in paginas():
        s = arq.read_text(encoding="utf-8")
        original = s
        for url, pad in ALVOS:
            if contagem[url] >= LIMITE or f'href="{url}"' in s or "/" + rel + "/" == url:
                continue
            t = ligar(s, url, pad)
            if t:
                s = t
                contagem[url] += 1
        if s != original:
            arq.write_text(s, encoding="utf-8", newline="")
            alteradas.add(rel)
    for u, n in contagem.items():
        print(f"{n:3d} links novos para {u}")
    print(f"paginas alteradas: {len(alteradas)}")
    for r in sorted(alteradas):
        print("  /" + r + "/")


if __name__ == "__main__":
    main()
