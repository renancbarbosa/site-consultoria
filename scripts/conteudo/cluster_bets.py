# -*- coding: utf-8 -*-
"""
Cluster C — bets, apostas, iGaming e jogos online.

C1 /seo-para-bets/                        (pilar do cluster; absorve "cassino online")
C2 /seo-para-igaming/                     (B2B)
C3 /seo-para-afiliados-de-apostas/
C4 /criacao-de-site-para-afiliado-de-bet/
C5 /link-building-para-bets/
C6 /seo-para-jogos-online/

POLÍTICA DO CLUSTER (docs/seo-mercados-competitivos-plan.md §2.6)
- Linguagem neutra quanto à regulação. Não afirmar que qualquer empresa pode
  operar apostas legalmente no Brasil, nem dar conclusão jurídica.
- Orientar o leitor a verificar a situação regulatória da própria operação.
- Sem apelo ao jogo, sem promessa de ganho, sem menção a público menor de idade.

/seo-para-cassino-online/ NÃO foi criada: mesma audiência, mesmo serviço e mesma
jornada de C1. Virou seção própria aqui + artigo de apoio.
"""
from rcb_base import (
    BASE_URL, head_comum, montar, breadcrumb_html, hero, sec_texto, sec_split,
    cards, problem_cards, passos, lista, tabela, sec_faq, cta_final,
    relacionados, grafo, schema_webpage, schema_breadcrumb, schema_service,
    schema_faq,
)

HOJE = "2026-08-06"
ANALISE = "/analise-de-projeto/"

NOTA_REGULATORIA = """<h3>Sobre a parte regulatória</h3>
          <p>O setor de apostas no Brasil passou por mudanças regulatórias relevantes nos últimos anos, e as
          regras aplicáveis variam conforme o tipo de operação, a origem da empresa e a atividade exercida.</p>
          <p>A RCB atua na comunicação e no posicionamento orgânico — <strong>não presta orientação
          jurídica nem avalia a regularidade da sua operação</strong>. Cada empresa deve verificar com
          assessoria própria a situação regulatória a que está sujeita, inclusive quanto a regras de
          publicidade do setor.</p>"""


# ============================================================
# C1 — /seo-para-bets/   (pilar do cluster)
# ============================================================

def c1_seo_para_bets():
    slug = "seo-para-bets"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para bets: projeto para o setor de apostas | RCB"
    desc = ("SEO para casas de apostas, portais e operadores: conteúdo, autoridade e execução técnica "
            "para disputa nacional, com comunicação responsável.")
    page_id = "seo-bets"

    faq = [
        ("Quanto custa um projeto de SEO para bet?",
         "É um dos nichos mais caros do país para disputar organicamente, porque os concorrentes investem "
         "pesado e há muito dinheiro em jogo em cada posição. O que forma a faixa é o alvo escolhido, o "
         "ponto de partida e a intensidade da construção de autoridade — definido na análise do projeto."),
        ("A RCB trabalha com sites de apostas?",
         "Sim, na parte de comunicação e posicionamento orgânico: conteúdo, arquitetura, execução técnica e "
         "autoridade. A RCB não presta orientação jurídica nem avalia a regularidade da operação — isso "
         "cabe à assessoria própria de cada empresa."),
        ("Em quanto tempo dá para posicionar uma bet?",
         "Termos principais deste setor estão entre os mais disputados do Brasil e costumam exigir horizonte "
         "longo. Termos específicos e de cauda longa respondem antes. Nenhum prazo é garantido — a análise "
         "entrega cenários com as premissas explícitas."),
        ("Vale mais investir em conteúdo ou em autoridade?",
         "Nos primeiros meses, conteúdo, porque autoridade sem conteúdo que a justifique é desperdício. "
         "Depois os dois andam juntos, e neste setor a autoridade costuma ser o fator que decide as "
         "posições de topo."),
        ("Como fica a comunicação nas páginas?",
         "Informativa e sóbria: o que o serviço é, como funciona, o que diferencia. Sem apelo ao jogo, sem "
         "promessa de ganho e sem linguagem que estimule comportamento de risco. Isso não é só postura — "
         "é o que sustenta o conteúdo no longo prazo."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para bets", canonical)]),
        schema_service("SEO para bets",
                       "Projeto de SEO para marcas, plataformas e portais do setor de apostas: arquitetura "
                       "de conteúdo, execução técnica, construção de autoridade e acompanhamento.",
                       canonical, tipo="SEO para o setor de apostas"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("SEO para bets", canonical)])

    painel = """<h2>Frentes do projeto</h2>
          <ul class="audit-list">
            <li>Arquitetura de conteúdo por intenção</li>
            <li>Páginas comerciais e de categoria</li>
            <li>SEO técnico e indexação em escala</li>
            <li>Construção de autoridade</li>
            <li>Conteúdo editorial e calendário</li>
            <li>Medição e relatórios</li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:.75rem;">Escopo definido na análise, conforme o tipo de operação.</p>"""

    corpo = hero(
        trilha,
        "Setor de apostas",
        "SEO para bets: disputa orgânica em um dos mercados mais caros do Brasil",
        "Conteúdo, arquitetura e autoridade para marcas, plataformas e portais do setor — com "
        "comunicação sóbria e execução dimensionada para a concorrência real.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#publicos", "Ver os perfis atendidos"),
        painel, page_id,
    )

    corpo += sec_split(
        "Contexto",
        "Por que este é um dos nichos mais difíceis do país",
        """          <p>Poucos mercados no Brasil concentram tanto investimento por posição orgânica. Isso tem
          três consequências práticas para quem entra agora.</p>
          <p><strong>Os concorrentes não são amadores.</strong> Há equipes internas dedicadas, produção de
          conteúdo em ritmo industrial e verbas de autoridade que a maior parte dos setores não vê. Entrar
          com meio projeto não entrega meio resultado — costuma não entregar nada.</p>
          <p><strong>A mídia paga é limitada e cara.</strong> O que empurra ainda mais concorrente para o
          orgânico e encarece a disputa por cada posição.</p>
          <p><strong>O ambiente muda.</strong> Regras de publicidade do setor e o próprio ambiente
          regulatório passaram por alterações relevantes, o que afeta como a comunicação pode ser feita. Um
          projeto de conteúdo precisa ser construído para suportar mudança, não para depender de uma janela.</p>""",
        NOTA_REGULATORIA,
        "contexto-titulo",
    )

    corpo += sec_texto(
        "Perfis atendidos",
        "Quatro operações diferentes dentro do mesmo setor",
        cards([
            ("#", "Marcas e operadores",
             "Casas de apostas que disputam busca de marca e de categoria, e precisam de conteúdo próprio "
             "para não depender de portais de terceiros.", None),
            ("/seo-para-afiliados-de-apostas/", "Portais e afiliados",
             "Sites de review, comparação e conteúdo, monetizados por afiliação e totalmente dependentes de orgânico.",
             "Ver SEO para afiliados"),
            ("/seo-para-igaming/", "Fornecedores e plataformas",
             "Empresas B2B — provedores de jogo, plataformas, meios de pagamento — que vendem para operadores.",
             "Ver SEO para iGaming"),
            ("/seo-para-jogos-online/", "Jogos e entretenimento",
             "Portais e plataformas de jogos que não são de aposta, com público e disputa próprios.",
             "Ver SEO para jogos online"),
        ]),
        "publicos", classe="cluster-section",
        desc="São públicos, jornadas e páginas de resultado diferentes. Tratá-los com a mesma estratégia é "
             "o erro que mais desperdiça verba neste setor.",
    )

    corpo += sec_split(
        "Cassino online",
        "O que muda quando o foco é cassino e jogos de mesa",
        """          <p>Esta é uma das buscas mais procuradas do setor, e ela pede tratamento próprio dentro do
          projeto — não uma página separada disputando as mesmas posições, mas uma <strong>estrutura de
          categoria com profundidade real</strong>.</p>
          <p>A diferença em relação a apostas esportivas está na arquitetura. Enquanto o esportivo se
          organiza por competição, time e evento — com forte componente de calendário —, a área de cassino
          se organiza por <strong>tipo de jogo, provedor e mecânica</strong>. São hierarquias diferentes,
          com conteúdo que envelhece em ritmos diferentes.</p>
          <p>Na prática, isso significa páginas de categoria por tipo de jogo, conteúdo explicativo sobre
          funcionamento e regras, e organização por provedor quando o catálogo justifica. O conteúdo aqui é
          mais estável que o esportivo, o que o torna um ativo de longo prazo dentro do projeto.</p>
          <p>Aprofundamento em <a href="/blog/seo-para-cassino-online-desafios/">SEO para cassino online:
          principais desafios</a>.</p>""",
        """<h3>Duas arquiteturas</h3>
          <p><strong>Esportivo</strong></p>
          <ul class="audit-list">
            <li>Organizado por competição e evento</li>
            <li>Forte dependência de calendário</li>
            <li>Picos previsíveis, conteúdo perecível</li>
          </ul>
          <p style="margin-top:1rem;"><strong>Cassino</strong></p>
          <ul class="audit-list">
            <li>Organizado por tipo de jogo e provedor</li>
            <li>Demanda mais constante</li>
            <li>Conteúdo de vida longa</li>
          </ul>""",
        "cassino-titulo",
    )

    corpo += sec_texto(
        "Estratégia",
        "Como o projeto é construído",
        passos([
            ("Leitura da SERP", "Quem ocupa cada grupo de termos: operadores, portais de afiliado ou "
                                "veículos de mídia. Cada tipo exige uma resposta diferente."),
            ("Arquitetura", "Definição da hierarquia — categorias, páginas comerciais e conteúdo editorial — "
                            "para evitar que as próprias páginas disputem entre si."),
            ("Base técnica", "Indexação em escala, desempenho, tratamento de páginas geradas dinamicamente e "
                             "dados estruturados adequados."),
            ("Conteúdo em ritmo", "Publicação contínua, com calendário para o que é sazonal e conteúdo "
                                  "estável para o que sustenta posição o ano todo."),
            ("Autoridade", "Construção com critério de relevância e análise de risco — a frente que costuma "
                           "decidir as posições de topo neste setor."),
            ("Medição", "Acompanhamento por grupo de termos, com leitura separada do que é sazonal e do que é "
                        "estrutural."),
        ]),
        "estrategia-titulo", classe="metodo",
    )

    corpo += sec_split(
        "Conteúdo",
        "O que sustenta posição quando todo mundo publica muito",
        """          <p>Em um setor onde todos produzem em volume, volume deixa de ser diferencial. O que separa
          o conteúdo que sustenta posição do que só ocupa espaço:</p>
"""
        + lista([
            "<strong>Informação verificável</strong> — condições, regras e funcionamento descritos com "
            "precisão, e atualizados quando mudam. Conteúdo desatualizado neste setor perde posição rápido.",
            "<strong>Profundidade real</strong> — responder a dúvida por completo, incluindo o que a "
            "concorrência omite por ser inconveniente.",
            "<strong>Organização navegável</strong> — o visitante precisa comparar. Tabela, filtro e "
            "estrutura clara valem mais que texto corrido longo.",
            "<strong>Sobriedade</strong> — comunicação informativa, sem apelo ao jogo e sem promessa de "
            "ganho. Além de ser a postura correta, é o que mantém o conteúdo utilizável quando as regras "
            "de publicidade mudam.",
            "<strong>Manutenção</strong> — conteúdo do setor envelhece. Um plano de revisão periódica faz "
            "parte do escopo, não é extra.",
        ])
        + """
          <p>Esse último ponto é o mais negligenciado: projetos que só publicam e nunca revisam acumulam
          páginas desatualizadas que passam a puxar o site para baixo.</p>""",
        """<h3>Tipos de página</h3>
          <ul class="audit-list">
            <li>Páginas de categoria por modalidade</li>
            <li>Páginas de produto e condições</li>
            <li>Conteúdo explicativo de funcionamento</li>
            <li>Comparativos e guias de escolha</li>
            <li>Conteúdo sazonal por calendário</li>
            <li>Suporte e dúvidas frequentes</li>
          </ul>""",
        "conteudo-bets-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre SEO para bets")

    corpo += relacionados("Continue por aqui", [
        ("/blog/quanto-custa-seo-para-sites-de-apostas/", "Quanto custa SEO para apostas?",
         "O que forma o custo em um dos nichos mais caros do país."),
        ("/blog/quanto-tempo-para-posicionar-uma-bet/", "Quanto tempo demora?",
         "Os fatores que mexem no prazo, sem promessa de calendário."),
        ("/link-building-para-bets/", "Link building para bets",
         "A frente que costuma decidir as posições de topo neste setor."),
    ])

    corpo += cta_final(
        "Quer dimensionar a disputa do seu segmento?",
        "Na análise eu leio a SERP dos seus termos, identifico o tipo de concorrente que ocupa cada grupo e "
        "devolvo o escopo necessário — com cenário de prazo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-afiliados-de-apostas/", "Sou afiliado, não operador"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar um projeto de SEO no setor de apostas.",
        float_aria="Falar sobre SEO para bets pelo WhatsApp",
    )


# ============================================================
# C2 — /seo-para-igaming/
# ============================================================

def c2_igaming():
    slug = "seo-para-igaming"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para iGaming no Brasil: B2B e expansão | RCB"
    desc = ("SEO para plataformas, provedores e fornecedores de iGaming que vendem para operadores "
            "ou entram no mercado brasileiro. Localização em português.")
    page_id = "igaming"

    faq = [
        ("Qual a diferença entre SEO para bets e SEO para iGaming?",
         "O público. SEO para bets mira o apostador — volume alto, disputa massiva. SEO para iGaming, no "
         "recorte desta página, mira quem compra de fornecedores: operadores, plataformas e empresas do "
         "setor. Volume muito menor, ciclo de decisão longo e valor por contato muito maior."),
        ("Vale a pena investir em orgânico com tão pouco volume de busca?",
         "Em B2B, o número de buscas importa menos que quem está buscando. Uma busca por integração de "
         "plataforma vinda de um operador tem valor incomparável a mil visitas sem intenção. O trabalho é "
         "cobrir um conjunto pequeno de buscas com profundidade."),
        ("Traduzir o site em inglês para português resolve?",
         "Raramente. Tradução preserva o texto e perde a busca: os termos que o mercado brasileiro usa não "
         "são a tradução literal dos termos em inglês. Localização começa por pesquisar como se pesquisa "
         "aqui, e às vezes conclui que a estrutura de páginas precisa ser outra."),
        ("Como o conteúdo B2B gera contato?",
         "Não por botão de compra. Gera por material que demonstra competência técnica — documentação clara, "
         "explicação de integração, comparação honesta de abordagens — e por caminhos de contato adequados "
         "a decisão corporativa, com formulário de qualificação em vez de conversa imediata."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para bets", f"{BASE_URL}/seo-para-bets/"),
                           ("SEO para iGaming", canonical)]),
        schema_service("SEO para iGaming",
                       "SEO B2B para plataformas, provedores e fornecedores do setor de iGaming, incluindo "
                       "localização de conteúdo para o mercado brasileiro.",
                       canonical, tipo="SEO B2B para iGaming"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para bets", "/seo-para-bets/"),
                              ("SEO para iGaming", canonical)])

    corpo = hero(
        trilha,
        "B2B · expansão para o Brasil",
        "SEO para iGaming: poucas buscas, cada uma valendo muito",
        "Fornecedor de tecnologia não disputa volume — disputa as buscas específicas que um operador faz "
        "antes de escolher com quem integrar.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#b2b", "Ver o que muda no B2B"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "O recorte",
        "Este cluster é B2B, não B2C",
        tabela(
            ["", "SEO para bets (B2C)", "SEO para iGaming (B2B)"],
            [
                ["Quem pesquisa", "apostador", "operador, plataforma, investidor"],
                ["Volume de busca", "muito alto", "baixo e específico"],
                ["Concorrência orgânica", "massiva", "moderada, e pouco explorada"],
                ["Ciclo de decisão", "imediato", "meses, com várias pessoas envolvendo"],
                ["Valor por contato", "baixo, no volume", "alto, no contrato"],
                ["Conteúdo que funciona", "categoria e comparativo", "técnico, documentação, integração"],
                ["Conversão", "cadastro", "formulário de qualificação e reunião"],
            ],
            nota="A mesma empresa pode precisar das duas frentes — mas com páginas e conteúdos separados.",
        ),
        "b2b",
        desc="A confusão entre os dois é o erro mais caro deste setor: fornecedor B2B produzindo conteúdo "
             "de apostador, e disputando um volume que não vai converter em contrato nenhum.",
    )

    corpo += sec_split(
        "Quem é atendido",
        "Empresas de tecnologia e serviço do setor",
        """          <p>O perfil deste cluster é a empresa que <strong>vende para quem opera</strong>, e não
          para quem aposta:</p>
"""
        + lista([
            "<strong>Provedores de jogo</strong> — desenvolvedores de conteúdo e mecânicas licenciadas para operadores.",
            "<strong>Plataformas</strong> — sistemas que sustentam a operação, integração e gestão.",
            "<strong>Meios de pagamento</strong> — soluções de processamento e conciliação para o setor.",
            "<strong>Sistemas de CRM e retenção</strong> — ferramentas de relacionamento e automação.",
            "<strong>Programas de afiliação</strong> — plataformas de gestão e rastreamento de parceiros.",
            "<strong>Serviços especializados</strong> — consultorias, fornecedores de dados e integradores.",
        ])
        + """
          <p>Muitas dessas empresas são estrangeiras estruturando presença no Brasil, e chegam com um site
          em inglês e uma tradução automática do conteúdo. É quase sempre o ponto de partida errado — pelo
          motivo explicado na seção seguinte.</p>""",
        """<h3>O que costuma faltar</h3>
          <ul class="audit-list">
            <li>Conteúdo em português pensado para o Brasil</li>
            <li>Páginas por solução, não só institucional</li>
            <li>Material técnico público e indexável</li>
            <li>Documentação acessível sem cadastro</li>
            <li>Caminho de contato adequado a B2B</li>
          </ul>
          <p style="margin-top:1rem;">São lacunas comuns — e é por isso que a disputa orgânica neste recorte
          costuma ser menos acirrada que no B2C.</p>""",
        "quem-igaming-titulo",
    )

    corpo += sec_split(
        "Localização",
        "Por que traduzir o site não resolve",
        """          <p>Tradução e localização não são a mesma coisa, e a diferença aparece exatamente onde
          importa para busca.</p>
          <p><strong>Tradução</strong> mantém a estrutura e troca o idioma. O texto fica correto e o site
          continua invisível, porque os termos que o mercado brasileiro digita não são a tradução literal
          dos termos usados lá fora. Boa parte do vocabulário técnico do setor circula em inglês mesmo no
          Brasil, mas nem todo ele — e adivinhar quais é o trabalho.</p>
          <p><strong>Localização</strong> começa pela pesquisa: como o operador brasileiro descreve o que
          procura, quais termos ele usa em português e quais mantém em inglês, e o que a concorrência local
          já ocupa. Só depois se decide o que traduzir, o que reescrever e o que criar do zero.</p>
          <p>Com frequência a conclusão é que a estrutura de páginas precisa ser diferente da matriz — o
          que costuma exigir uma conversa com a sede antes de começar.</p>""",
        """<h3>Etapas da localização</h3>
          <ul class="audit-list">
            <li>Pesquisa de como se busca no Brasil</li>
            <li>Mapeamento do vocabulário real do setor</li>
            <li>Leitura da concorrência local</li>
            <li>Decisão de estrutura de páginas</li>
            <li>Produção de conteúdo original em português</li>
            <li>Configuração técnica de idioma e região</li>
          </ul>""",
        "localizacao-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre iGaming")

    corpo += relacionados("Continue por aqui", [
        ("/blog/como-funciona-seo-para-igaming/", "Como funciona SEO para iGaming",
         "O artigo completo sobre a disputa B2B neste setor."),
        ("/blog/seo-no-brasil-para-empresas-estrangeiras-de-igaming/", "Empresa estrangeira no Brasil",
         "O que muda ao estruturar presença orgânica em português."),
        ("/seo-para-negocios-digitais/", "SEO para negócios digitais",
         "A visão geral de aquisição orgânica para plataforma e produto digital."),
    ])

    corpo += cta_final(
        "Quer mapear as buscas B2B do seu segmento?",
        "Na análise eu levanto como o mercado brasileiro pesquisa a sua solução, o que a concorrência local "
        "já ocupa e qual estrutura de conteúdo faz sentido — com escopo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Trabalho com iGaming B2B e quero avaliar um projeto de SEO.",
        float_aria="Falar sobre SEO para iGaming pelo WhatsApp",
    )


# ============================================================
# C3 — /seo-para-afiliados-de-apostas/
# ============================================================

def c3_afiliados():
    slug = "seo-para-afiliados-de-apostas"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para afiliados de apostas: portais e reviews | RCB"
    desc = ("Arquitetura de portal de afiliado: categorias, reviews, comparativos, bônus e "
            "rastreamento. Como competir nacionalmente por tráfego orgânico.")
    page_id = "afiliados-apostas"

    faq = [
        ("Portal de afiliado ainda consegue competir?",
         "Consegue, mas não com conteúdo raso. O que perdeu espaço foi o site de review superficial, feito "
         "em massa. O que sustenta posição é cobertura profunda, informação verificável e atualização "
         "constante — que é justamente o que dá trabalho e afasta concorrente."),
        ("Quantas páginas um portal precisa ter?",
         "Não é uma questão de quantidade, e sim de cobertura de estrutura: as categorias que importam, "
         "uma página por casa avaliada, comparativos que respondam às decisões reais e conteúdo "
         "informacional que sustente autoridade temática. O número sai daí."),
        ("Como evitar que as páginas concorram entre si?",
         "Com hierarquia definida antes de publicar. Cada página precisa de uma intenção própria e um "
         "termo-alvo próprio. Review, comparativo e página de bônus da mesma casa são conteúdos distintos "
         "— quando viram três textos parecidos, o site compete consigo mesmo."),
        ("Preciso atualizar o conteúdo com que frequência?",
         "Neste nicho, mais que na média. Condições, ofertas e disponibilidade mudam, e conteúdo "
         "desatualizado perde posição e credibilidade ao mesmo tempo. Um calendário de revisão faz parte "
         "do projeto, não é opcional."),
        ("Como o rastreamento de conversão é feito?",
         "Com eventos por página e por elemento, para você saber qual conteúdo gera clique qualificado e "
         "não só visita. Isso permite investir onde há retorno, em vez de distribuir esforço igualmente "
         "por todo o site."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para bets", f"{BASE_URL}/seo-para-bets/"),
                           ("SEO para afiliados de apostas", canonical)]),
        schema_service("SEO para afiliados de apostas",
                       "Estratégia e arquitetura de conteúdo para portais de afiliado do setor de apostas: "
                       "categorias, avaliações, comparativos, conteúdo informacional e rastreamento.",
                       canonical, tipo="SEO para portais de afiliado"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para bets", "/seo-para-bets/"),
                              ("Afiliados de apostas", canonical)])

    corpo = hero(
        trilha,
        "Portais de conteúdo",
        "SEO para afiliados de apostas: o site é o negócio inteiro",
        "Em portal de afiliado não existe outro canal para compensar. Ou a arquitetura de conteúdo "
        "sustenta posição, ou não há operação.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#arquitetura", "Ver a arquitetura recomendada"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O modelo",
        "Por que afiliado é um projeto de SEO diferente de operador",
        """          <p>Um operador tem marca, produto e outros canais. Se o orgânico vai mal, ele compensa em
          outro lugar. <strong>Um portal de afiliado não tem esse colchão</strong>: o tráfego orgânico é a
          receita, e a arquitetura do site é a operação.</p>
          <p>Isso muda as prioridades. Em vez de sustentar uma marca, o trabalho é <strong>cobrir um mercado
          por completo</strong> — todas as decisões que o usuário toma antes de escolher, cada uma com a
          página adequada. Em vez de campanhas, ritmo constante de publicação e revisão.</p>
          <p>E muda o risco: portal que depende de poucas páginas de alto volume fica exposto a qualquer
          oscilação. A arquitetura correta distribui a receita por muitos conteúdos, para que nenhuma
          mudança isolada derrube a operação inteira.</p>""",
        """<h3>O que sustenta um portal</h3>
          <ul class="audit-list">
            <li>Cobertura ampla, não páginas isoladas</li>
            <li>Informação verificável e atualizada</li>
            <li>Estrutura que facilita comparação</li>
            <li>Ritmo constante de revisão</li>
            <li>Receita distribuída por muitas páginas</li>
          </ul>
          <p style="margin-top:1rem;">Quem depende de três páginas para faturar tem um problema de modelo,
          não de SEO.</p>""",
        "modelo-titulo",
    )

    corpo += sec_texto(
        "Arquitetura",
        "As camadas de um portal que funciona",
        tabela(
            ["Camada", "Função", "Intenção que atende", "Frequência de revisão"],
            [
                ["Categorias", "organizar o mercado por tipo", "quem explora opções", "baixa"],
                ["Avaliações", "uma página por casa avaliada", "quem já tem candidato em mente", "alta"],
                ["Comparativos", "confronto direto entre opções", "quem está decidindo", "alta"],
                ["Bônus e condições", "condições vigentes e regras", "quem busca oferta específica", "muito alta"],
                ["Conteúdo informacional", "explicar funcionamento e conceitos", "quem está aprendendo", "baixa"],
                ["Conteúdo de calendário", "eventos e datas do setor", "busca sazonal", "por evento"],
            ],
            nota="Cada camada tem termo-alvo próprio. Sobreposição entre camadas é a principal causa de canibalização interna.",
        ),
        "arquitetura",
        desc="A ordem de construção não é a ordem da tabela: começa pelas camadas de decisão, que convertem, "
             "e depois se expande para as que trazem volume e sustentam autoridade temática.",
    )

    corpo += sec_split(
        "Conteúdo",
        "O que diferencia review que ranqueia de review que não ranqueia",
        """          <p>Página de avaliação é o formato mais copiado — e mais mal executado — do nicho. O que
          separa uma que sustenta posição:</p>
"""
        + lista([
            "<strong>Critério explícito.</strong> Dizer como a avaliação foi feita e o que foi considerado. "
            "Sem isso, é opinião sem lastro, e o leitor percebe.",
            "<strong>Informação que só existe ali.</strong> Detalhe de funcionamento, condição específica, "
            "observação prática — algo que não está na página oficial nem em todos os concorrentes.",
            "<strong>Pontos negativos de verdade.</strong> Review que só elogia não convence ninguém e não "
            "diferencia. Apontar limitações aumenta credibilidade e tempo de permanência.",
            "<strong>Estrutura para comparação.</strong> Tabela com os itens que o leitor quer confrontar, "
            "no formato em que ele quer ver.",
            "<strong>Data de atualização visível.</strong> Neste nicho o leitor procura por isso, e o "
            "conteúdo desatualizado é descartado rápido.",
            "<strong>Comunicação sóbria.</strong> Informar sem apelo ao jogo e sem promessa de ganho — "
            "postura correta e conteúdo mais durável quando as regras de publicidade mudam.",
        ])
        + """
          <p>Nenhum desses pontos é sobre palavra-chave. São sobre ser efetivamente a melhor resposta —
          que é o que a disputa neste nicho passou a exigir.</p>""",
        NOTA_REGULATORIA,
        "conteudo-afiliado-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre portais de afiliado")

    corpo += relacionados("Continue por aqui", [
        ("/criacao-de-site-para-afiliado-de-bet/", "Criação do site",
         "A construção técnica: estrutura de conteúdo, tabelas, filtros e escalabilidade."),
        ("/blog/como-criar-paginas-de-avaliacao-de-casas-de-apostas/", "Páginas de avaliação",
         "O passo a passo de uma página de review que sustenta posição."),
        ("/link-building-para-bets/", "Link building",
         "Como construir autoridade em um dos nichos mais disputados do país."),
    ])

    corpo += cta_final(
        "Quer estruturar ou reestruturar seu portal?",
        "Na análise eu avalio a arquitetura atual, identifico canibalização entre páginas e devolvo o plano "
        "de estrutura e conteúdo — com escopo, prazo estimado e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/criacao-de-site-para-afiliado-de-bet/", "Preciso construir o site"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Tenho um portal de afiliado e quero avaliar o projeto de SEO.",
        float_aria="Falar sobre SEO para portal de afiliado pelo WhatsApp",
    )


# ============================================================
# C4 — /criacao-de-site-para-afiliado-de-bet/
# ============================================================

def c4_criacao_site_afiliado():
    slug = "criacao-de-site-para-afiliado-de-bet"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Criação de site para afiliado de bet | RCB Consultoria"
    desc = ("Site de afiliado construído para escalar: estrutura de conteúdo, comparativos, tabelas, "
            "filtros e CTAs. Preparado para SEO desde o início.")
    page_id = "site-afiliado-bet"

    faq = [
        ("Que tipo de estrutura é usada?",
         "A escolha depende do volume de conteúdo previsto e de quem vai manter o site. O critério é que a "
         "estrutura suporte crescer para centenas de páginas sem virar bagunça, permita publicar sem "
         "depender de desenvolvedor e não sacrifique desempenho."),
        ("Dá para migrar meu portal atual sem perder posições?",
         "Migração sempre envolve risco, e quem diz o contrário não está sendo honesto. O que reduz o risco "
         "é planejamento: mapeamento completo de endereços, redirecionamentos corretos e monitoramento "
         "depois da troca. Veja migração de domínio e SEO."),
        ("Como as tabelas comparativas são construídas?",
         "Como conteúdo estruturado, não como imagem ou texto solto. Isso permite atualizar em um lugar só, "
         "reaproveitar a mesma informação em páginas diferentes e manter tudo legível no celular — onde "
         "está a maior parte do acesso."),
        ("O rastreamento de cliques vem configurado?",
         "Sim. Eventos por página e por elemento, para separar o conteúdo que gera clique qualificado do "
         "que só gera visita. Sem isso não dá para decidir onde investir conteúdo."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para afiliados de apostas", f"{BASE_URL}/seo-para-afiliados-de-apostas/"),
                           ("Criação de site para afiliado", canonical)]),
        schema_service("Criação de site para afiliado de bet",
                       "Desenvolvimento de portal de afiliado do setor de apostas: estrutura de conteúdo "
                       "escalável, comparativos, tabelas, filtros, CTAs e rastreamento.",
                       canonical, tipo="Criação de site"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Afiliados de apostas", "/seo-para-afiliados-de-apostas/"),
                              ("Criação de site", canonical)])

    corpo = hero(
        trilha,
        "Desenvolvimento",
        "Criação de site para afiliado de bet: construído para chegar a centenas de páginas",
        "Portal de afiliado cresce rápido. Se a estrutura não foi pensada para isso, a reforma chega "
        "junto com o primeiro resultado — e custa mais que ter feito certo.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/seo-para-afiliados-de-apostas/", "Ver a estratégia de conteúdo"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O erro fundador",
        "Site montado para dez páginas, que precisa comportar trezentas",
        """          <p>Quase todo portal de afiliado começa pequeno: algumas avaliações, um comparativo, um
          punhado de textos. A estrutura escolhida nessa fase costuma ser a mais simples possível — e é
          exatamente ela que trava o projeto seis meses depois.</p>
          <p>Os sintomas são previsíveis: categorias improvisadas porque não havia hierarquia, a mesma
          informação repetida manualmente em vinte páginas, tabelas que precisam ser editadas uma a uma
          quando uma condição muda, e endereços inconsistentes porque cada página nova foi criada de um
          jeito.</p>
          <p>Nada disso é problema de conteúdo. É de arquitetura — e resolver depois significa reorganizar
          o site inteiro, com risco de perder o que já foi conquistado.</p>""",
        """<h3>Decisões que precisam vir antes</h3>
          <ul class="audit-list">
            <li>Hierarquia de categorias e subcategorias</li>
            <li>Padrão de endereços das páginas</li>
            <li>Onde a informação repetida fica armazenada</li>
            <li>Como as tabelas são geradas e atualizadas</li>
            <li>Regras de link interno entre camadas</li>
            <li>O que é indexável e o que não é</li>
          </ul>""",
        "erro-titulo",
    )

    corpo += sec_texto(
        "O que é construído",
        "Componentes de um portal que escala",
        cards([
            (None, "Estrutura de conteúdo",
             "Hierarquia de categorias, avaliações e comparativos definida antes da primeira página, com "
             "padrão de endereços consistente.", None),
            (None, "Tabelas comparativas",
             "Conteúdo estruturado, atualizado em um lugar só e reaproveitado em várias páginas — "
             "responsivo, com rolagem própria no celular.", None),
            (None, "Filtros e navegação",
             "Formas de o visitante encontrar o que procura, com regras claras sobre o que gera página "
             "indexável e o que é só navegação.", None),
            (None, "Componentes de conversão",
             "Blocos de chamada padronizados, posicionados por tipo de página, todos com rastreamento "
             "próprio de origem.", None),
            (None, "Desempenho",
             "Páginas de conteúdo pesado que continuam rápidas no celular — carregamento diferido de "
             "imagem e ausência de excesso de biblioteca externa.", None),
            (None, "Base de SEO técnico",
             "Canonical, dados estruturados, hierarquia de títulos e controle de indexação resolvidos na "
             "construção, não depois.", None),
        ]),
        "componentes-titulo",
    )

    corpo += sec_split(
        "Manutenção",
        "O custo que ninguém calcula no começo",
        """          <p>A parte mais subestimada de um portal de afiliado não é construir — é
          <strong>manter atualizado</strong>. Condições mudam, ofertas terminam, casas entram e saem do
          mercado. Um portal com cem avaliações desatualizadas vale menos que um com trinta corretas.</p>
          <p>Por isso a construção decide, desde o início, onde cada informação volátil fica guardada. Se o
          dado de uma casa está escrito manualmente em quinze páginas, atualizar significa quinze edições —
          e na prática significa que não vai ser atualizado.</p>
          <p>A estrutura correta guarda esse dado em um lugar só e o exibe onde for necessário. Uma edição
          atualiza o site inteiro. É o que torna a manutenção viável no volume em que esses portais operam.</p>""",
        """<h3>Reduzindo o custo de manutenção</h3>
          <ul class="audit-list">
            <li>Informação volátil armazenada uma única vez</li>
            <li>Tabelas geradas a partir dessa fonte</li>
            <li>Data de atualização automática</li>
            <li>Calendário de revisão por camada</li>
            <li>Alerta de conteúdo antigo demais</li>
          </ul>
          <p style="margin-top:1rem;">Decisões de construção que se pagam já no segundo trimestre de operação.</p>""",
        "manutencao-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre a construção do portal")

    corpo += relacionados("Continue por aqui", [
        ("/seo-para-afiliados-de-apostas/", "Estratégia para afiliados",
         "A arquitetura de conteúdo que o site precisa sustentar."),
        ("/blog/como-criar-site-para-afiliado-de-apostas/", "Como criar o site do zero",
         "O passo a passo, incluindo o que decidir antes da primeira página."),
        ("/migracao-de-dominio-seo/", "Migração de domínio",
         "Se o portal já existe e vai trocar de endereço ou plataforma."),
    ])

    corpo += cta_final(
        "Vai construir ou reconstruir seu portal?",
        "Na análise definimos a arquitetura, o escopo de construção e o plano de crescimento — incluindo "
        "o que aproveitar, se já existe site no ar.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero construir um portal de afiliado e avaliar o projeto.",
        float_aria="Falar sobre criação de portal de afiliado pelo WhatsApp",
    )


# ============================================================
# C5 — /link-building-para-bets/
# ============================================================

def c5_link_building_bets():
    slug = "link-building-para-bets"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Link building para bets e iGaming | RCB Consultoria"
    desc = ("Construção de autoridade em um dos nichos mais disputados: relevância, análise de risco, "
            "ritmo controlado e acompanhamento dos domínios de referência.")
    page_id = "link-building-bets"

    faq = [
        ("Por que link building neste setor é tão caro?",
         "Porque a demanda é altíssima e o conjunto de veículos relevantes é limitado. Muitos sites cobram "
         "valores elevados justamente por saberem disso. Isso torna o critério de seleção mais importante "
         "aqui que em qualquer outro nicho — pagar caro por fonte irrelevante é o desperdício mais comum."),
        ("Dá para competir sem investir pesado em autoridade?",
         "Em termos principais, dificilmente. Em recortes específicos e conteúdo de cauda longa, sim — e é "
         "por aí que projetos novos costumam entrar, acumulando relevância antes de disputar o topo."),
        ("Como saber se um veículo vale o que cobra?",
         "Olhando se ele tem tráfego próprio, se o conteúdo é real, se a relevância temática é genuína e "
         "como é o perfil de links de saída. Site que vende link para qualquer tema entrega pouco, "
         "independentemente da métrica de autoridade que apresente."),
        ("A RCB trabalha com PBN neste setor?",
         "Não. É explicado no conteúdo do site porque os clientes perguntam, mas não é executado. O risco "
         "fica com o domínio do cliente, e projetos deste setor costumam envolver investimento alto demais "
         "para serem construídos sobre base frágil."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para bets", f"{BASE_URL}/seo-para-bets/"),
                           ("Link building para bets", canonical)]),
        schema_service("Link building para bets e iGaming",
                       "Construção de autoridade para projetos do setor de apostas e iGaming, com critério "
                       "de relevância, análise de risco e ritmo controlado.",
                       canonical, tipo="Link building"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"), ("SEO para bets", "/seo-para-bets/"),
                              ("Link building", canonical)])

    corpo = hero(
        trilha,
        "Construção de autoridade",
        "Link building para bets: onde a maior parte da verba do setor é desperdiçada",
        "É a frente que decide as posições de topo neste mercado — e a que mais recebe proposta de "
        "quantidade em vez de critério.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/link-building-para-nichos-competitivos/", "Ver a metodologia completa"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O mercado de links do setor",
        "Muita oferta, pouca relevância",
        """          <p>Existe um mercado ativo e caro de venda de links neste setor. Quem opera um projeto aqui
          recebe propostas constantes: pacotes por quantidade, listas de sites com métricas altas, promessas
          de posicionamento rápido.</p>
          <p>O problema é que <strong>métrica alta não é o mesmo que relevância</strong>. Boa parte desses
          veículos existe para vender link: publicam sobre qualquer assunto, têm pouco ou nenhum tráfego
          próprio e mantêm um perfil de saída que denuncia o modelo. Um link desses custa caro e entrega
          pouco — e, somados, formam um padrão que é passivo, não patrimônio.</p>
          <p>A abordagem aqui é inversa: menos fontes, escolhidas por critério, com verba concentrada onde
          há relevância temática real e tráfego verificável.</p>""",
        """<h3>Sinais de veículo que não vale</h3>
          <ul class="audit-list">
            <li>Publica sobre qualquer assunto sem linha editorial</li>
            <li>Métrica de autoridade alta e tráfego quase nulo</li>
            <li>Muitos links de saída para nichos sem relação</li>
            <li>Conteúdo visivelmente produzido só para hospedar link</li>
            <li>Oferta de pacote por quantidade</li>
          </ul>
          <p style="margin-top:1rem;">Nenhum desses sinais aparece na planilha que acompanha a proposta.</p>""",
        "mercado-titulo",
    )

    corpo += sec_texto(
        "Critério",
        "Como cada fonte é avaliada",
        problem_cards([
            ("Relevância temática",
             "A proximidade de assunto entre o veículo e o projeto é o fator de maior peso. Um link de "
             "contexto realmente relacionado vale mais que vários de sites genéricos com métrica melhor."),
            ("Tráfego real",
             "Site que ninguém visita entrega pouco, por melhor que pareça em ferramenta. A verificação "
             "de audiência própria é parte da triagem, não detalhe."),
            ("Perfil de saída",
             "Para onde aquele site aponta revela o modelo dele. Muitos links de saída para nichos "
             "desconexos indicam venda em massa — e associação a esse padrão não interessa ao projeto."),
            ("Contexto do link",
             "Menção dentro de conteúdo que faz sentido rende diferente de link em rodapé ou em lista. "
             "O contexto é negociado, não aceito como vier."),
        ]),
        "criterio-titulo", classe="problem-section",
        desc="Fonte que não passa nesses quatro filtros não entra no plano, mesmo quando o preço é "
             "convidativo — principalmente quando é.",
    )

    corpo += sec_split(
        "Ritmo e risco",
        "Por que a construção é gradual",
        """          <p>Aquisição em lote cria padrão detectável. Um site que passa de poucos domínios de
          referência para muitos em pouco tempo, com âncoras concentradas nos termos que quer ranquear,
          exibe exatamente o perfil que sistemas antisspam procuram.</p>
          <p>A construção segue um ritmo compatível com o crescimento do projeto: mais lenta enquanto o
          site é novo e tem pouco conteúdo, acelerando conforme ele acumula material que justifique a
          referência. Isso alonga o prazo e é a razão de a autoridade ser o principal fator de tempo em
          projetos deste setor.</p>
          <p>A distribuição de âncoras segue a mesma lógica: mistura de marca, endereço, termos genéricos
          e variações. Concentrar no termo exato é o erro mais fácil de cometer e o mais fácil de detectar.</p>""",
        """<h3>Relatório do serviço</h3>
          <ul class="audit-list">
            <li>Domínios conquistados, com endereço de cada um</li>
            <li>Contexto de cada menção</li>
            <li>Distribuição de âncoras acumulada</li>
            <li>Evolução do total de domínios de referência</li>
            <li>Comparação com os concorrentes-alvo</li>
            <li>Fontes descartadas e o motivo</li>
          </ul>
          <p style="margin-top:1rem;">Sem promessa de quantidade fixa e sem métrica proprietária sem
          explicação.</p>""",
        "ritmo-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre autoridade no setor")

    corpo += relacionados("Continue por aqui", [
        ("/link-building-para-nichos-competitivos/", "Metodologia completa",
         "Como a construção de autoridade funciona em projetos nacionais e disputados."),
        ("/consultoria-de-backlinks/", "Auditoria do perfil atual",
         "Quando o problema é o que já está apontando para o seu site."),
        ("/blog/quanto-custa-um-backlink-de-qualidade/", "Quanto custa um backlink",
         "O que forma o preço e por que o mais caro nem sempre é o melhor."),
    ])

    corpo += cta_final(
        "Quer saber quanta autoridade o seu alvo exige?",
        "Na análise eu levanto o perfil de links de quem ocupa as posições que você quer, comparo com o seu "
        "e devolvo um plano com critério de seleção e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/seo-para-bets/", "Ver o projeto completo"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar a construção de autoridade do meu projeto no setor.",
        float_aria="Falar sobre link building para bets pelo WhatsApp",
    )


# ============================================================
# C6 — /seo-para-jogos-online/
# ============================================================

def c6_jogos_online():
    slug = "seo-para-jogos-online"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "SEO para jogos online e portais de games | RCB"
    desc = ("Aquisição orgânica para plataformas de jogos, portais e apps: ciclo de lançamento, "
            "conteúdo de comunidade e disputa nacional por tráfego.")
    page_id = "jogos-online"

    faq = [
        ("Este cluster é sobre apostas?",
         "Não. Esta página trata de jogos digitais, portais de games, plataformas e aplicativos de "
         "entretenimento. O setor de apostas tem páginas próprias, com público e disputa diferentes."),
        ("Como aproveitar o pico de um lançamento?",
         "Publicando antes dele. Página nova raramente ranqueia a tempo de pegar a janela de pico, que "
         "costuma durar pouco. O conteúdo precisa estar indexado e já acumulando sinais quando o interesse "
         "chega — o que significa planejar por calendário, não por notícia."),
        ("Conteúdo de comunidade ajuda no posicionamento?",
         "Ajuda de forma indireta e consistente. Guias, dúvidas e conteúdo de uso capturam buscas muito "
         "específicas, com pouca disputa, e sustentam relevância temática. Somados, costumam superar o "
         "tráfego dos termos principais."),
        ("Portal de games consegue competir com sites grandes?",
         "Em termos amplos, dificilmente no começo. Em recortes específicos — um jogo, uma mecânica, um "
         "problema técnico — sim, e é o caminho usual: acumular cobertura em nichos que os grandes "
         "atendem superficialmente."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("SEO para jogos online", canonical)]),
        schema_service("SEO para jogos online",
                       "Aquisição orgânica para plataformas de jogos, portais de games e aplicativos: "
                       "ciclo de lançamento, conteúdo de comunidade e arquitetura de conteúdo.",
                       canonical, tipo="SEO para jogos online"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Jogos online", canonical)])

    corpo = hero(
        trilha,
        "Games e entretenimento digital",
        "SEO para jogos online: o tráfego está nas perguntas específicas",
        "Portais de games perdem tempo disputando termos amplos contra veículos gigantes. O volume que "
        "sustenta um projeto está nas dúvidas que ninguém respondeu direito.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/seo-para-negocios-digitais/", "Ver negócios digitais"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "Quem é atendido",
        "Operações deste cluster",
        cards([
            (None, "Plataformas de jogos",
             "Serviços com catálogo próprio, assinatura ou acesso a biblioteca de títulos.", None),
            (None, "Portais e sites de games",
             "Veículos de conteúdo sobre jogos, monetizados por audiência, parceria ou afiliação.", None),
            (None, "Aplicativos e jogos móveis",
             "Operações cuja descoberta passa pela busca na web antes da instalação, e não só pelas lojas.", None),
            (None, "Jogos por assinatura",
             "Modelos recorrentes, em que retenção pesa tanto quanto aquisição.", None),
            (None, "Estúdios e lançamentos",
             "Projetos com data marcada, que precisam de presença construída antes do pico de interesse.", None),
            (None, "Comunidades e serviços",
             "Ferramentas, servidores e serviços em torno de jogos, com público altamente específico.", None),
        ]),
        "quem-jogos-titulo", classe="cluster-section",
    )

    corpo += sec_split(
        "Estratégia",
        "Por que a cauda longa carrega este nicho",
        """          <p>Termos amplos de games são disputados por veículos com anos de acúmulo e equipes
          grandes. Entrar por ali é caro e lento. Mas o comportamento de busca deste público abre uma porta
          que poucos nichos oferecem.</p>
          <p>Quem joga pesquisa de forma <strong>extremamente específica</strong>: como resolver uma
          situação, onde encontrar um item, por que um erro acontece, qual configuração usar. São milhares
          de buscas de baixo volume individual e disputa quase nula — que, somadas, superam com folga o
          tráfego dos termos principais.</p>
          <p>A estratégia é construir cobertura nesses recortes, acumular relevância temática e só então
          disputar os termos amplos, já com autoridade acumulada. É mais lento de explicar e mais rápido de
          acontecer que o caminho inverso.</p>""",
        """<h3>Tipos de busca que rendem</h3>
          <ul class="audit-list">
            <li>Como fazer algo específico dentro do jogo</li>
            <li>Solução de erro e problema técnico</li>
            <li>Requisitos e compatibilidade</li>
            <li>Comparação entre títulos ou versões</li>
            <li>Guias de progressão e mecânica</li>
            <li>Dúvidas sobre assinatura e acesso</li>
          </ul>""",
        "estrategia-jogos-titulo",
    )

    corpo += sec_split(
        "Lançamento",
        "A janela que quase todo mundo perde",
        """          <p>Lançamento gera pico de busca previsível e curto. E a maior parte dos sites publica no
          dia — quando já é tarde.</p>
          <p>Página nova raramente ranqueia a tempo: leva dias ou semanas para ser avaliada, e o pico
          costuma durar menos que isso. Quem aparece na janela é quem já tinha conteúdo publicado e
          indexado antes, acumulando sinais enquanto o interesse crescia.</p>
          <p>Na prática, isso significa trabalhar por calendário: mapear datas conhecidas com antecedência,
          publicar conteúdo preparatório semanas antes e expandi-lo conforme a informação oficial aparece.
          O conteúdo evolui na mesma URL, em vez de nascer no dia do pico.</p>
          <p>É a mesma lógica de <a href="/seo-para-streaming-e-tv-online/">plataformas de streaming</a> —
          e um dos poucos lugares em SEO onde antecedência vale mais que qualidade de última hora.</p>""",
        """<h3>Calendário de lançamento</h3>
          <ul class="audit-list">
            <li>Mapeamento de datas com antecedência</li>
            <li>Conteúdo preparatório publicado antes</li>
            <li>Expansão na mesma URL, sem página nova</li>
            <li>Cobertura de dúvidas do pós-lançamento</li>
            <li>Revisão quando o interesse se estabiliza</li>
          </ul>""",
        "lancamento-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre jogos online")

    corpo += relacionados("Continue por aqui", [
        ("/blog/como-posicionar-portal-de-jogos-online/", "Como posicionar um portal de jogos",
         "A estratégia completa, do recorte inicial à disputa dos termos amplos."),
        ("/seo-para-negocios-digitais/", "SEO para negócios digitais",
         "Aquisição orgânica para produto digital, plataforma e assinatura."),
        ("/seo-para-streaming-e-tv-online/", "Streaming e TV online",
         "Ciclo de lançamento e retenção em plataformas de conteúdo."),
    ])

    corpo += cta_final(
        "Quer mapear onde está o tráfego do seu nicho?",
        "Na análise eu levanto os recortes de busca com demanda real e baixa disputa no seu segmento, e "
        "devolvo o plano de cobertura — com escopo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Tenho um projeto na área de jogos e quero avaliar SEO.",
        float_aria="Falar sobre SEO para jogos online pelo WhatsApp",
    )


PAGINAS = [c1_seo_para_bets, c2_igaming, c3_afiliados, c4_criacao_site_afiliado,
           c5_link_building_bets, c6_jogos_online]
