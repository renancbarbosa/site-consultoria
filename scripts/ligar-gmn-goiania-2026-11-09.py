# -*- coding: utf-8 -*-
"""Liga /google-meu-negocio-goiania/ ao resto do site (auditoria de 09/11/2026, itens 6 e 7).

1. Menu (dropdown "SEO e Google") e coluna Servicos do rodape: item novo, em todas as paginas
   com menu. Trava: a pagina so e gravada se a UNICA diferenca for o item novo.
2. Caixa de texto (marcador RCB:GMN-GOIANIA) antes das perguntas frequentes nas paginas do
   mesmo assunto, com link para a pagina nova e para o consultor em Goiania (item 7: reforca a
   pagina dona do termo "consultor seo goiania"). Ancoras variadas.
3. llms.txt: a pagina nova na lista de servicos.

/consultor-seo-goiania/ (PROTEGIDA) fica de fora. Idempotente: 2a execucao, 0 alteradas.
    python scripts/ligar-gmn-goiania-2026-11-09.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import rcb_menu  # noqa: E402

URL = "/google-meu-negocio-goiania/"
PROTEGIDA = "consultor-seo-goiania/index.html"
INTERNAS = ("docs/", "scripts/", "data/", "reports/", "node_modules/", "graphify-out/",
            "Projetos/", "modelos/", "functions/")
ITEM_MENU = '<a href="%s" class="nav-dropdown-item" role="menuitem">Google Meu Negócio em Goiânia</a>' % URL
ITENS_RODAPE = ('<li><a href="%s">Google Meu Negócio em Goiânia</a></li>' % URL,
                '<a href="%s">Google Meu Negócio em Goiânia</a>' % URL)

GMN = '<a href="/google-meu-negocio-goiania/">%s</a>'
CONS = '<a href="/consultor-seo-goiania/">%s</a>'
TEXTOS = [
    "<strong>Sua empresa é de Goiânia ou região?</strong> Veja como funciona o " + GMN % "Google Meu Negócio em Goiânia"
    + ", com atendimento presencial do " + CONS % "consultor de SEO em Goiânia" + ".",
    "<strong>Para empresas de Goiânia</strong>, eu faço a " + GMN % "otimização do perfil no Google em Goiânia"
    + " pessoalmente, com hora marcada. Conheça o " + CONS % "consultor SEO em Goiânia" + " por trás do trabalho.",
    "<strong>Quer aparecer no Google Maps em Goiânia?</strong> Veja " + GMN % "como eu cuido do Google Meu Negócio de empresas goianienses"
    + " e fale direto com o " + CONS % "consultor de SEO local em Goiânia" + ".",
]
# paginas do mesmo assunto (perfil no Google, Maps, SEO local, Goiania). Fora: cidades (o gerador
# sobrescreve) e a protegida.
ALVOS = [
    "google-perfil-empresa/index.html", "seo-local-goiania/index.html", "contato/index.html",
    "google-meu-negocio-para-clinicas/index.html", "consultoria-seo-local/index.html",
    "criacao-de-sites-goiania/index.html", "para-comercios-locais/index.html",
    "para-profissionais-liberais/index.html", "seo-para-pequenas-empresas/index.html",
    "como-aparecer-no-google/index.html", "guia-seo-local/index.html",
    "blog/como-aparecer-no-google-maps/index.html", "blog/google-meu-negocio-nao-aparece/index.html",
    "blog/quanto-custa-otimizar-google-meu-negocio/index.html",
    "blog/como-otimizar-google-perfil-empresa/index.html",
    "blog/vale-a-pena-contratar-consultor-google-meu-negocio/index.html",
    "blog/como-saber-se-consultor-google-meu-negocio-e-bom/index.html",
    "blog/google-perfil-atrapalhando-resultados/index.html",
    "blog/como-escolher-consultoria-seo-goiania/index.html",
    "blog/como-aparecer-google-clinica-estetica-goiania/index.html",
    "blog/o-que-e-seo-local/index.html", "blog/seo-para-empresas-locais/index.html",
]
_CAIXA = re.compile(r'<!--RCB:GMN-GOIANIA-->.*?<!--/RCB:GMN-GOIANIA-->\n', re.S)
_FAQ = re.compile(r'<h2[^>]*>\s*Perguntas frequentes', re.I)


def paginas():
    out = subprocess.run(["git", "ls-files", "*.html"], cwd=RAIZ, capture_output=True,
                         text=True, encoding="utf-8").stdout.split()
    out.append("google-meu-negocio-goiania/index.html")
    return sorted(set(p for p in out if not p.startswith(INTERNAS)))


def menu_e_rodape(h):
    novo = rcb_menu._troca_menu(h)
    novo = rcb_menu._SITES_FOOTER.sub(lambda m: "<!--RCB:SITES-FOOTER-->" + rcb_menu._bloco_servicos(m.group(1))
                                      + "<!--/RCB:SITES-FOOTER-->", novo)
    conferir = novo
    if ITEM_MENU not in h:
        conferir = conferir.replace(ITEM_MENU, "", 1)
    for it in ITENS_RODAPE:
        if it not in h and it in conferir:
            conferir = conferir.replace(it, "", 1)
            break
    return novo, conferir == h


def caixa(h, rel, i):
    h = _CAIXA.sub("", h)
    texto = TEXTOS[i % len(TEXTOS)]
    blog = rel.startswith("blog/")
    if blog:
        bloco = '<div class="artigo-cta-box"><p>%s</p></div>' % texto
    else:
        bloco = ('<section class="solution-section"><div class="container"><div class="split-copy" '
                 'style="max-width:860px;margin:0 auto"><p>%s</p></div></div></section>' % texto)
    bloco = "<!--RCB:GMN-GOIANIA-->" + bloco + "<!--/RCB:GMN-GOIANIA-->\n"
    m = _FAQ.search(h)
    if m:
        pos = h.rfind("<section", 0, m.start())
        if blog or pos < 0:
            pos = h.rfind("\n", 0, h.rfind("<", 0, m.start()) + 1) + 1 if pos < 0 else pos
    else:
        pos = h.find("</article>") if blog and "</article>" in h else h.find("</main>")
    if pos <= 0:
        return None
    return h[:pos] + bloco + h[pos:]


def llms():
    p = os.path.join(RAIZ, "llms.txt")
    s = io.open(p, encoding="utf-8", newline="").read()
    if URL in s:
        return False
    alvo = re.search(r"^- .*https://rcbseo\.com\.br/google-perfil-empresa/.*$", s, re.M)
    if not alvo:
        print("AVISO: llms.txt sem a linha do google-perfil-empresa; nao mexi")
        return False
    linha = ("- Google Meu Negócio em Goiânia: https://rcbseo.com.br/google-meu-negocio-goiania/. "
             "Otimização do Perfil da Empresa no Google para negócios de Goiânia e região, com atendimento "
             "presencial; para aparecer no mapa e no Google Maps quando o cliente procura perto.")
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s[:alvo.end()] + nl + linha + s[alvo.end():]
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    return True


def main():
    alteradas, recusadas, sem_lugar = [], [], []
    for rel in paginas():
        if rel == PROTEGIDA:
            continue
        p = os.path.join(RAIZ, rel)
        raw = io.open(p, encoding="utf-8", newline="").read()
        novo, ok = menu_e_rodape(raw)
        if not ok:
            recusadas.append(rel)
            novo = raw
        if rel in ALVOS:
            c = caixa(novo, rel, ALVOS.index(rel))
            if c is None:
                sem_lugar.append(rel)
            else:
                novo = c
        if novo != raw:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            alteradas.append(rel)
    print("alteradas:", len(alteradas))
    print("menu/rodape recusado (diferenca alem do item novo):", recusadas)
    print("caixa sem lugar:", sem_lugar)
    print("llms.txt:", "atualizado" if llms() else "sem mudanca")


if __name__ == "__main__":
    main()
