# -*- coding: utf-8 -*-
"""Deixa a resposta da pagina caber nas primeiras ~70 palavras (answer-first).

Item 17 da auditoria de 08/09/2026: 39 paginas indexaveis abriam com mais de 70
palavras antes de fechar o primeiro paragrafo. O AI Overview do Google e o
ChatGPT extraem a resposta do inicio; um paragrafo de 90 palavras dilui isso.

O que este script NAO faz: reescrever texto. Olhando as 39, a resposta ja
estava la - so vinha grudada no contexto dentro do mesmo paragrafo. Entao ele
apenas QUEBRA o primeiro paragrafo em dois, numa fronteira de frase:

    <p>Resposta direta. Contexto que vem depois.</p>
    ->
    <p>Resposta direta.</p>
    <p>Contexto que vem depois.</p>

Nenhuma palavra e adicionada, removida ou trocada de lugar. O sentido do texto
e exatamente o mesmo; muda so onde o paragrafo termina.

Regras de seguranca do corte:
  * so corta em ".", "!" ou "?" que esteja FORA de qualquer tag HTML;
  * so corta com as tags do paragrafo fechadas ate ali (nunca dentro de um
    <a> ou <strong>);
  * a primeira parte precisa ter entre 25 e 70 palavras - abaixo de 25 o
    paragrafo fica amputado, entao a pagina e deixada como esta;
  * escolhe o corte que chega mais perto de 70 palavras sem passar.

Uso: python scripts/answer-first-2026-09-08.py [--aplicar]
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_PALAVRAS, MAX_PALAVRAS = 25, 70


def ler(p):
    return io.open(p, encoding='utf-8').read()


def gravar(p, t):
    io.open(p, 'w', encoding='utf-8', newline='').write(t)


def paginas():
    for root, _d, fs in os.walk(RAIZ):
        if '.git' in root or 'node_modules' in root or 'graphify-out' in root:
            continue
        for f in fs:
            if f.endswith('.html'):
                yield os.path.join(root, f)


def texto(html):
    return re.sub(r'<[^>]+>', '', html)


def cortes_validos(interno):
    """Posicoes onde da para cortar o HTML do paragrafo com seguranca."""
    fora_de_tag = True
    abertas = 0
    for i, ch in enumerate(interno):
        if ch == '<':
            fora_de_tag = False
            abertas += -1 if interno[i + 1:i + 2] == '/' else 1
        elif ch == '>':
            fora_de_tag = True
        elif fora_de_tag and ch in '.!?' and abertas == 0:
            if interno[i + 1:i + 2] in (' ', ''):
                yield i + 1


def quebrar(interno):
    """Devolve (primeira_parte, segunda_parte) ou None."""
    melhor = None
    for corte in cortes_validos(interno):
        n = len(texto(interno[:corte]).split())
        if MIN_PALAVRAS <= n <= MAX_PALAVRAS:
            if melhor is None or n > melhor[0]:
                melhor = (n, corte)
    if not melhor:
        return None
    corte = melhor[1]
    a, b = interno[:corte].strip(), interno[corte:].strip()
    return (a, b) if b else None


def main():
    aplicar = '--aplicar' in sys.argv
    mexidas, pulos = [], []

    for p in paginas():
        t = ler(p)
        if re.search(r'name="robots"[^>]*content="[^"]*noindex', t):
            continue
        corpo = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
        mh = re.search(r'<h1[^>]*>.*?</h1>', corpo, re.S)
        if not mh:
            continue
        mp = re.search(r'<p[^>]*>(.*?)</p>', corpo[mh.end():], re.S)
        if not mp:
            continue
        interno = mp.group(1)
        n = len(texto(interno).split())
        if n <= MAX_PALAVRAS:
            continue

        rel = os.path.relpath(p, RAIZ)
        r = quebrar(interno)
        if not r:
            pulos.append((rel, n, 'sem ponto final em posicao segura'))
            continue
        a, b = r
        alvo = mp.group(0)
        if t.count(alvo) != 1:
            pulos.append((rel, n, 'paragrafo nao localizado sem ambiguidade'))
            continue
        i = t.find(alvo)
        abre = re.match(r'<p[^>]*>', alvo).group(0)
        novo = '%s%s</p>\n\n        <p>%s</p>' % (abre, a, b)
        t = t[:i] + novo + t[i + len(alvo):]
        if aplicar:
            gravar(p, t)
        mexidas.append((rel, n, len(texto(a).split())))

    print('paginas ajustadas:', len(mexidas))
    for rel, antes, depois in mexidas[:8]:
        print('   %-56s %d -> %d palavras' % (rel[:56], antes, depois))
    if len(mexidas) > 8:
        print('   ... e mais', len(mexidas) - 8)
    if pulos:
        print()
        print('deixadas como estavam:', len(pulos))
        for rel, n, motivo in pulos:
            print('   %-50s %d palavras (%s)' % (rel[:50], n, motivo))
    if not aplicar:
        print('\n(modo relatorio - rode com --aplicar para gravar)')


if __name__ == '__main__':
    main()
