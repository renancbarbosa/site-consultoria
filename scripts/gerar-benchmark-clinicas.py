# -*- coding: utf-8 -*-
"""
Gera /blog/velocidade-sites-clinicas-goiania/ (estrutura de 28/10/2026): teste real
de velocidade dos sites de clínicas de Goiânia no PageSpeed Insights (celular).

DADOS: data/benchmark-clinicas.json (pasta interna, bloqueada no site). Formato:
  {"data": "AAAA-MM-DD", "mostrar_nomes": false,
   "fora": [{"clinica", "url", "nicho", "motivo"}],   # sites que não deu para medir
   "resultados": [{"clinica": "...", "url": "https://...", "nicho": "Estética", "plataforma": "WordPress",
                   "prova": "Sim|Parcial|Não", "https": true, "score": 0-100, "lcp": 4.2, "obs": "..."}, ...]}
Medição de 28/10/2026: Lighthouse (motor do PageSpeed), celular, 3 testes por site, mediana.
Sem resultado medido o script PARA: a página nunca vai ao ar com tabela vazia ou
número de exemplo (regra de 08/09/2026: nada de pesquisa inventada).
Com "mostrar_nomes": false a tabela mostra "Clínica A, B, C..." e o CSV não traz URL.

Saída: a página + dados.csv (o "baixar os dados" que outros sites podem citar).
Uso:  python scripts/gerar-benchmark-clinicas.py [--previa PASTA]
      --previa grava fora do site, para conferir antes de publicar.
Esqueleto: o mesmo de gerar-ferramentas.py (montar() do gerador de serviços).
"""
import csv
import importlib.util
import io
import json
import os
import statistics
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("servicos", os.path.join(AQUI, "gerar-servicos-marketing.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)
M, rcb_copy, e = S.M, S.rcb_copy, S.e

SLUG = "blog/velocidade-sites-clinicas-goiania"
DP = SLUG.replace("/", "-")  # data-page do GA4
DADOS = os.path.join(S.RAIZ, "data", "benchmark-clinicas.json")
CSV = "benchmark-dados.csv"
# Com nomes à mostra, a nota vale para o dia do teste e o dono pode pedir um teste novo.
AVISO_NOMES = {False: "Nomes trocados por letras.",
               True: "As notas valem para o dia do teste: o site pode ter mudado depois. "
                     "É responsável por uma das clínicas e quer um teste novo? Fale comigo no WhatsApp."}
FONTE_LENTIDAO = "https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/page-load-time-statistics/"


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


def conclusoes(rs):
    """Números das conclusões, todos calculados dos dados (nada escrito à mão no texto)."""
    notas = [r["score"] for r in rs]
    wp = [r["score"] for r in rs if r["plataforma"] == "WordPress"]
    outros = [r["score"] for r in rs if r["plataforma"] != "WordPress"]
    agencia = [r["score"] for r in rs if r["plataforma"] == "Plataforma de agência"]
    lcps = [r["lcp"] for r in rs]
    return dict(
        media=round(statistics.mean(notas)), mediana=round(statistics.median(notas)),
        lentos=sum(1 for x in notas if x < 50), rapidos=sum(1 for x in notas if x >= 90),
        maior=max(notas), menor=min(notas),
        n_wp=len(wp), media_wp=round(statistics.mean(wp)) if wp else 0,
        n_outros=len(outros), media_outros=round(statistics.mean(outros)) if outros else 0,
        n_agencia=len(agencia), agencia_min=min(agencia) if agencia else 0, agencia_max=max(agencia) if agencia else 0,
        lcp_mediana=num(statistics.median(lcps)), lcp_ok=sum(1 for x in lcps if x <= 2.5),
        lcp_menor=num(min(lcps)), lcp_maior=num(max(lcps)), lcp_10=sum(1 for x in lcps if x > 10),
        prova_sim=sum(1 for r in rs if r["prova"] == "Sim"),
        prova_nao=sum(1 for r in rs if r["prova"] == "Não"),
        prova_vazio=sum(1 for r in rs if "vazio" in r.get("obs", "")),
        sem_redirecionar=sum(1 for r in rs if not r.get("https", True)),
    )


def pagina(dados):
    rs = sorted(dados["resultados"], key=lambda r: -r["score"])
    for i, r in enumerate(rs):
        r["rotulo"] = r["clinica"] if dados.get("mostrar_nomes") else "Clínica %s" % chr(65 + i)
    c = conclusoes(rs)
    media = c["media"]
    n, quando, fora = len(rs), br(dados["data"]), dados.get("fora") or []
    total = n + len(fora)
    h1 = ("Testamos o site de %d clínicas de Goiânia no celular. Nenhum foi rápido." % total
          if c["rapidos"] == 0 else "Testamos o site de %d clínicas de Goiânia no celular" % total)
    p = {
        "slug": SLUG, "trilha": "Velocidade dos sites de clínicas", "data": dados["data"], "mostrar_nomes": bool(dados.get("mostrar_nomes")),
        "title": M.titulo("Sites de Clínicas em Goiânia: %d Testados no Celular | RCB SEO" % total),
        "desc": ("Testamos %d sites de clínicas de Goiânia no celular: média %d de 100%s. "
                 "Veja a tabela, o que mais pesa e baixe os dados."
                 % (total, media, " e nenhum rápido" if c["rapidos"] == 0 else "")),
        "msg": "Olá, Renan! Vi o teste de velocidade das clínicas e quero saber a nota do meu site.",
        "faq_titulo": "Perguntas frequentes sobre o teste de velocidade",
        "faq": [
            ("A nota muda se eu testar de novo?",
             "Muda um pouco, sim. O PageSpeed simula um celular numa internet média, e cada teste varia alguns pontos. "
             "Por isso rodamos cada site três vezes e usamos a nota do meio."),
            ("Nota baixa quer dizer que o site é ruim?",
             "Quer dizer que ele demora para abrir no celular. O site pode ser bonito e bem escrito e ainda assim "
             "fazer o paciente esperar. Velocidade é uma parte do problema, não o problema inteiro."),
            ("Posso testar o meu site sozinho?",
             "Pode. Abra o PageSpeed Insights, cole o endereço do seu site e olhe a aba Celular. A nossa página de "
             "ferramentas grátis explica como ler o resultado."),
        ],
        "relacionados": [
            ("/ferramentas/", "Ferramentas grátis", "Teste o seu site e o seu perfil no Google em poucos minutos."),
            ("/seo-para-clinicas/", "SEO para clínicas", "Como a clínica aparece no Google quando o paciente procura."),
            ("/criacao-de-sites-goiania/", "Criação de sites", "Site rápido no celular, feito para o paciente chamar."),
        ],
        "cta_final": ("Quer saber a nota do seu site?",
                      "Me chama no WhatsApp e eu rodo o teste na hora, com você, e explico o resultado sem complicação."),
    }
    linhas = "".join(
        '\n              <tr><td>%s</td><td class="bench-num">%d</td><td><span class="%s">%s</span></td>'
        '<td>%s</td><td>%s</td><td>%s</td></tr>'
        % (e(r["rotulo"]), r["score"], *faixa(r["score"]), e(r["nicho"]), e(r["plataforma"]), e(r["prova"]))
        for r in rs)
    aviso_nomes = AVISO_NOMES[bool(dados.get("mostrar_nomes"))]
    nota_fora = ""
    if fora:
        nota_fora = (" %s ficou fora da conta: %s." % (
            "Um site" if len(fora) == 1 else "%d sites" % len(fora),
            "; ".join(e(f["motivo"]) for f in fora)))
    if c["sem_redirecionar"]:
        https = ("<p>Todos os sites têm o cadeado de site seguro. Mas %s não leva para a versão com cadeado quem "
                 "digita o endereço sem o \"https\": essa pessoa vê o aviso de \"não seguro\" no navegador. "
                 "É um ajuste de minutos no servidor.</p>" % (
                     "um deles" if c["sem_redirecionar"] == 1 else "%d deles" % c["sem_redirecionar"]))
    else:
        https = "<p>Todos os sites têm o cadeado de site seguro e levam para ele sozinhos.</p>"
    vazio = ""
    if c["prova_vazio"]:
        vazio = (" E %s o quadro de avaliações do Google, mas ele aparece vazio: o espaço existe, a nota não."
                 % ("uma clínica instalou" if c["prova_vazio"] == 1 else "%d clínicas instalaram" % c["prova_vazio"]))
    agencia = ""
    if c["n_agencia"] >= 2:
        agencia = (" %d dos sites usam a mesma plataforma de uma agência, e ficaram entre %d e %d. Com tão poucos "
                   "sites não dá para culpar a plataforma, mas vale o recado: quando o fornecedor monta todos do mesmo "
                   "jeito, o que está lento se repete em todos." % (c["n_agencia"], c["agencia_min"], c["agencia_max"]))
    corpo = """    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><a href="/blog/">Blog</a><span>/</span><span>%(trilha)s</span></nav>
        <div class="eyebrow">Teste real · %(quando)s</div>
        <h1 class="page-title">%(h1)s</h1>
        <p class="page-subtitle">Abrimos a página inicial de %(total)d clínicas de Goiânia como se fosse um paciente no celular. A nota média foi %(media)d de 100, e em %(lcp_10)d dos %(n)d sites medidos o conteúdo principal levou mais de 10 segundos para aparecer.</p>%(byline)s
      </div>
    </section>

    <section class="solution-section">
      <div class="container bench">
        <p>Antes de ver os números: se quiser testar o seu site enquanto lê, a nossa <a href="/ferramentas/">página de ferramentas grátis</a> mostra como fazer em dois minutos.</p>
        <h2 class="section-title">Como testamos</h2>
        <p>Usamos o Lighthouse, o mesmo motor de teste que roda dentro do <a href="https://pagespeed.web.dev/" target="_blank" rel="noopener">PageSpeed Insights</a> do Google, no modo celular e com internet 4G lenta simulada. Cada site foi testado três vezes em %(quando)s e usamos a nota do meio, porque o resultado varia alguns pontos de um teste para outro.%(nota_fora)s</p>
        <p>Também abrimos cada página no navegador, em tela de celular, para ver se ela mostra as avaliações do Google. "Sim" quer dizer nota ou avaliações do Google à vista; "Parcial", depoimentos sem ligação com o Google; "Não", nenhum dos dois.</p>
        <p>A nota vai de 0 a 100 e segue as cores do próprio Google: <span class="status-bad">0 a 49 é lento</span>, <span class="status-mid">50 a 89 é razoável</span> e <span class="status-good">90 a 100 é rápido</span>.</p>

        <h2 class="section-title">O resultado</h2>
        <div class="bench-tabela-wrap">
          <table class="bench-tabela">
            <caption>Nota de desempenho no celular, da maior para a menor (%(quando)s). %(aviso_nomes)s</caption>
            <thead><tr><th scope="col">Clínica</th><th scope="col">Nota no celular</th><th scope="col">Situação</th><th scope="col">Ramo</th><th scope="col">Como o site foi feito</th><th scope="col">Avaliações do Google na página</th></tr></thead>
            <tbody>%(linhas)s
            </tbody>
          </table>
        </div>
        <p class="bench-download"><a class="btn btn-outline" href="%(csv)s" download data-event="cta_click" data-location="baixar_dados" data-page="%(dp)s">Baixar os dados (CSV)</a></p>

        <h2 class="section-title">O que os números mostram</h2>
        <h3>1. %(t1)s</h3>
        <p>A média foi <strong>%(media)d</strong> e a nota do meio, %(mediana)d. A maior foi %(maior)d e a menor, %(menor)d. %(lentos_txt)s</p>
        <h3>2. O conteúdo principal demora a aparecer</h3>
        <p>O Google considera bom quando a maior parte da página aparece em até 2,5 segundos. %(lcp_ok_txt)s O tempo do meio da lista foi %(lcp_mediana)s segundos, e os tempos foram de %(lcp_menor)s a %(lcp_maior)s. Lembre que o teste simula uma internet 4G lenta: no Wi-Fi o número cai, mas a diferença entre os sites continua. Na prática, o paciente olha uma tela incompleta enquanto espera.</p>
        <h3>3. A ferramenta usada não decidiu a nota</h3>
        <p>%(n_wp)d dos sites são feitos em WordPress, com média %(media_wp)d. Os outros %(n_outros)d, feitos sob medida, com ferramenta de IA ou em plataforma de agência, tiveram média %(media_outros)d. Nenhum usa Wix nem Shopify. A diferença é pequena e o melhor e o pior site estão em grupos diferentes: o que pesa é como o site foi montado (tamanho das fotos, quantidade de recursos extras), não a ferramenta.%(agencia)s</p>
        <h3>4. Só %(prova_sim)d de %(n)d mostram as avaliações do Google</h3>
        <p>Quem chega ao site de uma clínica já viu as estrelas no Google, mas na maioria dos sites testados essa prova some. Em %(prova_nao)d deles não há nem depoimento.%(vazio)s</p>
        <h3>5. Cadeado de site seguro</h3>
        %(https)s

        <h2 class="section-title">O que isso significa para a sua clínica</h2>
        <p>Site lento custa paciente. Um <a href="%(fonte)s" target="_blank" rel="noopener">levantamento do Google</a> mostrou que, quando a página leva de 1 para 3 segundos para abrir no celular, a chance de a pessoa desistir sobe 32%%. Quem procura clínica no Google costuma abrir dois ou três resultados; se o seu demora, ele fecha e fica com o próximo.</p>
        <p>Velocidade é só uma parte de aparecer bem para o paciente. A outra é ser encontrado: veja como funciona o <a href="/seo-para-clinicas/">SEO para clínicas</a>, o trabalho de fazer a sua clínica aparecer no Google quando alguém procura pelo tratamento.</p>
        <div class="dica-rcb">
          <strong>Dica RCB</strong>
          <p>Quer testar o seu antes de falar com alguém? A nossa <a href="/ferramentas/#pagespeed">página de ferramentas grátis</a> mostra como fazer e como ler a nota.</p>
        </div>
      </div>
    </section>
""" % dict(trilha=e(p["trilha"]), quando=quando, aviso_nomes=e(aviso_nomes), h1=e(h1), n=n, total=total, byline=S.autor_data(p),
           linhas=linhas, fonte=FONTE_LENTIDAO, dp=DP, csv=CSV, nota_fora=nota_fora, https=https,
           vazio=vazio, agencia=agencia,
           t1=("Nenhum site chegou ao verde" if c["rapidos"] == 0
               else "%d de %d chegaram ao verde" % (c["rapidos"], n)),
           lentos_txt=("%d ficaram na faixa vermelha e o resto na laranja." % c["lentos"] if c["lentos"]
                       else "Todos ficaram na faixa laranja."),
           lcp_ok_txt=("Nenhum dos %d sites conseguiu." % n if c["lcp_ok"] == 0
                       else "Só %d dos %d sites conseguiram." % (c["lcp_ok"], n)),
           **{k: v for k, v in c.items() if k not in ("lentos", "rapidos", "lcp_ok")})
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
         "name": "Velocidade dos sites de clínicas de Goiânia (PageSpeed Insights, celular)",
         "description": "Nota de desempenho no celular (0 a 100), tempo até o conteúdo principal aparecer, "
                        "plataforma e presença de avaliações do Google na página inicial de %d sites de clínicas "
                        "de Goiânia, medidos com o Lighthouse (motor do PageSpeed Insights) em %s. "
                        "%s" % (len(rs), br(p["data"]), ("Inclui o nome de cada clínica." if p["mostrar_nomes"] else "Nomes trocados por letras.")),
         "url": url, "creator": autor, "license": "https://creativecommons.org/licenses/by/4.0/",
         "isAccessibleForFree": True, "temporalCoverage": p["data"], "inLanguage": "pt-BR",
         "spatialCoverage": {"@type": "Place", "name": "Goiânia, GO, Brasil"},
         "variableMeasured": ["Nota de desempenho no celular (0 a 100)",
                              "Largest Contentful Paint no celular (segundos)",
                              "Plataforma do site", "Avaliações do Google na página inicial"],
         "distribution": {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": url + CSV}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": S.BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": S.BASE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["trilha"], "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def main():
    global DADOS
    if "--dados" in sys.argv:  # teste da montagem com outro arquivo (use junto com --previa)
        DADOS = sys.argv[sys.argv.index("--dados") + 1]
    if not os.path.exists(DADOS):
        sys.exit("Sem dados: crie %s com os resultados medidos (formato no topo deste arquivo)." % DADOS)
    dados = json.load(io.open(DADOS, encoding="utf-8"))
    rs = dados.get("resultados") or []
    if len(rs) < 5 or any(not (0 <= r.get("score", -1) <= 100) for r in rs):
        sys.exit("Dados insuficientes ou com nota fora de 0 a 100: a página não é gerada.")
    faltando = [r.get("clinica") for r in rs if not all(r.get(k) for k in ("nicho", "plataforma", "prova", "lcp"))]
    if faltando:
        sys.exit("Faltam nicho/plataforma/prova/lcp em: %s" % faltando)
    # o texto afirma "nenhum usa Wix nem Shopify": só vale enquanto os dados confirmarem
    assert not any(x in r["plataforma"].lower() for r in rs for x in ("wix", "shopify"))
    p, corpo, rs, h1 = pagina(dados)
    assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (len(p["title"]), len(p["desc"]))
    S.schema, S.corpo = (lambda _: schema(p, rs, h1)), (lambda _: corpo)  # montar() chama estes dois
    modelo = io.open(os.path.join(S.RAIZ, S.MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    h = S.montar(modelo, dict(p, servico="site"))
    h = h.replace('aria-label="Pedir orçamento de site pelo WhatsApp"',
                  'aria-label="Pedir o teste do meu site pelo WhatsApp"')
    # menu e barra do celular herdam "#orcamento" do modelo (mesmo ajuste de gerar-ferramentas.py)
    h = h.replace('href="#orcamento"', 'href="/#pacotes"').replace(
        'data-page="%s">Quanto custa?</a>' % SLUG, 'data-page="%s">Orçamento grátis</a>' % SLUG)
    h = h.replace('data-page="%s"' % SLUG, 'data-page="%s"' % DP)
    assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1 and 'href="#orcamento"' not in h
    assert "R$" not in h and '"price"' not in h
    h = rcb_copy.humanizar(M.texto_html(h))

    pasta = sys.argv[sys.argv.index("--previa") + 1] if "--previa" in sys.argv else os.path.join(S.RAIZ, SLUG)
    os.makedirs(pasta, exist_ok=True)
    io.open(os.path.join(pasta, "index.html"), "w", encoding="utf-8", newline="\n").write(h)
    nomes = dados.get("mostrar_nomes")
    with io.open(os.path.join(pasta, CSV), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["clinica"] + (["url"] if nomes else [])
                   + ["ramo", "plataforma", "avaliacoes_google_na_pagina", "nota_celular", "lcp_segundos",
                      "https_automatico", "situacao", "data_do_teste"])
        for r in rs:
            w.writerow([r["rotulo"]] + ([r["url"]] if nomes else [])
                       + [r["nicho"], r["plataforma"], r["prova"], r["score"], r["lcp"],
                          "sim" if r.get("https", True) else "não", faixa(r["score"])[1], dados["data"]])
    print("ok  %s  (%d clínicas, média %d)" % (pasta, len(rs), round(statistics.mean(r["score"] for r in rs))))


if __name__ == "__main__":
    main()
