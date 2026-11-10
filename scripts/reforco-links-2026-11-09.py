# -*- coding: utf-8 -*-
"""Reforco de links internos (auditoria de 09/11/2026, item 10).

19 paginas indexaveis recebiam so 1 ou 2 links do resto do site. Cada uma ganha links de 2 a 3
paginas do MESMO assunto, numa caixa "Leia tambem" antes das perguntas frequentes
(marcador RCB:REFORCO). Ancoras descritivas e variadas; nunca o termo exato de uma pagina de
venda (evita disputa entre paginas, ex.: "seo para clinicas").
Fora: cidades (o gerador sobrescreve) e /consultor-seo-goiania/ (protegida).
Idempotente: 2a execucao, 0 alteradas.
    python scripts/reforco-links-2026-11-09.py
"""
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = '<a href="%s">%s</a>'
B = "/blog/"
DED = B + "como-conseguir-clientes-para-dedetizadora/"
GUI = B + "como-conseguir-clientes-para-guincho/"
EST = B + "como-conseguir-clientes-para-higienizacao-de-estofados/"
REF = B + "como-conseguir-clientes-para-reformas/"
ODO = B + "como-atrair-pacientes-consultorio-odontologico/"
ESC = B + "como-escolher-consultoria-seo-goiania/"
VAL = B + "seo-para-clinicas-vale-a-pena/"
GMNV = B + "vale-a-pena-contratar-consultor-google-meu-negocio/"
VEL = B + "velocidade-sites-clinicas-goiania/"
C = "/consultoria-seo/"
CIDADES = ("Atendo online empresas do Brasil inteiro, por exemplo em "
           + A % (C + "brasilia/", "Brasília") + ", " + A % (C + "rio-de-janeiro/", "Rio de Janeiro") + ", "
           + A % (C + "niteroi/", "Niterói") + ", " + A % (C + "porto-alegre/", "Porto Alegre") + ", "
           + A % (C + "vitoria/", "Vitória") + ", " + A % (C + "cuiaba/", "Cuiabá") + ", "
           + A % (C + "campo-grande/", "Campo Grande") + ", " + A % (C + "palmas/", "Palmas") + ", "
           + A % (C + "petrolina/", "Petrolina") + " e " + A % (C + "presidente-prudente/", "Presidente Prudente")
           + ". Veja " + A % (C, "todas as cidades atendidas") + ".")

DOADORES = {
    "blog/seo-para-prestadores-de-servico/index.html":
        "<strong>Leia também, por ramo:</strong> " + A % (DED, "como conseguir clientes para dedetizadora") + ", "
        + A % (GUI, "como conseguir clientes para guincho") + ", "
        + A % (EST, "clientes para higienização de estofados") + " e "
        + A % (REF, "clientes para empresa de reformas") + ".",
    "nichos/index.html":
        "<strong>Guias práticos por ramo:</strong> " + A % (DED, "dedetizadoras") + ", "
        + A % (GUI, "guinchos e reboques") + ", " + A % (EST, "higienização de estofados") + ", "
        + A % (REF, "reformas e manutenção") + " e " + A % (ODO, "consultórios odontológicos") + ".",
    "blog/seo-para-manutencao-e-reformas/index.html":
        "<strong>Leia também:</strong> " + A % (REF, "onde a empresa de reformas acha cliente hoje") + " e "
        + A % (EST, "como a higienização de estofados consegue clientes") + ".",
    "marketing-para-empresa-de-limpeza/index.html":
        "<strong>Ramos parecidos com o seu:</strong> " + A % (EST, "higienização de estofados") + " e "
        + A % (DED, "dedetização") + ", com o que funciona para conseguir clientes em cada um.",
    "seo-para-dentistas/index.html":
        "<strong>Leia também:</strong> " + A % (ODO, "como atrair pacientes para o consultório odontológico")
        + ", com o que o paciente procura antes de marcar.",
    "blog/por-que-minha-clinica-odontologica-nao-aparece-no-google/index.html":
        "<strong>Próximo passo:</strong> depois de aparecer, veja " + A % (ODO, "como atrair mais pacientes para o consultório") + ".",
    "seo-local-goiania/index.html":
        "<strong>Vai contratar alguém?</strong> Leia " + A % (ESC, "como escolher uma consultoria de SEO em Goiânia")
        + " antes de fechar com qualquer um, inclusive comigo.",
    "blog/como-escolher-consultoria-seo-local/index.html":
        "<strong>Sua empresa é de Goiânia?</strong> Veja " + A % (ESC, "o que conferir numa consultoria de SEO goianiense") + ".",
    "blog/quanto-tempo-leva-seo-local-clinicas/index.html":
        "<strong>Leia também:</strong> " + A % (VAL, "quando o investimento no Google compensa para uma clínica")
        + " e o " + A % (VEL, "teste de velocidade dos sites de clínicas de Goiânia") + ".",
    "blog/seo-para-clinicas-por-que-aparecer-no-google-vale-mais-que-indicacao/index.html":
        "<strong>Leia também:</strong> " + A % (VAL, "as contas para saber se vale a pena para a sua clínica") + ".",
    "google-perfil-empresa/index.html":
        "<strong>Pensando em contratar?</strong> Leia " + A % (GMNV, "vale a pena pagar alguém para cuidar do perfil?")
        + " " + CIDADES,
    "blog/como-saber-se-consultor-google-meu-negocio-e-bom/index.html":
        "<strong>Leia também:</strong> " + A % (GMNV, "quando vale a pena contratar ajuda para o perfil no Google") + ".",
    "criacao-de-sites-goiania/index.html":
        "<strong>Dado real:</strong> veja o " + A % (VEL, "teste de velocidade que fiz nos sites de clínicas de Goiânia")
        + ", e por que site lento perde cliente.",
    "site-para-clinica/index.html":
        "<strong>Leia também:</strong> o " + A % (VEL, "teste de velocidade com 15 sites de clínicas de Goiânia") + ".",
    "seo-para-clinicas/index.html":
        "<strong>Antes de decidir:</strong> " + A % (VAL, "faça as contas de retorno para a sua clínica")
        + " e veja o " + A % (VEL, "teste de velocidade dos sites de clínicas da cidade") + ".",
    "consultoria-seo-local/index.html": "<strong>Fora de Goiânia?</strong> " + CIDADES,
}
_CAIXA = re.compile(r'<!--RCB:REFORCO-->.*?<!--/RCB:REFORCO-->\n', re.S)
_FAQ = re.compile(r'<h2[^>]*>\s*Perguntas frequentes', re.I)


def caixa(h, rel, texto):
    h = _CAIXA.sub("", h)
    blog = rel.startswith("blog/")
    if blog:
        bloco = '<div class="artigo-cta-box"><p>%s</p></div>' % texto
    else:
        bloco = ('<section class="solution-section"><div class="container"><div class="split-copy" '
                 'style="max-width:860px;margin:0 auto"><p>%s</p></div></div></section>' % texto)
    bloco = "<!--RCB:REFORCO-->" + bloco + "<!--/RCB:REFORCO-->\n"
    m = _FAQ.search(h)
    pos = h.rfind("<section", 0, m.start()) if m else -1
    if pos < 0:
        pos = h.find("</article>") if blog and "</article>" in h else h.find("</main>")
    # a caixa do Google Meu Negocio em Goiania (RCB:GMN-GOIANIA) fica imediatamente antes do FAQ:
    # esta entra antes dela, nunca dentro.
    k = h.rfind("<!--RCB:GMN-GOIANIA-->", 0, pos + 1)
    if k >= 0 and h.find("<!--/RCB:GMN-GOIANIA-->", k) < pos and pos - h.find("<!--/RCB:GMN-GOIANIA-->", k) < 40:
        pos = k
    if pos <= 0:
        return None
    return h[:pos] + bloco + h[pos:]


def main():
    alteradas, sem = [], []
    for rel, texto in DOADORES.items():
        p = os.path.join(RAIZ, rel)
        raw = io.open(p, encoding="utf-8", newline="").read()
        for href in re.findall(r'href="([^"]+)"', texto):
            alvo = os.path.join(RAIZ, href.strip("/"), "index.html")
            assert os.path.exists(alvo), (rel, href)
        novo = caixa(raw, rel, texto)
        if novo is None:
            sem.append(rel)
            continue
        if novo != raw:
            io.open(p, "w", encoding="utf-8", newline="").write(novo)
            alteradas.append(rel)
    print("alteradas:", len(alteradas))
    print("sem lugar:", sem)


if __name__ == "__main__":
    main()
