# -*- coding: utf-8 -*-
"""
Cluster IPTV e streaming — lote 2 (backlog do plano §5.1, produzido em 07/08/2026).

 3 iptv-primeira-pagina-3-4-meses
 7 backlinks-para-iptv-funcionam
 9 seo-nacional-para-iptv-o-que-muda

Diferenciação em relação ao lote 1 e às páginas comerciais (o backlog só foi
produzido depois de definir um ângulo que não repetisse o que já existe):

  3 × artigo 2 (prazo)      — o 2 explica os fatores de prazo; o 3 responde a
                              pergunta fechada com um modelo de faixas de termo.
  7 × artigo 8 (investir)   — o 8 dimensiona verba; o 7 avalia eficácia por tipo
                              de veículo, que é outra pergunta.
  9 × página B1 (pilar)     — o pilar VENDE o projeto; o 9 EXPLICA a mecânica da
                              disputa nacional. O artigo aponta para o pilar como
                              destino comercial, nunca disputa o mesmo termo.
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-07"
CAT = "IPTV e streaming"
ANALISE = "/analise-de-projeto/"

NOTA_LICENCA = ('<p><strong>Nota sobre este cluster:</strong> os conteúdos de IPTV e streaming deste site '
                'se dirigem a operadores, plataformas e distribuidores que possuem direito ou autorização '
                'sobre o conteúdo que distribuem. Essa condição é verificada na análise do projeto, antes '
                'de qualquer proposta.</p>')

ARTIGOS = []


# ------------------------------------------------------------------
# 3
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "iptv-primeira-pagina-3-4-meses",
    "h1": "É possível colocar IPTV na primeira página em três ou quatro meses?",
    "title": "IPTV na primeira página em 3 ou 4 meses? | RCB",
    "desc": ("Depende inteiramente de qual termo. Um modelo de faixas para saber quais buscas são "
             "viáveis nesse prazo e quais não são, sem promessa de calendário."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-iptv/", "SEO para IPTV"),
    "corpo": f"""
        <p>Essa é a pergunta que mais aparece em conversa inicial, e ela costuma ser respondida com um
        "sim" de vendedor ou um "não" de quem não quer se comprometer. As duas respostas são inúteis,
        porque a pergunta está incompleta: <strong>primeira página de qual termo?</strong></p>

        {caixa('<p><strong>Resposta direta:</strong> para buscas específicas e de baixa disputa, três a '
               'quatro meses é um prazo plausível. Para os termos principais do nicho, não é — eles '
               'dependem de conteúdo acumulado e de autoridade construída, e autoridade tem um ritmo que '
               'não se compra. A diferença entre os dois cenários é de uma ordem de grandeza, e é por isso '
               'que a pergunta só faz sentido com o termo junto.</p>')}

        {caixa(NOTA_LICENCA)}

        <h2>Um modelo de faixas para responder por conta própria</h2>

        <p>Antes de falar com qualquer fornecedor, dá para classificar os seus termos-alvo em quatro
        faixas. O critério é o que aparece na página de resultados, não o volume de busca:</p>

        {tabela(
            ["Faixa", "Como identificar", "Viável em 3–4 meses?"],
            [
                ["1 — Cauda muito longa",
                 "pergunta específica; resultados são fóruns, redes sociais e páginas desatualizadas",
                 "sim, com frequência"],
                ["2 — Cauda longa comercial",
                 "termo com intenção clara; resultados são sites pequenos e páginas de serviço simples",
                 "muitas vezes sim"],
                ["3 — Disputa média",
                 "resultados são sites estruturados, com blog ativo e alguns anos de domínio",
                 "raramente; costuma passar disso"],
                ["4 — Termos principais",
                 "resultados são domínios maduros, com muito conteúdo e perfil de links robusto",
                 "não"],
            ],
            nota="Classificação por dificuldade observada na página de resultados. Não é garantia — é leitura de cenário."
        )}

        <p>A conta prática: um projeto novo bem executado costuma conquistar posições nas faixas 1 e 2
        dentro dos primeiros meses, porque essas buscas dependem mais de responder bem a pergunta do que
        de autoridade acumulada. As faixas 3 e 4 dependem de algo que o tempo constrói.</p>

        <h2>Por que os termos principais não cabem nesse prazo</h2>

        <p>Não é falta de esforço nem de orçamento. São três limites que se somam:</p>

        <p><strong>O site precisa ser rastreado e avaliado.</strong> Conteúdo novo não entra no índice e
        assume posição no mesmo dia. Só essa etapa já consome parte do prazo.</p>

        <p><strong>A cobertura precisa existir.</strong> Nos termos principais, raramente uma página
        isolada ranqueia. O que ranqueia é o site que cobre o tema — e produzir essa cobertura leva meses,
        mesmo com equipe dedicada.</p>

        <p><strong>A autoridade tem teto de velocidade.</strong> Este é o limite mais rígido. Adquirir
        muitos links em pouco tempo cria um padrão artificial que trabalha contra o site. Existe um ritmo
        máximo compatível com a idade e o tamanho do projeto, e ele não é acelerável por dinheiro. É por
        isso que {link('/link-building-para-iptv/', 'a construção de autoridade')} precisa começar cedo em
        vez de ser concentrada no fim.</p>

        <h2>O que dá para ter em três ou quatro meses</h2>

        <p>Reduzir a pergunta a "primeira página, sim ou não" esconde o que realmente acontece nesse
        período em um projeto que está indo bem:</p>

        <ul>
          <li><strong>Site no ar</strong>, com estrutura de conversão funcionando e contatos sendo medidos.</li>
          <li><strong>Dezenas de páginas indexadas</strong> e sendo rastreadas com regularidade.</li>
          <li><strong>Posições conquistadas</strong> nas faixas 1 e 2 — que já trazem visitante com
          intenção real.</li>
          <li><strong>Primeiros contatos</strong> vindos do orgânico, normalmente de buscas específicas.</li>
          <li><strong>Impressões crescendo</strong> em dezenas ou centenas de termos diferentes, incluindo
          os principais em posições ainda baixas.</li>
          <li><strong>Base de autoridade iniciada</strong>, com as primeiras menções conquistadas.</li>
        </ul>

        <p>Esse conjunto é o que indica que o projeto está no caminho. Avaliar o trabalho só pela posição
        do termo principal no quarto mês é o erro que mais faz projeto bom ser cancelado antes da hora —
        e o assunto é tratado a fundo em
        {link('/blog/quanto-tempo-posicionar-site-iptv/', 'quanto tempo demora para posicionar um site de IPTV')}.</p>

        <h2>Quando alguém promete o prazo curto no termo principal</h2>

        <p>Se um fornecedor garante primeira página em três ou quatro meses no termo principal do nicho,
        faça duas perguntas antes de qualquer coisa:</p>

        <ol>
          <li><strong>Qual termo exatamente?</strong> Costuma aparecer uma variação longa que ninguém
          pesquisa, ou o próprio nome da sua marca — posições que você conquistaria de qualquer forma.</li>
          <li><strong>Como será medido?</strong> Busca feita no computador de quem já visitou o site
          várias vezes mostra um resultado que não é o que o público vê.</li>
        </ol>

        <p>Se as respostas forem vagas, a promessa é de expectativa, não de trabalho. O mesmo mecanismo
        está detalhado em
        {link('/blog/e-possivel-garantir-primeira-pagina/', 'é possível garantir primeira página no Google')}.</p>

        <h2>O caminho que costuma ser mais rápido</h2>

        <p>Contraintuitivamente, mirar o termo mais valioso primeiro costuma ser o caminho mais lento.
        A sequência que tende a render antes:</p>

        <ol>
          <li>Conquistar as faixas 1 e 2, que trazem resultado no curto prazo.</li>
          <li>Usar esse resultado para sustentar a continuidade do investimento.</li>
          <li>Acumular cobertura e autoridade durante todo esse período.</li>
          <li>Avançar para a faixa 3 com força já construída.</li>
          <li>Chegar aos termos principais por último.</li>
        </ol>

        <p>Além de mais rápido, esse caminho gera receita durante a construção — em vez de exigir meses de
        investimento sem nenhum retorno visível.</p>
    """,
    "faq": [
        ("Então nenhum projeto chega à primeira página em 4 meses?",
         "Chega, e com frequência — em buscas de cauda longa e de disputa baixa, que são a maior parte das "
         "buscas de qualquer nicho. O que não acontece nesse prazo é chegar ao topo dos termos principais, "
         "que são poucos e disputados por quem já está lá há anos."),
        ("Um domínio com histórico encurta esse prazo?",
         "Pode encurtar parte do caminho, se a análise confirmar histórico limpo e relevância temática. Mas "
         "não transforma um termo da faixa 4 em faixa 1 — e domínio nenhum garante autoridade herdada."),
        ("Investir mais dinheiro acelera?",
         "Acelera conteúdo e execução técnica, que são limitados por capacidade de produção. Não acelera a "
         "construção de autoridade além do ritmo que parece natural para o site — e é justamente ela que "
         "decide os termos principais."),
        ("Como sei em qual faixa está o meu termo?",
         "Pesquise o termo em uma janela anônima e olhe os dez primeiros resultados: há quanto tempo esses "
         "sites existem, quanto conteúdo têm sobre o assunto e se publicam com regularidade. Isso classifica "
         "o termo com boa precisão, sem precisar de ferramenta."),
    ],
    "cta": ("Quer saber em qual faixa estão os seus termos — e o que é realista em três, seis ou doze meses? "
            "Na análise do projeto eu classifico cada termo pela dificuldade observada e devolvo o cenário "
            "com as premissas escritas.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 7
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "backlinks-para-iptv-funcionam",
    "h1": "Backlinks para IPTV funcionam?",
    "title": "Backlinks para IPTV funcionam? O que rende e o que não | RCB",
    "desc": ("Funcionam, mas nem todo tipo de veículo rende igual neste nicho. A leitura de "
             "eficácia por tipo de fonte, e onde a verba costuma ser desperdiçada."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-iptv/", "Link building para IPTV"),
    "corpo": f"""
        <p>Funcionam — links continuam sendo um dos sinais que mais pesam em disputa nacional. A pergunta
        útil não é se funcionam, e sim <strong>quais funcionam neste nicho</strong>, porque a resposta é
        bem diferente da média do mercado.</p>

        {caixa('<p><strong>Resposta direta:</strong> o que decide a eficácia de um link aqui é a '
               'relevância temática e a audiência real do veículo — não a métrica de autoridade que aparece '
               'na proposta. E como poucos veículos aceitam o tema, este é um dos nichos em que mais se '
               'paga caro por fonte que entrega pouco.</p>')}

        {caixa(NOTA_LICENCA)}

        <h2>A dificuldade específica do nicho</h2>

        <p>Em mercados neutros, o conjunto de veículos dispostos a publicar sobre o tema é grande. Aqui
        ele é pequeno — muitos sites evitam o assunto, o que produz três consequências práticas:</p>

        <p><strong>Cada conquista custa mais.</strong> Menos oferta com a mesma demanda eleva o preço e o
        tempo de prospecção.</p>

        <p><strong>A tentação de baixar o critério aumenta.</strong> Quando as fontes boas são escassas,
        fica fácil aceitar qualquer site que diga sim. É exatamente aí que projetos se enterram.</p>

        <p><strong>O prazo do projeto se estende.</strong> Por isso a autoridade precisa começar cedo, e não
        depois que o conteúdo estiver pronto.</p>

        <h2>Eficácia por tipo de veículo</h2>

        <p>Nem todo link rende igual. A leitura aproximada, do que mais rende para o que menos rende neste
        nicho específico:</p>

        {tabela(
            ["Tipo de veículo", "Por que rende (ou não)", "Eficácia"],
            [
                ["Site técnico ou de tecnologia",
                 "tema adjacente legítimo, audiência real, contexto natural", "alta"],
                ["Veículo de entretenimento e mídia",
                 "proximidade temática e público sobreposto", "alta"],
                ["Comunidade ou fórum ativo do assunto",
                 "audiência genuína e contexto de discussão real", "média a alta"],
                ["Blog de nicho com leitores",
                 "relevância boa, desde que o site tenha tráfego próprio", "média"],
                ["Diretório ou agregador genérico",
                 "sem relevância temática e sem audiência", "baixa"],
                ["Site que publica sobre todos os nichos",
                 "modelo é vender link; contexto artificial", "muito baixa"],
                ["Rede de sites controlada pelo fornecedor",
                 "padrão detectável; risco recai sobre o seu domínio", "negativa"],
            ],
            nota="Leitura qualitativa de contexto e audiência, não medição. A última linha é passivo, não ganho."
        )}

        <p>O padrão que aparece na tabela é consistente: <strong>o que decide não é a métrica, é se existe
        gente real do outro lado e se o assunto tem relação com o seu</strong>.</p>

        <h2>Onde a verba costuma ser desperdiçada</h2>

        <ul>
          <li><strong>Pacotes por quantidade.</strong> Vinte links de sites sem audiência somam menos que
          dois de veículos relevantes — e ainda criam um padrão que precisa ser gerenciado depois.</li>
          <li><strong>Pagar por métrica alta com tráfego nulo.</strong> Site que ninguém visita entrega
          pouco, por melhor que pareça na ferramenta.</li>
          <li><strong>Adquirir tudo em poucas semanas.</strong> Ritmo destoante é um dos sinais mais fáceis
          de identificar.</li>
          <li><strong>Concentrar a âncora no termo comercial.</strong> Perfil natural mistura marca,
          endereço e variações.</li>
          <li><strong>Começar antes de ter conteúdo.</strong> Link apontando para site sem substância
          desperdiça a fonte — e a mesma menção não se consegue duas vezes.</li>
        </ul>

        <p>Os critérios de avaliação estão detalhados em
        {link('/blog/como-avaliar-qualidade-de-um-backlink/', 'como avaliar a qualidade de um backlink')},
        e o dimensionamento de verba em
        {link('/blog/quanto-investir-backlinks-iptv/', 'quanto investir em backlinks para um projeto de IPTV')}.</p>

        <h2>O que fazer quando as fontes são escassas</h2>

        <p>A resposta não é forçar volume. É <strong>ampliar o que conta como relevante</strong>, sem
        abrir mão do critério:</p>

        <ol>
          <li><strong>Trabalhar temas adjacentes.</strong> Tecnologia, dispositivos, conectividade,
          entretenimento — assuntos legitimamente próximos, com veículos que aceitam o tema.</li>
          <li><strong>Produzir material que mereça referência.</strong> Comparativos técnicos, guias de
          compatibilidade e dados organizados atraem menção com mais facilidade que página comercial.</li>
          <li><strong>Aceitar ritmo menor e constante.</strong> Poucas conquistas boas por mês, sustentadas
          por muitos meses, rendem mais que um lote grande de uma vez.</li>
          <li><strong>Compensar com cobertura.</strong> Onde a autoridade é escassa, cobertura profunda de
          tema ajuda a sustentar posições em buscas de menor disputa.</li>
        </ol>

        <h2>Como saber se está funcionando</h2>

        <p>Autoridade age de forma acumulada e defasada — raramente dá para atribuir um movimento de
        posição a um link específico. O que se observa é o conjunto:</p>

        <ul>
          <li>Evolução do número de domínios de referência ao longo dos meses.</li>
          <li>Distribuição de âncoras se mantendo variada.</li>
          <li>Posição média subindo por grupo de termos, não em um termo isolado.</li>
          <li>Comparação com o perfil de quem ocupa as posições que você quer.</li>
        </ul>

        <p>Se o relatório do seu fornecedor não mostra os endereços conquistados e o contexto de cada
        menção, não há como avaliar nada disso — e essa recusa costuma ser a resposta que você procurava.</p>
    """,
    "faq": [
        ("Quantos backlinks preciso para este nicho?",
         "Não existe número. A referência é comparativa: quantos domínios distintos apontam para quem "
         "ocupa as posições que você quer, e de que tipo são. Esse levantamento é específico por termo."),
        ("Link de site estrangeiro serve?",
         "Serve quando há relevância temática real e audiência, mas rende menos para posicionamento em "
         "português. Um perfil formado majoritariamente por fontes de outro idioma e sem relação com o "
         "público brasileiro é um sinal de construção artificial."),
        ("Vale a pena comprar links já que as fontes são escassas?",
         "A escassez é justamente o que torna a compra mais arriscada aqui: o que está à venda em volume "
         "costuma vir de sites sem audiência, criados para vender link. Paga-se caro por algo que entrega "
         "pouco e deixa passivo."),
        ("Quanto tempo até os links renderem?",
         "Não há prazo definido. O efeito é acumulado e aparece na evolução do conjunto ao longo de meses, "
         "não logo após cada conquista."),
    ],
    "cta": ("Recebeu uma proposta de link building e quer uma segunda opinião? Na análise do projeto eu "
            "avalio as fontes oferecidas por relevância, audiência e contexto — e comparo com o perfil de "
            "quem ocupa as posições que você quer.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 9
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "seo-nacional-para-iptv-o-que-muda",
    "h1": "SEO nacional para IPTV: o que muda?",
    "title": "SEO nacional para IPTV: o que muda na disputa | RCB",
    "desc": ("Sem mapa e sem proximidade, a disputa por IPTV é nacional desde o primeiro dia. O que "
             "isso muda na estratégia, no prazo e na forma de medir o progresso."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-iptv/", "SEO para IPTV"),
    "corpo": f"""
        <p>Quase todo projeto deste nicho é nacional por natureza, e muita gente descobre isso só depois de
        aplicar uma estratégia local que não tinha como funcionar.</p>

        {caixa('<p><strong>Resposta direta:</strong> em IPTV não existe filtro geográfico ajudando você. '
               'O serviço é entregue pela internet, o cliente pode estar em qualquer lugar, e o Google não '
               'mostra mapa nem favorece quem está perto. Todo o peso recai sobre conteúdo, estrutura e '
               'autoridade — que são exatamente as três frentes mais lentas.</p>')}

        {caixa(NOTA_LICENCA)}

        <h2>As três coisas que somem</h2>

        <p>Quem vem do SEO local perde três alavancas de uma vez, e vale entender o tamanho da perda:</p>

        <p><strong>O perfil no Google Maps deixa de existir como fator.</strong> No SEO local, o perfil da
        empresa costuma ser a alavanca mais rápida — otimizar categorias, fotos e avaliações rende em
        semanas. Aqui não há mapa para aparecer, então essa via simplesmente não está disponível.</p>

        <p><strong>A proximidade para de filtrar concorrentes.</strong> No local, você compete com quem
        atende a mesma região — algumas dezenas de negócios. No nacional, você compete com todos os sites
        do Brasil ao mesmo tempo, em toda busca.</p>

        <p><strong>Não existe versão fácil do termo.</strong> No local, um termo difícil na capital pode
        ser fácil em uma cidade menor. Aqui não há esse recorte: cada busca é a disputa completa.</p>

        <h2>O que entra no lugar</h2>

        {tabela(
            ["", "SEO local", "IPTV (nacional)"],
            [
                ["Alavanca mais rápida", "perfil no Maps", "cauda longa de conteúdo"],
                ["Filtro de concorrência", "distância", "nenhum"],
                ["Peso dos backlinks", "secundário na maioria dos casos", "determinante"],
                ["Volume de conteúdo", "moderado", "alto e contínuo"],
                ["Primeiro sinal de progresso", "ações no perfil", "impressões em termos específicos"],
                ["Horizonte típico", "mais curto", "trimestres"],
            ],
            nota="Comparação estrutural entre os dois modelos de disputa. Prazos variam e não são garantidos."
        )}

        <p>A comparação geral entre os dois modelos está em
        {link('/blog/seo-local-ou-seo-nacional-diferenca/', 'SEO local ou SEO nacional')}. O que segue é o
        que muda especificamente neste nicho.</p>

        <h2>A cauda longa carrega os primeiros meses</h2>

        <p>Esta é a consequência prática mais importante. Sem mapa e sem proximidade, um projeto novo não
        tem como aparecer nos termos principais no começo. O que sustenta a fase inicial são as buscas
        muito específicas:</p>

        <ul>
          <li>dúvidas de compatibilidade com aparelho;</li>
          <li>requisitos técnicos e configuração;</li>
          <li>solução de problema durante o uso;</li>
          <li>comparações entre formas de contratar;</li>
          <li>perguntas de quem está avaliando antes de decidir.</li>
        </ul>

        <p>São buscas de volume individual baixo e disputa quase nula que, somadas, trazem visitante com
        intenção real. E têm um segundo efeito: cobrir bem esses assuntos constrói a relevância temática
        que depois sustenta a disputa dos termos maiores. É por isso que
        {link('/criacao-de-site-para-iptv/', 'o site precisa nascer com lugar para o conteúdo entrar')} —
        um site de página única não tem como capturar nada disso.</p>

        <h2>O que muda na forma de medir</h2>

        <p>No SEO local, dá para acompanhar ações no perfil e ver movimento em semanas. Aqui os primeiros
        indicadores são outros, e confundi-los faz o projeto parecer parado:</p>

        <ol>
          <li><strong>Páginas indexadas</strong> — mostra que a base técnica está certa. Primeiras semanas.</li>
          <li><strong>Termos únicos gerando impressão</strong> — mostra que o conteúdo está sendo
          considerado, mesmo em posições baixas. Primeiras semanas.</li>
          <li><strong>Posição média por grupo de termos</strong> — mostra avanço agregado. Alguns meses.</li>
          <li><strong>Domínios de referência</strong> — mostra a autoridade crescendo. Contínuo.</li>
          <li><strong>Posição dos termos principais</strong> — o objetivo, e o último a se mover.</li>
        </ol>

        <p>Um projeto que está indo bem mostra os itens 1 e 2 subindo bem antes do item 5. Avaliar só pelo
        último é o erro que mais faz projeto bom ser interrompido no meio.</p>

        <h2>O que isso muda no investimento</h2>

        <p>Disputa nacional custa mais que disputa local pelo mesmo motivo que demora mais: exige volume de
        conteúdo e construção de autoridade que a disputa local dispensa em boa parte dos casos.</p>

        <p>E existe um patamar mínimo. Em mercado nacional disputado, metade do investimento não entrega
        metade do resultado — costuma não entregar nada, porque o projeto não alcança o nível de cobertura
        e autoridade que aquela primeira página exige. Se o orçamento não cabe no alvo, a decisão certa é
        mudar de alvo, não reduzir o investimento no mesmo alvo. O raciocínio completo está em
        {link('/blog/quanto-custa-seo-para-iptv/', 'quanto custa SEO para IPTV')}.</p>

        <p>Como esse projeto é montado ponta a ponta — da marca ao acompanhamento — está em
        {link('/seo-para-iptv/', 'SEO para IPTV')}.</p>
    """,
    "faq": [
        ("Faz sentido criar páginas por cidade para IPTV?",
         "Quase nunca. Páginas regionais só fazem sentido quando existe busca real com nome de cidade e "
         "quando cada página tem informação própria daquele lugar. Nas buscas deste nicho, a cidade "
         "raramente aparece — criar essas páginas gera conteúdo repetido sem demanda para capturar."),
        ("O Google Meu Negócio ajuda em algum aspecto?",
         "Para a operação em si, não — não há busca local relevante para captar. Um perfil pode servir a "
         "outros propósitos institucionais, mas não é alavanca de aquisição neste modelo."),
        ("Dá para começar por uma região e expandir depois?",
         "Não funciona como no SEO local, porque não existe recorte geográfico na busca. O equivalente aqui "
         "é começar por recortes de assunto — cobrir bem um conjunto de dúvidas específicas e expandir a "
         "cobertura a partir dele."),
        ("Por que o prazo é maior que em SEO local?",
         "Porque as duas alavancas rápidas do local não existem aqui, e sobram justamente as mais lentas: "
         "acumular cobertura de conteúdo e construir autoridade, que tem ritmo próprio e não é acelerável "
         "por orçamento."),
    ],
    "cta": ("Quer entender o tamanho da disputa nacional no seu caso? Na análise do projeto eu leio quem "
            "ocupa as posições que você quer, classifico seus termos por dificuldade e devolvo o escopo "
            "necessário com cenário de prazo.",
            ANALISE, "Solicitar análise do projeto"),
})
