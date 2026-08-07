# -*- coding: utf-8 -*-
"""
Cluster A — páginas centrais da divisão de mercados competitivos.

A1 /seo-para-mercados-competitivos/  (pilar/hub da divisão)
A2 /seo-nacional/
A3 /seo-para-nichos-competitivos/
A4 /seo-agressivo/
A5 /seo-para-negocios-digitais/

Cada página compõe suas próprias seções, na ordem que faz sentido para a sua
intenção de busca. Nenhuma reaproveita o texto da outra — ver
docs/seo-mercados-competitivos-plan.md §3 para a matriz de diferenciação.
"""
from rcb_base import (
    BASE_URL, head_comum, montar, breadcrumb_html, hero, sec_texto, sec_split,
    cards, problem_cards, passos, lista, tabela, pills, sec_faq, cta_final,
    relacionados, grafo, schema_webpage, schema_breadcrumb, schema_service,
    schema_faq, whats_link,
)

HOJE = "2026-08-06"
ANALISE = "/analise-de-projeto/"


# ============================================================
# A1 — /seo-para-mercados-competitivos/  (pilar da divisão)
# ============================================================

def a1_mercados_competitivos():
    slug = "seo-para-mercados-competitivos"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para mercados competitivos | Projeto nacional | RCB"
    desc = ("Projeto completo de SEO para nichos de alta concorrência: site, conteúdo, "
            "autoridade e acompanhamento. Disputa nacional. Peça a análise do projeto.")
    page_id = "mercados-competitivos"

    faq = [
        ("A RCB constrói o projeto do zero, incluindo marca e site?",
         "Sim. Boa parte dos projetos desta divisão começa sem nada no ar: nome, domínio, identidade, "
         "site, estrutura de conteúdo e plano de autoridade são construídos juntos. Quando já existe "
         "site, o ponto de partida é uma auditoria do que dá para aproveitar."),
        ("Por que um projeto desses custa mais que uma consultoria comum?",
         "Porque o volume de trabalho é outro. Em um mercado disputado, não basta ajustar páginas: é "
         "preciso produzir conteúdo continuamente, construir autoridade fora do site e manter execução "
         "técnica por vários meses. O custo acompanha a quantidade de execução, não o tamanho da empresa."),
        ("Em quanto tempo o projeto começa a dar resultado?",
         "Depende da concorrência do termo, da idade do domínio e do ritmo de execução acordado. Os "
         "primeiros sinais costumam ser de cauda longa e aparecem antes dos termos principais. O prazo "
         "de cada meta é estimado na análise do projeto e revisado no acompanhamento — não é garantido."),
        ("Vocês garantem primeira página?",
         "Não, e desconfie de quem garante. Nenhum fornecedor controla o algoritmo do Google. O que a "
         "RCB assume é o plano de execução, as metas de posicionamento e o acompanhamento do que está "
         "avançando ou travando — com relatório do que foi feito e do que os dados mostram."),
        ("Preciso continuar investindo depois dos primeiros meses?",
         "Na maioria dos nichos competitivos, sim. Concorrente que continua publicando e construindo "
         "autoridade recupera terreno. A intensidade pode cair depois da fase de construção, mas parar "
         "por completo costuma significar perder posição ao longo do tempo."),
        ("Que tipo de projeto a RCB não aceita?",
         "Operações que dependam de burlar bloqueio judicial ou administrativo, uso de marca de "
         "terceiros sem autorização, ou distribuição de conteúdo sem direito sobre ele. Isso é "
         "verificado na análise do projeto, antes de qualquer proposta."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", canonical)]),
        schema_service("SEO para mercados competitivos",
                       "Projeto completo de SEO para nichos de alta concorrência com disputa nacional: "
                       "criação de site, arquitetura de conteúdo, construção de autoridade e acompanhamento.",
                       canonical, tipo="SEO para mercados competitivos"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para mercados competitivos", canonical)])

    painel = """<h2>O que entra em um projeto</h2>
          <ul class="audit-list">
            <li><strong>Marca e domínio</strong> — quando o projeto nasce do zero.</li>
            <li><strong>Site</strong> construído para conversão e para escalar em conteúdo.</li>
            <li><strong>Arquitetura de palavras-chave</strong> por intenção, não por lista solta.</li>
            <li><strong>Produção contínua</strong> de conteúdo comercial e informacional.</li>
            <li><strong>Autoridade</strong> construída fora do site, em ritmo controlado.</li>
            <li><strong>Acompanhamento</strong> com relatório do que avançou e do que travou.</li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:.75rem;">O escopo exato sai da análise do projeto — nem todo caso precisa de tudo.</p>"""

    corpo = hero(
        trilha,
        "Divisão nacional · alta concorrência",
        "SEO para mercados competitivos: projeto completo para disputar o Brasil inteiro",
        "Estratégias completas de site, conteúdo, autoridade e SEO para empresas e investidores que "
        "precisam competir nacionalmente — em nichos onde ajustar meta tag não muda nada.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#mercados", "Ver os mercados atendidos"),
        painel, page_id,
    )

    corpo += sec_texto(
        "O problema",
        "Quando o SEO comum para de resolver",
        problem_cards([
            ("A primeira página já está ocupada há anos",
             "Os resultados que aparecem não são sites recém-criados. São domínios antigos, com histórico, "
             "volume de conteúdo e links acumulados. Entrar nessa disputa não é questão de otimizar — é "
             "questão de construir algo comparável."),
            ("O concorrente publica todo dia",
             "Em nicho disputado, conteúdo não é projeto de três meses. Quem está na frente mantém ritmo. "
             "Um site que publica dez páginas e para não sustenta posição contra quem publica toda semana."),
            ("Ninguém linka para você espontaneamente",
             "Fora de temas editorialmente atraentes, links não aparecem sozinhos. A autoridade precisa ser "
             "construída de forma deliberada, com critério de relevância e ritmo — e isso é trabalho, não compra avulsa."),
            ("O projeto ainda nem existe",
             "Boa parte dos casos começa sem marca, sem domínio e sem site. Contratar SEO antes de existir "
             "estrutura só faz sentido se quem faz o SEO também constrói a estrutura."),
        ]),
        "problema-titulo", classe="problem-section",
        desc="Existe um ponto em que otimização de página deixa de ser o gargalo. "
             "Reconhecer esse ponto é o que separa um projeto que anda de um que fica orçando serviço errado.",
    )

    corpo += sec_split(
        "Perfil do cliente",
        "Para quem este projeto foi desenhado — e para quem não foi",
        """          <p>Esta divisão atende quem precisa de uma <strong>operação digital inteira</strong>, não de um
          ajuste pontual. Na prática, é quem se reconhece aqui:</p>
"""
        + lista([
            "Empresário ou investidor que vai lançar um projeto digital e quer que ele nasça posicionado.",
            "Operação que já fatura e depende demais de anúncio — e quer um canal que não pare quando a verba para.",
            "Marca nacional disputando termos genéricos contra concorrentes maiores e mais antigos.",
            "Afiliado ou portal de conteúdo que vive de posicionamento orgânico.",
            "Empresa estrangeira entrando no Brasil e precisando de presença em português.",
        ])
        + """
          <p>E não faz sentido se você atende só a sua cidade e quer aparecer no mapa: esse é outro
          serviço, mais barato e mais rápido — veja a <a href="/consultoria-seo-local/">consultoria de SEO local</a>
          ou a <a href="/consultoria-seo/">consultoria por cidade</a>. Também não faz sentido se a expectativa
          é resultado em poucas semanas sem investimento proporcional.</p>""",
        """<h3>Critério de atendimento</h3>
          <p>Antes de qualquer proposta, a análise do projeto verifica a base do negócio: o que é
          distribuído ou vendido, se há direito ou autorização sobre isso, e qual a situação regulatória
          da operação.</p>
          <p>Projetos que dependem de contornar bloqueio judicial ou administrativo, usar marca de
          terceiros sem autorização ou distribuir conteúdo protegido sem direito <strong>não são
          atendidos</strong> — independentemente do valor.</p>""",
        "perfil-titulo",
    )

    corpo += sec_texto(
        "O que é entregue",
        "Quatro frentes que andam juntas",
        cards([
            (None, "1. Estrutura", "Marca, domínio e site — ou auditoria e reconstrução do que já existe. "
                                   "Sem base técnica sólida, o resto não sustenta.", None),
            (None, "2. Conteúdo", "Arquitetura por intenção de busca: páginas comerciais, conteúdo de "
                                  "decisão e conteúdo informacional, publicados em ritmo constante.", None),
            (None, "3. Autoridade", "Construção de menções e links com critério de relevância temática, "
                                    "em ritmo que não destoe do perfil natural do site.", None),
            (None, "4. Acompanhamento", "Medição do que entrou no índice, do que ganhou posição e do que "
                                        "não saiu do lugar — com decisão de rota a cada ciclo.", None),
        ]),
        "entregaveis-titulo",
        desc="Em mercado competitivo, essas quatro frentes não funcionam separadas. Conteúdo sem "
             "autoridade não sobe; autoridade sem conteúdo não tem o que sustentar; nenhum dos dois "
             "resolve se a estrutura técnica atrapalha.",
    )

    corpo += sec_texto(
        "Como funciona",
        "O processo, do diagnóstico à manutenção",
        passos([
            ("Análise do projeto", "Leitura do mercado, da SERP, da concorrência real e da situação do negócio. "
                                   "Sai daqui o escopo, a estimativa de prazo e a faixa de investimento."),
            ("Construção", "Marca, domínio, site e arquitetura de conteúdo. É a fase mais pesada e a que "
                           "define o teto do projeto."),
            ("Publicação em ritmo", "Conteúdo entrando de forma contínua, priorizado por intenção comercial "
                                    "e por dificuldade de disputa."),
            ("Autoridade", "Construção de menções e links, iniciada depois que existe conteúdo que justifique "
                           "a referência."),
            ("Leitura e ajuste", "Relatório periódico, revisão de prioridade e correção de rota conforme "
                                 "os dados de indexação e posição."),
        ]),
        "processo-titulo", classe="metodo",
        desc="A ordem importa. Construir autoridade para um site sem conteúdo é desperdício; "
             "publicar conteúdo sobre uma estrutura quebrada também.",
    )

    corpo += sec_split(
        "Investimento",
        "Por que esses projetos exigem outro nível de investimento",
        """          <p>A conta é de execução, não de tabela. O que move a faixa de investimento de um projeto
          para cima é sempre a mesma coisa: <strong>quanto trabalho é preciso para chegar perto de quem
          já está na frente</strong>.</p>
"""
        + tabela(
            ["O que pesa", "Projeto leve", "Projeto de alta concorrência"],
            [
                ["Concorrentes na primeira página", "poucos, e mal estruturados", "domínios antigos, com histórico e volume"],
                ["Volume de conteúdo", "dezenas de páginas", "centenas, com atualização contínua"],
                ["Autoridade necessária", "pouca ou nenhuma", "construção constante por vários meses"],
                ["Ponto de partida", "site já existente", "marca, domínio e site do zero"],
                ["Horizonte de execução", "meses", "trimestres, com manutenção depois"],
            ],
            nota="Comparação de esforço, não tabela de preço. A faixa de cada projeto é definida na análise.",
        )
        + """
          <p>É por isso que o formulário de análise pergunta faixa de investimento inicial e mensal:
          sem essa informação, qualquer proposta seria chute. Um projeto subfinanciado em nicho duro
          não entrega meio resultado — costuma não entregar resultado nenhum, porque não atinge o
          patamar mínimo de execução que o mercado exige.</p>""",
        """<h3>O que não muda o preço</h3>
          <ul class="audit-list">
            <li>O tamanho da sua empresa.</li>
            <li>Quantos funcionários você tem.</li>
            <li>O quanto você espera faturar.</li>
          </ul>
          <h3 style="margin-top:1.25rem;">O que muda</h3>
          <ul class="audit-list">
            <li>A dificuldade real da SERP que você quer disputar.</li>
            <li>Se existe estrutura ou se começa do zero.</li>
            <li>O ritmo de conteúdo acordado.</li>
            <li>A intensidade da construção de autoridade.</li>
            <li>O prazo desejado — apertar prazo aumenta custo.</li>
          </ul>""",
        "investimento-titulo",
    )

    corpo += sec_split(
        "Prazo e limites",
        "O que é honesto dizer sobre prazo",
        """          <p>Não existe prazo garantido em SEO, e quem oferece isso está vendendo o que não controla.
          O que dá para fazer é estimar cenários e acompanhar de perto.</p>
          <p>Na prática, os primeiros movimentos aparecem em termos de <strong>cauda longa</strong> —
          buscas mais específicas, com menos disputa. Os termos principais, os que motivaram o projeto,
          vêm depois, e dependem de o site ter acumulado conteúdo e autoridade suficientes para ser
          considerado uma alternativa legítima àqueles que já ocupam a página.</p>
          <p>Três fatores mexem mais no prazo do que qualquer outro: a <strong>idade e o histórico do
          domínio</strong>, o <strong>ritmo real de publicação</strong> e a <strong>força de quem já
          está posicionado</strong>. Nenhum deles é ajustável por técnica — só por tempo e execução.</p>
          <p>Se o prazo desejado for muito curto para a disputa pretendida, isso é dito na análise, com
          as alternativas: mirar termos menos disputados primeiro, considerar
          <a href="/analise-de-dominios-expirados/">um domínio com histórico</a> ou rever o alvo.</p>""",
        """<h3>O que a RCB não promete</h3>
          <ul class="audit-list">
            <li>Primeira posição garantida.</li>
            <li>Primeira página garantida.</li>
            <li>Prazo garantido de ranqueamento.</li>
            <li>Resultado garantido pelo Google.</li>
            <li>Quantidade ilimitada de backlinks.</li>
            <li>Que trocar de domínio preserva posições.</li>
          </ul>
          <p style="margin-top:1rem;">O que é assumido: o plano, a execução, a medição e a transparência
          sobre o que está funcionando e o que não está.</p>""",
        "prazo-titulo",
    )

    corpo += sec_texto(
        "Mercados atendidos",
        "Onde a RCB aplica esse método",
        cards([
            ("/seo-para-iptv/", "IPTV e streaming",
             "Projeto completo para operadores e distribuidores licenciados: marca, site, conteúdo e autoridade.",
             "Ver SEO para IPTV"),
            ("/seo-para-bets/", "Bets e apostas",
             "Marcas, plataformas e portais do setor de apostas, com comunicação adequada às regras aplicáveis.",
             "Ver SEO para bets"),
            ("/seo-para-afiliados-de-apostas/", "Afiliados de apostas",
             "Portais de review, comparação e bônus que vivem de posicionamento orgânico.",
             "Ver SEO para afiliados"),
            ("/seo-para-igaming/", "iGaming (B2B)",
             "Provedores, plataformas e sistemas que vendem para operadores e estão entrando no Brasil.",
             "Ver SEO para iGaming"),
            ("/seo-para-negocios-digitais/", "Negócios digitais",
             "Produtos digitais, plataformas e negócios por assinatura com operação nacional.",
             "Ver negócios digitais"),
            ("/seo-para-jogos-online/", "Jogos online",
             "Portais, plataformas e apps de jogos — aquisição orgânica e conteúdo de comunidade.",
             "Ver SEO para jogos online"),
        ]),
        "mercados-titulo", classe="cluster-section",
        desc="São mercados diferentes, com a mesma característica: primeira página cara, concorrente "
             "bem estruturado e pouco espaço para improviso.",
    )

    corpo += sec_texto(
        "Serviços avulsos",
        "Frentes que também são contratadas separadamente",
        cards([
            ("/seo-nacional/", "SEO nacional",
             "Para quem já tem operação e quer sair do alcance regional para disputa em todo o Brasil.",
             "Ver SEO nacional"),
            ("/link-building-para-nichos-competitivos/", "Link building",
             "Construção de autoridade com critério de relevância, ritmo e avaliação de risco.",
             "Ver link building"),
            ("/analise-de-dominios-expirados/", "Análise de domínios expirados",
             "Triagem e avaliação de histórico, perfil de links e risco antes de qualquer compra.",
             "Ver análise de domínios"),
            ("/migracao-de-dominio-seo/", "Migração de domínio",
             "Troca de domínio, rebrand ou consolidação de sites com processo técnico controlado.",
             "Ver migração de domínio"),
            ("/consultoria-de-backlinks/", "Consultoria de backlinks",
             "Auditoria do perfil de links existente, identificação de risco e plano de prioridade.",
             "Ver consultoria de backlinks"),
            ("/recuperacao-de-trafego-organico/", "Recuperação de tráfego",
             "Diagnóstico de queda de posição e plano de recuperação para sites que perderam visibilidade.",
             "Ver recuperação de tráfego"),
        ]),
        "servicos-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre projetos competitivos")

    corpo += cta_final(
        "Quer saber se o seu projeto é viável — e a que custo?",
        "A análise do projeto é o primeiro passo. Você descreve o mercado, o estágio atual e o objetivo; "
        "eu devolvo a leitura da concorrência, o escopo necessário, a estimativa de prazo e a faixa de "
        "investimento. Sem proposta genérica.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/blog/quanto-custa-chegar-primeira-pagina/", "Antes disso: quanto custa chegar à primeira página?"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Tenho um projeto em um mercado competitivo e quero solicitar a análise.",
        float_aria="Solicitar análise de projeto competitivo pelo WhatsApp",
    )


# ============================================================
# A2 — /seo-nacional/
# ============================================================

def a2_seo_nacional():
    slug = "seo-nacional"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO nacional: apareça em todo o Brasil | RCB Consultoria"
    desc = ("SEO nacional para empresas que disputam buscas em todo o Brasil. A diferença para o "
            "SEO local, o prazo real e como o projeto é estruturado.")
    page_id = "seo-nacional"

    faq = [
        ("Qual a diferença prática entre SEO local e SEO nacional?",
         "No SEO local, a disputa é filtrada pela localização de quem pesquisa — você compete com quem "
         "está por perto, e o Google Perfil da Empresa pesa muito. No SEO nacional não existe esse filtro: "
         "você compete com todo mundo do Brasil ao mesmo tempo, e o que decide é conteúdo, estrutura e autoridade."),
        ("Minha empresa é local. Faz sentido investir em SEO nacional?",
         "Só se você vende para fora da sua região. Se o atendimento é presencial e limitado a uma cidade, "
         "SEO nacional gasta esforço em visitantes que não podem comprar de você. Nesse caso a "
         "consultoria de SEO local resolve melhor e mais barato."),
        ("Dá para fazer os dois ao mesmo tempo?",
         "Dá, e em alguns casos é o certo: uma operação com atendimento presencial em uma cidade e venda "
         "online para o Brasil inteiro precisa das duas frentes. Elas usam páginas diferentes, para não "
         "competirem entre si dentro do próprio site."),
        ("Preciso de páginas para cada cidade do Brasil?",
         "Depende da intenção da busca. Se as pessoas pesquisam com nome de cidade, páginas regionais fazem "
         "sentido e precisam ter conteúdo próprio de verdade. Se pesquisam sem cidade nenhuma, criar centenas "
         "de páginas quase iguais só gera conteúdo repetido e problema de canibalização."),
        ("Quanto tempo demora para posicionar nacionalmente?",
         "Mais do que localmente, quase sempre. A disputa é maior e a autoridade necessária é maior. O prazo "
         "de cada meta é estimado na análise e depende do domínio, da concorrência e do ritmo de execução — "
         "não é garantido por nenhum fornecedor."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO nacional", canonical)]),
        schema_service("SEO nacional",
                       "Projeto de SEO para disputa de buscas em todo o território nacional: arquitetura "
                       "de conteúdo, autoridade e execução técnica para operações que vendem para o Brasil inteiro.",
                       canonical, tipo="SEO nacional"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("SEO nacional", canonical)])

    corpo = hero(
        trilha,
        "Alcance nacional",
        "SEO nacional: estrutura para disputar pesquisas em todo o Brasil",
        "Quando o cliente pode estar em qualquer lugar do país, a disputa muda de natureza. "
        "Não é o mesmo trabalho do SEO local feito em escala maior — é outro projeto.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#local-x-nacional", "Ver a diferença para o SEO local"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "A diferença que mais confunde",
        "SEO local e SEO nacional não são o mesmo serviço em tamanhos diferentes",
        tabela(
            ["", "SEO local", "SEO nacional"],
            [
                ["Quem é o concorrente", "quem atende a mesma região", "qualquer site do Brasil"],
                ["Peso do Google Perfil da Empresa", "alto — mapa e proximidade decidem", "baixo ou nulo"],
                ["O que mais pesa", "perfil, avaliações, sinais locais", "conteúdo, estrutura e autoridade"],
                ["Volume de conteúdo necessário", "moderado", "alto e contínuo"],
                ["Papel dos backlinks", "secundário na maioria dos casos", "determinante"],
                ["Prazo típico até tração", "mais curto", "mais longo"],
                ["Onde o resultado aparece", "Maps e busca com cidade", "busca orgânica sem filtro geográfico"],
            ],
            nota="Comparação estrutural entre os dois modelos de disputa. Prazos variam por nicho e não são garantidos.",
        ),
        "local-x-nacional", classe="solution-section",
        desc="Essa confusão custa caro: empresa local pagando por projeto nacional que não converte, "
             "e operação nacional presa a uma estratégia de bairro. Se a sua dúvida é qual dos dois é o "
             "seu caso, o artigo <a href=\"/blog/seo-local-ou-seo-nacional-diferenca/\">SEO local ou SEO "
             "nacional</a> destrincha isso com exemplos.",
    )

    corpo += sec_split(
        "Quando faz sentido",
        "Sinais de que o seu caso é nacional",
        """          <p>A pergunta não é o tamanho da empresa. É <strong>onde está o cliente que pode comprar
          de você</strong>. Se a resposta é "em qualquer lugar do Brasil", a disputa é nacional:</p>
"""
        + lista([
            "Você vende, entrega ou atende online, sem limite de distância.",
            "Seu produto é digital: assinatura, plataforma, software, conteúdo.",
            "Sua receita vem de tráfego e não de visita presencial.",
            "Você é fornecedor B2B e seus clientes estão espalhados pelo país.",
            "Sua marca disputa termos genéricos, sem nome de cidade junto.",
        ])
        + """
          <p>E o contrário também vale como sinal: se todo o seu faturamento vem de gente que precisa
          ir até você fisicamente, SEO nacional é dinheiro em visita que não vira cliente. Nesse caso, o
          caminho é a <a href="/consultoria-seo-local/">consultoria de SEO local</a> — ou a
          <a href="/consultoria-seo/">página da sua cidade</a>, se você atende uma região específica.</p>""",
        """<h3>Um teste rápido</h3>
          <p>Pegue os cinco termos que você mais quer ranquear e digite no Google.</p>
          <p>Se aparecerem <strong>mapa e perfis de empresa</strong>, a busca tem intenção local — e a
          disputa passa pelo Google Perfil da Empresa.</p>
          <p>Se aparecerem <strong>artigos, comparativos e páginas de serviço</strong> de sites de todo o
          país, a busca é nacional — e a disputa passa por conteúdo e autoridade.</p>
          <p>Muitos termos misturam os dois. Ler isso corretamente é a primeira coisa feita na análise.</p>""",
        "quando-titulo",
    )

    corpo += sec_texto(
        "Como o projeto é montado",
        "As quatro decisões que definem um projeto nacional",
        problem_cards([
            ("Arquitetura por intenção",
             "Antes de escrever qualquer coisa: mapear o que as pessoas pesquisam em cada estágio — quem "
             "está descobrindo o problema, quem está comparando opções e quem já quer contratar. Cada estágio "
             "pede um tipo de página, e misturá-los é a causa mais comum de site que tem conteúdo e não converte."),
            ("Hierarquia do site",
             "Definir o que é página pilar e o que é conteúdo de apoio, e como eles se linkam. Sem hierarquia, "
             "o site vira uma pilha de textos disputando os mesmos termos entre si — canibalização interna, que "
             "prejudica todas as páginas envolvidas."),
            ("Ritmo de publicação",
             "Um projeto nacional que publica esporadicamente não acompanha quem publica toda semana. O ritmo é "
             "acordado no começo, porque ele define custo e prazo — e mudar de ideia no meio atrasa tudo."),
            ("Construção de autoridade",
             "Em disputa nacional, links são determinantes. A construção começa quando já existe conteúdo que "
             "justifique a menção, segue critério de relevância temática e mantém um ritmo que não destoe do "
             "perfil natural do site. Detalhes em <a href=\"/link-building-para-nichos-competitivos/\">link building</a>."),
        ]),
        "montagem-titulo", classe="problem-section",
    )

    corpo += sec_split(
        "Páginas regionais",
        "Quando criar páginas por cidade — e quando isso vira problema",
        """          <p>É a dúvida mais frequente em projeto nacional, e a resposta depende inteiramente de
          como as pessoas pesquisam o seu serviço.</p>
          <p><strong>Faz sentido</strong> quando existe busca real com nome de cidade e quando cada página
          tem conteúdo próprio — dado local, contexto de mercado, informação que só serve para aquele lugar.
          É exatamente assim que as <a href="/consultoria-seo/">páginas de cidade deste site</a> foram
          construídas: cada uma carrega dados públicos de CNPJ daquele município.</p>
          <p><strong>Vira problema</strong> quando as páginas são o mesmo texto com o nome da cidade trocado.
          Isso não engana mais ninguém: gera conteúdo raso em massa, dilui a força do site e pode fazer as
          páginas competirem entre si. Centenas de páginas fracas valem menos que dez páginas fortes.</p>
          <p>Se a busca do seu nicho <em>não</em> usa nome de cidade — e em muitos mercados digitais não usa —,
          páginas regionais simplesmente não têm demanda para capturar.</p>""",
        """<h3>Critério objetivo</h3>
          <p>Antes de criar uma página regional, três perguntas:</p>
          <ul class="audit-list">
            <li>Existe busca com o nome dessa cidade?</li>
            <li>Eu tenho informação real e específica sobre esse lugar?</li>
            <li>Essa página resolve algo que a página nacional não resolve?</li>
          </ul>
          <p style="margin-top:1rem;">Se qualquer resposta for não, a página não deve existir.</p>""",
        "regionais-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre SEO nacional")

    corpo += relacionados("Conteúdos que ajudam a decidir", [
        ("/blog/seo-local-ou-seo-nacional-diferenca/", "SEO local ou SEO nacional?",
         "O comparativo completo, com exemplos de negócio para cada modelo."),
        ("/seo-para-nichos-competitivos/", "Seu nicho é competitivo?",
         "Como medir a dificuldade real da disputa antes de dimensionar o projeto."),
        ("/blog/quanto-custa-chegar-primeira-pagina/", "Quanto custa chegar à primeira página?",
         "O que forma o custo de um projeto e por que ele varia tanto entre nichos."),
    ])

    corpo += cta_final(
        "Vamos medir a disputa do seu mercado?",
        "Na análise do projeto eu leio a SERP dos seus termos, identifico quem realmente ocupa a primeira "
        "página e devolvo o escopo necessário para entrar nessa disputa — com estimativa de prazo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-mercados-competitivos/", "Ver a divisão completa"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar um projeto de SEO nacional.",
        float_aria="Falar sobre projeto de SEO nacional pelo WhatsApp",
    )


# ============================================================
# A3 — /seo-para-nichos-competitivos/
# ============================================================

def a3_nichos_competitivos():
    slug = "seo-para-nichos-competitivos"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para nichos competitivos | Quando o básico não basta"
    desc = ("Seu SEO parou de evoluir? Entenda por que alguns nichos exigem estratégia técnica, "
            "conteúdo e autoridade em outro nível — e como medir essa dificuldade.")
    page_id = "nichos-competitivos"

    faq = [
        ("Como sei se o meu nicho é competitivo de verdade?",
         "Olhando quem ocupa a primeira página, não o volume de busca. Se os dez resultados são domínios "
         "antigos, com muito conteúdo e perfil de links robusto, o nicho é duro. Se há sites fracos, fóruns "
         "e páginas desatualizadas no meio, existe brecha — mesmo que o volume seja alto."),
        ("Meu SEO travou depois de alguns meses. Isso é normal?",
         "É comum quando o projeto resolveu o que era fácil e chegou no limite do que conteúdo sozinho "
         "alcança. A partir daí, o que costuma faltar é autoridade e profundidade de cobertura — não mais "
         "ajuste de página."),
        ("Vale a pena disputar um termo muito difícil?",
         "Nem sempre. Às vezes o retorno está em dez termos médios que somados trazem mais gente qualificada "
         "que o termo principal. A análise compara esforço estimado contra intenção de compra antes de "
         "recomendar onde concentrar."),
        ("Trocar de estratégia significa jogar fora o que já foi feito?",
         "Raramente. Na maioria dos casos o conteúdo existente é reaproveitado — reorganizado, consolidado "
         "ou aprofundado. Descartar só faz sentido quando o material foi produzido em massa, sem intenção "
         "definida, e está prejudicando o resto do site."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para nichos competitivos", canonical)]),
        schema_service("SEO para nichos competitivos",
                       "Diagnóstico de dificuldade de mercado e estratégia de SEO para nichos de alta "
                       "concorrência, com foco em cobertura de conteúdo, execução técnica e autoridade.",
                       canonical, tipo="SEO para nichos competitivos"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Nichos competitivos", canonical)])

    corpo = hero(
        trilha,
        "Diagnóstico de dificuldade",
        "SEO para nichos competitivos: quando otimizar página deixa de ser o suficiente",
        "Há mercados em que o SEO convencional entrega os primeiros ganhos e depois trava. "
        "Entender por que ele travou é mais útil que contratar mais do mesmo.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#medir", "Como medir a dificuldade"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "O sintoma",
        "O padrão que se repete em quase todo projeto travado",
        problem_cards([
            ("Subiu rápido e parou",
             "Nos primeiros meses tudo melhora: indexação, termos de cauda longa, alguns cliques. Depois "
             "estaciona. Isso normalmente marca o ponto em que o site esgotou o que consegue alcançar sem "
             "autoridade — e não um erro técnico novo."),
            ("Aparece na posição 15, nunca na 5",
             "Estar na segunda página costuma significar relevância reconhecida, mas força insuficiente. "
             "O conteúdo responde à busca; o site ainda não é visto como referência comparável aos que estão acima."),
            ("O concorrente novo passou na frente",
             "Quando um site mais novo ultrapassa, quase sempre há uma explicação de execução: cobertura mais "
             "completa do tema, ritmo maior de publicação ou trabalho de autoridade mais consistente."),
            ("Muito conteúdo, pouco resultado",
             "Volume sem arquitetura gera páginas que disputam entre si. É comum encontrar quinze textos "
             "sobre variações do mesmo assunto, todos medianos, quando dois materiais completos resolveriam melhor."),
        ]),
        "sintoma-titulo", classe="problem-section",
    )

    corpo += sec_split(
        "Diagnóstico",
        "Como medir a dificuldade real de um nicho",
        """          <p>Ferramenta nenhuma decide isso sozinha. Um índice de dificuldade ajuda, mas o que
          determina o esforço é a leitura de quem já está lá. O método usado na análise segue esta ordem:</p>
"""
        + lista([
            "<strong>Quem ocupa as dez primeiras posições</strong> — são marcas do setor, portais, sites de "
            "conteúdo ou agregadores? Cada tipo pede uma resposta diferente.",
            "<strong>Idade e histórico dos domínios</strong> — disputar contra sites com anos de acúmulo é "
            "diferente de disputar contra projetos recentes.",
            "<strong>Profundidade da cobertura</strong> — o que esses sites publicaram sobre o tema além da "
            "página que ranqueia. Muitas vezes eles ganham por cobertura, não por página.",
            "<strong>Perfil de links</strong> — de onde vem a autoridade deles e se esses veículos são "
            "acessíveis para um projeto novo.",
            "<strong>Formato que o Google está premiando</strong> — comparativo, guia, página de serviço, "
            "vídeo. Entregar formato errado custa posição.",
            "<strong>Brechas</strong> — subtemas mal cobertos, conteúdo desatualizado, intenções que ninguém "
            "respondeu direito. É por aqui que projeto novo entra.",
        ])
        + """
          <p>O resultado disso não é uma nota. É uma decisão: <strong>entrar de frente, entrar pelas bordas
          ou não entrar</strong>. Recomendar não disputar um termo também é resposta — e sai mais barato
          que descobrir isso depois de seis meses.</p>""",
        """<h3>Sinais de nicho duro</h3>
          <ul class="audit-list">
            <li>Nenhum resultado da primeira página tem menos de dois anos.</li>
            <li>Todos os concorrentes mantêm blog ativo.</li>
            <li>Há portais grandes ocupando posições.</li>
            <li>Os anúncios do topo são muitos e disputados.</li>
          </ul>
          <h3 style="margin-top:1.25rem;">Sinais de brecha</h3>
          <ul class="audit-list">
            <li>Fóruns e redes sociais ranqueando alto.</li>
            <li>Conteúdo desatualizado nas primeiras posições.</li>
            <li>Resultados que respondem parcialmente à busca.</li>
            <li>Nenhum concorrente cobrindo o subtema por completo.</li>
          </ul>""",
        "medir", classe="solution-section",
    )

    corpo += sec_texto(
        "A resposta",
        "O que muda na execução quando o nicho é duro",
        passos([
            ("Cobertura em vez de página", "Deixar de mirar uma página por termo e passar a cobrir o tema "
                                           "inteiro — pilar, subtemas e dúvidas periféricas — de forma organizada."),
            ("Profundidade real", "Conteúdo que responde a pergunta por completo, com critério de decisão e "
                                  "exemplo, e não texto de tamanho padrão."),
            ("Execução técnica limpa", "Hierarquia, links internos, indexação e desempenho resolvidos — em nicho "
                                       "duro, detalhe técnico vira diferença de posição."),
            ("Autoridade constante", "Construção de menções e links em ritmo sustentado, não em lote. "
                                     "Ver <a href=\"/link-building-para-nichos-competitivos/\">link building</a>."),
            ("Revisão do que já existe", "Consolidar, atualizar ou remover conteúdo antigo que esteja "
                                         "competindo internamente e segurando o resto."),
        ]),
        "resposta-titulo", classe="metodo",
        desc="Não é fazer mais do mesmo. É mudar a unidade de trabalho: de página para tema, "
             "de campanha para ritmo.",
    )

    corpo += sec_split(
        "Expectativa",
        "O que é razoável esperar — e o que não é",
        """          <p>Em nicho competitivo, a curva de resultado raramente é uma linha reta subindo. É comum
          ver meses de aparente estagnação enquanto indexação e autoridade se acumulam, seguidos de
          movimentos mais visíveis.</p>
          <p>Por isso o acompanhamento não olha só posição. Olha <strong>quantas páginas entraram no
          índice</strong>, <strong>quantos termos novos começaram a gerar impressão</strong> e
          <strong>como a posição média se move</strong> — indicadores que se mexem antes do ranking dos
          termos principais e que mostram se o projeto está no caminho.</p>
          <p>O que não é razoável esperar: prazo garantido, posição garantida, ou que um investimento
          abaixo do patamar que o mercado exige produza um resultado proporcionalmente menor. Em disputa
          dura, abaixo de certo nível de execução o resultado tende a ser nenhum, não parcial.</p>""",
        """<h3>Indicadores acompanhados</h3>
          <ul class="audit-list">
            <li>Páginas indexadas e taxa de indexação.</li>
            <li>Termos únicos gerando impressão.</li>
            <li>Posição média por grupo de termos.</li>
            <li>Evolução de domínios de referência.</li>
            <li>Cliques e conversões por página.</li>
          </ul>
          <p style="margin-top:1rem;">Relatório periódico, com o que avançou, o que travou e a decisão do
          próximo ciclo.</p>""",
        "expectativa-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre nichos competitivos")

    corpo += relacionados("Continue por aqui", [
        ("/seo-agressivo/", "SEO agressivo: o que é de fato",
         "A diferença entre execução intensa e prática arriscada — e o que a RCB faz no lugar."),
        ("/blog/como-funciona-projeto-de-seo-para-nichos-competitivos/", "Como funciona um projeto desses",
         "O passo a passo completo de um projeto em mercado disputado."),
        ("/blog/conteudo-ou-backlinks-onde-investir-primeiro/", "Conteúdo ou backlinks primeiro?",
         "A ordem de investimento que evita desperdício nos primeiros meses."),
    ])

    corpo += cta_final(
        "Quer saber onde o seu projeto travou?",
        "Na análise eu leio a SERP dos seus termos, comparo sua cobertura com a dos concorrentes que "
        "estão à frente e aponto se o gargalo é conteúdo, estrutura ou autoridade.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/recuperacao-de-trafego-organico/", "Perdi tráfego que já tinha"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Meu projeto de SEO travou e quero entender o motivo.",
        float_aria="Falar sobre projeto travado em nicho competitivo pelo WhatsApp",
    )


# ============================================================
# A4 — /seo-agressivo/
# ============================================================

def a4_seo_agressivo():
    slug = "seo-agressivo"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO agressivo: o que é, o que funciona e os limites | RCB"
    desc = ("O que o mercado chama de SEO agressivo: execução intensa de conteúdo, arquitetura e "
            "autoridade. Sem spam e sem promessa de primeira página garantida.")
    page_id = "seo-agressivo"

    faq = [
        ("SEO agressivo é a mesma coisa que black hat?",
         "Não. Muita gente usa os termos como sinônimo, mas são coisas diferentes. Agressivo descreve "
         "intensidade de execução: mais conteúdo, mais rápido, com construção de autoridade constante. "
         "Black hat descreve técnicas que violam as diretrizes de busca. Dá para ser muito agressivo sem "
         "usar nenhuma delas."),
        ("A RCB usa PBN ou compra de links em massa?",
         "Não. PBN e compra em massa são explicadas nos conteúdos do site porque os clientes perguntam, "
         "mas não são o que a RCB executa. O risco recai sobre o ativo do cliente, e projeto que depende "
         "disso fica refém de uma atualização de algoritmo."),
        ("Então o que é feito para acelerar de verdade?",
         "Volume e frequência de publicação acima da média do nicho, cobertura completa de tema em vez de "
         "página avulsa, arquitetura interna bem resolvida, correção técnica rápida e construção de "
         "autoridade contínua. É trabalho, não atalho."),
        ("Dá para chegar à primeira página em três meses?",
         "Em termos de baixa e média disputa, às vezes sim. Em termos principais de nicho duro, dificilmente. "
         "O que muda o cenário é o ponto de partida: um domínio com histórico limpo e conteúdo já publicado "
         "encurta caminho; um domínio novo em mercado saturado, não."),
        ("Estratégia agressiva aumenta o risco de penalização?",
         "Depende inteiramente do que se faz. Publicar muito conteúdo bom e conquistar links relevantes não "
         "cria risco. O risco aparece em padrões artificiais — links comprados em massa, texto gerado sem "
         "revisão, esquemas de troca. É exatamente isso que a análise de risco procura evitar."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO agressivo", canonical)]),
        schema_service("SEO agressivo",
                       "Projeto de SEO de alta intensidade: ritmo elevado de produção de conteúdo, execução "
                       "técnica e construção acelerada de autoridade, com avaliação de risco.",
                       canonical, tipo="SEO de alta intensidade"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("SEO agressivo", canonical)])

    corpo = hero(
        trilha,
        "Alta intensidade",
        "SEO agressivo: velocidade não é o mesmo que imprudência",
        "Quem procura por SEO agressivo geralmente quer uma coisa: prazo. A questão é que existem duas "
        "formas muito diferentes de acelerar — e só uma delas não coloca o seu ativo em risco.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#duas-formas", "Ver as duas formas de acelerar"),
        page_id=page_id,
    )

    corpo += sec_split(
        "Definição",
        "O que o mercado chama de \"SEO agressivo\"",
        """          <p>O termo não tem definição técnica. Ele é usado para descrever, ao mesmo tempo, duas
          coisas que não se parecem em nada:</p>
          <p><strong>1. Intensidade de execução.</strong> Publicar muito mais que a média do nicho, cobrir o
          tema inteiro rapidamente, corrigir problemas técnicos sem espera e construir autoridade de forma
          constante. É caro e trabalhoso, mas não viola diretriz nenhuma.</p>
          <p><strong>2. Técnicas de risco.</strong> Redes privadas de sites, compra de links em escala, texto
          gerado em massa sem revisão, manipulação de conteúdo. Pode dar resultado rápido, e pode custar o
          projeto inteiro numa atualização de algoritmo.</p>
          <p>Quando alguém pede "SEO agressivo", quase sempre está pedindo a primeira e sendo oferecida a
          segunda. É por isso que esta página existe: para separar as duas antes de qualquer contrato.</p>""",
        """<h3>Vocabulário sem rodeio</h3>
          <p>Os clientes desta divisão conhecem os termos, então vale explicá-los direito:</p>
          <ul class="audit-list">
            <li><strong>White hat</strong> — dentro das diretrizes de busca.</li>
            <li><strong>Gray hat</strong> — zona ambígua, sem violação clara, mas com risco.</li>
            <li><strong>Black hat</strong> — violação direta das diretrizes.</li>
            <li><strong>PBN</strong> — rede de sites controlados para gerar links próprios.</li>
          </ul>
          <p style="margin-top:1rem;">Explicados em detalhe em
          <a href="/blog/black-hat-gray-hat-white-hat-diferenca/">black, gray e white hat</a> e em
          <a href="/blog/o-que-e-pbn-e-como-funciona/">o que é PBN</a>.</p>""",
        "duas-formas",
    )

    corpo += sec_texto(
        "O que é feito",
        "As alavancas legítimas de aceleração",
        cards([
            (None, "Volume e frequência",
             "Ritmo de publicação acima da média do nicho, sustentado por meses. É a alavanca mais previsível "
             "e a que mais gente subestima, porque exige processo de produção de verdade.", None),
            (None, "Cobertura de tema",
             "Em vez de uma página por termo, o tema inteiro: pilar, subtemas, comparativos e dúvidas "
             "periféricas. Cobertura completa costuma render mais que otimização fina de página isolada.", None),
            (None, "Arquitetura interna",
             "Hierarquia e links internos organizados para concentrar força nas páginas que importam, "
             "em vez de espalhá-la igualmente por tudo.", None),
            (None, "Correção técnica rápida",
             "Indexação, desempenho, canonical, conteúdo duplicado. Em nicho apertado, esses detalhes "
             "decidem posições que o conteúdo sozinho não move.", None),
            (None, "Autoridade contínua",
             "Construção de menções e links em ritmo sustentado, com critério de relevância temática — "
             "não em lote, não de qualquer fonte.", None),
            (None, "Ponto de partida melhor",
             "Quando faz sentido, avaliar um domínio com histórico limpo em vez de começar do zero. "
             "Avaliado caso a caso em <a href=\"/analise-de-dominios-expirados/\">análise de domínios</a>.", None),
        ]),
        "alavancas-titulo",
        desc="Nenhuma delas é atalho. Todas são execução — e é justamente por isso que funcionam de forma "
             "durável e que o custo acompanha o ritmo desejado.",
    )

    corpo += sec_split(
        "Limites",
        "O que a RCB não faz, e por quê",
        """          <p>A recusa aqui não é moral, é de risco de ativo. Quem contrata esta divisão está
          construindo um patrimônio digital que pretende manter por anos. Técnica que entrega posição em
          seis semanas e derruba o domínio no ano seguinte destrói esse patrimônio.</p>
"""
        + lista([
            "<strong>Redes privadas de sites (PBN)</strong> — o padrão é detectável e o histórico de "
            "desvalorização dessas redes é longo.",
            "<strong>Compra de links em massa</strong> — cria perfil artificial e desperdiça verba em "
            "veículos sem relevância real.",
            "<strong>Conteúdo gerado em escala sem revisão</strong> — enche o site de páginas que não "
            "respondem nada e derrubam a percepção de qualidade do domínio inteiro.",
            "<strong>Cloaking e redirecionamento enganoso</strong> — mostrar uma coisa ao buscador e outra "
            "ao visitante.",
            "<strong>Uso de marca de terceiros sem autorização</strong> — problema jurídico, não de SEO.",
            "<strong>Qualquer coisa voltada a contornar bloqueio judicial ou administrativo</strong> — "
            "não é atendido, em nenhuma faixa de investimento.",
        ])
        + """
          <p>Esses assuntos aparecem nos artigos do blog porque os clientes perguntam, e informação boa
          sobre eles é melhor que desinformação. Explicar o que é uma PBN não é o mesmo que montar uma.</p>""",
        """<h3>Análise de risco</h3>
          <p>Todo projeto desta divisão passa por uma leitura de risco que verifica:</p>
          <ul class="audit-list">
            <li>Se o ritmo de aquisição de links destoa do perfil do site.</li>
            <li>Se as fontes têm relevância temática real.</li>
            <li>Se a distribuição de âncoras parece natural.</li>
            <li>Se o histórico do domínio carrega passivo.</li>
            <li>Se o volume de conteúdo mantém qualidade.</li>
          </ul>
          <p style="margin-top:1rem;">É o mesmo critério da
          <a href="/consultoria-de-backlinks/">consultoria de backlinks</a>.</p>""",
        "limites-titulo",
    )

    corpo += sec_split(
        "Prazo",
        "O que realmente encurta o caminho",
        """          <p>Descontando promessa de vendedor, quatro coisas mudam prazo de forma consistente:</p>
          <p><strong>O ponto de partida.</strong> Domínio com histórico limpo e alguma autoridade acumulada
          parte de outro lugar que um domínio registrado ontem. É por isso que
          <a href="/analise-de-dominios-expirados/">a análise de domínios expirados</a> faz parte de vários
          projetos — com a ressalva de que domínio nenhum garante autoridade herdada.</p>
          <p><strong>O alvo escolhido.</strong> Mirar primeiro os termos de disputa média, ganhar tração e
          depois avançar para os principais costuma ser mais rápido que atacar o termo mais difícil de cara.</p>
          <p><strong>O ritmo real.</strong> Não o ritmo contratado: o executado. Projeto que atrasa aprovação
          de conteúdo atrasa resultado na mesma proporção.</p>
          <p><strong>A consistência.</strong> Seis meses de execução constante rendem mais que dois meses
          intensos seguidos de quatro parados.</p>
          <p>O que <em>não</em> encurta: pagar mais por técnicas de risco. Isso muda a variância, não a média —
          aumenta a chance de resultado rápido e também a de perder tudo.</p>""",
        """<h3>Estimativa, não garantia</h3>
          <p>Na análise do projeto você recebe cenários de prazo por grupo de termos, com as premissas
          explícitas: ritmo assumido, ponto de partida e força dos concorrentes.</p>
          <p>Se qualquer premissa mudar durante a execução, o cenário muda junto — e isso é comunicado no
          relatório, não escondido até o fim do contrato.</p>
          <p style="margin-top:1rem;">Leia também:
          <a href="/blog/e-possivel-garantir-primeira-pagina/">é possível garantir primeira página?</a></p>""",
        "prazo-agressivo-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre estratégia agressiva")

    corpo += relacionados("Continue por aqui", [
        ("/blog/o-que-e-seo-agressivo/", "O que é SEO agressivo",
         "O artigo completo, com o que muda na prática entre intensidade e risco."),
        ("/blog/o-que-e-black-hat-seo/", "O que é black hat SEO",
         "As técnicas, por que ainda circulam e o que costuma acontecer depois."),
        ("/blog/pbn-ainda-funciona-para-seo/", "PBN ainda funciona?",
         "O que mudou, o que sobrou e por que o risco recai sobre quem contrata."),
    ])

    corpo += cta_final(
        "Quer acelerar sem colocar o projeto em risco?",
        "Na análise eu digo o que dá para acelerar no seu caso, quanto isso custa e qual cenário de prazo "
        "é realista — incluindo quando a resposta honesta é que o alvo escolhido não vale o esforço.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-nichos-competitivos/", "Medir a dificuldade do meu nicho"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero acelerar um projeto de SEO e entender o que é seguro fazer.",
        float_aria="Falar sobre estratégia agressiva de SEO pelo WhatsApp",
    )


# ============================================================
# A5 — /seo-para-negocios-digitais/
# ============================================================

def a5_negocios_digitais():
    slug = "seo-para-negocios-digitais"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para negócios digitais e plataformas | RCB Consultoria"
    desc = ("SEO para produtos digitais, plataformas e negócios por assinatura: aquisição orgânica, "
            "arquitetura de conteúdo e autoridade para operações nacionais.")
    page_id = "negocios-digitais"

    faq = [
        ("Meu produto é novo e ninguém pesquisa por ele. SEO serve?",
         "Serve, mas não pelo nome do produto. Quando a categoria ainda não é conhecida, a busca existe na "
         "forma do problema que o produto resolve. O trabalho começa por essas buscas e só depois migra para "
         "os termos de categoria e de marca."),
        ("SEO faz sentido para negócio por assinatura?",
         "Faz, e por um motivo específico: o custo de aquisição pago se repete a cada novo cliente, enquanto "
         "uma página que ranqueia continua trazendo gente sem custo marginal. Em modelo recorrente, isso "
         "muda a economia do canal ao longo do tempo."),
        ("Preciso de blog ou só de páginas de produto?",
         "Depende do ciclo de decisão. Produto simples e barato converte com páginas de produto e comparativos. "
         "Produto que exige entendimento antes da compra precisa de conteúdo que eduque — senão você só captura "
         "quem já sabia o que queria."),
        ("Como isso se integra com tráfego pago?",
         "Bem, quando os dois são planejados juntos. O pago mostra rapidamente quais termos convertem e qual "
         "mensagem funciona; o orgânico assume os termos de maior volume e menor custo ao longo do tempo. "
         "O erro comum é tratá-los como canais isolados, com metas separadas."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para negócios digitais", canonical)]),
        schema_service("SEO para negócios digitais",
                       "Aquisição orgânica para produtos digitais, plataformas, aplicativos e negócios por "
                       "assinatura com operação nacional.",
                       canonical, tipo="SEO para negócios digitais"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Negócios digitais", canonical)])

    corpo = hero(
        trilha,
        "Produto digital · plataforma · assinatura",
        "SEO para negócios digitais: aquisição que não para quando a verba de anúncio para",
        "Operações digitais nascem dependentes de mídia paga. O orgânico é o que reduz essa dependência — "
        "mas exige ser tratado como projeto, e não como blog no canto do site.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#modelos", "Ver os modelos atendidos"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "Quem é atendido",
        "Modelos de negócio deste cluster",
        cards([
            (None, "Produtos digitais",
             "Cursos, ferramentas, aplicativos e produtos vendidos inteiramente online, sem limite geográfico.", None),
            (None, "Plataformas e marketplaces",
             "Operações de duas pontas, onde o orgânico precisa atender oferta e demanda com conteúdos diferentes.", None),
            (None, "Negócios por assinatura",
             "Receita recorrente, em que o custo de aquisição pago pesa mês a mês e o orgânico muda a conta.", None),
            (None, "Serviços online nacionais",
             "Prestadores que atendem o Brasil inteiro a distância e disputam termos sem recorte de cidade.", None),
            (None, "Projetos em construção",
             "Operações que ainda não existem: marca, domínio, site e posicionamento montados juntos.", None),
            (None, "Operações estrangeiras",
             "Empresas de fora estruturando presença em português para o mercado brasileiro.", None),
        ]),
        "modelos", classe="cluster-section",
        desc="O que une esses modelos é depender de tráfego qualificado sem recorte geográfico — "
             "e ter concorrentes que já entenderam isso.",
    )

    corpo += sec_split(
        "O problema de fundo",
        "Dependência de mídia paga é um risco de modelo, não só um custo",
        """          <p>Operação digital que cresce só com anúncio tem uma fragilidade estrutural: o
          faturamento é proporcional à verba. Reduziu a verba, caiu a receita, no mesmo mês. E o custo
          por aquisição tende a subir conforme mais concorrentes disputam o mesmo leilão.</p>
          <p>O orgânico funciona de forma diferente. É mais lento para construir e não liga como uma
          chave, mas <strong>uma página que ranqueia continua trazendo visitante sem custo por clique</strong>.
          Em negócio recorrente, essa diferença se acumula.</p>
          <p>Isso não é argumento para trocar um pelo outro. É argumento para não depender de um só. Quem
          tem os dois canais funcionando decide onde investir por eficiência, e não por necessidade.</p>""",
        """<h3>Onde o orgânico entra melhor</h3>
          <ul class="audit-list">
            <li>Termos de <strong>problema</strong>, que o pago costuma ignorar por baixa conversão imediata.</li>
            <li>Termos de <strong>comparação</strong>, onde o usuário está decidindo entre opções.</li>
            <li>Termos de <strong>categoria</strong>, com volume alto e custo por clique elevado.</li>
            <li>Dúvidas de <strong>pós-compra</strong>, que sustentam retenção e reduzem cancelamento.</li>
          </ul>""",
        "dependencia-titulo",
    )

    corpo += sec_texto(
        "Estrutura",
        "Como o conteúdo é organizado por estágio de decisão",
        tabela(
            ["Estágio", "O que a pessoa busca", "Tipo de página", "O que ela faz depois"],
            [
                ["Descoberta", "o problema, sem saber que existe solução", "conteúdo explicativo", "conhece a categoria"],
                ["Consideração", "compara caminhos e alternativas", "comparativo, guia de escolha", "entende critérios"],
                ["Decisão", "compara fornecedores e preço", "página de produto, comparativo direto", "testa ou compra"],
                ["Marca", "procura você pelo nome", "página institucional, avaliações", "converte"],
                ["Uso", "dúvidas de quem já é cliente", "conteúdo de suporte", "permanece assinante"],
            ],
            nota="O último estágio é o mais esquecido — e é o que sustenta receita recorrente.",
        ),
        "estagios-titulo",
        desc="A maior parte dos projetos de conteúdo em negócio digital falha por concentrar tudo em um "
             "estágio: ou só conteúdo de topo, que traz visita sem intenção, ou só página de produto, "
             "que só captura quem já decidiu.",
    )

    corpo += sec_split(
        "Execução técnica",
        "O que costuma travar site de produto digital",
        """          <p>Sites de operação digital têm um conjunto de problemas técnicos bem característico,
          diferente do que se vê em site institucional:</p>
"""
        + lista([
            "<strong>Conteúdo dependente de JavaScript</strong> que o buscador não enxerga como o visitante enxerga.",
            "<strong>Páginas geradas dinamicamente</strong> em quantidade, sem controle de indexação — filtros e "
            "parâmetros criando milhares de URLs quase iguais.",
            "<strong>Área logada e área pública misturadas</strong>, com conteúdo relevante preso atrás de login.",
            "<strong>Desempenho ruim</strong> em páginas pesadas de aplicação, que penaliza justamente as páginas de conversão.",
            "<strong>Ausência de estrutura de conteúdo</strong> — o site foi construído como produto, não como ativo de busca, "
            "e não há onde publicar sem improviso.",
            "<strong>Migrações de plataforma</strong> feitas sem plano de redirecionamento, que apagam histórico acumulado. "
            "Ver <a href=\"/migracao-de-dominio-seo/\">migração de domínio e SEO</a>.",
        ])
        + """
          <p>Resolver isso normalmente exige conversar com quem desenvolve o produto, e não só com quem
          cuida do marketing. Quando o site é construído do zero pela RCB, essas decisões já entram na
          arquitetura desde o começo.</p>""",
        """<h3>Entregáveis técnicos</h3>
          <ul class="audit-list">
            <li>Auditoria de renderização e indexação.</li>
            <li>Regras de indexação para páginas dinâmicas.</li>
            <li>Estrutura de conteúdo escalável.</li>
            <li>Plano de desempenho das páginas de conversão.</li>
            <li>Dados estruturados adequados ao tipo de produto.</li>
            <li>Plano de migração, quando houver troca de plataforma.</li>
          </ul>""",
        "tecnico-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre negócios digitais")

    corpo += relacionados("Segmentos com página própria", [
        ("/seo-para-streaming-e-tv-online/", "Streaming e TV online",
         "Plataformas de conteúdo por assinatura: catálogo, lançamento e retenção."),
        ("/seo-para-jogos-online/", "Jogos online",
         "Portais, plataformas e apps de jogos, com conteúdo de comunidade e ciclo de lançamento."),
        ("/seo-para-igaming/", "iGaming (B2B)",
         "Provedores e plataformas que vendem para operadores e entram no mercado brasileiro."),
    ])

    corpo += cta_final(
        "Quer reduzir a dependência de anúncio?",
        "Na análise do projeto eu mapeio quais buscas do seu mercado o orgânico pode assumir, o que o seu "
        "site atual suporta e o que precisa ser reconstruído — com escopo, prazo estimado e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-nacional/", "Entender a disputa nacional"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Tenho um negócio digital e quero avaliar um projeto de SEO.",
        float_aria="Falar sobre SEO para negócio digital pelo WhatsApp",
    )


PAGINAS = [a1_mercados_competitivos, a2_seo_nacional, a3_nichos_competitivos,
           a4_seo_agressivo, a5_negocios_digitais]
