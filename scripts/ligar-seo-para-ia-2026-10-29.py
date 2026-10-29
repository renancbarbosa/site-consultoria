# -*- coding: utf-8 -*-
"""
Liga o 5º pilar (SEO para IA, 29/10/2026) ao resto do site, sem regenerar páginas antigas.

  1. Menu e rodapé: rcb_menu.aplicar() em todas as páginas (o item novo já está em
     scripts/rcb_menu.py). PULA /consultor-seo-goiania/ (protegida).
  2. /servicos/: painel "Os 5 serviços", frase em "Qual serviço a sua empresa precisa
     primeiro?", 5º grupo de cartões (mesmo componente dos outros 4) e os 5 links no ItemList.
  3. /seo-para-youtube/ e /sobre/: uma frase com link para o pilar.
  4. llms.txt e llms-full.txt: o 5º pilar.

Por que não regenerar /servicos/ e /seo-para-youtube/: o gerar-servicos-marketing.py está
fora de sincronia com o site no ar (regerar mexe em 21 páginas). As mesmas mudanças foram
escritas também no módulo scripts/conteudo/servicos_marketing.py, para uma regeração futura
não apagar nada.

Idempotente (marcador RCB:PILAR-IA no HTML). Rodar sem argumento só relata; --aplicar grava.
"""
import glob
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import rcb_menu  # noqa: E402

APLICAR = "--aplicar" in sys.argv
PROTEGIDA = os.path.join("consultor-seo-goiania", "index.html")
FORA = ("node_modules", "docs", "scripts", "graphify-out", "Projetos", "reports", "data", ".playwright-mcp")
INI, FIM = "<!--RCB:PILAR-IA-->", "<!--/RCB:PILAR-IA-->"

GRUPO = """
    """ + INI + """
    <section class="solution-section">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">SEO para IA</div>
          <h2 class="section-title">Como aparecer nas respostas do ChatGPT, do Gemini e do Google com IA?</h2>
          <p class="section-desc">Para quando o seu cliente pergunta à inteligência artificial quem indicar.</p>
        </div>
        <div class="cards-grid">
          <article class="feature-card">
            <h3><a href="/seo-para-ia/">SEO para IA</a></h3>
            <p>O serviço completo: deixar a empresa fácil de achar, entender e indicar pelas IAs.</p>
          </article>
          <article class="feature-card">
            <h3><a href="/auditoria-de-seo-para-ia/">Auditoria de SEO para IA</a></h3>
            <p>O que o ChatGPT e o Gemini dizem hoje sobre o seu ramo, e o que arrumar primeiro.</p>
          </article>
          <article class="feature-card">
            <h3><a href="/como-aparecer-no-chatgpt/">Como aparecer no ChatGPT</a></h3>
            <p>Por que não existe cadastro e o que o ChatGPT lê para indicar uma empresa.</p>
          </article>
          <article class="feature-card">
            <h3><a href="/ai-overviews-e-gemini/">AI Overviews e Gemini</a></h3>
            <p>Como a empresa entra na resposta de IA do próprio Google.</p>
          </article>
          <article class="feature-card">
            <h3><a href="/o-que-e-geo-e-aeo/">O que é GEO e AEO</a></h3>
            <p>Os nomes novos do SEO para IA, explicados sem complicação.</p>
          </article>
        </div>
      </div>
    </section>
    """ + FIM + "\n"

ITENS_LISTA = [("SEO para IA", "seo-para-ia"), ("Auditoria de SEO para IA", "auditoria-de-seo-para-ia"),
               ("Como aparecer no ChatGPT", "como-aparecer-no-chatgpt"),
               ("AI Overviews e Gemini", "ai-overviews-e-gemini"), ("O que é GEO e AEO", "o-que-e-geo-e-aeo")]


def troca(h, velho, novo, onde):
    assert h.count(velho) == 1, (onde, velho[:60], h.count(velho))
    return h.replace(velho, novo)


def servicos(h):
    if INI in h:
        return h
    h = troca(h, "<h2>Os 4 serviços</h2>", "<h2>Os 5 serviços</h2>", "servicos")
    h = troca(h, "<li>SEO para YouTube.</li>",
              "<li>SEO para YouTube.</li>\n            <li>SEO para IA (ChatGPT e Gemini).</li>", "servicos")
    h = troca(h, '<a href="/nichos/">nichos que atendemos</a>.</p>',
              '<a href="/nichos/">nichos que atendemos</a>.</p>\n          ' + INI + '<p>Se o seu cliente já '
              'pergunta ao ChatGPT ou ao Gemini quem indicar, entra o <a href="/seo-para-ia/">SEO para IA</a>. '
              'Ele usa a mesma base do SEO e do Google Meu Negócio, então costuma vir junto com eles ou logo '
              'depois.</p>' + FIM, "servicos")
    h = troca(h, '\n    <section class="pacotes-section" id="orcamento"',
              GRUPO + '\n    <section class="pacotes-section" id="orcamento"', "servicos")
    fim_lista = ('          "url": "https://rcbseo.com.br/seo-para-youtube/"\n        }\n      ]')
    novos = "".join(',\n        {\n          "@type": "ListItem",\n          "position": %d,\n          "name": "%s",\n'
                    '          "url": "https://rcbseo.com.br/%s/"\n        }' % (17 + i, n, s)
                    for i, (n, s) in enumerate(ITENS_LISTA))
    h = troca(h, fim_lista, fim_lista[:-8] + novos + "\n      ]", "servicos ItemList")
    return h


def youtube(h):
    if INI in h:
        return h
    velho = "valem tanto quanto a gravação.</p>"
    return troca(h, velho, velho + "\n          " + INI + "<p>Se você quer que a empresa inteira, e não só o vídeo, "
                 "apareça nas respostas do ChatGPT e do Gemini, veja o <a href=\"/seo-para-ia/\">SEO para IA</a>."
                 "</p>" + FIM, "seo-para-youtube")


def sobre(h):
    if INI in h:
        return h
    velho = '<a href="/para-profissionais-liberais/">profissionais liberais</a>.</p>'
    return troca(h, velho, velho[:-4] + " " + INI + "Para quem quer aparecer também nas respostas do ChatGPT e "
                 "do Gemini, há o <a href=\"/seo-para-ia/\">SEO para IA</a>." + FIM + "</p>", "sobre")


LLMS = ("- SEO para IA (ChatGPT, Gemini e Google com IA): https://rcbseo.com.br/seo-para-ia/. preparar a empresa "
        "para ser indicada nas respostas escritas por inteligência artificial (também chamado de GEO e AEO): robôs "
        "das IAs liberados, dados iguais no site, no Perfil da Empresa no Google e nos outros mapas e cadastros, páginas com "
        "respostas diretas e menções fora do site. Sem promessa de ser citado. Auditoria de entrada: "
        "https://rcbseo.com.br/auditoria-de-seo-para-ia/. Guias: https://rcbseo.com.br/como-aparecer-no-chatgpt/, "
        "https://rcbseo.com.br/ai-overviews-e-gemini/ e https://rcbseo.com.br/o-que-e-geo-e-aeo/.\n")


def llms(t):
    if "/seo-para-ia/" in t:
        return t
    t = troca(t, "## Os 4 serviços\n", "## Os 5 serviços\n", "llms")
    ancora = "Não inclui gravação nem edição de vídeo.\n- Todos os serviços"
    t = troca(t, ancora, ancora.replace("\n- Todos", "\n" + LLMS + "- Todos"), "llms")
    t = troca(t, "os 4 serviços e as páginas de cada um", "os 5 serviços e as páginas de cada um", "llms")
    t = troca(t, "agentes de IA, automação e recuperação de vendas.\n",
              "agentes de IA (robôs de atendimento), automação e recuperação de vendas. SEO para IA é outra coisa: é "
              "fazer a empresa aparecer nas respostas das IAs, e esse a RCB SEO oferece.\n", "llms")
    return t


def llms_full(t):
    if "/seo-para-ia/" in t:
        return t
    t = troca(t, "Os 4 serviços:\n", "Os 5 serviços:\n", "llms-full")
    yt = "Não inclui gravação nem edição de vídeo. https://rcbseo.com.br/seo-para-youtube/\n"
    t = troca(t, yt, yt + "5. **SEO para IA (GEO e AEO)**, preparar a empresa para ser indicada nas respostas do "
              "ChatGPT, do Gemini, do Perplexity, do Copilot e do Google com IA: robôs das IAs liberados, dados iguais "
              "em todo lugar, páginas com respostas diretas e menções fora do site. Sem promessa de ser citado. "
              "https://rcbseo.com.br/seo-para-ia/ e a auditoria de entrada em "
              "https://rcbseo.com.br/auditoria-de-seo-para-ia/\n", "llms-full")
    t = troca(t, "agentes de IA, automação e recuperação de vendas.\n",
              "agentes de IA (robôs de atendimento), automação e recuperação de vendas. SEO para IA é outra coisa: "
              "é fazer a empresa aparecer nas respostas das IAs, e esse a RCB SEO oferece.\n", "llms-full")
    t = troca(t, "gestão de anúncios no Google Ads e SEO para YouTube. Atende",
              "gestão de anúncios no Google Ads, SEO para YouTube e SEO para IA (aparecer nas respostas do ChatGPT e "
              "do Gemini). Atende", "llms-full")
    t = troca(t, "* SEO para YouTube: https://rcbseo.com.br/seo-para-youtube/\n",
              "* SEO para YouTube: https://rcbseo.com.br/seo-para-youtube/\n"
              "* SEO para IA: https://rcbseo.com.br/seo-para-ia/\n"
              "* Auditoria de SEO para IA: https://rcbseo.com.br/auditoria-de-seo-para-ia/\n"
              "* Como aparecer no ChatGPT: https://rcbseo.com.br/como-aparecer-no-chatgpt/\n"
              "* AI Overviews e Gemini: https://rcbseo.com.br/ai-overviews-e-gemini/\n"
              "* O que é GEO e AEO: https://rcbseo.com.br/o-que-e-geo-e-aeo/\n", "llms-full")
    return t


ESPECIAIS = {os.path.join("servicos", "index.html"): servicos,
             os.path.join("seo-para-youtube", "index.html"): youtube,
             os.path.join("sobre", "index.html"): sobre}


def main():
    os.chdir(RAIZ)
    alteradas = []
    arquivos = glob.glob("**/index.html", recursive=True) + ["404.html"]
    for f in sorted(arquivos):
        if f.startswith(FORA) or os.path.normpath(f) == PROTEGIDA:
            continue
        h = io.open(f, encoding="utf-8").read()
        novo = rcb_menu.aplicar(h)
        if f in ESPECIAIS:
            novo = ESPECIAIS[f](novo)
        if novo != h:
            assert novo.lstrip().lower().startswith("<!doctype"), f
            alteradas.append(f)
            if APLICAR:
                io.open(f, "w", encoding="utf-8", newline="").write(novo)
    for f, fn in (("llms.txt", llms), ("llms-full.txt", llms_full)):
        t = io.open(f, encoding="utf-8").read()
        novo = fn(t)
        if novo != t:
            alteradas.append(f)
            if APLICAR:
                io.open(f, "w", encoding="utf-8", newline="").write(novo)
    print("%s: %d arquivos" % ("alterados" if APLICAR else "seriam alterados", len(alteradas)))
    for f in alteradas[:8]:
        print("  ", f)


if __name__ == "__main__":
    main()
