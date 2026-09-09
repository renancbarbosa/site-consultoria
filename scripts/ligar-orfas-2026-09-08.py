# -*- coding: utf-8 -*-
"""Reforca os links internos das paginas que quase nao recebem nenhum.

Item 19 da auditoria de 08/09/2026: 36 paginas indexaveis recebiam menos de 3
links internos. Pagina que so recebe link do indice do blog e tratada pelo
Google como periferica, por melhor que seja o texto.

Tres grupos, tres tratamentos:

  1. ARTIGOS DO BLOG - ganham um bloco "Leia tambem" no fim do artigo DOADOR,
     escolhido por afinidade de tema (palavras em comum no titulo, fora as
     palavras vazias). Nunca aponta para si mesmo, nunca repete link que a
     pagina ja tenha, e nunca usa outra pagina fraca como doadora.
  2. CIDADES - entram na lista do hub /consultoria-seo/, que ja e a pagina que
     distribui autoridade para elas.
  3. PAGINAS DE APOIO (/marketing-para-*/) - recebem link contextual das
     paginas de nicho irmas.

Idempotente pelos marcadores RCB:RELACIONADOS e RCB:HUB-EXTRA.
Uso: python scripts/ligar-orfas-2026-09-08.py [--aplicar]
"""
import io
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_LINKS = 3

VAZIAS = set("""a o as os de do da dos das e em no na nos nas para por com que
se um uma uns umas ao aos meu minha seu sua vale pena como onde quando qual
quais mais menos ja nao sim ou mas ser esta estao tem ter sobre""".split())


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn').lower()


def palavras(s):
    return {p for p in re.findall(r'[a-z]{3,}', sem_acento(s)) if p not in VAZIAS}


def ler(p):
    return io.open(p, encoding='utf-8').read()


def gravar(p, t):
    io.open(p, 'w', encoding='utf-8', newline='').write(t)


def todas():
    for root, _d, fs in os.walk(RAIZ):
        if '.git' in root or 'node_modules' in root or 'graphify-out' in root:
            continue
        for f in fs:
            if f.endswith('.html'):
                yield os.path.join(root, f)


def caminho_de(p):
    u = p.replace(RAIZ, '').replace(os.sep, '/')
    return u.replace('/index.html', '/') or '/'


def levantar():
    info, recebe = {}, {}
    for p in todas():
        t = ler(p)
        c = caminho_de(p)
        m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
        info[c] = {
            'arquivo': p,
            'titulo': re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else '',
            'noindex': bool(re.search(r'name="robots"[^>]*content="[^"]*noindex', t)),
            'saida': {l.rstrip('/') + '/' for l in re.findall(r'href="(/[^"#?]*)"', t)},
        }
    for _c, d in info.items():
        for l in d['saida']:
            recebe[l] = recebe.get(l, 0) + 1
    return info, recebe


BLOCO = """        <!--RCB:RELACIONADOS-->
        <div class="artigo-relacionados">
          <h2>Leia também</h2>
          <ul>
%s
          </ul>
        </div>
        <!--/RCB:RELACIONADOS-->
"""


def main():
    aplicar = '--aplicar' in sys.argv
    info, recebe = levantar()

    fracas = [c for c, d in info.items()
              if not d['noindex'] and recebe.get(c, 0) < MIN_LINKS]
    artigos = [c for c in fracas if c.startswith('/blog/')]
    cidades = [c for c in fracas if c.startswith('/consultoria-seo/')]
    apoio = [c for c in fracas if c not in artigos and c not in cidades]
    print('fracas: %d (blog %d, cidades %d, apoio %d)'
          % (len(fracas), len(artigos), len(cidades), len(apoio)))

    # ---- 1. artigos do blog ----
    candidatos = [c for c, d in info.items()
                  if c.startswith('/blog/') and c != '/blog/' and not d['noindex']]
    novos = {}
    for alvo in artigos:
        pa = palavras(info[alvo]['titulo'])
        notas = []
        for doador in candidatos:
            if doador == alvo or alvo in info[doador]['saida']:
                continue
            if recebe.get(doador, 0) < MIN_LINKS:
                continue
            n = len(pa & palavras(info[doador]['titulo']))
            if n:
                notas.append((n, doador))
        notas.sort(reverse=True)
        for _n, doador in notas[:2]:
            novos.setdefault(doador, []).append((alvo, info[alvo]['titulo']))

    mexidos = criados = 0
    for doador, alvos in novos.items():
        p = info[doador]['arquivo']
        t = ler(p)
        if '<!--RCB:RELACIONADOS-->' in t:
            continue
        m = re.search(r'\n\s*</div>\s*\n\s*<div class="artigo-voltar">', t)
        if not m:
            continue
        itens = '\n'.join('            <li><a href="%s">%s</a></li>' % (u, tit)
                          for u, tit in alvos)
        t = t[:m.start()] + '\n' + BLOCO % itens + t[m.start():]
        if aplicar:
            gravar(p, t)
        mexidos += 1
        criados += len(alvos)
    print('artigos com bloco "Leia também":', mexidos, '| links criados:', criados)

    # ---- 2. cidades ----
    # O hub ja linka todas. O reforco vem da pagina nacional do servico, que e o
    # lugar onde "atendo em varias cidades" faz sentido editorial.
    doador_cidades = os.path.join(RAIZ, 'consultoria-seo-local', 'index.html')
    t = ler(doador_cidades)
    faltam = [c for c in cidades if c not in info['/consultoria-seo-local/']['saida']]
    if faltam and '<!--RCB:HUB-EXTRA-->' not in t:
        itens = ' · '.join(
            '<a href="%s">%s</a>' % (c, info[c]['titulo'].split(':')[0]
                                     .replace('Consultoria de SEO em ', '').strip())
            for c in sorted(faltam))
        bloco = ('<!--RCB:HUB-EXTRA--><p class="hub-extra">Atendo online empresas de '
                 'todo o Brasil — entre elas %s. Veja a '
                 '<a href="/consultoria-seo/">lista completa de cidades</a>.</p>'
                 '<!--/RCB:HUB-EXTRA-->' % itens)
        m = re.search(r'\n\s*</main>', t)
        if m:
            t = t[:m.start()] + '\n      ' + bloco + t[m.start():]
            if aplicar:
                gravar(doador_cidades, t)
            print('cidades ligadas da pagina nacional: %d' % len(faltam))
    else:
        print('cidades: nada a fazer')

    # ---- 3. paginas de apoio ----
    # Essas paginas de nicho nao tem secao "Leia tambem"; o link entra na ultima
    # frase do texto, que e onde o leitor ja esta decidindo o proximo passo.
    PARES = {
        '/marketing-para-clinicas/': [('/seo-para-clinicas/',
                                       u'marketing para clínicas'),
                                      ('/site-para-clinica/',
                                       u'marketing para clínicas')],
        '/marketing-para-advogados/': [('/para-advogados/',
                                        u'marketing para advogados')],
    }
    n = 0
    for alvo, doadores in PARES.items():
        if alvo not in fracas:
            continue
        for doador, ancora in doadores:
            if doador not in info:
                continue
            p = info[doador]['arquivo']
            t = ler(p)
            if alvo in t or '<!--RCB:LINK-APOIO-->' in t:
                continue
            # ultimo paragrafo antes do rodape
            corte = t.rfind('<footer')
            ps = list(re.finditer(r'</p>', t[:corte]))
            if not ps:
                continue
            ini = ps[-1].start()
            extra = (u' <!--RCB:LINK-APOIO--><a href="%s">Veja também o guia de %s</a>.'
                     u'<!--/RCB:LINK-APOIO-->' % (alvo, ancora))
            t = t[:ini] + extra + t[ini:]
            if aplicar:
                gravar(p, t)
            n += 1
    print('páginas de apoio ligadas:', n)

    if not aplicar:
        print('\n(modo relatorio - rode com --aplicar para gravar)')


if __name__ == '__main__':
    main()
