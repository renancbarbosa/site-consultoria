# -*- coding: utf-8 -*-
"""
Liga os 10 artigos do lote 2 ao restante do site.

Uso:  python scripts/ligar-artigos-lote2.py
      python scripts/gerar-paginas-competitivas.py
      python scripts/gerar-artigos-competitivos.py

Edita os MÓDULOS DE CONTEÚDO (não o HTML gerado) para que os links sobrevivam a
qualquer regeração. Depois de rodar, é preciso regerar as páginas e os artigos.

Duas frentes:
  A. páginas comerciais -> artigos novos, via bloco "Continue por aqui"
  B. artigos do lote 1  -> artigos novos, via link contextual dentro do texto

Idempotente: cada substituição só é aplicada se o link ainda não estiver lá.
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CONTEUDO = os.path.join(AQUI, "conteudo")

# ---------------------------------------------------------------
# A. Páginas comerciais -> artigos novos (cards em "Continue por aqui")
#    (arquivo, âncora única, texto inserido logo depois)
# ---------------------------------------------------------------
CARDS = [
    # /seo-para-iptv/  -> artigos 3, 7 e 9
    ("cluster_iptv.py",
     '        ("/blog/dominio-novo-ou-expirado-para-iptv/", "Domínio novo ou expirado?",\n'
     '         "A comparação honesta entre começar do zero e comprar histórico."),',
     '\n        ("/blog/iptv-primeira-pagina-3-4-meses/", "Dá para chegar em 3 ou 4 meses?",\n'
     '         "Um modelo de faixas para saber quais termos são viáveis nesse prazo e quais não são."),\n'
     '        ("/blog/seo-nacional-para-iptv-o-que-muda/", "O que muda na disputa nacional",\n'
     '         "Sem mapa e sem proximidade: o que sobra, e por que o prazo é maior."),\n'
     '        ("/blog/backlinks-para-iptv-funcionam/", "Backlinks funcionam neste nicho?",\n'
     '         "Quais tipos de veículo rendem de verdade e onde a verba costuma ser desperdiçada."),'),

    # /link-building-para-iptv/ -> artigo 7
    ("cluster_iptv.py",
     '        ("/blog/quanto-investir-backlinks-iptv/", "Quanto investir em autoridade",\n'
     '         "Como dimensionar a verba dessa frente dentro do projeto."),',
     '\n        ("/blog/backlinks-para-iptv-funcionam/", "Backlinks para IPTV funcionam?",\n'
     '         "A leitura de eficácia por tipo de veículo, do que mais rende ao que é passivo."),'),

    # /dominio-expirado-para-iptv/ -> artigo 6
    ("cluster_iptv.py",
     '        ("/blog/como-saber-se-dominio-expirado-foi-usado-para-spam/", "Sinais de spam",\n'
     '         "O que procurar para identificar um domínio comprometido antes de comprar."),',
     '\n        ("/blog/como-escolher-dominio-expirado-com-autoridade/", "Como escolher entre candidatos",\n'
     '         "Os critérios de comparação em ordem de peso, e como definir um teto de preço."),'),

    # /analise-de-dominios-expirados/ -> artigo 6
    ("cluster_dominios.py",
     '        ("/blog/dominio-premium-ou-dominio-expirado/", "Premium ou expirado?",\n'
     '         "A comparação entre pagar pelo nome e pagar pelo histórico."),',
     '\n        ("/blog/como-escolher-dominio-expirado-com-autoridade/", "Como escolher entre candidatos",\n'
     '         "Quando você já tem três ou quatro opções e precisa decidir qual comprar."),'),

    # /migracao-de-dominio-seo/ -> artigos 11 e 13
    ("cluster_dominios.py",
     '        ("/blog/trocar-de-dominio-faz-perder-posicoes/", "Trocar faz perder posições?",\n'
     '         "O que realmente acontece e quanto tempo costuma levar a estabilização."),',
     '\n        ("/blog/o-que-acontece-com-seo-ao-trocar-dominio/", "A mecânica da troca",\n'
     '         "O que é reavaliado, o que atravessa pelos redirecionamentos e o que se perde."),\n'
     '        ("/blog/dominio-caiu-o-que-fazer/", "Domínio caiu: o que fazer",\n'
     '         "O diagnóstico das causas — registro, DNS, hospedagem — e o que fazer em cada uma."),'),

    # /recuperacao-de-trafego-organico/ -> artigo 13
    ("cluster_dominios.py",
     '        ("/blog/trocar-de-dominio-faz-perder-posicoes/", "Queda após troca de domínio",\n'
     '         "O cenário mais comum e mais corrigível de todos."),',
     '\n        ("/blog/dominio-caiu-o-que-fazer/", "O site saiu do ar",\n'
     '         "Como descobrir a causa antes de agir, e o impacto real de uma indisponibilidade."),'),

    # /seo-para-bets/ -> artigo 26
    ("cluster_bets.py",
     '        ("/link-building-para-bets/", "Link building para bets",\n'
     '         "A frente que costuma decidir as posições de topo neste setor."),',
     '\n        ("/blog/conteudo-autoridade-conversao-sites-de-apostas/", "Como as três frentes se conectam",\n'
     '         "Conteúdo, autoridade e conversão se condicionam — e o desequilíbrio trava o projeto."),'),

    # /seo-para-afiliados-de-apostas/ -> artigos 20 e 27
    ("cluster_bets.py",
     '        ("/blog/como-criar-paginas-de-avaliacao-de-casas-de-apostas/", "Páginas de avaliação",\n'
     '         "O passo a passo de uma página de review que sustenta posição."),',
     '\n        ("/blog/seo-para-afiliados-como-estruturar-projeto/", "A sequência de execução",\n'
     '         "Em que ordem construir cada camada — e por que a maioria inverte."),\n'
     '        ("/blog/site-de-afiliado-competir-nacionalmente/", "Competir com portal grande",\n'
     '         "Onde um portal pequeno ganha de um grande, e onde não adianta tentar."),'),

    # /criacao-de-site-para-afiliado-de-bet/ -> artigo 27
    ("cluster_bets.py",
     '        ("/blog/como-criar-site-para-afiliado-de-apostas/", "Como criar o site do zero",\n'
     '         "O passo a passo, incluindo o que decidir antes da primeira página."),',
     '\n        ("/blog/site-de-afiliado-competir-nacionalmente/", "O que é preciso para competir",\n'
     '         "A leitura de porte que define onde concentrar esforço."),'),

    # /link-building-para-bets/ -> artigo 21
    ("cluster_bets.py",
     '        ("/blog/quanto-custa-um-backlink-de-qualidade/", "Quanto custa um backlink",\n'
     '         "O que forma o preço e por que o mais caro nem sempre é o melhor."),',
     '\n        ("/blog/link-building-para-bets-o-que-avaliar/", "Como julgar as propostas",\n'
     '         "As sete perguntas a fazer antes de fechar, e os sinais de proposta ruim."),'),
]

# ---------------------------------------------------------------
# B. Artigos do lote 1 -> artigos novos (link contextual no texto)
#    (arquivo, âncora única, texto inserido logo depois)
# ---------------------------------------------------------------
CONTEXTUAIS = [
    # artigo 2 -> artigo 3
    ("artigos_iptv.py",
     "        <p>Se alguém oferece primeira página em poucas semanas nos termos principais, vale perguntar\n"
     "        exatamente qual termo, com qual volume de busca — a resposta costuma revelar que o termo prometido\n"
     "        não é o que interessa.</p>",
     '\n\n        <p>A pergunta fechada — <em>dá para chegar em três ou quatro meses?</em> — é respondida com um\n'
     '        modelo de faixas de dificuldade em\n'
     '        {link(\'/blog/iptv-primeira-pagina-3-4-meses/\', \'IPTV na primeira página em 3 ou 4 meses\')}.</p>'),

    # artigo 8 -> artigo 7
    ("artigos_iptv.py",
     "        <p>Os critérios de seleção estão em\n"
     "        {link('/blog/como-avaliar-qualidade-de-um-backlink/', 'como avaliar a qualidade de um backlink')}.</p>",
     "\n\n        <p>E a leitura de quais tipos de veículo realmente rendem neste nicho está em\n"
     "        {link('/blog/backlinks-para-iptv-funcionam/', 'backlinks para IPTV funcionam?')}.</p>"),

    # artigo 14 -> artigo 6
    ("artigos_dominios.py",
     "        <p>A recomendação que sai daí tem três formas possíveis: comprar, não comprar, ou comprar até\n"
     "        determinado valor. Qualquer conclusão sem um teto de preço está incompleta.</p>",
     "\n\n        <p>Se você tem mais de um candidato aprovado e precisa decidir entre eles, os critérios de\n"
     "        comparação estão em\n"
     "        {link('/blog/como-escolher-dominio-expirado-com-autoridade/', 'como escolher um domínio expirado com autoridade')}.</p>"),

    # artigo 43 -> artigo 11
    ("artigos_dominios.py",
     "        <p>Não existe prazo garantido, e desconfie de quem der um número exato. O que se observa na prática:\n"
     "        sites menores tendem a estabilizar mais rápido, sites grandes levam mais tempo, e o processo é\n"
     "        gradual — não há um dia em que tudo volta.</p>",
     "\n\n        <p>A mecânica por trás disso — o que exatamente é reavaliado e o que atravessa pelos\n"
     "        redirecionamentos — está em\n"
     "        {link('/blog/o-que-acontece-com-seo-ao-trocar-dominio/', 'o que acontece com o SEO quando o domínio é trocado')}.</p>"),

    # artigo 12 -> artigo 13
    ("artigos_dominios.py",
     "        <p><strong>Não desligue o domínio antigo.</strong> Os redirecionamentos precisam continuar\n"
     "        funcionando por bastante tempo — não semanas. Enquanto houver links externos apontando para ele,\n"
     "        ele tem função.</p>",
     "\n\n        <p>Esse ponto é o que separa uma migração planejada de uma perda de domínio. Se o seu caso for\n"
     "        o segundo — o registro venceu, o site saiu do ar —, o diagnóstico está em\n"
     "        {link('/blog/dominio-caiu-o-que-fazer/', 'domínio caiu: o que fazer com o site e o SEO')}.</p>"),

    # artigo 38 -> artigo 21
    ("artigos_backlinks.py",
     "        <p>A última pergunta costuma resolver os casos duvidosos sozinha.</p>",
     "\n\n        <p>Em setores onde chega proposta de link toda semana, vale conhecer também os sinais de oferta\n"
     "        ruim: {link('/blog/link-building-para-bets-o-que-avaliar/', 'link building para bets: o que avaliar')}\n"
     "        trata do mercado de venda de links de um dos nichos mais caros do país.</p>"),

    # artigo 19 -> artigo 20
    ("artigos_bets.py",
     "        <p>Por isso as decisões de estrutura importam tanto: elas determinam se manter o site atualizado é\n"
     "        viável no volume em que esses portais operam. A estratégia de conteúdo está em\n"
     "        {link('/seo-para-afiliados-de-apostas/', 'SEO para afiliados de apostas')}.</p>",
     "\n\n        <p>E a ordem de construção — o que publicar primeiro para o projeto gerar receita durante a\n"
     "        obra — está em\n"
     "        {link('/blog/seo-para-afiliados-como-estruturar-projeto/', 'como estruturar o projeto de um portal de afiliado')}.</p>"),

    # artigo 22 -> artigo 27
    ("artigos_bets.py",
     "        <p>Este conteúdo envelhece rápido. Um calendário de revisão por camada faz parte do projeto, não é\n"
     "        opcional — e a estrutura do site precisa tornar essa revisão viável, com a informação volátil\n"
     "        armazenada em um lugar só. Ver\n"
     "        {link('/blog/como-criar-site-para-afiliado-de-apostas/', 'como criar o site do zero')}.</p>",
     "\n\n        <p>Manter poucas páginas corretas e atualizadas é, aliás, uma das poucas frentes em que um\n"
     "        portal pequeno ganha de um grande — o assunto está em\n"
     "        {link('/blog/site-de-afiliado-competir-nacionalmente/', 'o que um site de afiliado precisa para competir nacionalmente')}.</p>"),

    # artigo 16 -> artigo 26
    ("artigos_bets.py",
     "        <p>Praticamente todo recorte deste setor tem subtemas menos disputados com demanda real —\n"
     "        modalidades específicas, dúvidas de funcionamento, conteúdo de decisão. Conquistar o topo nesses\n"
     "        recortes costuma render mais que ficar na terceira página do termo principal.</p>",
     "\n\n        <p>Antes de decidir onde aplicar o orçamento, vale entender como conteúdo, autoridade e\n"
     "        conversão se condicionam:\n"
     "        {link('/blog/conteudo-autoridade-conversao-sites-de-apostas/', 'as três frentes de um site de apostas')}.</p>"),
]


def aplicar(lista, rotulo):
    aplicadas = puladas = falhas = 0
    for arquivo, ancora, insercao in lista:
        caminho = os.path.join(CONTEUDO, arquivo)
        s = io.open(caminho, encoding="utf-8").read()

        # Idempotência: verifica se ESTA inserção já está logo após ESTA âncora.
        # Checar só o slug no arquivo inteiro daria falso positivo — cada módulo
        # contém várias páginas, e o mesmo artigo é linkado a partir de mais de uma.
        slug = insercao.split("/blog/")[1].split("/")[0]
        if ancora + insercao in s:
            puladas += 1
            continue

        if ancora not in s:
            print(f"  !! âncora não encontrada em {arquivo} (destino: {slug})")
            falhas += 1
            continue

        s = s.replace(ancora, ancora + insercao, 1)
        io.open(caminho, "w", encoding="utf-8", newline="\n").write(s)
        print(f"  ok  {arquivo:26s} -> /blog/{slug}/")
        aplicadas += 1

    print(f"{rotulo}: {aplicadas} inseridas | {puladas} já existiam | {falhas} falhas\n")
    return falhas


def main():
    print("A. Páginas comerciais -> artigos do lote 2")
    f1 = aplicar(CARDS, "A")
    print("B. Artigos do lote 1 -> artigos do lote 2")
    f2 = aplicar(CONTEXTUAIS, "B")

    if f1 or f2:
        print("Houve falhas. Nada foi regerado — corrija as âncoras e rode de novo.")
        return 1
    print("Agora rode:")
    print("  python scripts/gerar-paginas-competitivas.py")
    print("  python scripts/gerar-artigos-competitivos.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
