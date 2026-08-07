# -*- coding: utf-8 -*-
"""
Insere links contextuais da divisão nova dentro do conteúdo antigo do site.

Uso:  python scripts/links-internos-divisao.py

Regra seguida (docs/seo-mercados-competitivos-plan.md §6): UM link por página,
dentro de um parágrafo já existente e topicamente compatível — nada de bloco
"veja também" enxertado no fim da página. A frase inserida precisa fazer sentido
para quem está lendo aquele parágrafo, senão o link não entra.

Idempotente: se o link já está no arquivo, o trecho é pulado.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from rcb_base import RAIZ  # noqa: E402

# (arquivo, trecho âncora que já existe, frase inserida antes do </p>)
INSERCOES = [
    (
        "consultoria-seo-local/index.html",
        "Para cidades fora dessa área, o atendimento é online via videochamada — mesma metodologia, mesmo nível de diagnóstico.",
        ' Vale uma distinção: aqui a disputa é pela busca da sua região. Se o seu cliente pode estar '
        'em qualquer lugar do país e o mercado é concorrido, a frente certa é o '
        '<a href="/seo-nacional/">SEO nacional</a> — outro tipo de projeto.',
    ),
    (
        "consultoria-seo/index.html",
        "As páginas acima cobrem as 200 maiores cidades do país, mas o atendimento online funciona em qualquer lugar. Fale comigo e conte onde fica a sua empresa.",
        ' E se a sua disputa não é por cidade nenhuma — se você vende para o Brasil inteiro —, o '
        'caminho é o <a href="/seo-nacional/">SEO nacional</a>.',
    ),
    (
        "auditoria-seo/index.html",
        "A auditoria existe para responder com clareza: o que está bom, o que está quebrado e o que tem maior potencial de melhorar a presença no Google.",
        ' Quando a suspeita recai sobre o perfil de links do site, o aprofundamento é a '
        '<a href="/consultoria-de-backlinks/">consultoria de backlinks</a>; quando o site perdeu '
        'posições que já tinha, o caminho é a '
        '<a href="/recuperacao-de-trafego-organico/">recuperação de tráfego orgânico</a>.',
    ),
    (
        "conteudo-para-seo/index.html",
        "Conteúdo para SEO parte de outra pergunta: o que o seu cliente pesquisa antes de decidir? A partir daí, cada peça tem um papel claro dentro de um conjunto — e aponta para a página que vende.",
        ' Em mercados muito disputados, conteúdo sozinho costuma não bastar: ele precisa vir '
        'acompanhado de <a href="/link-building-para-nichos-competitivos/">construção de '
        'autoridade</a> para sustentar posição.',
    ),
    (
        "acompanhamento-seo/index.html",
        "O acompanhamento existe para sustentar e ampliar o que foi feito, reagindo ao que muda no Google e no mercado, com base nos dados e não no achismo.",
        ' É também no acompanhamento que uma queda aparece cedo — e quedas já instaladas têm '
        'diagnóstico próprio em <a href="/recuperacao-de-trafego-organico/">recuperação de '
        'tráfego orgânico</a>.',
    ),
    (
        "site-otimizado-para-seo/index.html",
        "Um site que ranqueia e converte é construído de dentro para fora: primeiro a estrutura e a intenção de busca, depois a estética. Os dois importam — mas na ordem certa.",
        ' Para operações que vendem online para todo o país — produto digital, plataforma ou '
        'assinatura —, essa construção tem particularidades próprias, tratadas em '
        '<a href="/seo-para-negocios-digitais/">SEO para negócios digitais</a>.',
    ),
]


def main():
    aplicadas = puladas = nao_achadas = 0

    for arquivo, ancora, frase in INSERCOES:
        caminho = os.path.join(RAIZ, arquivo)
        if not os.path.exists(caminho):
            print(f"  !! não existe: {arquivo}")
            nao_achadas += 1
            continue

        with open(caminho, encoding="utf-8") as f:
            html = f.read()

        # Checa se já foi inserido — olhando SÓ o corpo da página. O menu e o
        # rodapé apontam para várias dessas URLs, e conferir o arquivo inteiro
        # daria falso positivo em todas elas.
        corpo = html.split("<main", 1)[-1].split("</main>", 1)[0]
        href = frase.split('href="')[1].split('"')[0]
        if f'href="{href}"' in corpo:
            print(f"  -- já tinha link: {arquivo}")
            puladas += 1
            continue

        if ancora not in html:
            print(f"  !! âncora não encontrada em {arquivo}")
            nao_achadas += 1
            continue

        html = html.replace(ancora, ancora + frase, 1)
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            f.write(html)
        print(f"  ok  {arquivo}")
        aplicadas += 1

    print(f"\nInseridas: {aplicadas} | Já existiam: {puladas} | Falhas: {nao_achadas}")


if __name__ == "__main__":
    main()
