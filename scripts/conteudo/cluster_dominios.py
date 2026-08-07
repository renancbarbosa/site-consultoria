# -*- coding: utf-8 -*-
"""
Cluster D — domínios, autoridade e recuperação.

D1 /analise-de-dominios-expirados/
D2 /migracao-de-dominio-seo/            (absorve a migração específica de IPTV)
D3 /link-building-para-nichos-competitivos/
D4 /consultoria-de-backlinks/
D5 /recuperacao-de-trafego-organico/

Separações que evitam canibalização (plano §3):
  D1 avalia domínio ANTES da compra   ×  D2 troca de endereço de um site existente
  D3 CONSTRÓI autoridade nova         ×  D4 AUDITA a autoridade que já existe
  D2 é projeto planejado              ×  D5 é sintoma com causa desconhecida
"""
from rcb_base import (
    BASE_URL, head_comum, montar, breadcrumb_html, hero, sec_texto, sec_split,
    cards, problem_cards, passos, lista, tabela, sec_faq, cta_final,
    relacionados, grafo, schema_webpage, schema_breadcrumb, schema_service,
    schema_faq,
)

HOJE = "2026-08-06"
ANALISE = "/analise-de-projeto/"


# ============================================================
# D1 — /analise-de-dominios-expirados/
# ============================================================

def d1_analise_dominios():
    slug = "analise-de-dominios-expirados"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Análise de domínios expirados antes de comprar | RCB"
    desc = ("Triagem e análise de domínios expirados: histórico, perfil de links, relevância e risco. "
            "Recomendação objetiva antes de você comprar.")
    page_id = "analise-dominios"

    faq = [
        ("Um domínio expirado garante autoridade?",
         "Não. Nenhum domínio transmite autoridade automaticamente. O que ele carrega é histórico, que pode "
         "ajudar, ser irrelevante ou atrapalhar. A diferença entre os três casos só aparece na análise — "
         "não no preço nem em uma métrica isolada."),
        ("Quanto custa um domínio expirado?",
         "Varia de valores baixos em leilão até quantias muito altas por nomes disputados. O preço reflete "
         "a percepção de valor do nome, não a qualidade do histórico. Domínio caro com passado ruim continua "
         "sendo um domínio com passado ruim."),
        ("Qual a diferença entre domínio premium e domínio expirado?",
         "Premium normalmente é um nome curto e comercialmente valioso, vendido pelo nome em si, muitas "
         "vezes sem histórico relevante. Expirado é um domínio que já foi usado e carrega passado. Um vende "
         "memorização; o outro vende histórico — e histórico exige verificação."),
        ("O domínio fica registrado em nome de quem?",
         "Do cliente, sempre. A RCB avalia e orienta a compra; o registro é feito em nome de quem contrata, "
         "com acesso completo. Domínio registrado em nome do fornecedor é um risco que não faz sentido correr."),
        ("E se a recomendação for não comprar?",
         "Acontece com frequência, e é justamente para isso que a análise existe. Sai muito mais barato "
         "descartar um domínio antes da compra do que descobrir o passivo depois de construir um projeto em cima."),
        ("Vocês analisam um domínio que eu já comprei?",
         "Sim. Nesse caso o objetivo muda: em vez de recomendar a compra, a análise mede o que veio junto e "
         "indica o que dá para fazer — desautorizar links problemáticos, diluir o perfil com aquisição de "
         "qualidade ou, em casos extremos, avaliar troca de domínio."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Análise de domínios expirados", canonical)]),
        schema_service("Análise de domínios expirados",
                       "Pesquisa, triagem e análise de domínios expirados: histórico de conteúdo, perfil de "
                       "links, relevância temática, sinais de spam e recomendação de compra.",
                       canonical, tipo="Análise de domínio"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Análise de domínios expirados", canonical)])

    painel = """<h2>O entregável</h2>
          <ul class="audit-list">
            <li>Histórico de conteúdo recuperado</li>
            <li>Perfil de links, com origem e padrão</li>
            <li>Relevância temática com o seu projeto</li>
            <li>Sinais de spam ou penalização</li>
            <li>Avaliação do nome em si</li>
            <li><strong>Recomendação: comprar, não comprar, ou comprar até X</strong></li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:.75rem;">Com o motivo escrito — inclusive quando a resposta é desistir.</p>"""

    corpo = hero(
        trilha,
        "Antes da compra",
        "Análise de domínios expirados: descobrir o passivo antes de pagar por ele",
        "Domínio com histórico pode encurtar caminho ou enterrar um projeto. A diferença não está no "
        "preço nem na métrica que o vendedor mostra — está no passado do domínio.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#criterios", "Ver o que é verificado"),
        painel, page_id,
    )

    corpo += sec_split(
        "O problema",
        "O que o mercado vende e o que você recebe",
        """          <p>O mercado de domínios expirados funciona com base em métricas de autoridade que
          ferramentas de terceiros calculam. Elas são úteis como triagem inicial e péssimas como critério
          de decisão — porque são <strong>estimativas, e podem ser manipuladas de propósito</strong>.</p>
          <p>É comum encontrar domínios com métrica alta cujo histórico revela outra coisa: links vindos de
          redes de sites, âncoras concentradas de forma artificial, conteúdo em outro idioma sem relação
          nenhuma com o tema, ou um período usado para spam que continua registrado publicamente.</p>
          <p>Nada disso aparece no anúncio. Aparece no histórico — que é público e verificável, mas dá
          trabalho de levantar. É esse trabalho que o serviço faz.</p>""",
        """<h3>Por que a métrica engana</h3>
          <ul class="audit-list">
            <li>É estimativa de terceiro, não dado do Google</li>
            <li>Pode ser inflada de propósito antes da venda</li>
            <li>Não distingue link legítimo de link comprado</li>
            <li>Ignora relevância temática por completo</li>
            <li>Não enxerga histórico de conteúdo</li>
          </ul>
          <p style="margin-top:1rem;">Serve para filtrar candidatos. Não serve para decidir compra.</p>""",
        "problema-titulo",
    )

    corpo += sec_texto(
        "O que é verificado",
        "Seis frentes de análise",
        cards([
            (None, "Histórico de conteúdo",
             "O que esteve publicado no domínio ao longo dos anos, recuperado de registros públicos de "
             "arquivo. Revela mudanças de tema, períodos de abandono e uso para spam.", None),
            (None, "Perfil de links",
             "Quantos domínios distintos apontam, de onde vêm, se há concentração suspeita e se o padrão "
             "sugere aquisição natural ou compra em massa.", None),
            (None, "Relevância temática",
             "Se o assunto anterior tem relação com o projeto novo. Sem proximidade de tema, o histórico "
             "entrega pouco, mesmo quando é legítimo.", None),
            (None, "Sinais de spam",
             "Âncoras artificiais, links de redes conhecidas, conteúdo problemático indexado e outros "
             "indícios de uso abusivo que ficam registrados.", None),
            (None, "Idade e continuidade",
             "Há quanto tempo o domínio existe e se ficou muito tempo parado. Períodos longos de inatividade "
             "reduzem bastante o valor do histórico.", None),
            (None, "O nome em si",
             "Se funciona comercialmente, é memorizável, não gera confusão e não carrega marca de terceiros "
             "— que seria problema jurídico, não de SEO.", None),
        ]),
        "criterios",
        desc="Nenhum item isolado decide. É o conjunto que forma a recomendação — e um único sinal grave "
             "em qualquer frente costuma bastar para descartar o candidato.",
    )

    corpo += sec_texto(
        "Como funciona",
        "Do briefing à recomendação",
        passos([
            ("Briefing", "Qual o projeto, qual o tema e o que se espera do domínio. Sem isso não há como "
                         "avaliar relevância temática."),
            ("Triagem", "Levantamento de candidatos e primeiro filtro por nome, tema aparente e sinais "
                        "grosseiros de problema."),
            ("Análise profunda", "Verificação das seis frentes nos candidatos que passaram na triagem."),
            ("Recomendação", "Parecer objetivo por domínio: comprar, não comprar ou comprar até determinado "
                             "valor — com o motivo."),
            ("Acompanhamento da compra", "Orientação no processo de aquisição e registro em nome do cliente."),
        ]),
        "processo-titulo", classe="metodo",
        desc="O serviço pode ser contratado sozinho, para um domínio específico que você já tem em vista, "
             "ou como parte de um projeto completo.",
    )

    corpo += sec_split(
        "Expectativa",
        "O que um bom domínio faz — e o que ele não faz",
        """          <p>Vale ser direto, porque a expectativa errada aqui custa caro.</p>
          <p><strong>O que um bom domínio faz:</strong> encurta parte do caminho. Um domínio com histórico
          limpo, relevância temática e links legítimos parte de uma posição melhor que um domínio
          registrado ontem. Isso é real e mensurável.</p>
          <p><strong>O que ele não faz:</strong> substituir conteúdo, substituir trabalho de autoridade
          novo ou garantir posição. Domínio é ponto de partida, não projeto. Comprar um bom domínio e não
          construir nada em cima dele não produz resultado nenhum.</p>
          <p>Há também um efeito temporal: o valor do histórico se dilui com o tempo. Se o domínio ficou
          anos parado, boa parte do que ele carregava já perdeu força — e o preço cobrado raramente
          reflete isso.</p>""",
        """<h3>Quando NÃO vale a pena</h3>
          <ul class="audit-list">
            <li>Quando o tema anterior não tem relação com o seu.</li>
            <li>Quando o perfil de links é claramente artificial.</li>
            <li>Quando há histórico de spam identificado.</li>
            <li>Quando o preço supera o custo de construir do zero.</li>
            <li>Quando o nome não serve comercialmente.</li>
          </ul>
          <p style="margin-top:1rem;">Na dúvida entre um domínio duvidoso e um domínio novo, o novo costuma
          ser a escolha mais barata no fim das contas.</p>""",
        "expectativa-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre domínios expirados")

    corpo += relacionados("Continue por aqui", [
        ("/blog/dominio-expirado-ainda-funciona-para-seo/", "Domínio expirado ainda funciona?",
         "O que mudou, o que sobrou e onde ainda faz diferença."),
        ("/blog/como-saber-se-dominio-expirado-foi-usado-para-spam/", "Como identificar spam",
         "Os sinais que aparecem no histórico e como verificá-los."),
        ("/blog/dominio-premium-ou-dominio-expirado/", "Premium ou expirado?",
         "A comparação entre pagar pelo nome e pagar pelo histórico."),
    ])

    corpo += cta_final(
        "Tem um domínio em vista?",
        "Envie o domínio na análise do projeto. Você recebe o parecer com histórico, perfil de links, risco "
        "e recomendação objetiva — antes de gastar.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/migracao-de-dominio-seo/", "Já tenho site e vou trocar de domínio"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero analisar um domínio expirado antes de comprar.",
        float_aria="Solicitar análise de domínio expirado pelo WhatsApp",
    )


# ============================================================
# D2 — /migracao-de-dominio-seo/
# ============================================================

def d2_migracao_dominio():
    slug = "migracao-de-dominio-seo"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Migração de domínio e SEO: como trocar sem perder | RCB"
    desc = ("Troca de domínio, rebrand ou consolidação de sites com processo técnico controlado: "
            "redirecionamentos, sitemap, monitoramento e recuperação.")
    page_id = "migracao-dominio"

    faq = [
        ("Trocar de domínio faz perder posições?",
         "Costuma haver oscilação, sim, e quem promete migração sem nenhum impacto não está sendo honesto. "
         "O que um processo bem feito faz é reduzir a perda e encurtar o tempo de recuperação. O que uma "
         "migração malfeita causa é perda que pode não se recuperar."),
        ("Quanto tempo leva para o Google reconhecer o novo domínio?",
         "Varia com o tamanho do site e a frequência de rastreamento. Sites pequenos costumam estabilizar "
         "mais rápido; sites grandes levam mais tempo porque cada endereço precisa ser rastreado de novo. "
         "O monitoramento acompanha isso semana a semana."),
        ("A autoridade do domínio antigo é transferida?",
         "Parte dela tende a ser reconhecida através dos redirecionamentos, mas não é uma transferência "
         "automática nem integral. Tratar migração como se a autoridade fosse simplesmente mudar de endereço "
         "é o erro que gera as piores surpresas."),
        ("Perdi o registro do meu domínio. Dá para recuperar o SEO?",
         "Depende de conseguir o domínio de volta. Se ele foi registrado por outra pessoa, na prática o "
         "caminho é reconstruir em um novo endereço — recuperando o conteúdo, refazendo o contato com as "
         "fontes de links mais relevantes e reconstruindo autoridade."),
        ("Dá para juntar vários sites em um só?",
         "Dá, e às vezes é a decisão certa: dois ou três sites fracos disputando os mesmos termos rendem "
         "menos que um site consolidado. Exige mapeamento cuidadoso de qual conteúdo vai para onde e o que "
         "é consolidado ou descartado."),
        ("A RCB atende migração motivada por bloqueio judicial?",
         "Não. Trocar de endereço para contornar bloqueio judicial ou administrativo está fora do escopo, "
         "em qualquer nicho. O serviço atende necessidades legítimas: rebrand, mudança de marca, "
         "consolidação, troca de plataforma e perda de registro."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Migração de domínio e SEO", canonical)]),
        schema_service("Migração de domínio",
                       "Planejamento e execução técnica de troca de domínio, rebrand, consolidação de sites "
                       "e migração de plataforma, com redirecionamentos, monitoramento e recuperação.",
                       canonical, tipo="Migração de domínio"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Migração de domínio", canonical)])

    corpo = hero(
        trilha,
        "Processo técnico",
        "Migração de domínio: reduzir a perda, não fingir que ela não existe",
        "Toda troca de endereço tem impacto. A diferença entre uma oscilação de semanas e um prejuízo "
        "permanente está inteiramente no planejamento.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#processo", "Ver o processo completo"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "Situações atendidas",
        "Nem toda migração é igual",
        cards([
            (None, "Mudança de marca",
             "A empresa mudou de nome e o domínio precisa acompanhar. É o caso mais comum e o mais "
             "planejável, porque a data costuma ser conhecida com antecedência.", None),
            (None, "Troca de endereço",
             "Mudança para um domínio melhor, mais curto ou mais adequado ao mercado — incluindo migração "
             "para um domínio com histórico avaliado.", None),
            (None, "Consolidação de sites",
             "Dois ou mais sites da mesma operação disputando os mesmos termos, que fazem mais sentido "
             "reunidos em um só.", None),
            (None, "Perda de registro",
             "O domínio não foi renovado a tempo. O cenário mais difícil, porque a recuperação depende de "
             "conseguir o endereço de volta.", None),
            (None, "Troca de plataforma",
             "O domínio permanece, mas a estrutura de endereços muda. Tecnicamente parecido com migração de "
             "domínio, e igualmente arriscado sem plano.", None),
            (None, "Migração já feita sem plano",
             "A troca aconteceu, o tráfego caiu e ninguém mapeou o que quebrou. Aqui o trabalho é de "
             "diagnóstico e reparo.", None),
        ]),
        "situacoes-titulo", classe="cluster-section",
        desc="Cada situação tem risco e sequência diferentes. O que muda entre elas é o quanto dá para "
             "preparar antes — e é aí que a maior parte do resultado é decidida.",
    )

    corpo += sec_texto(
        "O processo",
        "As etapas que reduzem a perda",
        passos([
            ("Inventário", "Levantamento de todos os endereços do site atual, do que ranqueia, do que recebe "
                           "links externos e do que pode ser descartado. Migração sem inventário é migração no escuro."),
            ("Mapa de destino", "Definição de para onde cada endereço antigo aponta. Um a um, sem jogar tudo "
                                "para a página inicial — que é o erro mais destrutivo e mais frequente."),
            ("Preparação do destino", "O novo site pronto e conferido antes da virada: conteúdo, estrutura "
                                      "interna, certificado, desempenho e configuração de idioma."),
            ("Virada", "Redirecionamentos ativados, DNS e certificado ajustados, sitemap novo enviado e "
                       "propriedades de monitoramento configuradas."),
            ("Atualização externa", "Contato com as fontes de links mais relevantes para atualizar o endereço, "
                                    "e ajuste de perfis, redes e materiais próprios."),
            ("Monitoramento", "Acompanhamento semanal de indexação, erros, posições e tráfego — com correção "
                              "rápida do que aparecer quebrado."),
        ]),
        "processo", classe="metodo",
    )

    corpo += sec_split(
        "Erros",
        "O que costuma dar errado em migração",
        """          <p>Os problemas de migração se repetem tanto que dá para listá-los por ordem de frequência:</p>
"""
        + lista([
            "<strong>Redirecionar tudo para a página inicial.</strong> O erro mais destrutivo. Cada endereço "
            "antigo precisa apontar para o conteúdo equivalente — senão o histórico daquela página se perde.",
            "<strong>Esquecer endereços que ninguém lembrava.</strong> Páginas antigas que ainda ranqueiam ou "
            "recebem links. Só o inventário completo encontra.",
            "<strong>Desligar o domínio antigo cedo demais.</strong> Os redirecionamentos precisam continuar "
            "funcionando por bastante tempo — não semanas.",
            "<strong>Trocar domínio e estrutura ao mesmo tempo.</strong> Duas mudanças grandes juntas "
            "impedem saber o que causou o quê. Quando possível, separar em etapas.",
            "<strong>Não conferir o conteúdo do destino.</strong> Páginas que chegam vazias, com título "
            "errado ou sem os links internos que tinham.",
            "<strong>Parar de monitorar cedo.</strong> Problemas de migração aparecem ao longo de semanas, "
            "conforme o rastreamento avança. Sair na primeira semana boa é sair cedo demais.",
        ])
        + """
          <p>Se a sua migração já aconteceu e o tráfego caiu, o caminho é
          <a href="/recuperacao-de-trafego-organico/">diagnóstico e recuperação</a> — vários desses erros
          são corrigíveis depois, desde que identificados.</p>""",
        """<h3>Limites do serviço</h3>
          <p>Migração é atendida para necessidades legítimas: rebrand, mudança de marca, consolidação,
          troca de plataforma e perda de registro.</p>
          <p><strong>Não é atendida</strong> quando a motivação é contornar bloqueio judicial ou
          administrativo — em qualquer nicho e em qualquer faixa de investimento.</p>""",
        "erros-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre migração")

    corpo += relacionados("Continue por aqui", [
        ("/blog/como-migrar-site-para-outro-dominio/", "Como migrar passo a passo",
         "O processo completo, com o checklist de cada etapa."),
        ("/blog/trocar-de-dominio-faz-perder-posicoes/", "Trocar faz perder posições?",
         "O que realmente acontece e quanto tempo costuma levar a estabilização."),
        ("/recuperacao-de-trafego-organico/", "Recuperação de tráfego",
         "Se a migração já foi feita e o tráfego caiu."),
    ])

    corpo += cta_final(
        "Vai trocar de domínio?",
        "Na análise eu avalio o cenário, monto o inventário e o mapa de redirecionamento e defino a sequência "
        "de virada — com o que dá para preparar antes de qualquer coisa ir ao ar.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/analise-de-dominios-expirados/", "Ainda estou escolhendo o domínio"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Preciso migrar meu site para outro domínio.",
        float_aria="Falar sobre migração de domínio pelo WhatsApp",
    )


# ============================================================
# D3 — /link-building-para-nichos-competitivos/
# ============================================================

def d3_link_building():
    slug = "link-building-para-nichos-competitivos"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Link building para nichos competitivos | RCB Consultoria"
    desc = ("Metodologia de construção de autoridade para projetos nacionais: critério de relevância, "
            "ritmo controlado, análise de risco e relatórios verificáveis.")
    page_id = "link-building"

    faq = [
        ("Quantos backlinks meu site precisa?",
         "Não existe número universal. A referência é comparativa: quantos domínios distintos apontam para "
         "quem ocupa as posições que você quer, e de que tipo de site vêm. Esse levantamento define o alvo — "
         "e ele muda conforme o termo."),
        ("Comprar backlinks funciona?",
         "Pode gerar movimento de curto prazo e cria passivo de longo prazo. O problema não é só o risco de "
         "desvalorização: é que a maior parte do que se vende em pacote vem de sites sem tráfego e sem "
         "relevância, o que significa pagar por algo que entrega pouco desde o início."),
        ("Quanto custa um backlink de qualidade?",
         "Varia muito por nicho e por veículo. O erro mais comum é comparar preço sem comparar o que se "
         "está comprando: um link de veículo com audiência real e relevância temática não é o mesmo produto "
         "que um link de site criado para vender links, mesmo quando a métrica exibida é parecida."),
        ("Em quanto tempo a autoridade construída aparece?",
         "Autoridade age de forma acumulada e defasada — raramente dá para atribuir um movimento de posição "
         "a um link específico. O acompanhamento observa a evolução do conjunto ao longo de meses, não o "
         "efeito individual de cada conquista."),
        ("A RCB usa PBN?",
         "Não. PBN é explicada nos conteúdos do site porque os clientes perguntam, mas não é executada. O "
         "risco recairia sobre o domínio do cliente, e o histórico de desvalorização dessas redes é longo."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Link building para nichos competitivos", canonical)]),
        schema_service("Link building para nichos competitivos",
                       "Construção de autoridade para projetos nacionais em mercados de alta concorrência: "
                       "seleção por relevância, ritmo controlado, análise de risco e relatórios.",
                       canonical, tipo="Link building"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Link building", canonical)])

    corpo = hero(
        trilha,
        "Metodologia",
        "Link building para nichos competitivos: critério em vez de quantidade",
        "Em disputa nacional, autoridade costuma ser o fator que decide. E é onde mais se gasta mal, "
        "porque o mercado vende quantidade e o que move posição é relevância.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#metodo", "Ver o método"),
        page_id=page_id,
    )

    corpo += sec_split(
        "O princípio",
        "Por que quantidade é a métrica errada",
        """          <p>A pergunta "quantos backlinks eu preciso?" parte de uma premissa equivocada: a de que
          links são unidades intercambiáveis que se somam até atingir um total.</p>
          <p>Não funcionam assim. Um link de um veículo com audiência real, tratando de um assunto próximo
          ao seu, dentro de um conteúdo que faz sentido, tem peso incomparável ao de dezenas de links de
          sites sem tráfego que publicam sobre qualquer tema. E o segundo grupo não é neutro: em volume,
          forma um padrão que passa a trabalhar contra o domínio.</p>
          <p>Por isso o alvo deste serviço nunca é uma quantidade. É um <strong>perfil</strong>: que tipo de
          veículo aponta para quem ocupa as posições desejadas, e como chegar a algo comparável em ritmo
          que não destoe do crescimento natural do site.</p>""",
        """<h3>O que define o valor de um link</h3>
          <ul class="audit-list">
            <li>Relevância temática com o seu projeto</li>
            <li>Audiência real do veículo</li>
            <li>Contexto em que o link aparece</li>
            <li>Perfil de links de saída do veículo</li>
            <li>Texto usado como âncora</li>
            <li>Se o link foi conquistado ou fabricado</li>
          </ul>
          <p style="margin-top:1rem;">Nenhum deles é a métrica de autoridade que aparece nas propostas.</p>""",
        "principio-titulo",
    )

    corpo += sec_texto(
        "O método",
        "Cinco etapas, na ordem",
        passos([
            ("Levantamento do alvo", "Análise do perfil de links de quem ocupa as posições desejadas: "
                                     "quantos domínios, de que tipo, com que ritmo cresceram."),
            ("Auditoria do que existe", "Leitura do perfil atual do site — o que já aponta, o que ajuda e "
                                        "o que é passivo. Detalhado em consultoria de backlinks."),
            ("Preparação do ativo", "Garantir que existe conteúdo que justifique a referência. Buscar menção "
                                    "para site sem conteúdo desperdiça a fonte."),
            ("Prospecção e conquista", "Seleção de veículos por critério, contato e negociação de contexto — "
                                       "não aceitação de lista pronta."),
            ("Acompanhamento", "Registro do que foi conquistado, distribuição de âncoras e evolução do "
                               "conjunto ao longo do tempo."),
        ]),
        "metodo", classe="metodo",
        desc="A terceira etapa é a mais pulada e a que mais compromete resultado: autoridade apontando para "
             "um site que não tem o que oferecer não se sustenta.",
    )

    corpo += sec_split(
        "Risco",
        "O que a análise de risco procura",
        """          <p>Toda construção de autoridade carrega risco. Ele é gerenciável, desde que observado
          continuamente e não só no começo:</p>
"""
        + lista([
            "<strong>Ritmo destoante</strong> — crescimento súbito no número de domínios de referência, "
            "incompatível com o tamanho e a idade do site.",
            "<strong>Concentração de âncora</strong> — muitos links usando exatamente o termo que se quer "
            "ranquear. É o padrão artificial mais fácil de identificar.",
            "<strong>Fontes de baixa qualidade</strong> — veículos sem audiência, sem linha editorial ou "
            "com perfil de saída típico de venda em massa.",
            "<strong>Falta de diversidade</strong> — links vindos sempre do mesmo tipo de fonte, ou de um "
            "grupo pequeno de sites relacionados entre si.",
            "<strong>Ausência de links de marca</strong> — perfil natural inclui menções ao nome e ao "
            "endereço do site, não só a termos comerciais.",
        ])
        + """
          <p>Quando algum desses sinais aparece, o plano é ajustado: reduzir ritmo, diversificar fontes ou
          mudar a distribuição de âncoras. É por isso que o relatório mostra o perfil acumulado, e não
          apenas a lista do mês.</p>""",
        """<h3>Onde este serviço se aplica</h3>
          <ul class="audit-list">
            <li><a href="/link-building-para-iptv/">IPTV e streaming</a> — poucos veículos aceitam o tema</li>
            <li><a href="/link-building-para-bets/">Bets e iGaming</a> — mercado caro e saturado de oferta</li>
            <li>Negócios digitais e plataformas</li>
            <li>Projetos nacionais em qualquer nicho disputado</li>
          </ul>
          <p style="margin-top:1rem;">As páginas de nicho tratam da dificuldade específica de cada mercado;
          o método é este.</p>""",
        "risco-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre construção de autoridade")

    corpo += relacionados("Continue por aqui", [
        ("/consultoria-de-backlinks/", "Auditoria do perfil atual",
         "Quando o problema não é conquistar links, e sim o que já aponta para o site."),
        ("/blog/como-avaliar-qualidade-de-um-backlink/", "Como avaliar um backlink",
         "Os critérios práticos para julgar uma oportunidade antes de aceitar."),
        ("/blog/conteudo-ou-backlinks-onde-investir-primeiro/", "Conteúdo ou backlinks primeiro?",
         "A ordem de investimento que evita desperdício nos primeiros meses."),
    ])

    corpo += cta_final(
        "Quer saber qual perfil de autoridade o seu alvo exige?",
        "Na análise eu levanto o perfil de links de quem ocupa as posições que você quer, comparo com o seu "
        "e devolvo o plano — com critério de seleção, ritmo e faixa de investimento.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero avaliar a construção de autoridade do meu site.",
        float_aria="Falar sobre link building pelo WhatsApp",
    )


# ============================================================
# D4 — /consultoria-de-backlinks/
# ============================================================

def d4_consultoria_backlinks():
    slug = "consultoria-de-backlinks"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Consultoria de backlinks: auditoria de perfil | RCB"
    desc = ("Auditoria do perfil de links do seu site: fontes de risco, oportunidades, comparação com "
            "concorrentes e plano de prioridade.")
    page_id = "consultoria-backlinks"

    faq = [
        ("Como sei se tenho links tóxicos?",
         "Sinais comuns: muitos links de sites sem relação temática, âncoras repetidas e concentradas, "
         "picos de aquisição sem motivo, links de sites em outros idiomas sem contexto ou de páginas que "
         "existem só para hospedar links. A auditoria quantifica isso em vez de estimar no olho."),
        ("Devo desautorizar links ruins?",
         "Nem sempre. A desautorização é uma ferramenta de último recurso e usá-la sem critério pode remover "
         "links que estavam ajudando. Na maior parte dos casos, diluir o perfil com aquisição de qualidade "
         "resolve melhor. A auditoria indica em qual dos dois cenários o site está."),
        ("A auditoria inclui a construção dos links novos?",
         "Não — são serviços diferentes de propósito. A consultoria entrega diagnóstico, priorização e plano. "
         "A execução é o escopo de link building para nichos competitivos, e pode ser contratada em seguida."),
        ("Dá para ver os backlinks dos concorrentes?",
         "Dá, de forma aproximada. Nenhuma ferramenta enxerga o perfil completo de um site, mas a amostra é "
         "suficiente para identificar padrões: de que tipo de veículo eles vêm, quais fontes se repetem "
         "entre vários concorrentes e onde há oportunidade acessível."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Consultoria de backlinks", canonical)]),
        schema_service("Consultoria de backlinks",
                       "Auditoria do perfil de links de um site: identificação de risco, análise de "
                       "concorrentes, mapeamento de oportunidades e plano de priorização.",
                       canonical, tipo="Auditoria de backlinks"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Consultoria de backlinks", canonical)])

    corpo = hero(
        trilha,
        "Diagnóstico",
        "Consultoria de backlinks: entender o que já aponta para o seu site",
        "Antes de conquistar link novo, vale saber o que você já tem — porque parte do que aponta para "
        "o seu site pode estar segurando ele.",
        (ANALISE, "Solicitar análise do projeto"),
        ("/link-building-para-nichos-competitivos/", "Já sei que preciso construir"),
        page_id=page_id,
    )

    corpo += sec_split(
        "Quando faz sentido",
        "Situações que pedem auditoria antes de qualquer execução",
        """          <p>Nem todo projeto precisa desta auditoria. Ela é indicada quando existe passado a
          verificar:</p>
"""
        + lista([
            "<strong>O site já contratou link building antes</strong> — principalmente pacotes por "
            "quantidade, sem relatório detalhado do que foi feito.",
            "<strong>Houve queda de posição sem causa evidente</strong> — e o conteúdo e a parte técnica "
            "já foram descartados como explicação.",
            "<strong>O domínio foi comprado com histórico</strong> — para medir o que veio junto. Se a "
            "compra ainda não aconteceu, o serviço indicado é a "
            "<a href=\"/analise-de-dominios-expirados/\">análise de domínios expirados</a>.",
            "<strong>Antes de investir pesado em autoridade nova</strong> — para não construir sobre um "
            "perfil que precisa ser corrigido primeiro.",
            "<strong>Aparecem links estranhos no relatório</strong> — de sites desconhecidos, em outros "
            "idiomas ou de origem duvidosa.",
        ])
        + """
          <p>Se nada disso se aplica e o site é novo, a auditoria tem pouco a revelar — e o caminho é ir
          direto para a construção.</p>""",
        """<h3>O entregável</h3>
          <ul class="audit-list">
            <li>Mapa do perfil atual, por tipo de fonte</li>
            <li>Classificação de risco por grupo de links</li>
            <li>Distribuição de âncoras acumulada</li>
            <li>Comparação com concorrentes-alvo</li>
            <li>Oportunidades acessíveis identificadas</li>
            <li>Plano de prioridade, com o que fazer primeiro</li>
          </ul>
          <p style="margin-top:1rem;">Diagnóstico e priorização — a execução é serviço separado.</p>""",
        "quando-titulo",
    )

    corpo += sec_texto(
        "Análise",
        "As quatro leituras da auditoria",
        problem_cards([
            ("Perfil próprio",
             "De onde vêm os links que apontam para o site, quantos domínios distintos são, qual a "
             "proporção de fontes relevantes e quanto do perfil é herança de trabalho antigo."),
            ("Risco",
             "Quais grupos de links apresentam sinais de artificialidade — concentração de âncora, fontes "
             "sem audiência, padrões de aquisição em lote — e qual a dimensão real do problema."),
            ("Concorrentes",
             "De onde vem a autoridade de quem ocupa as posições desejadas, quais fontes se repetem entre "
             "vários deles e quais dessas fontes são realisticamente acessíveis."),
            ("Oportunidade",
             "Menções à marca sem link, conteúdo próprio que já atrai referência espontânea e veículos do "
             "setor ainda não trabalhados — o que costuma ser o caminho mais barato."),
        ]),
        "analise-titulo", classe="problem-section",
    )

    corpo += sec_split(
        "Decisão",
        "Desautorizar, diluir ou ignorar",
        """          <p>Encontrar links ruins não significa que é preciso agir sobre eles. Essa é a confusão
          mais frequente, e agir errado costuma piorar a situação.</p>
          <p><strong>Ignorar</strong> é o cenário mais comum. Todo site acumula links de baixa qualidade
          que nunca pediu, e sistemas de busca lidam com isso desconsiderando o que não faz sentido. Mexer
          sem necessidade só cria risco.</p>
          <p><strong>Diluir</strong> é a resposta usual quando há um volume relevante de fontes fracas: em
          vez de remover, aumentar a proporção de links bons até que o perfil deixe de chamar atenção pelo
          lado errado.</p>
          <p><strong>Desautorizar</strong> fica para casos com evidência forte — histórico de trabalho
          manipulativo conhecido, padrão claro e concentrado, ou notificação recebida. É irreversível na
          prática e remove links que talvez estivessem ajudando.</p>
          <p>A auditoria diz em qual dos três cenários o site está, com o que sustenta a conclusão.</p>""",
        """<h3>Erros comuns nesta etapa</h3>
          <ul class="audit-list">
            <li>Desautorizar em massa por precaução</li>
            <li>Usar pontuação de ferramenta como veredito</li>
            <li>Confundir link irrelevante com link tóxico</li>
            <li>Tratar o sintoma sem investigar a causa da queda</li>
            <li>Repetir a auditoria sem mudar nada entre elas</li>
          </ul>""",
        "decisao-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre auditoria de links")

    corpo += relacionados("Continue por aqui", [
        ("/link-building-para-nichos-competitivos/", "Construção de autoridade",
         "A execução, depois que o diagnóstico apontou a prioridade."),
        ("/blog/como-analisar-backlinks-dos-concorrentes/", "Analisar backlinks dos concorrentes",
         "O método para identificar de onde vem a autoridade de quem está à frente."),
        ("/recuperacao-de-trafego-organico/", "Recuperação de tráfego",
         "Se a queda já aconteceu e a causa ainda não está clara."),
    ])

    corpo += cta_final(
        "Quer saber o que está apontando para o seu site?",
        "Na análise do projeto eu faço a primeira leitura do perfil e indico se há sinal de risco que "
        "justifique a auditoria completa — ou se o caminho é ir direto para a construção.",
        ANALISE, "Solicitar análise do projeto", page_id,
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Quero auditar o perfil de backlinks do meu site.",
        float_aria="Solicitar auditoria de backlinks pelo WhatsApp",
    )


# ============================================================
# D5 — /recuperacao-de-trafego-organico/
# ============================================================

def d5_recuperacao():
    slug = "recuperacao-de-trafego-organico"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Recuperação de tráfego orgânico após queda | RCB"
    desc = ("Perdeu posições no Google? Diagnóstico diferencial da causa — atualização, migração, "
            "técnico ou conteúdo — e plano de recuperação.")
    page_id = "recuperacao-trafego"

    faq = [
        ("Dá para recuperar o tráfego perdido?",
         "Depende da causa. Queda por problema técnico ou migração malfeita costuma ser a mais recuperável, "
         "porque há algo concreto para consertar. Queda por atualização de algoritmo exige trabalho de fundo "
         "e prazo maior. E há casos em que o patamar anterior não volta — quando o que mudou foi o próprio "
         "mercado ou o formato de resultado da busca."),
        ("Quanto tempo leva a recuperação?",
         "Correções técnicas podem mostrar efeito em semanas. Recuperação de queda por qualidade ou "
         "autoridade leva meses e depende de execução contínua. Nenhum prazo é garantido — o que a análise "
         "entrega é a causa mais provável e o que é razoável esperar."),
        ("Perdi tráfego depois de uma atualização do Google. E agora?",
         "Primeiro confirma-se que a queda coincide mesmo com a atualização, e não com outra coisa que "
         "aconteceu junto. Depois se identifica que tipo de conteúdo perdeu — costuma ser um padrão, não o "
         "site inteiro. A resposta trabalha esse padrão, não o site como um todo."),
        ("Meu tráfego caiu depois de trocar de domínio.",
         "É um dos cenários mais comuns e um dos mais corrigíveis. Costuma ser redirecionamento faltando ou "
         "apontando para o lugar errado. O diagnóstico compara o inventário antigo com o novo e encontra o "
         "que se perdeu no caminho. Ver migração de domínio e SEO."),
        ("A queda pode ser normal?",
         "Pode. Sazonalidade, fim de um pico de interesse ou mudança no formato do resultado de busca "
         "reduzem tráfego sem que nada tenha piorado no site. Separar oscilação normal de problema real é a "
         "primeira coisa que o diagnóstico faz — e evita tratar o que não está quebrado."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Recuperação de tráfego orgânico", canonical)]),
        schema_service("Recuperação de tráfego orgânico",
                       "Diagnóstico da causa de queda de tráfego orgânico e plano de recuperação: análise "
                       "técnica, de conteúdo, de autoridade e de migração.",
                       canonical, tipo="Recuperação de tráfego orgânico"),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Recuperação de tráfego", canonical)])

    corpo = hero(
        trilha,
        "Diagnóstico de queda",
        "Recuperação de tráfego orgânico: primeiro descobrir a causa, depois agir",
        "A pressa faz quase todo mundo começar mexendo no site. Mudar coisas sem saber o que quebrou "
        "costuma atrasar a recuperação e apagar as pistas.",
        (ANALISE, "Solicitar análise do projeto"),
        ("#causas", "Ver o diagnóstico diferencial"),
        page_id=page_id,
    )

    corpo += sec_texto(
        "Diagnóstico diferencial",
        "As causas possíveis, e como distingui-las",
        tabela(
            ["Causa provável", "Como a queda se comporta", "Onde confirmar"],
            [
                ["Atualização de algoritmo", "queda em poucos dias, atingindo um padrão de conteúdo",
                 "data da queda × janela da atualização"],
                ["Migração malfeita", "queda logo após troca de domínio ou plataforma",
                 "inventário de endereços e redirecionamentos"],
                ["Problema técnico", "queda abrupta, às vezes só em parte do site",
                 "indexação, erros de rastreamento, desempenho"],
                ["Perda de links", "queda gradual, concentrada em páginas específicas",
                 "evolução dos domínios de referência"],
                ["Conteúdo em massa", "queda lenta e generalizada após publicação em volume",
                 "histórico de publicação × curva de tráfego"],
                ["Concorrência", "queda gradual em termos específicos",
                 "quem passou a ocupar aquelas posições"],
                ["Sazonalidade ou mudança de SERP", "queda que se repete ou acompanha novo formato de resultado",
                 "comparação com o mesmo período anterior"],
            ],
            nota="A data exata da queda é a informação mais valiosa do diagnóstico — é ela que separa as hipóteses.",
        ),
        "causas",
        desc="Boa parte dos casos tem mais de uma causa acontecendo junto, e é por isso que a ordem "
             "importa: tratar a causa errada primeiro consome tempo e não devolve posição.",
    )

    corpo += sec_split(
        "Antes de mexer",
        "O erro que mais atrasa a recuperação",
        """          <p>A reação natural a uma queda é mudar coisas: reescrever títulos, alterar textos,
          desautorizar links, publicar mais. Feito antes do diagnóstico, isso costuma piorar a situação por
          três motivos.</p>
          <p><strong>Apaga as pistas.</strong> Depois de vinte alterações, não dá mais para saber o que
          estava acontecendo antes — e o diagnóstico fica muito mais difícil.</p>
          <p><strong>Introduz variáveis novas.</strong> Se o tráfego mudar depois, não há como saber se foi
          a correção certa, uma das outras alterações ou o efeito tardio da causa original.</p>
          <p><strong>Pode remover o que funcionava.</strong> Reescrever páginas que ainda ranqueavam bem, ou
          desautorizar links que estavam ajudando, transforma uma queda parcial em uma queda maior.</p>
          <p>A sequência correta é: congelar alterações, levantar dados, formar hipótese, testar a hipótese
          mais provável e medir. Mais lenta no primeiro dia, muito mais rápida no resultado.</p>""",
        """<h3>O que preservar</h3>
          <ul class="audit-list">
            <li>Dados de posição e tráfego antes da queda</li>
            <li>A data exata em que começou</li>
            <li>Histórico de alterações no site</li>
            <li>Registro do que foi publicado e quando</li>
            <li>Backup da estrutura anterior, se houve migração</li>
          </ul>
          <p style="margin-top:1rem;">Quanto mais desse material existir, mais rápido e mais barato é o
          diagnóstico.</p>""",
        "antes-titulo",
    )

    corpo += sec_texto(
        "Como funciona",
        "Do levantamento ao acompanhamento",
        passos([
            ("Levantamento", "Reconstrução da linha do tempo: quando caiu, quanto caiu, quais páginas e "
                             "quais termos foram atingidos."),
            ("Hipóteses", "Cruzamento da data com atualizações conhecidas, mudanças no site, migrações e "
                          "movimentação da concorrência."),
            ("Confirmação", "Verificação técnica, de conteúdo e de perfil de links para confirmar ou "
                            "descartar cada hipótese."),
            ("Plano priorizado", "O que corrigir primeiro, com o impacto esperado e o esforço de cada item — "
                                 "e o que deliberadamente não deve ser mexido."),
            ("Execução e medição", "Correções aplicadas em ordem, com acompanhamento para atribuir efeito a "
                                   "cada mudança."),
        ]),
        "processo-titulo", classe="metodo",
    )

    corpo += sec_split(
        "Expectativa",
        "O que é honesto dizer sobre recuperação",
        """          <p>Recuperação não é garantida, e o cenário varia muito conforme a causa.</p>
          <p>Quedas <strong>técnicas ou de migração</strong> costumam ser as mais recuperáveis: há algo
          concreto quebrado, o conserto é objetivo e o efeito tende a aparecer em semanas.</p>
          <p>Quedas por <strong>qualidade ou autoridade</strong> exigem trabalho de fundo — revisar ou
          consolidar conteúdo, reconstruir cobertura, retomar construção de autoridade. O horizonte é de
          meses e depende de execução contínua.</p>
          <p>E há casos em que <strong>o patamar anterior não volta</strong>: quando o formato do resultado
          de busca mudou, quando o mercado se reorganizou ou quando o tráfego anterior vinha de algo que
          deixou de existir. Nesses casos, o trabalho honesto é redefinir o alvo, não perseguir um número
          que não está mais disponível.</p>
          <p>Isso é dito na análise — inclusive quando a conclusão é que investir na recuperação daquele
          patamar específico não é o melhor uso do orçamento.</p>""",
        """<h3>Serviços relacionados</h3>
          <ul class="audit-list">
            <li><a href="/migracao-de-dominio-seo/">Migração de domínio</a> — se a queda veio de troca de endereço</li>
            <li><a href="/consultoria-de-backlinks/">Consultoria de backlinks</a> — se o perfil de links é suspeito</li>
            <li><a href="/link-building-para-nichos-competitivos/">Link building</a> — se faltou autoridade</li>
            <li><a href="/seo-para-nichos-competitivos/">Nichos competitivos</a> — se a causa foi concorrência</li>
          </ul>""",
        "expectativa-titulo",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre queda de tráfego")

    corpo += relacionados("Continue por aqui", [
        ("/blog/como-recuperar-trafego-organico-apos-queda/", "Como recuperar após uma queda",
         "O passo a passo do diagnóstico, com o que verificar em cada hipótese."),
        ("/blog/trocar-de-dominio-faz-perder-posicoes/", "Queda após troca de domínio",
         "O cenário mais comum e mais corrigível de todos."),
        ("/auditoria-seo/", "Auditoria de SEO",
         "Se o objetivo é revisão geral e não investigação de uma queda específica."),
    ])

    corpo += cta_final(
        "Seu tráfego caiu e você não sabe por quê?",
        "Na análise eu reconstruo a linha do tempo da queda e aponto a causa mais provável — antes de "
        "qualquer alteração no site, para não apagar as pistas.",
        ANALISE, "Solicitar análise do projeto", page_id,
        secundario=("/migracao-de-dominio-seo/", "A queda foi depois de uma migração"),
    )

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(
        head, corpo, page_id,
        float_msg="Olá, Renan. Meu site perdeu tráfego orgânico e preciso de um diagnóstico.",
        float_aria="Solicitar diagnóstico de queda de tráfego pelo WhatsApp",
    )


PAGINAS = [d1_analise_dominios, d2_migracao_dominio, d3_link_building,
           d4_consultoria_backlinks, d5_recuperacao]
