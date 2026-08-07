# -*- coding: utf-8 -*-
"""
Artigos do cluster IPTV e streaming.

 1 quanto-custa-seo-para-iptv
 2 quanto-tempo-posicionar-site-iptv
 4 como-criar-site-para-iptv-do-zero
 5 dominio-novo-ou-expirado-para-iptv
 8 quanto-investir-backlinks-iptv
10 estruturar-site-iptv-para-gerar-contatos
15 site-para-revendedor-iptv-o-que-precisa-ter

POLÍTICA (plano §2.5): todo artigo deste cluster fala a operações que possuem
direito ou autorização sobre o conteúdo que distribuem. Nenhum texto trata de
contornar bloqueio judicial ou administrativo, nem orienta distribuição de
conteúdo sem direito.
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-06"
CAT = "IPTV e streaming"
ANALISE = "/analise-de-projeto/"

NOTA_LICENCA = ('<p><strong>Nota sobre este cluster:</strong> os conteúdos de IPTV e streaming deste site '
                'se dirigem a operadores, plataformas e distribuidores que possuem direito ou autorização '
                'sobre o conteúdo que distribuem. Essa condição é verificada na análise do projeto, antes '
                'de qualquer proposta.</p>')

ARTIGOS = []


# ------------------------------------------------------------------
# 1
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quanto-custa-seo-para-iptv",
    "h1": "Quanto custa SEO para IPTV?",
    "title": "Quanto custa SEO para IPTV? O que forma o preço | RCB",
    "desc": ("Por que não existe valor de tabela para um projeto de IPTV, quais fatores formam o "
             "custo e como estimar o investimento antes de pedir orçamento."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-iptv/", "SEO para IPTV"),
    "corpo": f"""
        <p>Não existe preço de tabela, e qualquer valor dito antes de olhar a concorrência do seu caso
        seria chute. O que dá para explicar é o que forma o custo — e isso permite estimar a faixa.</p>

        {caixa(NOTA_LICENCA)}

        <h2>Por que este nicho é mais caro que a média</h2>

        <p>Três características empurram o custo para cima, e nenhuma delas é margem do fornecedor:</p>

        <p><strong>A disputa é nacional por natureza.</strong> O serviço é entregue pela internet e o
        cliente pode estar em qualquer lugar. Não há mapa nem proximidade ajudando — todo o peso recai
        sobre conteúdo, estrutura e autoridade, que são as frentes mais lentas e mais caras.</p>

        <p><strong>Autoridade é difícil de construir aqui.</strong> Muitos veículos evitam o tema, o que
        reduz o conjunto de fontes relevantes disponíveis. Cada conquista custa mais tempo e mais dinheiro
        que em nichos neutros — e é o principal fator de prazo do projeto.</p>

        <p><strong>Costuma começar do zero.</strong> Sem marca, sem domínio, sem site. Isso significa que a
        construção da base faz parte do projeto, e não é algo que aconteceu antes dele.</p>

        <h2>Os fatores que movem a faixa</h2>

        {tabela(
            ["Fator", "Reduz o custo", "Aumenta o custo"],
            [
                ["Ponto de partida", "site e conteúdo existentes", "marca, domínio e site do zero"],
                ["Domínio", "histórico limpo e relevante já definido", "necessidade de triagem e avaliação"],
                ["Alvo escolhido", "termos de disputa média", "termo principal do nicho"],
                ["Volume de conteúdo", "cobertura enxuta", "cobertura ampla e contínua"],
                ["Autoridade", "ritmo moderado e constante", "construção intensiva"],
                ["Prazo desejado", "horizonte de trimestres", "expectativa de semanas"],
                ["Manutenção", "revisão periódica", "atualização de alta frequência"],
            ],
            nota="Fatores de esforço, não tabela de preço. A faixa de cada projeto sai da análise."
        )}

        <h2>Como estimar sozinho antes de pedir orçamento</h2>

        <ol>
          <li>Pesquise os termos que você quer disputar.</li>
          <li>Liste os dez primeiros resultados e veja há quanto tempo cada site existe.</li>
          <li>Conte aproximadamente quantas páginas cada um tem sobre o tema.</li>
          <li>Observe se publicam com frequência — datas recentes indicam ritmo ativo.</li>
          <li>Estime quanto conteúdo você precisaria para ter cobertura comparável.</li>
          <li>Some a construção de autoridade e o período de manutenção.</li>
        </ol>

        <p>O número aproximado que sai já responde a pergunta mais útil: <strong>esse alvo cabe no seu
        orçamento?</strong> Se não couber, a decisão certa normalmente não é gastar menos no mesmo alvo,
        e sim escolher um alvo menor primeiro.</p>

        <h2>O erro que custa mais que o projeto</h2>

        <p>Investir abaixo do patamar que a disputa exige. Em mercado competitivo, metade do investimento
        não entrega metade do resultado — costuma não entregar nada, porque o projeto não alcança o nível
        mínimo de cobertura e autoridade daquela primeira página.</p>

        <p>O resultado prático é: dinheiro gasto, conteúdo publicado, site na terceira página. Por isso uma
        análise honesta pode recomendar
        {link('/seo-para-revendedor-iptv/', 'começar com um escopo menor e proporcional')} em vez de um
        projeto grande subfinanciado.</p>

        <h2>O que costuma estar incluído</h2>

        <ul>
          <li>Estratégia e leitura de concorrência.</li>
          <li>Marca e domínio, quando o projeto começa do zero.</li>
          <li>{link('/criacao-de-site-para-iptv/', 'Construção do site')} com estrutura de conversão.</li>
          <li>Arquitetura de conteúdo e produção contínua.</li>
          <li>{link('/link-building-para-iptv/', 'Construção de autoridade')}.</li>
          <li>Execução técnica e acompanhamento com relatórios.</li>
        </ul>

        <p>Nem todo caso precisa de tudo — o escopo é definido na análise, e é ele que determina a faixa.</p>
    """,
    "faq": [
        ("Existe um valor mínimo para começar?",
         "Existe um patamar mínimo de execução, que varia conforme o alvo escolhido. Abaixo dele o projeto "
         "tende a não produzir resultado. Qual é esse patamar no seu caso só dá para dizer depois de ler a "
         "concorrência dos termos pretendidos."),
        ("O domínio e a hospedagem estão incluídos?",
         "A escolha e a configuração fazem parte do trabalho. O custo dos serviços em si é do cliente, e "
         "tudo é registrado em nome dele, com acesso completo."),
        ("Backlinks entram no valor?",
         "A construção de autoridade faz parte do escopo quando contratada, com plano e critério definidos. "
         "O que não existe é pacote de quantidade fixa nem promessa de backlinks ilimitados."),
        ("Dá para pagar por etapas?",
         "O desenho mais comum é uma fase de construção mais pesada seguida de acompanhamento mensal. Isso "
         "distribui o investimento e permite avaliar o retorno antes de ampliar o escopo."),
    ],
    "cta": ("Quer um número que faça sentido para o seu caso? Na análise do projeto eu leio a concorrência "
            "real dos seus termos e devolvo escopo, cenário de prazo e faixa de investimento.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 2
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quanto-tempo-posicionar-site-iptv",
    "h1": "Quanto tempo demora para posicionar um site de IPTV?",
    "title": "Quanto tempo demora para posicionar um site de IPTV? | RCB",
    "desc": ("Os fatores que realmente mexem no prazo de um projeto no nicho, o que costuma "
             "aparecer primeiro e por que nenhum prazo é garantido."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-iptv/", "SEO para IPTV"),
    "corpo": f"""
        <p>Depende do termo, do ponto de partida e do ritmo de execução. Qualquer resposta em forma de
        número fixo é vendedor falando, não análise.</p>

        {caixa('<p><strong>Resposta direta:</strong> buscas específicas e de cauda longa costumam responder '
               'antes; os termos principais do nicho levam consideravelmente mais tempo e dependem de '
               'conteúdo acumulado e autoridade construída. Nenhum prazo é garantido — o que uma análise '
               'séria entrega são cenários com as premissas escritas.</p>')}

        <h2>O que aparece primeiro</h2>

        <p>A curva de um projeto neste nicho tem uma ordem previsível:</p>

        <ol>
          <li><strong>Indexação.</strong> As páginas começam a entrar no índice em semanas. É o primeiro
          sinal de que a base técnica está correta.</li>
          <li><strong>Impressões em cauda longa.</strong> Buscas muito específicas — dúvidas técnicas,
          compatibilidade de dispositivo, como funciona — começam a gerar aparições.</li>
          <li><strong>Primeiros cliques.</strong> Ainda em volume baixo, vindos dessas buscas específicas.</li>
          <li><strong>Posição média subindo.</strong> O conjunto de termos começa a melhorar de forma
          agregada, mesmo sem nenhum termo principal ter chegado ao topo.</li>
          <li><strong>Termos principais.</strong> Por último, e dependendo de autoridade acumulada.</li>
        </ol>

        <p>Avaliar o projeto só pelo item 5 faz ele parecer parado durante meses em que está avançando. É
        o motivo mais comum de projetos bons serem cancelados cedo demais.</p>

        <h2>Os quatro fatores que mais mexem no prazo</h2>

        <h3>1. A força de quem já está posicionado</h3>
        <p>É o fator dominante. Concorrentes com domínios maduros, muito conteúdo e perfil de links robusto
        exigem que você construa algo comparável — e isso leva tempo, não só dinheiro.</p>

        <h3>2. O domínio</h3>
        <p>Um domínio novo parte do zero. Um domínio com histórico limpo e relevante pode encurtar parte do
        caminho — com a ressalva de que domínio nenhum garante autoridade herdada. Ver
        {link('/blog/dominio-novo-ou-expirado-para-iptv/', 'domínio novo ou expirado para IPTV')}.</p>

        <h3>3. O ritmo real de execução</h3>
        <p>Não o contratado: o executado. Projeto que atrasa aprovação de conteúdo atrasa resultado na mesma
        proporção. É a variável que mais está sob o seu controle.</p>

        <h3>4. A construção de autoridade</h3>
        <p>A frente mais lenta deste nicho, porque poucos veículos aceitam o tema. É o principal motivo de
        o prazo aqui ser maior que em mercados neutros. Detalhado em
        {link('/link-building-para-iptv/', 'link building para IPTV')}.</p>

        <h2>O que não encurta o prazo</h2>

        <ul>
          <li>Pagar mais por técnicas de risco — isso aumenta a variância, não a média.</li>
          <li>Publicar muito conteúdo raso de uma vez.</li>
          <li>Adquirir muitos links em pouco tempo, o que cria padrão artificial.</li>
          <li>Trocar de fornecedor a cada poucos meses, reiniciando a curva.</li>
        </ul>

        <h2>Como acompanhar sem se enganar</h2>

        {tabela(
            ["Indicador", "O que mostra", "Quando se move"],
            [
                ["Páginas indexadas", "se a base técnica está certa", "primeiras semanas"],
                ["Termos únicos com impressão", "se o conteúdo está sendo considerado", "primeiras semanas"],
                ["Posição média por grupo", "avanço agregado", "alguns meses"],
                ["Domínios de referência", "se a autoridade cresce", "contínuo"],
                ["Contatos gerados", "se o tráfego é qualificado", "conforme o volume aparece"],
                ["Posição dos termos principais", "o objetivo final", "por último"],
            ],
            nota="Os quatro primeiros indicam direção muito antes de o último se mexer."
        )}

        <h2>Uma expectativa honesta</h2>

        <p>Projetos neste nicho trabalham em horizonte de trimestres, não de semanas. É comum haver
        períodos de aparente estagnação enquanto indexação e autoridade se acumulam, seguidos de movimentos
        mais visíveis.</p>

        <p>Se alguém oferece primeira página em poucas semanas nos termos principais, vale perguntar
        exatamente qual termo, com qual volume de busca — a resposta costuma revelar que o termo prometido
        não é o que interessa.</p>

        <p>A pergunta fechada — <em>dá para chegar em três ou quatro meses?</em> — é respondida com um
        modelo de faixas de dificuldade em
        {link('/blog/iptv-primeira-pagina-3-4-meses/', 'IPTV na primeira página em 3 ou 4 meses')}.</p>
    """,
    "faq": [
        ("É possível chegar à primeira página em três ou quatro meses?",
         "Em termos de baixa e média disputa, às vezes sim. Nos termos principais do nicho, dificilmente. O "
         "que muda o cenário é o ponto de partida: domínio com histórico limpo e conteúdo já publicado "
         "encurta caminho; domínio novo em mercado saturado, não."),
        ("Por que meu projeto parece parado no terceiro mês?",
         "Porque provavelmente está sendo avaliado só pela posição dos termos principais, que são os "
         "últimos a se mover. Verifique indexação, número de termos únicos gerando impressão e posição "
         "média — esses indicadores mostram se há avanço."),
        ("Parar de publicar por alguns meses atrasa muito?",
         "Atrasa mais do que o tempo parado, porque os concorrentes continuam avançando. Retomar significa "
         "recuperar terreno perdido antes de voltar a progredir."),
    ],
    "cta": ("Quer um cenário de prazo com as premissas escritas? Na análise do projeto eu leio a "
            "concorrência dos seus termos e devolvo a estimativa por grupo, com o que ela assume — sem "
            "prometer calendário.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 4
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-criar-site-para-iptv-do-zero",
    "h1": "Como criar um site para IPTV do zero",
    "title": "Como criar um site para IPTV do zero | RCB Consultoria",
    "desc": ("As decisões que precisam ser tomadas antes da primeira página: marca, domínio, "
             "estrutura, conversão e o que preparar para o site crescer sem reforma."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/criacao-de-site-para-iptv/", "Criação de site"),
    "corpo": f"""
        <p>A maior parte dos erros de um projeto neste nicho é cometida antes da primeira linha de conteúdo
        — nas decisões de estrutura que parecem detalhes e definem o teto do projeto.</p>

        {caixa(NOTA_LICENCA)}

        <h2>Decisão 1 — Marca própria ou não</h2>

        <p>É a primeira e a mais subestimada. Operar sem nome próprio significa competir divulgando a marca
        de quem fornece o serviço — e qualquer outro distribuidor do mesmo serviço aparece na mesma busca,
        com a mesma mensagem.</p>

        <p>Marca própria é o que separa o seu ativo do ativo de terceiros. Não precisa ser um projeto de
        branding longo: nome, logotipo, paleta e aplicação básica bastam para o negócio ter identidade.</p>

        <h2>Decisão 2 — O domínio</h2>

        <p>Critérios que importam, em ordem:</p>

        <ul>
          <li>Fácil de falar e de escrever — vai ser dito em conversa e digitado no celular.</li>
          <li>Não reproduz marca de terceiros. Isso é questão jurídica, não de SEO.</li>
          <li>Curto o suficiente para caber em mensagem e ser lembrado.</li>
          <li>Sem histórico problemático, se for um domínio já usado.</li>
        </ul>

        <p>Se estiver considerando um domínio com histórico, a verificação vem antes da compra —
        {link('/blog/dominio-novo-ou-expirado-para-iptv/', 'domínio novo ou expirado')} compara os dois
        caminhos.</p>

        <h2>Decisão 3 — Estrutura de páginas</h2>

        <p>Aqui está o erro mais comum do nicho: o site de uma página só, com uma tabela de planos e um
        botão de contato. Funciona para quem já conhece a marca e não serve para mais nada — porque
        <strong>não existe onde o conteúdo entrar</strong>.</p>

        <p>Sem páginas por assunto, o site não tem como disputar busca nenhuma, e qualquer investimento
        posterior em SEO começa refazendo a base. A estrutura mínima que sustenta crescimento:</p>

        {tabela(
            ["Página", "Função", "Busca que atende"],
            [
                ["Inicial", "proposta clara e caminho para os planos", "marca"],
                ["Planos e condições", "o que está incluído em cada opção", "quem já quer contratar"],
                ["Compatibilidade e dispositivos", "onde funciona e o que é preciso", "dúvida técnica pré-contratação"],
                ["Como funciona", "explicação do serviço", "quem está aprendendo"],
                ["Dúvidas frequentes", "objeções respondidas", "comparação e decisão"],
                ["Suporte e configuração", "resolução de problema", "quem já é cliente"],
                ["Blog", "cobertura ampla do tema", "cauda longa"],
                ["Contato", "conversão direta", "todas"],
            ],
            nota="Cada uma com endereço próprio — é isso que permite disputar a busca correspondente."
        )}

        <h2>Decisão 4 — Como o visitante vira contato</h2>

        <p>Quatro coisas costumam decidir se a visita vira conversa:</p>

        <ol>
          <li><strong>Clareza sobre o que está incluído.</strong> Quem não entende o que recebe não pergunta
          — sai e procura outro.</li>
          <li><strong>Comparação entre planos na mesma tela.</strong> Rolar para cima e para baixo
          comparando é fricção.</li>
          <li><strong>Dúvidas respondidas antes do contato.</strong> Quem resolve sozinho chega mais
          preparado e converte melhor.</li>
          <li><strong>Contato sem atrito.</strong> Botão visível em qualquer ponto, com a mensagem já
          iniciada e identificando a origem.</li>
        </ol>

        <p>Detalhado em {link('/blog/estruturar-site-iptv-para-gerar-contatos/', 'como estruturar o site para gerar contatos')}.</p>

        <h2>Decisão 5 — Preparar para crescer</h2>

        <p>O site vai passar de poucas páginas para dezenas. Se a estrutura não foi pensada para isso, a
        reforma chega junto com o primeiro resultado. O que decidir agora:</p>

        <ul>
          <li>Padrão de endereços das páginas, consistente desde o início.</li>
          <li>Hierarquia entre páginas principais e conteúdo de apoio.</li>
          <li>Onde a informação que muda com frequência fica armazenada — em um lugar só, não repetida
          manualmente em várias páginas.</li>
          <li>Regras de link interno entre as camadas.</li>
          <li>Onde o blog vai morar e como ele se conecta às páginas comerciais.</li>
        </ul>

        <h2>Decisão 6 — Base técnica</h2>

        <p>Resolvido na construção, não depois: hierarquia de títulos, endereços limpos, título e descrição
        próprios por página, dados estruturados adequados, carregamento rápido no celular — que é de onde
        vem a maior parte do acesso — e medição instalada desde o primeiro dia.</p>

        <p>Nada disso encarece significativamente se for feito junto. Tudo isso encarece muito se for
        corrigido depois.</p>
    """,
    "faq": [
        ("Quanto tempo leva para o site ficar pronto?",
         "Depende do escopo: um site de planos com poucas páginas sai mais rápido que uma estrutura com "
         "blog, suporte e várias páginas comerciais. O prazo é fechado junto com o escopo, na análise."),
        ("Posso começar com uma página só e crescer depois?",
         "Pode, desde que a base já esteja preparada para receber as demais — padrão de endereços, "
         "hierarquia e local do conteúdo definidos. O problema não é começar pequeno; é começar sem "
         "estrutura e ter que refazer."),
        ("Preciso de blog desde o começo?",
         "Não precisa estar cheio, mas precisa existir e estar estruturado. É o blog que captura as buscas "
         "de cauda longa que sustentam os primeiros meses do projeto."),
    ],
    "cta": ("Vai construir o site do zero? Na análise do projeto definimos escopo, estrutura de páginas, "
            "prazo e faixa de investimento — e verificamos o critério de atendimento antes de qualquer "
            "proposta.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 5
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "dominio-novo-ou-expirado-para-iptv",
    "h1": "Domínio novo ou domínio expirado para IPTV?",
    "title": "Domínio novo ou expirado para IPTV? | RCB Consultoria",
    "desc": ("A comparação honesta entre começar do zero e comprar histórico neste nicho — o que "
             "cada opção entrega e quando uma delas é claramente melhor."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/dominio-expirado-para-iptv/", "Domínio expirado"),
    "corpo": f"""
        <p>É a primeira decisão de quase todo projeto do nicho, e a que mais recebe conselho ruim.</p>

        {caixa('<p><strong>Resposta direta:</strong> domínio novo é a opção previsível e suficiente para a '
               'maioria dos casos. Domínio expirado só compensa quando a análise confirma histórico limpo '
               '<em>e</em> relevância temática com o projeto — e mesmo assim ele encurta o ponto de partida, '
               'não substitui conteúdo nem autoridade nova.</p>')}

        <h2>O que se espera e o que se recebe</h2>

        <p>A expectativa que circula é a de que um domínio com links apontando faz o projeto começar com
        anos de vantagem. Na prática, o que se compra é <strong>histórico</strong> — e histórico pode
        ajudar, ser indiferente ou atrapalhar.</p>

        <p>Links antigos apontam para páginas que não existem mais. Se o conteúdo novo não tem relação
        nenhuma com o que estava lá, esses links perdem boa parte do sentido. E o valor do histórico se
        dilui com o tempo: um domínio que ficou anos parado já perdeu muito do que carregava.</p>

        <h2>Comparação</h2>

        {tabela(
            ["", "Domínio novo", "Domínio expirado"],
            [
                ["Custo", "baixo", "de baixo a muito alto"],
                ["Risco herdado", "nenhum", "existe e precisa ser verificado"],
                ["Previsibilidade", "total", "depende inteiramente da análise"],
                ["Ponto de partida", "do zero", "pode encurtar parte do caminho"],
                ["Tempo até estar pronto", "imediato", "triagem, análise e aquisição"],
                ["Quando escolher", "quase sempre", "quando as verificações passam"],
            ],
            nota="Não existe escolha certa universal — existe escolha certa para um domínio específico, verificado."
        )}

        <h2>Os três desfechos de um domínio expirado</h2>

        <p><strong>Ajuda.</strong> Histórico limpo, tema próximo ao seu, links legítimos. O site novo parte
        com alguma relevância reconhecida. É o cenário desejado e o menos frequente.</p>

        <p><strong>É indiferente.</strong> O domínio teve uso real, tem alguns links legítimos, mas de um
        assunto sem relação com o seu. Você pagou por algo que não vai render — e teria o mesmo resultado
        com um domínio novo, por uma fração do preço.</p>

        <p><strong>Atrapalha.</strong> Perfil de links artificial, período de uso para spam, conteúdo
        problemático ainda indexado ou penalização anterior. O passivo vem junto e não desaparece porque o
        dono mudou.</p>

        <h2>O que verificar antes de comprar</h2>

        <ol>
          <li><strong>Histórico de conteúdo</strong> — o que esteve publicado ali ao longo dos anos.
          Mudanças bruscas de tema ou idioma são o sinal mais grave.</li>
          <li><strong>Distribuição de âncoras</strong> — repetição do mesmo termo comercial indica perfil
          fabricado.</li>
          <li><strong>Origem dos links</strong> — os sites que apontam existem de verdade e têm audiência?</li>
          <li><strong>Relevância temática</strong> — o tema anterior tem relação com o seu projeto?</li>
          <li><strong>Reputação do nome</strong> — o domínio aparece associado a algo indesejado?</li>
        </ol>

        <p>O passo a passo completo está em
        {link('/blog/como-analisar-historico-de-dominio-expirado/', 'como analisar o histórico de um domínio expirado')}
        e em {link('/blog/como-saber-se-dominio-expirado-foi-usado-para-spam/', 'como identificar uso para spam')}.</p>

        <h2>A regra prática deste nicho</h2>

        <p>Se a escolha é entre um domínio expirado duvidoso e um domínio novo, o novo quase sempre sai mais
        barato no fim das contas — porque limpar um domínio comprometido custa mais tempo e mais dinheiro
        do que construir a partir do zero, e nem sempre funciona.</p>

        <p>E vale lembrar a proporção: se o custo do domínio consumir uma fatia grande do orçamento total,
        provavelmente é a decisão errada. Domínio é ponto de partida, não projeto.</p>
    """,
    "faq": [
        ("Domínio expirado garante autoridade?",
         "Não. Nenhum domínio transmite autoridade automaticamente. O que ele carrega é histórico, e só a "
         "análise do caso específico diz se esse histórico ajuda, é indiferente ou atrapalha."),
        ("Quanto costuma custar um domínio expirado?",
         "Varia de valores baixos em leilão a quantias altas por nomes disputados. O preço reflete a "
         "percepção de valor do nome, não a qualidade do histórico — comprar caro não reduz o risco."),
        ("Posso comprar e testar?",
         "Pode, mas é uma aposta cara: se o domínio tiver passivo, você descobre depois de construir o "
         "projeto em cima dele. A verificação prévia custa muito menos que a correção posterior."),
    ],
    "cta": ("Tem um domínio em vista? Envie na análise do projeto e eu verifico histórico, perfil de links "
            "e risco antes da compra — inclusive quando a recomendação for não comprar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 8
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "quanto-investir-backlinks-iptv",
    "h1": "Quanto investir em backlinks para um projeto de IPTV?",
    "title": "Quanto investir em backlinks para IPTV? | RCB",
    "desc": ("Como dimensionar a verba de autoridade dentro do projeto, por que este nicho é mais "
             "caro nessa frente e o que não fazer com o orçamento."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/link-building-para-iptv/", "Link building para IPTV"),
    "corpo": f"""
        <p>Autoridade é a frente mais cara e mais lenta de um projeto neste nicho — e a que mais recebe
        proposta de quantidade em vez de critério.</p>

        {caixa('<p><strong>Resposta direta:</strong> não existe valor de referência, porque o alvo é '
               'comparativo, não absoluto. O que se dimensiona é: quantos domínios distintos apontam para '
               'quem ocupa as posições que você quer, de que tipo são, e quanto custaria conquistar algo '
               'comparável no seu ritmo. Esse número é específico do seu caso.</p>')}

        <h2>Por que este nicho custa mais nessa frente</h2>

        <p>Não é por causa de preço inflado — é por <strong>escassez</strong>. Muitos veículos evitam o
        tema, o que reduz bastante o conjunto de fontes relevantes disponíveis.</p>

        <p>Isso tem três efeitos práticos: cada conquista exige mais prospecção, a tentação de recorrer a
        fontes de baixa qualidade aumenta, e o prazo do projeto se estende. O terceiro é o mais importante
        de assumir desde o início, para não virar surpresa no terceiro mês.</p>

        <h2>Como dimensionar a verba</h2>

        <ol>
          <li>Levante quantos domínios distintos apontam para os cinco primeiros resultados do seu termo-alvo.</li>
          <li>Classifique por tipo: veículos setoriais, blogs, portais, comunidades.</li>
          <li>Identifique quais desses tipos são realisticamente acessíveis para um projeto novo.</li>
          <li>Estime o custo médio de conquista no seu nicho para esses tipos.</li>
          <li>Multiplique pela quantidade necessária para chegar perto do perfil deles.</li>
          <li><strong>Divida pelo prazo do projeto</strong> — porque adquirir tudo de uma vez cria padrão
          artificial e trabalha contra você.</li>
        </ol>

        <p>O último passo é o que transforma um número assustador em um orçamento mensal viável. E não é
        só uma questão de caixa: o ritmo gradual é tecnicamente necessário.</p>

        <h2>A proporção dentro do projeto</h2>

        <p>Autoridade não é uma frente isolada. Ela compete por orçamento com conteúdo e execução técnica,
        e a proporção certa muda ao longo do projeto:</p>

        {tabela(
            ["Fase", "Peso em conteúdo", "Peso em autoridade", "Por quê"],
            [
                ["Início", "maior", "início da prospecção", "sem conteúdo, o link não tem o que sustentar"],
                ["Meio", "constante", "crescente", "há material que justifica a referência"],
                ["Maturidade", "manutenção", "maior", "autoridade decide os termos principais"],
            ],
            nota="Investir pesado em autoridade antes de existir conteúdo é o desperdício mais comum do nicho."
        )}

        <h2>O que não fazer com o orçamento</h2>

        <ul>
          <li><strong>Comprar pacotes por quantidade.</strong> Volume de fontes fracas entrega pouco e cria
          passivo que precisa ser gerenciado depois.</li>
          <li><strong>Concentrar a aquisição em poucos meses.</strong> Cria padrão detectável, justamente o
          oposto do objetivo.</li>
          <li><strong>Pagar caro por métrica alta sem audiência.</strong> Site sem leitores entrega pouco,
          por melhor que pareça em ferramenta.</li>
          <li><strong>Começar antes de ter conteúdo.</strong> Gasta a fonte antes de ela render — e você
          não consegue a mesma menção duas vezes.</li>
        </ul>

        <p>Os critérios de seleção estão em
        {link('/blog/como-avaliar-qualidade-de-um-backlink/', 'como avaliar a qualidade de um backlink')}.</p>

        <p>E a leitura de quais tipos de veículo realmente rendem neste nicho está em
        {link('/blog/backlinks-para-iptv-funcionam/', 'backlinks para IPTV funcionam?')}.</p>

        <h2>O que esperar do investimento</h2>

        <p>Autoridade age de forma acumulada e defasada. Raramente dá para atribuir um movimento de posição
        a um link específico — o que se observa é a evolução do conjunto ao longo de meses.</p>

        <p>Por isso o relatório desta frente mostra domínios conquistados com endereço e data, contexto de
        cada menção, distribuição de âncoras acumulada e comparação com os concorrentes-alvo. Não mostra
        promessa de quantidade fixa por mês, porque isso não é como o trabalho funciona.</p>
    """,
    "faq": [
        ("Quantos links por mês devo conquistar?",
         "O ritmo deve ser compatível com o tamanho e a idade do site, não com uma meta fixa. Crescimento "
         "súbito em site novo cria padrão que trabalha contra o projeto — a construção acelera ao longo do "
         "tempo, em vez de começar no máximo."),
        ("Dá para competir neste nicho sem investir em autoridade?",
         "Em termos de cauda longa e recortes específicos, sim — e é por aí que projetos novos entram. Nos "
         "termos principais, dificilmente, porque é justamente a autoridade que decide as posições de topo."),
        ("Vale mais um link caro ou vários baratos?",
         "Em geral o caro de veículo relevante, desde que o preço reflita audiência e relevância reais. "
         "Vários links baratos de sites sem audiência tendem a somar pouco e formar padrão indesejado."),
    ],
    "cta": ("Quer dimensionar essa frente com base no seu alvo real? Na análise do projeto eu levanto o "
            "perfil de links de quem ocupa as posições que você quer e devolvo um plano com critério e "
            "faixa de investimento.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 10
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "estruturar-site-iptv-para-gerar-contatos",
    "h1": "Como estruturar um site de IPTV para gerar contatos",
    "title": "Como estruturar um site de IPTV para gerar contatos | RCB",
    "desc": ("O que separa um site que recebe visita de um que gera conversa: clareza de oferta, "
             "comparação, objeções respondidas e contato sem atrito."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/criacao-de-site-para-iptv/", "Criação de site"),
    "corpo": f"""
        <p>Tráfego sem conversão é custo. E neste nicho o problema raramente é falta de visita — é a visita
        chegar e não virar conversa.</p>

        {caixa(NOTA_LICENCA)}

        <h2>O que o visitante precisa resolver antes de chamar</h2>

        <p>Quem chega a uma página deste tipo tem um conjunto previsível de dúvidas. Se elas não forem
        respondidas na página, a pessoa não pergunta — ela sai e procura outro. As principais:</p>

        <ul>
          <li>O que exatamente está incluído?</li>
          <li>Funciona no aparelho que eu tenho?</li>
          <li>O que preciso ter para funcionar?</li>
          <li>Como é a instalação e quem me ajuda?</li>
          <li>Qual a diferença entre os planos?</li>
          <li>Como faço para contratar?</li>
        </ul>

        <p>Cada uma dessas dúvidas é uma seção da página — ou uma página inteira, quando o volume de busca
        justifica.</p>

        <h2>Os quatro elementos que mais movem conversão</h2>

        <h3>1. Clareza sobre a oferta</h3>
        <p>Descrição objetiva do que o serviço entrega, sem promessa vaga. Visitante que não entende o que
        recebe não pergunta — presume o pior e sai.</p>

        <h3>2. Comparação na mesma tela</h3>
        <p>Se há mais de um plano, eles precisam ser comparáveis lado a lado, com as mesmas linhas de
        informação. Obrigar a pessoa a rolar para cima e para baixo comparando é fricção pura — e no celular
        é pior ainda.</p>

        <h3>3. Objeções respondidas antes do contato</h3>
        <p>Compatibilidade, requisitos, funcionamento, suporte. Quem tira a dúvida sozinho chega mais
        preparado à conversa — e converte melhor, porque já passou pela própria triagem.</p>

        <h3>4. Contato sem atrito</h3>
        <p>Botão visível em qualquer ponto da página, não só no fim. Mensagem já iniciada, para a pessoa
        não precisar formular a primeira frase. E identificação de origem, para você saber de qual página
        veio cada conversa.</p>

        <h2>A estrutura de uma página que converte</h2>

        {tabela(
            ["Bloco", "Função", "Erro comum"],
            [
                ["Topo", "dizer o que é, para quem, e o próximo passo", "frase genérica sem informação"],
                ["Planos", "comparação clara lado a lado", "tabela ilegível no celular"],
                ["Compatibilidade", "onde funciona e o que é preciso", "omitir e gerar dúvida"],
                ["Como funciona", "reduzir insegurança do processo", "explicar de forma técnica demais"],
                ["Dúvidas frequentes", "derrubar objeções restantes", "perguntas que ninguém faz"],
                ["Contato", "conversão", "só no rodapé"],
            ],
            nota="A ordem pode variar, mas nenhum desses blocos deveria faltar."
        )}

        <h2>Medir para saber onde investir</h2>

        <p>Sem medição, a decisão de onde investir conteúdo vira palpite. O mínimo:</p>

        <ul>
          <li>Evento de clique por botão e por página, para separar o que gera conversa do que só gera visita.</li>
          <li>Origem identificada na própria mensagem, para você saber de onde veio sem perguntar.</li>
          <li>Relatório periódico de quais páginas convertem.</li>
        </ul>

        <p>Esse dado costuma revelar surpresas — páginas de dúvida técnica que geram mais contato que a
        página de planos, por exemplo. Sem medir, ninguém saberia.</p>

        <h2>O erro estrutural que limita tudo</h2>

        <p>Site de uma página só. Ele pode até converter quem já conhece a marca, mas não tem onde receber
        conteúdo — e portanto não capta ninguém novo pela busca.</p>

        <p>Cada dúvida do visitante é uma busca que alguém está fazendo agora. Sem uma página para
        respondê-la, essa busca vai para o concorrente que tem. Detalhado em
        {link('/blog/como-criar-site-para-iptv-do-zero/', 'como criar um site do zero')}.</p>
    """,
    "faq": [
        ("Preciso mostrar preço na página?",
         "Mostrar reduz contato desqualificado e aumenta a qualidade da conversa — quem chega já sabe o "
         "que esperar. Não mostrar aumenta o volume de mensagens, com boa parte delas perguntando preço e "
         "saindo em seguida. A escolha depende de qual dos dois problemas incomoda mais."),
        ("Formulário ou contato direto por mensagem?",
         "Neste nicho, mensagem direta costuma converter melhor, porque o público espera resposta rápida. "
         "Formulário faz sentido quando há qualificação a fazer antes da conversa."),
        ("Quantas páginas o site precisa ter para começar a converter?",
         "Menos do que parece: a página de planos bem construída e três ou quatro páginas de dúvida "
         "frequente já sustentam a conversão inicial. O volume maior vem depois, para captar cauda longa."),
    ],
    "cta": ("Quer o site construído para converter desde o começo? Na análise do projeto definimos "
            "estrutura, páginas necessárias e medição — com escopo, prazo e faixa de investimento.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 15
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "site-para-revendedor-iptv-o-que-precisa-ter",
    "h1": "Site para revendedor de IPTV: o que precisa ter",
    "title": "Site para revendedor de IPTV: o que precisa ter | RCB",
    "desc": ("O mínimo que um revendedor autorizado precisa para deixar de depender só de rede "
             "social e começar a captar pelo Google."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/seo-para-revendedor-iptv/", "Revendedor"),
    "corpo": f"""
        <p>A maior parte dos revendedores vende por perfil de rede social e mensagem direta. Funciona — até
        o dia em que o perfil cai, e aí não sobra nada.</p>

        {caixa('<p><strong>Nota:</strong> este conteúdo se dirige a revendedores e distribuidores '
               '<strong>autorizados</strong>, que operam com contrato ou autorização do fornecedor do '
               'serviço que revendem. Essa condição é verificada na análise do projeto.</p>')}

        <h2>Por que ter site próprio muda o jogo</h2>

        <p><strong>O canal passa a ser seu.</strong> Perfil em plataforma de terceiros pode ser restringido,
        ter alcance reduzido ou ser encerrado sem aviso — levando junto a lista de contatos e o histórico.
        Site próprio e contatos registrados continuam existindo.</p>

        <p><strong>Quem pesquisa passa a te encontrar.</strong> Rede social não aparece bem em busca. Existe
        demanda pesquisando esse tipo de serviço todo dia, e ela vai inteira para quem tem site.</p>

        <p><strong>A marca deixa de ser a do fornecedor.</strong> Sem nome próprio, você compete divulgando
        a marca de quem te fornece — e qualquer outro revendedor do mesmo serviço aparece na mesma busca,
        com a mesma mensagem.</p>

        <h2>O mínimo necessário</h2>

        <p>Não é preciso começar grande. O que não pode faltar:</p>

        {tabela(
            ["Item", "Por quê", "Sem isso"],
            [
                ["Marca própria simples", "diferencia você dos demais revendedores", "você é intercambiável"],
                ["Página de planos clara", "responde a dúvida principal", "visitante sai sem perguntar"],
                ["Comparação entre planos", "facilita a escolha", "fricção na decisão"],
                ["Compatibilidade e requisitos", "dúvida técnica mais frequente", "perde quem tem dúvida"],
                ["Contato com origem identificada", "você sabe de onde veio", "não dá para medir nada"],
                ["Páginas de dúvida frequente", "captura busca de cauda longa", "não capta ninguém novo"],
                ["Medição básica", "mostra o que funciona", "decisão por palpite"],
            ],
            nota="Sete itens que cabem em um site enxuto — e que sustentam crescimento depois."
        )}

        <h2>A ordem que faz sentido para quem está começando</h2>

        <p>A tentação é querer tudo de uma vez. Para operação pequena, isso costuma ser desperdício. A
        sequência que respeita o retorno:</p>

        <ol>
          <li><strong>Primeiro:</strong> site enxuto com marca própria, planos claros e contato
          identificado. Resolve o problema do ativo e já capta quem chega.</li>
          <li><strong>Depois:</strong> páginas para as dúvidas mais comuns antes da contratação. É o
          conteúdo que traz busca sem exigir autoridade alta.</li>
          <li><strong>Em seguida:</strong> conteúdo contínuo e início de trabalho de autoridade, quando o
          retorno das etapas anteriores justificar.</li>
          <li><strong>Só então:</strong> disputa dos termos mais amplos, que já é escopo de
          {link('/seo-para-iptv/', 'projeto completo')}.</li>
        </ol>

        <p>Essa ordem existe para o investimento acompanhar o retorno, em vez de exigir de uma vez um valor
        que não faz sentido para o porte da operação.</p>

        <h2>O que não vale a pena no começo</h2>

        <ul>
          <li>Identidade visual elaborada — nome, logo e paleta bastam.</li>
          <li>Blog com dezenas de artigos antes de o site converter.</li>
          <li>Investimento pesado em autoridade antes de existir conteúdo.</li>
          <li>Disputar de cara os termos mais amplos do nicho.</li>
          <li>Domínio caro — {link('/blog/dominio-novo-ou-expirado-para-iptv/', 'domínio novo resolve')}
          na maioria dos casos.</li>
        </ul>

        <h2>Continue usando a rede social</h2>

        <p>Nada disso é argumento para abandonar o canal que já funciona. É argumento para não depender só
        dele. O desenho que costuma render mais: rede social continua gerando conversa com quem já segue, e
        o site capta quem está pesquisando e ainda não conhece você — com os dois apontando para o mesmo
        canal de contato.</p>
    """,
    "faq": [
        ("Sou revendedor pequeno. Vale a pena ter site?",
         "Vale, principalmente pelo risco: se o perfil cair, quem tem site perde um canal e quem não tem "
         "perde o negócio. E o site capta quem pesquisa no Google, que é público que a rede social não "
         "alcança."),
        ("Preciso de marca própria mesmo revendendo serviço de outro?",
         "Ajuda muito. Sem nome próprio você divulga a marca do fornecedor e concorre com todos os outros "
         "revendedores dele na mesma busca. Marca própria é o que separa o seu ativo do dele."),
        ("Quanto tempo até o site trazer contato?",
         "Buscas específicas e de menor disputa costumam responder antes; termos mais amplos levam mais "
         "tempo. O cenário de prazo sai na análise, com as premissas explícitas — sem garantia de calendário."),
    ],
    "cta": ("Quer montar uma estrutura própria com escopo proporcional ao seu tamanho? Na análise do "
            "projeto a gente dimensiona o começo sem empurrar o que você ainda não precisa.",
            ANALISE, "Solicitar análise do projeto"),
})
