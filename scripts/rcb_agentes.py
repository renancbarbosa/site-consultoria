# -*- coding: utf-8 -*-
"""Componentes visuais da linha "Agentes de IA" (paginas comerciais + artigos).

Este modulo NAO tem texto de venda dentro. Ele so sabe MONTAR:
  * o celular com a conversa simulada (bloco_whatsapp)
  * o fluxo em linguagem leiga (bloco_fluxo)
  * a calculadora de perda (bloco_calculadora)
  * o mockup de relatorio (bloco_painel)
  * a linha do tempo (bloco_linha_tempo)
  * o comparativo hoje/depois (bloco_antes_depois)
  * os depoimentos REAIS (bloco_depoimentos)
  * o esqueleto da pagina clonado de /consultor-seo-goiania/ (montar_pagina)

O texto de cada pagina fica em gerar-agentes-ia.py / gerar-artigos-agentes-ia.py.

REGRAS QUE NAO PODEM SER AFROUXADAS (decididas com o Renan em 08/09/2026):
  1. Toda simulacao carrega o selo "Demonstracao - conversa simulada". Nunca
     apresentar como print de cliente real.
  2. Nenhum depoimento inventado. Os tres depoimentos daqui sao os mesmos que
     ja estao na home, com nome real, e a legenda diz que sao de clientes de
     consultoria de SEO - nao de automacao, que ainda nao tem cliente.
  3. Nenhum numero de resultado inventado ("reduza 40% de faltas", "+70% de
     vendas", "15 clinicas atendidas"). Numero na tela so se for do proprio
     visitante (calculadora) ou tiver fonte citada.
  4. Sem preco nestas paginas: a linha e nova e cada projeto e diferente.
     O caminho e orcamento pelo WhatsApp.

A pagina /consultor-seo-goiania/ e apenas LIDA como molde. Nunca escrita.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rcb_pacotes as P

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOADOR = os.path.join(RAIZ, "consultor-seo-goiania", "index.html")

CSS = '<link rel="stylesheet" href="/assets/css/agentes-ia.css">'
JS = '  <script src="/assets/js/agentes-ia.js" defer></script>\n'
OG_IMG = "https://rcbseo.com.br/assets/img/og-rcb-1200x628.png"

SELO = u'<p class="selo-demo selo-demo--bloco">Demonstração — conversa simulada</p>'


def esc(t):
    """Escapa para texto dentro de HTML."""
    return (t.replace(u"&", u"&amp;").replace(u"<", u"&lt;").replace(u">", u"&gt;"))


def esc_attr(t):
    return esc(t).replace(u'"', u"&quot;")


# ---------------------------------------------------------------------------
# 1. O celular
# ---------------------------------------------------------------------------

def _balao_estatico(msg):
    """Primeiro cenario ja renderizado no HTML.

    Motivo: sem JavaScript o visitante ainda le a conversa inteira, e o Google
    e as IAs leem o texto (que e justamente o que explica o servico).
    """
    enviada = msg.get("de") == "agente"
    classe = u"wa-linha--enviada" if enviada else u"wa-linha--recebida"
    partes = [u'<p>%s</p>' % esc(p) for p in msg.get("texto", u"").split(u"\n") if p.strip()]
    if msg.get("opcoes"):
        partes.append(u'<ul class="wa-opcoes">%s</ul>'
                      % u"".join(u"<li>%s</li>" % esc(o) for o in msg["opcoes"]))
    check = (u'<svg class="wa-check" width="15" height="11" viewBox="0 0 16 11" fill="none" '
             u'aria-hidden="true"><path d="M1 5.5 4.2 8.7 10.2 1" stroke="currentColor" '
             u'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
             u'<path d="M5.8 5.5 9 8.7 15 1" stroke="currentColor" stroke-width="1.6" '
             u'stroke-linecap="round" stroke-linejoin="round"/></svg>') if enviada else u""
    partes.append(u'<div class="wa-meta">%s%s</div>' % (esc(msg.get("hora", u"")), check))
    return (u'\n            <div class="wa-linha %s"><div class="wa-balao">%s</div></div>'
            % (classe, u"".join(partes)))


def demo_em_artigo(roteiro, id_secao="demonstracao", paragrafos=()):
    """A mesma demonstracao, sem o invólucro de <section>, para caber dentro do
    corpo de um artigo do blog (coluna de 720px). Empilha em vez de dividir."""
    return demo_whatsapp(roteiro, id_secao=id_secao, paragrafos=paragrafos,
                         coluna=True)


def demo_whatsapp(roteiro, id_secao="demonstracao", espelhado=False,
                  paragrafos=(), coluna=False):
    """So o bloco .wa-demo (celular + abas + roteiro em JSON).

    roteiro = dicionario com:
      contato  {nome, iniciais, status}
      dia      texto da etiqueta de data ("Ontem", "Sabado")
      cenarios [{id, rotulo, nota (HTML curto), mensagens:[{de,hora,texto,opcoes,espera}]}]

    'de' e "cliente" (balao branco, esquerda) ou "agente" (balao verde, direita).
    """
    c = roteiro["contato"]
    cenarios = roteiro["cenarios"]
    primeiro = cenarios[0]

    abas = u"".join(
        u'\n            <button type="button" class="wa-cenario-btn" role="tab" '
        u'id="cen-%s-%s" data-cenario="%s" aria-controls="thread-%s" '
        u'aria-selected="%s" tabindex="%s">%s</button>'
        % (id_secao, cen["id"], cen["id"], id_secao,
           u"true" if i == 0 else u"false", u"0" if i == 0 else u"-1", esc(cen["rotulo"]))
        for i, cen in enumerate(cenarios))

    mensagens = u"".join(_balao_estatico(m) for m in primeiro["mensagens"])

    copy = u"".join(u'\n          <p>%s</p>' % p for p in paragrafos)

    return u"""
        <div class="wa-demo%(espelho)s" data-wa-demo>
          <div class="wa-demo-copy">%(copy)s
            <div class="wa-cenarios" role="tablist" aria-label="Cenários da conversa">%(abas)s
            </div>
            <p class="wa-cenario-nota" data-wa-nota>%(nota)s</p>
          </div>

          <div class="wa-demo-device">
            <div class="wa-phone">
              <div class="wa-phone-tela">
                <div class="wa-topo">
                  <span class="wa-avatar" aria-hidden="true">%(iniciais)s</span>
                  <span class="wa-topo-id">
                    <span class="wa-topo-nome">%(nome)s</span>
                    <span class="wa-topo-status">%(status)s</span>
                  </span>
                </div>
                <div class="wa-thread" id="thread-%(id)s" role="tabpanel" data-wa-thread aria-live="polite" aria-label="Conversa de demonstração">
                  <div class="wa-dia">%(dia)s</div>%(mensagens)s
                </div>
                <div class="wa-barra-inferior" aria-hidden="true">
                  <span class="wa-campo">Mensagem</span>
                  <span class="wa-enviar"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M2.01 21 23 12 2.01 3 2 10l15 2-15 2z"/></svg></span>
                </div>
              </div>
            </div>
            <div class="wa-controles">
              <button type="button" class="wa-replay" data-wa-replay>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>
                Ver a conversa de novo
              </button>
              <span class="wa-legenda">
                <span><i class="wa-cor-cliente"></i>Cliente</span>
                <span><i class="wa-cor-agente"></i>Agente</span>
              </span>
            </div>
            %(selo)s
          </div>

          <script type="application/json" data-wa-roteiro>%(json)s</script>
        </div>
""" % {
        "id": id_secao,
        "copy": copy,
        "abas": abas,
        "nota": primeiro.get("nota", u""),
        "espelho": ((u" wa-demo--espelhado" if espelhado else u"")
                    + (u" wa-demo--coluna" if coluna else u"")),
        "iniciais": esc(c["iniciais"]),
        "nome": esc(c["nome"]),
        "status": esc(c.get("status", u"on-line")),
        "dia": esc(roteiro.get("dia", u"Hoje")),
        "mensagens": mensagens,
        "selo": SELO,
        "json": json.dumps(roteiro, ensure_ascii=False),
    }


def bloco_whatsapp(titulo, tag, intro, roteiro, id_secao="demonstracao",
                   espelhado=False, paragrafos=()):
    """A secao inteira da demonstracao, para as paginas comerciais."""
    return u"""
    <section class="solution-section" id="%(id)s">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%(tag)s</div>
          <h2 class="section-title">%(titulo)s</h2>
          <p class="section-desc">%(intro)s</p>
        </div>
%(demo)s      </div>
    </section>
""" % {"id": id_secao, "tag": esc(tag), "titulo": esc(titulo), "intro": esc(intro),
       "demo": demo_whatsapp(roteiro, id_secao=id_secao, espelhado=espelhado,
                             paragrafos=paragrafos)}


# ---------------------------------------------------------------------------
# 2. Fluxo
# ---------------------------------------------------------------------------

def bloco_fluxo(titulo, tag, intro, passos):
    """passos = [(titulo, texto, etiqueta_de_tempo_ou_None), ...]"""
    itens = u"".join(
        u'\n          <article class="fluxo-passo"><h3>%s</h3><p>%s</p>%s</article>'
        % (esc(t), esc(p), (u'<span class="fluxo-tempo">%s</span>' % esc(q)) if q else u"")
        for t, p, q in passos)
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="fluxo">%s
        </div>
      </div>
    </section>
""" % (esc(tag), esc(titulo), esc(intro), itens)


# ---------------------------------------------------------------------------
# 3. Calculadora
# ---------------------------------------------------------------------------

def bloco_calculadora(tipo, titulo, tag, intro, campos, rotulo_resultado, rodape):
    """campos = [(nome, label, min, max, passo, valor_inicial, formato, sufixo,
                  escala_min, escala_max)]

    formato: "reais" mostra R$; qualquer outra coisa mostra o numero cru + sufixo.
    A conta em si esta no agentes-ia.js (funcao montarCalculadora).
    """
    html_campos = u"".join(
        u'\n            <div class="calc-campo">'
        u'\n              <label for="calc-%(t)s-%(n)s">%(l)s '
        u'<span class="calc-valor-atual" data-eco="%(n)s"></span></label>'
        u'\n              <input type="range" id="calc-%(t)s-%(n)s" data-campo="%(n)s" '
        u'min="%(min)s" max="%(max)s" step="%(passo)s" value="%(val)s" '
        u'data-formato="%(fmt)s" data-sufixo="%(suf)s">'
        u'\n              <div class="calc-escala"><span>%(emin)s</span><span>%(emax)s</span></div>'
        u'\n            </div>'
        % {"t": tipo, "n": n, "l": esc(l), "min": mn, "max": mx, "passo": st,
           "val": vi, "fmt": fmt, "suf": esc_attr(suf),
           "emin": esc(emin), "emax": esc(emax)}
        for n, l, mn, mx, st, vi, fmt, suf, emin, emax in campos)

    return u"""
    <section class="solution-section" id="calculadora">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%(tag)s</div>
          <h2 class="section-title">%(titulo)s</h2>
          <p class="section-desc">%(intro)s</p>
        </div>
        <div class="calc" data-calc="%(tipo)s">
          <div class="calc-campos">%(campos)s
          </div>
          <div class="calc-resultado">
            <span class="calc-resultado-rotulo">%(rot)s</span>
            <strong class="calc-resultado-numero" data-calc-numero aria-live="polite">R$ 0</strong>
            <span class="calc-resultado-obs" data-calc-obs></span>
          </div>
          <p class="calc-rodape">%(rodape)s</p>
        </div>
      </div>
    </section>
""" % {"tag": esc(tag), "titulo": esc(titulo), "intro": esc(intro), "tipo": tipo,
       "campos": html_campos, "rot": esc(rotulo_resultado), "rodape": rodape}


# ---------------------------------------------------------------------------
# 4. Painel / relatorio
# ---------------------------------------------------------------------------

def bloco_painel(titulo, tag, intro, nome_painel, numeros, alturas, legenda):
    """numeros = [(valor, descricao, destaque_bool)]; alturas = lista de % das barras."""
    nums = u"".join(
        u'\n              <div class="painel-num"><strong%s>%s</strong><span>%s</span></div>'
        % (u' class="eh-bom"' if bom else u"", esc(v), esc(d))
        for v, d, bom in numeros)
    barras = u"".join(u'<i style="height:%s%%"></i>' % a for a in alturas)
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%(tag)s</div>
          <h2 class="section-title">%(titulo)s</h2>
          <p class="section-desc">%(intro)s</p>
        </div>
        <div class="painel">
          <div class="painel-topo">
            <span class="painel-bolinhas" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="painel-titulo">%(nome)s</span>
          </div>
          <div class="painel-corpo">
            <div class="painel-numeros">%(nums)s
            </div>
            <div class="painel-grafico" role="img" aria-label="%(legenda)s">%(barras)s</div>
          </div>
        </div>
        %(selo)s
      </div>
    </section>
""" % {"tag": esc(tag), "titulo": esc(titulo), "intro": esc(intro),
       "nome": esc(nome_painel), "nums": nums, "barras": barras,
       "legenda": esc_attr(legenda),
       "selo": SELO.replace(u"conversa simulada", u"números de exemplo")}


# ---------------------------------------------------------------------------
# 5. Linha do tempo
# ---------------------------------------------------------------------------

def bloco_linha_tempo(titulo, tag, intro, etapas):
    """etapas = [(hora, titulo, texto)] - a ultima ganha destaque."""
    itens = u""
    for i, (hora, tit, txt) in enumerate(etapas):
        fim = u' class="linha-tempo--fim"' if i == len(etapas) - 1 else u""
        itens += (u'\n          <li%s><span class="linha-tempo-hora">%s</span>'
                  u'<h3>%s</h3><p>%s</p></li>' % (fim, esc(hora), esc(tit), esc(txt)))
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <ol class="linha-tempo">%s
        </ol>
      </div>
    </section>
""" % (esc(tag), esc(titulo), esc(intro), itens)


# ---------------------------------------------------------------------------
# 6. Antes / depois
# ---------------------------------------------------------------------------

def bloco_antes_depois(titulo, tag, intro, t_antes, antes, t_depois, depois):
    def col(classe, tit, itens):
        return (u'\n          <div class="ad-col%s"><h3>%s</h3><ul>%s</ul></div>'
                % (classe, esc(tit),
                   u"".join(u"<li>%s</li>" % esc(i) for i in itens)))
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">%s</div>
          <h2 class="section-title">%s</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="antes-depois">%s%s
        </div>
      </div>
    </section>
""" % (esc(tag), esc(titulo), esc(intro),
       col(u"", t_antes, antes), col(u" ad-col--depois", t_depois, depois))


# ---------------------------------------------------------------------------
# 7. Depoimentos REAIS
# ---------------------------------------------------------------------------
# Sao os mesmos tres que ja estao na home, com nome real e autorizacao.
# A legenda deixa claro que sao clientes de consultoria de SEO - nao de
# automacao. Inventar depoimento de automacao seria mentira e, marcado como
# dado estruturado, violacao de politica do Google.

DEPOIMENTOS = [
    (u"Excelente trabalho de otimização do perfil Google. A consultoria ajudou minha "
     u"confeitaria a aparecer muito melhor nas buscas e hoje consigo ver minha confeitaria "
     u"no topo em várias pesquisas da região. O que mais gostei foi a forma clara e "
     u"objetiva de explicar tudo, sem promessas fáceis ou milagrosas.",
     u"Laís Breitenbach Simão", u"Confeitaria — Goiânia/GO"),
    (u"Serviço impecável, ágil e direto ao ponto. Um parceiro estratégico confiável que "
     u"cumpre os prazos e garante a eficiência necessária para o fluxo da nossa operação. "
     u"Atendimento altamente profissional. Recomendo fortemente.",
     u"Marcius Fleury", u"Cliente — Goiânia/GO"),
    (u"A consultoria que fez meu comércio local aparecer no Google Maps em Goiânia. "
     u"Serviço excelente.",
     u"Fátima Isabel Breitenbach Simão", u"Comércio local — Goiânia/GO"),
]


def bloco_depoimentos(nota_honestidade):
    cards = u"".join(
        u'\n          <figure class="depoimento-card">'
        u'\n            <div class="depoimento-estrelas" aria-label="5 de 5 estrelas">★★★★★</div>'
        u'\n            <blockquote><p>%s</p></blockquote>'
        u'\n            <figcaption><strong>%s</strong><span>%s</span></figcaption>'
        u'\n          </figure>' % (esc(t), esc(n), esc(c))
        for t, n, c in DEPOIMENTOS)
    return u"""
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Quem já trabalhou comigo</div>
          <h2 class="section-title">O que os clientes escreveram, com o nome deles</h2>
          <p class="section-desc">%s</p>
        </div>
        <div class="depoimentos-grid">%s
        </div>
      </div>
    </section>
""" % (esc(nota_honestidade), cards)


# ---------------------------------------------------------------------------
# 8. FAQ + faixa final
# ---------------------------------------------------------------------------

def bloco_faq(titulo, perguntas):
    itens = u"".join(
        u'\n          <details class="faq-item">'
        u'\n            <summary><h3>%s</h3></summary>'
        u'\n            <p>%s</p>'
        u'\n          </details>' % (esc(p), esc(r)) for p, r in perguntas)
    return u"""
    <section class="solution-section" id="faq">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">%s</h2>
        </div>
        <div class="faq-list">%s
        </div>
      </div>
    </section>
""" % (esc(titulo), itens)


def bloco_cta(titulo, texto, link_wa, slug, rotulo=u"Pedir um orçamento no WhatsApp"):
    return u"""
    <section class="cta-band">
      <div class="container cta-band-inner">
        <h2>%s</h2>
        <p>%s</p>
        <a class="btn btn-whatsapp btn-lg" href="%s" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="cta_band" data-page="%s">%s</a>
      </div>
    </section>
""" % (esc(titulo), esc(texto), link_wa, slug, esc(rotulo))


# ---------------------------------------------------------------------------
# 9. Esqueleto da pagina
# ---------------------------------------------------------------------------

def cta_mobile(slug):
    """Barra fixa do celular. Nestas paginas nao ha tabela de precos, entao o
    primeiro botao leva para a demonstracao (que e o que vende) e nao para
    uma ancora #pacotes que nao existe aqui."""
    msg = u"Olá, Renan! Vi a página de agentes de IA e quero um orçamento."
    return (
        u'  <!-- RCB:CTA-MOBILE -->\n'
        u'  <div class="cta-mobile" aria-label="Ações rápidas">\n'
        u'    <a href="#demonstracao" class="btn btn-outline" data-event="cta_click" '
        u'data-location="cta_mobile_demo" data-page="%s">Ver funcionando</a>\n'
        u'    <a href="%s" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer" '
        u'data-event="cta_click" data-location="cta_mobile_whatsapp" '
        u'data-page="%s">Pedir orçamento</a>\n'
        u'  </div>\n\n' % (slug, P.wa(msg), slug)
    )


def montar_pagina(destino, slug, url, title, desc, og_title, og_desc, schema, corpo,
                  com_js=True, doador_path=None, marca_main="<main id=",
                  ld_unico=False):
    """Clona head/nav/rodape de uma pagina doadora e troca o miolo.

    Padrao: /consultor-seo-goiania/ (paginas comerciais). Os artigos do blog
    usam outro doador e abrem com "<main>" sem atributo - dai o marca_main.

    A pagina doadora e so lida - nunca escrita. Idempotente: sobrescreve o
    arquivo de destino inteiro a cada execucao.
    """
    doador = io.open(doador_path or DOADOR, encoding="utf-8", newline="").read()
    head = doador[:doador.index("</head>")]
    nav = doador[doador.index("<body"):doador.index(marca_main)]
    rodape = doador[doador.index("</main>") + len("</main>"):]

    def troca(padrao, valor, texto):
        return re.sub(padrao, lambda m: m.group(1) + valor + m.group(2), texto,
                      flags=re.I | re.S)

    head = re.sub(r"(?is)<title>.*?</title>", lambda m: u"<title>%s</title>" % title, head)
    head = troca(r'(<meta name="description" content=")[^"]*(")', desc, head)
    head = troca(r'(<link rel="canonical" href=")[^"]*(")', url, head)
    head = troca(r'(<link rel="alternate" hreflang="pt-BR" href=")[^"]*(")', url, head)
    head = troca(r'(<meta property="og:url" content=")[^"]*(")', url, head)
    head = troca(r'(<meta property="og:title" content=")[^"]*(")', og_title, head)
    head = troca(r'(<meta name="twitter:title" content=")[^"]*(")', og_title, head)
    head = troca(r'(<meta property="og:description" content=")[^"]*(")', og_desc, head)
    head = troca(r'(<meta name="twitter:description" content=")[^"]*(")', og_desc, head)
    head = troca(r'(<meta property="og:image" content=")[^"]*(")', OG_IMG, head)
    head = troca(r'(<meta name="twitter:image" content=")[^"]*(")', OG_IMG, head)

    novo_ld = (u'<script type="application/ld+json">\n%s\n  </script>'
               % json.dumps(schema, ensure_ascii=False, indent=2))
    # ATENCAO: os artigos do blog trazem TRES blocos JSON-LD. Trocar so o
    # primeiro deixaria dois com os dados do artigo doador. Por isso, quando
    # ld_unico=True, todos sao apagados e entra um so.
    if ld_unico:
        primeiro = [True]

        def _troca_ld(m):
            if primeiro[0]:
                primeiro[0] = False
                return novo_ld
            return u""
        head = re.sub(r'(?is)\s*<script type="application/ld\+json">.*?</script>',
                      _troca_ld, head)
    else:
        head = re.sub(r'(?is)<script type="application/ld\+json">.*?</script>',
                      lambda m: novo_ld, head, count=1)

    # folha de estilo propria da linha, logo depois da global
    if CSS not in head:
        head = head.replace('<link rel="stylesheet" href="/styles.min.css">',
                            '<link rel="stylesheet" href="/styles.min.css">\n  ' + CSS, 1)

    # o rotulo do GA4 tem que bater com a URL. Troca qualquer data-page herdado
    # do doador (comercial ou artigo) pelo slug desta pagina.
    novo_dp = 'data-page="%s"' % slug
    nav = re.sub(r'data-page="[^"]*"', novo_dp, nav)
    rodape = re.sub(r'data-page="[^"]*"', novo_dp, rodape)
    # estas paginas nao tem tabela de precos: a ancora #pacotes viraria link morto
    nav = nav.replace('href="#pacotes"', 'href="/#pacotes"')
    rodape = re.sub(r"(?s)<!-- RCB:CTA-MOBILE -->.*?</div>\r?\n",
                    lambda m: cta_mobile(slug), rodape, count=1)

    # ATENCAO: o doador esta gravado com quebra de linha do Windows (CRLF).
    # Procurar por "...</script>\n" nao casa. Por isso a insercao e por regex,
    # que aceita as duas formas e devolve a mesma quebra que encontrou.
    if com_js and JS.strip() not in rodape:
        rodape = re.sub(
            r'(  <script src="/script\.js" defer></script>(\r?\n))',
            lambda m: m.group(1) + JS.rstrip("\n") + m.group(2),
            rodape, count=1)

    html = head + u"</head>\n" + nav + corpo + rodape
    pasta = os.path.dirname(destino)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    return len(html)


# ---------------------------------------------------------------------------
# 10. Schema
# ---------------------------------------------------------------------------

LOCALBUSINESS = {
    "@type": "LocalBusiness", "@id": "https://rcbseo.com.br/#localbusiness",
    "name": "RCB Consultoria", "url": "https://rcbseo.com.br/",
    "telephone": "+5562991161040",
    "address": {"@type": "PostalAddress", "streetAddress": "Rua 18-A, 256",
                "addressLocality": u"Goiânia", "addressRegion": "GO",
                "postalCode": "74070-060", "addressCountry": "BR"},
}


def schema_pagina(url, title, desc, trilha, servico=None, faq=None):
    """Monta o @graph da pagina.

    Nao inclui 'offers' de proposito: a linha nova nao tem preco publicado.
    Nao inclui AggregateRating: os depoimentos sao de outro servico.
    """
    grafo = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title,
         "description": desc, "inLanguage": "pt-BR",
         "isPartOf": {"@type": "WebSite", "@id": "https://rcbseo.com.br/#website",
                      "name": "RCB Consultoria", "url": "https://rcbseo.com.br/"},
         "breadcrumb": {"@id": url + "#breadcrumb"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb",
         "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": nome, "item": item}
             for i, (nome, item) in enumerate(trilha)]},
        {"@type": "Person", "@id": "https://rcbseo.com.br/#renan",
         "name": "Renan Carvalho Barbosa",
         "jobTitle": u"Consultor de SEO local e automação",
         "url": "https://rcbseo.com.br/consultor-seo-goiania/",
         "worksFor": {"@id": "https://rcbseo.com.br/#localbusiness"}},
        dict(LOCALBUSINESS),
    ]
    if servico:
        grafo.append(servico)
    if faq:
        grafo.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": p,
             "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in faq]})
    return {"@context": "https://schema.org", "@graph": grafo}
