# -*- coding: utf-8 -*-
"""
Gera /blog/velocidade-sites-construtoras-goiania/ (24/11/2026): teste real de velocidade no celular dos
sites das construtoras e incorporadoras associadas à ADEMI-GO. Mesmo método do teste das clínicas
(gerar-benchmark-clinicas.py) e o mesmo molde de página.

DADOS: data/benchmark-construtoras.json (pasta interna, bloqueada no site), gravado por
    python scripts/medir-velocidade-sites.py data/benchmark-construtoras-selecao.json data/benchmark-construtoras.json
e completado à mão: "plataforma" (lida dos "sinais" que o medidor achou) e, no "fora", o "motivo" em
texto para o público (sem o nome da empresa). Formato completo no topo do medidor.
Sem resultado medido o script PARA: a página nunca vai ao ar com tabela vazia ou número de exemplo
(regra de 08/09/2026: nada de pesquisa inventada). Todo número do texto sai dos dados.
Com "mostrar_nomes": false a tabela mostra "Construtora A, B, C..." e o CSV não traz o endereço.

Saída: a página + benchmark-construtoras.csv (o "baixar os dados" que outros sites podem citar).
Uso:  python scripts/gerar-benchmark-construtoras.py [--previa PASTA] [--dados ARQUIVO]
Quem linka para cá: /marketing-para-construtoras/ e /blog/landing-page-para-construtora/ (texto-fonte em
scripts/conteudo/nichos_2026_11_*.py) e o teste das clínicas (relacionados do gerar-benchmark-clinicas.py).
"""
import csv
import importlib.util
import io
import json
import os
import re
import statistics
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("servicos", os.path.join(AQUI, "gerar-servicos-marketing.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)
M, rcb_copy, e = S.M, S.rcb_copy, S.e

SLUG = "blog/velocidade-sites-construtoras-goiania"
DP = SLUG.replace("/", "-")  # data-page do GA4
DADOS = os.path.join(S.RAIZ, "data", "benchmark-construtoras.json")
CSV = "benchmark-construtoras.csv"
ADEMI = "https://ademigo.com.br/associados"
FONTE_LENTIDAO = "https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/page-load-time-statistics/"
FONTE_CHROME = "https://blog.google/security/https-by-defau/"  # "HTTPS by default", Google, 28/10/2025
AVISO_NOMES = {False: "Nomes trocados por letras.",
               True: "As notas valem para o dia do teste: o site pode ter mudado depois. "
                     "É responsável por uma das construtoras e quer um teste novo? Fale comigo no WhatsApp."}
WA_SIM = ("link", "botão")


def faixa(score):
    if score >= 90:
        return "status-good", "Rápido"
    if score >= 50:
        return "status-mid", "Razoável"
    return "status-bad", "Lento"


def br(d):
    a, m, dia = d.split("-")
    return "%s/%s/%s" % (dia, m, a)


def num(x):
    return ("%.1f" % x).replace(".", ",")


def contagem(n, um, varios):
    """'um site' / '3 sites' (o número por extenso só no singular)."""
    return um if n == 1 else "%d %s" % (n, varios)


def conclusoes(rs):
    """Números das conclusões, todos calculados dos dados (nada escrito à mão no texto)."""
    notas = [r["score"] for r in rs]
    lcps = [r["lcp"] for r in rs]
    pesos = [r["peso_mb"] for r in rs]
    wp = [r["score"] for r in rs if r["plataforma"] == "WordPress"]
    outros = [r["score"] for r in rs if r["plataforma"] != "WordPress"]
    return dict(
        media=round(statistics.mean(notas)), mediana=round(statistics.median(notas)),
        lentos=sum(1 for x in notas if x < 50), medios=sum(1 for x in notas if 50 <= x < 90),
        rapidos=sum(1 for x in notas if x >= 90), maior=max(notas), menor=min(notas),
        lcp_mediana=num(statistics.median(lcps)), lcp_ok=sum(1 for x in lcps if x <= 2.5),
        lcp_menor=num(min(lcps)), lcp_maior=num(max(lcps)), lcp_10=sum(1 for x in lcps if x > 10),
        peso_mediana=num(statistics.median(pesos)), peso_maior=num(max(pesos)),
        peso_5=sum(1 for x in pesos if x >= 5),
        n_video=sum(1 for r in rs if r["video_mb"] >= 0.1),
        lcp_video=sum(1 for r in rs if r["lcp_elemento"] == "video"),
        n_wp=len(wp), media_wp=round(statistics.mean(wp)) if wp else 0,
        n_outros=len(outros), media_outros=round(statistics.mean(outros)) if outros else 0,
        n_wa=sum(1 for r in rs if r["whatsapp"] in WA_SIM),
        sem_cadeado=sum(1 for r in rs if r["https"] == "não"),
        parcial=sum(1 for r in rs if r["https"] == "parcial"),
    )


def pagina(dados):
    rs = sorted(dados["resultados"], key=lambda r: (-r["score"], r["lcp"]))
    for i, r in enumerate(rs):
        r["rotulo"] = r["nome"] if dados.get("mostrar_nomes") else "Construtora %s" % chr(65 + i)
    c = conclusoes(rs)
    n, quando, fora = len(rs), br(dados["data"]), dados.get("fora") or []
    n_lista = n + len(fora)  # empresas da lista da ADEMI-GO; título e H1 contam só as medidas
    h1 = ("Testamos o site de %d construtoras de Goiânia no celular. Nenhum chegou ao verde." % n
          if c["rapidos"] == 0 else
          "Testamos o site de %d construtoras de Goiânia no celular. Só um chegou ao verde." % n
          if c["rapidos"] == 1 else
          "Testamos o site de %d construtoras de Goiânia no celular" % n)
    p = {
        "slug": SLUG, "trilha": "Velocidade dos sites de construtoras", "data": dados["data"],
        "mostrar_nomes": bool(dados.get("mostrar_nomes")),
        "title": M.titulo("Construtoras de Goiânia: %d Sites Testados no Celular | RCB SEO" % n),
        "desc": ("Testamos no celular o site de %d construtoras de Goiânia: média %d de 100%s. "
                 "Veja a tabela, o que mais pesa e baixe os dados."
                 % (n, c["media"], " e nenhum no verde" if c["rapidos"] == 0
                    else " e só um no verde" if c["rapidos"] == 1 else "")),
        "msg": "Olá, Renan! Vi o teste de velocidade das construtoras e quero saber a nota do site da minha.",
        "faq_titulo": "Perguntas frequentes sobre o teste das construtoras",
        "faq": [
            ("Por que só as associadas da ADEMI-GO?",
             "Para não escolher a dedo. A lista de associadas é pública, reúne construtoras e incorporadoras de "
             "Goiânia e região, e qualquer pessoa pode conferir quem está nela."),
            ("Por que testar a página inicial?",
             "Porque é o endereço que a própria construtora informa à associação e o primeiro que o comprador "
             "abre quando procura o nome da empresa. A página de cada empreendimento pode ser mais rápida ou "
             "mais lenta."),
            ("A nota muda se eu testar de novo?",
             "Muda um pouco, sim. O PageSpeed simula um celular numa internet média, e cada teste varia alguns "
             "pontos. Por isso rodamos cada site três vezes e usamos a nota do meio."),
            ("Posso testar o site da minha construtora sozinho?",
             "Pode. Abra o PageSpeed Insights, cole o endereço do site e olhe a aba Celular. A nossa página de "
             "ferramentas grátis explica como ler o resultado."),
        ],
        "relacionados": [
            ("/marketing-para-construtoras/", "Marketing para construtoras",
             "O contato certo para cada empreendimento."),
            ("/blog/landing-page-para-construtora/", "Landing page para construtora",
             "O que a página de cada lançamento precisa ter."),
            ("/blog/velocidade-sites-clinicas-goiania/", "O teste das clínicas",
             "O mesmo teste feito com os sites de clínicas de Goiânia."),
        ],
        "cta_final": ("Quer saber a nota do site da sua construtora?",
                      "Me chama no WhatsApp e eu rodo o teste na hora, com você, e explico o resultado sem "
                      "complicação."),
    }
    linhas = "".join(
        '\n              <tr><td>%s</td><td class="bench-num">%d</td><td><span class="%s">%s</span></td>'
        '<td>%s&nbsp;s</td><td>%s&nbsp;MB</td><td>%s</td></tr>'
        % (e(r["rotulo"]), r["score"], *faixa(r["score"]), num(r["lcp"]), num(r["peso_mb"]),
           "Sim" if r["whatsapp"] in WA_SIM else "Não")
        for r in rs)
    nota_fora = ""
    if fora:
        nota_fora = " %s fora da conta: %s." % (
            "Um site ficou" if len(fora) == 1 else "%d sites ficaram" % len(fora),
            "; ".join(e(f["motivo"]) for f in fora))
    lentos_txt = []
    for qtd, txt in ((c["lentos"], "na faixa vermelha"), (c["medios"], "na laranja"), (c["rapidos"], "na verde")):
        if qtd:
            lentos_txt.append("%d %s" % (qtd, txt))
    faixas_txt = (", ".join(lentos_txt[:-1]) + " e " + lentos_txt[-1]) if len(lentos_txt) > 1 else lentos_txt[0]
    if c["n_video"]:
        video = (" Em %s a página carrega vídeo logo na abertura%s." % (
            contagem(c["n_video"], "um site", "sites"),
            (", e em %s o vídeo é o próprio conteúdo principal" % contagem(c["lcp_video"], "um deles", "deles"))
            if c["lcp_video"] else ""))
    else:
        video = " Nenhum site carrega vídeo na abertura: o peso vem das fotos e dos recursos extras."
    cadeado = []
    if c["sem_cadeado"]:
        cadeado.append(
            "%s não %s o cadeado de site seguro funcionando. Desde outubro de 2026, o Google Chrome "
            "<a href=\"%s\" target=\"_blank\" rel=\"noopener\">pede permissão antes do primeiro acesso a um site "
            "assim</a>: quem entra pela primeira vez vê um aviso de conexão não segura antes de ver o imóvel. Para "
            "medir a velocidade, passamos pelo aviso, como faria quem clica em continuar." % (
                contagem(c["sem_cadeado"], "Um site", "sites").capitalize(),
                "tem" if c["sem_cadeado"] == 1 else "têm", FONTE_CHROME))
    if c["parcial"]:
        cadeado.append(
            "Em %s a versão com cadeado funciona, mas quem digita o endereço sem o \"https\" não é levado até ela." % (
                contagem(c["parcial"], "um site", "sites")))
    if not cadeado:
        cadeado.append("Todos os sites medidos têm o cadeado de site seguro e levam para ele sozinhos.")
    # frases que só entram quando os dados confirmam (nada escrito à mão sobre uma empresa)
    verdes = [r for r in rs if r["score"] >= 90]
    verde_leve = (" O único no verde também tem a página mais leve do teste: %s MB." % num(verdes[0]["peso_mb"])
                  if len(verdes) == 1 and verdes[0]["peso_mb"] == min(r["peso_mb"] for r in rs) else "")
    gordo = max(rs, key=lambda r: r.get("maior_arquivo_mb") or 0)
    outros_pesos = [r["peso_mb"] for r in rs if r is not gordo]
    maior_arquivo = ""
    if gordo.get("maior_arquivo_mb") and gordo["maior_arquivo_mb"] > max(outros_pesos):
        tipo = ("foto" if gordo.get("maior_arquivo_mime") == "image/jpeg" else
                "imagem" if gordo.get("maior_arquivo_tipo") == "Image" else
                "vídeo" if gordo.get("maior_arquivo_tipo") == "Media" else "arquivo")
        maior_arquivo = (" O maior arquivo encontrado é uma única %s de %s MB, mais pesada do que a página inteira de "
                         "qualquer outro site do teste." % (tipo, num(gordo["maior_arquivo_mb"])))
    # comparação por ferramenta só quando os dois grupos têm ao menos 3 sites (menos que isso é acaso)
    montagem = "o que pesa é como o site foi montado (tamanho das fotos e dos vídeos, quantidade de recursos extras)"
    if c["n_wp"] >= 3 and c["n_outros"] >= 3:
        perto = abs(c["media_wp"] - c["media_outros"]) < 10
        t4 = ("A ferramenta usada não decidiu a nota" if perto
              else "WordPress ficou %s, mas há rápidos e lentos nos dois grupos" % (
                  "na frente" if c["media_wp"] > c["media_outros"] else "atrás"))
        plataforma_txt = ("%d dos %d sites são feitos em WordPress, com média %d. Os outros %d, feitos sob medida ou "
                          "em outras ferramentas, tiveram média %d. %s" % (
                              c["n_wp"], n, c["media_wp"], c["n_outros"], c["media_outros"],
                              ("A diferença é pequena: %s, não a ferramenta." if perto
                               else "Mesmo assim, %s.") % montagem))
    else:
        t4 = "A ferramenta usada não explica a nota"
        plataforma_txt = ("%d dos %d sites são feitos em WordPress, e ficaram entre %d e %d. Com quase todos na "
                          "mesma ferramenta, a diferença entre eles vem de outro lugar: %s." % (
                              c["n_wp"], n, min(r["score"] for r in rs if r["plataforma"] == "WordPress"),
                              max(r["score"] for r in rs if r["plataforma"] == "WordPress"), montagem)
                          if c["n_wp"] > c["n_outros"] else
                          "Só %d dos %d sites são feitos em WordPress: poucos para comparar ferramentas. A diferença "
                          "entre eles vem de outro lugar: %s." % (c["n_wp"], n, montagem))
    corpo = """    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><a href="/blog/">Blog</a><span>/</span><span>%(trilha)s</span></nav>
        <div class="eyebrow">Teste real · %(quando)s</div>
        <h1 class="page-title">%(h1)s</h1>
        <p class="page-subtitle">Abrimos a página inicial das construtoras e incorporadoras associadas à ADEMI-GO como se fosse um comprador no celular. A nota média foi %(media)d de 100, e o conteúdo principal levou %(lcp_mediana)s segundos para aparecer no site do meio da lista.</p>%(byline)s
      </div>
    </section>

    <section class="solution-section">
      <div class="container bench">
        <p>Antes de ver os números: se quiser testar o site da sua construtora enquanto lê, a nossa <a href="/ferramentas/">página de ferramentas grátis</a> mostra como fazer em dois minutos.</p>
        <h2 class="section-title">Como escolhemos e como testamos</h2>
        <p>Para não escolher a dedo, partimos da <a href="%(ademi)s" target="_blank" rel="noopener">lista pública de associadas da ADEMI-GO</a>, a associação das empresas do mercado imobiliário de Goiás, consultada em %(quando)s: %(n_lista)d empresas de Goiânia e região. Usamos o endereço de site que a própria lista informa e medimos %(n)d sites.%(nota_fora)s</p>
        <p>Usamos o Lighthouse, o mesmo motor de teste que roda dentro do <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener">PageSpeed Insights</a> do Google, no modo celular e com internet 4G lenta simulada. Cada site foi testado três vezes, um de cada vez, e usamos o valor do meio, porque o resultado varia alguns pontos de um teste para outro.</p>
        <p>Também abrimos cada página no navegador, em tela de celular, para ver se ela tem botão ou link de WhatsApp, e conferimos o cadeado de site seguro.</p>
        <p>A nota vai de 0 a 100 e segue as cores do próprio Google: <span class="status-bad">0 a 49 é lento</span>, <span class="status-mid">50 a 89 é razoável</span> e <span class="status-good">90 a 100 é rápido</span>.</p>

        <h2 class="section-title">O resultado</h2>
        <div class="bench-tabela-wrap">
          <table class="bench-tabela">
            <caption>Nota de desempenho no celular, da maior para a menor (%(quando)s). %(aviso_nomes)s</caption>
            <thead><tr><th scope="col">Construtora</th><th scope="col">Nota no celular</th><th scope="col">Situação</th><th scope="col">Conteúdo principal aparece em</th><th scope="col">Peso da página</th><th scope="col">WhatsApp na página</th></tr></thead>
            <tbody>%(linhas)s
            </tbody>
          </table>
        </div>
        <p class="bench-download"><a class="btn btn-outline" href="%(csv)s" download data-event="cta_click" data-location="baixar_dados" data-page="%(dp)s">Baixar os dados (CSV)</a></p>

        <h2 class="section-title">O que os números mostram</h2>
        <h3>1. %(t1)s</h3>
        <p>A média foi <strong>%(media)d</strong> e a nota do meio, %(mediana)d. A maior foi %(maior)d e a menor, %(menor)d. Ficaram %(faixas_txt)s.%(verde_leve)s</p>
        <h3>2. O conteúdo principal demora a aparecer</h3>
        <p>O Google considera bom quando a maior parte da página aparece em até 2,5 segundos. %(lcp_ok_txt)s O tempo do meio da lista foi %(lcp_mediana)s segundos, e os tempos foram de %(lcp_menor)s a %(lcp_maior)s. Lembre que o teste simula uma internet 4G lenta: no Wi-Fi o número cai, mas a diferença entre os sites continua. Na prática, o comprador olha uma tela incompleta enquanto espera.</p>
        <h3>3. Foto e vídeo pesam mais do que parece</h3>
        <p>A página inicial do meio da lista pesa %(peso_mediana)s MB, e a mais pesada chega a %(peso_maior)s MB. %(peso_5_txt)s%(maior_arquivo)s%(video)s Lançamento pede imagem bonita, mas foto e vídeo sem compressão fazem o comprador esperar no celular.</p>
        <h3>4. %(t4)s</h3>
        <p>%(plataforma_txt)s</p>
        <h3>5. %(t5)s</h3>
        <p>%(wa_txt)s</p>
        <h3>6. Cadeado de site seguro</h3>
        <p>%(cadeado)s</p>

        <h2 class="section-title">O que isso significa para a sua construtora</h2>
        <p>Site lento custa visita ao decorado. Um <a href="%(fonte)s" target="_blank" rel="noopener">levantamento do Google</a> mostrou que, quando a página leva de 1 para 3 segundos para abrir no celular, a chance de a pessoa desistir sobe 32%%. Quem procura apartamento compara vários lançamentos; se o seu demora, ele fecha e abre o do concorrente.</p>
        <p>Velocidade é só uma parte de vender pelo site. A outra é aparecer para quem procura imóvel na região, com uma página para cada empreendimento: veja como funciona o <a href="/marketing-para-construtoras/">marketing para construtoras</a> e o que a <a href="/blog/landing-page-para-construtora/">landing page de um lançamento</a> precisa ter.</p>
        <div class="dica-rcb">
          <strong>Dica RCB</strong>
          <p>Quer testar o seu antes de falar com alguém? A nossa <a href="/ferramentas/#pagespeed">página de ferramentas grátis</a> mostra como fazer e como ler a nota.</p>
        </div>
      </div>
    </section>
""" % dict(
        trilha=e(p["trilha"]), quando=quando, aviso_nomes=e(AVISO_NOMES[p["mostrar_nomes"]]), h1=e(h1),
        n_lista=n_lista, n=n, byline=S.autor_data(p), verde_leve=verde_leve, maior_arquivo=maior_arquivo, linhas=linhas, fonte=FONTE_LENTIDAO, ademi=ADEMI, dp=DP, csv=CSV,
        nota_fora=nota_fora, faixas_txt=faixas_txt, video=video, cadeado=" ".join(cadeado),
        t1=("Nenhum site chegou ao verde" if c["rapidos"] == 0
            else "Só um dos %d chegou ao verde" % n if c["rapidos"] == 1
            else "%d de %d chegaram ao verde" % (c["rapidos"], n)),
        lcp_ok_txt=(("Nenhum dos %d sites conseguiu." % n if c["lcp_ok"] == 0
                     else "Só um dos %d sites conseguiu." % n if c["lcp_ok"] == 1
                     else "Só %d dos %d sites conseguiram." % (c["lcp_ok"], n))
                    + (" Em %s, passou de 10 segundos." % contagem(c["lcp_10"], "um deles", "deles")
                       if c["lcp_10"] else "")),
        peso_5_txt=("" if not c["peso_5"] else
                    "%s passa%s de 5 MB só na página inicial." % (
                        contagem(c["peso_5"], "Um site", "sites").capitalize(), "" if c["peso_5"] == 1 else "m")),
        t4=t4, plataforma_txt=plataforma_txt,
        t5=("Todos têm WhatsApp na página" if c["n_wa"] == n
            else "%d de %d têm WhatsApp na página inicial" % (c["n_wa"], n)),
        wa_txt=("Comprador de imóvel quer tirar dúvida na hora, e o WhatsApp é o caminho mais curto até o corretor. "
                + ("Todos os sites medidos têm botão ou link de WhatsApp na página inicial." if c["n_wa"] == n
                   else "%s não %s botão nem link de WhatsApp na página inicial: quem quer conversar precisa achar "
                        "outro caminho, como telefone ou formulário." % (
                            contagem(n - c["n_wa"], "Um site", "sites").capitalize(),
                            "tem" if n - c["n_wa"] == 1 else "têm"))),
        **{k: v for k, v in c.items() if k in ("media", "mediana", "maior", "menor", "lcp_mediana", "lcp_menor",
                                               "lcp_maior", "peso_mediana", "peso_maior")})
    corpo += S.s_faq(p) + S.s_relacionados(p) + S.s_cta_final(p)
    return p, corpo, rs, h1


def schema(p, rs, h1):
    url = "%s/%s/" % (S.BASE, SLUG)
    autor = {"@type": "Person", "@id": "https://rcbseo.com.br/#renan", "name": "Renan Carvalho Barbosa"}
    g = [
        {"@type": "Article", "@id": url + "#article", "headline": h1, "description": p["desc"],
         "url": url, "mainEntityOfPage": url, "inLanguage": "pt-BR", "author": autor,
         "publisher": {"@id": M.ID_EMPRESA}, "datePublished": p["data"], "dateModified": p["data"],
         "image": "https://rcbseo.com.br/assets/img/og-rcb-1200x628.png", "isPartOf": M.site()},
        {"@type": "Dataset", "@id": url + "#dados",
         "name": "Velocidade dos sites de construtoras de Goiânia (PageSpeed Insights, celular)",
         "description": "Nota de desempenho no celular (0 a 100), tempo até o conteúdo principal aparecer, peso "
                        "da página, vídeo na abertura, plataforma, WhatsApp e cadeado de site seguro na página "
                        "inicial de %d sites de construtoras e incorporadoras associadas à ADEMI-GO, medidos com o "
                        "Lighthouse (motor do PageSpeed Insights) em %s. %s" % (
                            len(rs), br(p["data"]),
                            "Inclui o nome de cada construtora." if p["mostrar_nomes"] else "Nomes trocados por letras."),
         "url": url, "creator": autor, "license": "https://creativecommons.org/licenses/by/4.0/",
         "isAccessibleForFree": True, "temporalCoverage": p["data"], "inLanguage": "pt-BR",
         "spatialCoverage": {"@type": "Place", "name": "Goiânia e Aparecida de Goiânia, GO, Brasil"},
         "variableMeasured": ["Nota de desempenho no celular (0 a 100)",
                              "Largest Contentful Paint no celular (segundos)",
                              "Peso da página inicial (MB)", "Vídeo carregado na abertura (MB)",
                              "Plataforma do site", "Link ou botão de WhatsApp na página inicial",
                              "Cadeado de site seguro (https)"],
         "distribution": {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": url + CSV}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": S.BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": S.BASE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["trilha"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def _ler(rel):
    return io.open(os.path.join(S.RAIZ, rel), encoding="utf-8", newline="").read()


def _gravar(rel, texto):
    if _ler(rel) != texto:
        io.open(os.path.join(S.RAIZ, rel), "w", encoding="utf-8", newline="").write(texto)
        return True
    return False


def _linha(texto, url, nova, depois_de):
    """Troca a linha que cita `url` por `nova`; se não houver, põe `nova` logo depois da linha que
    começa com `depois_de`. Respeita a quebra de linha do arquivo (CRLF no Windows)."""
    nl = "\r\n" if "\r\n" in texto else "\n"
    linhas = texto.split(nl)
    for i, x in enumerate(linhas):
        if url in x:
            linhas[i] = nova
            return nl.join(linhas)
    for i, x in enumerate(linhas):
        if x.startswith(depois_de):
            linhas.insert(i + 1, nova)
            return nl.join(linhas)
    raise SystemExit("âncora não encontrada: %r" % depois_de)


def integrar(dados, c, total):
    """Sitemap e os dois llms (o que as IAs leem). Idempotente: a 2ª execução não muda nada."""
    url = "%s/%s/" % (S.BASE, SLUG)
    mudou = []
    sm = _ler("sitemap.xml")
    if "<loc>%s</loc>" % url not in sm:
        nl = "\r\n" if "\r\n" in sm else "\n"
        bloco = nl.join(["  <url>", "    <loc>%s</loc>" % url, "    <lastmod>%s</lastmod>" % dados["data"],
                         "    <changefreq>monthly</changefreq>", "    <priority>0.7</priority>", "  </url>",
                         "</urlset>"])
        sm = sm.replace("</urlset>", bloco, 1)
    else:  # mantém o lastmod igual à data do teste
        sm = re.sub(r"(<loc>%s</loc>\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(url),
                    lambda m: m.group(1) + dados["data"] + m.group(2), sm)
    if _gravar("sitemap.xml", sm):
        mudou.append("sitemap.xml")
    clin = json.load(io.open(os.path.join(S.RAIZ, "data", "benchmark-clinicas.json"), encoding="utf-8"))
    notas_clin = [r["score"] for r in clin["resultados"]]
    url_clin = "%s/blog/velocidade-sites-clinicas-goiania/" % S.BASE
    d_clin = ("Teste de velocidade no celular dos sites de %d clínicas de Goiânia (dados próprios, %s): "
              "Lighthouse, 3 testes por site; média %d de 100%s. Tabela e dados para baixar (CSV)." % (
                  len(clin["resultados"]) + len(clin.get("fora") or []), br(clin["data"]),
                  round(statistics.mean(notas_clin)),
                  ", nenhum no verde" if not any(x >= 90 for x in notas_clin) else ""))
    d_cons = ("Teste de velocidade no celular dos sites de %d construtoras e incorporadoras associadas à ADEMI-GO "
              "(dados próprios, %s): Lighthouse, 3 testes por site; média %d de 100%s; conteúdo principal em "
              "%s segundos no site do meio da lista. Tabela e dados para baixar (CSV)." % (
                  total, br(dados["data"]), c["media"], ", nenhum no verde" if c["rapidos"] == 0 else "",
                  c["lcp_mediana"]))
    t = _ler("llms.txt")
    ferr = "- Ferramentas grátis para ver sua empresa no Google:"
    t = _linha(t, url_clin, "- Velocidade dos sites de clínicas de Goiânia: %s. %s" % (url_clin, d_clin), ferr)
    t = _linha(t, url, "- Velocidade dos sites de construtoras de Goiânia: %s. %s" % (url, d_cons),
               "- Velocidade dos sites de clínicas de Goiânia:")
    if _gravar("llms.txt", t):
        mudou.append("llms.txt")
    f = _ler("llms-full.txt")
    ferr_full = "* Ferramentas grátis para ver sua empresa no Google:"
    f = _linha(f, url_clin, "* Velocidade dos sites de clínicas de Goiânia: %s. %s" % (url_clin, d_clin), ferr_full)
    f = _linha(f, url, "* Velocidade dos sites de construtoras de Goiânia: %s. %s" % (url, d_cons),
               "* Velocidade dos sites de clínicas de Goiânia:")
    if _gravar("llms-full.txt", f):
        mudou.append("llms-full.txt")
    return mudou


def main():
    global DADOS
    if "--dados" in sys.argv:  # teste da montagem com outro arquivo (use junto com --previa)
        DADOS = sys.argv[sys.argv.index("--dados") + 1]
    if not os.path.exists(DADOS):
        sys.exit("Sem dados: rode o medidor (comando no topo deste arquivo).")
    dados = json.load(io.open(DADOS, encoding="utf-8"))
    rs = dados.get("resultados") or []
    if len(rs) < 5 or any(not (0 <= r.get("score", -1) <= 100) for r in rs):
        sys.exit("Dados insuficientes ou com nota fora de 0 a 100: a página não é gerada.")
    faltando = [r.get("nome") for r in rs
                if not r.get("plataforma") or r.get("lcp") is None or r.get("peso_mb") is None
                or r.get("whatsapp") not in ("link", "botão", "") or r.get("https") not in ("sim", "parcial", "não")
                or len(r.get("notas") or []) != 3]
    if faltando:
        sys.exit("Falta plataforma/lcp/peso/whatsapp/cadeado/3 notas em: %s" % faltando)
    sem_motivo = [f.get("nome") for f in dados.get("fora") or [] if not f.get("motivo")]
    if sem_motivo:
        sys.exit("Site fora da conta sem motivo: %s" % sem_motivo)
    p, corpo, rs, h1 = pagina(dados)
    assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (len(p["title"]), len(p["desc"]))
    S.schema, S.corpo = (lambda _: schema(p, rs, h1)), (lambda _: corpo)  # montar() chama estes dois
    modelo = io.open(os.path.join(S.RAIZ, S.MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    h = S.montar(modelo, dict(p, servico="site"))
    h = h.replace('aria-label="Pedir orçamento de site pelo WhatsApp"',
                  'aria-label="Pedir o teste do meu site pelo WhatsApp"')
    # menu e barra do celular herdam "#orcamento" do modelo (mesmo ajuste de gerar-benchmark-clinicas.py)
    h = h.replace('href="#orcamento"', 'href="/#pacotes"').replace(
        'data-page="%s">Quanto custa?</a>' % SLUG, 'data-page="%s">Orçamento grátis</a>' % SLUG)
    h = h.replace('data-page="%s"' % SLUG, 'data-page="%s"' % DP)
    assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1 and 'href="#orcamento"' not in h
    assert "R$" not in h and '"price"' not in h and "priceRange" not in h
    h = rcb_copy.humanizar(M.texto_html(h))
    miolo = h.split('<main id="main-content">')[1].split("</main>")[0]
    assert "—" not in miolo and "–" not in miolo, "travessão no texto"

    pasta = sys.argv[sys.argv.index("--previa") + 1] if "--previa" in sys.argv else os.path.join(S.RAIZ, SLUG)
    os.makedirs(pasta, exist_ok=True)
    io.open(os.path.join(pasta, "index.html"), "w", encoding="utf-8", newline="\n").write(h)
    nomes = dados.get("mostrar_nomes")
    with io.open(os.path.join(pasta, CSV), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["construtora"] + (["url"] if nomes else [])
                   + ["cidade", "nota_celular", "situacao", "notas_dos_3_testes", "lcp_segundos", "peso_mb",
                      "video_mb", "plataforma", "whatsapp_na_pagina", "cadeado_https", "data_do_teste"])
        for r in rs:
            w.writerow([r["rotulo"]] + ([r["url"]] if nomes else [])
                       + [r["cidade"], r["score"], faixa(r["score"])[1], " ".join(str(x) for x in r["notas"]),
                          r["lcp"], r["peso_mb"], r["video_mb"], r["plataforma"],
                          "sim" if r["whatsapp"] in WA_SIM else "não", r["https"], dados["data"]])
    print("ok  %s  (%d construtoras medidas, %d fora, média %d)" % (
        pasta, len(rs), len(dados.get("fora") or []), round(statistics.mean(r["score"] for r in rs))))
    if "--previa" not in sys.argv:
        print("integração:", ", ".join(integrar(dados, conclusoes(rs), len(rs))) or "sem mudança")


if __name__ == "__main__":
    main()
