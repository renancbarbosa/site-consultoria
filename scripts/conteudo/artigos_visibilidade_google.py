# -*- coding: utf-8 -*-
"""Artigos de intenção leiga sobre presença e divulgação no Google."""
from rcb_artigo import caixa, tabela, link

DATA = "2026-08-15"


ARTIGOS = [
    {
        "slug": "como-colocar-minha-empresa-no-google",
        "h1": "Como colocar minha empresa no Google: passo a passo",
        "title": "Como colocar minha empresa no Google: passo a passo | RCB",
        "desc": ("Como colocar sua empresa no Google de graça: veja como criar ou reivindicar o perfil, "
                 "verificar o negócio e aparecer na Busca e no Maps."),
        "cat": "Google Perfil da Empresa",
        "data": DATA,
        "imagem": {
            "src": "/assets/img/blog/como-colocar-minha-empresa-no-google.svg",
            "alt": "Fluxo para colocar uma empresa no Google: pesquisar a ficha, criar ou reivindicar, verificar e completar o perfil",
            "width": 1200,
            "height": 675,
            "legenda": "O cadastro termina quando a ficha está verificada e completa; posicionamento vem na etapa seguinte.",
        },
        "trilha_extra": ("/como-aparecer-no-google/", "Aparecer no Google"),
        "corpo": f"""
        <p>Para colocar uma empresa no Google, você precisa criar ou reivindicar o <strong>Google Perfil da
        Empresa</strong>, preencher os dados reais do negócio e concluir a verificação solicitada. O cadastro
        é gratuito e permite que a empresa seja encontrada na Busca e no Google Maps.</p>

        {caixa('<p><strong>Resposta rápida:</strong> primeiro pesquise o nome da empresa no Google Maps para '
               'ver se já existe uma ficha. Se existir, reivindique-a; se não existir, crie um novo perfil. '
               'Depois informe categoria, telefone, site, endereço ou área atendida e faça a verificação. '
               'Evite criar uma segunda ficha para o mesmo negócio.</p>')}

        <p>Eu separo cadastro de posicionamento porque os números mostram essa diferença. Em um projeto local
        documentado pela RCB, o perfil acumulou <strong>1.969 visualizações e 252 solicitações de rota</strong>
        no período analisado. O ganho não veio de abrir outra ficha, mas de organizar a ficha correta e
        acompanhar o que o cliente fazia depois de encontrá-la. Os registros e as capturas estão na
        {link('/cases/#case-docevidade', 'página de cases da RCB')}.</p>

        <p>Este guia trata do <strong>cadastro inicial</strong>. Se a sua empresa já tem perfil verificado,
        mas aparece pouco, vá para o checklist de {link('/blog/como-otimizar-google-perfil-empresa/', 'como otimizar o Google Perfil da Empresa')}. E, se a dúvida envolve perfil, site e avaliações ao
        mesmo tempo, veja o {link('/como-aparecer-no-google/', 'guia completo para aparecer no Google')}.</p>

        <h2>Antes de começar: sua empresa pode ter um perfil?</h2>

        <p>O Google Perfil da Empresa foi feito para negócios que mantêm contato presencial com clientes.
        Isso inclui lojas e escritórios com endereço aberto ao público, profissionais que visitam o cliente
        e empresas de área de cobertura, como eletricistas, instaladores e serviços de entrega local.</p>

        <p>Negócios exclusivamente online, marcas sem atendimento presencial e endereços usados apenas para
        receber correspondência não se enquadram da mesma forma. Antes de cadastrar, confira as
        <a class="artigo-link" href="https://support.google.com/business/answer/3038177?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">diretrizes oficiais de qualificação do Google</a>. Essa
        checagem reduz o risco de criar um perfil que depois seja suspenso.</p>

        <h2>Separe estas informações</h2>

        <ul>
          <li><strong>nome real da empresa</strong>, igual ao usado na fachada, no site e nos documentos;</li>
          <li><strong>categoria principal</strong> que melhor descreve o serviço central;</li>
          <li><strong>endereço</strong> ou cidades e bairros atendidos, conforme o modelo do negócio;</li>
          <li><strong>telefone, site e horário</strong> atualizados;</li>
          <li><strong>fotos reais</strong> do local, equipe, produtos ou execução do serviço;</li>
          <li>acesso ao e-mail que ficará responsável pelo perfil.</li>
        </ul>

        <p>Nome, endereço e telefone devem ser consistentes em todos os canais. Não invente complemento no
        nome para encaixar palavras-chave. Se a marca é “Clínica Exemplo”, cadastre “Clínica Exemplo”, e não
        “Clínica Exemplo Melhor Dentista em Goiânia”.</p>

        <h2>Como colocar sua empresa no Google em 7 passos</h2>

        <h3>1. Pesquise a empresa antes de criar</h3>

        <p>Abra o Google Maps e procure pelo nome, telefone e endereço. Um cliente, um antigo funcionário ou
        o próprio Google pode ter criado uma ficha automaticamente. Encontrou uma ficha correta? Use a opção
        para reivindicar a propriedade. Criar outra ficha divide avaliações, confunde o cliente e pode gerar
        duplicidade.</p>

        <h3>2. Crie ou reivindique o perfil</h3>

        <p>Acesse o fluxo oficial de
        <a class="artigo-link" href="https://support.google.com/business/answer/2911778?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">adicionar ou reivindicar uma empresa</a> com a conta Google
        que ficará responsável pelo cadastro. O próprio Google orientará se você está criando uma nova ficha
        ou solicitando acesso a uma existente.</p>

        <h3>3. Informe o nome e a categoria principal</h3>

        <p>Use o nome real. Depois escolha a categoria que representa a principal fonte de receita, não uma
        categoria ampla apenas porque parece ter mais buscas. Uma clínica odontológica, por exemplo, precisa
        partir da categoria compatível com o atendimento que presta; os serviços específicos entram nos
        campos próprios e nas páginas do site.</p>

        <h3>4. Defina endereço ou área de atendimento</h3>

        <p>Se o cliente vai até o estabelecimento durante o horário informado, cadastre o endereço visitável.
        Se você trabalha no endereço do cliente, configure a área atendida e oculte o endereço residencial.
        Não use caixa postal, escritório virtual sem operação real ou endereço de terceiro só para aparecer
        em outra cidade.</p>

        <h3>5. Adicione telefone, site e horário</h3>

        <p>Use um telefone atendido pela empresa, vincule a página mais útil do site e informe horários que
        você realmente cumpre. Esses dados ajudam o cliente a decidir e também conectam o perfil ao restante
        da presença digital. Se ainda não há site, o perfil pode existir, mas um
        {link('/site-otimizado-para-seo/', 'site preparado para SEO')} amplia as buscas que a empresa consegue
        disputar.</p>

        <h3>6. Conclua a verificação</h3>

        <p>O Google define quais métodos de verificação ficam disponíveis para cada negócio. Pode pedir vídeo,
        telefone, e-mail, correspondência ou outra comprovação. Siga exatamente o método exibido na conta e
        mostre sinais reais da operação. Não existe um atalho legítimo que dispense a comprovação quando ela
        é solicitada.</p>

        <h3>7. Complete o perfil e confira como ele aparece</h3>

        <p>Após a verificação, adicione descrição, serviços, atributos e fotos reais. Pesquise a marca e
        confira telefone, rota, horário e link do site. Faça também um teste no celular: é onde muitos
        clientes verão o perfil pela primeira vez.</p>

        <h2>O que muda depois que o cadastro fica ativo?</h2>

        {tabela(
            ["Situação", "O que significa", "Próximo passo"],
            [
                ["Perfil criado, não verificado", "os dados foram enviados, mas a gestão ainda não foi confirmada", "concluir a verificação pedida"],
                ["Perfil verificado", "a empresa pode gerenciar seus dados na Busca e no Maps", "completar informações e começar a acompanhar"],
                ["Aparece pelo nome, não pelo serviço", "o cadastro existe, mas ainda falta relevância e força local", "otimizar perfil, site e avaliações"],
                ["Perfil suspenso", "o Google identificou possível violação ou precisa de comprovação", "corrigir dados e seguir o recurso oficial"],
            ],
            nota="Ter o perfil ativo não garante as primeiras posições. Cadastro e posicionamento são etapas diferentes."
        )}

        <h2>Colocar no Google não é o mesmo que aparecer em primeiro</h2>

        <p>Ao concluir o cadastro, você torna a empresa elegível para aparecer. A ordem dos resultados locais
        depende principalmente de <strong>relevância, distância e destaque</strong>. Categoria adequada,
        informações completas, avaliações reais, proximidade de quem pesquisa e a força da empresa na web
        influenciam a disputa.</p>

        <p>É por isso que uma ficha recém-criada pode aparecer quando alguém busca o nome da marca, mas não
        aparecer ainda para “dentista perto de mim” ou “eletricista em Goiânia”. Nesse momento, o trabalho
        deixa de ser cadastro e passa a ser {link('/google-perfil-empresa/', 'otimização do Google Perfil da Empresa')}, conteúdo local e reputação.</p>

        <h2>Erros que mais atrasam o processo</h2>

        <ul>
          <li>criar uma ficha nova sem procurar uma já existente;</li>
          <li>encher o nome da empresa com serviço e cidade;</li>
          <li>usar categoria que não representa a atividade principal;</li>
          <li>mostrar endereço residencial quando o negócio atende somente no local do cliente;</li>
          <li>informar telefone ou horário que ninguém consegue atender;</li>
          <li>comprar avaliações ou oferecer recompensa em troca delas;</li>
          <li>entregar a propriedade principal do perfil a uma conta que você não controla.</li>
        </ul>

        <h2>Checklist depois de publicar</h2>

        <ol>
          <li>confira se o perfil está verificado e sem alertas;</li>
          <li>teste telefone, site, rota e horário pelo celular;</li>
          <li>adicione fotos reais e serviços importantes;</li>
          <li>peça avaliações honestas a clientes atendidos e responda todas;</li>
          <li>ligue cada serviço importante a uma página útil do site;</li>
          <li>acompanhe buscas, ligações, rotas e cliques no próprio perfil;</li>
          <li>se ele não aparecer, use o diagnóstico de {link('/blog/google-meu-negocio-nao-aparece/', 'Google Meu Negócio que não aparece')} antes de criar outra ficha.</li>
        </ol>
        """,
        "faq": [
            ("É gratuito colocar minha empresa no Google?",
             "Sim. Criar ou reivindicar um Google Perfil da Empresa é gratuito. Você só paga se decidir anunciar em produtos como o Google Ads ou contratar alguém para configurar e otimizar a presença."),
            ("Preciso ter site para cadastrar a empresa?",
             "Não. O perfil pode ser criado sem site, desde que o negócio seja elegível. Porém, o site ajuda a explicar serviços, gerar confiança e disputar pesquisas orgânicas que não mostram apenas o mapa."),
            ("Posso colocar uma empresa que funciona em casa?",
             "Pode, quando existe atendimento presencial real. Se você vai até o cliente e não o recebe em casa, configure uma empresa de área de atendimento e oculte o endereço residencial."),
            ("Minha empresa já aparece. Devo criar outro perfil?",
             "Não. O mais seguro é reivindicar a ficha existente. Uma duplicata pode dividir avaliações e criar conflitos nos dados."),
            ("Quanto tempo leva para aparecer?",
             "O prazo varia conforme o método de verificação e as análises solicitadas pelo Google. Depois de verificado, o perfil pode aparecer pela marca antes de ganhar posição nas buscas por serviço."),
        ],
        "cta": ("Já existe uma ficha, mas você não sabe se ela está bem configurada? No diagnóstico eu verifico perfil, site, avaliações e os bloqueios que impedem a empresa de ser encontrada.",
                "/diagnostico-presenca-digital/", "Solicitar diagnóstico gratuito"),
    },
    {
        "slug": "como-divulgar-minha-empresa-no-google",
        "h1": "Como divulgar minha empresa no Google",
        "title": "Como divulgar minha empresa no Google: guia prático | RCB",
        "desc": ("Como divulgar sua empresa no Google com Perfil da Empresa, site, SEO e anúncios. "
                 "Compare os canais e siga um plano prático de 30 dias."),
        "cat": "Aparecer no Google",
        "data": DATA,
        "imagem": {
            "src": "/assets/img/blog/como-divulgar-minha-empresa-no-google.svg",
            "alt": "Comparação entre Google Maps, site com SEO e Google Ads para divulgar uma empresa",
            "width": 1200,
            "height": 675,
            "legenda": "Maps, SEO e Ads ocupam espaços diferentes; a melhor combinação depende da intenção e da urgência.",
        },
        "trilha_extra": ("/como-aparecer-no-google/", "Aparecer no Google"),
        "corpo": f"""
        <p>Divulgar uma empresa no Google não significa usar uma ferramenta só. Você pode aparecer no
        <strong>Google Maps</strong> com o Perfil da Empresa, nos resultados orgânicos com um site útil e,
        quando precisa de velocidade, nos espaços pagos com o Google Ads. A melhor estratégia costuma
        combinar essas frentes em momentos diferentes.</p>

        {caixa('<p><strong>Resposta rápida:</strong> comece pelo Google Perfil da Empresa se você atende uma '
               'região, organize um site com uma página para cada serviço importante e use anúncios apenas '
               'com orçamento, página de destino e medição definidos. O perfil e o SEO constroem presença; '
               'o anúncio compra exposição enquanto houver verba.</p>')}

        <p>Em um projeto de site documentado pela RCB, a busca orgânica gerou <strong>686 impressões, 29
        cliques, CTR de 4,2% e posição média 4,1</strong> nos primeiros 30 dias medidos, sem anúncio. É um
        caso específico, não uma promessa de prazo, mas mostra por que o site precisa ser tratado como ativo
        e não como cartão de visita. As consultas e capturas estão no
        {link('/cases/#case-naluprado', 'case da Nalu Prado')}.</p>

        <p>Se você ainda nem cadastrou o negócio, siga primeiro o tutorial de
        {link('/blog/como-colocar-minha-empresa-no-google/', 'como colocar sua empresa no Google')}. Aqui a
        intenção é outra: escolher como promover a empresa depois que a base existe.</p>

        <h2>As 3 formas principais de divulgar uma empresa no Google</h2>

        {tabela(
            ["Canal", "Custo de mídia", "Velocidade", "Melhor uso"],
            [
                ["Google Perfil da Empresa e Maps", "gratuito", "cadastro rápido; posição leva trabalho", "negócio local e busca perto de mim"],
                ["Site e SEO orgânico", "sem custo por clique", "construção gradual", "serviços, dúvidas e procura recorrente"],
                ["Google Ads", "pago por campanha", "pode gerar exposição imediata", "demanda urgente, teste de oferta e escala"],
            ],
            nota="Gratuito não significa sem trabalho, e pago não significa resultado automático. Cada canal precisa de configuração, mensagem e acompanhamento."
        )}

        <h2>1. Divulgue no Google Maps com o Perfil da Empresa</h2>

        <p>Para lojas, clínicas, escritórios e prestadores locais, o perfil é a porta de entrada. Ele pode
        mostrar telefone, horário, rota, fotos, avaliações, serviços e o link do site diretamente na Busca e
        no Maps. O cadastro é gratuito, como confirma a
        <a class="artigo-link" href="https://support.google.com/business/answer/7039811?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">documentação do Google Perfil da Empresa</a>.</p>

        <p>Preencha a categoria principal correta, mantenha dados atualizados e adicione fotos reais. Peça
        avaliações a clientes atendidos sem oferecer recompensa e responda todas com naturalidade. Posts do
        perfil podem comunicar novidades, ofertas e eventos, mas não devem ser tratados como fórmula mágica
        de ranqueamento.</p>

        <p>O objetivo aqui é facilitar a decisão de quem já está procurando algo perto. Veja também
        {link('/blog/como-aparecer-no-google-maps/', 'como aparecer no Google Maps')} e o checklist de
        {link('/blog/como-otimizar-google-perfil-empresa/', 'otimização do perfil')}.</p>

        <h2>2. Use o site para aparecer nas buscas orgânicas</h2>

        <p>O perfil resolve parte da jornada, mas não todas as pesquisas exibem o mapa. Em muitas buscas, o
        Google mostra páginas de serviço, guias, comparativos e respostas. O site permite disputar esses
        espaços e explicar com profundidade por que o cliente deveria escolher a sua empresa.</p>

        <h3>Crie uma página para cada serviço importante</h3>

        <p>Uma home genérica dificilmente responde bem a todas as intenções. Se a empresa oferece implante,
        clareamento e aparelho, por exemplo, cada serviço merece uma página própria com indicação, processo,
        dúvidas, diferenciais e próximo passo. Isso ajuda o Google a entender o assunto e o visitante a
        decidir.</p>

        <h3>Escreva para a dúvida real do cliente</h3>

        <p>Artigos funcionam quando respondem ao que a pessoa pergunta antes de contratar. “Quanto custa?”,
        “como funciona?”, “qual profissional procurar?” e “por que meu problema acontece?” são buscas que
        antecedem a compra. Cada artigo deve levar naturalmente à página do serviço relacionado, sem forçar
        a venda em todos os parágrafos.</p>

        <h3>Cuide da base técnica</h3>

        <p>Título claro, URL simples, conteúdo acessível no celular, carregamento razoável, sitemap e links
        internos ajudam o Google a encontrar e entender as páginas. Ainda assim, o próprio
        <a class="artigo-link" href="https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=pt-br"
        target="_blank" rel="noopener noreferrer">Guia de SEO do Google</a> lembra que não existe garantia
        automática de rastreamento, indexação ou posição.</p>

        <p>Se o site abre pelo endereço, mas não aparece nem quando você pesquisa a marca ou um trecho do
        conteúdo, consulte o diagnóstico de {link('/blog/por-que-meu-site-nao-aparece-no-google/', 'site que não aparece no Google')}.</p>

        <h2>3. Use o Google Ads quando precisa de velocidade</h2>

        <p>No Google Ads, você configura uma campanha, escolhe objetivo e orçamento e paga pela mídia. Entre
        os formatos disponíveis estão campanhas de pesquisa e Performance Max, entre outras opções descritas
        no guia oficial para
        <a class="artigo-link" href="https://support.google.com/google-ads/answer/6324971?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">criar uma campanha no Google Ads</a>.</p>

        <p>Para uma empresa de serviços, a campanha de pesquisa costuma ser o ponto mais fácil de entender:
        o anúncio aparece quando alguém busca termos escolhidos. Mas anunciar uma palavra não basta. O clique
        precisa chegar a uma página que responda exatamente à busca, apresente prova, informe a região
        atendida e facilite o contato.</p>

        <p>Antes de investir, defina:</p>

        <ul>
          <li>qual serviço e região a campanha vai promover;</li>
          <li>quanto pode ser gasto por dia e por mês;</li>
          <li>para qual página cada anúncio será enviado;</li>
          <li>o que conta como conversão: ligação, formulário, WhatsApp ou compra;</li>
          <li>como separar contatos bons de cliques sem intenção.</li>
        </ul>

        <p>Anúncio e SEO não precisam ser rivais. O Ads pode testar rapidamente uma oferta e gerar demanda
        enquanto a presença orgânica amadurece. O SEO reduz a dependência de pagar por cada visita ao longo
        do tempo. Veja a comparação detalhada entre {link('/blog/seo-ou-trafego-pago-empresa-local/', 'SEO e tráfego pago para empresa local')}.</p>

        <h2>Como divulgar sua empresa no Google de graça</h2>

        <p>Sem comprar mídia, você ainda pode construir presença. O custo aparece em tempo, produção e
        manutenção, não em cada clique. A ordem mais eficiente costuma ser:</p>

        <p>Se esse é o seu objetivo principal, use também o roteiro completo de
        {link('/blog/como-aparecer-no-google-sem-pagar/', 'como aparecer no Google sem pagar por anúncios')}.
        Ele separa cadastro gratuito, indexação, páginas de serviço, conteúdo e medição.</p>

        <ol>
          <li>criar ou reivindicar o perfil e concluir a verificação;</li>
          <li>preencher dados, serviços, fotos e horário;</li>
          <li>pedir avaliações reais depois de cada atendimento;</li>
          <li>publicar no site páginas dos serviços com maior valor comercial;</li>
          <li>responder dúvidas que o cliente pesquisa antes de comprar;</li>
          <li>conectar perfil, site, páginas de serviço e artigos com links úteis;</li>
          <li>acompanhar o que gera visualização, clique e contato.</li>
        </ol>

        <p>Evite chamar esse processo de “anunciar de graça”. Você não está comprando espaço publicitário;
        está tornando a empresa mais compreensível, confiável e encontrável nos resultados gratuitos.</p>

        <h2>Um plano simples para os próximos 30 dias</h2>

        {tabela(
            ["Período", "Ação principal", "Entrega concreta"],
            [
                ["Dias 1 a 7", "arrumar a base", "perfil verificado, dados consistentes e canais de contato testados"],
                ["Dias 8 a 14", "organizar a oferta", "lista de serviços prioritários e uma página boa para cada prioridade"],
                ["Dias 15 a 21", "construir confiança", "fotos reais, processo de avaliações e provas no site"],
                ["Dias 22 a 30", "medir e decidir", "Search Console, Analytics e desempenho do perfil revisados; decisão sobre Ads"],
            ]
        )}

        <p>Não é uma promessa de primeira página em 30 dias. É um cronograma para sair da improvisação e
        criar uma base mensurável. Depois desse período, você terá dados para decidir se precisa fortalecer
        conteúdo, corrigir o site, melhorar o perfil ou acelerar com anúncios.</p>

        <h2>Como saber se a divulgação está funcionando</h2>

        <p>Visualização sozinha não paga conta. Acompanhe indicadores ligados à jornada do cliente:</p>

        <ul>
          <li><strong>no Perfil da Empresa:</strong> buscas, ligações, pedidos de rota e cliques no site;</li>
          <li><strong>no Search Console:</strong> consultas, páginas exibidas, cliques e posição média;</li>
          <li><strong>no Analytics:</strong> visitas às páginas importantes e ações de contato;</li>
          <li><strong>no atendimento:</strong> quantidade e qualidade dos leads e vendas originadas do Google.</li>
        </ul>

        <p>O resultado que importa é a sequência completa: a pessoa encontra, entende, confia e entra em
        contato. Por isso perfil, site e WhatsApp precisam funcionar como um sistema, não como peças soltas.</p>

        <h2>Erros que desperdiçam esforço e dinheiro</h2>

        <ul>
          <li>depender apenas do Instagram e deixar o Google sem informação;</li>
          <li>criar um perfil e abandoná-lo com dados errados;</li>
          <li>mandar todos os anúncios para uma home genérica;</li>
          <li>publicar dezenas de artigos sem ligação com os serviços vendidos;</li>
          <li>medir curtidas e visitas, mas não ligações, formulários e vendas;</li>
          <li>esperar que uma única ação resolva cadastro, posição e conversão ao mesmo tempo.</li>
        </ul>

        <p>Se você não sabe qual desses canais está travando, um
        {link('/diagnostico-presenca-digital/', 'diagnóstico de presença digital')} separa o problema de
        cadastro, indexação, posicionamento e conversão antes de investir mais.</p>
        """,
        "faq": [
            ("Dá para divulgar minha empresa no Google de graça?",
             "Sim. O Google Perfil da Empresa e a presença orgânica do site não cobram por clique. Ainda existe custo de tempo, conteúdo, configuração e manutenção, feito internamente ou por um profissional."),
            ("Preciso pagar Google Ads para aparecer?",
             "Não. Anúncios são uma forma paga de ganhar exposição, mas perfil, Maps e resultados orgânicos podem aparecer sem compra de mídia. A posição gratuita depende de relevância, qualidade, contexto local e concorrência."),
            ("É melhor começar pelo perfil, pelo site ou pelo anúncio?",
             "Negócios locais normalmente começam pelo perfil e pela base do site. O anúncio entra quando existe uma oferta clara, uma boa página de destino, orçamento e medição de conversões."),
            ("Preciso ter um site para anunciar no Google?",
             "Muitas campanhas levam o usuário para um site ou página de destino, e isso costuma dar mais controle sobre mensagem e conversão. Algumas configurações podem usar outras superfícies, mas uma página própria e relevante continua sendo uma base importante."),
            ("Quanto tempo demora para a divulgação dar resultado?",
             "Anúncios podem gerar exposição assim que a campanha é aprovada e ativada; perfil e SEO constroem resultado de forma gradual. O prazo varia conforme concorrência, região, qualidade da base e consistência da execução."),
        ],
        "cta": ("Quer saber se o próximo investimento deveria ir para perfil, site, conteúdo ou anúncios? Eu avalio a presença atual e mostro onde está o maior gargalo antes de propor qualquer serviço.",
                "/diagnostico-presenca-digital/", "Solicitar diagnóstico gratuito"),
    },
    {
        "slug": "como-aparecer-nas-buscas-perto-de-mim",
        "h1": "Como aparecer nas buscas “perto de mim” no Google",
        "title": "Como aparecer nas buscas perto de mim no Google | RCB",
        "desc": ("Entenda como aparecer nas buscas perto de mim: ajuste Perfil da Empresa, site, "
                 "localização, serviços e avaliações sem inventar endereço ou cidade."),
        "cat": "SEO local",
        "data": DATA,
        "trilha_extra": ("/como-aparecer-no-google/", "Aparecer no Google"),
        "corpo": f"""
        <p>Para aparecer quando alguém pesquisa <strong>“perto de mim”</strong>, sua empresa precisa deixar
        claro o que faz, onde atende e por que é uma opção confiável naquela região. Não existe um campo
        secreto para preencher com essa frase. O resultado nasce da combinação entre Google Perfil da
        Empresa, localização de quem pesquisa, página do serviço e sinais reais de reputação.</p>

        {caixa('<p><strong>Resposta direta:</strong> verifique o Perfil da Empresa, use a categoria que '
               'representa o serviço principal, mantenha endereço ou área atendida corretos, descreva os '
               'serviços no perfil e no site e conquiste avaliações de clientes reais. O Google explica '
               'que os resultados locais se baseiam principalmente em relevância, distância e destaque. '
               'Não é possível comprar uma posição orgânica melhor no mapa.</p>')}

        <p>Essa divisão não é opinião de mercado. A própria documentação do Google lista
        <a class="artigo-link" href="https://support.google.com/business/answer/7091?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">relevância, distância e destaque como os principais fatores locais</a>
        e informa que não há como solicitar ou pagar por uma classificação local orgânica melhor.</p>

        <p>A expressão muda — “aberto perto de mim”, “empresa próxima”, “serviço aqui perto” —, mas a
        intenção costuma ser a mesma: a pessoa quer resolver algo agora e prefere uma opção que faça
        sentido para a localização dela. É uma busca mais próxima da decisão do que uma pesquisa ampla
        sobre o assunto.</p>

        <p>Este guia trata dessa intenção. Se o seu perfil ainda nem foi criado ou verificado, comece pelo
        passo a passo de {link('/blog/como-colocar-minha-empresa-no-google/', 'como colocar sua empresa no Google')}.
        Se a dúvida é sobre a ficha aparecer no mapa, veja também {link('/blog/como-aparecer-no-google-maps/', 'como aparecer no Google Maps')}.</p>

        <h2>O que o Google entende por “perto”</h2>

        <p>“Perto” não é uma distância fixa igual para todos os negócios. O Google considera a posição da
        pessoa ou, quando ela não compartilha a localização, as informações disponíveis sobre onde ela
        está. O raio aceitável também muda conforme o serviço. É comum alguém atravessar a cidade para uma
        consulta especializada; para comprar pão, a expectativa de proximidade costuma ser outra.</p>

        <p>Isso explica por que duas pessoas podem fazer a mesma busca e ver empresas diferentes. Também
        explica por que testar apenas do computador do estabelecimento dá uma leitura incompleta. Você
        precisa observar bairros e pontos reais da área atendida, sem concluir que uma posição vista em um
        endereço representa a cidade inteira.</p>

        {tabela(
            ["Sinal", "O que ele ajuda o Google a entender", "Como trabalhar"],
            [
                ["Categoria principal", "qual é o negócio central", "escolher a categoria mais específica e verdadeira"],
                ["Endereço ou área de serviço", "onde existe atendimento real", "manter os dados corretos e dentro das regras"],
                ["Serviços e páginas", "para quais necessidades a empresa é relevante", "descrever cada serviço importante com clareza"],
                ["Avaliações", "experiência e destaque percebido", "pedir opiniões honestas após atendimentos reais"],
                ["Site e menções", "relação entre marca, serviço e local", "usar páginas úteis e dados consistentes"],
            ],
            nota="Nenhum item isolado garante o bloco local. A combinação muda conforme busca, localização e concorrência."
        )}

        <h2>1. Arrume a base do Perfil da Empresa</h2>

        <p>Abra o perfil e confira o básico como se você fosse um cliente que nunca ouviu falar da marca:
        nome real, categoria, telefone, horário, site e endereço ou área de atendimento. Uma informação
        errada não é detalhe. Ela pode impedir o contato e ainda deixar menos clara a correspondência entre
        a empresa e a pesquisa.</p>

        <p>Não acrescente bairro, cidade ou serviço ao nome apenas para repetir palavras-chave. O nome deve
        acompanhar a marca usada no mundo real. Uma ficha inflada pode até parecer “agressiva”, mas cria
        risco de edição, suspensão e perda de confiança. A força deve vir da cobertura correta dos campos,
        das páginas e das provas, não de um nome inventado.</p>

        <h2>2. Transforme cada serviço importante em uma resposta concreta</h2>

        <p>Uma empresa que oferece dez serviços, mas resume tudo em “soluções completas”, dificulta o
        entendimento. Liste os serviços no perfil e crie no site uma página realmente útil para cada linha
        comercial prioritária. Explique para quem serve, qual problema resolve, como funciona, onde há
        atendimento e como pedir orçamento.</p>

        <p>Essa organização também melhora a conversão. Quem procura “conserto de ar-condicionado perto de
        mim” não quer aterrissar em uma página genérica sobre climatização. Quer confirmar rapidamente se a
        empresa faz aquele reparo, atende a região e pode ser acionada.</p>

        <h2>3. Mostre a região sem fabricar páginas-porta</h2>

        <p>É válido informar cidades e bairros realmente atendidos. O problema começa quando se publica a
        mesma página dezenas de vezes, trocando somente o nome do lugar, ou quando se afirma ter unidade
        onde não existe operação. Além de frustrar o cliente, isso cria páginas sem valor próprio.</p>

        <p>Uma página local boa contém evidência local: forma de atendimento, limites da área, prazo ou
        logística quando isso for relevante, trabalhos reais, perguntas específicas e dados que ajudem a
        decidir. Se não há informação suficiente para diferenciar uma cidade, é melhor fortalecer a página
        principal do serviço e explicar nela a cobertura verdadeira.</p>

        <h2>4. Construa avaliações que ajudem uma pessoa a escolher</h2>

        <p>Peça a avaliação depois de um atendimento concluído, por um caminho simples e sem oferecer
        prêmio. Responda de forma individual, inclusive quando a mensagem for curta. A avaliação existe
        primeiro para o próximo cliente; o valor para o posicionamento vem junto com essa prova pública de
        que a empresa atende pessoas reais.</p>

        <p>Não entregue um texto pronto para todo mundo copiar. Além de soar artificial, uma sequência de
        comentários iguais não explica o que a empresa fez bem. O cliente pode mencionar espontaneamente o
        serviço e a experiência que teve, com as palavras dele.</p>

        <h2>5. Confira se site, perfil e contato contam a mesma história</h2>

        <p>Telefone diferente, endereço antigo, horários conflitantes e páginas que falam de serviços que o
        perfil não mostra criam ruído. Faça uma revisão simples em todos os pontos controlados pela empresa.
        Depois, teste o clique no telefone, no WhatsApp e no site pelo celular.</p>

        <p>Para comércio e atendimento local, a página de {link('/para-comercios-locais/', 'SEO para negócios locais')}
        mostra como perfil, site e reputação trabalham juntos. Ela é o destino comercial deste assunto; este
        artigo existe para explicar a dúvida “perto de mim” sem transformar a resposta em uma propaganda.</p>

        <h2>Como medir uma busca que muda por localização</h2>

        <p>Não use uma busca manual isolada como relatório. Registre um conjunto de termos ligados aos
        serviços, acompanhe as ações do Perfil da Empresa e compare os contatos recebidos. No site, observe
        consultas e páginas no Search Console, além de ligações, formulários e cliques no WhatsApp.</p>

        <ul>
          <li>se a empresa aparece pelo nome, mas não pelo serviço, falta relevância para a intenção;</li>
          <li>se aparece perto do endereço e some em outros bairros, a distância pesa naquele cenário;</li>
          <li>se aparece, recebe visualização e ninguém clica, reveja fotos, avaliações, horário e proposta;</li>
          <li>se o clique chega e não vira contato, o problema pode estar na página ou no atendimento.</li>
        </ul>

        <h2>Plano de ação para esta semana</h2>

        <ol>
          <li>pesquise e elimine fichas duplicadas antes de criar qualquer coisa;</li>
          <li>confira categoria principal, endereço ou área, telefone, horário e site;</li>
          <li>liste os três serviços que mais trazem receita e veja se cada um está explicado;</li>
          <li>adicione fotos atuais e organize um pedido de avaliação pós-atendimento;</li>
          <li>teste a empresa em alguns pontos reais da área atendida, registrando data e local;</li>
          <li>meça ações de contato durante algumas semanas antes de mudar tudo de novo.</li>
        </ol>
        """,
        "faq": [
            ("Preciso escrever “perto de mim” no nome da empresa?",
             "Não. Use o nome real da empresa. A proximidade é calculada a partir da localização de quem pesquisa e dos dados corretos do negócio; acrescentar a expressão ao nome pode contrariar as diretrizes do perfil."),
            ("Uma empresa sem endereço aberto ao público pode aparecer?",
             "Pode, quando é uma empresa elegível de área de atendimento e visita o cliente. Nesse caso, configure a área atendida e oculte o endereço residencial, seguindo as regras do Google."),
            ("Avaliação com nome do serviço ajuda?",
             "O mais importante é que a avaliação seja real e espontânea. Não dê um texto pronto. Oriente apenas o cliente a contar, com as palavras dele, como foi a experiência."),
            ("Devo criar uma página para cada bairro?",
             "Somente se cada página tiver utilidade e evidência próprias. Copiar o mesmo texto e trocar o bairro cria páginas fracas. Na maioria dos casos, uma página forte por serviço e uma cobertura regional clara são uma base melhor."),
        ],
        "cta": ("Sua empresa existe no mapa, mas some quando o cliente busca o serviço perto dele? Eu verifico perfil, site, área atendida e concorrentes para mostrar onde a visibilidade está travando.",
                "/diagnostico-presenca-digital/", "Solicitar diagnóstico gratuito"),
    },
    {
        "slug": "como-aparecer-no-google-sem-pagar",
        "h1": "Como aparecer no Google sem pagar por anúncios",
        "title": "Como aparecer no Google sem pagar por anúncios | RCB",
        "desc": ("Veja como aparecer no Google sem pagar por anúncios: Perfil da Empresa gratuito, "
                 "site indexável, páginas de serviço, conteúdo e medição."),
        "cat": "Aparecer no Google",
        "data": DATA,
        "trilha_extra": ("/como-aparecer-no-google/", "Aparecer no Google"),
        "corpo": f"""
        <p>Dá para aparecer no Google sem comprar anúncios. Para um negócio local, o caminho gratuito passa
        por um Perfil da Empresa verificado, um site que o Google consiga rastrear e páginas que respondam
        ao que o cliente procura. Você não paga por clique, mas precisa investir trabalho e consistência.</p>

        {caixa('<p><strong>Em termos simples:</strong> crie ou reivindique o Perfil da Empresa sem custo, '
               'publique páginas úteis no site, facilite o rastreamento, conquiste avaliações verdadeiras '
               'e acompanhe as consultas no Search Console. Google Ads compra exposição; não é uma taxa '
               'obrigatória para entrar nos resultados orgânicos ou no Maps.</p>')}

        <p>Essa distinção evita duas frustrações comuns. A primeira é achar que o cadastro gratuito garante
        o primeiro lugar. A segunda é pensar que, sem dinheiro para mídia, não há nada a fazer. Nem uma
        coisa nem outra é verdade: existe um caminho orgânico, só que ele leva tempo e depende da qualidade
        da execução.</p>

        <p>Se você ainda está decidindo entre os canais, leia {link('/blog/como-divulgar-minha-empresa-no-google/', 'como divulgar sua empresa no Google')}.
        Aqui o recorte é mais específico: o que fazer quando a meta é construir visibilidade sem pagar por
        anúncios.</p>

        <h2>O que é gratuito — e o que continua tendo custo</h2>

        {tabela(
            ["Frente", "Há cobrança do Google por clique?", "Custo real"],
            [
                ["Perfil da Empresa", "não", "tempo para configurar, verificar e manter"],
                ["Google Maps orgânico", "não", "relevância local, reputação e consistência"],
                ["Resultados orgânicos do site", "não", "site, conteúdo, ajustes técnicos e acompanhamento"],
                ["Google Ads", "sim, conforme campanha", "mídia, configuração, página e medição"],
            ],
            nota="Gratuito significa sem cobrança por exposição orgânica ou clique; não significa resultado automático nem trabalho zero."
        )}

        <p>O Google informa que
        <a class="artigo-link" href="https://support.google.com/business/answer/7039811?hl=pt-BR"
        target="_blank" rel="noopener noreferrer">criar e gerenciar um Perfil da Empresa não tem custo financeiro</a>.
        Também não cobra para rastrear ou indexar uma página que atende aos
        <a class="artigo-link" href="https://developers.google.com/search/docs/essentials/technical?hl=pt-br"
        target="_blank" rel="noopener noreferrer">requisitos técnicos da Pesquisa</a>. Ainda assim, criação do site,
        fotografia, redação, manutenção e consultoria podem ser feitos pela própria empresa ou contratados.
        O custo muda de mídia para operação.</p>

        <h2>1. Coloque a empresa no Maps sem pagar</h2>

        <p>Pesquise primeiro o nome, telefone e endereço no Google Maps. Se já existir uma ficha, solicite a
        propriedade; se não existir, crie o perfil e siga a verificação mostrada pelo Google. Duplicar a
        empresa porque você não encontrou o acesso antigo costuma piorar o problema.</p>

        <p>Depois da verificação, preencha os campos de forma completa e honesta. Categoria, horário,
        telefone, área de atendimento, serviços e fotos reais ajudam o cliente e dão contexto ao sistema.
        O tutorial detalhado está em {link('/blog/como-colocar-minha-empresa-no-google/', 'como colocar uma empresa no Google')}.</p>

        <h2>2. Confira se o site pode entrar no índice</h2>

        <p>Um site publicado não entra automaticamente em todas as buscas. Ele precisa responder com status
        correto, permitir o acesso do Googlebot, ter conteúdo indexável e não carregar uma instrução
        <code>noindex</code>. O sitemap ajuda o Google a descobrir URLs, mas não garante indexação nem melhora
        posição sozinho.</p>

        <p>Faça uma busca por <code>site:seudominio.com.br</code> como triagem e confirme as páginas mais
        importantes na inspeção de URL do Search Console. Se nada aparecer, siga o diagnóstico de
        {link('/blog/por-que-meu-site-nao-aparece-no-google/', 'site que não aparece no Google')} antes de publicar dezenas de textos.</p>

        <h2>3. Crie páginas para o serviço que a pessoa procura</h2>

        <p>A página inicial raramente consegue explicar todos os serviços com profundidade. Escolha primeiro
        as ofertas que geram receita e crie uma página para cada intenção comercial importante. O título,
        a introdução e os subtítulos precisam responder com clareza: o que é, para quem serve, como funciona,
        onde atende, quais provas existem e como falar com a empresa.</p>

        <p>Não abra cinco URLs para sinônimos da mesma pergunta. “Conserto de geladeira” e “assistência para
        refrigerador”, por exemplo, podem pertencer à mesma intenção. Uma página completa costuma ser mais
        forte do que várias versões curtas competindo entre si.</p>

        <h2>4. Publique conteúdo que resolva uma dúvida anterior à compra</h2>

        <p>Artigo funciona quando aproxima uma dúvida real de um serviço real. Liste as perguntas que chegam
        no WhatsApp, as objeções ouvidas em orçamento e os erros que o cliente comete antes de contratar.
        Depois responda com exemplos, limites, passos e critérios de decisão.</p>

        <p>Ao final, a ligação com a página comercial precisa ser natural. Quem termina um guia sobre
        indexação pode querer uma auditoria; quem lê sobre presença local pode precisar de
        {link('/consultoria-seo-local/', 'consultoria de SEO local')}. O link deve ajudar a próxima decisão,
        não existir apenas para repetir uma palavra-chave.</p>

        <h2>5. Use avaliações, fotos e casos como prova</h2>

        <p>Resultados gratuitos ainda disputam atenção. Fotos atuais, avaliações legítimas, respostas úteis
        e casos documentados ajudam uma pessoa a escolher entre empresas que oferecem algo parecido. Não
        compre avaliações e não publique números que você não consegue demonstrar.</p>

        <p>No site da RCB, por exemplo, números são ligados aos registros apresentados na
        {link('/cases/', 'página de cases')}. Essa é a diferença entre prova e decoração: o leitor consegue
        entender o período, a métrica e o que realmente mudou.</p>

        <h2>6. Faça a linkagem interna trabalhar a seu favor</h2>

        <p>Uma página órfã depende de o Google encontrá-la apenas no sitemap. Ligue guias relacionados entre
        si e, principalmente, conecte artigos informativos às páginas de serviço adequadas. Use textos de
        link variados e descritivos, sem transformar cada parágrafo em uma lista de palavras-chave.</p>

        <p>Um caminho simples para este tema é: {link('/como-aparecer-no-google/', 'guia principal para aparecer no Google')},
        cadastro do perfil, diagnóstico de páginas que não aparecem e páginas comerciais por serviço. Assim,
        cada URL tem um papel, e a arquitetura mostra quais são os conteúdos centrais.</p>

        <h2>7. Meça antes de concluir que não funcionou</h2>

        <p>No Search Console, acompanhe impressões, consultas, páginas e posição média. No Perfil da Empresa,
        observe visualizações e ações disponíveis, como cliques, ligações e rotas. No site, registre envio de
        formulário e clique no WhatsApp. Sem isso, uma alta de visibilidade pode passar despercebida — ou uma
        página pode receber visitas sem gerar nenhum contato.</p>

        <p>Compare períodos equivalentes e anote a data das mudanças. SEO não reage como um interruptor. O
        rastreamento, a indexação e a reavaliação levam tempo, e a concorrência não fica parada enquanto você
        trabalha.</p>

        <h2>Plano orgânico de 30 dias</h2>

        <ol>
          <li><strong>Semana 1:</strong> reivindique o perfil, corrija os dados e teste todos os contatos.</li>
          <li><strong>Semana 2:</strong> instale Search Console e Analytics, revise indexação e sitemap.</li>
          <li><strong>Semana 3:</strong> melhore uma página comercial prioritária e publique uma resposta útil.</li>
          <li><strong>Semana 4:</strong> ligue as páginas, peça avaliações reais e registre o ponto de partida.</li>
        </ol>

        <p>Em 30 dias, a meta não é prometer o topo. É deixar uma base rastreável, compreensível e mensurável.
        A partir daí, os dados mostram se o gargalo está na indexação, relevância, contexto local, reputação
        ou conversão.</p>

        <h2>Quando anúncios ainda podem fazer sentido</h2>

        <p>Não pagar anúncios é uma escolha válida, mas não precisa virar regra ideológica. Mídia pode ajudar
        em lançamento, oferta urgente ou teste de demanda. O ponto é não confundir os canais: Ads compra
        exposição enquanto há orçamento; SEO constrói páginas e sinais que continuam existindo.</p>

        <p>Se o orçamento é curto, arrume primeiro o destino do clique. Pagar para enviar gente a uma página
        lenta, genérica ou sem contato apenas acelera o desperdício. Uma base orgânica boa também melhora a
        experiência de quem chega por anúncio depois.</p>
        """,
        "faq": [
            ("O Google cobra para colocar uma empresa no Maps?",
             "Não. Criar ou reivindicar um Perfil da Empresa elegível é gratuito. Pode haver custo se você contratar alguém para configurar, produzir fotos ou manter o perfil."),
            ("Preciso pagar para o Google indexar meu site?",
             "Não. O Google não cobra para rastrear ou indexar páginas. A página precisa estar acessível, funcionar e ter conteúdo indexável; mesmo assim, a indexação não é garantida."),
            ("Sem anúncio eu consigo ficar em primeiro?",
             "É possível aparecer organicamente, mas ninguém pode garantir a primeira posição. O resultado depende da busca, concorrência, localização, qualidade da página e outros sinais."),
            ("Quanto tempo leva para aparecer sem pagar?",
             "Não existe prazo fixo. Perfil verificado e busca pela marca podem reagir antes; páginas novas e termos competitivos podem levar mais tempo para rastreamento, indexação e ganho de posição."),
        ],
        "cta": ("Quer descobrir o que dá para fazer com a estrutura que você já tem, antes de gastar com anúncio? Eu reviso perfil, site, indexação e páginas prioritárias e mostro a ordem de ataque.",
                "/diagnostico-presenca-digital/", "Solicitar diagnóstico gratuito"),
    },
]
