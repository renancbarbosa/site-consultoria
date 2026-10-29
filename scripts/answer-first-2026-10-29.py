# -*- coding: utf-8 -*-
"""
Fase 4 do pilar SEO para IA (29/10/2026): abertura "resposta primeiro" nas 10 páginas com mais
impressão no Search Console (90 dias, lista em docs/visibilidade-ia/AUDITORIA.md).

O padrão: o primeiro parágrafo da página responde a pergunta do título em até 2 frases, começando
pelo termo da página. O resto do texto que estava ali vai para um segundo parágrafo, logo abaixo.
É o trecho que o Google (AI Overviews) e o ChatGPT recortam para citar.

Diferente do answer-first-2026-09-08.py (que só quebrava parágrafo), aqui o texto foi reescrito à
mão, a pedido do Renan ("coloque tudo nesse padrão"). Por isso as 4 aberturas com gancho editorial
(estética, clínicas, criação de sites, comércio local) também mudaram: a cena continua, só que
depois da resposta.

Estas páginas não têm gerador (o HTML é a fonte), exceto /criacao-de-sites-goiania/, cujo gerador
está travado desde 28/09. /consultor-seo-goiania/ (protegida) fica de fora.
Idempotente. Sem argumento só relata; --aplicar grava.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APLICAR = "--aplicar" in sys.argv

GMN = "(a ficha da sua empresa no Google Maps, com endereço, horário, fotos e avaliações)"
SEO = "(o trabalho de fazer o Google mostrar a sua empresa de graça para quem procura o que você vende)"

TROCAS = {
    "como-aparecer-no-google": (
        '<p class="page-subtitle">Como aparecer no Google é a dúvida de quem vê a cidade inteira pesquisar o que '
        'ele vende, e encontrar o concorrente. Aqui você vê, sem jargão, o que decide quem aparece no Google e no '
        'Google Maps: o cadastro da empresa, o site e as avaliações. E o que fazer quando você já tentou tudo isso e '
        'continua invisível.</p>',
        '<p class="page-subtitle">Para aparecer no Google, a sua empresa precisa de três coisas em ordem: o cadastro '
        'no Google Maps completo, um site que o Google entende e avaliações de clientes. É isso que decide quem '
        'aparece quando a cidade inteira pesquisa o que você vende.</p>\n'
        '          <p class="page-subtitle">Aqui você vê, sem jargão, como cada uma funciona. E o que fazer quando '
        'você já tentou tudo isso e continua invisível.</p>'),
    "seo-para-contadores": (
        '<p class="page-subtitle">SEO ' + SEO + ' para contadores existe porque quem está abrindo empresa, saindo do '
        'MEI ou insatisfeito com o contador atual não pede indicação, pesquisa no Google. A consultoria organiza o '
        'Google Meu Negócio ' + GMN + ', o site com uma página por serviço contábil e o conteúdo que responde as '
        'dúvidas do empreendedor. Atendimento online para todo o Brasil e presencial em Goiânia.</p>',
        '<p class="page-subtitle">SEO ' + SEO + ' para contadores é fazer o seu escritório aparecer no Google quando '
        'o empresário pesquisa quem vai cuidar da contabilidade dele. Quem está abrindo empresa, saindo do MEI ou '
        'insatisfeito com o contador atual não pede indicação: pesquisa no Google.</p>\n'
        '          <p class="page-subtitle">A consultoria organiza o Google Meu Negócio ' + GMN + ', o site com uma '
        'página por serviço contábil e o conteúdo que responde as dúvidas do empreendedor. Atendimento online para '
        'todo o Brasil e presencial em Goiânia.</p>'),
    "seo-para-clinicas-de-estetica": (
        '<p class="page-subtitle">A paciente que vai fazer harmonização, botox ou depilação a laser pesquisa muito '
        'antes de marcar. Ela olha foto de resultado, lê avaliação, compara três clínicas e escolhe uma. Eu faço a '
        'sua aparecer nessa hora, com site e Google Meu Negócio ' + GMN + ' prontos, com orçamento sob medida e '
        'grátis, presencial em Goiânia e online no Brasil inteiro.</p>',
        '<p class="page-subtitle">SEO para clínicas de estética é fazer a sua clínica aparecer no Google e no Google '
        'Maps quando a paciente pesquisa harmonização, botox ou depilação a laser. Antes de marcar, ela olha foto de '
        'resultado, lê avaliação, compara três clínicas e escolhe uma.</p>\n'
        '          <p class="page-subtitle">Eu faço a sua aparecer nessa hora, com site e Google Meu Negócio ' + GMN +
        ' prontos, com orçamento sob medida e grátis, presencial em Goiânia e online no Brasil inteiro.</p>'),
    "criacao-de-sites-goiania": (
        '<p class="page-subtitle">Seu cliente procura no Google o que você vende. Se a sua empresa não tem site, ou '
        'tem um que ninguém encontra, quem aparece é o concorrente. Eu crio o site da sua empresa em Goiânia já '
        'pensado para ser achado no Google e para levar a pessoa até o seu WhatsApp.</p>',
        '<p class="page-subtitle">Criação de sites em Goiânia, do jeito que eu faço, é um site pensado para ser achado '
        'no Google e para levar a pessoa até o seu WhatsApp. Sem isso, quando o seu cliente procura o que você vende, '
        'quem aparece é o concorrente.</p>\n'
        '          <p class="page-subtitle">Vale para quem ainda não tem site e para quem tem um que ninguém '
        'encontra.</p>'),
    "seo-para-clinicas": (
        '<p class="page-subtitle">Hoje até o paciente indicado pesquisa seu nome no Google antes de marcar. Ele olha '
        'as fotos, lê as avaliações, vê se o site explica o que você faz, e só então liga. Eu deixo essa parte '
        'pronta: site e Google Meu Negócio ' + GMN + ', com orçamento sob medida e grátis, presencial em Goiânia e '
        'online no Brasil inteiro.</p>',
        '<p class="page-subtitle">SEO para clínicas é deixar a sua clínica pronta para ser encontrada e escolhida no '
        'Google, com site e Google Meu Negócio ' + GMN + ' completos. Hoje até o paciente indicado pesquisa seu nome '
        'no Google antes de marcar.</p>\n'
        '          <p class="page-subtitle">Ele olha as fotos, lê as avaliações, vê se o site explica o que você faz, '
        'e só então liga. Eu deixo essa parte pronta, com orçamento sob medida e grátis, presencial em Goiânia e '
        'online no Brasil inteiro.</p>'),
    "seo-para-pequenas-empresas": (
        '<p class="page-subtitle">SEO ' + SEO + ' para pequenas empresas parte de um fato: empresa pequena não compete '
        'com as grandes em verba de anúncio, e não precisa. A disputa que traz cliente acontece na sua cidade, no seu '
        'bairro, na pesquisa "perto de mim". Nessa disputa, ganha quem está mais bem organizado no Google, não quem '
        'tem mais dinheiro.</p>',
        '<p class="page-subtitle">SEO ' + SEO + ' para pequenas empresas é ganhar cliente pelo Google sem disputar '
        'verba de anúncio com as grandes. A disputa que traz cliente acontece na sua cidade, no seu bairro, na '
        'pesquisa "perto de mim", e nela ganha quem está mais bem organizado no Google, não quem tem mais '
        'dinheiro.</p>'),
    "google-perfil-empresa": (
        '<p class="page-subtitle">O Google Perfil da Empresa ' + GMN + ', que durante anos foi chamado de Google Meu '
        'Negócio, é o que decide como o seu negócio aparece no Google Maps e na busca local, a base de qualquer '
        'trabalho de <a href="/seo-local-goiania/">SEO local</a>. Um perfil bem configurado transmite confiança, '
        'responde dúvidas e leva o cliente ao WhatsApp, à rota ou à ligação.</p>',
        '<p class="page-subtitle">O Google Perfil da Empresa ' + GMN + ', antigo Google Meu Negócio, é o que decide '
        'como o seu negócio aparece no Google Maps e na busca local. Otimizar o perfil é deixar essa ficha completa e '
        'certa, para ela levar o cliente ao WhatsApp, à rota ou à ligação.</p>\n'
        '          <p class="page-subtitle">É a base de qualquer trabalho de <a href="/seo-local-goiania/">SEO '
        'local</a>, e um perfil bem configurado também transmite confiança e responde dúvidas antes do '
        'contato.</p>'),
    "para-comercios-locais": (
        '            Restaurante, loja, salão, pet shop, oficina, qualquer negócio elegível para o Perfil da Empresa '
        'pode disputar buscas locais. Eu organizo seu perfil no Maps e seu site, com orçamento sob medida e grátis. '
        'Presencial',
        '            SEO ' + SEO + ' para comércio local é colocar o seu negócio entre os três primeiros do mapa quando alguém '
        'busca "perto de mim". Eu organizo seu perfil no Maps e seu site para isso, com orçamento sob medida e grátis. '
        'Restaurante, loja, salão, pet shop, oficina: qualquer negócio elegível para o Perfil da Empresa pode '
        'disputar buscas locais. Presencial'),
    "seo-para-imobiliarias": (
        '<p class="page-subtitle">SEO ' + SEO + ' para imobiliárias começa por uma conta simples: o portal traz '
        'contato, cobrando por ele, e entregando o mesmo contato para três concorrentes. O caminho para ter cliente '
        'exclusivo é ser encontrado direto: no Google Maps ("imobiliária no bairro"), nas buscas do seu recorte e no '
        'conteúdo sobre a sua região. A consultoria organiza essa presença para imobiliárias e corretores.</p>',
        '<p class="page-subtitle">SEO ' + SEO + ' para imobiliárias é ser encontrado direto pelo cliente no Google, '
        'sem pagar portal por cada contato. Isso acontece no Google Maps ("imobiliária no bairro"), nas buscas do seu '
        'recorte e no conteúdo sobre a sua região.</p>\n'
        '          <p class="page-subtitle">A conta é simples: o portal traz contato, cobrando por ele, e entrega o '
        'mesmo contato para três concorrentes. A consultoria organiza essa presença própria para imobiliárias e '
        'corretores.</p>'),
    "guia-seo-local": (
        '<p class="page-subtitle">Este guia de SEO local ' + SEO + ' é organizado por tema para empresas locais e '
        'profissionais de serviço entenderem, passo a passo, como aparecer melhor no Google: organizar a presença '
        'digital, otimizar o Google Perfil da Empresa ' + GMN + ', estruturar o site, produzir conteúdo, converter '
        'visitas em contato e acompanhar a evolução. Cada bloco reúne os conteúdos certos e aponta para o serviço '
        'correspondente.</p>',
        '<p class="page-subtitle">SEO local ' + SEO + ' é o que faz a sua empresa aparecer no Google e no Google Maps '
        'para os clientes da sua cidade. Este guia mostra, passo a passo e por tema, como chegar '
        'lá.</p>\n'
        '          <p class="page-subtitle">Os temas são: organizar a presença digital, otimizar o Google Perfil da '
        'Empresa ' + GMN + ', estruturar o site, produzir conteúdo, converter visitas em contato e acompanhar a '
        'evolução. Cada bloco reúne os conteúdos certos e aponta para o serviço correspondente.</p>'),
}


def main():
    alteradas = []
    for slug, (velho, novo) in TROCAS.items():
        f = os.path.join(RAIZ, slug, "index.html")
        h = io.open(f, encoding="utf-8").read()
        if novo in h:
            continue
        assert h.count(velho) == 1, (slug, h.count(velho))
        alteradas.append(slug)
        if APLICAR:
            io.open(f, "w", encoding="utf-8", newline="").write(h.replace(velho, novo))
    print("%s: %d" % ("alteradas" if APLICAR else "seriam alteradas", len(alteradas)))
    for s in alteradas:
        print("  ", s)


if __name__ == "__main__":
    main()
