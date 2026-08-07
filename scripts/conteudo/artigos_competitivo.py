# -*- coding: utf-8 -*-
"""
Artigos do cluster "SEO para mercados competitivos" — parte 1.

28 quanto-custa-chegar-primeira-pagina
29 e-possivel-garantir-primeira-pagina
30 o-que-e-seo-agressivo
31 seo-agressivo-funciona-em-nichos-concorridos
32 o-que-e-black-hat-seo
33 black-hat-gray-hat-white-hat-diferenca
34 o-que-e-pbn-e-como-funciona
35 pbn-ainda-funciona-para-seo
45 por-que-alguns-projetos-de-seo-precisam-de-mais-investimento
46 seo-local-ou-seo-nacional-diferenca
47 como-funciona-projeto-de-seo-para-nichos-competitivos
48 conteudo-ou-backlinks-onde-investir-primeiro

Política: black hat e PBN aparecem em posição explicativa/analítica — o que são,
por que circulam, qual o risco e o que a RCB faz no lugar. Nunca como tutorial
operacional nem como serviço oferecido (plano §2.3 e §2.4).
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-06"
CAT = "Mercados competitivos"
ANALISE = "/analise-de-projeto/"

ARTIGOS = []


# ------------------------------------------------------------------
# 28
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quanto-custa-chegar-primeira-pagina",
    "h1": "Quanto custa chegar à primeira página do Google?",
    "title": "Quanto custa chegar à primeira página do Google? | RCB",
    "desc": ("Por que não existe preço de tabela para primeira página, quais fatores formam o custo "
             "real de um projeto e como estimar o investimento do seu caso."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-mercados-competitivos/", "Mercados competitivos"),
    "corpo": f"""
        <p>A resposta honesta é que não existe um preço. Existe um <strong>custo de execução</strong>, e
        ele varia tanto entre um caso e outro que qualquer número dito antes de olhar a sua concorrência
        seria invenção.</p>

        {caixa('<p><strong>Resposta direta:</strong> o custo de chegar à primeira página é proporcional '
               'à distância entre o seu site e os que já estão lá. Quem define essa distância não é o seu '
               'orçamento — é a quantidade de conteúdo, autoridade e tempo que os concorrentes já acumularam. '
               'Por isso o mesmo objetivo pode custar alguns milhares em um nicho e valores muito superiores '
               'em outro.</p>')}

        <h2>Por que ninguém consegue dar um preço por telefone</h2>

        <p>"Primeira página" não é um produto. É uma posição relativa em uma disputa que muda por termo,
        por região e por mês. Chegar à primeira página de uma busca com três concorrentes mal estruturados
        é trabalho de semanas. Chegar à primeira página de uma busca disputada por marcas com equipes
        internas e anos de acúmulo é projeto de trimestres — e mesmo assim sem garantia.</p>

        <p>Quando alguém oferece um valor fechado sem ter olhado a busca que você quer disputar, uma de
        duas coisas está acontecendo: ou o preço embute uma margem enorme para cobrir o desconhecido, ou
        o que vai ser entregue não tem relação com o objetivo prometido.</p>

        <h2>Os seis fatores que realmente formam o custo</h2>

        <h3>1. Quem já ocupa a primeira página</h3>
        <p>É o fator de maior peso, e o mais ignorado. Abra a busca que você quer disputar e olhe os dez
        resultados. Se forem domínios antigos, com centenas de páginas sobre o tema e perfil de links
        robusto, o custo de entrar nessa lista é alto — porque você vai precisar construir algo comparável.
        Se houver fóruns, redes sociais e páginas desatualizadas no meio, existe brecha, e o custo cai
        bastante.</p>

        <h3>2. O ponto de partida do seu projeto</h3>
        <p>Um site que já existe, já tem conteúdo e já é indexado parte de um lugar. Um projeto que começa
        sem marca, sem domínio e sem site parte de outro — e a construção dessa base é parte do custo.</p>

        <h3>3. O volume de conteúdo necessário</h3>
        <p>Em disputa séria, raramente basta uma página. O que costuma ranquear é <strong>cobertura</strong>:
        a página principal mais o conjunto de conteúdos que sustenta a relevância do site naquele tema.
        Quanto mais completo for o conjunto dos concorrentes, maior o volume que você precisa produzir.</p>

        <h3>4. A autoridade que precisa ser construída</h3>
        <p>Em nichos disputados, links são determinantes — e são a parte mais cara e mais lenta.
        {link('/link-building-para-nichos-competitivos/', 'Construir autoridade')} com critério custa mais
        por unidade que comprar pacotes, e é o que sustenta posição no longo prazo.</p>

        <h3>5. O prazo desejado</h3>
        <p>Apertar prazo aumenta custo, porque exige mais execução simultânea. E existe um limite: acima
        de certo ponto, mais dinheiro não compra mais velocidade, porque a resposta dos mecanismos de busca
        não é comprável.</p>

        <h3>6. A manutenção depois</h3>
        <p>Chegar não é o fim. Concorrente que continua publicando recupera terreno. O custo de manter uma
        posição conquistada costuma ser menor que o de conquistá-la, mas não é zero.</p>

        <h2>Uma forma de estimar sem chutar</h2>

        <p>Você pode fazer uma leitura aproximada antes de falar com qualquer fornecedor:</p>

        <ol>
          <li>Pesquise o termo que quer disputar e liste os dez primeiros resultados.</li>
          <li>Para cada um, veja há quanto tempo o site existe e quantas páginas ele tem sobre o tema.</li>
          <li>Observe se eles publicam com frequência — datas recentes no blog são um indicador.</li>
          <li>Estime quanto conteúdo você teria que produzir para ter cobertura equivalente.</li>
          <li>Multiplique isso pelo custo de produzir conteúdo bom no seu mercado.</li>
          <li>Some a construção de autoridade e a manutenção pelo período.</li>
        </ol>

        <p>O número que sai não é preciso, mas costuma ser suficiente para responder a pergunta mais
        importante: <strong>esse alvo cabe no seu orçamento?</strong> Se não couber, a decisão certa
        normalmente não é gastar menos no mesmo alvo — é escolher um alvo diferente.</p>

        <h2>O erro que custa mais caro que o projeto</h2>

        <p>É investir abaixo do patamar que a disputa exige. Em mercado competitivo, metade do investimento
        não entrega metade do resultado — costuma não entregar resultado nenhum, porque o projeto não
        alcança o nível mínimo de cobertura e autoridade que aquela primeira página exige.</p>

        <p>Nesse cenário, o dinheiro é gasto, o conteúdo é publicado, e o site fica na terceira página.
        É por isso que uma análise séria pode concluir que o melhor uso do seu orçamento é
        {link('/seo-para-nichos-competitivos/', 'mirar termos menos disputados primeiro')}, acumular
        tração e só depois atacar o principal.</p>

        <h2>E quando o alvo não vale o custo</h2>

        <p>Às vezes o cálculo simplesmente não fecha. Um termo pode ser caro demais para o retorno que
        traria, ou o volume pode estar concentrado em buscas que não têm intenção de compra. Nesses casos,
        a resposta útil não é uma proposta mais barata — é apontar onde está o retorno de verdade, que
        muitas vezes está em dez termos médios somados, e não no termo mais óbvio.</p>
    """,
    "faq": [
        ("Existe um valor mínimo para um projeto de SEO competitivo?",
         "Existe um patamar mínimo de execução, que varia por nicho. Abaixo dele o projeto tende a não "
         "produzir resultado — não um resultado menor. Qual é esse patamar no seu caso só dá para dizer "
         "depois de ler a concorrência dos termos que você quer disputar."),
        ("Pagar mais acelera o resultado?",
         "Até certo ponto, sim: mais verba permite mais conteúdo simultâneo e construção de autoridade mais "
         "intensa. Passado esse ponto, o limite deixa de ser dinheiro e passa a ser o tempo de resposta dos "
         "mecanismos de busca, que ninguém compra."),
        ("Por que dois fornecedores dão orçamentos tão diferentes?",
         "Geralmente porque estão propondo escopos diferentes para o mesmo objetivo. Compare o que cada um "
         "entrega — volume de conteúdo, trabalho de autoridade, execução técnica, prazo — e não só o valor. "
         "Orçamento muito abaixo dos outros costuma significar escopo muito menor."),
        ("Vale mais a pena investir em anúncio?",
         "São coisas diferentes. Anúncio traz resultado imediato e para no dia em que a verba acaba; "
         "orgânico demora e continua. Em mercado caro, muita gente usa anúncio para validar quais termos "
         "convertem e orgânico para assumir esses termos ao longo do tempo."),
    ],
    "cta": ("Quer um número que faça sentido para o seu caso? Na análise do projeto eu leio a concorrência "
            "real dos seus termos e devolvo o escopo necessário, o cenário de prazo e a faixa de investimento "
            "— inclusive quando a conclusão é que o alvo escolhido não compensa.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 29
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "e-possivel-garantir-primeira-pagina",
    "h1": "É possível garantir primeira página no Google?",
    "title": "É possível garantir primeira página no Google? | RCB",
    "desc": ("Por que nenhum fornecedor pode garantir posição no Google, como identificar promessa "
             "vazia e o que dá para assumir de verdade em um projeto de SEO."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-mercados-competitivos/", "Mercados competitivos"),
    "corpo": f"""
        <p>Não. E quem garante está prometendo algo que não controla.</p>

        {caixa('<p><strong>Resposta direta:</strong> nenhum fornecedor de SEO tem acesso ao algoritmo do '
               'Google, influência sobre ele ou capacidade de reservar posições. O que existe é execução '
               'competente que aumenta a probabilidade de posicionamento — o que é bem diferente de garantia. '
               'Promessa de primeira página garantida é o sinal de alerta mais confiável do mercado.</p>')}

        <h2>Por que a garantia é impossível</h2>

        <p>Três razões, todas estruturais:</p>

        <p><strong>O ranqueamento é relativo.</strong> Sua posição não depende só do que você faz — depende
        do que os concorrentes fazem ao mesmo tempo. Você pode melhorar tudo e perder posição porque outro
        melhorou mais.</p>

        <p><strong>O algoritmo muda.</strong> Atualizações acontecem com frequência e mexem em nichos
        inteiros. Um site pode perder posição sem ter mudado nada.</p>

        <p><strong>A própria página de resultados muda.</strong> O Google altera formatos, adiciona blocos,
        muda a quantidade de resultados orgânicos visíveis. "Primeira página" hoje não significa o mesmo
        que significava alguns anos atrás.</p>

        <h2>Os truques por trás das "garantias"</h2>

        <p>Quando alguém garante posição, normalmente há uma armadilha na definição. Vale conhecê-las:</p>

        <ul>
          <li><strong>Termo sem disputa.</strong> Garante-se primeira página em uma busca que ninguém faz —
          frequentemente o nome da sua própria empresa, onde você já ranquearia sozinho.</li>
          <li><strong>Termo longuíssimo.</strong> Uma frase de oito palavras que tem volume de busca
          próximo de zero. Tecnicamente é primeira página; comercialmente não é nada.</li>
          <li><strong>Busca personalizada.</strong> O resultado é demonstrado no computador de quem já
          visitou o site várias vezes, onde o histórico de navegação distorce o que aparece.</li>
          <li><strong>Prazo elástico.</strong> A garantia vale "em até 12 meses", com renovação automática
          se não cumprida — o que na prática só prende o contrato.</li>
          <li><strong>Garantia de devolução impraticável.</strong> Condicionada a exigências que quase
          nunca se cumprem, como aprovar todo conteúdo em 24 horas.</li>
        </ul>

        <h2>O que dá para assumir com seriedade</h2>

        <p>A ausência de garantia de posição não significa ausência de compromisso. O que um fornecedor
        sério assume:</p>

        {tabela(
            ["Não dá para garantir", "Dá para assumir"],
            [
                ["Posição específica em um termo", "O plano de execução e o escopo acordado"],
                ["Prazo exato de ranqueamento", "O ritmo de entrega e o volume produzido"],
                ["Volume de tráfego", "A qualidade técnica do que é implementado"],
                ["Que o algoritmo não vai mudar", "A leitura correta do que mudou e a resposta a isso"],
                ["Resultado de negócio", "Medição honesta do que está e do que não está funcionando"],
            ],
            nota="A coluna da direita é verificável mês a mês. A da esquerda depende de terceiros."
        )}

        <h2>Metas de posicionamento: o meio-termo honesto</h2>

        <p>Não poder garantir não significa trabalhar sem alvo. O que substitui a garantia é uma
        <strong>meta de posicionamento com premissas explícitas</strong>: qual grupo de termos, em que
        horizonte, assumindo qual ritmo de execução e qual comportamento dos concorrentes.</p>

        <p>A diferença é que a meta vem acompanhada do raciocínio. Se ela não for atingida, dá para
        olhar as premissas e entender o que falhou — se foi execução abaixo do combinado, se um concorrente
        mudou de patamar, se houve atualização de algoritmo. Uma garantia não permite essa conversa: ela
        só produz discussão contratual.</p>

        <h2>O que perguntar antes de contratar</h2>

        <ol>
          <li>Quais termos exatamente serão trabalhados, e qual o volume de busca deles?</li>
          <li>Quem ocupa a primeira página desses termos hoje?</li>
          <li>O que exatamente será entregue por mês, em quantidade e em tipo?</li>
          <li>Como o progresso será medido antes de as posições principais se moverem?</li>
          <li>O que acontece se a meta não for atingida — qual a conversa prevista?</li>
        </ol>

        <p>Fornecedor que responde essas cinco perguntas com clareza está vendendo trabalho. Quem desconversa
        e volta para a promessa de primeira página está vendendo expectativa.</p>
    """,
    "faq": [
        ("Vi um contrato que devolve o dinheiro se não chegar à primeira página. É seguro?",
         "Leia as condições com atenção. Costuma haver exigências que transferem a responsabilidade para "
         "você — prazos de aprovação curtíssimos, obrigação de aceitar todo conteúdo proposto, definição "
         "vaga de qual termo vale. Além disso, receber o dinheiro de volta não devolve os meses perdidos."),
        ("Então como sei se estou contratando alguém competente?",
         "Pelo diagnóstico, não pela promessa. Quem entende do assunto consegue explicar por que você não "
         "ranqueia hoje, quem são os concorrentes reais e o que precisaria ser feito — antes de falar de "
         "preço. Quem começa pelo preço e pela garantia geralmente pulou o diagnóstico."),
        ("É possível estimar prazo com alguma precisão?",
         "É possível estimar cenários, com as premissas escritas. Termos de menor disputa costumam responder "
         "antes; termos principais dependem de conteúdo e autoridade acumulados. Estimativa com premissa "
         "explícita é útil; data cravada é ficção."),
    ],
    "cta": ("Prefere um diagnóstico a uma promessa? Na análise do projeto eu digo por que você não "
            "ranqueia hoje, quem realmente ocupa as posições que você quer e o que seria preciso para "
            "disputá-las — com metas e premissas escritas, não com garantia.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 30
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "o-que-e-seo-agressivo",
    "h1": "O que é SEO agressivo?",
    "title": "O que é SEO agressivo? Intensidade × risco | RCB",
    "desc": ("SEO agressivo descreve duas coisas muito diferentes: execução intensa e técnicas de "
             "risco. Entenda a diferença antes de contratar."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>"SEO agressivo" não tem definição técnica. É um termo de mercado, usado para descrever duas
        práticas que não se parecem em nada — e confundir as duas é caro.</p>

        {caixa('<p><strong>Resposta direta:</strong> SEO agressivo pode significar (a) execução de alta '
               'intensidade — muito conteúdo, muito rápido, com construção de autoridade constante — ou '
               '(b) técnicas que violam as diretrizes de busca em troca de resultado rápido. A primeira é '
               'cara e legítima. A segunda é arriscada e pode custar o domínio. Quem contrata precisa saber '
               'qual das duas está comprando.</p>')}

        <h2>Acepção 1: intensidade de execução</h2>

        <p>Nesta leitura, agressivo é sinônimo de <strong>ritmo</strong>. O projeto faz em três meses o
        que um projeto convencional faria em doze:</p>

        <ul>
          <li>Publicação em volume muito acima da média do nicho, de forma sustentada.</li>
          <li>Cobertura completa de um tema — pilar, subtemas e dúvidas periféricas — em vez de páginas avulsas.</li>
          <li>Correção técnica imediata, sem esperar ciclo de desenvolvimento.</li>
          <li>Construção de autoridade contínua, começando cedo.</li>
          <li>Revisão e consolidação do conteúdo antigo que esteja atrapalhando.</li>
        </ul>

        <p>Nada disso viola diretriz nenhuma. É simplesmente caro, porque exige processo de produção real
        e equipe disponível. É o que a RCB entende por
        {link('/seo-agressivo/', 'projeto de alta intensidade')}.</p>

        <h2>Acepção 2: técnicas de risco</h2>

        <p>Nesta leitura, agressivo significa <strong>aceitar risco de penalização</strong> em troca de
        velocidade. Entram aqui redes privadas de sites, compra de links em escala, geração de conteúdo em
        massa sem revisão e manipulação de sinais.</p>

        <p>Essas técnicas às vezes funcionam por um período. O problema é o formato do risco: elas não
        entregam um resultado ligeiramente pior quando dão errado — elas costumam derrubar o domínio
        inteiro, e a recuperação pode não acontecer. Quem carrega esse risco é o dono do site, não quem
        vendeu o serviço.</p>

        <h2>Como distinguir na prática</h2>

        {tabela(
            ["Pergunta", "Execução intensa", "Técnica de risco"],
            [
                ["De onde vêm os links?", "veículos identificáveis, com audiência", "não é dito com clareza"],
                ["Dá para ver o que foi feito?", "sim, com endereços e datas", "relatório genérico ou métrica própria"],
                ["O que acontece numa atualização?", "oscilação normal", "risco de queda severa"],
                ["O custo vem de quê?", "horas de produção e prospecção", "compra de ativos e volume"],
                ["Funciona se o Google apertar?", "sim, é o comportamento esperado", "é exatamente o alvo do aperto"],
            ],
            nota="Se o fornecedor não consegue mostrar de onde vem cada link, a resposta já apareceu."
        )}

        <h2>A pergunta que resolve a dúvida</h2>

        <p>Antes de fechar contrato, pergunte: <em>"me mostra exatamente onde os links vão aparecer?"</em></p>

        <p>Quem trabalha com execução intensa responde com nomes de veículos, exemplos de contexto e
        critério de seleção. Quem trabalha com técnica de risco desconversa, fala em "rede própria",
        "parceiros exclusivos" ou apresenta uma planilha com métricas e sem endereços.</p>

        <h2>Velocidade sem imprudência: o que realmente encurta prazo</h2>

        <p>Descontando promessa de vendedor, quatro coisas mudam prazo de forma consistente e sem risco:</p>

        <ol>
          <li><strong>Ponto de partida melhor</strong> — um domínio com histórico limpo e relevante parte
          de outro lugar. Avaliado em
          {link('/analise-de-dominios-expirados/', 'análise de domínios expirados')}.</li>
          <li><strong>Alvo mais inteligente</strong> — atacar termos de disputa média primeiro e avançar
          depois costuma ser mais rápido que enfrentar o termo mais difícil de cara.</li>
          <li><strong>Ritmo executado de verdade</strong> — projeto que atrasa aprovação atrasa resultado
          na mesma proporção.</li>
          <li><strong>Consistência</strong> — seis meses constantes rendem mais que dois intensos seguidos
          de quatro parados.</li>
        </ol>

        <p>O que não encurta: pagar mais por risco. Isso aumenta a variância, não a média — melhora a
        chance de resultado rápido e cria a chance de perder tudo.</p>
    """,
    "faq": [
        ("SEO agressivo é o mesmo que black hat?",
         "Não. Agressivo descreve intensidade de execução; black hat descreve violação de diretrizes. Dá "
         "para ser extremamente agressivo em ritmo sem usar nenhuma técnica proibida — e é isso que "
         "projetos sérios em nichos duros fazem."),
        ("Estratégia agressiva aumenta o risco de penalização?",
         "Só se envolver técnicas de risco. Publicar muito conteúdo bom e conquistar links relevantes não "
         "cria exposição. O risco aparece em padrões artificiais: aquisição de links em lote, âncoras "
         "concentradas, conteúdo gerado sem revisão."),
        ("Quanto custa um projeto de alta intensidade?",
         "Mais que um projeto convencional, porque o custo acompanha o volume de execução. O que define a "
         "faixa é o ritmo acordado, o ponto de partida e a intensidade da construção de autoridade."),
    ],
    "cta": ("Quer acelerar sem colocar o domínio em risco? Na análise do projeto eu digo o que dá para "
            "acelerar no seu caso, quanto isso custa e qual cenário de prazo é realista.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 31
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "seo-agressivo-funciona-em-nichos-concorridos",
    "h1": "SEO agressivo funciona em nichos concorridos?",
    "title": "SEO agressivo funciona em nicho concorrido? | RCB",
    "desc": ("Em mercados disputados, intensidade de execução é quase obrigatória — mas ela resolve "
             "certos gargalos e não resolve outros. Entenda quais."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>Funciona, com uma ressalva importante: intensidade resolve alguns gargalos e não resolve outros.
        Aplicar mais força no gargalo errado só gasta dinheiro mais rápido.</p>

        {caixa('<p><strong>Resposta direta:</strong> em nicho concorrido, execução intensa costuma ser '
               'necessária — mas não suficiente. Ela resolve falta de cobertura e falta de ritmo. Não '
               'resolve falta de autoridade (que depende de tempo além de esforço), nem alvo mal escolhido, '
               'nem problema estrutural do site.</p>')}

        <h2>O que a intensidade resolve bem</h2>

        <h3>Falta de cobertura</h3>
        <p>É o gargalo mais comum e o que melhor responde a volume. Se os concorrentes têm cem conteúdos
        sobre o tema e você tem oito, produzir muito e rápido fecha essa distância de forma direta.</p>

        <h3>Falta de ritmo</h3>
        <p>Sites que publicam de forma irregular ficam para trás de quem publica sempre. Estabelecer e
        sustentar cadência é puro problema de processo — e processo se resolve com investimento.</p>

        <h3>Dívida técnica acumulada</h3>
        <p>Problemas de indexação, desempenho e estrutura muitas vezes estão parados há meses por falta de
        prioridade. Um projeto intenso resolve isso em semanas.</p>

        <h2>O que a intensidade não resolve</h2>

        <h3>Autoridade</h3>
        <p>Esta é a limitação mais importante de entender. Construção de autoridade tem um componente
        temporal que não é comprimível: adquirir muitos links em pouco tempo cria um padrão que trabalha
        contra você. Dá para acelerar dentro de um limite, e o limite é dado pelo que parece natural para
        um site do seu tamanho e idade.</p>

        <p>Por isso, em nicho onde o gargalo é autoridade,
        {link('/link-building-para-nichos-competitivos/', 'a construção precisa começar cedo')} e seguir
        constante — não intensa e concentrada.</p>

        <h3>Alvo mal escolhido</h3>
        <p>Se o termo escolhido é dominado por portais gigantes ou tem intenção incompatível com o seu
        negócio, nenhuma quantidade de execução resolve. O trabalho aqui é de
        {link('/seo-para-nichos-competitivos/', 'leitura da disputa')}, não de volume.</p>

        <h3>Produto ou oferta que não converte</h3>
        <p>SEO leva gente até a página. Se a página não convence, mais tráfego só amplia o desperdício.
        Vale checar a conversão antes de multiplicar a visita.</p>

        <h2>Como saber qual é o seu gargalo</h2>

        {tabela(
            ["Sintoma", "Gargalo provável", "Intensidade resolve?"],
            [
                ["Poucas páginas indexadas sobre o tema", "cobertura", "sim, diretamente"],
                ["Publicação irregular", "ritmo", "sim"],
                ["Páginas na posição 15–30 há meses", "autoridade", "parcialmente, e com tempo"],
                ["Tráfego que não vira contato", "conversão", "não"],
                ["Nenhum movimento em nenhum termo", "técnico ou alvo", "não, antes de diagnosticar"],
                ["Concorrente novo passou na frente", "cobertura ou ritmo", "sim"],
            ],
            nota="Mais de um gargalo ao mesmo tempo é o cenário mais comum — o que muda é a ordem de ataque."
        )}

        <h2>A sequência que costuma funcionar</h2>

        <p>Em nicho duro, a ordem importa tanto quanto a intensidade:</p>

        <ol>
          <li><strong>Resolver o técnico primeiro.</strong> Publicar sobre base quebrada desperdiça produção.</li>
          <li><strong>Começar a autoridade cedo.</strong> Ela é a mais lenta, então precisa do maior prazo.</li>
          <li><strong>Atacar cobertura com volume.</strong> É onde a intensidade rende mais.</li>
          <li><strong>Mirar termos médios antes dos principais.</strong> Tração inicial sustenta o resto.</li>
          <li><strong>Consolidar o que já existe.</strong> Muitas vezes há conteúdo antigo competindo internamente.</li>
        </ol>

        <p>Projetos que fazem tudo ao mesmo tempo, com força máxima, costumam gastar muito e conseguir
        menos do que projetos que respeitam essa ordem.</p>
    """,
    "faq": [
        ("Dá para compensar falta de autoridade com muito conteúdo?",
         "Até certo ponto. Cobertura ampla e profunda melhora a percepção de relevância temática do site e "
         "rende bem em termos de menor disputa. Nos termos principais de nicho duro, porém, a autoridade "
         "costuma ser o fator que decide — e ela não é substituível por volume."),
        ("Quanto tempo até ver se a intensidade está funcionando?",
         "Os indicadores que se movem primeiro são indexação e número de termos únicos gerando impressão. "
         "Eles respondem em semanas e mostram se o conteúdo está sendo reconhecido, muito antes de as "
         "posições principais mudarem."),
        ("Vale começar intenso e depois reduzir?",
         "Costuma ser o desenho certo: fase de construção mais pesada, seguida de manutenção. O que não "
         "funciona é parar por completo — concorrente que continua publicando recupera terreno."),
    ],
    "cta": ("Quer saber qual é o gargalo do seu projeto antes de investir em volume? Na análise eu comparo "
            "a sua cobertura com a dos concorrentes que estão à frente e aponto se o problema é conteúdo, "
            "estrutura ou autoridade.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 32
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "o-que-e-black-hat-seo",
    "h1": "O que é black hat SEO?",
    "title": "O que é black hat SEO? Técnicas e riscos | RCB",
    "desc": ("O que o mercado chama de black hat, por que essas técnicas ainda circulam e o que "
             "costuma acontecer com quem depende delas."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>Black hat SEO é o nome que o mercado dá ao conjunto de práticas que buscam posição violando as
        diretrizes dos mecanismos de busca — em vez de atender ao que elas pedem.</p>

        {caixa('<p><strong>Este artigo é explicativo.</strong> Ele descreve o que essas técnicas são e '
               'qual o risco de depender delas, porque clientes perguntam e informação boa é melhor que '
               'desinformação. Não é um guia de execução, e nenhuma dessas práticas faz parte dos serviços '
               'da RCB.</p>')}

        <h2>A fronteira: o que define black hat</h2>

        <p>A linha não é "o que funciona" contra "o que não funciona" — várias dessas técnicas já
        funcionaram muito bem. A linha é <strong>a intenção de manipular sinais em vez de merecê-los</strong>.</p>

        <p>Se uma prática só faz sentido porque o mecanismo de busca ainda não a detectou, ela é frágil por
        construção: o dia em que for detectada, ela deixa de funcionar e frequentemente passa a prejudicar.</p>

        <h2>As categorias mais conhecidas</h2>

        <h3>Manipulação de links</h3>
        <p>Compra de links em escala, esquemas de troca recíproca e redes privadas de sites criadas só para
        apontar para os próprios projetos. É a categoria mais ativa, porque links continuam sendo um sinal
        importante. Detalhado em {link('/blog/o-que-e-pbn-e-como-funciona/', 'o que é uma PBN')}.</p>

        <h3>Conteúdo enganoso</h3>
        <p>Texto escondido, repetição excessiva de termos, conteúdo copiado ou gerado em massa sem revisão
        e páginas criadas apenas para capturar busca e empurrar o visitante para outro lugar.</p>

        <h3>Cloaking</h3>
        <p>Mostrar um conteúdo para o mecanismo de busca e outro para a pessoa. É uma das violações mais
        diretas, porque contradiz o próprio propósito do índice.</p>

        <h3>Redirecionamento enganoso</h3>
        <p>Enviar o visitante para um destino diferente daquele que o resultado da busca indicava.</p>

        <h3>Manipulação de sinais de terceiros</h3>
        <p>Avaliações falsas, engajamento fabricado e outras formas de inventar prova social.</p>

        <h2>Por que ainda circula</h2>

        <p>Três motivos, e nenhum deles é "porque funciona melhor":</p>

        <p><strong>Funciona por um tempo.</strong> Detecção não é instantânea. Existe uma janela em que o
        resultado aparece — e é essa janela que sustenta a venda do serviço.</p>

        <p><strong>O risco é assimétrico.</strong> Quem executa recebe pelo trabalho. Quem sofre a
        consequência é o dono do domínio. Essa assimetria explica boa parte do mercado.</p>

        <p><strong>É mais barato de entregar.</strong> Produzir conteúdo bom e conquistar links relevantes
        dá trabalho. Comprar volume, não.</p>

        <h2>O que costuma acontecer depois</h2>

        <p>As consequências variam em severidade:</p>

        <ul>
          <li><strong>Desvalorização silenciosa.</strong> O mais comum. Os sinais manipulados simplesmente
          deixam de contar. Não há aviso — só o resultado que some. O dinheiro investido vira perda.</li>
          <li><strong>Queda por atualização.</strong> Um ajuste de algoritmo atinge o padrão usado e o site
          perde posição em bloco.</li>
          <li><strong>Ação manual.</strong> Uma penalização registrada, que exige correção e pedido de
          reconsideração — processo demorado e sem prazo garantido.</li>
          <li><strong>Passivo permanente.</strong> Mesmo depois de parar, o perfil de links artificial
          continua apontando para o domínio, e limpá-lo custa tempo e dinheiro.</li>
        </ul>

        <p>O ponto crítico é que a perda raramente é parcial. Um projeto construído sobre sinais
        manipulados tende a cair inteiro, porque o que sustentava a posição era exatamente o que foi
        desvalorizado.</p>

        <h2>Como identificar se estão fazendo isso no seu site</h2>

        <ol>
          <li>Peça a lista completa de links conquistados, com endereço e data. Recusa é resposta.</li>
          <li>Visite alguns desses sites. Eles têm conteúdo real? Público real? Falam do seu assunto?</li>
          <li>Veja se um mesmo grupo de sites aponta para muitos projetos diferentes e desconexos.</li>
          <li>Observe o ritmo: dezenas de domínios novos em poucas semanas é padrão artificial.</li>
          <li>Confira a distribuição de âncoras — se quase todas usam o termo comercial exato, é sinal claro.</li>
        </ol>

        <p>Se algo aí acender um alerta, uma
        {link('/consultoria-de-backlinks/', 'auditoria do perfil de links')} mede o tamanho real do
        problema antes de qualquer decisão.</p>
    """,
    "faq": [
        ("Usar black hat sempre resulta em penalização?",
         "Nem sempre em penalização formal. O desfecho mais comum é a desvalorização silenciosa: os sinais "
         "manipulados param de contar e o resultado desaparece sem aviso. O prejuízo é o mesmo, só não vem "
         "com notificação."),
        ("Meu concorrente usa e está na primeira página. Por quê?",
         "Pode estar na janela em que ainda funciona, pode ter outros ativos sustentando a posição, ou pode "
         "não estar usando o que parece. Vale lembrar que você vê o resultado atual, não o que acontece "
         "depois — e não vê os projetos que já caíram."),
        ("Dá para reverter os efeitos?",
         "Depende do caso. Perfis de links artificiais podem ser trabalhados com desautorização e diluição; "
         "conteúdo problemático pode ser removido ou reescrito. Ação manual exige correção e pedido de "
         "reconsideração, sem prazo garantido. Em casos graves, começar em outro domínio sai mais barato."),
    ],
    "cta": ("Desconfia do que foi feito no seu site? Na análise do projeto eu faço uma primeira leitura do "
            "perfil de links e do conteúdo e indico se há sinal de risco que justifique auditoria completa.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 33
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "black-hat-gray-hat-white-hat-diferenca",
    "h1": "Black hat, gray hat e white hat: qual é a diferença?",
    "title": "Black hat, gray hat e white hat: a diferença | RCB",
    "desc": ("As três categorias de prática em SEO, onde fica a fronteira entre elas e por que a "
             "zona cinzenta é a que mais confunde quem contrata."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>As três expressões classificam práticas de SEO pela relação com as diretrizes dos mecanismos de
        busca. Elas são úteis como vocabulário e enganosas como certeza — porque a fronteira real é bem
        menos nítida do que os nomes sugerem.</p>

        {caixa('<p><strong>Resposta direta:</strong> white hat segue as diretrizes; black hat as viola '
               'deliberadamente; gray hat fica na zona ambígua, sem violação clara mas com risco real. A '
               'maior parte do mercado opera em algum ponto do cinza — e é justamente aí que quem contrata '
               'precisa saber o que está comprando.</p>')}

        <h2>White hat</h2>

        <p>Práticas alinhadas ao que os mecanismos de busca pedem: conteúdo que responde de fato à busca,
        estrutura técnica que facilita o rastreamento, boa experiência de uso e links conquistados por
        mérito editorial.</p>

        <p>A crítica comum é que seria lento demais para nicho competitivo. Isso confunde white hat com
        pouca intensidade. Dá para ser {link('/seo-agressivo/', 'extremamente agressivo em ritmo')} sem sair
        das diretrizes — o que muda é o custo, não a categoria.</p>

        <h2>Black hat</h2>

        <p>Práticas que buscam manipular sinais em vez de merecê-los: redes privadas de sites, compra de
        links em escala, cloaking, conteúdo enganoso, redirecionamento fraudulento. Detalhado em
        {link('/blog/o-que-e-black-hat-seo/', 'o que é black hat SEO')}.</p>

        <h2>Gray hat: onde mora a confusão</h2>

        <p>É a categoria mais relevante na prática, porque quase todo o mercado transita por ela. São
        práticas que não violam uma regra explícita, mas cuja intenção é claramente influenciar o
        ranqueamento — e que podem ser reclassificadas a qualquer momento.</p>

        <p>Exemplos frequentes:</p>

        <ul>
          <li><strong>Conteúdo patrocinado com link</strong> em veículos reais, sem sinalização adequada.</li>
          <li><strong>Guest post em escala</strong>, produzido primariamente para o link e não para o leitor.</li>
          <li><strong>Compra de domínios expirados</strong> para redirecionar ou reconstruir. Ver
          {link('/analise-de-dominios-expirados/', 'análise de domínios expirados')}.</li>
          <li><strong>Reaproveitamento intenso de conteúdo</strong> entre páginas com pequenas variações.</li>
          <li><strong>Conteúdo gerado por IA</strong> publicado com revisão superficial.</li>
        </ul>

        <p>O risco do cinza não é ser pego hoje — é a régua se mover. Práticas comuns há alguns anos hoje
        são tratadas como problema, e projetos construídos sobre elas foram junto.</p>

        <h2>Comparação prática</h2>

        {tabela(
            ["", "White hat", "Gray hat", "Black hat"],
            [
                ["Alinhamento às diretrizes", "sim", "ambíguo", "viola"],
                ["Velocidade", "depende do investimento", "moderada a alta", "alta no curto prazo"],
                ["Custo por resultado", "alto", "médio", "baixo até dar errado"],
                ["Durabilidade", "alta", "incerta", "baixa"],
                ["Risco de perda total", "muito baixo", "existe", "alto"],
                ["Quem carrega o risco", "—", "o dono do domínio", "o dono do domínio"],
            ],
            nota="Em todas as colunas, quem responde pelo prejuízo é quem é dono do site — não quem executou."
        )}

        <h2>Como decidir onde você quer estar</h2>

        <p>A pergunta útil não é "isso é black hat?". É: <strong>quanto vale o meu domínio, e o que
        acontece se ele parar de ranquear?</strong></p>

        <p>Para um projeto descartável, aceitar risco alto pode ser uma decisão de negócio consciente.
        Para uma operação que pretende existir por anos, construir sobre base frágil é um péssimo negócio —
        porque o valor acumulado é justamente o que se perde.</p>

        <p>Duas perguntas ajudam a decidir qualquer prática específica:</p>

        <ol>
          <li>Se isso virasse público, seria constrangedor explicar?</li>
          <li>Isso continuaria fazendo sentido se não trouxesse nenhum benefício de ranqueamento?</li>
        </ol>

        <p>Prática que passa nas duas costuma ser segura. Que falha nas duas costuma ser black hat com
        outro nome. Que passa em uma só é cinza — e aí a decisão precisa ser consciente, não acidental.</p>
    """,
    "faq": [
        ("Gray hat é seguro?",
         "É menos arriscado que black hat e mais arriscado que white hat — e o risco não é estático. O que "
         "hoje está na zona cinzenta pode ser reclassificado, e projetos construídos sobre isso perdem "
         "posição sem ter mudado nada."),
        ("Conteúdo gerado por IA é black hat?",
         "Não por si só. O que importa é o resultado: conteúdo útil, verificado e revisado tende a ser "
         "tratado como qualquer outro conteúdo. Publicação em massa sem revisão, feita só para ocupar "
         "espaço no índice, é o que cria problema."),
        ("Como saber em qual categoria meu fornecedor atua?",
         "Peça a lista de links com endereços e datas, e pergunte como cada um foi conseguido. Quem atua "
         "no branco ou no cinza claro responde sem hesitar. Quem atua no escuro fala em rede própria, "
         "parceiros exclusivos ou método proprietário."),
    ],
    "cta": ("Quer saber em que categoria está o trabalho feito no seu site? Na análise do projeto eu faço "
            "a leitura do perfil de links e do conteúdo e aponto onde há risco — antes de qualquer proposta.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 34
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "o-que-e-pbn-e-como-funciona",
    "h1": "O que é PBN e como ela funciona?",
    "title": "O que é PBN (rede privada de blogs)? | RCB Consultoria",
    "desc": ("O que é uma rede privada de sites, por que ela foi criada, como costuma ser montada "
             "e quais os riscos para quem depende dela."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>PBN é a sigla de <em>private blog network</em> — rede privada de blogs, ou rede privada de sites.
        É um conjunto de sites controlados pela mesma pessoa ou empresa, cuja função principal é apontar
        links para um site de destino.</p>

        {caixa('<p><strong>Este artigo é explicativo.</strong> Ele descreve o conceito, a lógica por trás '
               'dele e os riscos envolvidos, porque é uma das perguntas mais frequentes de quem contrata '
               'SEO em nicho competitivo. Não é um guia de montagem, e a RCB não constrói nem opera PBN.</p>')}

        <h2>A lógica por trás da ideia</h2>

        <p>Links continuam sendo um sinal relevante de relevância e confiança. Conquistar links de veículos
        reais dá trabalho: exige conteúdo que mereça referência, prospecção e negociação.</p>

        <p>A PBN pula essa etapa. Em vez de convencer sites de terceiros, o operador <strong>controla os
        próprios sites</strong> e coloca os links onde quiser, quando quiser, com o texto que quiser. É a
        tentativa de transformar um sinal de confiança externa em algo administrável internamente.</p>

        <h2>Como essas redes costumam ser montadas</h2>

        <p>Em linhas gerais, o padrão é: adquirir domínios que já tiveram uso e carregam algum histórico
        de links, republicar conteúdo neles para parecerem sites ativos, e distribuir os links para os
        projetos de destino — tentando disfarçar que tudo pertence ao mesmo dono.</p>

        <p>É justamente esse disfarce que define o modelo. Uma rede que não esconde a propriedade comum
        não funciona para o propósito pretendido, porque o padrão fica evidente.</p>

        <h2>Por que é detectável</h2>

        <p>O disfarce é difícil de sustentar em escala. Os sinais que denunciam uma rede são muitos, e
        errar em qualquer um deles compromete o conjunto:</p>

        <ul>
          <li><strong>Padrões de infraestrutura</strong> — hospedagem, configuração e registros que se repetem.</li>
          <li><strong>Padrões de publicação</strong> — mesma estrutura, mesmo ritmo, mesma origem de conteúdo.</li>
          <li><strong>Padrão de saída</strong> — sites que apontam para um conjunto pequeno e desconexo de projetos.</li>
          <li><strong>Ausência de audiência</strong> — sites sem visitantes reais, sem menções e sem tráfego de marca.</li>
          <li><strong>Ausência de links de entrada naturais</strong> — ninguém linka espontaneamente para eles.</li>
        </ul>

        <p>Manter dezenas de sites que passem em todos esses testes exige um esforço que, somado, rivaliza
        com o de produzir conteúdo bom e conquistar links de verdade — com a diferença de que o resultado
        é frágil.</p>

        <h2>Os riscos concretos</h2>

        <p><strong>Perda do investimento na rede.</strong> Quando a rede é desvalorizada, os domínios,
        a hospedagem e o conteúdo produzido viram custo afundado.</p>

        <p><strong>Perda de posição do site de destino.</strong> Se a posição era sustentada por esses links,
        ela cai junto — e o site de destino é o ativo que interessa.</p>

        <p><strong>Passivo no perfil de links.</strong> Os links continuam apontando depois que deixam de
        contar, e limpar isso custa tempo.</p>

        <p><strong>Dependência de fornecedor.</strong> Quando a rede é de terceiros, você não controla o que
        acontece com ela. Se o operador some, os links somem — e a posição vai junto.</p>

        <p><strong>Assimetria de risco.</strong> Quem vende recebe pelo serviço prestado. Quem perde o
        domínio é você.</p>

        <h2>O que costuma ser oferecido com outro nome</h2>

        <p>Poucos fornecedores usam o termo "PBN" na proposta. As formulações mais comuns são:</p>

        <ul>
          <li>"rede própria de portais"</li>
          <li>"parceiros exclusivos"</li>
          <li>"blogs de autoridade do nosso grupo"</li>
          <li>"método proprietário de link building"</li>
        </ul>

        <p>A pergunta que esclarece é simples e direta: <em>"me manda a lista de endereços onde os links
        vão aparecer"</em>. Quem trabalha com veículos reais responde. Quem opera rede desconversa —
        porque revelar a lista é justamente o que destrói o disfarce.</p>

        <h2>A alternativa</h2>

        <p>É mais lenta e mais cara por unidade: {link('/link-building-para-nichos-competitivos/', 'construção de autoridade')}
        com seleção por relevância temática, audiência real e contexto adequado. Em compensação, o
        resultado não depende de um esquema continuar não sendo detectado.</p>
    """,
    "faq": [
        ("PBN é ilegal?",
         "Não é uma questão de legalidade — é violação de diretriz de mecanismo de busca, o que gera "
         "consequência de ranqueamento, não jurídica. O prejuízo é perder posição e perder o investimento."),
        ("Como saber se meu fornecedor usa PBN?",
         "Peça a lista de endereços onde os links aparecem. Depois visite alguns: eles têm audiência real? "
         "Publicam sobre assuntos coerentes entre si? Apontam para projetos de nichos completamente "
         "diferentes? Esse último sinal é o mais revelador."),
        ("Já usei PBN. E agora?",
         "Vale medir o tamanho da exposição antes de agir. Uma auditoria mostra que proporção do perfil "
         "vem dessas fontes e se há padrão evidente. A partir daí se decide entre diluir com aquisição de "
         "qualidade, desautorizar ou uma combinação das duas."),
    ],
    "cta": ("Quer saber se o perfil de links do seu site tem exposição a esse tipo de fonte? Na análise do "
            "projeto eu faço a primeira leitura e indico se há risco que justifique auditoria completa.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 35
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "pbn-ainda-funciona-para-seo",
    "h1": "PBN ainda funciona para SEO?",
    "title": "PBN ainda funciona para SEO em 2026? | RCB Consultoria",
    "desc": ("Por que a pergunta certa não é se PBN funciona, e sim por quanto tempo, a que custo "
             "e com qual risco para o domínio que você quer manter."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-agressivo/", "SEO agressivo"),
    "corpo": f"""
        <p>Essa é uma das perguntas mais frequentes de quem opera em nicho competitivo — e ela está mal
        formulada, o que explica por que as respostas que circulam são tão contraditórias.</p>

        {caixa('<p><strong>Resposta direta:</strong> redes privadas podem produzir movimento de posição em '
               'determinadas situações e por um período. A pergunta útil não é "funciona?", e sim "por '
               'quanto tempo, a que custo e com qual risco para o ativo que eu quero manter?". Respondida '
               'assim, a conta raramente fecha para quem está construindo algo de longo prazo.</p>')}

        <h2>Por que a resposta parece contraditória</h2>

        <p>Você encontra relatos de sucesso e relatos de desastre com a mesma técnica. Os dois são
        verdadeiros — em momentos diferentes do ciclo.</p>

        <p>O ciclo costuma ser: a rede é montada, os links começam a contar, o site sobe, o operador
        divulga o resultado. Meses ou anos depois, um ajuste de algoritmo ou uma detecção derruba o
        conjunto. O segundo momento raramente vira estudo de caso — o que enviesa toda a discussão
        pública sobre o assunto.</p>

        <p>Quem só vê a primeira metade conclui que funciona. Quem passou pela segunda conclui o contrário.</p>

        <h2>O que mudou ao longo do tempo</h2>

        <p>Três movimentos tornaram o modelo progressivamente mais frágil:</p>

        <p><strong>A detecção de padrão melhorou.</strong> Não se trata mais de identificar um site
        isolado, e sim de reconhecer conjuntos — sites que se comportam de forma parecida e apontam para
        os mesmos destinos.</p>

        <p><strong>A desvalorização substituiu a punição.</strong> Em vez de penalizar, o mais comum
        passou a ser simplesmente ignorar o sinal. Isso é pior para quem opera: não há aviso, não há o que
        corrigir, e o dinheiro já foi gasto.</p>

        <p><strong>O custo de manter o disfarce subiu.</strong> Sites que precisam parecer reais exigem
        conteúdo real, hospedagem variada e alguma audiência. Somado, isso se aproxima do custo de fazer
        o trabalho legítimo.</p>

        <h2>A conta que raramente é feita</h2>

        {tabela(
            ["", "Rede privada", "Autoridade construída"],
            [
                ["Custo inicial", "alto (domínios + estrutura)", "moderado, distribuído no tempo"],
                ["Custo de manutenção", "contínuo, para manter o disfarce", "baixo depois de conquistado"],
                ["Velocidade", "rápida enquanto funciona", "gradual"],
                ["Durabilidade", "até a próxima detecção", "acumula"],
                ["Se der errado", "perde a rede e a posição", "oscilação normal"],
                ["Quem assume o prejuízo", "o dono do site de destino", "—"],
            ],
            nota="A linha decisiva é a penúltima: o desfecho negativo não é resultado menor, é perda do que foi construído."
        )}

        <h2>Quando alguém decide usar mesmo assim</h2>

        <p>Existe um cenário em que a decisão é racional: projeto descartável, com horizonte curto, em que
        o domínio não tem valor de marca e perder tudo é um custo aceitável e previsto.</p>

        <p>Esse cenário existe e algumas pessoas operam assim conscientemente. O problema aparece quando a
        técnica é aplicada a um ativo que <em>não</em> é descartável — uma marca real, uma operação que
        pretende existir daqui a cinco anos, um negócio que depende do domínio para faturar. Aí o risco
        está mal alocado, e normalmente sem que o dono tenha entendido isso.</p>

        <h2>A pergunta que substitui a original</h2>

        <p>Em vez de "PBN ainda funciona?", pergunte:</p>

        <ol>
          <li>Quanto vale o meu domínio hoje, e quanto valerá em três anos?</li>
          <li>Se ele parar de ranquear amanhã, o que acontece com o meu faturamento?</li>
          <li>Eu tenho de onde recomeçar se isso acontecer?</li>
        </ol>

        <p>Se as respostas indicarem que o domínio é o ativo central do negócio, a discussão sobre PBN
        se encerra sozinha — independentemente de a técnica estar funcionando neste mês.</p>

        <p>A alternativa é conhecida: {link('/link-building-para-nichos-competitivos/', 'construção de autoridade com critério')},
        mais lenta e mais cara por unidade, cujo resultado não depende de um esquema continuar oculto.</p>
    """,
    "faq": [
        ("Existe forma segura de usar rede privada?",
         "Não, no sentido de eliminar o risco. É possível reduzir a chance de detecção investindo muito em "
         "disfarce, mas o risco continua existindo e o custo se aproxima do trabalho legítimo — o que "
         "remove a vantagem econômica que motivava a escolha."),
        ("Meu concorrente usa e está bem posicionado.",
         "Você está vendo o momento atual do ciclo dele, não o desfecho. E não está vendo os projetos que "
         "usaram a mesma abordagem e desapareceram — esses não aparecem em lugar nenhum, o que distorce a "
         "percepção de quem observa o mercado de fora."),
        ("Comprei links de uma rede sem saber. Como descobrir?",
         "Levante a lista de domínios que apontam para o seu site e verifique: eles têm audiência própria? "
         "Publicam sobre temas coerentes? Apontam para projetos de nichos totalmente diferentes? Uma "
         "auditoria de backlinks quantifica a exposição."),
    ],
    "cta": ("Prefere construir autoridade que não dependa de um esquema continuar funcionando? Na análise "
            "do projeto eu levanto o perfil de links de quem ocupa as posições que você quer e devolvo um "
            "plano com critério de seleção e faixa de investimento.",
            ANALISE, "Solicitar análise do projeto"),
})
