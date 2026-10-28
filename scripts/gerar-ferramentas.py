# -*- coding: utf-8 -*-
"""
Gera /ferramentas/ (28/10/2026): 5 ferramentas gratuitas e oficiais para o dono
de negócio conferir a própria empresa no Google, cada uma com uma "Dica RCB"
apontando para um artigo do site.

Reaproveita o gerador das páginas de serviço (gerar-servicos-marketing.py): o
esqueleto (menu, rodapé, barra do celular, cookies) vem da página viva
/criacao-de-sites-goiania/ pela mesma função montar(). Só o corpo e o schema
são desta página.

Regras: SEM PREÇO da RCB; nenhum resultado prometido; links das ferramentas
vão direto para o endereço oficial. Idempotente: sobrescreve o arquivo.
"""
import importlib.util
import io
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("servicos", os.path.join(AQUI, "gerar-servicos-marketing.py"))
S = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S)
M, rcb_copy, e, wa, cta = S.M, S.rcb_copy, S.e, S.wa, S.cta

DATA = "2026-10-28"

P = {
    "slug": "ferramentas",
    "title": "Ferramentas Grátis para Ver sua Empresa no Google | RCB SEO",
    "desc": "5 ferramentas grátis e oficiais para conferir sua empresa no Google: perfil no Maps, "
            "velocidade do site e o que o cliente digita. Passo a passo simples.",
    "trilha": "Ferramentas grátis",
    "eyebrow": "Grátis e oficiais",
    "h1": "Ferramentas Grátis para Ver sua Empresa no Google",
    "sub": "Não precisa entender de SEO para saber se o seu negócio está aparecendo. "
           "Com estas 5 ferramentas gratuitas você faz um diagnóstico rápido em poucos minutos.",
    "data": DATA,
    "painel_h2": "O que você descobre aqui",
    "painel": [
        "Se o seu perfil no Google Maps está certo",
        "Se o seu site abre rápido no celular",
        "O que as pessoas digitam antes de achar você",
        "Se a sua empresa também aparece no Bing",
        "Se o Google entende os dados do seu site",
    ],
    "msg": "Olá, Renan! Testei minha empresa nas ferramentas do site e quero ajuda para entender o resultado.",
    "faq_titulo": "Perguntas frequentes sobre as ferramentas grátis",
    "faq": [
        ("Essas ferramentas são grátis mesmo?",
         "Sim. As cinco são gratuitas e oficiais, do Google e da Microsoft. Só pedem uma conta Google ou Microsoft, "
         "que você provavelmente já tem."),
        ("Preciso saber mexer com computador?",
         "Não. Quatro delas funcionam colando um endereço ou entrando com a sua conta. O Search Console é a única que "
         "pede um passo a mais: provar que o site é seu. Se travar nessa parte, quem fez o seu site resolve em minutos."),
        ("Fiz o teste e o resultado veio ruim. E agora?",
         "Calma, quase todo negócio tem alguma coisa para acertar. Tire um print do resultado e me mande no WhatsApp: "
         "eu digo o que pesa de verdade e o que pode esperar."),
        ("De quanto em quanto tempo vale olhar?",
         "O perfil no Google, toda semana, por causa das avaliações e perguntas novas. O Search Console, uma vez por mês. "
         "O teste de velocidade, sempre que o site for alterado."),
    ],
    "relacionados": [
        ("/google-perfil-empresa/", "Perfil da Empresa no Google", "Como deixar o seu perfil no Maps completo e na frente."),
        ("/criacao-de-sites-goiania/", "Criação de sites", "Site rápido no celular, feito para o cliente achar e chamar."),
        ("/blog/por-que-minha-empresa-nao-aparece-no-google/", "Por que minha empresa não aparece?",
         "Os motivos mais comuns, explicados sem complicação."),
    ],
    "cta_final": ("Testou e ficou com dúvida?",
                  "Me mande o print do resultado no WhatsApp. Eu olho com você e digo, com franqueza, o que vale a pena arrumar primeiro."),
}

# (id, nome, de quem, para que serve, endereço oficial, dica, link da dica, texto do link)
FERRAMENTAS = [
    ("perfil", "Perfil da Empresa no Google", "Google",
     "É a sua vitrine no Google e no Maps. Confira se o horário, o telefone, o endereço e as fotos estão certos.",
     "https://www.google.com/business/",
     "Pesquise o nome da sua empresa no Google, pelo celular, como um cliente faria. Horário errado manda o "
     "cliente para a porta fechada, e ele não volta.",
     "/blog/como-otimizar-google-perfil-empresa/", "Veja como deixar o perfil completo, passo a passo"),
    ("pagespeed", "PageSpeed Insights", "Google",
     "Mostra se o seu site é lento. Site lento é cliente que desiste antes de ver o que você vende.",
     "https://pagespeed.web.dev/",
     "Olhe sempre a aba Celular, que é como o seu cliente abre o site. A nota vai de 0 a 100: vermelho (0 a 49) "
     "pede atenção, laranja (50 a 89) é razoável e verde (90 a 100) é ótimo.",
     "/blog/site-bonito-nao-aparece-no-google/", "Entenda por que site bonito nem sempre aparece no Google"),
    ("search-console", "Search Console", "Google",
     "Mostra o que as pessoas digitam no Google antes de ver o seu site, e quantas clicam.",
     "https://search.google.com/search-console",
     "Os números começam a aparecer alguns dias depois de você cadastrar o site. Abra o relatório Desempenho: "
     "ali está a lista das buscas que mostraram a sua empresa.",
     "/blog/por-que-meu-site-nao-aparece-no-google/", "Saiba o que fazer quando o site some do Google"),
    ("bing-places", "Bing Places", "Microsoft",
     "É o perfil da sua empresa no Bing, a busca que vem no Windows e que alimenta o Copilot.",
     "https://www.bingplaces.com/",
     "O Bing deixa importar os dados do seu Perfil da Empresa no Google. Se o perfil do Google está certo, "
     "o do Bing fica pronto em poucos cliques.",
     "/google-perfil-empresa/", "Veja o que deixa o Perfil da Empresa completo"),
    ("rich-results", "Teste de pesquisa aprimorada", "Google",
     "Confere se o Google consegue ler as informações do seu site, como endereço, horário e telefone.",
     "https://search.google.com/test/rich-results",
     "Cole o endereço da página inicial do seu site. Passar no teste não garante destaque na busca: mostra só "
     "que o Google entende o que está escrito. Se ele não encontrar nada, vale ajustar.",
     "/blog/erros-que-impedem-empresa-aparecer-no-google/", "Conheça outros erros que escondem a empresa no Google"),
]


def s_hero(p):
    return """    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Início</a><span>/</span><span>%s</span></nav>
          <div class="eyebrow">%s</div>
          <h1 class="page-title">%s</h1>
          <p class="page-subtitle">%s</p>%s
          <div class="page-actions">
            <a class="btn btn-primary" href="#ferramentas" data-event="cta_click" data-location="hero_lista" data-page="%s">Ver as 5 ferramentas</a>
            %s
          </div>
        </div>
        <aside class="page-hero-panel">
          <h2>%s</h2>
          <ul class="audit-list">%s
          </ul>
        </aside>
      </div>
    </section>
""" % (e(p["trilha"]), e(p["eyebrow"]), e(p["h1"]), e(p["sub"]), S.autor_data(p), p["slug"],
       cta(wa(p["msg"]), "Tirar dúvida no WhatsApp", "hero", p["slug"], "btn btn-outline"),
       e(p["painel_h2"]), "".join("\n            <li>%s</li>" % e(x) for x in p["painel"]))


def s_ferramentas(slug):
    cards = []
    for n, (fid, nome, dono, serve, url, dica, link, ancora) in enumerate(FERRAMENTAS, 1):
        cards.append("""
          <article class="ferramenta-card" id="%s">
            <div class="ferramenta-topo"><span class="ferramenta-num">%d</span><span class="ferramenta-dono">%s</span></div>
            <h2>%s</h2>
            <p>%s</p>
            <a class="btn btn-outline" href="%s" target="_blank" rel="noopener" data-event="ferramenta_click" data-location="ferramenta_%s" data-page="%s">Abrir %s</a>
            <div class="dica-rcb">
              <strong>Dica RCB</strong>
              <p>%s <a href="%s">%s</a>.</p>
            </div>
          </article>""" % (fid, n, e(dono), e(nome), e(serve), url, fid, slug, e(nome), e(dica), link, e(ancora)))
    return """
    <section class="solution-section" id="ferramentas">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">As 5 ferramentas</div>
          <p class="section-desc">Siga na ordem: a primeira é a que mais pesa para quem atende na cidade.</p>
        </div>
        <div class="ferramentas-lista">%s
        </div>
      </div>
    </section>
""" % "".join(cards)


def corpo(p):
    return s_hero(p) + s_ferramentas(p["slug"]) + S.s_faq(p) + S.s_relacionados(p) + S.s_cta_final(p)


def schema(p):
    url = "%s/%s/" % (S.BASE, p["slug"])
    g = [
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": p["title"],
         "description": p["desc"], "inLanguage": "pt-BR", "isPartOf": M.site(),
         "datePublished": DATA, "dateModified": DATA,
         "author": {"@type": "Person", "@id": "https://rcbseo.com.br/#renan", "name": "Renan Carvalho Barbosa"},
         "mainEntity": {"@id": url + "#lista"}, "breadcrumb": {"@id": url + "#breadcrumb"}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": S.BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["trilha"], "item": url}]},
        {"@type": "ItemList", "@id": url + "#lista", "name": "Ferramentas grátis para ver sua empresa no Google",
         "numberOfItems": len(FERRAMENTAS), "itemListOrder": "https://schema.org/ItemListOrderAscending",
         "itemListElement": [
             {"@type": "ListItem", "position": n, "item": {
                 "@type": "SoftwareApplication", "name": nome, "url": url_f, "description": serve,
                 "applicationCategory": "BusinessApplication", "operatingSystem": "Navegador",
                 "publisher": {"@type": "Organization", "name": dono}, "isAccessibleForFree": True}}
             for n, (_, nome, dono, serve, url_f, *_r) in enumerate(FERRAMENTAS, 1)]},
        M.no_empresa(),
        {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2)


def main():
    S.schema, S.corpo = schema, corpo  # montar() do gerador de serviços chama estes dois
    modelo = io.open(os.path.join(S.RAIZ, S.MODELO, "index.html"), encoding="utf-8").read()
    assert modelo.startswith("<!DOCTYPE"), "modelo corrompido"
    p = dict(P, title=M.titulo(P["title"]))
    assert len(p["title"]) <= 65 and len(p["desc"]) <= 160, (len(p["title"]), len(p["desc"]))
    h = S.montar(modelo, dict(p, servico="site"))  # "servico" só monta o rótulo do WhatsApp, trocado abaixo
    h = h.replace('aria-label="Pedir orçamento de site pelo WhatsApp"',
                  'aria-label="Tirar dúvida sobre as ferramentas pelo WhatsApp"')
    # menu e barra do celular herdam "#orcamento" do modelo; aqui não há essa seção (padrão do blog: /#pacotes)
    h = h.replace('href="#orcamento"', 'href="/#pacotes"').replace(
        'data-page="ferramentas">Quanto custa?</a>', 'data-page="ferramentas">Orçamento grátis</a>')
    assert 'href="#orcamento"' not in h and "Quanto custa?" not in h
    assert h.startswith("<!DOCTYPE") and h.count("<h1") == 1
    assert "R$" not in h and '"price"' not in h and "priceRange" not in h
    assert 'data-page="%s"' % S.MODELO not in h
    destino = os.path.join(S.RAIZ, p["slug"], "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    h = rcb_copy.humanizar(M.texto_html(h))
    io.open(destino, "w", encoding="utf-8", newline="\n").write(h)
    miolo = h.split('<main id="main-content">')[1].split("</main>")[0]
    print("ok  /%s/  %d palavras" % (p["slug"], len(re.sub(r"<[^>]+>", " ", miolo).split())))


if __name__ == "__main__":
    main()
