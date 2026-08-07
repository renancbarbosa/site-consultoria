# -*- coding: utf-8 -*-
"""
Artigos do cluster "Domínios e autoridade" — backlinks e link building.

36 comprar-backlinks-ajuda-no-posicionamento
37 quanto-custa-um-backlink-de-qualidade
38 como-avaliar-qualidade-de-um-backlink
49 quantos-backlinks-um-site-precisa
50 como-analisar-backlinks-dos-concorrentes

Nenhum destes textos promete quantidade de backlinks nem trata compra de links
como serviço da RCB (plano §2.1 e §2.3).
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-06"
CAT = "Domínios e autoridade"
ANALISE = "/analise-de-projeto/"

ARTIGOS = []


# ------------------------------------------------------------------
# 36
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "comprar-backlinks-ajuda-no-posicionamento",
    "h1": "Comprar backlinks ajuda no posicionamento?",
    "title": "Comprar backlinks ajuda no posicionamento? | RCB",
    "desc": ("O que realmente acontece quando se compra links, por que a maior parte do que se vende "
             "entrega pouco e qual é a alternativa que sustenta posição."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-nichos-competitivos/", "Link building"),
    "corpo": f"""
        <p>A resposta que interessa não é "sim" ou "não". É entender o que se está comprando — porque na
        maior parte das ofertas, o produto não é o que o comprador imagina.</p>

        {caixa('<p><strong>Resposta direta:</strong> comprar links pode gerar movimento de curto prazo e '
               'cria passivo de longo prazo. O problema maior nem é o risco de desvalorização: é que a '
               'maior parte do que se vende em pacote vem de sites sem audiência e sem relevância temática '
               '— ou seja, você paga por algo que entrega pouco desde o primeiro dia.</p>')}

        <h2>O que normalmente está à venda</h2>

        <p>Existe um mercado grande e organizado de venda de links. As ofertas costumam ter uma forma
        parecida: uma planilha com dezenas de sites, cada um com uma métrica de autoridade e um preço.</p>

        <p>O que a planilha não mostra:</p>

        <ul>
          <li>Se aqueles sites têm leitores de verdade.</li>
          <li>Se publicam sobre um assunto coerente ou sobre tudo.</li>
          <li>Quantos outros links comerciais já saem de cada um.</li>
          <li>Se o conteúdo que vai hospedar seu link existiria sem o pagamento.</li>
        </ul>

        <p>Um site que publica sobre advocacia, pet shop, apostas e reforma predial na mesma semana não é
        um veículo — é um espaço publicitário disfarçado. E o valor que ele transfere é proporcional a isso.</p>

        <h2>Os três desfechos possíveis</h2>

        <p><strong>1. Não acontece nada.</strong> O mais comum. Os links são desconsiderados por não terem
        relevância nem sinal de confiança. O dinheiro foi gasto, o perfil ganhou entradas inúteis e a
        posição não mudou.</p>

        <p><strong>2. Funciona por um tempo.</strong> Acontece, principalmente em nichos menos vigiados. O
        risco é que o resultado depende de aquele padrão continuar não sendo detectado.</p>

        <p><strong>3. Vira passivo.</strong> Quando o volume é grande e o padrão é evidente, o perfil do
        site passa a exibir exatamente a assinatura que sistemas antisspam procuram. Aí não é só ausência
        de ganho — é problema a resolver.</p>

        <h2>Por que a linha é confusa</h2>

        <p>Vale reconhecer que a fronteira não é nítida. Publicidade paga em veículos reais existe há
        décadas e é legítima. A diferença está na intenção e na sinalização:</p>

        {tabela(
            ["", "Publicidade legítima", "Compra de link para ranquear"],
            [
                ["Objetivo", "audiência do veículo", "transferir sinal de ranqueamento"],
                ["Veículo", "tem leitores próprios", "existe para hospedar links"],
                ["Conteúdo", "existiria de qualquer forma", "criado só para o link"],
                ["Sinalização", "identificada como publicidade", "disfarçada de editorial"],
                ["Relevância temática", "coerente com o veículo", "irrelevante para o vendedor"],
            ],
            nota="A mesma verba aplicada na coluna da esquerda costuma render mais — inclusive em tráfego direto."
        )}

        <h2>A pergunta que resolve antes de pagar</h2>

        <p>Antes de aceitar qualquer oferta, pergunte-se: <em>eu anunciaria neste site se ele não passasse
        nenhum sinal de ranqueamento?</em></p>

        <p>Se a resposta for sim — porque o público dele é o seu público — a compra faz sentido comercial
        independentemente de SEO. Se a resposta for não, você está pagando exclusivamente por um sinal que
        pode deixar de contar a qualquer momento.</p>

        <h2>A alternativa</h2>

        <p>É mais lenta e mais cara por unidade: {link('/link-building-para-nichos-competitivos/', 'construção de autoridade com critério')}
        — seleção por relevância temática, audiência real e contexto adequado, em ritmo compatível com o
        crescimento do site.</p>

        <p>Rende menos links pelo mesmo dinheiro e rende links que continuam valendo. Em projeto que
        pretende existir daqui a alguns anos, essa diferença é o que separa patrimônio de custo.</p>

        <h2>Se você já comprou</h2>

        <p>Não entre em pânico e não desautorize tudo por precaução — isso pode remover o que estava
        ajudando. O caminho é medir: uma
        {link('/consultoria-de-backlinks/', 'auditoria do perfil de links')} mostra que proporção do perfil
        vem dessas fontes e se existe padrão evidente. A partir daí se decide entre diluir com aquisição de
        qualidade, desautorizar o que for claramente problemático, ou não fazer nada.</p>
    """,
    "faq": [
        ("Meu concorrente compra links e está bem posicionado.",
         "Pode estar na janela em que ainda funciona, pode ter outros ativos sustentando a posição, ou "
         "pode não estar fazendo o que parece. Você vê o resultado atual, não o desfecho — e não vê os "
         "projetos que caíram usando a mesma abordagem."),
        ("Existe compra de link segura?",
         "Publicidade em veículo real, com público real, sinalizada como publicidade, é legítima e útil — "
         "inclusive pelo tráfego que traz. O que cria exposição é comprar volume de sites sem audiência "
         "com o único objetivo de manipular ranqueamento."),
        ("Como reconhecer uma oferta ruim?",
         "Preço por unidade muito baixo, pacotes por quantidade, métrica de autoridade alta com tráfego "
         "quase nulo, sites que publicam sobre todos os nichos e recusa em mostrar exemplos reais de "
         "onde o link vai aparecer."),
    ],
    "cta": ("Quer saber se o perfil de links do seu site tem exposição a fontes de risco? Na análise do "
            "projeto eu faço a primeira leitura e indico se há problema que justifique auditoria completa.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 37
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quanto-custa-um-backlink-de-qualidade",
    "h1": "Quanto custa um backlink de qualidade?",
    "title": "Quanto custa um backlink de qualidade? | RCB Consultoria",
    "desc": ("O que forma o preço de um link, por que a variação é tão grande entre nichos e como "
             "comparar ofertas sem olhar só o valor."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-nichos-competitivos/", "Link building"),
    "corpo": f"""
        <p>A pergunta parece simples e não tem resposta única — porque "backlink" não é um produto
        padronizado. O que se compra varia tanto que comparar preços sem comparar o que está sendo
        entregue leva a decisões ruins.</p>

        {caixa('<p><strong>Resposta direta:</strong> o preço de um link varia enormemente conforme o '
               'veículo, o nicho e a forma de conquista. O erro mais comum não é pagar caro — é comparar '
               'valores entre coisas diferentes: um link de veículo com audiência real e relevância '
               'temática não é o mesmo produto que um link de site criado para vender links, mesmo quando '
               'a métrica exibida é parecida.</p>')}

        <h2>O que forma o preço</h2>

        <h3>Audiência do veículo</h3>
        <p>Site com leitores próprios cobra mais e entrega mais — inclusive em tráfego direto, que muitas
        vezes é ignorado na conta e é o benefício mais imediato.</p>

        <h3>Relevância temática</h3>
        <p>Veículos especializados no seu setor costumam ser mais caros e mais escassos. É justamente essa
        escassez que faz link building em nichos específicos custar mais.</p>

        <h3>O nicho do comprador</h3>
        <p>Alguns setores pagam muito mais que outros pelo mesmo veículo, simplesmente porque há mais
        dinheiro disputando as mesmas posições. É o caso de
        {link('/link-building-para-bets/', 'apostas e iGaming')}, e é o oposto do que acontece em
        {link('/link-building-para-iptv/', 'nichos que muitos veículos evitam')} — onde o problema não é
        preço, é indisponibilidade.</p>

        <h3>A forma de conquista</h3>
        <p>Menção conquistada por mérito editorial custa em tempo de prospecção. Conteúdo colaborativo
        custa em produção. Publicidade sinalizada custa em mídia. São modelos de custo diferentes.</p>

        <h3>O contexto do link</h3>
        <p>Link dentro de um conteúdo relevante vale mais que link em rodapé, lista de parceiros ou texto
        genérico — e o preço costuma refletir isso quando o vendedor é sério.</p>

        <h2>Como comparar ofertas de verdade</h2>

        <p>Em vez de comparar preço por link, compare o que cada oferta entrega:</p>

        {tabela(
            ["Pergunte", "Boa resposta", "Sinal de alerta"],
            [
                ["Qual o endereço exato?", "informa sem hesitar", "'não podemos revelar'"],
                ["O site tem tráfego próprio?", "mostra evidência", "só apresenta métrica de autoridade"],
                ["Qual a linha editorial?", "assunto coerente e definido", "publica sobre tudo"],
                ["Quantos links comerciais saem de lá?", "poucos, contextuais", "não sabe ou não responde"],
                ["Como o link será inserido?", "dentro de conteúdo relevante", "'onde couber'"],
                ["O conteúdo existiria sem o link?", "sim, tem valor próprio", "criado só para hospedar"],
            ],
            nota="Duas ofertas com o mesmo preço podem ser produtos completamente diferentes."
        )}

        <h2>O cálculo que quase ninguém faz</h2>

        <p>Em vez de perguntar quanto custa um link, pergunte <strong>quanto custa a autoridade que o seu
        alvo exige</strong>.</p>

        <ol>
          <li>Levante quantos domínios distintos apontam para quem ocupa as posições que você quer.</li>
          <li>Veja de que tipo de veículo eles vêm.</li>
          <li>Estime quantas conquistas comparáveis você precisaria.</li>
          <li>Multiplique pelo custo realista de conquista no seu nicho.</li>
          <li>Distribua isso pelo prazo do projeto — porque adquirir tudo de uma vez cria padrão artificial.</li>
        </ol>

        <p>O número que sai costuma ser bem diferente do que uma tabela de preços sugere, e serve para uma
        decisão muito mais importante: se o alvo escolhido é viável com o seu orçamento.</p>

        <h2>Por que barato costuma sair caro</h2>

        <p>Link muito abaixo do preço de mercado normalmente vem de site sem audiência, criado para vender
        links. Ele não entrega valor, ocupa espaço no seu perfil e, em volume, forma um padrão que precisa
        ser gerenciado depois — o que vira custo de {link('/consultoria-de-backlinks/', 'auditoria')} que
        não estava na conta.</p>

        <p>A comparação honesta não é entre link caro e link barato. É entre <strong>link que conta</strong>
        e <strong>link que não conta</strong>.</p>
    """,
    "faq": [
        ("Existe faixa de preço de referência?",
         "Existe, mas ela varia tanto por nicho, país e tipo de veículo que citar um número aqui geraria "
         "mais confusão que ajuda. O útil é comparar ofertas pelos critérios de qualidade, não pelo valor "
         "isolado."),
        ("Vale mais um link caro ou vários baratos?",
         "Em geral, o caro de veículo relevante — desde que o preço reflita audiência e relevância reais. "
         "Vários links baratos de sites sem audiência tendem a somar pouco e a criar padrão indesejado."),
        ("O link precisa ser permanente?",
         "Idealmente sim. Links com prazo de validade somem quando o pagamento para, e a posição que "
         "dependia deles some junto. Vale confirmar isso antes de fechar, porque nem sempre é dito."),
    ],
    "cta": ("Quer saber quanto de autoridade o seu alvo exige — e a que custo? Na análise do projeto eu "
            "levanto o perfil de links de quem ocupa as posições que você quer e devolvo um plano com "
            "critério de seleção e faixa de investimento.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 38
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-avaliar-qualidade-de-um-backlink",
    "h1": "Como avaliar a qualidade de um backlink",
    "title": "Como avaliar a qualidade de um backlink | RCB",
    "desc": ("Os critérios práticos para julgar uma oportunidade de link antes de aceitar — e por "
             "que a métrica de autoridade é o pior deles isoladamente."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-nichos-competitivos/", "Link building"),
    "corpo": f"""
        <p>Existe um atalho muito usado para essa avaliação: olhar a métrica de autoridade do site e
        decidir. É o critério mais popular e o menos confiável isoladamente.</p>

        {caixa('<p><strong>Resposta direta:</strong> a qualidade de um link se define por relevância '
               'temática, audiência real do veículo e contexto em que ele aparece. Métricas de autoridade '
               'são estimativas de ferramentas de terceiros — úteis para triagem, ruins como veredito, e '
               'manipuláveis por quem quer vender.</p>')}

        <h2>Os seis critérios, em ordem de peso</h2>

        <h3>1. Relevância temática</h3>
        <p>O fator mais importante. Um link vindo de um site que trata de assunto próximo ao seu sinaliza
        muito mais do que um link de site sem relação nenhuma — mesmo que o segundo tenha métricas melhores.</p>

        <p>Relevância não exige que o veículo fale exatamente do seu produto. Exige proximidade de assunto:
        um site sobre tecnologia é relevante para uma plataforma digital; um site sobre decoração não é.</p>

        <h3>2. Audiência real</h3>
        <p>O site tem leitores? Recebe visitas? É citado por outras pessoas? Um veículo sem público
        entrega pouco, porque o link não gera nem tráfego nem sinal de confiança genuíno.</p>

        <p>Verificação rápida: procure o nome do site no Google. Se ele não aparece em lugar nenhum além
        do próprio domínio, provavelmente não tem audiência.</p>

        <h3>3. Contexto do link</h3>
        <p>Onde exatamente o link aparece muda bastante:</p>

        <ul>
          <li><strong>Melhor:</strong> dentro do corpo de um conteúdo que trata do assunto e cita você por
          um motivo.</li>
          <li><strong>Razoável:</strong> em uma lista de referências relevante ao tema.</li>
          <li><strong>Fraco:</strong> rodapé, barra lateral, lista de parceiros.</li>
          <li><strong>Ruim:</strong> texto genérico criado exclusivamente para hospedar o link.</li>
        </ul>

        <h3>4. Perfil de saída do veículo</h3>
        <p>Para onde mais aquele site aponta? Se ele distribui links comerciais para dezenas de nichos
        desconexos, o modelo de negócio dele é vender links — e associação a esse padrão entrega pouco.</p>

        <h3>5. Texto da âncora</h3>
        <p>O texto usado no link deve fazer sentido no contexto. Âncora com o termo comercial exato repetida
        muitas vezes é o padrão artificial mais fácil de identificar. Perfis naturais misturam nome da
        marca, endereço, termos genéricos e variações.</p>

        <h3>6. Métricas de autoridade</h3>
        <p>Por último, e com ressalva. Servem para <strong>filtrar</strong> candidatos rapidamente, nunca
        para decidir. São estimativas, não dados do Google, e podem ser infladas de propósito.</p>

        <h2>Comparação de dois casos</h2>

        {tabela(
            ["", "Site A", "Site B"],
            [
                ["Métrica de autoridade", "alta", "média"],
                ["Tráfego próprio", "quase nenhum", "audiência real do setor"],
                ["Tema", "publica sobre tudo", "especializado no seu assunto"],
                ["Links de saída", "muitos, comerciais", "poucos, contextuais"],
                ["Contexto do seu link", "texto criado para o link", "artigo que cita você por um motivo"],
                ["Preço", "mais barato", "mais caro"],
                ["Vale?", "não", "sim"],
            ],
            nota="Só a primeira linha favorece o site A — e é a única que aparece na maioria das propostas."
        )}

        <h2>Um checklist de cinco minutos</h2>

        <ol>
          <li>Abra o site. Ele parece feito para pessoas ou para buscadores?</li>
          <li>Leia dois artigos. Fazem sentido? Têm autoria e data?</li>
          <li>Veja os assuntos publicados. São coerentes entre si?</li>
          <li>Procure o nome do site no Google. Alguém fala dele?</li>
          <li>Olhe os links de saída de alguns artigos. Muitos são comerciais?</li>
          <li>Pergunte-se: eu anunciaria aqui se não houvesse nenhum ganho de ranqueamento?</li>
        </ol>

        <p>A última pergunta costuma resolver os casos duvidosos sozinha.</p>

        <p>Em setores onde chega proposta de link toda semana, vale conhecer também os sinais de oferta
        ruim: {link('/blog/link-building-para-bets-o-que-avaliar/', 'link building para bets: o que avaliar')}
        trata do mercado de venda de links de um dos nichos mais caros do país.</p>

        <h2>Um link ruim faz mal?</h2>

        <p>Um link ruim isolado, não — todo site acumula links que nunca pediu, e sistemas de busca lidam
        com isso desconsiderando o que não faz sentido.</p>

        <p>O problema é o <strong>padrão</strong>: muitos links de fontes fracas, adquiridos em ritmo
        incompatível com o tamanho do site, com âncoras concentradas. Aí o conjunto passa a exibir uma
        assinatura artificial. Medir isso é escopo de
        {link('/consultoria-de-backlinks/', 'auditoria de perfil de links')}.</p>
    """,
    "faq": [
        ("Qual métrica de autoridade é a mais confiável?",
         "Todas são estimativas proprietárias de ferramentas de terceiros e nenhuma reflete como o Google "
         "avalia o site. Use qualquer uma para triagem inicial e decida pelos critérios qualitativos."),
        ("Link sem seguir tem valor?",
         "Tem valor de tráfego e de visibilidade, e o tratamento desses atributos pelos buscadores é mais "
         "matizado do que se costuma dizer. Um perfil natural inclui links de tipos variados — perfil só "
         "com links de um tipo é sinal de construção artificial."),
        ("Preciso recusar links ruins que aparecem sozinhos?",
         "Normalmente não. Links espontâneos de baixa qualidade acontecem com qualquer site e tendem a ser "
         "simplesmente ignorados. Agir sobre eles sem necessidade cria mais risco que o problema original."),
    ],
    "cta": ("Recebeu uma proposta de link building e quer uma segunda opinião? Na análise do projeto eu "
            "avalio as fontes oferecidas pelos critérios de relevância, audiência e contexto — antes de "
            "você pagar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 49
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quantos-backlinks-um-site-precisa",
    "h1": "Quantos backlinks um site precisa?",
    "title": "Quantos backlinks um site precisa? | RCB Consultoria",
    "desc": ("Por que não existe número mágico, como calcular a referência comparativa do seu caso "
             "e o que importa mais que a quantidade."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-nichos-competitivos/", "Link building"),
    "corpo": f"""
        <p>É a pergunta mais frequente sobre autoridade e parte de uma premissa que não se sustenta: a de
        que links são unidades intercambiáveis que se somam até atingir um total.</p>

        {caixa('<p><strong>Resposta direta:</strong> não existe número. A referência útil é comparativa — '
               'quantos <em>domínios distintos</em> apontam para quem ocupa as posições que você quer, e de '
               'que tipo de site eles vêm. Esse levantamento é específico por termo e muda ao longo do tempo.</p>')}

        <h2>Por que a pergunta está mal formulada</h2>

        <p>Três razões:</p>

        <p><strong>Links não são equivalentes.</strong> Um de veículo relevante com audiência real vale
        mais que dezenas de sites sem público. Somar quantidade ignora a variável que mais importa.</p>

        <p><strong>O que conta é domínio distinto, não link.</strong> Cinquenta links vindos do mesmo site
        contam muito menos que cinquenta links de cinquenta sites diferentes. Propostas que falam em "número
        de backlinks" costumam estar inflando esse número com repetições.</p>

        <p><strong>O alvo é móvel.</strong> Mesmo que você calcule quantos precisa hoje, os concorrentes
        continuam adquirindo. O número não é uma linha de chegada.</p>

        <h2>A pergunta que substitui</h2>

        <p>Em vez de "quantos preciso?", pergunte: <strong>qual o perfil de autoridade de quem ocupa as
        posições que eu quero?</strong></p>

        <p>Isso se responde levantando, para os cinco ou dez primeiros resultados do termo-alvo:</p>

        <ul>
          <li>Quantos domínios distintos apontam para cada um.</li>
          <li>Que tipo de veículo são — imprensa, setoriais, blogs, institucionais.</li>
          <li>Em quanto tempo esse perfil foi construído.</li>
          <li>Quantos desses veículos seriam realisticamente acessíveis para você.</li>
        </ul>

        <p>O resultado não é um número a atingir. É um <strong>perfil a construir</strong> — o que muda
        completamente o plano. O método está em
        {link('/blog/como-analisar-backlinks-dos-concorrentes/', 'como analisar os backlinks dos concorrentes')}.</p>

        <h2>O que importa mais que a quantidade</h2>

        {tabela(
            ["Dimensão", "Por que importa"],
            [
                ["Diversidade de domínios", "muitos links de poucos sites somam pouco"],
                ["Relevância temática", "define quanto do sinal é aproveitado"],
                ["Ritmo de aquisição", "crescimento súbito cria padrão artificial"],
                ["Distribuição de âncoras", "concentração denuncia construção fabricada"],
                ["Presença de links de marca", "perfil natural inclui menções ao nome e ao endereço"],
                ["Qualidade da página que recebe", "link para página fraca rende menos"],
            ],
            nota="Um perfil pequeno e coerente supera um perfil grande e desorganizado."
        )}

        <h2>Uma referência prática por estágio</h2>

        <p>Sem números absolutos, dá para pensar em estágios relativos:</p>

        <p><strong>Site novo.</strong> O objetivo não é volume — é começar a existir. As primeiras menções
        legítimas, de fontes coerentes, valem mais pelo que estabelecem do que pelo peso que carregam.</p>

        <p><strong>Site com conteúdo consolidado.</strong> Aqui a construção acelera, porque existe material
        que justifica a referência. É a fase em que o ritmo pode subir sem parecer artificial.</p>

        <p><strong>Site disputando termos principais.</strong> A referência passa a ser explicitamente
        comparativa: chegar perto do perfil de quem já está nas posições-alvo, mantendo naturalidade.</p>

        <h2>O sinal de que você tem links suficientes</h2>

        <p>Existe um diagnóstico razoável: se as suas páginas aparecem consistentemente entre as posições
        10 e 30 com conteúdo tão bom quanto o de quem está acima, o gargalo é autoridade. Se elas nem
        aparecem, o gargalo provavelmente é
        {link('/blog/conteudo-ou-backlinks-onde-investir-primeiro/', 'conteúdo ou estrutura')} — e adquirir
        links não vai resolver.</p>
    """,
    "faq": [
        ("Meu concorrente tem muito mais backlinks. Já perdi?",
         "Não necessariamente. Perfis grandes e desorganizados perdem para perfis menores e coerentes com "
         "frequência. Vale olhar de onde vêm os links dele: se a maioria for de fontes fracas, a distância "
         "real é menor do que o número sugere."),
        ("Quantos links devo conquistar por mês?",
         "O ritmo deve ser compatível com o tamanho e a idade do site, não com uma meta fixa. Crescimento "
         "súbito em site novo cria padrão que trabalha contra você — por isso a construção acelera ao longo "
         "do projeto, em vez de começar no máximo."),
        ("Links internos contam?",
         "Contam para outra coisa: organizar a hierarquia do site e concentrar força nas páginas que "
         "importam. São importantes e não substituem links externos, que sinalizam reconhecimento de terceiros."),
    ],
    "cta": ("Quer saber qual perfil de autoridade o seu alvo exige? Na análise do projeto eu levanto o "
            "perfil de quem ocupa as posições que você quer, comparo com o seu e devolvo o plano.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 50
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-analisar-backlinks-dos-concorrentes",
    "h1": "Como analisar os backlinks dos concorrentes",
    "title": "Como analisar os backlinks dos concorrentes | RCB",
    "desc": ("O método para descobrir de onde vem a autoridade de quem está à frente e transformar "
             "isso em um plano de oportunidades acessíveis."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/consultoria-de-backlinks/", "Consultoria de backlinks"),
    "corpo": f"""
        <p>Analisar o perfil de links de quem está à frente é a forma mais direta de transformar
        "preciso de backlinks" em um plano com nomes, prioridades e custo estimado.</p>

        {caixa('<p><strong>Antes de começar:</strong> nenhuma ferramenta enxerga o perfil completo de um '
               'site. O que se obtém é uma amostra — suficiente para identificar padrões e oportunidades, '
               'insuficiente para conclusões precisas sobre volume. Use como mapa, não como censo.</p>')}

        <h2>Passo 1 — Escolher os concorrentes certos</h2>

        <p>Concorrente de SEO não é necessariamente concorrente de negócio. O que interessa é quem ocupa
        as posições que você quer, para os termos que você quer.</p>

        <p>Pesquise seus cinco termos principais e anote quem aparece consistentemente no topo. Se um
        portal grande ocupa metade das posições, separe-o: o perfil dele não é replicável e vai distorcer
        a análise. Foque nos concorrentes de porte comparável ao que você pretende alcançar.</p>

        <h2>Passo 2 — Levantar os domínios de referência</h2>

        <p>Para cada concorrente, extraia a lista de <strong>domínios distintos</strong> que apontam para
        ele — não a lista de links, que infla o número com repetições do mesmo site.</p>

        <p>Anote também o tipo de cada veículo, porque é isso que vai orientar a estratégia:</p>

        <ul>
          <li>imprensa e portais de notícia;</li>
          <li>veículos setoriais e especializados;</li>
          <li>blogs e sites de conteúdo;</li>
          <li>instituições, associações e entidades;</li>
          <li>diretórios e agregadores;</li>
          <li>fóruns e comunidades.</li>
        </ul>

        <h2>Passo 3 — Encontrar as fontes que se repetem</h2>

        <p>Este é o passo mais valioso da análise. Cruze as listas e identifique os veículos que apontam
        para <strong>vários concorrentes ao mesmo tempo</strong>.</p>

        <p>Esses sites são, quase por definição, receptivos ao seu tema — eles já demonstraram disposição
        de falar sobre aquilo mais de uma vez. E a ausência do seu site nessa lista é uma lacuna concreta,
        com nome e endereço.</p>

        <p>É daqui que sai a lista de prospecção mais eficiente que existe.</p>

        <h2>Passo 4 — Classificar por acessibilidade</h2>

        <p>Nem toda fonte é alcançável agora. Separe em três grupos:</p>

        {tabela(
            ["Grupo", "Características", "Prioridade"],
            [
                ["Acessível agora", "veículos setoriais, blogs, comunidades do nicho", "alta"],
                ["Acessível com esforço", "imprensa especializada, parcerias, entidades", "média"],
                ["Fora de alcance no momento", "grandes veículos, links históricos, institucionais antigos", "baixa"],
            ],
            nota="Concentrar esforço no primeiro grupo produz resultado antes de tentar o terceiro."
        )}

        <h2>Passo 5 — Entender como eles conseguiram</h2>

        <p>Não basta saber onde o link está — importa saber por quê. Abra a página que contém o link e
        observe:</p>

        <ul>
          <li>É um artigo editorial que cita o concorrente como referência?</li>
          <li>É conteúdo produzido pelo próprio concorrente?</li>
          <li>É uma lista, um comparativo, um diretório?</li>
          <li>É publicidade sinalizada?</li>
          <li>É menção espontânea a um material que ele publicou?</li>
        </ul>

        <p>Esse último caso é o mais interessante: se um veículo linkou espontaneamente para um conteúdo do
        concorrente, existe um tipo de material que atrai referência naquele nicho — e você pode produzir
        algo equivalente ou melhor.</p>

        <h2>Passo 6 — Comparar com o seu perfil</h2>

        <p>Feito o levantamento deles, faça o seu. A comparação responde três perguntas práticas:</p>

        <ol>
          <li><strong>Qual a distância real?</strong> Em domínios distintos e em qualidade, não em número
          bruto de links.</li>
          <li><strong>Onde estão as lacunas?</strong> Que tipos de veículo eles têm e você não.</li>
          <li><strong>O que você tem e eles não?</strong> Às vezes existe vantagem que não estava sendo
          aproveitada.</li>
        </ol>

        <h2>O que fazer com o resultado</h2>

        <p>A saída dessa análise é uma lista priorizada de alvos, com o motivo de cada um e o caminho
        provável de conquista. Isso é o insumo do trabalho de
        {link('/link-building-para-nichos-competitivos/', 'construção de autoridade')} — e o que separa
        prospecção dirigida de disparo aleatório de e-mails.</p>

        <h2>Erros comuns nessa análise</h2>

        <ul>
          <li>Comparar com portais gigantes cujo perfil não é replicável.</li>
          <li>Olhar número total de links em vez de domínios distintos.</li>
          <li>Tentar copiar o perfil inteiro em vez de priorizar o acessível.</li>
          <li>Ignorar o contexto em que cada link aparece.</li>
          <li>Tratar a amostra da ferramenta como se fosse o perfil completo.</li>
        </ul>
    """,
    "faq": [
        ("Preciso de ferramenta paga para isso?",
         "Para o levantamento de perfis de links, sim — as versões gratuitas costumam limitar demais a "
         "amostra. Já a análise de quem ocupa as posições e o exame do contexto de cada link se fazem "
         "manualmente, sem custo."),
        ("Devo tentar conseguir os mesmos links que o concorrente?",
         "Os acessíveis, sim, e essa costuma ser a via mais eficiente. Mas replicar o perfil inteiro não é "
         "objetivo realista nem necessário — parte dele é histórica e não se repete."),
        ("Com que frequência refazer essa análise?",
         "Uma vez a cada poucos meses costuma bastar para acompanhar movimentação relevante. Refazer com "
         "frequência alta consome tempo e mostra pouca mudança."),
    ],
    "cta": ("Quer essa análise feita e transformada em plano? Na análise do projeto eu levanto o perfil dos "
            "concorrentes que ocupam as suas posições-alvo, comparo com o seu e devolvo a lista priorizada "
            "de oportunidades.",
            ANALISE, "Solicitar análise do projeto"),
})
