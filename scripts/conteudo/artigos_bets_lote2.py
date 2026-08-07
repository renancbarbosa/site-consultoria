# -*- coding: utf-8 -*-
"""
Cluster bets, iGaming e afiliados — lote 2 (backlog do plano §5.1, produzido em 07/08/2026).

20 seo-para-afiliados-como-estruturar-projeto
21 link-building-para-bets-o-que-avaliar
26 conteudo-autoridade-conversao-sites-de-apostas
27 site-de-afiliado-competir-nacionalmente

Diferenciação em relação ao que já existe:
  20 × página C3   — a C3 descreve a ARQUITETURA (que camadas existem); o 20 dá a
                     SEQUÊNCIA de execução (em que ordem construir, por fase).
  21 × artigo 38   — o 38 ensina a avaliar um link qualquer; o 21 trata do mercado
                     de venda de links deste setor e de como julgar as propostas
                     que chegam.
  26 × página C1   — a C1 vende o projeto; o 26 explica como as três frentes se
                     conectam e quais métricas ligam uma à outra.
  27 × C3 + art.19 — recorte de PORTE: onde um afiliado pequeno ganha de um portal
                     grande, e onde não adianta tentar.

Política §2.6: linguagem neutra quanto à regulação, sem conclusão jurídica, sem
apelo ao jogo e sem promessa de ganho.
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-07"
CAT = "Bets e iGaming"
ANALISE = "/analise-de-projeto/"

NOTA_REG = ('<p><strong>Sobre a parte regulatória:</strong> o setor de apostas no Brasil passou por '
            'mudanças regulatórias relevantes, e as regras aplicáveis variam conforme o tipo de operação e '
            'a atividade exercida. Este conteúdo trata de comunicação e posicionamento orgânico — não é '
            'orientação jurídica. Cada empresa deve verificar com assessoria própria a situação a que está '
            'sujeita, inclusive quanto a regras de publicidade do setor.</p>')

ARTIGOS = []


# ------------------------------------------------------------------
# 20
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "seo-para-afiliados-como-estruturar-projeto",
    "h1": "SEO para afiliados de bets: como estruturar o projeto?",
    "title": "SEO para afiliados de bets: como estruturar o projeto | RCB",
    "desc": ("A sequência de execução de um portal de afiliado, fase por fase: o que construir "
             "primeiro, o que deixar para depois e onde a maioria inverte a ordem."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-afiliados-de-apostas/", "Afiliados de apostas"),
    "corpo": f"""
        <p>Saber quais camadas um portal precisa ter é uma coisa — está em
        {link('/seo-para-afiliados-de-apostas/', 'SEO para afiliados de apostas')}. Saber <strong>em que
        ordem construí-las</strong> é outra, e é onde a maioria dos projetos se perde.</p>

        {caixa('<p><strong>Resposta direta:</strong> comece pelas camadas que convertem, não pelas que '
               'trazem volume. Um portal com dez páginas de decisão bem-feitas e receita entrando sustenta '
               'a construção do resto. Um portal com cem artigos informacionais e nenhuma página de '
               'conversão consome caixa e não gera retorno para justificar a continuidade.</p>')}

        {caixa(NOTA_REG)}

        <h2>Fase 0 — Decidir a estrutura antes da primeira página</h2>

        <p>Esta fase não produz conteúdo e define o teto do projeto. As decisões que precisam estar
        fechadas antes de publicar qualquer coisa:</p>

        <ul>
          <li>Hierarquia de categorias — como o mercado será organizado.</li>
          <li>Padrão de endereços, consistente desde o início.</li>
          <li>Onde a informação que muda com frequência fica armazenada, em um lugar só.</li>
          <li>Como as tabelas comparativas são geradas a partir dessa fonte.</li>
          <li>O que é página indexável e o que é apenas navegação.</li>
        </ul>

        <p>Pular esta fase é o erro fundador do nicho: o portal cresce, a estrutura não acompanha, e a
        reorganização chega junto com o primeiro resultado. Detalhado em
        {link('/blog/como-criar-site-para-afiliado-de-apostas/', 'como criar um site para afiliado de apostas')}.</p>

        <h2>Fase 1 — Camadas de decisão</h2>

        <p>O que se publica primeiro é o que captura quem já está decidindo:</p>

        <ol>
          <li><strong>Páginas de avaliação</strong> das principais opções do mercado. Uma por opção, com
          critério explícito e informação própria.</li>
          <li><strong>Comparativos diretos</strong> entre as opções mais procuradas.</li>
          <li><strong>Páginas de condições vigentes</strong>, que são as de maior rotatividade.</li>
        </ol>

        <p>São páginas trabalhosas e de disputa alta — mas é aqui que está a intenção comercial. O que
        diferencia uma avaliação que ranqueia está em
        {link('/blog/como-criar-paginas-de-avaliacao-de-casas-de-apostas/', 'como criar páginas de avaliação')}.</p>

        <h2>Fase 2 — Categorias e organização</h2>

        <p>Com as páginas de decisão publicadas, as categorias passam a ter o que organizar. Construídas
        antes, ficam vazias; construídas agora, já nascem com conteúdo e com links internos fazendo
        sentido.</p>

        <p>É também nesta fase que a estrutura de links internos é definida de verdade — quais páginas
        recebem força de quais, e por quê.</p>

        <h2>Fase 3 — Conteúdo informacional</h2>

        <p>Agora entra o volume: explicações de funcionamento, dúvidas de quem está aprendendo, conteúdo
        de cauda longa. Ele traz visitante em quantidade e, mais importante, sustenta a relevância temática
        que os termos de decisão precisam para subir.</p>

        <p>Deixar essa camada para a fase 3 não é desprezá-la — é reconhecer que ela rende mais quando há
        páginas comerciais para receber o visitante que ela atrai.</p>

        <h2>Fase 4 — Autoridade (que começa antes)</h2>

        <p>Aqui vale uma correção na ideia de "fase": a construção de autoridade não é a quarta etapa de
        uma fila. Ela <strong>começa na fase 1 e nunca para</strong>.</p>

        <p>O motivo é o teto de velocidade: adquirir muitos links em pouco tempo cria padrão artificial,
        então existe um ritmo máximo compatível com a idade do site. Se a construção só começar depois de
        todo o conteúdo pronto, o prazo total do projeto se estende bastante. O que muda por fase é o
        <em>peso</em> do investimento, não o início.</p>

        {tabela(
            ["Fase", "Foco principal", "Peso em conteúdo", "Peso em autoridade"],
            [
                ["0 — Estrutura", "decisões de arquitetura", "—", "—"],
                ["1 — Decisão", "avaliações e comparativos", "alto", "início da prospecção"],
                ["2 — Organização", "categorias e links internos", "médio", "crescente"],
                ["3 — Volume", "conteúdo informacional", "alto", "crescente"],
                ["4 — Disputa", "termos principais", "manutenção", "alto"],
            ],
            nota="A autoridade aparece em todas as fases a partir da 1 — o que muda é o peso, não o começo."
        )}

        <h2>Fase 5 — Manutenção, que não é uma fase</h2>

        <p>Neste nicho o conteúdo envelhece rápido. Condições mudam, opções entram e saem do mercado. Um
        portal com cem avaliações desatualizadas vale menos que um com trinta corretas — e o leitor procura
        pela data de atualização.</p>

        <p>Por isso a revisão precisa entrar no calendário desde a fase 1, com frequência diferente por
        camada: condições e ofertas com revisão alta, avaliações e comparativos com revisão média,
        conteúdo informacional com revisão baixa.</p>

        <h2>Os três erros de sequência mais comuns</h2>

        <ol>
          <li><strong>Começar pelo conteúdo informacional.</strong> Traz visita sem intenção, não gera
          receita, e o projeto perde fôlego antes de chegar às páginas que convertem.</li>
          <li><strong>Publicar tudo sem estrutura definida.</strong> As páginas passam a competir entre si,
          e reorganizar depois significa mexer no site inteiro.</li>
          <li><strong>Deixar a autoridade para o fim.</strong> Empurra o resultado dos termos principais
          para muito mais tarde do que seria necessário.</li>
        </ol>
    """,
    "faq": [
        ("Quanto tempo dura cada fase?",
         "Depende do escopo e do ritmo de produção acordado. O que importa mais que a duração é a ordem: "
         "projetos que respeitam a sequência costumam gerar receita antes e sustentar melhor a "
         "continuidade do investimento."),
        ("Posso rodar as fases em paralelo?",
         "Parcialmente, e é o que costuma acontecer na prática. O que não funciona é inverter: publicar "
         "volume informacional antes de existir página de conversão, ou publicar antes de fechar a "
         "estrutura."),
        ("E se eu já tenho um portal publicado sem essa ordem?",
         "O caminho é diagnóstico antes de produção: identificar canibalização entre páginas, o que "
         "consolidar, o que reescrever e o que já funciona. Quase sempre há mais a ganhar reorganizando o "
         "que existe do que publicando mais."),
        ("Preciso de todas as camadas para começar a competir?",
         "Não. Um recorte bem coberto — uma categoria, com suas avaliações e comparativos — compete melhor "
         "que uma cobertura rasa de tudo. Expandir depois é mais fácil que consertar um portal raso."),
    ],
    "cta": ("Vai começar ou reorganizar um portal? Na análise do projeto eu avalio a estrutura atual, "
            "identifico canibalização e devolvo a sequência recomendada com escopo e prazo estimado.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 21
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "link-building-para-bets-o-que-avaliar",
    "h1": "Link building para bets: o que avaliar?",
    "title": "Link building para bets: o que avaliar nas propostas | RCB",
    "desc": ("Este é um dos mercados de venda de links mais ativos e mais caros do país. Como "
             "julgar as propostas que chegam antes de gastar."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-bets/", "Link building para bets"),
    "corpo": f"""
        <p>Quem opera um projeto neste setor recebe propostas de link building o tempo todo. Este artigo é
        sobre <strong>como julgar essas propostas</strong> — não sobre como avaliar um link em geral, que
        está em {link('/blog/como-avaliar-qualidade-de-um-backlink/', 'como avaliar a qualidade de um backlink')}.</p>

        {caixa('<p><strong>Resposta direta:</strong> a maior parte do que se vende neste setor é volume de '
               'sites sem audiência, precificado alto porque a demanda é alta. O filtro mais eficiente é '
               'uma pergunta só: <em>eu anunciaria neste site se ele não passasse nenhum sinal de '
               'ranqueamento?</em> Se a resposta for não, você está pagando exclusivamente por um sinal que '
               'pode deixar de contar.</p>')}

        {caixa(NOTA_REG)}

        <h2>Por que este mercado é diferente</h2>

        <p>Três características se combinam e produzem um mercado particularmente ruim para o comprador:</p>

        <p><strong>Demanda altíssima.</strong> Muito dinheiro disputando posições, e todos precisando de
        autoridade ao mesmo tempo.</p>

        <p><strong>Oferta limitada.</strong> Muitos veículos evitam o tema, o que reduz o conjunto de
        fontes genuinamente relevantes.</p>

        <p><strong>Assimetria de informação.</strong> Quem vende sabe exatamente o que está vendendo. Quem
        compra costuma receber uma planilha com métricas e preços, sem o que importa.</p>

        <p>O resultado é previsível: preços muito acima da média do mercado por fontes que, examinadas,
        entregam pouco.</p>

        <h2>O que a proposta mostra e o que ela esconde</h2>

        {tabela(
            ["A planilha mostra", "O que ela não mostra"],
            [
                ["Métrica de autoridade do domínio", "se o site tem visitantes reais"],
                ["Preço por link", "quantos outros links comerciais saem daquele site"],
                ["Nicho declarado", "se o site publica sobre todos os nichos"],
                ["Prazo de publicação", "se o link é permanente ou some quando o pagamento para"],
                ["Quantidade de links do pacote", "quantos domínios distintos são de fato"],
                ["'Conteúdo incluso'", "se o texto existiria sem o link"],
            ],
            nota="Nenhuma das lacunas da direita é preenchida pagando mais caro — só verificando."
        )}

        <h2>Sete perguntas para fazer antes de fechar</h2>

        <ol>
          <li><strong>Qual o endereço exato onde o link vai aparecer?</strong> Recusa em informar é
          resposta suficiente.</li>
          <li><strong>O site tem tráfego próprio?</strong> Peça evidência, não a métrica de autoridade.</li>
          <li><strong>Qual a linha editorial dele?</strong> Se publica sobre advocacia, pet shop e apostas
          na mesma semana, é espaço publicitário disfarçado.</li>
          <li><strong>Quantos links comerciais saem de cada artigo?</strong> Muitos indicam venda em massa.</li>
          <li><strong>O link é permanente?</strong> Link com validade some quando o pagamento para — e a
          posição que dependia dele vai junto.</li>
          <li><strong>Quem escreve o conteúdo?</strong> Texto criado só para hospedar o link rende pouco.</li>
          <li><strong>Quantos domínios distintos são?</strong> Vinte links do mesmo site contam bem menos
          que vinte de sites diferentes.</li>
        </ol>

        <h2>Os sinais de proposta ruim</h2>

        <ul>
          <li>Preço por unidade muito abaixo do resto do mercado.</li>
          <li>Pacotes vendidos por quantidade, com prazo de entrega fixo.</li>
          <li>Métrica de autoridade alta combinada com tráfego quase nulo.</li>
          <li>Menção a "rede própria", "parceiros exclusivos" ou "método proprietário" —
          {link('/blog/o-que-e-pbn-e-como-funciona/', 'costuma descrever uma rede de sites')}.</li>
          <li>Garantia de posição atrelada ao pacote de links.</li>
          <li>Pressa para fechar, com desconto por tempo limitado.</li>
        </ul>

        <h2>Como decidir onde concentrar a verba</h2>

        <p>Como as fontes boas são escassas e caras, a estratégia que costuma render mais é o inverso da
        que o mercado vende: <strong>menos fontes, melhor escolhidas, com verba concentrada</strong>.</p>

        <p>Um caminho prático para priorizar:</p>

        <ol>
          <li>Levante de onde vem a autoridade de quem ocupa as posições que você quer — o método está em
          {link('/blog/como-analisar-backlinks-dos-concorrentes/', 'como analisar os backlinks dos concorrentes')}.</li>
          <li>Identifique os veículos que aparecem apontando para <em>vários</em> concorrentes: eles já
          demonstraram receptividade ao tema.</li>
          <li>Separe os que são realisticamente acessíveis agora.</li>
          <li>Concentre a verba neles, em ritmo constante.</li>
        </ol>

        <p>Essa lista costuma ser bem menor — e bem mais eficaz — que qualquer planilha recebida por
        e-mail.</p>

        <h2>O que fazer se você já comprou volume</h2>

        <p>Não desautorize nada por precaução: isso pode remover o que estava ajudando. O caminho é medir
        primeiro. Uma {link('/consultoria-de-backlinks/', 'auditoria do perfil de links')} mostra que
        proporção vem de fontes fracas e se existe padrão evidente — e só a partir daí se decide entre
        diluir com aquisição de qualidade, desautorizar o que for claramente problemático, ou não fazer nada.</p>
    """,
    "faq": [
        ("Existe faixa de preço justa neste setor?",
         "Os valores variam demais por veículo para que um número seja útil. O mais seguro é comparar "
         "propostas pelos critérios de audiência, relevância e contexto — duas ofertas com o mesmo preço "
         "podem ser produtos completamente diferentes."),
        ("Vale pagar caro por um veículo grande do setor?",
         "Pode valer, se ele tiver audiência real e o contexto do link fizer sentido. O que não vale é "
         "pagar caro por métrica alta sem público — que é exatamente o que mais se vende aqui."),
        ("Link em portal de notícias funciona?",
         "Depende do contexto. Menção dentro de conteúdo relevante, em veículo com leitores, rende. "
         "Conteúdo patrocinado genérico, publicado em massa e sem relação editorial, rende bem menos do "
         "que costuma custar."),
        ("Quanto tempo até ver efeito?",
         "Autoridade age de forma acumulada e defasada. Não espere atribuir movimento de posição a um link "
         "específico — o que se observa é a evolução do conjunto ao longo de meses."),
    ],
    "cta": ("Recebeu uma proposta e quer uma segunda opinião antes de gastar? Na análise do projeto eu "
            "avalio as fontes oferecidas e comparo com o perfil de quem ocupa as posições que você quer.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 26
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "conteudo-autoridade-conversao-sites-de-apostas",
    "h1": "Conteúdo, autoridade e conversão em sites de apostas",
    "title": "Conteúdo, autoridade e conversão em sites de apostas | RCB",
    "desc": ("As três frentes não funcionam separadas. Como elas se conectam, quais métricas ligam "
             "uma à outra e onde o desequilíbrio entre elas trava o projeto."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-bets/", "SEO para bets"),
    "corpo": f"""
        <p>É comum tratar conteúdo, autoridade e conversão como três projetos paralelos, cada um com sua
        meta. Em setor disputado isso não funciona: as três se condicionam, e o desequilíbrio entre elas
        é a causa mais frequente de projeto que consome orçamento sem sair do lugar.</p>

        {caixa('<p><strong>Resposta direta:</strong> conteúdo sem autoridade não sobe; autoridade sem '
               'conteúdo não tem o que sustentar; e os dois juntos sem conversão só produzem visita cara. '
               'O gargalo de um projeto está quase sempre em uma das três — e tratar a frente errada é o '
               'desperdício mais comum do setor.</p>')}

        {caixa(NOTA_REG)}

        <h2>Como as três se conectam</h2>

        <p><strong>Conteúdo → autoridade.</strong> Material que merece referência é o que torna a
        prospecção viável. Sem ele, cada menção vira negociação pura e custa mais. É por isso que buscar
        links para um site sem substância desperdiça a fonte — e a mesma menção não se consegue duas vezes.</p>

        <p><strong>Autoridade → conteúdo.</strong> O conteúdo que já existe passa a ranquear melhor quando
        o domínio ganha reconhecimento. Um mesmo artigo pode ficar parado por meses e subir sem ter sido
        alterado, simplesmente porque o site como um todo passou a ser considerado.</p>

        <p><strong>Conteúdo → conversão.</strong> Página que responde à busca por completo converte melhor
        que página que atrai o clique e frustra. Neste setor, boa parte do abandono acontece porque a
        informação que o visitante procurava não estava lá.</p>

        <p><strong>Conversão → decisão de investimento.</strong> Saber quais páginas geram clique
        qualificado é o que permite decidir onde investir conteúdo e autoridade. Sem esse dado, o
        investimento se distribui por igual — e por igual é quase sempre errado.</p>

        <h2>As métricas que ligam uma frente à outra</h2>

        {tabela(
            ["Frente", "Métrica própria", "Métrica que a liga à seguinte"],
            [
                ["Conteúdo", "páginas indexadas; termos únicos com impressão", "posição média por grupo de termos"],
                ["Autoridade", "domínios de referência; distribuição de âncoras", "evolução da posição média"],
                ["Conversão", "cliques qualificados por página", "receita por grupo de conteúdo"],
            ],
            nota="A coluna da direita é a que costuma faltar nos relatórios — e é a que permite decidir."
        )}

        <p>O erro clássico de medição é acompanhar cada frente isoladamente: número de artigos publicados,
        número de links conquistados, taxa de conversão geral. Os três podem subir enquanto o projeto não
        anda, porque nada aí mostra se as frentes estão se sustentando.</p>

        <h2>Diagnóstico: qual das três é o seu gargalo</h2>

        <p>Há um padrão razoavelmente confiável, baseado em onde as páginas estão:</p>

        <ul>
          <li><strong>Poucas páginas indexadas e poucos termos com impressão</strong> → o gargalo é
          conteúdo. Falta cobertura.</li>
          <li><strong>Muitas impressões, posições entre 10 e 30, conteúdo tão bom quanto o de quem está
          acima</strong> → o gargalo é autoridade. É o cenário mais comum em projeto que "travou".</li>
          <li><strong>Boas posições, tráfego chegando, poucos cliques qualificados</strong> → o gargalo é
          conversão. Investir mais em tráfego só amplia o desperdício.</li>
          <li><strong>Nada se move em nenhum indicador</strong> → verificar a base técnica antes de
          qualquer coisa.</li>
        </ul>

        <p>O raciocínio de priorização entre as duas primeiras está em
        {link('/blog/conteudo-ou-backlinks-onde-investir-primeiro/', 'conteúdo ou backlinks: onde investir primeiro')}.</p>

        <h2>O desequilíbrio mais caro do setor</h2>

        <p>É investir pesado em autoridade com o conteúdo raso. Acontece porque autoridade é a frente que
        mais recebe proposta comercial — chegam ofertas de link toda semana, e nenhuma de "produzir
        conteúdo melhor".</p>

        <p>O resultado é um perfil de links robusto apontando para páginas que não respondem por completo à
        busca. As posições até melhoram, mas param antes do topo, porque o que falta não é força — é o
        conteúdo ser efetivamente a melhor resposta disponível.</p>

        <h2>O que sustenta conversão neste setor</h2>

        <p>Sem apelo ao jogo e sem promessa de ganho, o que faz o visitante avançar é informação:</p>

        <ul>
          <li>Condições descritas com precisão e atualizadas.</li>
          <li>Estrutura que facilita comparação — tabela legível no celular vale mais que texto longo.</li>
          <li>Pontos negativos declarados, que aumentam a confiança na recomendação positiva.</li>
          <li>Data de atualização visível, porque o leitor procura por ela.</li>
          <li>Rastreamento por página e por elemento, para saber o que funciona.</li>
        </ul>

        <p>Esse último item é o que fecha o ciclo: é ele que transforma conversão em informação para
        decidir onde investir conteúdo e autoridade no ciclo seguinte.</p>
    """,
    "faq": [
        ("Dá para trabalhar as três frentes ao mesmo tempo?",
         "Dá, e é o desenho usual — o que muda é o peso de cada uma conforme a fase do projeto. O que não "
         "funciona é tratá-las como projetos independentes, com metas que não conversam."),
        ("Qual frente dá retorno mais rápido?",
         "Conversão, quase sempre — melhorar páginas que já recebem tráfego produz efeito em semanas, sem "
         "depender de rastreamento nem de autoridade. É por isso que vale checar conversão antes de "
         "investir em mais tráfego."),
        ("Meu conteúdo é bom e não sobe. É falta de autoridade?",
         "É a hipótese mais provável se as páginas estão consistentemente entre as posições 10 e 30 e a "
         "cobertura é comparável à dos concorrentes. Vale confirmar comparando o perfil de links antes de "
         "concluir."),
        ("Como saber se a conversão está ruim?",
         "Comparando o desempenho entre páginas do próprio site: se algumas convertem bem e outras "
         "recebem tráfego semelhante sem gerar clique qualificado, o problema está nas páginas, não no "
         "volume de visitas."),
    ],
    "cta": ("Quer saber qual das três frentes está travando o seu projeto? Na análise eu comparo sua "
            "cobertura, seu perfil de links e o desempenho das páginas com quem ocupa as posições-alvo.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 27
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "site-de-afiliado-competir-nacionalmente",
    "h1": "O que um site de afiliado precisa para competir nacionalmente?",
    "title": "O que um site de afiliado precisa para competir | RCB",
    "desc": ("Onde um portal pequeno ganha de um grande e onde não adianta tentar. A leitura de "
             "porte que define onde concentrar esforço."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-afiliados-de-apostas/", "Afiliados de apostas"),
    "corpo": f"""
        <p>A pergunta que está por trás desta é sempre a mesma: <em>eu, com um portal pequeno, consigo
        competir com os grandes?</em> A resposta é sim — em alguns lugares, e não em outros. Saber
        distinguir os dois é o que separa um projeto viável de um que queima orçamento.</p>

        {caixa('<p><strong>Resposta direta:</strong> um portal pequeno não vence um portal grande em '
               'cobertura nem em autoridade. Vence em <strong>profundidade de recorte, atualização e '
               'informação própria</strong> — três coisas que operação grande executa mal justamente por '
               'ser grande. A estratégia é escolher onde disputar, não disputar tudo.</p>')}

        {caixa(NOTA_REG)}

        <h2>Onde o portal grande é imbatível</h2>

        <p>Vale reconhecer antes de gastar dinheiro tentando:</p>

        <ul>
          <li><strong>Termos amplos e genéricos.</strong> Anos de domínio, milhares de páginas e perfil de
          links que não se replica em um ciclo de projeto.</li>
          <li><strong>Cobertura horizontal.</strong> Estar presente em todo subtema do mercado ao mesmo
          tempo exige equipe que o portal pequeno não tem.</li>
          <li><strong>Velocidade em conteúdo de calendário.</strong> Redação dedicada publicando no dia do
          evento.</li>
          <li><strong>Autoridade de marca.</strong> Gente que pesquisa o portal pelo nome.</li>
        </ul>

        <p>Disputar de frente qualquer um desses itens é o erro mais caro de portal iniciante.</p>

        <h2>Onde o portal pequeno ganha</h2>

        <h3>1. Profundidade em recorte estreito</h3>
        <p>O portal grande cobre tudo superficialmente porque precisa cobrir tudo. Um portal pequeno pode
        cobrir <strong>uma categoria por completo</strong> — todas as opções, todos os comparativos, todas
        as dúvidas periféricas — com uma profundidade que o grande não tem incentivo para igualar.</p>

        <p>Nessa categoria específica, o pequeno passa a ser a melhor resposta disponível. E cobertura
        completa de um recorte constrói relevância temática reconhecível, que depois se expande.</p>

        <h3>2. Atualização</h3>
        <p>Este é o ponto fraco estrutural das operações grandes. Manter centenas de páginas atualizadas é
        caro, e conteúdo desatualizado é comum mesmo em portais estabelecidos. Um portal com trinta páginas
        corretas e datadas supera um com trezentas desatualizadas — e o leitor deste setor procura pela
        data.</p>

        <h3>3. Informação própria</h3>
        <p>Conteúdo produzido em escala tende a repetir o material oficial. Informação que exigiu trabalho
        para descobrir — detalhe de funcionamento, condição específica, limitação que ninguém menciona — é
        o que diferencia, e é onde a operação pequena consegue ser melhor.</p>

        <h3>4. Honestidade editorial</h3>
        <p>Apontar limitações reais aumenta credibilidade e tempo de permanência. Operações grandes,
        com muitas parcerias comerciais simultâneas, têm mais dificuldade em fazer isso.</p>

        <h2>Comparação de porte</h2>

        {tabela(
            ["Dimensão", "Portal grande", "Portal pequeno", "Onde disputar"],
            [
                ["Cobertura de mercado", "ampla", "estreita", "não disputar"],
                ["Autoridade de domínio", "alta", "em construção", "não disputar"],
                ["Termos amplos", "domina", "inviável no início", "não disputar"],
                ["Profundidade por recorte", "média", "pode ser alta", "disputar"],
                ["Atualização", "irregular", "pode ser alta", "disputar"],
                ["Informação própria", "baixa em escala", "pode ser alta", "disputar"],
                ["Cauda longa específica", "cobre parcialmente", "pode cobrir bem", "disputar"],
            ],
            nota="A coluna da direita é a estratégia inteira: escolher as quatro linhas onde o porte não decide."
        )}

        <h2>O que é obrigatório ter para competir</h2>

        <p>Independentemente do porte, alguns itens não são opcionais:</p>

        <ol>
          <li><strong>Estrutura que suporte crescer.</strong> Hierarquia, padrão de endereços e informação
          volátil armazenada em um lugar só — ver
          {link('/criacao-de-site-para-afiliado-de-bet/', 'criação de site para afiliado')}.</li>
          <li><strong>Camadas com intenção separada.</strong> Avaliação, comparativo e página de condições
          não podem virar três textos parecidos.</li>
          <li><strong>Calendário de revisão.</strong> Sem isso, a vantagem de atualização se perde no
          segundo trimestre.</li>
          <li><strong>Construção de autoridade constante.</strong> Não para vencer o grande, mas para
          sustentar os recortes conquistados.</li>
          <li><strong>Rastreamento por página.</strong> Para saber onde a receita realmente vem.</li>
          <li><strong>Comunicação sóbria.</strong> Sem apelo ao jogo e sem promessa de ganho — postura
          correta e conteúdo mais durável quando as regras de publicidade mudam.</li>
        </ol>

        <h2>A sequência para expandir</h2>

        <p>Depois de dominar um recorte, a expansão não é aleatória:</p>

        <ol>
          <li>Escolher um recorte <strong>adjacente</strong>, que aproveite a relevância já construída.</li>
          <li>Cobri-lo com a mesma profundidade.</li>
          <li>Conectar os dois por links internos, para a força circular.</li>
          <li>Repetir, até que o conjunto sustente a disputa de termos mais amplos.</li>
        </ol>

        <p>É mais lento de descrever e mais rápido de acontecer que tentar cobrir o mercado inteiro desde
        o começo. A sequência de execução completa está em
        {link('/blog/seo-para-afiliados-como-estruturar-projeto/', 'como estruturar o projeto de um portal de afiliado')}.</p>
    """,
    "faq": [
        ("Quanto tempo até um portal pequeno gerar receita?",
         "Depende do recorte escolhido e do ritmo de execução. Recortes específicos costumam responder "
         "antes que termos amplos, e é justamente por isso que a estratégia começa por eles — para gerar "
         "receita durante a construção."),
        ("Vale a pena entrar se o mercado já tem portais consolidados?",
         "Vale, desde que a entrada seja por recorte e não por termo amplo. Mercado consolidado costuma "
         "ter cobertura rasa em vários subtemas — e é aí que projeto novo entra."),
        ("Preciso cobrir todas as opções do mercado?",
         "Não no começo, e talvez nunca. Cobrir bem as opções mais procuradas de uma categoria rende mais "
         "que cobrir superficialmente todas as categorias."),
        ("Um portal pequeno consegue conseguir bons backlinks?",
         "Consegue, em ritmo menor e com critério. A vantagem é que conteúdo com informação própria e "
         "profundidade real é mais fácil de referenciar que página genérica — o que reduz o custo por "
         "conquista."),
    ],
    "cta": ("Quer saber quais recortes do seu mercado são disputáveis com o seu porte? Na análise do "
            "projeto eu levanto onde há demanda real com cobertura fraca e devolvo o plano de entrada.",
            ANALISE, "Solicitar análise do projeto"),
})
