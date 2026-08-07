# -*- coding: utf-8 -*-
"""
Cluster "Domínios e autoridade" — lote 2 (backlog do plano §5.1, produzido em 07/08/2026).

 6 como-escolher-dominio-expirado-com-autoridade
11 o-que-acontece-com-seo-ao-trocar-dominio
13 dominio-caiu-o-que-fazer

Diferenciação em relação ao lote 1:
   6 × artigo 14  — o 14 VERIFICA um domínio (é seguro?); o 6 COMPARA candidatos
                    (qual dos três?). Perguntas e entregáveis diferentes.
  11 × artigo 43  — o 43 responde "vou perder posições?" (resultado); o 11 explica
                    a mecânica do que é reavaliado, o que atravessa e o que se perde.

ATENÇÃO — política §2.5 aplicada ao artigo 13:
"Domínio caiu" tem leituras legítimas (registro expirado, falha de DNS ou
hospedagem, suspensão por pendência cadastral, perda de controle do domínio) e uma
leitura que a RCB não atende: domínio retirado do ar por ordem judicial ou
administrativa. O artigo cobre as legítimas e, no caso da ordem judicial, diz o que
tem de ser dito — é assunto jurídico, não de SEO — sem oferecer nenhum contorno.
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-07"
CAT = "Domínios e autoridade"
ANALISE = "/analise-de-projeto/"

ARTIGOS = []


# ------------------------------------------------------------------
# 6
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-escolher-dominio-expirado-com-autoridade",
    "h1": "Como escolher um domínio expirado com autoridade",
    "title": "Como escolher um domínio expirado com autoridade | RCB",
    "desc": ("Você tem três ou quatro candidatos e precisa decidir qual comprar. Os critérios de "
             "comparação, em ordem de peso, e o teto de preço de cada um."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>Este artigo responde uma pergunta específica: você já tem alguns candidatos na mão e precisa
        decidir <strong>qual deles comprar</strong>. É diferente de verificar se um domínio é seguro —
        isso está em {link('/blog/como-analisar-historico-de-dominio-expirado/', 'como analisar o histórico de um domínio expirado')},
        e é o passo que vem antes deste.</p>

        {caixa('<p><strong>Resposta direta:</strong> entre candidatos que já passaram na verificação de '
               'segurança, o que decide é a <strong>relevância temática com o seu projeto</strong> — não a '
               'métrica de autoridade, não a quantidade de links, não a idade. Um domínio com poucos links '
               'do seu assunto vale mais que um com muitos links de assunto nenhum.</p>')}

        <h2>Primeiro: eliminar, não comparar</h2>

        <p>Comparação só faz sentido entre candidatos que sobreviveram à eliminação. Qualquer um destes
        sinais tira o domínio da lista, independentemente de quão bom ele pareça no resto:</p>

        <ul>
          <li>Mudança brusca de tema ou idioma no histórico — padrão de domínio capturado.</li>
          <li>Períodos de conteúdo gerado automaticamente, sem sentido.</li>
          <li>Âncoras concentradas em termo comercial de nicho monetizado.</li>
          <li>O nome reproduz marca de terceiros.</li>
          <li>O nome já aparece associado a golpe ou reclamação.</li>
        </ul>

        <p>Se você precisa se convencer de que um sinal desses é aceitável, ele não é. Domínio novo custa
        pouco e não traz surpresa.</p>

        <h2>Os critérios de comparação, em ordem de peso</h2>

        <h3>1. Relevância temática (peso maior)</h3>
        <p>O que estava publicado ali tem relação com o que você vai publicar? Esse é o fator que
        determina quanto do histórico se converte em vantagem. Sem proximidade de assunto, links herdados
        entregam pouco — e o domínio vira um domínio novo caro.</p>

        <p>Pergunta objetiva: <em>alguém que chegasse ao domínio pelo conteúdo antigo teria interesse no
        conteúdo novo?</em></p>

        <h3>2. Qualidade das fontes que apontam</h3>
        <p>Não quantos links, e sim de onde vêm. Abra dez domínios de referência ao acaso e conte quantos
        têm conteúdo real, publicação recente e linha editorial coerente. Se poucos passarem, o perfil não
        sustenta o preço.</p>

        <h3>3. Continuidade de uso</h3>
        <p>Um domínio usado de forma contínua vale mais que um que ficou anos parado. O valor do histórico
        se dilui com o tempo, e o preço pedido raramente reflete isso.</p>

        <h3>4. O nome em si</h3>
        <p>Fácil de falar, de escrever e de lembrar — porque ele vai ser dito em conversa e digitado no
        celular. Histórico bom com nome ruim resolve metade do problema e cria outro.</p>

        <h3>5. Métrica de autoridade (peso menor)</h3>
        <p>Serve para ordenar candidatos numa triagem rápida. Não serve para decidir: é estimativa de
        ferramenta de terceiro, não dado do Google, e pode ser inflada de propósito antes da venda.</p>

        <h2>Comparando na prática</h2>

        <p>Um exemplo do tipo de decisão que aparece com frequência:</p>

        {tabela(
            ["", "Candidato A", "Candidato B", "Candidato C"],
            [
                ["Métrica de autoridade", "alta", "média", "baixa"],
                ["Tema anterior", "sem relação", "próximo ao seu", "próximo ao seu"],
                ["Fontes que apontam", "muitas, sem audiência", "poucas, com audiência", "poucas, com audiência"],
                ["Continuidade", "3 anos parado", "uso contínuo", "1 ano parado"],
                ["Nome", "bom", "razoável", "bom"],
                ["Preço", "alto", "médio", "baixo"],
                ["Decisão", "descartar", "melhor opção", "boa alternativa"],
            ],
            nota="Exemplo ilustrativo do formato da decisão. O candidato com a melhor métrica é o que menos serve."
        )}

        <p>O candidato A é o que mais aparece em anúncio e o que menos entrega: métrica alta construída
        sobre fontes fracas, sem relação temática, e ainda com o histórico diluído por anos de abandono.</p>

        <h2>Definindo um teto de preço</h2>

        <p>Nenhuma recomendação de compra está completa sem um teto. A referência é sempre a mesma
        comparação: <strong>quanto custaria construir autoridade equivalente do zero?</strong></p>

        <p>Se o domínio custa mais que isso, não compensa — você paga mais por um ponto de partida do que
        pagaria pelo caminho inteiro, e ainda assume o risco de o histórico não render o esperado.</p>

        <p>Vale lembrar a proporção: se o domínio consumir uma fatia grande do orçamento total do projeto,
        provavelmente é a decisão errada, por melhor que ele pareça. Domínio é ponto de partida — o que
        define o resultado é o que se constrói em cima. Um domínio excelente sem conteúdo e sem
        {link('/link-building-para-nichos-competitivos/', 'autoridade construída')} não ranqueia.</p>

        <h2>Quando nenhum candidato serve</h2>

        <p>É um desfecho comum e perfeitamente aceitável. Se nenhum passa nos critérios, a resposta certa
        é registrar um domínio novo pelo nome e aplicar a diferença em conteúdo e autoridade — onde o
        retorno é previsível.</p>

        <p>A comparação completa entre os dois caminhos está em
        {link('/blog/dominio-expirado-ainda-funciona-para-seo/', 'domínio expirado ainda funciona para SEO')}.</p>
    """,
    "faq": [
        ("Devo escolher pelo maior número de backlinks?",
         "Não. O que conta é a quantidade de domínios distintos e, principalmente, a qualidade e a "
         "relevância deles. Um perfil com poucos links de veículos reais do seu assunto supera um com "
         "centenas de fontes sem audiência."),
        ("Idade do domínio é um critério forte?",
         "É secundário, e só vale acompanhado de uso contínuo. Um domínio registrado há dez anos mas "
         "parado há cinco tem histórico bem menos relevante que o registro sugere."),
        ("Posso mudar o tema do domínio depois de comprar?",
         "Pode, mas quanto mais distante o novo tema estiver do antigo, menos o histórico rende — e mais "
         "o domínio se aproxima de um domínio novo, só que caro."),
        ("Vale comprar mais de um domínio para testar?",
         "Raramente. O custo se multiplica e o esforço se divide: dois projetos pela metade rendem menos "
         "que um projeto inteiro. Melhor investir a análise em escolher bem um."),
    ],
    "cta": ("Tem candidatos na mão e precisa decidir? Na análise do projeto eu comparo os domínios pelos "
            "critérios acima e devolvo uma recomendação objetiva — qual comprar, até que valor, ou por que "
            "nenhum deles compensa.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 11
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "o-que-acontece-com-seo-ao-trocar-dominio",
    "h1": "O que acontece com o SEO quando o domínio é trocado?",
    "title": "O que acontece com o SEO ao trocar de domínio | RCB",
    "desc": ("A mecânica da troca: o que é reavaliado, o que atravessa pelos redirecionamentos e o "
             "que se perde de qualquer forma."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/migracao-de-dominio-seo/", "Migração de domínio"),
    "corpo": f"""
        <p>A pergunta "vou perder posições?" tem resposta prática em
        {link('/blog/trocar-de-dominio-faz-perder-posicoes/', 'trocar de domínio faz perder posições')}.
        Este artigo responde outra coisa: <strong>o que exatamente acontece por baixo</strong> — o que é
        reavaliado, o que atravessa e o que não atravessa.</p>

        {caixa('<p><strong>Resposta direta:</strong> o redirecionamento permanente informa que o conteúdo '
               'mudou de endereço, e boa parte do valor acumulado por cada página tende a ser reconhecida '
               'no destino. Mas isso não é uma transferência automática nem instantânea: cada endereço '
               'precisa ser rastreado de novo, e parte dos sinais estava ligada ao domínio antigo, não às '
               'páginas.</p>')}

        <h2>O que acontece, na ordem</h2>

        <ol>
          <li><strong>O rastreador encontra o redirecionamento.</strong> Ele volta a um endereço antigo
          que já conhecia e recebe a informação de que aquilo mudou de lugar em definitivo.</li>
          <li><strong>O endereço novo é rastreado.</strong> O conteúdo do destino é lido e comparado com o
          que existia antes.</li>
          <li><strong>A equivalência é avaliada.</strong> Se o destino tem conteúdo equivalente, o
          histórico da página antiga tende a ser associado a ele. Se o destino não tem relação — o caso
          clássico é redirecionar tudo para a página inicial — essa associação não acontece.</li>
          <li><strong>O índice é atualizado aos poucos.</strong> Página por página, conforme o rastreamento
          avança. Em site grande, isso leva bem mais tempo que em site pequeno.</li>
          <li><strong>As posições se reacomodam.</strong> Costuma haver oscilação durante esse período,
          porque parte do site está em situação indefinida enquanto o resto ainda não foi reavaliado.</li>
        </ol>

        <h2>O que atravessa e o que não atravessa</h2>

        {tabela(
            ["Elemento", "Atravessa?", "Observação"],
            [
                ["Valor dos links que apontavam para cada página", "em boa parte",
                 "desde que o destino tenha conteúdo equivalente"],
                ["Conteúdo e sua relevância", "sim", "é o mesmo conteúdo, em outro endereço"],
                ["Histórico de rastreamento do endereço", "não", "o endereço novo começa a ser conhecido agora"],
                ["Sinais ligados ao domínio antigo", "parcialmente", "parte estava associada ao domínio, não à página"],
                ["Menções ao nome antigo sem link", "não", "passam a apontar para uma marca que não existe mais"],
                ["Autoridade acumulada como um todo", "parcialmente", "não é uma transferência integral"],
                ["Endereços que você esqueceu de mapear", "não", "o histórico deles se perde"],
            ],
            nota="A última linha é a causa mais comum de perda permanente — e a mais evitável."
        )}

        <h2>Por que a equivalência de conteúdo é o ponto crítico</h2>

        <p>Este é o mecanismo que mais gente entende errado. O redirecionamento não é uma tubulação que
        despeja valor de um endereço no outro. Ele é uma <strong>informação</strong>: "isto agora está
        aqui".</p>

        <p>Essa informação só faz sentido se o destino for de fato o mesmo conteúdo. Uma página que
        ranqueava para uma busca específica, redirecionada para a home, aponta para algo que não responde
        àquela busca — e o histórico dela deixa de ter onde se apoiar.</p>

        <p>É por isso que o mapa um a um não é preciosismo: <strong>ele é a diferença entre preservar e
        perder</strong>. O processo completo está em
        {link('/blog/como-migrar-site-para-outro-dominio/', 'como migrar um site para outro domínio')}.</p>

        <h2>Por que manter o domínio antigo por muito tempo</h2>

        <p>Enquanto existirem links externos apontando para o endereço antigo, os redirecionamentos
        continuam tendo função — eles são o caminho pelo qual esse valor chega ao destino.</p>

        <p>Desligar o domínio antigo cedo interrompe esse caminho de forma permanente. Os links de
        terceiros passam a apontar para o nada, e não há como recuperá-los sem contatar cada veículo. Em
        termos de custo, manter um registro ativo é barato; refazer relacionamento com fontes de links é
        caro e demorado.</p>

        <h2>O que ajuda a atravessar melhor</h2>

        <ul>
          <li><strong>Inventário completo</strong> antes de qualquer coisa — inclusive páginas antigas que
          ninguém lembrava.</li>
          <li><strong>Mapa um a um</strong>, com o destino sendo sempre o conteúdo equivalente.</li>
          <li><strong>Conteúdo do destino igual ou melhor</strong> — reduzir o conteúdo durante a migração
          confunde a avaliação de equivalência.</li>
          <li><strong>Uma mudança de cada vez</strong> — trocar domínio e reestruturar o site juntos
          impede saber o que causou o quê.</li>
          <li><strong>Atualizar as fontes de links mais relevantes</strong>, porque link direto rende mais
          que link redirecionado.</li>
          <li><strong>Monitorar por semanas</strong>, já que os problemas aparecem conforme o rastreamento
          avança.</li>
        </ul>

        <p>Se a troca já aconteceu e o tráfego caiu, boa parte dessas falhas é corrigível — o caminho é
        {link('/recuperacao-de-trafego-organico/', 'diagnóstico e recuperação')}.</p>
    """,
    "faq": [
        ("O redirecionamento transfere 100% da autoridade?",
         "Não. Boa parte tende a ser reconhecida quando há equivalência de conteúdo, mas não é uma "
         "transferência integral nem automática — parte dos sinais estava associada ao domínio antigo."),
        ("Quanto tempo até o domínio novo assumir as posições?",
         "Varia com o tamanho do site e a frequência de rastreamento. Sites menores estabilizam mais rápido; "
         "sites grandes levam mais tempo porque cada endereço precisa ser rastreado de novo. Não há prazo garantido."),
        ("Posso usar redirecionamento temporário em vez de permanente?",
         "Para mudança definitiva de domínio, não. O redirecionamento temporário sinaliza que o endereço "
         "antigo vai voltar, o que é o oposto do que você quer comunicar."),
        ("E os links que apontam para páginas que eu apaguei?",
         "Se não houver destino equivalente, o valor desses links se perde. Vale identificar no inventário "
         "quais páginas antigas recebiam links externos antes de decidir apagar qualquer coisa."),
    ],
    "cta": ("Vai trocar de domínio e quer reduzir a perda? Na análise do projeto eu monto o inventário, o "
            "mapa de redirecionamento e a sequência de virada — com o que precisa estar pronto antes de "
            "qualquer coisa ir ao ar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 13
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "dominio-caiu-o-que-fazer",
    "h1": "Domínio caiu: o que fazer com o site e o SEO?",
    "title": "Domínio caiu: o que fazer com o site e o SEO | RCB",
    "desc": ("Antes de agir, descubra por que caiu. O diagnóstico das causas — registro, DNS, "
             "hospedagem, cadastro — e o que fazer em cada uma."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/migracao-de-dominio-seo/", "Migração de domínio"),
    "corpo": f"""
        <p>Site fora do ar é urgência, e urgência faz gente agir antes de entender. Neste caso a pressa
        custa caro: <strong>a causa determina completamente o que fazer</strong>, e algumas reações
        precipitadas transformam um problema de horas em perda permanente.</p>

        {caixa('<p><strong>Primeiro passo, sempre:</strong> descobrir por que caiu. As causas mais comuns '
               'são administrativas ou técnicas — registro não renovado, DNS mal configurado, hospedagem '
               'fora do ar, pendência cadastral no registrador. Cada uma tem uma solução diferente, e a '
               'maioria não exige trocar de domínio.</p>')}

        <h2>Diagnóstico: por que caiu</h2>

        {tabela(
            ["Causa", "Como identificar", "O que fazer"],
            [
                ["Registro expirado", "consulta pública mostra o domínio vencido ou em prazo de resgate",
                 "renovar imediatamente — há prazo, e ele é curto"],
                ["Pendência cadastral", "registrador informa dado desatualizado ou documentação pendente",
                 "regularizar junto ao registrador"],
                ["DNS mal configurado", "domínio ativo, mas não resolve para lugar nenhum",
                 "corrigir o apontamento"],
                ["Hospedagem fora do ar", "domínio resolve, servidor não responde",
                 "acionar a hospedagem"],
                ["Certificado vencido", "site abre com aviso de segurança e perde acesso",
                 "renovar o certificado"],
                ["Perda de controle do domínio", "transferência ou alteração que você não autorizou",
                 "acionar o registrador e, se for o caso, apoio jurídico"],
                ["Retirada por ordem judicial ou administrativa", "notificação formal ou bloqueio determinado por autoridade",
                 "assunto jurídico — ver observação abaixo"],
            ],
            nota="A consulta pública de registro e um teste de resolução de DNS resolvem o diagnóstico na maior parte dos casos."
        )}

        <h2>Uma observação necessária sobre o último caso</h2>

        <p>Se o domínio saiu do ar por determinação judicial ou administrativa, isso não é um problema de
        SEO e não tem solução técnica. É uma questão jurídica, e o caminho é assessoria jurídica
        própria — não um contorno técnico.</p>

        <p>Registrar outro domínio para continuar a mesma operação nessa situação não resolve o problema
        de origem e pode agravá-lo. <strong>A RCB não atende esse cenário</strong>, em nenhum nicho e em
        nenhuma faixa de investimento. O restante deste artigo trata das causas administrativas e técnicas,
        que são a maioria dos casos e têm solução.</p>

        <h2>O caso mais comum: registro expirado</h2>

        <p>É a causa que mais aparece, e a que tem o relógio correndo. Depois do vencimento existe um
        período em que o titular ainda consegue renovar. Passado esse prazo, o domínio pode ser liberado
        para registro por qualquer pessoa — e aí a recuperação deixa de ser uma questão de pagar a
        renovação.</p>

        <p>O que fazer, na ordem:</p>

        <ol>
          <li><strong>Consultar a situação do registro agora.</strong> Saber em que fase está define quanto
          tempo você tem.</li>
          <li><strong>Renovar imediatamente</strong>, se ainda estiver no prazo. Não espere resolver mais
          nada antes disso.</li>
          <li><strong>Conferir o apontamento de DNS</strong> depois da renovação — às vezes ele volta
          diferente.</li>
          <li><strong>Verificar se o site voltou completo</strong>, e não só a página inicial.</li>
          <li><strong>Ativar renovação automática e alerta de vencimento</strong>, para não repetir.</li>
        </ol>

        <h2>O impacto no SEO enquanto está fora</h2>

        <p>Vale calibrar a preocupação: <strong>uma queda curta costuma ter impacto pequeno</strong>. O
        rastreador encontra o site indisponível, tenta de novo depois, e a situação se normaliza quando o
        site volta.</p>

        <p>O problema aparece com a duração. Quanto mais tempo fora, mais páginas deixam de ser
        confirmadas no índice, e a recuperação passa a exigir que tudo seja rastreado novamente. Uma
        indisponibilidade de algumas horas raramente deixa marca; uma de semanas deixa.</p>

        <p>Por isso a prioridade é sempre <strong>voltar ao ar rápido</strong>, mesmo que provisoriamente,
        antes de qualquer otimização.</p>

        <h2>Quando não dá para recuperar o domínio</h2>

        <p>Se o registro foi perdido e outra pessoa assumiu, não existe migração possível — sem acesso ao
        domínio antigo, não há como criar redirecionamentos. O que resta é reconstrução:</p>

        <ul>
          <li><strong>Recuperar o conteúdo</strong>, a partir de backup próprio ou de registros públicos de
          arquivo da web.</li>
          <li><strong>Publicar em um domínio novo</strong>, mantendo a estrutura de endereços quando fizer
          sentido.</li>
          <li><strong>Refazer contato com as fontes de links mais relevantes</strong>, pedindo atualização
          do endereço. É trabalhoso e é o que mais recupera.</li>
          <li><strong>Atualizar perfis, materiais e integrações</strong> que apontavam para o endereço antigo.</li>
          <li><strong>Reconstruir autoridade</strong>, assumindo que boa parte do acumulado se perdeu.</li>
        </ul>

        <p>É um recomeço com vantagem — você tem o conteúdo e sabe o que funcionava —, mas é um recomeço.
        O processo de reconstrução se aproxima do descrito em
        {link('/migracao-de-dominio-seo/', 'migração de domínio')}, sem a parte que mais protege, que são
        os redirecionamentos.</p>

        <h2>Prevenção: cinco minutos que evitam o problema</h2>

        <ul>
          <li>Renovação automática ativada, com cartão válido e conferido.</li>
          <li>Registro em nome da empresa ou do titular real — nunca de fornecedor ou ex-funcionário.</li>
          <li>E-mail de contato do domínio acessível e monitorado.</li>
          <li>Dados cadastrais atualizados no registrador.</li>
          <li>Bloqueio de transferência ativado.</li>
          <li>Backup do site em lugar que não dependa da mesma hospedagem.</li>
        </ul>

        <p>O item mais negligenciado é o segundo: domínio registrado em nome de terceiro é o que transforma
        um contratempo administrativo em perda de ativo.</p>
    """,
    "faq": [
        ("Perdi tráfego enquanto o site ficou fora. Volta?",
         "Em quedas curtas, a recuperação costuma ser rápida e quase completa depois que o site volta. "
         "Quanto mais longa a indisponibilidade, mais páginas precisam ser rastreadas de novo e mais "
         "demorada é a normalização."),
        ("Devo registrar um domínio novo enquanto resolvo?",
         "Só se a recuperação do original for inviável. Publicar a mesma operação em dois domínios ao "
         "mesmo tempo divide sinais e cria conteúdo duplicado — piora a situação em vez de contornar."),
        ("O domínio expirou e outra pessoa registrou. Tem o que fazer?",
         "Do lado técnico, não: sem acesso ao domínio não há redirecionamento possível. Se houver marca "
         "registrada envolvida, pode existir caminho jurídico — mas isso é conversa com advogado, não com "
         "consultor de SEO."),
        ("Como saber se caiu por DNS ou por hospedagem?",
         "Se o domínio não resolve para endereço nenhum, o problema é de DNS ou de registro. Se resolve "
         "mas o servidor não responde, o problema é de hospedagem. Essa checagem leva menos de um minuto "
         "e direciona quem acionar."),
    ],
    "cta": ("Site fora do ar ou tráfego perdido depois de um problema de domínio? Na análise do projeto eu "
            "identifico a causa, o que dá para recuperar e em que ordem agir — antes de mexer no que não "
            "precisa ser mexido.",
            ANALISE, "Solicitar análise do projeto"),
})
