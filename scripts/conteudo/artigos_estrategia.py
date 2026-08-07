# -*- coding: utf-8 -*-
"""
Artigos do cluster "mercados competitivos" — parte 2 (estratégia e decisão).

45 por-que-alguns-projetos-de-seo-precisam-de-mais-investimento
46 seo-local-ou-seo-nacional-diferenca      <- ponte entre as duas frentes do site
47 como-funciona-projeto-de-seo-para-nichos-competitivos
48 conteudo-ou-backlinks-onde-investir-primeiro
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-06"
CAT = "Mercados competitivos"
ANALISE = "/analise-de-projeto/"

ARTIGOS = []


# ------------------------------------------------------------------
# 46 — ponte entre SEO local e SEO nacional
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "seo-local-ou-seo-nacional-diferenca",
    "h1": "SEO local ou SEO nacional: qual é a diferença?",
    "title": "SEO local ou SEO nacional: qual é a diferença? | RCB",
    "desc": ("Os dois não são o mesmo serviço em tamanhos diferentes. Entenda o que muda na disputa, "
             "no prazo e no custo — e descubra qual é o seu caso."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-nacional/", "SEO nacional"),
    "corpo": f"""
        <p>Essa confusão custa caro nos dois sentidos: empresa local pagando por projeto nacional que não
        traz cliente, e operação nacional presa a uma estratégia de bairro.</p>

        {caixa('<p><strong>Resposta direta:</strong> a diferença não é de tamanho, é de natureza. No SEO '
               'local, o Google filtra os resultados pela localização de quem pesquisa — você compete com '
               'quem está por perto, e o perfil da empresa no mapa pesa muito. No SEO nacional não existe '
               'esse filtro: você compete com todos os sites do Brasil ao mesmo tempo, e o que decide é '
               'conteúdo, estrutura e autoridade.</p>')}

        <h2>O que muda na prática</h2>

        {tabela(
            ["", "SEO local", "SEO nacional"],
            [
                ["Quem é o concorrente", "quem atende a mesma região", "qualquer site do país"],
                ["Peso do perfil no Google Maps", "alto — decide boa parte", "baixo ou nulo"],
                ["O que mais pesa", "perfil, avaliações, sinais locais", "conteúdo, estrutura, autoridade"],
                ["Volume de conteúdo", "moderado", "alto e contínuo"],
                ["Papel dos backlinks", "secundário na maioria dos casos", "determinante"],
                ["Prazo até tração", "mais curto", "mais longo"],
                ["Custo típico", "menor", "maior"],
                ["Onde o resultado aparece", "mapa e busca com cidade", "busca sem recorte geográfico"],
            ],
            nota="Prazos e custos variam por nicho e não são garantidos em nenhum dos dois modelos."
        )}

        <h2>O teste que resolve em cinco minutos</h2>

        <p>Não é preciso ferramenta nenhuma. Pegue os cinco termos que você mais quer ranquear e pesquise
        cada um no Google, de preferência em uma janela anônima.</p>

        <p><strong>Se aparecer o bloco de mapa</strong> com perfis de empresa logo no topo, aquela busca
        tem intenção local. O Google entendeu que quem pesquisa isso quer resolver perto de onde está. Sua
        disputa passa pelo perfil da empresa, pelas avaliações e por sinais de proximidade.</p>

        <p><strong>Se aparecerem artigos, comparativos e páginas de serviço</strong> de sites de todo o
        país, sem mapa, a busca é nacional. Não há proximidade ajudando ninguém — quem tem o melhor
        conteúdo e a maior autoridade ocupa as posições.</p>

        <p>Muitos termos misturam os dois comportamentos, e alguns mudam conforme quem pesquisa. Ler isso
        corretamente é a primeira coisa que uma análise séria faz, porque define todo o resto do projeto.</p>

        <h2>Qual é o seu caso</h2>

        <p>A pergunta não é o tamanho da empresa. É <strong>onde está o cliente que pode comprar de
        você</strong>.</p>

        <h3>Seu caso é local se…</h3>
        <ul>
          <li>o cliente precisa ir até você fisicamente;</li>
          <li>você atende uma cidade ou uma região delimitada;</li>
          <li>seu faturamento depende de visita, agendamento presencial ou entrega local;</li>
          <li>as pessoas pesquisam seu serviço junto com o nome da cidade ou do bairro.</li>
        </ul>

        <p>Nesse cenário, investir em disputa nacional é gastar em visitante que não pode comprar. O
        caminho é a {link('/consultoria-seo-local/', 'consultoria de SEO local')} — mais rápida, mais
        barata e mais eficaz para esse objetivo.</p>

        <h3>Seu caso é nacional se…</h3>
        <ul>
          <li>você vende, entrega ou atende online, sem limite de distância;</li>
          <li>seu produto é digital: assinatura, plataforma, software, conteúdo;</li>
          <li>sua receita vem de tráfego, não de visita presencial;</li>
          <li>você é fornecedor com clientes espalhados pelo país;</li>
          <li>as pessoas pesquisam seu serviço sem nome de cidade nenhum.</li>
        </ul>

        <p>Aqui o caminho é o {link('/seo-nacional/', 'SEO nacional')} — outra disputa, outro prazo e
        outro nível de investimento.</p>

        <h2>E quando são os dois</h2>

        <p>Existe um terceiro caso, mais comum do que parece: a operação que atende presencialmente em uma
        cidade <em>e</em> vende online para o Brasil inteiro.</p>

        <p>Aqui as duas frentes fazem sentido, mas com uma condição: <strong>elas precisam usar páginas
        diferentes</strong>. Se a mesma página tentar ranquear para "serviço em Goiânia" e para o termo
        nacional genérico, ela não faz nem uma coisa nem outra — e as duas intenções se atrapalham.</p>

        <p>A separação correta costuma ser: páginas locais falando de cidade, atendimento e região; páginas
        nacionais falando do serviço em si, sem recorte geográfico; e links entre elas para o visitante
        encontrar rapidamente a versão que interessa a ele.</p>

        <h2>O erro mais caro dos dois lados</h2>

        <p><strong>Empresa local contratando projeto nacional.</strong> Recebe tráfego de todo o país,
        vê o número de visitas subir e não recebe cliente nenhum — porque quem visitou não pode ser
        atendido. Custa mais e entrega menos que um projeto local bem-feito.</p>

        <p><strong>Operação nacional presa ao local.</strong> Investe no perfil do Google Maps e em
        conteúdo com nome de cidade, quando o cliente pesquisa sem cidade nenhuma. Fica invisível
        exatamente onde a demanda está.</p>

        <p>Nos dois casos o problema não foi execução — foi diagnóstico. Por isso vale gastar cinco minutos
        fazendo o teste da SERP antes de gastar meses no projeto errado.</p>
    """,
    "faq": [
        ("Dá para fazer os dois ao mesmo tempo?",
         "Dá, e em alguns casos é o certo — operação com atendimento presencial em uma cidade e venda "
         "online para o país inteiro. A condição é usar páginas diferentes para cada intenção, senão elas "
         "competem entre si dentro do próprio site."),
        ("SEO nacional é sempre mais caro?",
         "Quase sempre, porque a concorrência é maior e a autoridade necessária é maior. Mas o fator "
         "decisivo é a dificuldade do termo, não o rótulo: um termo nacional pouco disputado pode custar "
         "menos que um termo local em cidade grande e mercado saturado."),
        ("Minha empresa é pequena. Posso disputar nacionalmente?",
         "O tamanho da empresa não decide — decide onde está o cliente e quanto o mercado exige de execução. "
         "Uma operação pequena com produto digital pode disputar nacionalmente; uma empresa grande com "
         "atendimento presencial em uma cidade, não deveria."),
        ("Páginas por cidade servem para SEO nacional?",
         "Só quando existe busca real com nome de cidade e cada página tem conteúdo próprio de verdade. Se "
         "as buscas do seu nicho não usam cidade, criar páginas regionais gera conteúdo repetido sem "
         "demanda para capturar."),
    ],
    "cta": ("Na dúvida sobre qual é o seu caso? Na análise do projeto eu leio a SERP dos seus termos e digo "
            "se a disputa é local, nacional ou mista — e o que isso muda no escopo e no investimento.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 47
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-funciona-projeto-de-seo-para-nichos-competitivos",
    "h1": "Como funciona um projeto de SEO para nichos competitivos?",
    "title": "Como funciona um projeto de SEO competitivo | RCB",
    "desc": ("As fases de um projeto em mercado disputado, o que é entregue em cada uma e por que a "
             "ordem das etapas muda o resultado final."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-nichos-competitivos/", "Nichos competitivos"),
    "corpo": f"""
        <p>Projeto em nicho disputado não é "SEO normal com mais horas". A diferença está na unidade de
        trabalho e na ordem das etapas.</p>

        {caixa('<p><strong>Resposta direta:</strong> em nicho competitivo, o projeto deixa de trabalhar '
               'página por página e passa a trabalhar tema por tema. E a ordem importa tanto quanto o '
               'volume: técnico primeiro, autoridade começando cedo, cobertura em seguida, termos '
               'principais por último.</p>')}

        <h2>Fase 0 — Análise: decidir se vale entrar</h2>

        <p>Antes de qualquer produção, a pergunta é se a disputa escolhida faz sentido. Isso significa
        olhar quem ocupa as dez primeiras posições, há quanto tempo esses domínios existem, quanto conteúdo
        têm sobre o tema e de onde vem a autoridade deles.</p>

        <p>O resultado dessa leitura não é uma nota de dificuldade. É uma decisão: <strong>entrar de
        frente, entrar pelas bordas ou não entrar</strong>. Recomendar não disputar um termo é uma
        resposta legítima — e sai muito mais barato que descobrir isso depois de seis meses de produção.</p>

        <h2>Fase 1 — Base técnica</h2>

        <p>Publicar conteúdo sobre uma estrutura quebrada desperdiça produção. Antes do volume, resolve-se:
        indexação, hierarquia de páginas, desempenho, conteúdo duplicado e canibalização interna já
        existente.</p>

        <p>Em nicho apertado, detalhe técnico decide posições que o conteúdo sozinho não move — justamente
        porque todos os concorrentes já têm conteúdo bom.</p>

        <h2>Fase 2 — Autoridade começa aqui, não no fim</h2>

        <p>Esse é o erro de sequenciamento mais comum. Como a construção de autoridade é a frente mais
        lenta, ela precisa do maior prazo — o que significa começar cedo, e não depois que o conteúdo
        estiver pronto.</p>

        <p>Começar cedo não significa adquirir volume no primeiro mês. Significa iniciar a prospecção,
        mapear veículos relevantes e conquistar as primeiras menções em ritmo compatível com o tamanho do
        site. O ritmo acelera conforme o conteúdo se acumula e passa a justificar mais referências. Mais
        detalhes em {link('/link-building-para-nichos-competitivos/', 'link building para nichos competitivos')}.</p>

        <h2>Fase 3 — Cobertura, não páginas avulsas</h2>

        <p>Aqui está a mudança conceitual central do projeto. Em mercado fácil, uma página bem otimizada
        ranqueia. Em mercado difícil, o que ranqueia é o site que <strong>cobre o tema inteiro</strong>:</p>

        <ul>
          <li>a página principal sobre o assunto;</li>
          <li>os subtemas que se desdobram dele;</li>
          <li>as comparações que o usuário faz antes de decidir;</li>
          <li>as dúvidas periféricas que ninguém respondeu direito;</li>
          <li>os links internos organizando tudo isso em uma hierarquia clara.</li>
        </ul>

        <p>Vinte conteúdos organizados sobre um tema rendem mais que cem textos soltos sobre assuntos
        variados — e muito mais que cinco textos sobre variações do mesmo termo, que só competem entre si.</p>

        <h2>Fase 4 — Termos médios antes dos principais</h2>

        <p>A tentação é atacar o termo mais valioso primeiro. Costuma ser mais rápido fazer o contrário:
        conquistar posição em termos de disputa média, acumular sinais de relevância temática e chegar ao
        termo principal já com força construída.</p>

        <p>Além de ser mais rápido, esse caminho traz resultado intermediário — o que sustenta a decisão
        de continuar investindo enquanto o alvo maior amadurece.</p>

        <h2>Fase 5 — Medição que enxerga antes do ranking</h2>

        <p>Acompanhar só a posição dos termos principais faz o projeto parecer parado durante meses em que
        ele está avançando. Os indicadores que se movem primeiro:</p>

        {tabela(
            ["Indicador", "O que mostra", "Quando começa a se mover"],
            [
                ["Páginas indexadas", "se o conteúdo está sendo aceito", "primeiras semanas"],
                ["Termos únicos com impressão", "se o site está sendo considerado", "primeiras semanas"],
                ["Posição média do grupo", "se há avanço agregado", "alguns meses"],
                ["Domínios de referência", "se a autoridade cresce", "contínuo"],
                ["Posição dos termos principais", "o objetivo final", "por último"],
            ],
            nota="Ler só a última linha é o que faz projetos bons serem cancelados no meio do caminho."
        )}

        <h2>Fase 6 — Manutenção</h2>

        <p>Posição conquistada não é permanente. Concorrente que continua publicando recupera terreno, e
        conteúdo envelhece. A intensidade cai depois da fase de construção, mas parar por completo costuma
        significar perder gradualmente o que foi conquistado.</p>

        <h2>O que faz projetos assim fracassarem</h2>

        <ol>
          <li><strong>Investimento abaixo do patamar.</strong> Em disputa dura, meio projeto não entrega
          meio resultado.</li>
          <li><strong>Ordem trocada.</strong> Autoridade deixada para o fim, técnico deixado para depois.</li>
          <li><strong>Alvo mal escolhido.</strong> Termo dominado por portais gigantes ou com intenção
          incompatível com o negócio.</li>
          <li><strong>Avaliação prematura.</strong> Cancelar no quarto mês olhando só o termo principal.</li>
          <li><strong>Execução intermitente.</strong> Publicar em rajadas e parar.</li>
        </ol>
    """,
    "faq": [
        ("Quanto tempo dura um projeto desses?",
         "A fase de construção costuma ocupar vários trimestres, seguida de manutenção contínua. O prazo de "
         "cada meta é estimado na análise, com as premissas explícitas, e revisado no acompanhamento — não "
         "é garantido."),
        ("Dá para começar só pelo conteúdo e deixar autoridade para depois?",
         "Dá, mas costuma alongar o prazo total. Como a autoridade é a frente mais lenta, adiá-la empurra "
         "o resultado final para muito mais tarde. O desenho usual é começar as duas, com pesos diferentes."),
        ("Como saber se o projeto está no caminho antes de ranquear?",
         "Acompanhando indexação, número de termos únicos gerando impressão e posição média por grupo de "
         "termos. Esses indicadores se movem semanas ou meses antes das posições principais."),
    ],
    "cta": ("Quer saber quantas fases o seu caso exige e em que ordem? Na análise do projeto eu leio a "
            "concorrência, aponto o gargalo atual e devolvo a sequência recomendada com escopo e prazo estimado.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 48
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "conteudo-ou-backlinks-onde-investir-primeiro",
    "h1": "Conteúdo ou backlinks: onde investir primeiro?",
    "title": "Conteúdo ou backlinks: onde investir primeiro? | RCB",
    "desc": ("A ordem de investimento que evita desperdício nos primeiros meses de um projeto — e "
             "como identificar qual dos dois é o seu gargalo real."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-nichos-competitivos/", "Link building"),
    "corpo": f"""
        <p>A resposta curta é conteúdo — mas com uma ressalva que muda a execução: <em>começar</em> pelo
        conteúdo não significa <em>esperar</em> o conteúdo acabar para pensar em autoridade.</p>

        {caixa('<p><strong>Resposta direta:</strong> comece pelo conteúdo, porque links apontando para um '
               'site que não tem o que oferecer são desperdício. Mas inicie a construção de autoridade '
               'cedo, em paralelo, porque ela é a frente mais lenta e precisa do maior prazo. A ordem é '
               'de peso, não de exclusão.</p>')}

        <h2>Por que conteúdo vem primeiro</h2>

        <p>Três razões práticas:</p>

        <p><strong>Link precisa de destino.</strong> Conquistar uma menção relevante custa tempo e dinheiro.
        Gastar isso apontando para uma página fraca desperdiça a oportunidade — e você não consegue a mesma
        menção duas vezes.</p>

        <p><strong>Conteúdo bom reduz o custo do link.</strong> É muito mais fácil conseguir referência
        quando existe algo que valha a pena referenciar. Sem isso, cada link vira negociação pura.</p>

        <p><strong>Conteúdo rende sozinho em termos menos disputados.</strong> Buscas específicas e de cauda
        longa costumam responder a conteúdo bom mesmo com pouca autoridade. É o resultado inicial que
        sustenta a continuidade do projeto.</p>

        <h2>Por que autoridade não pode esperar o fim</h2>

        <p>A construção de autoridade tem um componente temporal que não é comprimível. Adquirir muitos
        links em pouco tempo cria um padrão que trabalha contra o site, então existe um teto de velocidade
        dado pelo que parece natural para um site daquele tamanho e idade.</p>

        <p>Consequência: se a autoridade só começar quando o conteúdo estiver pronto, o prazo total do
        projeto se estende bastante — e em nicho competitivo isso pode significar meses a mais.</p>

        <h2>A divisão que costuma funcionar</h2>

        {tabela(
            ["Fase", "Conteúdo", "Autoridade", "Foco"],
            [
                ["Início", "peso maior", "início da prospecção", "criar o que merece ser referenciado"],
                ["Meio", "ritmo constante", "peso crescente", "cobertura + primeiras conquistas"],
                ["Maturidade", "manutenção e atualização", "peso maior", "disputar termos principais"],
            ],
            nota="Proporções variam por nicho: onde o gargalo é claramente autoridade, o peso migra mais cedo."
        )}

        <h2>Como saber qual é o seu gargalo</h2>

        <p>Existe um diagnóstico razoavelmente confiável, baseado em onde suas páginas estão hoje:</p>

        <h3>Sinal de que falta conteúdo</h3>
        <ul>
          <li>Poucas páginas indexadas sobre o tema que você quer disputar.</li>
          <li>Termos relevantes para os quais você não tem nenhuma página.</li>
          <li>Concorrentes com dezenas de conteúdos sobre o assunto e você com poucos.</li>
          <li>Páginas que aparecem em buscas erradas, porque nenhuma responde à busca certa.</li>
        </ul>

        <h3>Sinal de que falta autoridade</h3>
        <ul>
          <li>Suas páginas aparecem entre as posições 10 e 30 e não passam disso.</li>
          <li>Você tem conteúdo tão bom ou melhor que o de quem está à frente.</li>
          <li>Você ranqueia bem em termos de cauda longa e mal nos principais.</li>
          <li>Os concorrentes que estão acima têm muito mais domínios de referência.</li>
        </ul>

        <p>Esse último cenário é o mais frequente em projetos que "travaram": o conteúdo já está bom, e o
        que falta é o site ser reconhecido como referência comparável. Aumentar o volume de texto aí não
        resolve — e é exatamente o que muita gente faz.</p>

        <h2>O erro dos dois extremos</h2>

        <p><strong>Só conteúdo.</strong> O projeto publica sem parar, ranqueia em cauda longa e nunca chega
        aos termos que motivaram o investimento. É comum durar dois anos assim.</p>

        <p><strong>Só backlinks.</strong> Verba concentrada em aquisição de links para um site com poucas
        páginas e conteúdo raso. Os links não sustentam o que não existe, e o dinheiro se perde. Costuma
        acontecer quando o fornecedor vende pacote de links sem olhar o site.</p>

        <h2>Uma regra prática</h2>

        <p>Se você tem menos conteúdo que os concorrentes da primeira página, o gargalo é conteúdo. Se você
        tem conteúdo equivalente e não passa da segunda página, o gargalo é autoridade. Se não tem nem um
        nem outro, comece pelo conteúdo — e inicie a prospecção de autoridade no mesmo mês.</p>

        <p>Em qualquer cenário, vale medir antes: uma
        {link('/consultoria-de-backlinks/', 'auditoria do perfil de links')} mostra onde você está em
        relação a quem ocupa as posições que você quer.</p>
    """,
    "faq": [
        ("Quanto da verba deve ir para cada frente?",
         "Varia por nicho e por fase. Em projeto novo, o peso costuma começar maior em conteúdo e migrar "
         "para autoridade conforme a cobertura se completa. Em nicho onde a autoridade é claramente o "
         "gargalo, essa migração acontece mais cedo."),
        ("Posso conquistar links sem produzir conteúdo?",
         "Pode, mas o rendimento é menor e o custo por link é maior — sem conteúdo que justifique a "
         "referência, cada menção vira negociação pura. E links apontando para páginas fracas não "
         "sustentam posição."),
        ("Conteúdo bom atrai links sozinho?",
         "Em alguns temas sim, em muitos não. Assuntos com apelo editorial atraem referência espontânea; "
         "temas comerciais e de nicho raramente atraem. Nesses casos, a construção precisa ser deliberada."),
    ],
    "cta": ("Quer saber se o seu gargalo é conteúdo ou autoridade? Na análise do projeto eu comparo a sua "
            "cobertura e o seu perfil de links com os de quem ocupa as posições que você quer disputar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 45
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "por-que-alguns-projetos-de-seo-precisam-de-mais-investimento",
    "h1": "Por que alguns projetos de SEO precisam de mais investimento?",
    "title": "Por que alguns projetos de SEO custam muito mais | RCB",
    "desc": ("O que faz o mesmo serviço custar valores tão diferentes entre nichos — e por que "
             "investir abaixo do patamar do mercado costuma não entregar resultado nenhum."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-mercados-competitivos/", "Mercados competitivos"),
    "corpo": f"""
        <p>Dois projetos de SEO podem ter escopos com nomes idênticos e custos que diferem em uma ordem de
        grandeza. Não é margem — é volume de execução.</p>

        {caixa('<p><strong>Resposta direta:</strong> o custo de um projeto de SEO não é definido pelo '
               'tamanho da sua empresa nem pelo que você espera faturar. É definido pela distância entre o '
               'seu site e os que já ocupam as posições que você quer — e por quanto trabalho é preciso '
               'para percorrer essa distância.</p>')}

        <h2>O que NÃO define o preço</h2>

        <ul>
          <li>O tamanho da sua empresa.</li>
          <li>Quantos funcionários você tem.</li>
          <li>O quanto você espera faturar com o projeto.</li>
          <li>Há quanto tempo o negócio existe.</li>
        </ul>

        <p>Esses fatores aparecem em proposta comercial, mas não têm relação com o trabalho necessário.
        Uma empresa pequena disputando um termo caro precisa da mesma execução que uma empresa grande
        disputando o mesmo termo.</p>

        <h2>O que define</h2>

        <h3>1. A força de quem já está lá</h3>
        <p>É o fator dominante. Disputar contra sites com anos de acúmulo, centenas de conteúdos e perfil
        de links robusto exige construir algo comparável. Disputar contra páginas desatualizadas e fóruns
        exige muito menos.</p>

        <h3>2. Quanto conteúdo precisa existir</h3>
        <p>Em nicho fácil, poucas páginas resolvem. Em nicho duro, o que ranqueia é
        {link('/blog/como-funciona-projeto-de-seo-para-nichos-competitivos/', 'cobertura de tema inteiro')} —
        e cobertura custa proporcionalmente ao tamanho do tema.</p>

        <h3>3. Quanta autoridade precisa ser construída</h3>
        <p>A frente mais cara e mais lenta. Em mercados onde poucos veículos aceitam o tema, cada conquista
        custa mais — o que explica boa parte da diferença de preço entre nichos aparentemente parecidos.</p>

        <h3>4. O ponto de partida</h3>
        <p>Site existente com conteúdo aproveitável parte de um lugar. Projeto sem marca, sem domínio e
        sem site parte de outro — e a construção da base é parte do custo.</p>

        <h3>5. O prazo desejado</h3>
        <p>Apertar prazo aumenta custo, porque exige mais execução simultânea. E há um teto: acima de certo
        ponto, mais dinheiro não compra mais velocidade.</p>

        <h2>Por que investir abaixo do patamar não entrega resultado proporcional</h2>

        <p>Essa é a parte contraintuitiva, e a que mais gera frustração.</p>

        <p>Em muitos serviços, metade do investimento entrega aproximadamente metade do resultado. Em SEO
        competitivo, não. Existe um <strong>patamar mínimo de execução</strong> abaixo do qual o projeto
        não alcança o nível de cobertura e autoridade que aquela primeira página exige — e fica fora dela.</p>

        <p>Na prática: o dinheiro é gasto, o conteúdo é publicado, o site melhora um pouco e continua na
        terceira página, onde praticamente ninguém clica. O retorno não é menor; é próximo de zero.</p>

        <p>Por isso uma análise honesta pode concluir que o melhor uso de um orçamento limitado é
        {link('/seo-para-nichos-competitivos/', 'mirar termos menos disputados')}, onde aquele investimento
        é suficiente para chegar ao topo — em vez de ser insuficiente para um alvo maior.</p>

        <h2>Como saber qual é o patamar do seu nicho</h2>

        <ol>
          <li>Liste os dez resultados da busca que você quer disputar.</li>
          <li>Veja quantas páginas cada um tem sobre o tema.</li>
          <li>Verifique com que frequência publicam.</li>
          <li>Estime quanto conteúdo você precisaria para ter cobertura equivalente.</li>
          <li>Some a construção de autoridade e o período de manutenção.</li>
        </ol>

        <p>O número aproximado que sai daí já responde a pergunta mais importante: esse alvo cabe no seu
        orçamento? Se não couber, mudar de alvo é decisão melhor que reduzir o investimento no mesmo alvo.</p>
    """,
    "faq": [
        ("Se eu não tenho o orçamento do patamar, não devo fazer SEO?",
         "Deve — em outro alvo. Praticamente todo nicho tem recortes menos disputados com demanda real. "
         "Conquistar o topo em termos médios costuma render mais que ficar na terceira página do termo "
         "principal."),
        ("Posso começar pequeno e aumentar depois?",
         "Pode, e costuma ser o desenho mais sensato: começar por recortes viáveis, gerar resultado e "
         "reinvestir. O que não funciona é começar pequeno mirando o termo mais difícil desde o primeiro mês."),
        ("Por que dois orçamentos para o mesmo objetivo variam tanto?",
         "Quase sempre porque propõem escopos diferentes. Compare volume de conteúdo, trabalho de "
         "autoridade, execução técnica e prazo — não só o valor final. Orçamento muito abaixo dos demais "
         "normalmente significa escopo muito menor."),
    ],
    "cta": ("Quer saber qual é o patamar do seu nicho antes de decidir? Na análise do projeto eu leio a "
            "concorrência real e devolvo o escopo necessário com faixa de investimento — inclusive quando "
            "a recomendação é mudar de alvo.",
            ANALISE, "Solicitar análise do projeto"),
})
