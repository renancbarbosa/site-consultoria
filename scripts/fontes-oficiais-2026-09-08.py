# -*- coding: utf-8 -*-
"""Liga o texto as fontes oficiais quando ele cita algo que tem fonte oficial.

Item 26 da auditoria de 08/09/2026: 110 de 150 paginas indexaveis nao citavam
nenhuma fonte de autoridade. Para SEO isso e um sinal fraco de E-E-A-T; para as
IAs e pior, porque elas seguem e conferem as fontes que a pagina cita.

Como funciona: procura a PRIMEIRA ocorrencia de um termo que tem documentacao
oficial e transforma so aquela ocorrencia em link. Nada de "leia mais" no
rodape - o link entra onde o assunto ja esta sendo tratado, que e onde ele
ajuda o leitor e onde o buscador entende o contexto.

Regras de seguranca:
  * no maximo 1 link novo por pagina (nao vira fazenda de links);
  * nunca dentro de uma tag, de um <a>, de um heading, de um <script> ou de um
    comentario;
  * pula a pagina que ja cita alguma fonte de autoridade;
  * so paginas indexaveis;
  * rel="nofollow" - sao fontes, nao parceiros.

Idempotente pelo marcador data-fonte-oficial.
Uso: python scripts/fontes-oficiais-2026-09-08.py [--aplicar]
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = 'data-fonte-oficial'

# ordem importa: o primeiro termo que casar e o que vira link
FONTES = [
    (u'Google Perfil da Empresa',
     'https://support.google.com/business/answer/3038177',
     u'documentação oficial do Google Perfil da Empresa'),
    (u'Google Meu Negócio',
     'https://support.google.com/business/answer/3038177',
     u'documentação oficial do Google'),
    (u'dados estruturados',
     'https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data',
     u'guia de dados estruturados do Google'),
    (u'Search Console',
     'https://support.google.com/webmasters/answer/9128668',
     u'documentação do Google Search Console'),
    (u'avaliações do Google',
     'https://support.google.com/business/answer/3474050',
     u'regras do Google sobre avaliações'),
    (u'Google Maps',
     'https://support.google.com/business/answer/7091',
     u'critérios de posicionamento local do Google'),
    (u'SEO local',
     'https://developers.google.com/search/docs/fundamentals/seo-starter-guide',
     u'guia de SEO do Google'),
    (u'SEO',
     'https://developers.google.com/search/docs/fundamentals/seo-starter-guide',
     u'guia de SEO do Google'),
]

JA_TEM = re.compile(r'href="https?://[^"]*(?:\.gov\.br|\.edu|support\.google|'
                    r'developers\.google|cfm\.org|cfo\.org|oab\.|anvisa)')


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


def zonas_regiao(t):
    """Areas inteiras onde o link nao pode entrar, por decisao editorial ou
    porque outro script reescreve aquele pedaco."""
    z = []
    for m in re.finditer(r'<(script|style|h[1-6]|a|title)\b.*?</\1>', t, re.S | re.I):
        z.append((m.start(), m.end()))
    # topo e rodape: link externo no hero rouba o visitante logo na chegada, e
    # no rodape nao ajuda ninguem a entender nada.
    m = re.search(r'<section class="(?:page-)?hero[^"]*"', t)
    if m:
        fim = t.find('</section>', m.end())
        z.append((0, fim if fim > 0 else m.end()))
    fim_rodape = t.rfind('<footer')
    if fim_rodape > 0:
        z.append((fim_rodape, len(t)))
    # blocos escritos por outros scripts: link ali seria apagado na proxima
    # regeracao. E a tabela de precos e area de conversao.
    for abre, fecha in [('<!-- RCB:PACOTES:INICIO -->', '<!-- RCB:PACOTES:FIM -->'),
                        ('<!-- RCB:CTA-MOBILE -->', '</div>'),
                        ('<!--RCB:AGENTES-NAV-->', '<!--/RCB:AGENTES-NAV-->'),
                        ('<!--RCB:RELACIONADOS-->', '<!--/RCB:RELACIONADOS-->'),
                        ('<nav class="navbar"', '</nav>'),
                        ('<section id="pacotes"', '</section>')]:
        i = t.find(abre)
        while i >= 0:
            j = t.find(fecha, i)
            z.append((i, (j + len(fecha)) if j > 0 else len(t)))
            i = t.find(abre, i + 1)
    return z


def zonas_tag(t):
    """Posicoes ocupadas por marcacao: nunca cortar o texto no meio delas."""
    z = [(m.start(), m.end()) for m in re.finditer(r'<[^>]*>', t)]
    z += [(m.start(), m.end()) for m in re.finditer(r'<!--.*?-->', t, re.S)]
    return z


def livre(pos, fim, zonas):
    return not any(a < fim and pos < b for a, b in zonas)


def main():
    aplicar = '--aplicar' in sys.argv
    feitos, sem_termo = [], []

    # paragrafos que nao servem: rotulo, breadcrumb, cartao de preco, botao.
    # O link tem que cair em texto corrido para ajudar o leitor e o buscador.
    FORA_DE_P = ('pacote-', 'cta-', 'btn', 'section-tag', 'breadcrumb',
                 'artigo-cat', 'hero', 'footer', 'byline', 'wa-',
                 'resultado-', 'depoimento', 'calc-')

    for p in paginas():
        t = ler(p)
        if re.search(r'name="robots"[^>]*content="[^"]*noindex', t):
            continue
        if MARCA in t or JA_TEM.search(t):
            continue

        regioes = zonas_regiao(t)
        tags = zonas_tag(t)
        # paragrafo serve se ele COMECA fora das regioes proibidas
        paragrafos = [m for m in re.finditer(r'<p([^>]*)>(.*?)</p>', t, re.S)
                      if not any(x in m.group(1) for x in FORA_DE_P)
                      and livre(m.start(), m.start() + 1, regioes)]

        escolha = None
        for termo, url, titulo in FONTES:
            for mp in paragrafos:
                m = re.search(re.escape(termo), t[mp.start(2):mp.end(2)])
                if not m:
                    continue
                ini = mp.start(2) + m.start()
                fim = mp.start(2) + m.end()
                if livre(ini, fim, tags) and livre(ini, fim, regioes):
                    escolha = (ini, fim, termo, url, titulo)
                    break
            if escolha:
                break

        if not escolha:
            sem_termo.append(os.path.relpath(p, RAIZ))
            continue

        ini, fim, termo, url, titulo = escolha
        link = (u'<a href="%s" target="_blank" rel="noopener noreferrer nofollow" '
                u'%s title="%s">%s</a>' % (url, MARCA, titulo, termo))
        t = t[:ini] + link + t[fim:]
        if aplicar:
            gravar(p, t)
        feitos.append((os.path.relpath(p, RAIZ), termo))

    print('paginas que ganharam fonte oficial:', len(feitos))
    for rel, termo in feitos[:8]:
        print('   %-50s -> %s' % (rel[:50], termo))
    if len(feitos) > 8:
        print('   ... e mais', len(feitos) - 8)
    if sem_termo:
        print()
        print('sem termo em texto corrido (deixadas como estavam):', len(sem_termo))
        for s in sem_termo[:6]:
            print('   ', s)
    if not aplicar:
        print('\n(modo relatorio - rode com --aplicar para gravar)')


if __name__ == '__main__':
    main()
