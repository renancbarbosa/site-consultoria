"""Caixa "Resultado real" com numeros dos cases nas paginas de nicho e de servico.

Insere, antes do FAQ (<section class="faq-section"), o bloco entre
<!-- RCB:CASE-NICHO --> e <!-- /RCB:CASE-NICHO -->. Se o bloco ja existe, ATUALIZA
(mudou numero de case? edite CASES abaixo e rode de novo). Idempotente.

Fonte dos numeros: /cases/ (Search Console, 4 primeiras x 4 ultimas semanas).
Regra do Renan: dizer que foi feito e que mudou, nunca o como.
Paginas geradas por script (gmn-goiania, agencia, criacao-de-sites) perdem o bloco se
forem regeradas: rode este script de novo depois.
"""
import re
import sys
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
INI, FIM = "<!-- RCB:CASE-NICHO -->", "<!-- /RCB:CASE-NICHO -->"
WA = "https://wa.me/5562991161040?text="

CASES = {
    "imune": {
        "ancora": "case-imune",
        "titulo": "Resultado real: um consultório médico saiu da 2ª para a 1ª página do Google",
        "numeros": [("17º → 8º", "posição média no Google"), ("+41%", "visitas vindas do Google"),
                    ("43", "buscas de pacientes na 1ª página")],
        "texto": "Imune Consultórios, do Dr. Paulo Prado, em Rio Verde (GO). Site novo e presença no "
                 "Google cuidados por nós. Números do próprio Google, publicados com autorização.",
        "wa": "Olá! Vi o case do consultório que foi para a 1ª página do Google e quero esse resultado.",
    },
    "nalu": {
        "ancora": "case-naluprado",
        "titulo": "Resultado real: site novo com +180% de aparições no Google",
        "numeros": [("+180%", "aparições no Google"), ("+124%", "visitas no mês"),
                    ("1º", "lugar em “orquestra casamento”")],
        "texto": "Nalu Prado Eventos Musicais, em Goiânia. Site feito do zero para ser encontrado por "
                 "quem está organizando um evento. Números do próprio Google, com autorização.",
        "wa": "Olá! Vi o case do site com +180% de aparições no Google e quero esse resultado.",
    },
    "docevidade": {
        "ancora": "case-docevidade",
        "ver": "Ver o case completo",
        "titulo": "Resultado real: 1º lugar no Google Maps com só 4 avaliações",
        "numeros": [("1º", "no Maps para “macarrons Goiânia”"), ("1.969", "visualizações do perfil"),
                    ("252", "pedidos de rota até a loja")],
        "texto": "Docevidade Patisserie, em Goiânia. Perfil da Empresa no Google cuidado por nós, à "
                 "frente de concorrentes que tinham 47 e 312 avaliações.",
        "wa": "Olá! Vi o case da confeitaria que ficou em 1º no Google Maps e quero esse resultado.",
    },
}

PAGINAS = {
    "seo-para-medicos": "imune",
    "seo-para-clinicas": "imune",
    "seo-para-clinicas-de-estetica": "imune",
    "seo-para-dentistas": "imune",
    "marketing-para-clinicas": "imune",
    "como-atrair-mais-pacientes": "imune",
    "google-meu-negocio-para-clinicas": "imune",
    "site-para-clinica": "imune",
    "google-perfil-empresa": "docevidade",
    "google-meu-negocio-goiania": "docevidade",
    "para-comercios-locais": "docevidade",
    "consultoria-seo-local": "nalu",
    "seo-para-imobiliarias": "nalu",
    "criacao-de-sites-goiania": "nalu",
    "agencia-de-marketing-digital-goiania": "nalu",
    # paginas leigas de maior procura (passo 3)
    "como-aparecer-no-google": "nalu",
    "blog/por-que-minha-empresa-nao-aparece-no-google": "imune",
    "blog/como-colocar-minha-empresa-no-google": "docevidade",
}

def caixa(c, data_page, recuo, artigo):
    nums = "".join(
        f'<div class="case-nicho-num"><strong>{n}</strong><span>{r}</span></div>' for n, r in c["numeros"])
    ev = f'data-event="cta_click" data-page="{data_page}"'
    extra = " case-nicho-artigo" if artigo else ""
    linhas = [
        f'<div class="case-nicho-box{extra}">',
        '  <p class="eyebrow">RESULTADO REAL</p>',
        f'  <h2 id="case-nicho-titulo">{c["titulo"]}</h2>',
        f'  <div class="case-nicho-numeros">{nums}</div>',
        f'  <p class="case-nicho-texto">{c["texto"]}</p>',
        '  <div class="case-nicho-acoes">',
        f'    <a href="{WA}{quote(c["wa"])}" class="btn btn-primary" target="_blank" rel="noopener" '
        f'{ev} data-location="case_nicho_whatsapp">Quero esse resultado</a>',
        f'    <a href="/cases/#{c["ancora"]}" class="btn btn-outline" {ev} '
        f'data-location="case_nicho_ver">{c.get("ver", "Ver o case com gráfico")}</a>',
        '  </div>',
        '</div>',
    ]
    return "\n".join(recuo + l for l in linhas)


def bloco(c, data_page, artigo=False):
    if artigo:  # dentro do artigo do blog: so a caixa, sem section/container
        return f"{INI}\n{caixa(c, data_page, '        ', True)}\n        {FIM}\n        "
    return (f'{INI}\n    <section class="case-nicho" aria-labelledby="case-nicho-titulo">\n'
            f'      <div class="container">\n{caixa(c, data_page, "        ", False)}\n'
            f'      </div>\n    </section>\n    {FIM}\n    ')


def main():
    alteradas = 0
    for slug, chave in PAGINAS.items():
        arq = RAIZ / slug / "index.html"
        s = arq.read_text(encoding="utf-8")
        m = re.search(r'data-page="([^"]+)"', s)
        artigo = '<section class="faq-section"' not in s
        novo = bloco(CASES[chave], m.group(1) if m else slug, artigo)
        if INI in s:
            pad = re.compile(re.escape(INI) + r".*?" + re.escape(FIM) + r"\n *", re.S)
            t = pad.sub(lambda _: novo, s, count=1)
        else:
            ancora = '<section class="artigo-faq"' if artigo else '<section class="faq-section"'
            if s.count(ancora) != 1:
                sys.exit(f"{slug}: ancora do FAQ nao encontrada (ou repetida)")
            t = s.replace(ancora, novo + ancora, 1)
        if t != s:
            arq.write_text(t, encoding="utf-8", newline="")
            alteradas += 1
            print(f"{slug}: {chave}")
    print(f"paginas alteradas: {alteradas}")


if __name__ == "__main__":
    main()
