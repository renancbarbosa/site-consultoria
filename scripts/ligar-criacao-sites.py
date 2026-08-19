# -*- coding: utf-8 -*-
"""Liga o site a /criacao-de-sites-goiania/ e registra a URL no sitemap.

Insere links editoriais contextuais (fora de menu e rodape) a partir das paginas
que ja falam de site e/ou de Goiania. As ancoras variam de proposito - repetir a
mesma frase em todas as origens e o padrao que o Google trata como link em bloco.

REGRA DESTA RODADA: /consultor-seo-goiania/ e PAGINA PROTEGIDA (4a posicao organica
para "consultor seo goiania", conferido em 18/08/2026). Nenhum link e inserido nela,
nem no menu (que e sitewide e alteraria o perfil de links dela).

Idempotente: se o link ja existe no arquivo, a pagina e pulada.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = "/criacao-de-sites-goiania/"
PROTEGIDA = os.path.join(RAIZ, "consultor-seo-goiania", "index.html")

# (arquivo, trecho exato que existe hoje, trecho novo com o link)
INSERCOES = [
    ("site-otimizado-para-seo/index.html",
     u"Os dois importam — mas na ordem certa.</p>",
     u"Os dois importam — mas na ordem certa. Se a sua empresa fica em Goiânia e o "
     u"site ainda nem existe, o caminho é a <a href=\"/criacao-de-sites-goiania/\">"
     u"criação de sites em Goiânia</a>, que já sai com o Perfil da Empresa "
     u"configurado junto.</p>"),

    ("seo-local-goiania/index.html",
     u"Site sem otimização local enfraquece o sinal do perfil.",
     u"Site sem otimização local enfraquece o sinal do perfil — e quem ainda não "
     u"tem site começa pela <a href=\"/criacao-de-sites-goiania/\">criação do site "
     u"da empresa em Goiânia</a>."),

    ("para-comercios-locais/index.html",
     u"Deixo o site rápido e escrito para as buscas do seu bairro e da sua cidade, "
     u"com o texto que o cliente da sua região realmente procura.</p>",
     u"Deixo o site rápido e escrito para as buscas do seu bairro e da sua cidade, "
     u"com o texto que o cliente da sua região realmente procura. Se você ainda não "
     u"tem site e o comércio é em Goiânia, veja a <a href=\"/criacao-de-sites-goiania/\">"
     u"criação de sites em Goiânia</a>.</p>"),

    ("blog/site-barato-empresa-local-vale-a-pena/index.html",
     u"É aí que o desconto vira prejuízo.</p>",
     u"É aí que o desconto vira prejuízo. Em Goiânia, o valor de um site feito "
     u"para ser encontrado está na tela na página de "
     u"<a href=\"/criacao-de-sites-goiania/\">criação de sites em Goiânia</a>, "
     u"sem \"solicite um orçamento\".</p>"),

    ("blog/melhorar-site-atual-ou-fazer-um-novo/index.html",
     u"Reconstruir seria desperdiçar uma base aproveitável.</p>",
     u"Reconstruir seria desperdiçar uma base aproveitável. Quando a base não existe "
     u"— ou nem há site — aí sim vale começar do zero: veja como funciona a "
     u"<a href=\"/criacao-de-sites-goiania/\">criação de um site novo em Goiânia</a>.</p>"),

    ("blog/site-bonito-nao-aparece-no-google/index.html",
     u"Quase sempre, falta SEO onde sobra estética — e isso tem conserto.</p>",
     u"Quase sempre, falta SEO onde sobra estética — e isso tem conserto. Quando o "
     u"conserto sai mais caro que recomeçar, a saída é a "
     u"<a href=\"/criacao-de-sites-goiania/\">criação de sites em Goiânia</a> "
     u"feita já com a estrutura certa.</p>"),

    ("blog/como-divulgar-minha-empresa-em-goiania/index.html",
     u"Eu reviso perfil, site, buscas e caminho até o WhatsApp.</p>",
     u"Eu reviso perfil, site, buscas e caminho até o WhatsApp — e, se a sua empresa "
     u"ainda não tem site, começamos pela "
     u"<a href=\"/criacao-de-sites-goiania/\">criação do site em Goiânia</a>.</p>"),

    ("blog/paginas-que-empresa-local-precisa-no-site/index.html",
     u"Não sabe se o seu site tem as páginas certas — ou se está perdendo buscas "
     u"por falta delas?</p>",
     u"Não sabe se o seu site tem as páginas certas — ou se está perdendo buscas "
     u"por falta delas? Em Goiânia, essas páginas já vêm montadas na "
     u"<a href=\"/criacao-de-sites-goiania/\">criação do site</a>.</p>"),

    ("blog/site-ou-instagram-para-empresa-local/index.html",
     u"investir no site, no perfil do Google ou ajustar o que já existe?</p>",
     u"investir no site, no perfil do Google ou ajustar o que já existe? Para empresa de "
     u"Goiânia que só tem Instagram, o primeiro passo costuma ser a "
     u"<a href=\"/criacao-de-sites-goiania/\">criação de sites em Goiânia</a>.</p>"),
]

ENTRADA_SITEMAP = (u"  <url>\n"
                   u"    <loc>https://rcbseo.com.br/criacao-de-sites-goiania/</loc>\n"
                   u"    <lastmod>2026-08-18</lastmod>\n"
                   u"    <changefreq>monthly</changefreq>\n"
                   u"    <priority>0.9</priority>\n"
                   u"  </url>\n")


def main():
    alterados, pulados, falhas = 0, 0, []
    for rel, antigo, novo in INSERCOES:
        caminho = os.path.join(RAIZ, rel.replace("/", os.sep))
        if os.path.abspath(caminho) == os.path.abspath(PROTEGIDA):
            raise SystemExit("ERRO: tentativa de escrever na pagina protegida")
        if not os.path.exists(caminho):
            falhas.append((rel, "arquivo nao existe"))
            continue
        html = io.open(caminho, encoding="utf-8", newline="").read()
        if DESTINO in html:
            pulados += 1
            continue
        if html.count(antigo) != 1:
            falhas.append((rel, "trecho ancora aparece %d vez(es)" % html.count(antigo)))
            continue
        io.open(caminho, "w", encoding="utf-8", newline="").write(html.replace(antigo, novo))
        alterados += 1
        print("  link inserido em /%s" % rel.replace("index.html", ""))

    sm = os.path.join(RAIZ, "sitemap.xml")
    conteudo = io.open(sm, encoding="utf-8", newline="").read()
    if DESTINO not in conteudo:
        conteudo = conteudo.replace(u"</urlset>", ENTRADA_SITEMAP + u"</urlset>")
        io.open(sm, "w", encoding="utf-8", newline="").write(conteudo)
        print("  sitemap: URL acrescentada")
    else:
        print("  sitemap: URL ja estava la")

    protegida = io.open(PROTEGIDA, encoding="utf-8", newline="").read()
    print("\npaginas alteradas: %d | ja tinham o link: %d" % (alterados, pulados))
    print("total de <loc> no sitemap: %d"
          % io.open(sm, encoding="utf-8").read().count("<loc>"))
    print("pagina protegida contem link novo? %s (esperado: False)"
          % (DESTINO in protegida))
    if falhas:
        print("\nFALHAS (nenhuma alteracao feita nestas):")
        for rel, motivo in falhas:
            print("  %-60s %s" % (rel, motivo))


if __name__ == "__main__":
    main()
