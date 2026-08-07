# -*- coding: utf-8 -*-
"""
Cluster B — IPTV, streaming e TV online.

B1 /seo-para-iptv/                    (pilar do cluster)
B2 /criacao-de-site-para-iptv/
B3 /seo-para-revendedor-iptv/
B4 /link-building-para-iptv/
B5 /dominio-expirado-para-iptv/
B6 /seo-para-streaming-e-tv-online/

POLÍTICA DO CLUSTER (docs/seo-mercados-competitivos-plan.md §2.5)
A busca por "IPTV" no Brasil mistura operação licenciada de streaming com
distribuição irregular de conteúdo protegido. Toda página deste cluster carrega
um critério de atendimento explícito: a RCB atende operações com direito ou
autorização sobre o conteúdo que distribuem, verificado antes de qualquer proposta.

A página /migracao-de-dominio-para-iptv/ NÃO existe de propósito — o recorte
"IPTV + trocar domínio" atrai demanda de evasão de bloqueio judicial, que não é
atendida. A necessidade legítima é coberta por /migracao-de-dominio-seo/.
"""
from rcb_base import (
    BASE_URL, head_comum, montar, breadcrumb_html, hero, sec_texto, sec_split,
    cards, problem_cards, passos, lista, tabela, sec_faq, cta_final,
    relacionados, grafo, schema_webpage, schema_breadcrumb, schema_service,
    schema_faq,
)

HOJE = "2026-08-06"
ANALISE = "/analise-de-projeto/"


# Bloco de critério de atendimento — o texto varia por página para não virar
# aviso repetido, mas a regra comunicada é sempre a mesma.
def criterio_card(variacao):
    textos = {
        "pilar": """<h3>Critério de atendimento</h3>
          <p>Este cluster atende <strong>operadores, plataformas e distribuidores que possuem direito ou
          autorização sobre o conteúdo que distribuem</strong> — serviços licenciados de streaming, TV por
          internet e distribuição autorizada.</p>
          <p>A análise do projeto verifica isso antes de qualquer proposta. Operações que dependam de
          distribuir conteúdo protegido sem autorização, usar marca de terceiros ou contornar bloqueio
          judicial ou administrativo não são atendidas, em nenhuma faixa de investimento.</p>""",
        "site": """<h3>Antes de começar</h3>
          <p>O desenvolvimento só começa depois que a análise do projeto confirma a base da operação:
          <strong>o que é distribuído e com qual autorização</strong>.</p>
          <p>É uma verificação rápida, mas inegociável — inclusive porque um projeto construído sobre base
          instável não sustenta investimento de longo prazo em SEO.</p>""",
        "revendedor": """<h3>Quem é atendido</h3>
          <p>Revendedores e distribuidores <strong>autorizados</strong>, que operam com contrato ou
          autorização do fornecedor do serviço que revendem.</p>
          <p>Essa condição é verificada na análise do projeto. Não é burocracia: é o que separa um ativo
          digital que vale a pena construir de um que pode desaparecer.</p>""",
        "curto": """<h3>Critério de atendimento</h3>
          <p>Atendemos operações com direito ou autorização sobre o conteúdo distribuído — verificado na
          análise do projeto, antes de qualquer proposta.</p>""",
    }
    return textos[variacao]


# ============================================================
# B1 — /seo-para-iptv/   (pilar do cluster)
# ============================================================

def b1_seo_para_iptv():
    slug = "seo-para-iptv"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para IPTV: projeto completo e disputa nacional | RCB"
    desc = ("Projeto de SEO para IPTV do zero: marca, site, conteúdo, autoridade e acompanhamento. "
            "Para operações com direito sobre o conteúdo distribuído.")
    page_id = "seo-iptv"

    faq = [
        ("Quanto custa um projeto de SEO para IPTV?",
         "Não existe valor de tabela, porque o esforço varia demais. O que define a faixa é o ponto de "
         "partida (do zero ou site existente), o ritmo de conteúdo acordado, a intensidade de construção "
         "de autoridade e o prazo desejado. A análise do projeto devolve escopo e faixa de investimento "
         "para o seu caso específico."),
        ("Em quanto tempo o site chega à primeira página?",
         "Depende do termo. Buscas específicas e de cauda longa costumam responder antes; os termos "
         "principais do nicho levam mais tempo e dependem de conteúdo acumulado e autoridade construída. "
         "Nenhum prazo é garantido — o que a análise entrega são cenários com as premissas explícitas."),
        ("A RCB cria a marca e o site, ou só faz o SEO?",
         "Faz os dois. A maior parte dos projetos deste cluster começa sem nada no ar: nome, domínio, "
         "identidade visual, site e estrutura de conteúdo são construídos junto com a estratégia de "
         "posicionamento. Quando já existe site, o projeto começa por uma auditoria do que aproveitar."),
        ("O domínio fica no meu nome?",
         "Sim. Domínio, hospedagem e contas de análise são registrados em nome do cliente, com acesso "
         "completo. Você é dono do ativo desde o primeiro dia — inclusive se decidir encerrar o projeto."),
        ("Vale a pena usar um domínio expirado nesse nicho?",
         "Às vezes. Um domínio com histórico limpo e relevância temática pode encurtar caminho, mas domínio "
         "nenhum garante autoridade herdada, e histórico ruim atrapalha mais do que ajuda. Por isso a "
         "avaliação vem antes da compra — veja domínio expirado para IPTV."),
        ("Backlinks estão incluídos no projeto?",
         "A construção de autoridade faz parte do escopo quando contratada, com plano, critério de "
         "relevância e ritmo definidos. O que não existe é pacote de quantidade fixa ou promessa de "
         "backlinks ilimitados — isso não é como autoridade funciona."),
        ("Que tipo de operação a RCB não atende neste nicho?",
         "Operações sem direito ou autorização sobre o conteúdo que distribuem, uso de marca de terceiros "
         "sem permissão e qualquer demanda voltada a contornar bloqueio judicial ou administrativo. "
         "Isso é verificado na análise do projeto."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para IPTV", canonical)]),
        schema_service("SEO para IPTV",
                       "Projeto completo de SEO para operações licenciadas de IPTV e TV por internet: "
                       "criação de marca e site, arquitetura de conteúdo, construção de autoridade e "
                       "acompanhamento, com disputa nacional.",
                       canonical, tipo="SEO para IPTV e streaming"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("SEO para IPTV", canonical)])

    painel = """<h2>Projeto ponta a ponta</h2>
          <ul class="audit-list">
            <li>Marca, domínio e identidade</li>
            <li>Site com estrutura de conversão</li>
            <li>Páginas comerciais e de planos</li>
            <li>Blog e arquitetura de conteúdo</li>
            <li>SEO técnico e indexação</li>
            <li>Construção de autoridade</li>
            <li>Acompanhamento e relatórios</li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:.75rem;">Escopo definido caso a caso na análise do projeto.</p>"""

    corpo = hero(
        trilha,
        "Cluster IPTV e streaming",
        "SEO para IPTV: projeto completo, do domínio à primeira página",
        "Disputa nacional em um mercado que não perdoa improviso. Marca, site, conteúdo e autoridade "
        "construídos como um projeto só — para operações licenciadas de TV por internet.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#processo", "Ver como o projeto funciona"),
        painel, page_id,
    )

    corpo += sec_split(
        "Antes de tudo",
        "Quem a RCB atende neste mercado",
        """          <p>Vale começar pelo filtro, porque ele economiza tempo dos dois lados.</p>
          <p>O termo "IPTV" cobre coisas muito diferentes no Brasil. De um lado, operações licenciadas de
          TV por internet, distribuidores autorizados e plataformas com contrato sobre o que transmitem.
          De outro, distribuição de conteúdo protegido sem qualquer direito sobre ele.</p>
          <p><strong>A RCB trabalha com o primeiro grupo.</strong> A verificação acontece na análise do
          projeto, antes de proposta, e é objetiva: o que é distribuído e com qual autorização.</p>
          <p>Há uma razão prática além da jurídica. Um projeto de SEO sério é investimento de meses,
          construindo um ativo que deve valer mais a cada trimestre. Base instável destrói esse ativo —
          e nenhum trabalho de posicionamento compensa isso.</p>""",
        criterio_card("pilar"),
        "criterio-titulo",
    )

    corpo += sec_texto(
        "O cenário",
        "Por que esse nicho é caro de disputar",
        problem_cards([
            ("Concorrência estabelecida",
             "Quem ocupa a primeira página está lá há tempo, com domínio maduro e volume de conteúdo "
             "acumulado. Entrar nessa disputa exige construir algo comparável, não apenas otimizar."),
            ("Poucos veículos dispostos a linkar",
             "É um tema que muitos sites evitam. Isso torna a construção de autoridade mais lenta e mais cara "
             "que em nichos neutros — e é o principal fator de prazo do projeto."),
            ("Busca nacional, sem filtro geográfico",
             "Não há mapa nem proximidade para ajudar. Você compete com todos os sites do Brasil ao mesmo "
             "tempo, e o que decide é cobertura de conteúdo, estrutura técnica e autoridade."),
            ("Projeto normalmente começa do zero",
             "Sem marca, sem domínio, sem site. O que significa que a fase de construção é parte do projeto "
             "de SEO, e não algo que acontece antes dele."),
        ]),
        "cenario-titulo", classe="problem-section",
    )

    corpo += sec_texto(
        "Como o projeto funciona",
        "Do domínio ao acompanhamento",
        passos([
            ("Análise e estratégia", "Leitura da concorrência real, mapeamento de buscas por intenção e "
                                     "definição de alvo. Sai daqui o escopo, o cenário de prazo e a faixa de investimento."),
            ("Marca e domínio", "Nome, identidade e escolha de domínio. Quando faz sentido, avaliação de "
                                "domínio com histórico — sempre com análise de risco antes da compra."),
            ("Site e conversão", "Construção do site com estrutura de planos, contato por WhatsApp e páginas "
                                 "comerciais. Detalhes em criação de site para IPTV."),
            ("Conteúdo em ritmo", "Publicação contínua, priorizada por intenção comercial: páginas de serviço, "
                                  "conteúdo de decisão e material informacional."),
            ("Autoridade", "Construção de menções e links com critério de relevância, iniciada quando já existe "
                           "conteúdo que justifique a referência."),
            ("Medição e ajuste", "Relatório periódico de indexação, impressão, posição e contatos gerados — "
                                 "com decisão de rota a cada ciclo."),
        ]),
        "processo", classe="metodo",
        desc="Seis fases que se sobrepõem: conteúdo não espera o site ficar perfeito, e autoridade não "
             "espera o conteúdo acabar.",
    )

    corpo += sec_split(
        "Estratégia de conteúdo",
        "O que é publicado, e por que nessa ordem",
        """          <p>A arquitetura de conteúdo separa três tipos de busca, e cada um recebe um tipo de página:</p>
          <p><strong>Quem já quer contratar</strong> — busca por serviço, plano, preço, forma de contratação.
          Recebe páginas comerciais objetivas, com planos claros e contato direto. É o conteúdo que converte,
          e o primeiro a ser construído.</p>
          <p><strong>Quem está comparando</strong> — busca por comparativos, diferenças entre opções, o que
          observar antes de contratar. Recebe conteúdo de decisão, que qualifica e encaminha para as páginas
          comerciais.</p>
          <p><strong>Quem está aprendendo</strong> — busca por como funciona, requisitos, compatibilidade de
          dispositivo, resolução de problema. Recebe conteúdo informacional. Traz volume, constrói relevância
          temática e sustenta o trabalho de autoridade.</p>
          <p>A ordem importa: começar pelo informacional gera visita sem intenção; começar só pelo comercial
          deixa o site sem cobertura para sustentar posição. Os três avançam juntos, com peso diferente ao
          longo do projeto.</p>""",
        """<h3>Tipos de página do projeto</h3>
          <ul class="audit-list">
            <li>Página inicial com proposta clara</li>
            <li>Páginas de planos e condições</li>
            <li>Página de compatibilidade e dispositivos</li>
            <li>Páginas de dúvida pré-contratação</li>
            <li>Conteúdo de suporte e configuração</li>
            <li>Blog com cobertura do tema</li>
            <li>Páginas de contato e atendimento</li>
          </ul>""",
        "conteudo-titulo",
    )

    corpo += sec_split(
        "Disputa nacional",
        "O que muda quando o alvo é o Brasil inteiro",
        """          <p>Praticamente todo projeto deste nicho é nacional por natureza: o serviço é entregue pela
          internet e o cliente pode estar em qualquer lugar. Isso tem três consequências práticas.</p>
          <p><strong>O Google Perfil da Empresa deixa de ser alavanca.</strong> Não há mapa para aparecer,
          nem proximidade para favorecer você. Todo o peso vai para conteúdo, estrutura e autoridade — as
          três coisas que levam mais tempo.</p>
          <p><strong>A concorrência é máxima em todo termo.</strong> Não existe versão "menos disputada" do
          termo por estar em uma cidade menor. Cada busca coloca você contra todos os concorrentes do país
          simultaneamente.</p>
          <p><strong>A cauda longa carrega o começo.</strong> Os primeiros meses vivem de buscas específicas —
          dúvidas técnicas, compatibilidade, comparações — enquanto os termos principais amadurecem. Um
          projeto avaliado só pelo termo principal parece parado quando na verdade está construindo base.</p>
          <p>A mecânica geral dessa disputa está detalhada em <a href="/seo-nacional/">SEO nacional</a>.</p>""",
        """<h3>O que é medido</h3>
          <ul class="audit-list">
            <li>Páginas indexadas ao longo do tempo</li>
            <li>Termos únicos gerando impressão</li>
            <li>Posição média por grupo de termos</li>
            <li>Evolução de domínios de referência</li>
            <li>Contatos gerados por página</li>
          </ul>
          <p style="margin-top:1rem;">Os três primeiros se movem antes do ranking dos termos principais —
          por isso são eles que mostram se o projeto está no caminho.</p>""",
        "nacional-titulo",
    )

    corpo += sec_texto(
        "Investimento e prazo",
        "O que forma o custo — e o que é honesto dizer sobre tempo",
        tabela(
            ["Fator", "Reduz custo e prazo", "Aumenta custo e prazo"],
            [
                ["Ponto de partida", "site e conteúdo já existentes", "marca, domínio e site do zero"],
                ["Domínio", "histórico limpo e relevante", "domínio novo, sem histórico"],
                ["Alvo", "termos de disputa média primeiro", "termo principal do nicho de cara"],
                ["Ritmo de conteúdo", "constante e aprovado sem atraso", "publicação irregular"],
                ["Autoridade", "construção contínua desde cedo", "início tardio ou intermitente"],
                ["Prazo desejado", "horizonte de trimestres", "expectativa de semanas"],
            ],
            nota="Fatores de esforço, não tabela de preço. A faixa de cada projeto sai da análise.",
        ),
        "investimento-titulo",
        desc="Nenhum prazo é garantido, aqui ou em qualquer fornecedor sério: ninguém controla o algoritmo "
             "do Google. O que a análise entrega são cenários com as premissas escritas — e o "
             "acompanhamento diz, a cada ciclo, se a realidade está confirmando ou desmentindo o cenário.",
    )

    corpo += sec_split(
        "Riscos e limites",
        "O que pode dar errado, dito antes e não depois",
        """          <p>Todo projeto tem risco. Os deste nicho são conhecidos, e vale explicitá-los:</p>
"""
        + lista([
            "<strong>Construção de autoridade mais lenta que a média</strong> — menos veículos aceitam o tema, "
            "o que estica o prazo. É o risco mais provável de se materializar.",
            "<strong>Domínio com passivo</strong> — histórico ruim herdado em compra mal avaliada. Mitigado "
            "por <a href=\"/analise-de-dominios-expirados/\">análise antes da compra</a>, nunca depois.",
            "<strong>Volatilidade de algoritmo</strong> — atualizações mexem em nichos inteiros. Nenhum "
            "fornecedor evita isso; o que dá para fazer é não depender de técnica frágil.",
            "<strong>Dependência de um único termo</strong> — projeto que aposta tudo em uma busca fica "
            "refém dela. A arquitetura distribui o risco por vários grupos de termos.",
            "<strong>Execução interrompida</strong> — parar a publicação no meio costuma custar mais que "
            "nunca ter começado, porque concorrente continua avançando.",
        ])
        + """
          <p>Nada disso é motivo para não fazer. É motivo para dimensionar corretamente e acompanhar de perto.</p>""",
        criterio_card("curto"),
        "riscos-titulo",
    )

    corpo += sec_texto(
        "Frentes do cluster",
        "Serviços que compõem ou complementam o projeto",
        cards([
            ("/criacao-de-site-para-iptv/", "Criação de site para IPTV",
             "O desenvolvimento em si: marca, layout, planos, WhatsApp, velocidade e dispositivos.",
             "Ver criação de site"),
            ("/seo-para-revendedor-iptv/", "SEO para revendedor",
             "Para quem revende de forma autorizada e ainda depende só de rede social.",
             "Ver SEO para revendedor"),
            ("/link-building-para-iptv/", "Link building para IPTV",
             "Construção de autoridade no nicho, com critério de relevância e avaliação de risco.",
             "Ver link building"),
            ("/dominio-expirado-para-iptv/", "Domínio expirado para IPTV",
             "O que o histórico entrega de verdade, o que é mito e como avaliar antes de comprar.",
             "Ver domínio expirado"),
            ("/seo-para-streaming-e-tv-online/", "Streaming e TV online",
             "Plataformas de conteúdo por assinatura: catálogo, lançamento e retenção.",
             "Ver streaming e TV online"),
            ("/migracao-de-dominio-seo/", "Migração de domínio",
             "Rebrand, troca de endereço ou consolidação de sites com processo técnico controlado.",
             "Ver migração de domínio"),
        ]),
        "frentes-titulo", classe="cluster-section",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre SEO para IPTV")

    corpo += relacionados("Conteúdos que respondem as dúvidas mais comuns", [
        ("/blog/quanto-custa-seo-para-iptv/", "Quanto custa SEO para IPTV?",
         "O que forma o custo de um projeto no nicho e por que a variação é tão grande."),
        ("/blog/quanto-tempo-posicionar-site-iptv/", "Quanto tempo demora para posicionar?",
         "Os fatores que realmente mexem no prazo, sem promessa de calendário."),
        ("/blog/dominio-novo-ou-expirado-para-iptv/", "Domínio novo ou expirado?",
         "A comparação honesta entre começar do zero e comprar histórico."),
        ("/blog/iptv-primeira-pagina-3-4-meses/", "Dá para chegar em 3 ou 4 meses?",
         "Um modelo de faixas para saber quais termos são viáveis nesse prazo e quais não são."),
        ("/blog/seo-nacional-para-iptv-o-que-muda/", "O que muda na disputa nacional",
         "Sem mapa e sem proximidade: o que sobra, e por que o prazo é maior."),
        ("/blog/backlinks-para-iptv-funcionam/", "Backlinks funcionam neste nicho?",
         "Quais tipos de veículo rendem de verdade e onde a verba costuma ser desperdiçada."),
    ])

    corpo += cta_final(
        "Vamos dimensionar o seu projeto?",
        "Na análise você descreve a operação e o objetivo; eu devolvo a leitura da concorrência, o escopo "
        "necessário, o cenário de prazo e a faixa de investimento. A verificação do critério de atendimento "
        "faz parte dessa etapa.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/criacao-de-site-para-iptv/", "Preciso do site primeiro"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero solicitar a análise de um projeto de SEO para IPTV.",
        float_aria="Solicitar análise de projeto de IPTV pelo WhatsApp",
    )


# ============================================================
# B2 — /criacao-de-site-para-iptv/
# ============================================================

def b2_criacao_site_iptv():
    slug = "criacao-de-site-para-iptv"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Criação de site para IPTV: estrutura e conversão | RCB"
    desc = ("Site para IPTV construído do zero: marca, planos, WhatsApp, velocidade e estrutura "
            "preparada para SEO e crescimento desde a primeira página.")
    page_id = "criacao-site-iptv"

    faq = [
        ("O site já vem preparado para SEO?",
         "Sim, e essa é a diferença principal em relação a um site feito só visualmente. Hierarquia de "
         "páginas, endereços limpos, títulos e descrições próprios, dados estruturados, desempenho e "
         "estrutura para crescer em conteúdo entram na construção — não são corrigidos depois."),
        ("Quanto tempo leva para o site ficar pronto?",
         "Depende do escopo: um site de planos com poucas páginas sai mais rápido que uma estrutura com "
         "blog, área de suporte e várias páginas comerciais. O prazo é fechado na análise do projeto, "
         "junto com o escopo."),
        ("Domínio e hospedagem estão incluídos?",
         "A escolha e a configuração fazem parte do trabalho. O custo dos serviços em si é do cliente, e "
         "tudo é registrado em nome dele — domínio, hospedagem e contas de análise, com acesso completo."),
        ("O site funciona bem no celular?",
         "É construído a partir do celular, não adaptado depois. A maior parte do acesso neste nicho vem de "
         "dispositivo móvel, incluindo a conversa pelo WhatsApp — então o layout é pensado para essa tela primeiro."),
        ("Posso atualizar o conteúdo sozinho depois?",
         "Sim. A estrutura é entregue com orientação de como publicar e atualizar. Quando o projeto inclui "
         "conteúdo contínuo, a publicação pode seguir com a RCB — mas o cliente nunca fica preso."),
        ("E se eu já tiver um site?",
         "Aí o começo é uma auditoria: o que dá para aproveitar, o que precisa ser refeito e se vale "
         "reconstruir ou corrigir. Reconstruir nem sempre é a resposta, e trocar de endereço exige plano "
         "próprio — veja migração de domínio e SEO."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para IPTV", f"{BASE_URL}/seo-para-iptv/"),
                           ("Criação de site para IPTV", canonical)]),
        schema_service("Criação de site para IPTV",
                       "Desenvolvimento de site para operações licenciadas de IPTV: marca, identidade "
                       "visual, páginas de planos, integração com WhatsApp, desempenho e estrutura "
                       "preparada para SEO desde a construção.",
                       canonical, tipo="Criação de site"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para IPTV", "/seo-para-iptv/"),
                              ("Criação de site", canonical)])

    corpo = hero(
        trilha,
        "Desenvolvimento",
        "Criação de site para IPTV: construído para converter e para crescer",
        "Um site que existe só para ter link na bio não sustenta um projeto. Aqui a estrutura já nasce "
        "preparada para receber conteúdo, aparecer na busca e transformar visita em conversa.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/seo-para-iptv/", "Ver a estratégia de posicionamento"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O ponto de partida",
        "Site bonito e site que funciona não são a mesma coisa",
        """          <p>A maioria dos sites deste nicho tem o mesmo problema: foram feitos como cartão de visitas.
          Uma página só, com uma tabela de planos e um botão de WhatsApp. Funciona para quem já conhece a
          marca e não serve para mais nada.</p>
          <p>O problema não é estético. É estrutural: <strong>não existe onde o conteúdo entrar</strong>.
          Sem páginas por assunto, sem hierarquia e sem lugar para publicar, o site não tem como disputar
          busca nenhuma — e qualquer investimento posterior em SEO começa refazendo a base.</p>
          <p>Construir já pensando nisso custa praticamente o mesmo e evita refazer tudo seis meses depois.</p>""",
        criterio_card("site"),
        "ponto-partida-titulo",
    )

    corpo += sec_texto(
        "O que é entregue",
        "Da marca à manutenção",
        cards([
            (None, "Marca e identidade",
             "Nome, logotipo, paleta e aplicação básica — quando o projeto começa sem marca definida. "
             "O suficiente para o negócio ter cara própria, sem virar projeto de branding de meses.", None),
            (None, "Estrutura de páginas",
             "Página inicial, planos, dúvidas, compatibilidade, suporte e contato. Cada uma com endereço "
             "próprio, para poder disputar a busca correspondente.", None),
            (None, "Planos e condições",
             "Apresentação clara do que está incluído em cada opção, com comparação lado a lado — a "
             "informação que o visitante procura antes de chamar no WhatsApp.", None),
            (None, "Conversão por WhatsApp",
             "Contato direto, com mensagem pré-preenchida por origem, para você saber de qual página veio "
             "cada conversa. Rastreamento configurado desde o início.", None),
            (None, "Desempenho e dispositivos",
             "Carregamento rápido e layout construído a partir da tela do celular, que é de onde vem a "
             "maior parte do acesso do nicho.", None),
            (None, "SEO desde a construção",
             "Hierarquia, endereços limpos, títulos próprios, dados estruturados e espaço preparado para "
             "conteúdo crescer sem reforma.", None),
        ]),
        "entrega-titulo",
    )

    corpo += sec_split(
        "Conversão",
        "O que faz o visitante chamar no WhatsApp",
        """          <p>Tráfego sem conversão é custo. Nas páginas deste nicho, quatro coisas costumam decidir
          se a visita vira conversa:</p>
"""
        + lista([
            "<strong>Clareza sobre o que está incluído.</strong> Visitante que não entende o que recebe não "
            "pergunta — ele sai e procura outro.",
            "<strong>Comparação entre planos na mesma tela.</strong> Escolher fica difícil quando é preciso "
            "rolar para cima e para baixo comparando.",
            "<strong>Resposta às dúvidas antes do contato.</strong> Compatibilidade, requisitos, como funciona "
            "a instalação. Quem tira a dúvida sozinho chega mais preparado — e converte melhor.",
            "<strong>Contato sem fricção.</strong> Botão visível em qualquer ponto da página, com a mensagem "
            "já iniciada e identificando de onde veio.",
        ])
        + """
          <p>Isso é medido. Cada botão carrega identificação de origem, e o relatório mostra quais páginas
          geram conversa e quais só geram visita — informação que orienta onde investir conteúdo depois.</p>""",
        """<h3>Medição configurada</h3>
          <ul class="audit-list">
            <li>Evento de clique por botão e por página</li>
            <li>Origem da conversa identificada na mensagem</li>
            <li>Análise com consentimento de cookies</li>
            <li>Relatório de páginas que mais convertem</li>
          </ul>
          <p style="margin-top:1rem;">Mesmo padrão de medição usado no restante dos projetos da RCB.</p>""",
        "conversao-titulo",
    )

    corpo += sec_texto(
        "Como funciona",
        "Etapas da construção",
        passos([
            ("Escopo", "Definição de páginas, funcionalidades e prazo, a partir da análise do projeto."),
            ("Marca e domínio", "Identidade e escolha do endereço — com avaliação de domínio quando fizer sentido."),
            ("Construção", "Desenvolvimento das páginas, estrutura de conteúdo e integração de contato."),
            ("Publicação", "Site no ar, com medição, indexação e envio de sitemap configurados."),
            ("Acompanhamento", "Ajustes conforme os primeiros dados de uso e conversão."),
        ]),
        "etapas-titulo", classe="metodo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre a criação do site")

    corpo += relacionados("Continue por aqui", [
        ("/seo-para-iptv/", "SEO para IPTV",
         "A estratégia de posicionamento que o site precisa sustentar."),
        ("/blog/como-criar-site-para-iptv-do-zero/", "Como criar um site do zero",
         "O passo a passo completo, incluindo o que decidir antes de começar."),
        ("/blog/estruturar-site-iptv-para-gerar-contatos/", "Estrutura que gera contato",
         "O que muda entre um site que recebe visita e um que gera conversa."),
    ])

    corpo += cta_final(
        "Quer o site construído da forma certa desde o começo?",
        "Na análise definimos escopo, páginas necessárias, prazo e faixa de investimento — e verificamos o "
        "critério de atendimento antes de qualquer proposta.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-revendedor-iptv/", "Sou revendedor e começo menor"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero criar um site para a minha operação e avaliar o projeto.",
        float_aria="Falar sobre criação de site pelo WhatsApp",
    )


# ============================================================
# B3 — /seo-para-revendedor-iptv/
# ============================================================

def b3_revendedor():
    slug = "seo-para-revendedor-iptv"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para revendedor de IPTV: estrutura própria | RCB"
    desc = ("Revendedor que depende só de rede social não constrói ativo. Site próprio, páginas de "
            "plano e captação de contatos pelo Google, com escopo proporcional.")
    page_id = "revendedor-iptv"

    faq = [
        ("Sou revendedor pequeno. Esse projeto não é grande demais para mim?",
         "O escopo é proporcional. Um revendedor que está começando não precisa da mesma estrutura de uma "
         "operação nacional: começa com um site enxuto, páginas de plano e captação organizada, e cresce "
         "conforme o retorno aparece."),
        ("Por que sair da rede social se ela já traz cliente?",
         "Não é para sair — é para não depender só dela. Perfil bloqueado, alcance reduzido ou mudança de "
         "regra derrubam o canal inteiro de uma vez, e você não leva nada. Site próprio e contatos "
         "registrados continuam seus."),
        ("Preciso ter marca própria?",
         "Ajuda muito. Sem nome próprio, você compete divulgando a marca do fornecedor — e qualquer outro "
         "revendedor do mesmo serviço aparece na mesma busca. Marca própria é o que separa o seu ativo do "
         "ativo de quem te fornece."),
        ("Quanto tempo até aparecer no Google?",
         "Buscas específicas e de menor disputa costumam responder antes; termos mais amplos levam mais "
         "tempo e dependem de conteúdo e autoridade acumulados. O cenário de prazo sai na análise, com as "
         "premissas explícitas — sem garantia de calendário."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para IPTV", f"{BASE_URL}/seo-para-iptv/"),
                           ("SEO para revendedor", canonical)]),
        schema_service("SEO para revendedor de IPTV",
                       "Estruturação de presença digital própria para revendedores autorizados: site, "
                       "páginas de plano, captação de contatos e posicionamento orgânico.",
                       canonical, tipo="SEO para revendedor"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para IPTV", "/seo-para-iptv/"),
                              ("Revendedor", canonical)])

    corpo = hero(
        trilha,
        "Escopo proporcional",
        "SEO para revendedor de IPTV: construir algo que é seu",
        "Quem revende costuma vender pelo perfil de rede social e pelo WhatsApp. Funciona — até o dia em "
        "que o perfil cai. Estrutura própria é o que resta quando isso acontece.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/criacao-de-site-para-iptv/", "Ver como o site é construído"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O risco invisível",
        "Todo o seu negócio está em uma conta que não é sua",
        """          <p>É o padrão mais comum entre revendedores: perfil em rede social, grupo de contatos e
          WhatsApp. Nada disso é ativo próprio. São contas em plataformas de terceiros, que podem ser
          restringidas, ter alcance reduzido ou ser encerradas sem aviso — e que levam junto a lista de
          clientes e o histórico de conversas.</p>
          <p>Quem tem site próprio e contatos registrados perde um canal quando isso acontece. Quem não
          tem, perde o negócio inteiro.</p>
          <p>Há um segundo ponto, menos dramático e igualmente relevante: <strong>quem procura no Google
          não te encontra</strong>. Rede social não aparece bem em busca. Existe demanda pesquisando por
          esse tipo de serviço todo dia, e ela vai inteira para quem tem site.</p>""",
        criterio_card("revendedor"),
        "risco-titulo",
    )

    corpo += sec_texto(
        "O que muda",
        "Da dependência de perfil para estrutura própria",
        tabela(
            ["", "Só rede social", "Com estrutura própria"],
            [
                ["De quem é o canal", "da plataforma", "seu"],
                ["Se a conta cai", "perde tudo", "perde um canal"],
                ["Quem te encontra", "quem já te segue", "quem pesquisa no Google"],
                ["Base de contatos", "presa ao aplicativo", "registrada e sua"],
                ["Marca", "confundida com a do fornecedor", "própria e reconhecível"],
                ["Crescimento", "limitado pelo alcance", "acumula com o tempo"],
            ],
            nota="Não é substituir a rede social. É deixar de depender só dela.",
        ),
        "mudanca-titulo",
    )

    corpo += sec_split(
        "Escopo",
        "O que um revendedor precisa de fato — e o que pode esperar",
        """          <p>A tentação, ao contratar, é querer tudo de uma vez. Para quem está começando, isso
          normalmente é desperdício. A sequência que costuma fazer mais sentido é esta:</p>
"""
        + lista([
            "<strong>Primeiro:</strong> site enxuto com marca própria, planos claros e contato por WhatsApp "
            "com origem identificada. Resolve o problema do ativo e já capta quem chega.",
            "<strong>Depois:</strong> páginas específicas para as dúvidas mais comuns antes da contratação — "
            "compatibilidade, requisitos, como funciona. É o conteúdo que traz busca sem exigir autoridade alta.",
            "<strong>Em seguida:</strong> conteúdo contínuo e trabalho de autoridade, quando o retorno das "
            "primeiras etapas justificar o investimento.",
            "<strong>Só então:</strong> disputa dos termos mais amplos, que exigem projeto completo — o que "
            "já é o escopo de <a href=\"/seo-para-iptv/\">SEO para IPTV</a>.",
        ])
        + """
          <p>Essa ordem existe para o investimento acompanhar o retorno, em vez de exigir de uma vez um
          valor que não faz sentido para o porte da operação.</p>""",
        """<h3>Começo enxuto</h3>
          <ul class="audit-list">
            <li>Marca própria simples</li>
            <li>Site com planos e comparação</li>
            <li>Páginas das dúvidas mais buscadas</li>
            <li>WhatsApp com origem identificada</li>
            <li>Medição básica configurada</li>
          </ul>
          <p style="margin-top:1rem;">A partir daí, cresce conforme o retorno — não conforme o orçamento
          disponível no primeiro mês.</p>""",
        "escopo-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes de revendedores")

    corpo += relacionados("Continue por aqui", [
        ("/criacao-de-site-para-iptv/", "Criação de site",
         "O que entra na construção e como o site é preparado para crescer."),
        ("/blog/site-para-revendedor-iptv-o-que-precisa-ter/", "O que o site precisa ter",
         "A lista prática do que não pode faltar em um site de revenda."),
        ("/seo-para-iptv/", "Projeto completo",
         "Quando a operação cresce e passa a fazer sentido disputar os termos principais."),
    ])

    corpo += cta_final(
        "Quer parar de depender de um perfil?",
        "Na análise a gente dimensiona o começo pelo tamanho da sua operação — sem empurrar escopo que "
        "você ainda não precisa.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Sou revendedor e quero montar uma estrutura própria.",
        float_aria="Falar sobre estrutura para revendedor pelo WhatsApp",
    )


# ============================================================
# B4 — /link-building-para-iptv/
# ============================================================

def b4_link_building_iptv():
    slug = "link-building-para-iptv"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Link building para IPTV: autoridade com critério | RCB"
    desc = ("Construção de autoridade para projetos de IPTV: relevância temática, avaliação de risco "
            "e ritmo controlado. Sem promessa de backlinks ilimitados.")
    page_id = "link-building-iptv"

    faq = [
        ("Quantos backlinks meu site precisa?",
         "Não existe número. A referência útil é comparativa: quantos domínios diferentes apontam para "
         "quem está nas posições que você quer ocupar, e de que tipo de site eles vêm. Esse levantamento "
         "faz parte da análise, e o plano sai dele — não de uma meta de quantidade."),
        ("Por que é mais difícil conseguir links neste nicho?",
         "Porque muitos veículos evitam o tema, o que reduz o conjunto de fontes relevantes disponíveis. "
         "Isso torna cada conquista mais trabalhosa e mais cara, e é o principal motivo de o prazo deste "
         "cluster ser mais longo que o de nichos neutros."),
        ("Comprar links resolve mais rápido?",
         "Costuma criar padrão artificial e desperdiçar verba em veículos sem relevância real. O ganho, "
         "quando existe, é instável, e o passivo fica no seu domínio. O que a RCB faz é construção com "
         "critério — mais lenta e que não coloca o ativo em risco."),
        ("O que acontece se o perfil de links já estiver ruim?",
         "Primeiro se mede o estrago: de onde vêm os links, qual proporção é de baixa qualidade e se há "
         "padrão evidente. Só depois se decide entre desautorizar, diluir com aquisição de qualidade ou "
         "as duas coisas. É o escopo da consultoria de backlinks."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para IPTV", f"{BASE_URL}/seo-para-iptv/"),
                           ("Link building para IPTV", canonical)]),
        schema_service("Link building para IPTV",
                       "Construção de autoridade para projetos de IPTV e streaming, com critério de "
                       "relevância temática, avaliação de risco e ritmo controlado.",
                       canonical, tipo="Link building"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para IPTV", "/seo-para-iptv/"),
                              ("Link building", canonical)])

    corpo = hero(
        trilha,
        "Construção de autoridade",
        "Link building para IPTV: o gargalo real do nicho",
        "Neste mercado, conteúdo raramente é o que trava um projeto. Autoridade é. E é justamente onde "
        "a maior parte da verba costuma ser mal gasta.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/link-building-para-nichos-competitivos/", "Ver a metodologia completa"),
        page_id=page_id,
    )

    corpo += sec_split(
        "Por que aqui é diferente",
        "A dificuldade específica deste nicho",
        """          <p>Link building já é a parte mais lenta de qualquer projeto competitivo. Neste cluster,
          é mais lenta ainda, por um motivo objetivo: <strong>o conjunto de veículos dispostos a tratar do
          tema é menor</strong>.</p>
          <p>Isso muda o cálculo de três formas. Primeiro, cada conquista custa mais tempo e mais dinheiro.
          Segundo, a tentação de recorrer a fontes de baixa qualidade aumenta — e é exatamente aí que
          projetos se enterram. Terceiro, o prazo estimado precisa refletir essa escassez desde o começo,
          em vez de virar surpresa no terceiro mês.</p>
          <p>A resposta não é forçar volume. É ampliar o que conta como fonte relevante: conteúdo técnico
          que sirva de referência, materiais sobre tecnologia e compatibilidade, presença em contextos
          adjacentes ao tema central. Relevância temática não exige que o veículo fale exatamente do seu
          produto — exige proximidade de assunto.</p>""",
        """<h3>Critérios de avaliação</h3>
          <p>Antes de buscar qualquer menção, cada fonte passa por:</p>
          <ul class="audit-list">
            <li>Relevância temática real com o projeto</li>
            <li>Histórico e idade do domínio</li>
            <li>Se o site tem tráfego próprio</li>
            <li>Perfil de links de saída — sinais de venda em massa</li>
            <li>Contexto em que o link apareceria</li>
          </ul>
          <p style="margin-top:1rem;">Fonte que não passa nesses critérios não entra, mesmo barata.</p>""",
        "diferenca-titulo",
    )

    corpo += sec_texto(
        "Como é feito",
        "Qualidade, relevância e ritmo",
        problem_cards([
            ("Qualidade antes de quantidade",
             "Poucos links de veículos relevantes movem mais que muitos links de qualquer lugar. E o "
             "inverso tem custo: perfil inflado de fontes fracas é passivo que precisa ser desfeito depois."),
            ("Relevância temática",
             "O que pesa é a proximidade de assunto entre o veículo e o seu projeto. Link de site sem "
             "nenhuma relação temática entrega pouco, independentemente de qualquer métrica de autoridade."),
            ("Ritmo que não destoa",
             "Aquisição em lote cria padrão. A construção segue um ritmo compatível com o crescimento "
             "natural do site — mais lento no começo, acelerando conforme o conteúdo se acumula."),
            ("Distribuição de âncoras",
             "Concentrar o texto do link no termo exato que se quer ranquear é o padrão artificial mais "
             "fácil de identificar. A distribuição mistura marca, endereço, termos genéricos e variações."),
        ]),
        "como-titulo", classe="problem-section",
        desc="A construção começa quando já existe conteúdo que justifique a referência. Buscar menção "
             "para um site sem conteúdo é gastar a fonte antes de ela render.",
    )

    corpo += sec_split(
        "Acompanhamento",
        "O que é reportado",
        """          <p>Link building é a frente em que mais se promete e menos se comprova. O relatório deste
          serviço mostra o que foi feito e o que mudou, sem métrica inventada:</p>
"""
        + lista([
            "Domínios de referência conquistados no período, com o endereço de cada um.",
            "Contexto de cada menção — em que tipo de conteúdo o link apareceu.",
            "Distribuição de âncoras acumulada, para acompanhar naturalidade do perfil.",
            "Evolução do total de domínios de referência ao longo do tempo.",
            "Comparação com o perfil dos concorrentes que ocupam as posições-alvo.",
            "Fontes descartadas e o motivo — informação que evita repetir avaliação.",
        ])
        + """
          <p>O que não aparece no relatório: promessa de quantidade fixa por mês, métrica proprietária sem
          explicação ou correlação direta entre link conquistado e posição. Autoridade age de forma
          acumulada e defasada, não link a link.</p>""",
        """<h3>O que não é oferecido</h3>
          <ul class="audit-list">
            <li>Backlinks ilimitados</li>
            <li>Pacote de quantidade fixa</li>
            <li>Rede privada de sites (PBN)</li>
            <li>Compra em massa</li>
            <li>Garantia de posição por link</li>
          </ul>
          <p style="margin-top:1rem;">Entenda o porquê em
          <a href="/blog/comprar-backlinks-ajuda-no-posicionamento/">comprar backlinks ajuda?</a></p>""",
        "relatorio-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre autoridade neste nicho")

    corpo += relacionados("Continue por aqui", [
        ("/link-building-para-nichos-competitivos/", "Metodologia completa",
         "Como a construção de autoridade funciona em projetos nacionais e disputados."),
        ("/consultoria-de-backlinks/", "Auditoria do perfil atual",
         "Quando o problema não é conquistar links, e sim o que já está apontando para o site."),
        ("/blog/quanto-investir-backlinks-iptv/", "Quanto investir em autoridade",
         "Como dimensionar a verba dessa frente dentro do projeto."),
        ("/blog/backlinks-para-iptv-funcionam/", "Backlinks para IPTV funcionam?",
         "A leitura de eficácia por tipo de veículo, do que mais rende ao que é passivo."),
    ])

    corpo += cta_final(
        "Quer saber quanta autoridade o seu alvo exige?",
        "Na análise eu levanto o perfil de links de quem ocupa as posições que você quer e comparo com o "
        "seu — o que transforma \"preciso de backlinks\" em um plano com escopo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-iptv/", "Ver o projeto completo"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar a construção de autoridade do meu projeto.",
        float_aria="Falar sobre link building pelo WhatsApp",
    )


# ============================================================
# B5 — /dominio-expirado-para-iptv/
# ============================================================

def b5_dominio_expirado_iptv():
    slug = "dominio-expirado-para-iptv"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Domínio expirado para IPTV: vale a pena? | RCB Consultoria"
    desc = ("Domínio novo ou expirado para IPTV: o que o histórico realmente entrega, o que é mito "
            "e como avaliar o risco antes de comprar.")
    page_id = "dominio-expirado-iptv"

    faq = [
        ("Domínio expirado garante autoridade?",
         "Não. Essa é a expectativa mais comum e a mais equivocada. O que um domínio carrega é histórico — "
         "que pode ajudar, ser irrelevante ou atrapalhar. Só a análise do histórico específico diz em qual "
         "desses casos ele está."),
        ("Quanto custa um domínio expirado?",
         "Varia muito, de valores baixos em leilão a quantias altas por nomes disputados. O preço acompanha "
         "a percepção de valor do nome e do histórico, não a certeza de resultado. Comprar caro não reduz o "
         "risco — só a análise reduz."),
        ("Domínio premium ou domínio expirado?",
         "São coisas diferentes. Premium costuma ser um nome curto e comercialmente valioso, geralmente sem "
         "histórico relevante. Expirado é um domínio que já foi usado e carrega passado. Um vende memorização, "
         "o outro vende histórico — e o segundo exige verificação."),
        ("O que acontece se o domínio já tiver sido usado para spam?",
         "O passivo vem junto. Perfil de links artificial, conteúdo problemático indexado e eventual histórico "
         "de penalização não desaparecem porque o dono mudou. Em muitos casos sai mais barato começar com "
         "domínio novo do que limpar um domínio comprometido."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para IPTV", f"{BASE_URL}/seo-para-iptv/"),
                           ("Domínio expirado para IPTV", canonical)]),
        schema_service("Análise de domínio expirado para IPTV",
                       "Avaliação de domínios expirados para projetos de IPTV e streaming: histórico, "
                       "perfil de links, relevância temática e risco antes da compra.",
                       canonical, tipo="Análise de domínio"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para IPTV", "/seo-para-iptv/"),
                              ("Domínio expirado", canonical)])

    corpo = hero(
        trilha,
        "Decisão de domínio",
        "Domínio expirado para IPTV: o que ele entrega de verdade",
        "É a pergunta mais frequente de quem vai começar um projeto neste nicho. A resposta honesta é "
        "menos animadora que a promessa de mercado — e mais útil.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/analise-de-dominios-expirados/", "Ver o serviço de análise"),
        page_id=page_id,
    )

    corpo += sec_split(
        "A expectativa",
        "O que se espera de um domínio expirado, e o que ele faz",
        """          <p>A expectativa que circula no mercado é mais ou menos esta: compra-se um domínio que já
          tem links apontando, sobe-se o site novo nele e o projeto começa com anos de vantagem.</p>
          <p>Na prática, o que um domínio expirado oferece é <strong>histórico</strong> — e histórico não é
          sinônimo de vantagem. Ele pode ser útil quando há relevância temática com o novo projeto, perfil
          de links legítimo e nenhum passivo. Pode ser neutro, quando os links vieram de contextos que não
          têm relação com o que você vai fazer. E pode ser prejuízo, quando o domínio foi usado para spam,
          acumulou links artificiais ou carrega histórico de penalização.</p>
          <p>Os três casos existem, e não dá para distinguir olhando o preço ou uma métrica isolada de
          autoridade. Só verificando o passado do domínio.</p>""",
        """<h3>Três resultados possíveis</h3>
          <ul class="audit-list">
            <li><strong>Ajuda</strong> — histórico limpo, tema próximo, links legítimos.</li>
            <li><strong>Indiferente</strong> — links reais, mas de contexto sem relação.</li>
            <li><strong>Atrapalha</strong> — spam, links artificiais ou penalização herdada.</li>
          </ul>
          <p style="margin-top:1rem;">A proporção entre esses três casos no mercado de leilão não favorece
          quem compra sem analisar.</p>""",
        "expectativa-titulo",
    )

    corpo += sec_texto(
        "Comparação",
        "Domínio novo ou domínio com histórico",
        tabela(
            ["", "Domínio novo", "Domínio expirado"],
            [
                ["Custo inicial", "baixo", "de baixo a muito alto"],
                ["Histórico", "nenhum", "precisa ser verificado"],
                ["Risco herdado", "nenhum", "existe e pode ser alto"],
                ["Ponto de partida", "do zero", "pode encurtar caminho"],
                ["Previsibilidade", "alta", "depende inteiramente da análise"],
                ["Quando faz sentido", "quase sempre", "quando a análise confirma histórico limpo e relevante"],
            ],
            nota="Não existe escolha certa universal: existe escolha certa para um domínio específico, verificado.",
        ),
        "comparacao-titulo",
        desc="Para a maior parte dos projetos, domínio novo é a opção previsível e suficiente. Domínio "
             "expirado entra quando a análise confirma que aquele caso específico compensa o risco.",
    )

    corpo += sec_split(
        "Avaliação",
        "O que é verificado antes de recomendar a compra",
        """          <p>A análise de um domínio candidato passa por seis pontos. Nenhum deles isolado decide —
          é o conjunto que forma a recomendação:</p>
"""
        + lista([
            "<strong>Histórico de conteúdo</strong> — o que esteve publicado ali ao longo dos anos, "
            "recuperado de registros públicos de arquivo.",
            "<strong>Perfil de links</strong> — de onde vêm, quantos domínios distintos, se há concentração "
            "suspeita ou padrão de compra em massa.",
            "<strong>Relevância temática</strong> — se o assunto anterior tem relação com o projeto novo. "
            "Sem isso, o histórico entrega pouco.",
            "<strong>Sinais de spam</strong> — âncoras artificiais, links de redes conhecidas, conteúdo "
            "indexado problemático.",
            "<strong>Idade e continuidade</strong> — há quanto tempo existe e se ficou muito tempo parado, "
            "o que reduz o valor do histórico.",
            "<strong>O nome em si</strong> — se funciona comercialmente, é memorizável e não carrega marca "
            "de terceiros, o que seria problema jurídico e não de SEO.",
        ])
        + """
          <p>O entregável é uma recomendação objetiva: comprar, não comprar, ou comprar até determinado
          valor. Com o motivo escrito — inclusive quando a recomendação é desistir do domínio.</p>
          <p>O serviço completo, com triagem de vários candidatos, está em
          <a href="/analise-de-dominios-expirados/">análise de domínios expirados</a>.</p>""",
        criterio_card("curto"),
        "avaliacao-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre domínio expirado")

    corpo += relacionados("Continue por aqui", [
        ("/analise-de-dominios-expirados/", "O serviço de análise",
         "Triagem, critérios, entregável e como funciona a recomendação de compra."),
        ("/blog/como-analisar-historico-de-dominio-expirado/", "Como analisar o histórico",
         "O passo a passo de verificação, com as fontes públicas usadas."),
        ("/blog/como-saber-se-dominio-expirado-foi-usado-para-spam/", "Sinais de spam",
         "O que procurar para identificar um domínio comprometido antes de comprar."),
        ("/blog/como-escolher-dominio-expirado-com-autoridade/", "Como escolher entre candidatos",
         "Os critérios de comparação em ordem de peso, e como definir um teto de preço."),
    ])

    corpo += cta_final(
        "Tem um domínio em vista?",
        "Envie o domínio na análise do projeto e eu verifico histórico, perfil de links e risco antes de "
        "você comprar — inclusive quando a recomendação for não comprar.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-iptv/", "Ver o projeto completo"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar um domínio antes de comprar.",
        float_aria="Falar sobre análise de domínio pelo WhatsApp",
    )


# ============================================================
# B6 — /seo-para-streaming-e-tv-online/
# ============================================================

def b6_streaming():
    slug = "seo-para-streaming-e-tv-online"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para streaming e TV online | RCB Consultoria"
    desc = ("Aquisição orgânica para plataformas de streaming, TV online e serviços por assinatura: "
            "catálogo, lançamentos, retenção e disputa nacional.")
    page_id = "streaming-tv-online"

    faq = [
        ("Faz sentido investir em orgânico se meu crescimento vem de anúncio?",
         "Faz, principalmente em assinatura. O custo pago se repete a cada novo assinante, enquanto uma "
         "página posicionada continua trazendo gente sem custo por clique. A questão não é trocar um pelo "
         "outro, é não depender só de um."),
        ("Meu catálogo muda toda semana. Como o conteúdo acompanha?",
         "Com estrutura, não com esforço manual repetido. Páginas de catálogo bem organizadas, regras claras "
         "de indexação e conteúdo editorial em volta dos lançamentos permitem acompanhar a rotatividade sem "
         "reescrever o site a cada mudança."),
        ("Conteúdo de suporte ajuda no posicionamento?",
         "Ajuda em duas frentes. Traz busca de quem está com um problema específico — muitas vezes gente que "
         "ainda nem é cliente — e reduz cancelamento, porque quem resolve a dificuldade sozinho permanece. "
         "É o tipo de conteúdo mais subestimado em serviço por assinatura."),
        ("A RCB atende plataforma estrangeira entrando no Brasil?",
         "Sim. Nesses casos o trabalho começa por localização de verdade: como o brasileiro pesquisa aquele "
         "tipo de serviço, quais termos são usados aqui e o que a concorrência local já ocupa — e não por "
         "tradução do conteúdo existente."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para streaming e TV online", canonical)]),
        schema_service("SEO para streaming e TV online",
                       "Aquisição orgânica para plataformas de streaming, TV por internet e serviços de "
                       "conteúdo por assinatura: arquitetura de catálogo, lançamentos e retenção.",
                       canonical, tipo="SEO para streaming"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Streaming e TV online", canonical)])

    corpo = hero(
        trilha,
        "Plataformas e assinatura",
        "SEO para streaming e TV online: aquisição que se acumula",
        "Plataforma de conteúdo cresce com mídia paga e sustenta com orgânico. A diferença aparece no "
        "custo por assinante depois do primeiro ano.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/seo-para-negocios-digitais/", "Ver negócios digitais"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "Quem é atendido",
        "Operações deste cluster",
        cards([
            (None, "Plataformas de streaming",
             "Serviços de conteúdo sob demanda com catálogo próprio ou licenciado e modelo de assinatura.", None),
            (None, "TV por internet licenciada",
             "Operações de transmissão com direito ou autorização sobre o conteúdo distribuído.", None),
            (None, "Conteúdo por assinatura",
             "Serviços de acesso recorrente a acervo — vídeo, áudio, eventos ou conteúdo especializado.", None),
            (None, "Aplicativos de conteúdo",
             "Apps cuja aquisição depende de busca na web antes da instalação, e não só das lojas.", None),
            (None, "Plataformas em lançamento",
             "Operações em construção, que podem nascer com estrutura de aquisição orgânica já pronta.", None),
            (None, "Entrada no mercado brasileiro",
             "Plataformas estrangeiras estruturando presença em português para o Brasil.", None),
        ]),
        "quem-titulo", classe="cluster-section",
    )

    corpo += sec_split(
        "Catálogo",
        "O problema estrutural de quem tem acervo grande",
        """          <p>Plataforma de conteúdo tem um desafio técnico que site institucional não tem: o catálogo
          gera <strong>muitas páginas, que mudam com frequência</strong>. Títulos entram, saem, ganham
          categoria nova, aparecem em várias listas ao mesmo tempo.</p>
          <p>Sem regra clara, isso produz um conjunto grande de páginas quase idênticas — a mesma obra
          acessível por caminhos diferentes, listas geradas por filtro e combinações que ninguém pesquisa.
          O resultado é diluição: o buscador gasta atenção em páginas irrelevantes e as que importam ficam
          para trás.</p>
          <p>A solução é decidir antes o que merece ser indexado, o que deve ser consolidado em um endereço
          único e o que fica fora do índice sem prejudicar a navegação de quem já é assinante. Essa decisão
          é arquitetural e precisa ser tomada com quem desenvolve a plataforma.</p>""",
        """<h3>Decisões de arquitetura</h3>
          <ul class="audit-list">
            <li>O que é página indexável e o que é navegação</li>
            <li>Endereço único por obra, com canonical claro</li>
            <li>Regras para filtros e combinações</li>
            <li>Tratamento de conteúdo que sai do catálogo</li>
            <li>Dados estruturados adequados ao tipo de conteúdo</li>
            <li>Separação entre área pública e área de assinante</li>
          </ul>""",
        "catalogo-titulo",
    )

    corpo += sec_split(
        "Ciclo",
        "Lançamento, rotina e retenção",
        """          <p>A aquisição orgânica de uma plataforma se organiza em três ritmos diferentes, e tratá-los
          igual é o erro mais comum:</p>
          <p><strong>Lançamento.</strong> Momento de pico de busca, curto e previsível. Exige conteúdo
          publicado <em>antes</em> do pico, porque página nova raramente ranqueia a tempo de aproveitar a
          janela. Quem publica no dia perde o movimento.</p>
          <p><strong>Rotina.</strong> A demanda constante — quem procura por categoria, por tipo de conteúdo,
          por comparação entre serviços. É o que sustenta o volume entre os lançamentos e onde o trabalho de
          autoridade rende.</p>
          <p><strong>Retenção.</strong> Conteúdo para quem já assina: como usar, resolver problema, aproveitar
          recurso. Não aparece nos relatórios de aquisição, mas reduz cancelamento — e em modelo recorrente,
          isso vale tanto quanto assinante novo.</p>""",
        """<h3>Indicadores por ritmo</h3>
          <ul class="audit-list">
            <li><strong>Lançamento</strong> — impressões na janela de pico</li>
            <li><strong>Rotina</strong> — termos únicos e posição média</li>
            <li><strong>Retenção</strong> — busca interna e conteúdo de suporte acessado</li>
            <li><strong>Geral</strong> — assinantes originados de orgânico</li>
          </ul>
          <p style="margin-top:1rem;">Medir os três separadamente evita concluir que "o orgânico caiu"
          quando o que acabou foi um pico de lançamento.</p>""",
        "ciclo-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre streaming")

    corpo += relacionados("Continue por aqui", [
        ("/seo-para-negocios-digitais/", "SEO para negócios digitais",
         "A visão geral de aquisição orgânica para produto digital e assinatura."),
        ("/seo-para-iptv/", "SEO para IPTV",
         "O projeto completo para operações licenciadas de TV por internet."),
        ("/seo-nacional/", "SEO nacional",
         "Como funciona a disputa quando o cliente pode estar em qualquer lugar do país."),
    ])

    corpo += cta_final(
        "Quer estruturar a aquisição orgânica da sua plataforma?",
        "Na análise eu avalio a arquitetura atual do catálogo, o que está diluindo força e quais buscas do "
        "seu mercado o orgânico pode assumir — com escopo, prazo estimado e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Tenho uma plataforma de streaming e quero avaliar aquisição orgânica.",
        float_aria="Falar sobre SEO para streaming pelo WhatsApp",
    )


PAGINAS = [b1_seo_para_iptv, b2_criacao_site_iptv, b3_revendedor,
           b4_link_building_iptv, b5_dominio_expirado_iptv, b6_streaming]
