# -*- coding: utf-8 -*-
"""Aplica as correcoes da auditoria SEO/GEO/AIO de 08/09/2026.

Relatorio: docs/AUDITORIA_SEO_GEO_AIO_2026-09-08.md

Cada etapa e idempotente e pode ser rodada isolada. Rodar duas vezes seguidas
tem que dizer "0 alteradas" na segunda.

  --descricoes   item 12: as 2 meta descriptions acima de 160 caracteres
  --headings     item 14: titulos de coluna do rodape de <h4> para <h3>
  --datas        item 33: dateModified nas paginas que nao tem
  --autor        item 30: foto do autor na assinatura dos artigos
  --css          item 9: gera styles.min.css e aponta o site para ele
  --tudo         todas as anteriores

ATENCAO ao --css: styles.css continua sendo a FONTE que se edita; o .min e
gerado. Mexeu no styles.css? Rode `python scripts/auditoria-2026-09-08.py --css`
de novo, senao o site serve CSS velho. O conferir-conversao.py avisa se os dois
estiverem fora de sincronia.

Sobre --headings: o Lighthouse acusava "heading elements are not in a
sequentially-descending order" porque o conteudo termina em <h2> e o rodape
abria em <h4>. Medido nas 318 paginas: o ultimo heading antes do rodape e h2
(243 paginas) ou h3 (75) - nunca h1. Entao <h3> no rodape nao pula nivel em
lugar nenhum.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- descricoes
DESCRICOES = {
    'agente-de-ia-para-clinicas/index.html': (
        u'Agente de IA para clínicas marca consulta no WhatsApp a qualquer hora, '
        u'confirma na véspera e avisa a equipe quando é urgência. Veja funcionando.'
    ),
    'recuperacao-de-vendas-whatsapp/index.html': (
        u'Recuperação de carrinho abandonado no WhatsApp: quem desistiu no pagamento '
        u'recebe uma mensagem, tira a dúvida e volta para a compra. Veja funcionando.'
    ),
}


def paginas():
    for root, _d, fs in os.walk(RAIZ):
        if '.git' in root or 'node_modules' in root or 'graphify-out' in root:
            continue
        for f in fs:
            if f.endswith('.html'):
                yield os.path.join(root, f)


def ler(p):
    return io.open(p, encoding='utf-8').read()


def gravar(p, t):
    io.open(p, 'w', encoding='utf-8', newline='').write(t)


def etapa_descricoes():
    n = 0
    for rel, nova in DESCRICOES.items():
        p = os.path.join(RAIZ, rel.replace('/', os.sep))
        t = ler(p)
        m = re.search(r'name="description"\s+content="([^"]*)"', t)
        antiga = m.group(1)
        if antiga == nova:
            continue
        assert len(nova) <= 160, '%s: %d caracteres' % (rel, len(nova))
        # a description aparece tambem em og: e twitter:
        t = t.replace(antiga, nova)
        gravar(p, t)
        print('   %s: %d -> %d caracteres' % (rel, len(antiga), len(nova)))
        n += 1
    print('descricoes alteradas:', n)
    return n


def etapa_headings():
    n = 0
    for p in paginas():
        t = ler(p)
        i = t.rfind('<footer')
        if i < 0:
            continue
        cabeca, rodape = t[:i], t[i:]
        novo = rodape.replace('<h4 class="footer-col-title">', '<h3 class="footer-col-title">')
        novo = novo.replace('<h4>', '<h3>').replace('</h4>', '</h3>')
        if novo == rodape:
            continue
        gravar(p, cabeca + novo)
        n += 1
    print('paginas com rodape em h3:', n)
    return n


def etapa_datas():
    """Acrescenta dateModified onde o JSON-LD ainda nao tem."""
    hoje = '2026-09-08'
    n = 0
    for p in paginas():
        t = ler(p)
        if 'application/ld+json' not in t or 'dateModified' in t:
            continue
        novo = t
        if '"datePublished"' in novo:
            novo = re.sub(r'"datePublished":\s*"[^"]*",',
                          lambda m: m.group(0) + '\n      "dateModified": "%s",' % hoje,
                          novo, count=1)
        else:
            m = re.search(r'"@type":\s*"(WebPage|Service|LocalBusiness|CollectionPage)"', novo)
            if not m:
                continue
            novo = novo[:m.end()] + ',\n      "dateModified": "%s"' % hoje + novo[m.end():]
        if novo != t:
            gravar(p, novo)
            n += 1
    print('paginas que ganharam dateModified:', n)
    return n


FOTO = '/renan-carvalho-barbosa-consultor-seo-local-goiania.webp'
MARCA_FOTO = '<!--RCB:AUTOR-FOTO-->'
IMG_AUTOR = (
    MARCA_FOTO +
    '<img class="byline-foto" src="%s" width="40" height="40" loading="lazy" '
    'decoding="async" alt="Renan Carvalho Barbosa, consultor de SEO local em Goiânia">'
    % FOTO
)


def etapa_autor():
    """Coloca a foto do autor na assinatura dos artigos do blog."""
    n = 0
    for p in paginas():
        if os.sep + 'blog' + os.sep not in p:
            continue
        t = ler(p)
        if MARCA_FOTO in t:
            continue
        m = re.search(r'<span class="byline-author"[^>]*>', t)
        if not m:
            continue
        gravar(p, t[:m.start()] + IMG_AUTOR + t[m.start():])
        n += 1
    print('artigos com foto na assinatura:', n)
    return n


def minificar(css):
    """Minificacao conservadora: so tira comentario e espaco. Nao reordena nada,
    nao mexe em valor, nao junta seletor - o risco de quebrar visual e zero."""
    m = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    m = re.sub(r'\s+', ' ', m)
    m = re.sub(r'\s*([{}:;,>~+])\s*', r'\1', m)
    m = re.sub(r';}', '}', m)
    return m.strip()


def etapa_css():
    """Gera styles.min.css e faz as paginas apontarem para ele."""
    fonte = os.path.join(RAIZ, 'styles.css')
    alvo = os.path.join(RAIZ, 'styles.min.css')
    novo = minificar(ler(fonte))
    atual = ler(alvo) if os.path.exists(alvo) else None
    if atual != novo:
        gravar(alvo, novo)
        print('   styles.min.css regerado (%.1f KB de %.1f KB)'
              % (len(novo.encode('utf-8')) / 1024,
                 os.path.getsize(fonte) / 1024))
    n = 0
    for p in paginas():
        t = ler(p)
        s = t.replace('href="/styles.css"', 'href="/styles.min.css"')
        if s != t:
            gravar(p, s)
            n += 1
    print('paginas apontando para o CSS minificado:', n)
    return n


def main():
    args = set(sys.argv[1:])
    if not args or '--tudo' in args:
        args = {'--descricoes', '--headings', '--datas', '--autor', '--css'}
    total = 0
    for flag, fn in [('--descricoes', etapa_descricoes), ('--headings', etapa_headings),
                     ('--datas', etapa_datas), ('--autor', etapa_autor),
                     ('--css', etapa_css)]:
        if flag in args:
            print('==', flag)
            total += fn()
    print()
    print('TOTAL de arquivos alterados:', total)


if __name__ == '__main__':
    main()
