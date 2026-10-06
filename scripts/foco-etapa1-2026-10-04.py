"""Etapa 1 do plano de nichos: limpeza de foco (04/10/2026). Ver docs/plano-nichos-2026-10.md.

1. Menu e rodape novos (fonte unica: scripts/rcb_menu.py) em todas as paginas:
   4 servicos (SEO e Google Meu Negocio | Sites e Landing Pages | Trafego Pago |
   SEO para YouTube) + Nichos + Contato. Sai a coluna "Agentes de IA" do rodape.
   Blog, Cases e Sobre passam para o rodape.
2. Agentes de IA, automacao e recuperacao de vendas: as 4 paginas saem; as 3 com
   impressao ganham 301 no _redirects; todo link interno para elas sai.
3. Home: subtitulo do topo, secao de servicos e ficha da empresa nos 4 servicos.
   Titulo e descricao da home NAO mudam (tem clique e posicao 4 no Search Console).
4. /contato/: ficha da empresa com os 4 servicos.
5. llms.txt: descricao da empresa, secao "Os 4 servicos", sem automacao.

Idempotente.  python scripts/foco-etapa1-2026-10-04.py
"""
import glob
import json
import os
import re
import shutil
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rcb_menu  # noqa: E402

RAIZ = os.path.dirname(AQUI)
S = re.S

APAGAR = ["agentes-de-ia", "agente-de-ia-para-clinicas", "recuperacao-de-vendas-whatsapp", "automacao-de-processos"]
REDIRECTS = [
    ("/agentes-de-ia/", "/"),
    ("/agentes-de-ia", "/"),
    ("/agente-de-ia-para-clinicas/", "/seo-para-clinicas/"),
    ("/agente-de-ia-para-clinicas", "/seo-para-clinicas/"),
    ("/recuperacao-de-vendas-whatsapp/", "/"),
    ("/recuperacao-de-vendas-whatsapp", "/"),
]

SERVICOS_SCHEMA = [
    "SEO e Google Meu Negócio",
    "Criação de sites e landing pages",
    "Gestão de tráfego pago (Google Ads)",
    "SEO para YouTube",
]
DESC_EMPRESA = ("SEO, Google Meu Negócio, sites e landing pages, gestão de tráfego pago no Google Ads e SEO "
                "para YouTube para donos de negócio. Orçamento grátis pelo WhatsApp em até 24 horas. "
                "Atendimento presencial em Goiânia e online em todo o Brasil.")

HERO_ANTIGO = re.compile(r'<p class="hero-headline"><strong>.*?</strong></p>', S)
# texto do topo atualizado em 05/10/2026 (copy para leigo, sem jargao): ver scripts/copy-reescrita-2026-10-05.py
HERO_NOVO = ('<p class="hero-headline"><strong>Eu faço a sua empresa aparecer no Google quando alguém procura o que '
             'você vende. O anúncio traz cliente já nesta semana. O Google Maps e o site trazem cliente todo mês, '
             'sem pagar por clique.</strong></p>')

SECAO_NOVA = """<section class="cluster-section" aria-labelledby="servicos-titulo">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Serviços</div>
          <h2 id="servicos-titulo" class="section-title">Como eu trago clientes pelo Google para a sua empresa?</h2>
          <p class="section-desc">Cada serviço resolve uma parte do caminho do cliente até o seu WhatsApp. Dá para começar por um só: o orçamento de cada um é grátis e sai em até 24 horas.</p>
        </div>
        <div class="cluster-grid">
          <a class="cluster-card" href="/consultoria-seo-local/"><h3>SEO e Google Meu Negócio</h3><p>É como ter a vitrine na rua mais movimentada da cidade: sua empresa aparece no mapa e nas buscas do Google, e o cliente chega sem você pagar por clique. É o resultado que dura.</p></a>
          <a class="cluster-card" href="{landing}"><h3>Sites e landing pages</h3><p>O site da sua empresa, feito para aparecer no Google, e a página de anúncio, que transforma o clique em conversa no WhatsApp.</p></a>
          <a class="cluster-card" href="{trafego}"><h3>Tráfego pago (Google Ads)</h3><p>Anúncio na pesquisa do Google para quem já está procurando o que você vende, com cada contato medido.</p></a>
          {youtube_card}
        </div>
      </div>
    </section>""".format(landing=rcb_menu.PROVISORIO["landing"], trafego=rcb_menu.PROVISORIO["trafego"],
                         youtube_card=('<a class="cluster-card" href="%s"><h3>SEO para YouTube</h3><p>Título, descrição, capítulos e transcrição para o seu vídeo ser encontrado no YouTube e no Google.</p></a>' % rcb_menu.PROVISORIO["seo_youtube"]) if rcb_menu.MOSTRAR_YOUTUBE else '<div class="cluster-card"><h3>SEO para YouTube</h3><p>Título, descrição, capítulos e transcrição para o seu vídeo ser encontrado no YouTube e no Google. Página própria em breve.</p></div>')
SECAO_ANTIGA = re.compile(r'<section class="cluster-section" aria-labelledby="(?:sites-anuncios|servicos)-titulo">.*?</section>', S)

LLMS_DESC_ANTIGA = ("Consultoria especializada em SEO Local, Google Meu Negócio (Google Business Profile), "
                    "sites otimizados e automação de processos para")
LLMS_DESC_NOVA = ("Consultoria de SEO, Google Meu Negócio (Google Business Profile), sites e landing pages, "
                  "tráfego pago no Google Ads e SEO para YouTube para")
LLMS_SECAO = """## Os 4 serviços
Mensagem central: trazer clientes pelo Google — anúncio para o resultado rápido, SEO para o resultado duradouro, site e landing page para converter. Público: donos de negócio. Cada projeto tem orçamento individual e grátis pelo WhatsApp em até 24 horas; não há garantia de posição.
- SEO e Google Meu Negócio: https://rcbseo.com.br/consultoria-seo-local/ e https://rcbseo.com.br/google-perfil-empresa/ — aparecer no mapa e nas buscas do Google sem pagar por clique.
- Sites e landing pages para anúncios: {landing} e https://rcbseo.com.br/criacao-de-sites-goiania/ — página rápida no celular, botão de WhatsApp e medição de conversão.
- Tráfego pago empresarial (Google Ads): {trafego} — anúncio na rede de pesquisa do Google, sempre com landing page e medição; Meta Ads só como complemento.
- SEO para YouTube: https://rcbseo.com.br/seo-para-youtube/ — título, descrição, capítulos, transcrição e miniatura para o vídeo ser encontrado no YouTube e no Google, sem promessa de inscritos.

""".format(landing="https://rcbseo.com.br" + rcb_menu.PROVISORIO["landing"],
           trafego="https://rcbseo.com.br" + rcb_menu.PROVISORIO["trafego"])


def ler(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def gravar(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def ficha_empresa(h):
    """description e serviceType do no principal da empresa (home e contato)."""
    def trata(m):
        d = json.loads(m.group(2))
        mudou = False
        for n in d.get("@graph", [d]):
            if n.get("@id") == "https://rcbseo.com.br/#business" and "serviceType" in n:
                if n["serviceType"] != SERVICOS_SCHEMA or n.get("description") != DESC_EMPRESA:
                    n["serviceType"] = list(SERVICOS_SCHEMA)
                    n["description"] = DESC_EMPRESA
                    mudou = True
        if not mudou:
            return m.group(0)
        base = re.match(r'\s*', m.group(2)).group(0)
        recuo = base.split("\n")[-1]
        out = json.dumps(d, ensure_ascii=False, indent=2).replace("\n", "\n" + recuo)
        return m.group(1) + base + out + re.search(r'\s*$', m.group(2)).group(0) + m.group(3)
    return re.sub(r'(<script[^>]+application/ld\+json[^>]*>)(.*?)(</script>)', trata, h, flags=S)


def main():
    alterados = []
    for d in APAGAR:
        if os.path.isdir(os.path.join(RAIZ, d)):
            shutil.rmtree(os.path.join(RAIZ, d))
            alterados.append("APAGADA /%s/" % d)
    for p in sorted(glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)):
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        if rel.startswith(("scripts/", "docs/", "data/", "node_modules/", "graphify-out/", ".playwright")):
            continue
        h0 = ler(p)
        h = rcb_menu.aplicar(h0)
        if rel == "index.html":
            h = HERO_ANTIGO.sub(HERO_NOVO, h, count=1)
            h = SECAO_ANTIGA.sub(lambda m: SECAO_NOVA, h, count=1)
        if rel in ("index.html", "contato/index.html"):
            h = ficha_empresa(h)
        if h != h0:
            if h0.lstrip().lower().startswith("<!doctype") and not h.lstrip().lower().startswith("<!doctype"):
                sys.exit("perdeu o DOCTYPE: " + rel)
            for b in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, S):
                json.loads(b)
            gravar(p, h)
            alterados.append(rel)
    rp = os.path.join(RAIZ, "_redirects")
    r0 = ler(rp)
    r = r0
    if "# Etapa 1 (04/10/2026)" not in r:
        r = r.rstrip("\r\n") + "\n# Etapa 1 (04/10/2026): agentes de IA e recuperacao de vendas sairam do site\n"
        r += "".join("%s %s 301\n" % (a, b) for a, b in REDIRECTS)
    if r != r0:
        gravar(rp, r)
        alterados.append("_redirects")
    lp = os.path.join(RAIZ, "llms.txt")
    l0 = ler(lp)
    l1 = l0.replace(LLMS_DESC_ANTIGA, LLMS_DESC_NOVA)
    l1 = re.sub(r'- Automação de processos: https://rcbseo\.com\.br/automacao-de-processos/[^\n]*\n', '', l1)
    if "## Os 4 serviços" not in l1:
        if "## Serviços\r\n" in l1:
            l1 = l1.replace("## Serviços\r\n", LLMS_SECAO.replace("\n", "\r\n") + "## Serviços\r\n", 1)
        else:
            l1 = l1.replace("## Serviços\n", LLMS_SECAO + "## Serviços\n", 1)
    if l1 != l0:
        gravar(lp, l1)
        alterados.append("llms.txt")
    print("alterados:", len(alterados))
    for a in alterados[:8]:
        print("  ", a)
    if len(alterados) > 8:
        print("   ... e mais", len(alterados) - 8)


if __name__ == "__main__":
    main()
