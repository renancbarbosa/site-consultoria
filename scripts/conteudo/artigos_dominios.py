# -*- coding: utf-8 -*-
"""
Artigos do cluster "Domínios e autoridade" — domínios expirados e migração.

39 dominio-expirado-ainda-funciona-para-seo
40 dominio-expirado-com-backlinks-vale-a-pena
41 como-saber-se-dominio-expirado-foi-usado-para-spam
42 dominio-premium-ou-dominio-expirado
14 como-analisar-historico-de-dominio-expirado
12 como-migrar-site-para-outro-dominio
43 trocar-de-dominio-faz-perder-posicoes
44 como-recuperar-trafego-organico-apos-queda

Nenhum destes textos promete que domínio expirado transmite autoridade, nem que
migração preserva posições (plano §2.1).
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-06"
CAT = "Domínios e autoridade"
ANALISE = "/analise-de-projeto/"

ARTIGOS = []


# ------------------------------------------------------------------
# 39
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "dominio-expirado-ainda-funciona-para-seo",
    "h1": "Domínio expirado ainda funciona para SEO?",
    "title": "Domínio expirado ainda funciona para SEO? | RCB",
    "desc": ("O que um domínio com histórico realmente entrega hoje, em que casos ajuda de verdade "
             "e quando ele custa mais caro que começar do zero."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>Funciona em alguns casos, é indiferente na maioria e atrapalha em uma parcela relevante. A
        diferença entre os três cenários não está no preço nem na métrica que o vendedor mostra — está no
        histórico do domínio específico.</p>

        {caixa('<p><strong>Resposta direta:</strong> nenhum domínio transmite autoridade automaticamente. '
               'O que ele carrega é histórico. Quando esse histórico é limpo, tem relevância temática com o '
               'novo projeto e vem de links legítimos, ele encurta parte do caminho. Quando não tem relação '
               'de tema, entrega pouco. Quando carrega spam ou penalização, é passivo.</p>')}

        <h2>O mito que sustenta o mercado</h2>

        <p>A expectativa que circula é mais ou menos esta: compra-se um domínio que já tem links apontando,
        sobe-se o site novo nele, e o projeto começa com anos de vantagem.</p>

        <p>O que realmente acontece é mais sutil. Links antigos apontam para páginas que não existem mais.
        Se o conteúdo novo não tem nenhuma relação com o que estava lá antes, esses links perdem boa parte
        do sentido — e sinal sem contexto vale pouco.</p>

        <p>Além disso, o valor do histórico se dilui com o tempo. Um domínio que ficou anos parado já
        perdeu boa parte do que carregava, mesmo que a métrica exibida no anúncio continue alta.</p>

        <h2>Quando realmente ajuda</h2>

        <p>Existe um cenário em que a compra compensa, e ele é bem específico. As quatro condições
        precisam valer juntas:</p>

        <ol>
          <li><strong>Relevância temática.</strong> O que estava publicado ali tem relação com o que você
          vai publicar. Sem isso, o resto importa pouco.</li>
          <li><strong>Perfil de links legítimo.</strong> As referências vieram de sites reais, com
          audiência, por motivos editoriais.</li>
          <li><strong>Histórico limpo.</strong> Nenhum período de uso para spam, conteúdo problemático ou
          sinal de penalização.</li>
          <li><strong>Continuidade razoável.</strong> O domínio não ficou muitos anos abandonado.</li>
        </ol>

        <p>Quando as quatro valem, o ganho é real: o site novo parte com alguma relevância já reconhecida,
        o que costuma encurtar a fase inicial do projeto. Não elimina a necessidade de conteúdo e de
        {link('/link-building-para-nichos-competitivos/', 'construção de autoridade nova')} — apenas
        adianta o ponto de partida.</p>

        <h2>Quando é indiferente</h2>

        <p>O caso mais comum. O domínio teve uso real, tem alguns links legítimos, mas de um assunto que
        não tem nada a ver com o seu projeto. O histórico existe e simplesmente não se converte em vantagem.</p>

        <p>Nesse cenário você pagou por algo que não vai render — e teria o mesmo resultado com um domínio
        novo, escolhido pelo nome, por uma fração do preço.</p>

        <h2>Quando atrapalha</h2>

        <p>O passivo vem junto e não desaparece porque o dono mudou:</p>

        <ul>
          <li>Perfil de links artificial, construído por compra em massa.</li>
          <li>Histórico de uso para spam, com conteúdo problemático ainda indexado.</li>
          <li>Penalização anterior que continua valendo.</li>
          <li>Associação do nome a algo indesejado, que aparece quando alguém pesquisa a marca.</li>
        </ul>

        <p>Em vários desses casos, limpar o domínio custa mais tempo e mais dinheiro do que começar do zero
        — e nem sempre funciona.</p>

        <h2>Como decidir sem apostar</h2>

        {tabela(
            ["Verificação", "O que procurar", "Sinal de alerta"],
            [
                ["Histórico de conteúdo", "que tema esteve publicado ali", "mudanças bruscas de assunto"],
                ["Perfil de links", "sites reais, com audiência", "muitos links de fontes desconhecidas"],
                ["Distribuição de âncoras", "variedade natural", "repetição do mesmo termo comercial"],
                ["Relevância temática", "proximidade com o seu projeto", "nenhuma relação de assunto"],
                ["Continuidade", "uso contínuo ao longo dos anos", "anos de abandono"],
                ["O nome", "serve comercialmente e é livre", "carrega marca de terceiros"],
            ],
            nota="Um único sinal de alerta grave costuma bastar para descartar o candidato."
        )}

        <p>O passo a passo dessa verificação está em
        {link('/blog/como-analisar-historico-de-dominio-expirado/', 'como analisar o histórico de um domínio expirado')}.</p>

        <h2>A conclusão prática</h2>

        <p>Para a maioria dos projetos, domínio novo é a escolha previsível e suficiente: custo baixo,
        risco zero e nenhuma surpresa. Domínio expirado entra quando a análise confirma que aquele caso
        específico compensa — e não como regra.</p>

        <p>Se a escolha é entre um domínio expirado duvidoso e um domínio novo, o novo quase sempre sai
        mais barato no fim das contas.</p>
    """,
    "faq": [
        ("Domínio expirado com métrica de autoridade alta é garantia de qualidade?",
         "Não. Essas métricas são estimativas de ferramentas de terceiros, não dados do Google, e podem "
         "ser infladas de propósito antes da venda. Servem como filtro inicial, nunca como critério de "
         "decisão."),
        ("Preciso manter o mesmo tema do domínio anterior?",
         "Não é obrigatório, mas é o que faz o histórico render. Quanto mais distante o novo tema estiver "
         "do antigo, menos os links herdados significam — e mais o domínio se aproxima de um domínio novo, "
         "só que caro."),
        ("Quanto tempo leva para o histórico fazer efeito?",
         "Não é imediato nem garantido. O conteúdo novo precisa ser rastreado e avaliado, e o efeito do "
         "histórico aparece de forma gradual. Em muitos casos o efeito percebido é pequeno o suficiente "
         "para não justificar o preço pago."),
    ],
    "cta": ("Tem um domínio em vista? Envie na análise do projeto e eu verifico histórico, perfil de links "
            "e risco antes de você comprar — inclusive quando a recomendação for não comprar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 40
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "dominio-expirado-com-backlinks-vale-a-pena",
    "h1": "Domínio expirado com backlinks vale a pena?",
    "title": "Domínio expirado com backlinks vale a pena? | RCB",
    "desc": ("Ter backlinks não é o mesmo que ter autoridade útil. Como avaliar se o perfil de links "
             "de um domínio à venda vale o preço pedido."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>"Domínio com backlinks" é o argumento de venda mais usado nesse mercado. Ele descreve um fato
        — existem links apontando — que por si só não diz nada sobre o valor.</p>

        {caixa('<p><strong>Resposta direta:</strong> o que importa não é <em>quantos</em> backlinks o '
               'domínio tem, e sim <em>de onde vêm</em>, <em>por quê</em> e <em>se têm relação com o que '
               'você vai publicar</em>. Um domínio com cinco links de veículos reais do seu setor vale mais '
               'que um com trezentos links de sites sem audiência.</p>')}

        <h2>As quatro perguntas que definem o valor</h2>

        <h3>1. Os sites que apontam existem de verdade?</h3>
        <p>Muitos domínios à venda têm perfis inflados por links de sites criados só para gerar links.
        Abra alguns deles: têm conteúdo real? Alguém visita? Publicam sobre assuntos coerentes ou sobre
        tudo ao mesmo tempo? Sites que apontam para nichos completamente desconexos são o sinal mais claro.</p>

        <h3>2. Os links foram conquistados ou fabricados?</h3>
        <p>Um link dentro de um artigo que cita o domínio por um motivo editorial é diferente de um link
        em rodapé, em lista de parceiros ou em um texto genérico criado para hospedá-lo. O contexto é
        visível e revela muito.</p>

        <h3>3. Existe relação temática com o seu projeto?</h3>
        <p>Esta é a pergunta que mais elimina candidatos. Links vindos de um tema completamente diferente
        do seu entregam pouco, porque a relevância que eles sinalizam não é a relevância que você precisa.</p>

        <h3>4. A distribuição de âncoras parece natural?</h3>
        <p>Se a maior parte dos links usa exatamente o mesmo termo comercial como texto, o perfil foi
        construído artificialmente. Perfis naturais misturam nome da marca, endereço do site, termos
        genéricos e variações.</p>

        <h2>O que os números do anúncio não mostram</h2>

        {tabela(
            ["O anúncio mostra", "O que ele não mostra"],
            [
                ["Métrica de autoridade alta", "se ela foi inflada de propósito antes da venda"],
                ["Número total de backlinks", "quantos domínios distintos são de fato"],
                ["Idade do domínio", "quantos anos ele ficou abandonado"],
                ["'Nunca penalizado'", "que a desvalorização silenciosa não gera registro"],
                ["'Nicho X'", "o que realmente esteve publicado ali ao longo dos anos"],
            ],
            nota="Nenhuma dessas lacunas é preenchida pagando mais caro — só por verificação."
        )}

        <h2>Um teste rápido antes de qualquer proposta</h2>

        <ol>
          <li>Pegue a lista de domínios que apontam para o candidato.</li>
          <li>Abra dez deles ao acaso.</li>
          <li>Conte quantos têm conteúdo real, publicação recente e assunto coerente.</li>
          <li>Veja quantos falam de algo próximo ao seu tema.</li>
        </ol>

        <p>Se poucos passarem nesse teste, o perfil não vale o que está sendo cobrado — independentemente
        do total exibido.</p>

        <h2>O erro de comprar pelo número</h2>

        <p>Quem compra por quantidade acaba levando um perfil que, além de não ajudar, precisa ser
        gerenciado depois. Links artificiais herdados continuam apontando para o seu domínio, e lidar com
        isso é escopo de {link('/consultoria-de-backlinks/', 'auditoria de perfil de links')} — um custo
        que não estava na conta da compra.</p>

        <p>A alternativa é simples: comprar um domínio novo pelo nome, gastar a diferença em
        {link('/link-building-para-nichos-competitivos/', 'autoridade construída com critério')} e saber
        exatamente de onde vem cada link do seu perfil.</p>
    """,
    "faq": [
        ("Quantos backlinks um domínio precisa ter para valer a pena?",
         "Não existe número. Um domínio com poucos links de veículos reais e temáticos vale mais que um com "
         "centenas de links de sites sem audiência. A avaliação é qualitativa, não quantitativa."),
        ("Posso redirecionar o domínio expirado para o meu site em vez de reconstruí-lo?",
         "É uma prática comum e ambígua: sem relação temática e sem conteúdo equivalente no destino, o "
         "redirecionamento tende a entregar pouco e pode ser interpretado como tentativa de manipulação. "
         "É uma decisão que precisa ser consciente."),
        ("Vale pagar caro por um domínio com bom perfil?",
         "Pode valer, se as quatro verificações passarem e o preço for menor que o custo de construir "
         "autoridade equivalente. Essa comparação é a única forma honesta de justificar o valor."),
    ],
    "cta": ("Quer saber se o perfil de links de um domínio à venda vale o preço? Na análise do projeto eu "
            "verifico origem, contexto, relevância temática e risco antes da compra.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 41
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-saber-se-dominio-expirado-foi-usado-para-spam",
    "h1": "Como saber se um domínio expirado foi usado para spam",
    "title": "Como saber se um domínio expirado teve spam | RCB",
    "desc": ("Os sinais que denunciam um domínio comprometido e como verificá-los com fontes "
             "públicas, antes de gastar dinheiro na compra."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>Boa parte dos domínios que circulam em leilão passou por algum período de uso abusivo. A boa
        notícia é que esse passado deixa rastro público — e verificar leva menos tempo do que se imagina.</p>

        {caixa('<p><strong>Resposta direta:</strong> os dois rastros mais confiáveis são o histórico de '
               'conteúdo (o que esteve publicado ali ao longo dos anos) e o perfil de links (de onde vêm '
               'as referências e com que texto). Um domínio comprometido quase sempre falha em pelo menos '
               'um dos dois — e o sinal é visível para quem sabe onde olhar.</p>')}

        <h2>Sinal 1 — Mudança brusca de idioma ou de tema</h2>

        <p>O padrão clássico: o domínio pertenceu a um negócio local por anos e, em determinado momento,
        passou a hospedar conteúdo em outro idioma sobre um assunto completamente diferente — normalmente
        de nichos que costumam usar esse tipo de recurso.</p>

        <p>Essa transição indica que o domínio foi capturado depois de expirar e usado para aproveitar o
        histórico. É o sinal mais fácil de identificar e um dos mais graves.</p>

        <h2>Sinal 2 — Períodos de conteúdo gerado automaticamente</h2>

        <p>Páginas com texto sem sentido, repetição excessiva de termos, listas de links soltos ou conteúdo
        visivelmente montado por máquina sem revisão. Indica uso para ocupar espaço no índice.</p>

        <h2>Sinal 3 — Âncoras concentradas em termos comerciais</h2>

        <p>Se a maior parte dos links que apontam para o domínio usa como texto exatamente o mesmo termo
        comercial — especialmente termos de nichos muito monetizados —, o perfil foi construído para
        manipular ranqueamento, não conquistado.</p>

        <p>Perfis naturais são desorganizados: misturam o nome da marca, o endereço do site, expressões
        genéricas e variações. Uniformidade é sinal de fabricação.</p>

        <h2>Sinal 4 — Volume de links vindo de fontes homogêneas</h2>

        <p>Muitos links chegando de sites que se parecem entre si — mesma estrutura, mesmo tipo de
        conteúdo, mesmo padrão de publicação — indica {link('/blog/o-que-e-pbn-e-como-funciona/', 'rede de sites')}.
        Herdar isso significa herdar o padrão.</p>

        <h2>Sinal 5 — Picos inexplicáveis de aquisição de links</h2>

        <p>Um domínio que ganhou centenas de links de referência em poucas semanas, sem nenhum motivo
        editorial visível naquele período, ganhou esses links por compra. O padrão fica registrado.</p>

        <h2>Sinal 6 — O nome já aparece associado a algo indesejado</h2>

        <p>Pesquise o nome do domínio entre aspas e veja o que aparece. Menções em listas de bloqueio,
        reclamações, fóruns de segurança ou associação a golpes são problema que nenhum trabalho de SEO
        resolve.</p>

        <h2>Onde verificar</h2>

        {tabela(
            ["O que verificar", "Onde olhar", "O que procurar"],
            [
                ["Histórico de conteúdo", "serviços públicos de arquivo da web", "mudanças de tema ou idioma"],
                ["Perfil de links", "ferramentas de análise de backlinks", "origem, volume e ritmo"],
                ["Âncoras", "as mesmas ferramentas", "repetição de termo comercial"],
                ["Reputação do nome", "busca pelo domínio entre aspas", "menções negativas"],
                ["Indexação atual", "busca pelo domínio no Google", "páginas estranhas ainda indexadas"],
            ],
            nota="Nenhuma fonte isolada é conclusiva. É o conjunto que forma o quadro."
        )}

        <h2>A ordem de verificação que economiza tempo</h2>

        <ol>
          <li>Comece pelo histórico de conteúdo — é onde os casos graves aparecem primeiro e descarta
          rápido os piores candidatos.</li>
          <li>Se passar, olhe a distribuição de âncoras — o segundo filtro mais eficiente.</li>
          <li>Se ainda passar, examine a origem dos links com calma.</li>
          <li>Por último, verifique reputação do nome e indexação atual.</li>
        </ol>

        <p>Essa ordem elimina a maioria dos candidatos nos dois primeiros passos, o que torna viável avaliar
        vários domínios sem gastar horas em cada um.</p>

        <h2>Encontrou um sinal. E agora?</h2>

        <p>Depende da gravidade. Mudança de idioma com conteúdo suspeito e âncoras concentradas são motivos
        para descartar sem pensar duas vezes — o preço não compensa. Um período curto de conteúdo fraco,
        seguido de anos de uso normal, pode ser tolerável.</p>

        <p>Na dúvida, a regra prática é: <strong>se você precisa se convencer de que está tudo bem, não
        está</strong>. Domínio novo custa pouco e não traz surpresa.</p>
    """,
    "faq": [
        ("Um domínio com histórico de spam pode ser recuperado?",
         "Às vezes, com desautorização de links, remoção de conteúdo indexado e reconstrução — processo "
         "longo e sem garantia. Na maioria dos casos sai mais barato começar em um domínio limpo."),
        ("O Google 'perdoa' o passado de um domínio?",
         "Histórico problemático tende a perder força com o tempo e com uso legítimo continuado, mas não "
         "há prazo definido nem certeza. Contar com esse esquecimento é apostar."),
        ("Ferramenta paga é obrigatória para essa verificação?",
         "Os dois sinais mais graves — mudança de tema no histórico e reputação do nome — dá para "
         "verificar com fontes públicas gratuitas. Para analisar perfil de links com profundidade, uma "
         "ferramenta de backlinks ajuda bastante."),
    ],
    "cta": ("Quer a verificação completa antes de comprar? Na análise do projeto eu levanto histórico, "
            "perfil de links, âncoras e reputação, e devolvo uma recomendação objetiva — comprar, não "
            "comprar, ou comprar até determinado valor.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 42
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "dominio-premium-ou-dominio-expirado",
    "h1": "Domínio premium ou domínio expirado: qual escolher?",
    "title": "Domínio premium ou expirado: qual escolher? | RCB",
    "desc": ("São produtos diferentes: um vende nome, o outro vende histórico. Entenda o que cada "
             "um entrega e qual faz sentido para o seu projeto."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>A comparação aparece o tempo todo e costuma partir de uma premissa errada — a de que os dois
        competem pela mesma função.</p>

        {caixa('<p><strong>Resposta direta:</strong> domínio premium vende <strong>nome</strong> — curto, '
               'memorável, comercialmente forte, normalmente sem histórico relevante. Domínio expirado vende '
               '<strong>histórico</strong> — um passado que pode ajudar, ser indiferente ou atrapalhar. Um '
               'exige avaliação de marca; o outro exige verificação de passado.</p>')}

        <h2>O que é cada um</h2>

        <h3>Domínio premium</h3>
        <p>Nome curto, fácil de falar e lembrar, muitas vezes uma palavra comum do setor. O preço reflete
        a raridade e o valor comercial do nome, não um histórico de SEO. Frequentemente está registrado há
        anos sem nunca ter tido site — o que significa histórico praticamente inexistente.</p>

        <h3>Domínio expirado</h3>
        <p>Domínio que teve uso e não foi renovado. O que se compra é o passado: conteúdo que esteve
        publicado, links acumulados, idade de uso real. O nome pode ser bom ou ruim — não é o ponto da venda.</p>

        <h2>Comparação direta</h2>

        {tabela(
            ["", "Premium", "Expirado"],
            [
                ["O que você compra", "o nome", "o histórico"],
                ["Risco herdado", "praticamente nenhum", "existe e precisa ser verificado"],
                ["Ganho de SEO imediato", "nenhum", "possível, se o histórico for bom"],
                ["Valor de marca", "alto", "variável, muitas vezes baixo"],
                ["Previsibilidade", "alta", "depende da análise"],
                ["Faixa de preço", "de alta a muito alta", "de baixa a muito alta"],
                ["Quando faz sentido", "marca de longo prazo", "quando a análise confirma histórico bom"],
            ],
            nota="Os dois podem ser caros. Só um dos dois pode vir com passivo."
        )}

        <h2>Qual escolher em cada situação</h2>

        <h3>Escolha premium quando…</h3>
        <ul>
          <li>a marca é parte central do negócio e vai durar anos;</li>
          <li>o nome será falado — em rádio, indicação boca a boca, vídeo;</li>
          <li>você quer previsibilidade e nenhuma surpresa;</li>
          <li>há orçamento e o nome disponível é realmente superior às alternativas.</li>
        </ul>

        <h3>Escolha expirado quando…</h3>
        <ul>
          <li>a análise confirmou histórico limpo <em>e</em> relevância temática com o seu projeto;</li>
          <li>o preço é menor que o custo estimado de construir autoridade equivalente;</li>
          <li>o nome também funciona comercialmente — histórico bom com nome ruim resolve metade do problema;</li>
          <li>você aceita que o ganho é de ponto de partida, não de resultado garantido.</li>
        </ul>

        <h3>Escolha um domínio novo comum quando…</h3>
        <ul>
          <li>nenhum candidato premium ou expirado passa nos critérios acima;</li>
          <li>o orçamento é melhor empregado em conteúdo e autoridade;</li>
          <li>você quer começar sem nenhuma variável desconhecida.</li>
        </ul>

        <p>Esse terceiro caminho é o mais frequente na prática — e o menos vendido, porque ninguém ganha
        comissão nele.</p>

        <h2>O falso dilema</h2>

        <p>Muita gente trata a escolha do domínio como a decisão que define o projeto. Não é. Domínio é
        ponto de partida; o que define o resultado é o que se constrói em cima dele.</p>

        <p>Um domínio excelente com pouco conteúdo e nenhuma autoridade não ranqueia. Um domínio comum com
        {link('/blog/como-funciona-projeto-de-seo-para-nichos-competitivos/', 'cobertura de tema e autoridade construída')}
        ranqueia. Gastar o orçamento inteiro no domínio e não sobrar para o projeto é o pior dos cenários.</p>

        <h2>Uma regra de proporção</h2>

        <p>Se o custo do domínio consumir uma fatia grande do orçamento total do projeto, provavelmente é a
        decisão errada — independentemente de quão bom o domínio pareça. O domínio deve ser uma parte
        pequena do investimento, não o investimento.</p>
    """,
    "faq": [
        ("Domínio premium ajuda no ranqueamento?",
         "Indiretamente, e pouco. Um nome memorável tende a gerar mais buscas pela marca e mais menções "
         "espontâneas ao longo do tempo, o que ajuda. Mas não existe vantagem direta de ranqueamento por "
         "o nome ser curto ou conter um termo do setor."),
        ("Domínio com a palavra-chave no nome ainda funciona?",
         "O peso desse fator caiu muito e hoje é pequeno. Pode ajudar marginalmente na percepção do "
         "usuário na página de resultados, mas escolher um nome ruim só para encaixar um termo costuma "
         "custar mais em marca do que rende em busca."),
        ("Posso trocar de domínio depois se escolher errado?",
         "Pode, mas toda troca tem custo e risco. É melhor decidir bem no começo do que planejar uma "
         "migração futura — veja como funciona uma migração de domínio."),
    ],
    "cta": ("Está decidindo entre candidatos? Na análise do projeto eu avalio nome, histórico, perfil de "
            "links e risco de cada opção — e digo qual faz sentido para o seu caso, incluindo quando a "
            "resposta é um domínio novo comum.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 14
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-analisar-historico-de-dominio-expirado",
    "h1": "Como analisar o histórico de um domínio expirado",
    "title": "Como analisar o histórico de um domínio expirado | RCB",
    "desc": ("O passo a passo de verificação antes de comprar: histórico de conteúdo, perfil de "
             "links, âncoras, relevância temática e reputação do nome."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/analise-de-dominios-expirados/", "Domínios expirados"),
    "corpo": f"""
        <p>A análise de um domínio candidato é um processo de eliminação. A maior parte dos candidatos cai
        nos dois primeiros passos — o que torna viável avaliar vários sem gastar horas em cada um.</p>

        {caixa('<p><strong>Antes de começar:</strong> defina o que você espera do domínio. Se a expectativa '
               'é herdar autoridade automaticamente, nenhuma análise vai satisfazer, porque isso não '
               'acontece. O objetivo realista é encontrar um domínio cujo passado <em>não atrapalhe</em> e '
               'que, com sorte, <em>ajude um pouco</em>.</p>')}

        <h2>Passo 1 — Histórico de conteúdo</h2>

        <p>Use um serviço público de arquivo da web e percorra a linha do tempo do domínio, ano a ano.
        Você está procurando:</p>

        <ul>
          <li><strong>Qual era o tema.</strong> Tem relação com o que você vai publicar?</li>
          <li><strong>Mudanças bruscas.</strong> Um site de negócio local que vira portal em outro idioma
          é o padrão clássico de domínio capturado.</li>
          <li><strong>Períodos de conteúdo automático.</strong> Texto sem sentido, listas de links, páginas
          repetidas.</li>
          <li><strong>Buracos longos.</strong> Anos sem nada indica abandono, o que dilui o valor do histórico.</li>
        </ul>

        <p>Esse passo elimina a maioria dos candidatos problemáticos e leva poucos minutos.</p>

        <h2>Passo 2 — Distribuição de âncoras</h2>

        <p>É o segundo filtro mais eficiente. Olhe os textos usados nos links que apontam para o domínio:</p>

        <p>Perfil natural é bagunçado — mistura nome da marca, endereço do site, expressões como "clique
        aqui", títulos de artigos e variações. Perfil fabricado é uniforme: o mesmo termo comercial
        repetido em grande proporção dos links.</p>

        <p>Concentração alta em termo comercial é motivo para descartar, porque indica que o perfil foi
        construído para manipular ranqueamento — e você herdaria esse padrão.</p>

        <h2>Passo 3 — Origem dos links</h2>

        <p>Agora vale olhar de onde vêm as referências. Abra dez domínios ao acaso e verifique:</p>

        {tabela(
            ["Verificação", "Bom sinal", "Mau sinal"],
            [
                ["O site tem conteúdo real?", "artigos com autoria e data", "texto genérico ou fora do ar"],
                ["Tem audiência própria?", "tráfego e menções", "nenhuma presença"],
                ["Linha editorial coerente?", "assuntos relacionados entre si", "todos os nichos ao mesmo tempo"],
                ["Para onde mais aponta?", "poucos links de saída, contextuais", "muitos links comerciais"],
                ["Contexto do link", "dentro de conteúdo relevante", "rodapé, lista, texto criado para o link"],
            ],
            nota="Se poucos dos dez passarem, o perfil não sustenta o preço pedido."
        )}

        <h2>Passo 4 — Relevância temática</h2>

        <p>Este é o passo que separa "domínio limpo" de "domínio útil". Um domínio pode ter histórico
        impecável e ainda assim não entregar nada, se o tema anterior não tem relação com o seu.</p>

        <p>Pergunta objetiva: <em>um leitor que chegasse ao domínio pelo conteúdo antigo teria interesse
        no conteúdo novo?</em> Se a resposta for não, o histórico vale pouco.</p>

        <h2>Passo 5 — Reputação e situação atual</h2>

        <ul>
          <li>Pesquise o nome do domínio entre aspas e veja o que aparece.</li>
          <li>Verifique se ainda há páginas indexadas — e se elas são problemáticas.</li>
          <li>Confirme que o nome não reproduz marca registrada de terceiros. Isso é questão jurídica, e
          nenhum ganho de SEO compensa.</li>
        </ul>

        <h2>Passo 6 — A decisão</h2>

        <p>Reúna tudo e responda três perguntas:</p>

        <ol>
          <li><strong>Há algum sinal grave?</strong> Se sim, descarte. Preço não compensa passivo.</li>
          <li><strong>Há relevância temática real?</strong> Se não, o domínio equivale a um domínio novo —
          e deve custar como um.</li>
          <li><strong>O preço é menor que o custo de construir autoridade equivalente?</strong> Se não,
          não compensa.</li>
        </ol>

        <p>A recomendação que sai daí tem três formas possíveis: comprar, não comprar, ou comprar até
        determinado valor. Qualquer conclusão sem um teto de preço está incompleta.</p>

        <p>Se você tem mais de um candidato aprovado e precisa decidir entre eles, os critérios de
        comparação estão em
        {link('/blog/como-escolher-dominio-expirado-com-autoridade/', 'como escolher um domínio expirado com autoridade')}.</p>

        <h2>Erros comuns nessa análise</h2>

        <ul>
          <li>Confiar na métrica de autoridade exibida no anúncio como se fosse dado do Google.</li>
          <li>Olhar só o número total de backlinks, e não quantos domínios distintos existem.</li>
          <li>Ignorar relevância temática porque o perfil "parece bom".</li>
          <li>Se convencer de que um sinal ruim é aceitável porque o preço está atraente.</li>
        </ul>
    """,
    "faq": [
        ("Quanto tempo leva para analisar um domínio?",
         "Uma triagem rápida leva poucos minutos e descarta a maioria. Uma análise completa, com "
         "verificação de origem dos links e relevância temática, leva bem mais — por isso a ordem de "
         "eliminação importa."),
        ("Preciso de ferramenta paga?",
         "Os dois filtros mais eficientes — histórico de conteúdo e reputação do nome — usam fontes "
         "públicas gratuitas. Para analisar perfil de links e âncoras com profundidade, uma ferramenta "
         "de backlinks facilita bastante."),
        ("Vale analisar um domínio que já comprei?",
         "Vale, com outro objetivo: em vez de decidir a compra, medir o que veio junto. A partir daí se "
         "decide entre desautorizar links problemáticos, diluir o perfil com aquisição de qualidade ou, "
         "em casos graves, avaliar troca de domínio."),
    ],
    "cta": ("Quer essa análise feita por quem faz isso com frequência? Na análise do projeto eu verifico "
            "histórico, perfil de links, âncoras, relevância e reputação — e devolvo recomendação com teto "
            "de preço.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 12
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-migrar-site-para-outro-dominio",
    "h1": "Como migrar um site para outro domínio",
    "title": "Como migrar um site para outro domínio sem quebrar | RCB",
    "desc": ("O processo completo de migração de domínio: inventário, mapa de redirecionamento, "
             "virada e monitoramento — com os erros que mais causam perda."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/migracao-de-dominio-seo/", "Migração de domínio"),
    "corpo": f"""
        <p>Migração de domínio é um dos poucos procedimentos de SEO em que a diferença entre fazer bem e
        fazer mal aparece em dias — e em que o erro é difícil de desfazer.</p>

        {caixa('<p><strong>Antes de começar:</strong> toda migração tem impacto. O objetivo de um processo '
               'bem-feito não é evitar oscilação — é reduzir a perda e encurtar o tempo de recuperação. '
               'Quem promete migração sem nenhum efeito não está sendo honesto.</p>')}

        <h2>Etapa 1 — Inventário completo</h2>

        <p>Nada começa antes disso. É preciso ter a lista de <strong>todos</strong> os endereços do site
        atual, não só os que você lembra:</p>

        <ul>
          <li>Todas as páginas publicadas, incluindo as antigas que ninguém acessa há meses.</li>
          <li>Quais delas ranqueiam e para quais termos.</li>
          <li>Quais recebem links de sites externos — essas são as mais críticas.</li>
          <li>Quais recebem tráfego, mesmo que pouco.</li>
          <li>Arquivos que também têm endereço próprio: imagens importantes, documentos.</li>
        </ul>

        <p>Migração sem inventário é migração no escuro. Páginas esquecidas que ainda ranqueavam ou
        recebiam links simplesmente desaparecem — e o efeito só aparece semanas depois.</p>

        <h2>Etapa 2 — Mapa de destino, um a um</h2>

        <p>Para cada endereço antigo, defina o endereço novo equivalente. Um para um, sempre que houver
        equivalente.</p>

        <p><strong>O erro mais destrutivo desta etapa</strong> é redirecionar tudo para a página inicial.
        É rápido de configurar e joga fora o histórico de cada página individualmente — o conteúdo que
        ranqueava aponta para algo que não responde à mesma busca.</p>

        <p>Quando não existe equivalente exato, escolha a página mais próxima em assunto. Quando não existe
        nada próximo, é melhor deixar o endereço retornar erro do que mandar o visitante para um lugar
        irrelevante.</p>

        <h2>Etapa 3 — Preparar o destino antes de virar</h2>

        <p>O site novo precisa estar pronto e conferido <em>antes</em> da virada:</p>

        <ul>
          <li>Conteúdo publicado e completo, não pela metade.</li>
          <li>Estrutura de links internos apontando para os endereços novos.</li>
          <li>Certificado de segurança funcionando.</li>
          <li>Desempenho verificado.</li>
          <li>Configuração de idioma e região.</li>
          <li>Medição instalada, para conseguir comparar depois.</li>
        </ul>

        <h2>Etapa 4 — A virada</h2>

        <p>Na ordem:</p>

        <ol>
          <li>Ativar os redirecionamentos permanentes do domínio antigo para o novo, conforme o mapa.</li>
          <li>Ajustar o apontamento de DNS.</li>
          <li>Confirmar que o certificado do domínio novo está ativo.</li>
          <li>Enviar o sitemap novo nas ferramentas de webmaster.</li>
          <li>Registrar a mudança de endereço, onde a ferramenta oferecer essa opção.</li>
          <li>Manter a propriedade do domínio antigo cadastrada para acompanhar o que ainda chega nele.</li>
        </ol>

        <p><strong>Não desligue o domínio antigo.</strong> Os redirecionamentos precisam continuar
        funcionando por bastante tempo — não semanas. Enquanto houver links externos apontando para ele,
        ele tem função.</p>

        <p>Esse ponto é o que separa uma migração planejada de uma perda de domínio. Se o seu caso for
        o segundo — o registro venceu, o site saiu do ar —, o diagnóstico está em
        {link('/blog/dominio-caiu-o-que-fazer/', 'domínio caiu: o que fazer com o site e o SEO')}.</p>

        <h2>Etapa 5 — Atualização externa</h2>

        <p>Redirecionamento resolve, mas link direto para o endereço novo resolve melhor. Vale entrar em
        contato com os veículos que mais importam para atualizar o endereço, além de ajustar:</p>

        <ul>
          <li>perfis em redes sociais e diretórios;</li>
          <li>assinatura de e-mail e materiais próprios;</li>
          <li>anúncios ativos;</li>
          <li>qualquer integração que aponte para o endereço antigo.</li>
        </ul>

        <h2>Etapa 6 — Monitoramento</h2>

        <p>É onde a maioria falha, porque relaxa cedo demais. Acompanhe semanalmente:</p>

        {tabela(
            ["O que observar", "Sinal de problema"],
            [
                ["Erros de rastreamento", "aumento de páginas não encontradas"],
                ["Indexação do domínio novo", "páginas entrando devagar demais ou não entrando"],
                ["Posições por termo", "queda que não se recupera após algumas semanas"],
                ["Tráfego por página", "páginas específicas que zeraram"],
                ["Redirecionamentos", "cadeias longas ou loops"],
            ],
            nota="Problemas de migração aparecem ao longo de semanas, conforme o rastreamento avança."
        )}

        <h2>Os erros que mais causam perda</h2>

        <ol>
          <li>Redirecionar tudo para a página inicial.</li>
          <li>Esquecer endereços antigos que ainda tinham valor.</li>
          <li>Desligar o domínio antigo cedo demais.</li>
          <li>Trocar domínio e reestruturar o site ao mesmo tempo — duas mudanças grandes juntas impedem
          saber o que causou o quê.</li>
          <li>Publicar o destino com conteúdo incompleto.</li>
          <li>Parar de monitorar na primeira semana boa.</li>
        </ol>

        <p>Se a sua migração já aconteceu e o tráfego caiu, vários desses erros são corrigíveis — o caminho
        é {link('/recuperacao-de-trafego-organico/', 'diagnóstico e recuperação')}.</p>
    """,
    "faq": [
        ("Quanto tempo leva para estabilizar depois da migração?",
         "Varia com o tamanho do site e a frequência de rastreamento. Sites pequenos costumam estabilizar "
         "mais rápido; sites grandes levam mais tempo, porque cada endereço precisa ser rastreado "
         "novamente. Não há prazo garantido."),
        ("Por quanto tempo preciso manter o domínio antigo?",
         "O máximo que for viável. Enquanto existirem links externos apontando para ele, os "
         "redirecionamentos continuam tendo função. Desligar cedo joga fora parte do que a migração "
         "tentou preservar."),
        ("Posso migrar e mudar a estrutura de páginas ao mesmo tempo?",
         "Tecnicamente sim, mas dificulta muito o diagnóstico se algo der errado — você não saberá se o "
         "problema foi o domínio ou a estrutura. Quando o prazo permite, separar em duas etapas é mais seguro."),
        ("A autoridade do domínio antigo passa para o novo?",
         "Parte tende a ser reconhecida através dos redirecionamentos, mas não é transferência automática "
         "nem integral. Tratar migração como mudança de endereço sem perda é o que gera as piores surpresas."),
    ],
    "cta": ("Vai migrar e quer reduzir o risco? Na análise do projeto eu monto o inventário, o mapa de "
            "redirecionamento e a sequência de virada — com o que precisa estar pronto antes de qualquer "
            "coisa ir ao ar.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 43
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "trocar-de-dominio-faz-perder-posicoes",
    "h1": "Trocar de domínio faz perder posições?",
    "title": "Trocar de domínio faz perder posições no Google? | RCB",
    "desc": ("O que realmente acontece com o ranqueamento em uma troca de domínio, quanto costuma "
             "durar a oscilação e o que separa perda temporária de perda permanente."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/migracao-de-dominio-seo/", "Migração de domínio"),
    "corpo": f"""
        <p>Sim, costuma haver perda. A questão relevante é se ela será temporária e pequena ou permanente
        e grande — e isso depende quase inteiramente do processo.</p>

        {caixa('<p><strong>Resposta direta:</strong> praticamente toda troca de domínio gera oscilação de '
               'posições. Com inventário completo e redirecionamento correto, ela tende a ser temporária e '
               'o site recupera. Com redirecionamento malfeito ou endereços esquecidos, a perda pode não se '
               'recuperar — porque o histórico daquelas páginas se perdeu.</p>')}

        <h2>Por que a perda acontece mesmo quando tudo está certo</h2>

        <p>Três motivos técnicos:</p>

        <p><strong>Reavaliação.</strong> O domínio novo precisa ser rastreado e avaliado. Isso leva tempo,
        e durante esse período há incerteza sobre onde cada página deve ficar.</p>

        <p><strong>Sinais que não migram.</strong> Parte do que sustentava a posição do domínio antigo
        estava ligada ao próprio domínio — não só às páginas. Isso não se transfere integralmente.</p>

        <p><strong>Velocidade de rastreamento.</strong> Sites grandes têm milhares de endereços para serem
        rastreados de novo. Enquanto isso não acontece, parte do site fica em situação indefinida.</p>

        <h2>O que separa perda temporária de perda permanente</h2>

        {tabela(
            ["Fator", "Perda temporária", "Perda permanente"],
            [
                ["Redirecionamento", "um a um, por equivalência", "tudo para a página inicial"],
                ["Inventário", "completo, incluindo páginas antigas", "só as páginas lembradas"],
                ["Domínio antigo", "mantido ativo por muito tempo", "desligado cedo"],
                ["Conteúdo no destino", "igual ou melhor", "reduzido ou incompleto"],
                ["Mudanças simultâneas", "só o domínio", "domínio + estrutura + conteúdo"],
                ["Monitoramento", "semanal, com correção rápida", "abandonado após dias"],
            ],
            nota="A coluna da direita descreve as causas mais comuns de queda que não se recupera."
        )}

        <h2>Quanto tempo dura</h2>

        <p>Não existe prazo garantido, e desconfie de quem der um número exato. O que se observa na prática:
        sites menores tendem a estabilizar mais rápido, sites grandes levam mais tempo, e o processo é
        gradual — não há um dia em que tudo volta.</p>

        <p>A mecânica por trás disso — o que exatamente é reavaliado e o que atravessa pelos
        redirecionamentos — está em
        {link('/blog/o-que-acontece-com-seo-ao-trocar-dominio/', 'o que acontece com o SEO quando o domínio é trocado')}.</p>

        <p>O acompanhamento correto olha a curva, não um ponto. Uma queda seguida de recuperação parcial
        e progressiva é o comportamento esperado. Uma queda que não se move depois de bastante tempo indica
        problema técnico, não paciência insuficiente.</p>

        <h2>Como reduzir a perda</h2>

        <ol>
          <li><strong>Inventário completo antes de qualquer coisa.</strong> É a etapa que mais protege.</li>
          <li><strong>Mapa de redirecionamento um a um.</strong> Cada endereço antigo para o equivalente.</li>
          <li><strong>Destino pronto antes da virada.</strong> Conteúdo completo, links internos corretos.</li>
          <li><strong>Domínio antigo mantido.</strong> Redirecionamentos funcionando por muito tempo.</li>
          <li><strong>Uma mudança de cada vez.</strong> Não troque domínio e reestruture o site juntos.</li>
          <li><strong>Atualização das fontes de links mais relevantes.</strong> Link direto rende mais que
          redirecionado.</li>
          <li><strong>Monitoramento semanal.</strong> Problemas aparecem ao longo de semanas.</li>
        </ol>

        <p>O processo completo está em
        {link('/blog/como-migrar-site-para-outro-dominio/', 'como migrar um site para outro domínio')}.</p>

        <h2>Quando a troca vale a pena mesmo com o risco</h2>

        <p>Migração nunca é gratuita, então precisa ter motivo:</p>

        <ul>
          <li>Mudança de marca — o domínio antigo deixou de fazer sentido.</li>
          <li>Consolidação — dois ou mais sites disputando os mesmos termos rendem menos que um.</li>
          <li>Domínio comprometido, com passivo que não compensa limpar.</li>
          <li>Nome que atrapalha comercialmente — difícil de falar, de escrever ou de lembrar.</li>
        </ul>

        <p>O que <strong>não</strong> justifica: a expectativa de que um domínio novo vai ranquear melhor
        por ser mais bonito ou por conter um termo do setor. Esse ganho não existe em escala que compense
        o risco.</p>

        <h2>Se a queda já aconteceu</h2>

        <p>Queda após migração é um dos cenários mais recuperáveis, porque a causa costuma ser concreta:
        redirecionamento faltando, apontando para o lugar errado, ou endereço esquecido. Comparar o
        inventário antigo com o novo normalmente encontra o problema — e o
        {link('/recuperacao-de-trafego-organico/', 'diagnóstico de queda')} começa exatamente por aí.</p>
    """,
    "faq": [
        ("Dá para trocar de domínio sem perder nada?",
         "Não é realista prometer isso. O que um processo bem-feito faz é reduzir a perda e encurtar a "
         "recuperação. Quem garante troca sem impacto está vendendo o que não controla."),
        ("E se eu perdi o registro do domínio para outra pessoa?",
         "Aí não é migração, é reconstrução. Sem acesso ao domínio antigo não há como criar "
         "redirecionamentos, então o caminho é recuperar o conteúdo, publicar em um novo endereço e "
         "refazer o contato com as fontes de links mais relevantes."),
        ("Vale trocar de domínio só para melhorar o nome?",
         "Só se o nome atual estiver realmente prejudicando — difícil de falar, de escrever, ou associado "
         "a algo indesejado. Trocar por preferência estética raramente compensa o risco."),
    ],
    "cta": ("Vai trocar de domínio ou já trocou e perdeu posição? Na análise do projeto eu avalio o "
            "cenário, monto o plano de virada ou identifico o que quebrou na migração já feita.",
            ANALISE, "Solicitar análise do projeto"),
})


# ------------------------------------------------------------------
# 44
# ------------------------------------------------------------------
ARTIGOS.append({
    "slug": "como-recuperar-trafego-organico-apos-queda",
    "h1": "Como recuperar tráfego orgânico após uma queda",
    "title": "Como recuperar tráfego orgânico após uma queda | RCB",
    "desc": ("O diagnóstico diferencial de uma queda de tráfego: como identificar a causa antes de "
             "mexer no site e por que a pressa costuma atrasar a recuperação."),
    "cat": CAT,
    "data": DATA,
    "trilha_extra": ("/recuperacao-de-trafego-organico/", "Recuperação de tráfego"),
    "corpo": f"""
        <p>A reação natural a uma queda é começar a mudar coisas. É também o que mais atrasa a recuperação.</p>

        {caixa('<p><strong>Antes de qualquer coisa:</strong> congele as alterações no site. Cada mudança '
               'feita antes do diagnóstico apaga pistas, introduz variáveis novas e pode remover o que '
               'estava funcionando. A sequência correta é levantar dados, formar hipótese, testar a mais '
               'provável e medir — nessa ordem.</p>')}

        <h2>Passo 1 — Determinar a data exata</h2>

        <p>É a informação mais valiosa de todo o diagnóstico, porque é ela que separa as hipóteses.</p>

        <p>Uma queda que acontece em poucos dias aponta para causas diferentes de uma queda que se
        desenvolve ao longo de meses. Uma queda que coincide com uma alteração no site aponta para o que
        foi alterado. Uma queda que coincide com uma atualização de algoritmo aponta para outro caminho.</p>

        <p>Levante: quando começou, quanto caiu, quais páginas foram atingidas e quais termos perderam
        posição. Se a queda foi em algumas páginas e não em todas, isso já elimina várias hipóteses.</p>

        <h2>Passo 2 — Descartar o que não é problema</h2>

        <p>Nem toda queda é um defeito. Antes de investigar, verifique:</p>

        <ul>
          <li><strong>Sazonalidade.</strong> Compare com o mesmo período do ano anterior, não com o mês passado.</li>
          <li><strong>Fim de um pico.</strong> Um conteúdo que bombou por um evento sempre volta ao normal.</li>
          <li><strong>Mudança no formato da busca.</strong> Se o Google passou a responder aquela pergunta
          direto na página de resultados, o clique cai mesmo mantendo a posição.</li>
          <li><strong>Problema de medição.</strong> Vale conferir se o código de análise continua instalado
          e funcionando — quedas "impossíveis" às vezes são isso.</li>
        </ul>

        <h2>Passo 3 — Diagnóstico diferencial</h2>

        {tabela(
            ["Causa", "Como a queda se comporta", "Onde confirmar"],
            [
                ["Atualização de algoritmo", "poucos dias, atingindo um padrão de conteúdo", "data × janela da atualização"],
                ["Migração malfeita", "logo após troca de domínio ou plataforma", "inventário e redirecionamentos"],
                ["Problema técnico", "abrupta, às vezes só em parte do site", "indexação e erros de rastreamento"],
                ["Perda de links", "gradual, em páginas específicas", "evolução dos domínios de referência"],
                ["Publicação em massa", "lenta e generalizada", "histórico de publicação × curva"],
                ["Concorrência", "gradual, termo a termo", "quem passou a ocupar as posições"],
                ["Bloqueio acidental", "abrupta e total", "arquivo de robots e meta de indexação"],
            ],
            nota="Mais de uma causa ao mesmo tempo é o cenário mais comum — o que muda é a ordem de ataque."
        )}

        <h2>Passo 4 — Verificar o básico antes do complexo</h2>

        <p>Uma parcela relevante das quedas tem causa banal. Antes de teorizar sobre algoritmo, confirme:</p>

        <ol>
          <li>O site está acessível e não está bloqueando rastreamento por engano.</li>
          <li>As páginas importantes continuam indexadas.</li>
          <li>Não há meta de não indexação aplicada por acidente — acontece com frequência depois de
          publicar uma versão de teste.</li>
          <li>O certificado de segurança está válido.</li>
          <li>O site não ficou fora do ar por um período longo.</li>
          <li>Nenhum redirecionamento novo está quebrando páginas.</li>
        </ol>

        <p>Esses itens custam minutos para verificar e explicam mais quedas do que se imagina.</p>

        <h2>Passo 5 — Agir na causa mais provável, uma de cada vez</h2>

        <p>A tentação é corrigir tudo simultaneamente. O problema é que, se o tráfego voltar, você não vai
        saber o que funcionou — e não vai poder repetir da próxima vez.</p>

        <p>Priorize por impacto estimado e esforço. Aplique uma correção, meça, depois avance para a
        seguinte. É mais lento no papel e mais rápido no resultado.</p>

        <h2>O que esperar de cada cenário</h2>

        <p><strong>Queda técnica ou de migração.</strong> A mais recuperável. Há algo concreto quebrado,
        o conserto é objetivo e o efeito tende a aparecer em semanas.</p>

        <p><strong>Queda por qualidade ou autoridade.</strong> Exige trabalho de fundo — revisar e
        consolidar conteúdo, retomar {link('/link-building-para-nichos-competitivos/', 'construção de autoridade')}.
        Horizonte de meses.</p>

        <p><strong>Queda por concorrência.</strong> Não é um defeito a corrigir, é uma disputa a retomar. O
        caminho é o de um {link('/seo-para-nichos-competitivos/', 'projeto em nicho competitivo')}.</p>

        <p><strong>Queda por mudança de formato da busca.</strong> Às vezes o patamar anterior não volta,
        porque o clique deixou de existir. Aqui o trabalho honesto é redefinir o alvo, não perseguir um
        número que não está mais disponível.</p>

        <h2>O que não fazer</h2>

        <ul>
          <li>Desautorizar links em massa por precaução — pode remover o que estava ajudando.</li>
          <li>Reescrever páginas que ainda ranqueavam bem.</li>
          <li>Publicar muito conteúdo novo achando que compensa a perda.</li>
          <li>Trocar de domínio para "recomeçar limpo" sem entender a causa.</li>
          <li>Fazer vinte alterações e esperar para ver.</li>
        </ul>
    """,
    "faq": [
        ("Quanto tempo leva para recuperar?",
         "Depende da causa. Correções técnicas podem mostrar efeito em semanas. Recuperação por qualidade "
         "ou autoridade leva meses e depende de execução contínua. E há casos em que o patamar anterior não "
         "volta, porque o que mudou foi o mercado ou o formato do resultado."),
        ("Perdi tráfego depois de uma atualização do Google. Devo esperar a próxima?",
         "Esperar sozinho raramente resolve. Atualizações costumam atingir um padrão específico de conteúdo "
         "ou de perfil — identificar qual padrão foi atingido e trabalhar nele é o que muda o resultado."),
        ("Vale a pena recomeçar em outro domínio?",
         "Quase nunca. Isso descarta todo o histórico acumulado e recria do zero um problema que "
         "provavelmente é corrigível. Só faz sentido em casos extremos de domínio comprometido, e depois "
         "de um diagnóstico que confirme isso."),
        ("Como saber se a queda é grave?",
         "Compare a proporção e o alcance: queda pequena e distribuída costuma ser oscilação normal; queda "
         "grande e concentrada em um tipo de página indica causa específica. E compare com o mesmo período "
         "do ano anterior, não com o mês anterior."),
    ],
    "cta": ("Seu tráfego caiu e você não sabe por quê? Na análise do projeto eu reconstruo a linha do tempo "
            "da queda e aponto a causa mais provável — antes de qualquer alteração no site, para não apagar "
            "as pistas.",
            ANALISE, "Solicitar análise do projeto"),
})
