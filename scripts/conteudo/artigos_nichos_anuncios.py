# -*- coding: utf-8 -*-
"""
Artigos de nicho ligados à linha "Sites e Anúncios" (28/09/2026).

Brecha medida: o blog cobria clínicas pelo lado orgânico, mas não tinha nada de
energia solar nem nada que ligasse os nichos a anúncio, landing page e site —
o espaço que o concorrente Máximos Digital ocupa com postagens de nicho.

Regras: sem preço da RCB (faixas/exemplos marcados como exemplo são permitidos),
sem resultado prometido, todo artigo termina no WhatsApp e aponta para as páginas
de serviço. Normas citadas só onde a referência é conhecida e estável.
"""
from urllib.parse import quote

from rcb_artigo import caixa, tabela, link

DATA = "2026-09-28"


def wa(texto):
    return "https://wa.me/5562991161040?text=" + quote(texto, safe="")


LEI_14300 = ('<a href="https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm" '
             'target="_blank" rel="noopener noreferrer">Lei 14.300/2022</a>')

PROV_205 = ('<a href="https://www.oab.org.br/leisnormas/legislacao/provimentos/205-2021" '
            'target="_blank" rel="noopener noreferrer">Provimento 205/2021</a>')

ARTIGOS = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "como-conseguir-clientes-energia-solar",
        "h1": "Como conseguir clientes de energia solar: o que funciona em 2026",
        "title": "Como conseguir clientes de energia solar em 2026",
        "desc": ("Como conseguir clientes de energia solar: Google Maps, site, Google Ads e Instagram para "
                 "integradoras venderem mais sem depender só de indicação."),
        "cat": "Energia solar",
        "data": DATA,
        "atualizado": "2026-10-04",
        "trilha_extra": ("/marketing-para-energia-solar/", "Marketing para energia solar"),
        "corpo": f"""
        <p>Para conseguir clientes de energia solar hoje, a integradora precisa estar onde o cliente pesquisa
        antes de pedir orçamento: no <strong>Google Maps</strong>, num <strong>site que explica o sistema na
        língua dele</strong> e em <strong>anúncios no Google e no Instagram</strong> bem segmentados por região.
        Indicação continua importante, mas sozinha ela não enche a agenda de visitas técnicas.</p>

        <p>O mercado de energia solar ficou mais disputado. O IBGE classifica a instalação de painéis solares em
        prédios dentro do
        <a href="https://cnae.ibge.gov.br/?subclasse=4321500&amp;tipo=cnae&amp;versao=10&amp;view=subclasse" target="_blank" rel="noopener noreferrer">CNAE 4321-5/00</a>
        (Instalação e manutenção elétrica), que tinha 328.524 empresas ativas e 17.358 aberturas em 90 dias pelos
        dados públicos de CNPJ de junho de 2026 — nem todas de energia solar, porque o código inclui eletricistas
        em geral. O cliente compara vários orçamentos antes de fechar, e quem aparece primeiro, passa confiança e
        responde rápido sai na frente — mesmo sem ser o mais barato.</p>

        {caixa('<p><strong>Resposta rápida:</strong> organize o Perfil da Empresa no Google com fotos de '
               'instalações reais e avaliações; tenha um site com páginas separadas para residencial, comercial e '
               'rural; anuncie no Google para quem já pesquisa "energia solar" na sua cidade e use o Instagram para '
               'mostrar obras e gerar demanda. Todo caminho deve terminar numa conversa no WhatsApp.</p>')}

        <h2>1. Google Maps: onde o cliente de energia solar começa a procurar</h2>
        <p>Quem pesquisa "energia solar perto de mim" ou "instalação de placa solar em Goiânia" recebe primeiro o
        mapa com três empresas. Estar ali depende do
        {link('/google-perfil-empresa/', 'Google Perfil da Empresa')} bem configurado: categoria certa, área
        atendida, fotos de instalações de verdade, descrição dos serviços e — principalmente — avaliações.</p>
        <p>Energia solar é compra alta e de longo prazo. O cliente lê avaliação com atenção, procurando sinais de
        que a empresa entrega no prazo, resolve problema e dá suporte depois. Cada obra entregue é uma chance de
        pedir avaliação com foto. Dez avaliações detalhadas valem mais que cinquenta genéricas.</p>

        <h2>2. Site que explica o sistema na língua do cliente</h2>
        <p>O cliente de energia solar tem muita dúvida: quanto vai economizar, quanto tempo leva para o sistema se
        pagar, o que acontece em dia nublado, se precisa trocar o telhado, como fica com as regras da
        {LEI_14300}, o marco legal da geração distribuída. O site que responde essas perguntas com clareza vende
        antes mesmo da primeira conversa.</p>
        <p>O erro comum é ter uma página só, falando de tudo. O certo é separar: uma página para energia solar
        residencial, uma para comercial, uma para rural, uma para cada cidade que você atende. Cada página
        responde a uma busca diferente. Veja o que precisa ter em
        {link('/blog/site-para-empresa-de-energia-solar/', 'site para empresa de energia solar')}.</p>

        <h2>3. Google Ads para quem já está pronto para pedir orçamento</h2>
        <p>Buscas como "orçamento energia solar", "empresa de energia solar em Goiânia" ou "preço de placa solar
        instalada" vêm de gente perto da decisão. O Google Ads coloca sua empresa na frente dessa pessoa hoje,
        enquanto o trabalho no Google orgânico ainda está maturando.</p>
        <p>Dois cuidados fazem a diferença entre anúncio que traz cliente e anúncio que queima verba:</p>
        <ul>
          <li><strong>Bloquear buscas erradas:</strong> "curso de energia solar", "vaga de instalador",
          "energia solar grátis", "como fazer placa solar". Sem essa lista, você paga clique de quem nunca vai
          comprar.</li>
          <li><strong>Mandar o clique para a página certa:</strong> quem clicou em "energia solar para
          fazenda" precisa cair numa página rural, não na página inicial. Uma
          {link('/criacao-de-landing-page/', 'landing page')} por tipo de cliente costuma mudar o
          resultado.</li>
        </ul>

        <h2>4. Instagram e Facebook para gerar demanda</h2>
        <p>No Instagram a pessoa não está procurando energia solar — ela está rolando o feed. Por isso o
        anúncio precisa despertar interesse: a obra do vizinho, a conta de luz antes e depois (com autorização do
        cliente), um vídeo curto da instalação. O objetivo da campanha deve ser conversa no WhatsApp, com público
        por região e perfil compatível com o investimento.</p>
        <p>Um cuidado: não prometa economia exata no anúncio. Economia depende do consumo, da tarifa e da
        instalação de cada cliente. Promessa genérica atrai curioso e gera desconfiança; simulação feita na
        conversa gera cliente.</p>

        <h2>5. Responder rápido fecha mais do que baixar preço</h2>
        <p>Quem pede orçamento de energia solar costuma pedir para várias empresas ao mesmo tempo. A primeira que
        responde com clareza, pergunta o valor da conta de luz e marca a visita técnica leva vantagem. Deixe uma
        mensagem pronta no botão de WhatsApp do site e do anúncio, para saber de onde cada contato veio, e
        responda no mesmo dia.</p>

        {tabela(
            ["Canal", "Quando funciona melhor", "O que não pode faltar"],
            [
                ["Google Maps", "Cliente que pesquisa empresa perto dele", "Fotos reais e avaliações detalhadas"],
                ["Site", "Cliente que compara e tira dúvida antes de chamar", "Páginas por tipo de cliente e por cidade"],
                ["Google Ads", "Cliente pronto para pedir orçamento", "Buscas bloqueadas e página certa"],
                ["Instagram/Facebook", "Gerar demanda na sua região", "Obras reais e objetivo de conversa"],
            ])}

        <h2>6. Esteja pronto quando a conta de luz pesar</h2>
        <p>A procura por energia solar costuma acompanhar o bolso. A ANEEL define todo mês a
        <a href="https://www.gov.br/aneel/pt-br/assuntos/tarifas/bandeiras-tarifarias" target="_blank" rel="noopener noreferrer">bandeira tarifária</a>
        — verde, amarela ou vermelha —, que indica se a energia vai custar mais naquele período. Meses de bandeira
        mais cara e de calor, com ar-condicionado ligado, tendem a ser quando muita gente decide fazer a conta. Quem já está
        no Google o ano todo e tem o anúncio pronto para aumentar a verba nesses meses recebe os pedidos primeiro;
        quem só começa a divulgar quando a conta já subiu chega atrasado.</p>

        <h2>Por onde começar a conseguir clientes de energia solar</h2>
        <p>Se a sua empresa ainda depende só de indicação, comece pelo que traz resultado mais rápido: Perfil da
        Empresa organizado e um anúncio no Google bem feito para a sua cidade, levando para uma página específica.
        Em paralelo, construa o site com as páginas certas — é ele que vai trazer cliente de graça daqui a alguns
        meses. Se você quer ajuda com a parte dos anúncios, veja como funciona o
        {link('/trafego-pago-para-energia-solar/', 'tráfego pago para energia solar')}. E para ver as quatro frentes
        juntas — Google Meu Negócio, site, anúncio e landing page —, leia sobre o
        {link('/marketing-para-energia-solar/', 'marketing para empresas de energia solar')}. Ideias práticas de
        divulgação estão em {link('/blog/como-divulgar-empresa-de-energia-solar/', 'como divulgar empresa de energia solar')}.</p>
""",
        "faq": [
            ("Qual a melhor forma de conseguir clientes de energia solar?",
             "A combinação que costuma funcionar é Google Perfil da Empresa com avaliações, site com páginas por "
             "tipo de cliente e anúncio no Google para quem já pesquisa na sua cidade. O Instagram ajuda a gerar "
             "demanda. Todo caminho deve terminar numa conversa rápida no WhatsApp."),
            ("Vale a pena anunciar energia solar no Google Ads?",
             "Vale, porque quem pesquisa \"orçamento energia solar\" está perto da decisão. O cuidado é bloquear "
             "buscas de curso, emprego e curiosidade, e mandar o clique para uma página específica, não para a "
             "página inicial."),
            ("Posso prometer economia na conta de luz no anúncio?",
             "Evite prometer número exato. A economia depende do consumo, da tarifa e da instalação de cada "
             "cliente. É melhor mostrar casos reais com autorização e fazer a simulação na conversa."),
            ("Instagram funciona para empresa de energia solar?",
             "Funciona para gerar demanda e mostrar obras, principalmente com anúncio segmentado por região. Mas "
             "para quem já está procurando orçamento, o Google costuma trazer contatos mais prontos para fechar."),
            ("Existe época melhor para buscar clientes de energia solar?",
             "A procura costuma crescer quando a conta de luz pesa — meses de calor e de bandeira tarifária mais cara. "
             "O ideal é estar no Google o ano todo e aumentar a verba de anúncio nesses períodos."),
        ],
        "cta": ("Tem uma empresa de energia solar e quer mais pedidos de orçamento? Me conte a sua cidade e como "
                "você vende hoje. Em até 24 horas eu te digo por onde começar — Maps, site ou anúncio.",
                wa("Olá, Renan! Tenho uma empresa de energia solar e quero mais clientes. Pode me ajudar?"),
                "Quero mais clientes de energia solar"),
    },

    # ------------------------------------------------------------------ 2
    {
        "slug": "site-para-empresa-de-energia-solar",
        "h1": "Site para empresa de energia solar: o que precisa ter para vender",
        "title": "Site para empresa de energia solar: o que precisa ter",
        "desc": ("Site para empresa de energia solar: as páginas, provas e respostas que fazem o cliente pedir "
                 "orçamento — e aparecer no Google na sua cidade."),
        "cat": "Energia solar",
        "data": DATA,
        "trilha_extra": ("/criacao-de-sites-goiania/", "Criação de sites"),
        "corpo": f"""
        <p>Um bom site para empresa de energia solar precisa de três coisas: <strong>páginas separadas para
        cada tipo de cliente</strong> (residencial, comercial e rural), <strong>provas de que você entrega</strong>
        (obras reais, avaliações, equipe) e <strong>um caminho curto até o WhatsApp</strong> com a pergunta certa
        — o valor da conta de luz. Site de uma página só, com um kit e um botão, raramente vende.</p>

        <p>O cliente de energia solar pesquisa muito antes de pedir orçamento. É um investimento alto, de longo
        prazo, e ele tem medo de cair em empresa que some depois da instalação. O site é onde ele decide se você
        merece a conversa.</p>

        {caixa('<p><strong>Checklist rápido:</strong> página por tipo de cliente; página por cidade atendida; '
               'galeria de obras com local e potência; avaliações reais; perguntas frequentes sobre economia, '
               'retorno e manutenção; botão de WhatsApp em todas as páginas pedindo o valor da conta; site rápido '
               'no celular; ligação com o Perfil da Empresa no Google.</p>')}

        <h2>As páginas que um site de energia solar precisa ter</h2>
        <h3>Uma página para cada tipo de cliente</h3>
        <p>O dono de casa, o comerciante e o produtor rural pesquisam coisas diferentes e têm dúvidas diferentes.
        O residencial quer saber da conta de luz e do telhado; o comercial quer saber de retorno do investimento
        e financiamento; o rural quer saber de bombeamento, irrigação e sistemas maiores. Cada um merece página
        própria — e cada página disputa uma busca diferente no Google.</p>

        <h3>Uma página para cada cidade que você atende</h3>
        <p>Busca de energia solar é local: "energia solar em Aparecida de Goiânia", "placa solar em Anápolis". Se
        você atende várias cidades, uma página por cidade, com obras daquela região, ajuda a aparecer em cada uma.
        Página copiada trocando só o nome da cidade não funciona — o Google percebe.</p>

        <h3>Galeria de obras de verdade</h3>
        <p>Foto de banco de imagem não convence ninguém. Mostre obras reais com cidade, tipo de telhado e potência
        instalada. Se o cliente autorizar, mostre também a conta de luz antes e depois. É a prova mais forte que
        existe nesse mercado.</p>

        <h3>Perguntas frequentes honestas</h3>
        <p>Quanto tempo o sistema leva para se pagar, o que acontece em dia nublado, se precisa de manutenção,
        como ficou a compensação de energia depois da {LEI_14300}. Responder com franqueza — inclusive dizendo
        "depende do seu consumo" — passa mais confiança do que prometer economia fixa.</p>

        <h2>O caminho até o orçamento</h2>
        <p>O botão de WhatsApp deve estar em todas as páginas e já abrir a conversa com a pergunta certa: "Qual o
        valor médio da sua conta de luz?". Isso qualifica o contato e acelera a simulação. Formulário longo com
        dez campos espanta; uma pergunta simples traz a conversa.</p>
        <p>Simulador no site pode ajudar, mas não substitui a conversa. O número que ele mostra é estimativa, e o
        cliente precisa saber disso para não se frustrar depois.</p>

        <h2>Site bonito não basta: ele precisa aparecer</h2>
        <p>O site só vende se for encontrado. Isso exige texto escrito para as buscas do seu cliente, velocidade no
        celular e ligação com o {link('/google-perfil-empresa/', 'Perfil da Empresa no Google')}. Enquanto o site
        sobe nas buscas orgânicas — o que leva meses —, anúncios no Google levando para as páginas certas trazem
        pedidos de orçamento desde o primeiro mês. Veja
        {link('/blog/como-conseguir-clientes-energia-solar/', 'como conseguir clientes de energia solar')} e como
        o site se junta ao Google Meu Negócio e ao anúncio no
        {link('/marketing-para-energia-solar/', 'marketing para empresas de energia solar')}.</p>

        {tabela(
            ["Página", "Busca que ela disputa", "O que precisa mostrar"],
            [
                ["Energia solar residencial", "energia solar para casa", "Conta de luz, telhado, retorno"],
                ["Energia solar comercial", "energia solar para empresa", "Retorno, financiamento, obras comerciais"],
                ["Energia solar rural", "energia solar para fazenda", "Bombeamento, irrigação, sistemas maiores"],
                ["Página por cidade", "energia solar em [cidade]", "Obras e avaliações daquela região"],
            ])}

        <h2>Erros comuns em site de energia solar</h2>
        <ul>
          <li><strong>Falar de painel, inversor e kWp antes de falar da conta de luz.</strong> O cliente quer
          saber quanto vai pagar a menos, não a ficha técnica do equipamento. A parte técnica é importante, mas
          vem depois, para quem já se interessou.</li>
          <li><strong>Esconder quem é a empresa.</strong> Sem endereço, sem CNPJ, sem foto da equipe e sem
          obras, o cliente não tem como saber se você vai existir daqui a cinco anos, quando precisar de
          suporte. Mostre tudo isso com clareza.</li>
          <li><strong>Prometer economia fixa.</strong> "Economize 95% na conta" atrai curioso e vira
          reclamação quando a conta real não bate. A economia depende do consumo e da tarifa de cada um.</li>
          <li><strong>Formulário no lugar do WhatsApp.</strong> Muita gente prefere mandar uma foto da conta de
          luz no WhatsApp do que preencher campos. Ofereça os dois, com o WhatsApp em destaque.</li>
          <li><strong>Site lento no celular.</strong> Galeria com fotos pesadas, sem compressão, faz a página
          demorar a abrir. Quem pesquisa pelo celular desiste antes de ver a primeira obra.</li>
        </ul>
        <p>Cada um desses erros custa pedido de orçamento todo mês — e quase todos são simples de corrigir em
        um site feito com o cliente de energia solar em mente.</p>

        <h2>Quanto custa um site para empresa de energia solar</h2>
        <p>Depende de quantas páginas, cidades e obras entram no projeto, e de quem escreve os textos. Um site com
        páginas por tipo de cliente e por cidade é um projeto maior do que um site de uma página — e é o que traz
        cliente pelo Google. Veja as faixas do mercado em
        {link('/blog/quanto-custa-um-site/', 'quanto custa um site')} e como funciona a
        {link('/criacao-de-sites-goiania/', 'criação de sites em Goiânia')}.</p>
""",
        "faq": [
            ("O que um site de energia solar precisa ter?",
             "Páginas separadas para residencial, comercial e rural, uma página por cidade atendida, galeria de "
             "obras reais, avaliações, perguntas frequentes honestas sobre economia e retorno e um botão de "
             "WhatsApp em todas as páginas."),
            ("Simulador de economia no site vale a pena?",
             "Pode ajudar a engajar, mas o número é sempre uma estimativa. O cliente precisa saber disso, e a "
             "simulação de verdade acontece na conversa, com o consumo real dele."),
            ("Preciso de uma página para cada cidade?",
             "Se você atende várias cidades e quer aparecer em cada uma, sim — desde que cada página tenha "
             "conteúdo próprio, com obras e avaliações daquela região. Página copiada trocando só o nome não funciona."),
            ("Quanto tempo o site leva para aparecer no Google?",
             "Entrar no Google é rápido; aparecer bem posicionado leva meses, porque depende da concorrência na "
             "sua cidade. Por isso muitas integradoras combinam o site com anúncio no começo."),
        ],
        "cta": ("Quer um site de energia solar que traga pedido de orçamento? Me conte as cidades que você atende e "
                "os tipos de cliente. Em até 24 horas você recebe o orçamento sob medida.",
                wa("Olá, Renan! Tenho uma empresa de energia solar e quero um orçamento de site."),
                "Quero o site da minha integradora"),
    },

    # ------------------------------------------------------------------ energia solar: divulgar
    # Etapa 4 do plano de nichos (04/10/2026). Busca do DONO: "como divulgar energia solar",
    # "ideias de marketing para energia solar". Diferente do "como conseguir clientes" (canais):
    # aqui sao ideias praticas de divulgacao. Fontes: ANEEL, CDC, LGPD.
    {
        "slug": "como-divulgar-empresa-de-energia-solar",
        "h1": "Como divulgar empresa de energia solar: 10 ideias que trazem pedido de orçamento",
        "title": "Como divulgar empresa de energia solar: 10 ideias",
        "desc": ("Como divulgar empresa de energia solar: 10 ideias práticas para o integrador — obras reais, "
                 "parcerias, indicação, conteúdo e anúncio no momento certo."),
        "cat": "Energia solar",
        "data": "2026-10-04",
        "trilha_extra": ("/marketing-para-energia-solar/", "Marketing para energia solar"),
        "corpo": f"""
        <p>Para divulgar uma empresa de energia solar, o integrador precisa mostrar prova — obras reais,
        clientes satisfeitos, processo explicado — no lugar onde o cliente da região já está olhando: o Google,
        o WhatsApp e as pessoas em quem ele confia. As ideias abaixo são práticas, cabem no orçamento de uma
        empresa pequena e não dependem de prometer economia que você não pode garantir.</p>

        {caixa('<p><strong>Resposta rápida:</strong> publique fotos e vídeos de obras reais (com autorização), '
               'peça avaliação na hora certa, faça parcerias com quem já fala com o seu cliente, organize a '
               'indicação, explique as dúvidas mais comuns e anuncie no Google quando a conta de luz pesa. Tudo '
               'levando para uma conversa no WhatsApp.</p>')}

        <h2>1. Transforme cada obra entregue em vitrine</h2>
        <p>Nada convence mais o vizinho do que a obra na rua dele. Fotografe o antes, o durante e o sistema
        pronto, grave um vídeo curto do telhado e publique no
        {link('/google-perfil-empresa/', 'Google Perfil da Empresa')} e nas redes — sempre com autorização
        escrita do cliente. Foto de banco de imagem não mostra que você existe; foto da sua equipe mostra.</p>

        <h2>2. Peça a avaliação no momento em que o cliente está feliz</h2>
        <p>O melhor momento costuma ser quando o sistema é ligado ou quando chega a primeira conta já com a
        energia compensada. Mande o link direto da avaliação pelo WhatsApp e peça que ele conte como foi a
        instalação. Avaliação detalhada, com cidade e tipo de obra, ajuda quem está decidindo — e ajuda a sua
        empresa a aparecer no mapa.</p>

        <h2>3. Faça parceria com quem já fala com o seu cliente</h2>
        <p>Arquitetos, engenheiros, construtoras, lojas de material elétrico e revendas agrícolas conversam todo
        dia com quem pode instalar energia solar. Uma parceria com regras por escrito — como a indicação chega,
        como é atendida, como cada parte é remunerada — vira um canal estável, que não depende de anúncio.</p>

        <h2>4. Organize a indicação, em vez de esperar por ela</h2>
        <p>Indicação boa não acontece por acaso. Depois da instalação, deixe com o cliente uma mensagem pronta
        para ele encaminhar e combine, por escrito, como você agradece quem indica. O que não pode é prometer um
        prêmio e não cumprir — isso desfaz a confiança que a obra construiu.</p>

        <h2>5. Responda as dúvidas que todo cliente faz</h2>
        <p>Funciona em dia nublado? Precisa trocar o telhado? Como fica a conta depois? E a
        {LEI_14300}, muda o quê? Cada pergunta dessas vira um texto curto no site, um vídeo no celular ou uma
        resposta pronta no WhatsApp. Quem explica bem chega na visita com o cliente já confiando.</p>

        <h2>6. Divulgue com mais força quando a conta de luz pesa</h2>
        <p>A ANEEL define todo mês a
        <a href="https://www.gov.br/aneel/pt-br/assuntos/tarifas/bandeiras-tarifarias" target="_blank" rel="noopener noreferrer">bandeira tarifária</a>
        que indica se a energia vai custar mais. Meses de bandeira mais cara e de calor tendem a ser quando muita gente
        para para fazer a conta. Planeje para ter conteúdo pronto, perfil atualizado e verba de anúncio reservada
        para esses períodos.</p>

        <h2>7. Anuncie no Google por cidade, com uma página de simulação</h2>
        <p>Para quem já pesquisa instalação, o anúncio na pesquisa do Google é o atalho. Separe as campanhas por
        cidade atendida, bloqueie buscas de curso e vaga e leve o clique para uma
        {link('/criacao-de-landing-page/', 'landing page')} que pede a conta de luz. Há um
        {link('/modelos/landing-page-energia-solar/', 'modelo demonstrativo')} para você ver como fica. O passo a
        passo dos anúncios está em {link('/trafego-pago-para-energia-solar/', 'tráfego pago para energia solar')}.</p>

        <h2>8. Apareça onde a sua cidade se reúne</h2>
        <p>Associação comercial, sindicato rural, cooperativa, feira de agronegócio, grupo de empresários: são
        lugares onde uma conversa de dez minutos explicando como funciona a geração própria vale mais do que um
        panfleto. Leve obras reais no celular e saia com contatos para visita.</p>

        <h2>9. Use o WhatsApp com consentimento, não como spam</h2>
        <p>Lista de transmissão funciona para quem pediu para receber: clientes, interessados que fizeram
        simulação, parceiros. Mande conteúdo útil — obra nova na região, dúvida respondida — e não disparos em
        massa para números comprados. Além de afastar o cliente, uso de dados sem base legal esbarra na
        <a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" target="_blank" rel="noopener noreferrer">LGPD (Lei 13.709/2018)</a>.</p>

        <h2>10. Fale a verdade sobre economia</h2>
        <p>"Conta de luz zerada" chama atenção, mas pode ser lida como publicidade enganosa, que o
        <a href="https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm" target="_blank" rel="noopener noreferrer">Código de Defesa do Consumidor</a>
        proíbe no art. 37. A divulgação que dura convida para a simulação, onde a economia real de cada cliente
        aparece. Isso protege a empresa e atrai quem está realmente pronto para fechar.</p>

        {tabela(
            ["Ideia", "Custo", "Quando dá resultado"],
            [
                ["Obras reais e avaliações", "Baixo: tempo da equipe", "Semanas, e acumula"],
                ["Parcerias e indicação", "Baixo: comissão combinada", "Meses, e fica estável"],
                ["Conteúdo que responde dúvidas", "Baixo a médio", "Meses, pelo Google"],
                ["Anúncio no Google com landing page", "Verba paga ao Google", "Dias, enquanto a verba roda"],
            ])}

        <h2>Por onde começar a divulgar a sua empresa de energia solar?</h2>
        <p>Se você só pode fazer três coisas agora, comece por fotos de obras e avaliações no Google Perfil da
        Empresa, uma parceria local e um anúncio no Google para a cidade onde você mais instala. Os canais que
        trazem pedido de orçamento estão detalhados em
        {link('/blog/como-conseguir-clientes-energia-solar/', 'como conseguir clientes de energia solar')}, e as
        quatro frentes juntas em {link('/marketing-para-energia-solar/', 'marketing para empresas de energia solar')}.</p>
""",
        "faq": [
            ("Qual a forma mais barata de divulgar energia solar?",
             "Fotos de obras reais e avaliações no Google Perfil da Empresa, parcerias com quem já fala com o seu "
             "cliente e indicação organizada. Custam mais tempo do que dinheiro e o resultado acumula."),
            ("Posso usar foto da casa do cliente na divulgação?",
             "Pode, com autorização dele, de preferência por escrito. Evite mostrar endereço ou detalhes que "
             "identifiquem a casa sem permissão."),
            ("Vale a pena divulgar energia solar no Instagram?",
             "Vale para mostrar obras e gerar lembrança na sua região. Para quem já procura orçamento, o Google "
             "costuma trazer pedidos mais prontos para fechar."),
            ("Posso mandar mensagem no WhatsApp para uma lista de contatos?",
             "Só para quem autorizou receber, como clientes e interessados que fizeram simulação. Disparo para "
             "números comprados afasta o cliente e pode esbarrar na LGPD."),
        ],
        "cta": ("Tem uma empresa de energia solar e quer divulgar do jeito certo? Me conte as cidades onde você "
                "instala. Em até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho uma empresa de energia solar e quero divulgar melhor. Pode me ajudar?"),
                "Quero divulgar minha empresa"),
    },

    # ------------------------------------------------------------------ 3
    {
        "slug": "trafego-pago-para-clinicas",
        "h1": "Tráfego pago para clínicas: Google Ads e Meta Ads dentro das regras",
        "title": "Tráfego pago para clínicas: Google Ads e Meta Ads",
        "desc": ("Tráfego pago para clínicas e consultórios: como anunciar no Google e no Instagram dentro das "
                 "regras do CFM e do CFO, sem queimar verba e sem risco ao registro."),
        "cat": "Clínicas",
        "data": DATA,
        "trilha_extra": ("/gestao-de-trafego-pago/", "Tráfego pago"),
        "corpo": f"""
        <p>Tráfego pago para clínicas funciona quando junta três coisas: <strong>anúncio no Google para quem já
        procura o tratamento</strong>, <strong>anúncio no Instagram para gerar demanda na sua região</strong> e
        <strong>respeito às regras de publicidade do seu conselho</strong>. Clínica que anuncia como loja — com
        promessa de resultado, preço em destaque e antes e depois sem cuidado — corre risco no conselho e ainda
        atrai o paciente errado.</p>

        <p>A boa notícia é que dá para anunciar bem dentro das regras. O anúncio de clínica que mais converte não
        é o mais agressivo: é o que responde à dúvida do paciente e passa segurança.</p>

        {caixa('<p><strong>Em resumo:</strong> use o Google Ads para buscas como "implante dentário em Goiânia" ou '
               '"dermatologista perto de mim"; use o Instagram para apresentar a clínica e os tratamentos para quem '
               'mora perto; leve cada anúncio para uma página específica do tratamento; e revise tudo contra as '
               'regras do seu conselho antes de publicar.</p>')}

        <h2>O que as regras de publicidade permitem e o que proíbem</h2>
        <p>Médicos seguem a Resolução CFM nº 2.336/2023, que atualizou as regras de publicidade médica — o texto
        está no <a href="https://portal.cfm.org.br/" target="_blank" rel="noopener noreferrer">portal do CFM</a>.
        Dentistas seguem o Código de Ética Odontológica e as resoluções do
        <a href="https://website.cfo.org.br/" target="_blank" rel="noopener noreferrer">CFO</a>. Os detalhes
        mudam por conselho, mas alguns pontos se repetem:</p>
        <ul>
          <li><strong>Sem promessa de resultado.</strong> "Sorriso perfeito em 7 dias" ou "emagreça 10 kg" é
          problema. Informe o tratamento, não garanta o desfecho.</li>
          <li><strong>Cuidado com antes e depois.</strong> As regras atuais permitem em situações específicas e
          com critérios. Na dúvida, consulte a norma do seu conselho antes de usar.</li>
          <li><strong>Identificação do responsável técnico</strong>, com número de registro, onde a norma exige.</li>
          <li><strong>Sem sensacionalismo e sem desconto como chamariz</strong> de procedimento.</li>
        </ul>
        <p>Além do conselho, o próprio Google e o Meta têm políticas para anúncios de saúde, e alguns termos e
        tratamentos têm restrição. Uma campanha bem montada já nasce respeitando as duas camadas.</p>

        <h2>Google Ads: o paciente que já está procurando</h2>
        <p>Quem pesquisa "clareamento dental em Goiânia" ou "clínica de fisioterapia perto de mim" já decidiu que
        precisa do tratamento — só falta escolher onde. É o anúncio que mais vira consulta. O trabalho está em:</p>
        <ul>
          <li>separar campanhas por tratamento, para saber qual traz paciente;</li>
          <li>limitar o anúncio ao raio que o paciente realmente se desloca;</li>
          <li>bloquear buscas de "grátis", "SUS", "curso" e "vaga", que queimam verba;</li>
          <li>mandar o clique para a página do tratamento, não para a página inicial.</li>
        </ul>

        <h2>Meta Ads: apresentar a clínica para quem mora perto</h2>
        <p>No Instagram, o paciente não está procurando você. O anúncio precisa apresentar a clínica, o
        profissional e o tratamento de forma educativa — um vídeo curto explicando como funciona um procedimento
        costuma render mais do que uma arte com "agende já". O objetivo da campanha deve ser conversa no WhatsApp,
        e a recepção precisa estar pronta para responder rápido.</p>

        <h2>A página que recebe o clique</h2>
        <p>Anúncio de clínica levando para a página inicial desperdiça verba. O paciente que clicou em "implante"
        precisa cair numa página sobre implante: o que é, para quem é indicado, como é o tratamento, quem é o
        profissional, onde fica a clínica e um botão de WhatsApp. Uma
        {link('/criacao-de-landing-page/', 'landing page por tratamento')} costuma ser a mudança que mais
        melhora o resultado de quem já anuncia.</p>

        {tabela(
            ["Canal", "Melhor para", "Cuidado principal"],
            [
                ["Google Ads", "Paciente que já pesquisa o tratamento", "Bloquear buscas erradas e limitar o raio"],
                ["Meta Ads", "Apresentar a clínica para quem mora perto", "Conteúdo educativo, sem promessa"],
                ["Landing page", "Transformar clique em conversa", "Uma página por tratamento"],
            ])}

        <h2>Quanto investir em anúncio de clínica</h2>
        <p>A verba certa depende de quanto vale um paciente novo para a sua clínica e de quanto custa o clique na
        sua especialidade e na sua cidade. Tratamentos de valor alto — implante, lente, harmonização, cirurgia —
        costumam suportar um custo por contato maior do que consultas simples, e por isso a conta fecha mais
        rápido.</p>
        <p>O caminho mais seguro é começar concentrado: um tratamento, um canal, uma página. Medir quantas
        conversas vieram e quantas viraram consulta nas primeiras semanas, e só então ampliar para outros
        tratamentos. Clínica que começa anunciando tudo ao mesmo tempo, com pouca verba, não descobre o que
        funciona. O passo a passo da conta está em
        {link('/blog/quanto-investir-em-trafego-pago/', 'quanto investir em tráfego pago')}.</p>
        <p>Um detalhe que pesa mais do que parece: o tempo de resposta da recepção. O paciente que chama pelo
        anúncio costuma chamar outras clínicas também. Responder em minutos, com a informação que ele pediu e uma
        sugestão de horário, é o que transforma o clique pago em consulta marcada. De nada adianta um anúncio
        bem feito se a mensagem fica sem resposta até o dia seguinte.</p>

        <h2>Tráfego pago e Google orgânico andam juntos</h2>
        <p>O anúncio traz paciente enquanto você paga. O {link('/seo-para-clinicas/', 'trabalho no Google orgânico')}
        e no Perfil da Empresa continua trazendo paciente depois. Clínicas que fazem os dois dependem menos da
        verba de anúncio com o passar dos meses. Se você quer ajuda com as campanhas, veja como funciona a
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')} — e, para consultório
        odontológico, o {link('/trafego-pago-para-dentistas/', 'tráfego pago para dentistas')}.</p>
""",
        "faq": [
            ("Clínica pode anunciar no Google e no Instagram?",
             "Pode, desde que respeite as regras de publicidade do seu conselho — CFM para médicos, CFO para "
             "dentistas — e as políticas de anúncios de saúde do Google e do Meta. O ponto principal é não prometer "
             "resultado."),
            ("Posso usar foto de antes e depois no anúncio?",
             "Depende do seu conselho. As regras atuais permitem em situações específicas e com critérios. "
             "Consulte a norma do seu conselho antes de usar, e prefira conteúdo educativo."),
            ("Google Ads ou Instagram: qual é melhor para clínica?",
             "Para agenda cheia no curto prazo, o Google Ads costuma trazer pacientes mais decididos, porque atinge "
             "quem já pesquisa o tratamento. O Instagram é bom para apresentar a clínica e gerar demanda na região."),
            ("Por que meu anúncio de clínica tem cliques e não tem agendamento?",
             "Normalmente por três motivos: o anúncio leva para a página inicial em vez da página do tratamento, as "
             "buscas não foram filtradas, ou a recepção demora para responder no WhatsApp."),
        ],
        "cta": ("Quer anunciar a sua clínica sem queimar verba e sem risco no conselho? Me conte os tratamentos e a "
                "região. Em até 24 horas você recebe o orçamento e uma análise dos anúncios da concorrência.",
                wa("Olá, Renan! Tenho uma clínica e quero um orçamento de tráfego pago."),
                "Quero anunciar minha clínica"),
    },

    # ------------------------------------------------------------------ 4
    {
        "slug": "quanto-investir-em-trafego-pago",
        "h1": "Quanto investir em tráfego pago para ter resultado",
        "title": "Quanto investir em tráfego pago? Como calcular a verba",
        "desc": ("Quanto investir em tráfego pago: como calcular a verba do Google Ads e do Meta Ads a partir do "
                 "valor do seu cliente, e quanto tempo esperar para julgar."),
        "cat": "Tráfego pago",
        "data": DATA,
        "trilha_extra": ("/gestao-de-trafego-pago/", "Tráfego pago"),
        "corpo": f"""
        <p>Não existe um valor certo de investimento em tráfego pago que sirva para todo mundo. A verba ideal é
        calculada de trás para frente: <strong>quanto vale um cliente para você</strong>, <strong>quanto custa um
        clique no seu ramo e na sua cidade</strong> e <strong>quantos cliques costumam virar conversa</strong>. Com
        esses três números dá para começar pequeno, medir e aumentar só o que dá retorno.</p>

        <p>O erro mais comum é o oposto: escolher um valor redondo ("vou colocar um pouco por mês e ver o que dá"),
        espalhar em várias campanhas e desistir em duas semanas dizendo que anúncio não funciona.</p>

        {caixa('<p><strong>Resposta rápida:</strong> comece com uma verba que permita juntar cliques suficientes '
               'para aprender — em geral, algumas dezenas de cliques por semana na campanha principal. Concentre em '
               'um canal e um serviço, meça quantas conversas vieram e quanto custou cada uma, e só então aumente. '
               'A verba é paga direto ao Google ou ao Meta; a gestão é outro valor.</p>')}

        <h2>Verba e gestão: dois dinheiros diferentes</h2>
        <p>A <strong>verba do anúncio</strong> vai direto para o Google ou para o Meta, no seu cartão. A
        <strong>gestão</strong> é o trabalho de montar, acompanhar e ajustar as campanhas. Separar os dois evita a
        confusão mais comum: achar que o valor da agência já inclui o anúncio, ou achar que gastar mais verba
        resolve campanha mal montada.</p>

        <h2>Como calcular quanto investir em tráfego pago a partir do seu cliente</h2>
        <p>Faça a conta com os seus números. O exemplo abaixo usa valores hipotéticos, só para mostrar o raciocínio:</p>
        {tabela(
            ["Pergunta", "Exemplo (hipotético)", "Onde achar o seu número"],
            [
                ["Quanto você lucra com um cliente novo?", "R$ 800", "Seu ticket menos o custo do serviço"],
                ["Quanto custa um clique no seu ramo?", "R$ 3", "Planejador de palavras-chave do Google Ads"],
                ["De cada 100 cliques, quantos chamam no WhatsApp?", "8", "Medição da página e do botão"],
                ["De cada 10 conversas, quantas fecham?", "2", "Seu histórico de atendimento"],
            ],
            "Exemplo: 100 cliques custam R$ 300, geram 8 conversas e cerca de 1 a 2 clientes. Com lucro de R$ 800 "
            "por cliente, a conta fecha. Com os seus números reais, o resultado pode ser outro.")}
        <p>Se a conta não fecha no papel, aumentar a verba não resolve. O caminho é melhorar a taxa de conversa —
        com uma {link('/criacao-de-landing-page/', 'página melhor')} e resposta mais rápida no WhatsApp — ou
        escolher buscas mais próximas da compra.</p>

        <h2>O que faz o custo do clique subir ou descer</h2>
        <ul>
          <li><strong>Concorrência no seu ramo:</strong> advocacia, saúde e reforma costumam ter clique mais caro
          que comércio de bairro.</li>
          <li><strong>Região:</strong> anunciar para a cidade inteira custa mais do que para o raio que o cliente
          realmente se desloca.</li>
          <li><strong>Qualidade do anúncio e da página:</strong> o Google tende a cobrar menos de quem entrega uma
          página relevante para a busca.</li>
          <li><strong>Buscas bloqueadas:</strong> cada busca errada que você bloqueia é verba que sobra para as
          certas.</li>
        </ul>

        <h2>Google Ads ou Meta Ads: onde colocar a primeira verba</h2>
        <p>Para negócio local com serviço que as pessoas pesquisam — dentista, advogado, energia solar, conserto —,
        a primeira verba costuma render mais no Google Ads, porque atinge quem já está procurando. O Meta Ads é
        melhor para gerar demanda, lançar oferta e para produtos que a pessoa compra por impulso. Começar com um
        canal e fazer ele funcionar é melhor do que dividir pouco dinheiro em dois.</p>
        <p>A mesma lógica vale dentro do canal: cada campanha precisa de verba suficiente para juntar dados. Cinco
        campanhas com pouco dinheiro cada uma demoram muito mais para mostrar o que funciona do que uma campanha
        bem abastecida no serviço que mais dá lucro.</p>

        <h2>Erros que fazem a verba acabar sem trazer cliente</h2>
        <ul>
          <li><strong>Usar o "impulsionar" do Instagram como estratégia.</strong> Ele otimiza para alcance e
          curtida, não para conversa. Para trazer cliente, a campanha precisa ter objetivo de mensagem ou de
          contato.</li>
          <li><strong>Deixar o Google escolher tudo sozinho.</strong> Campanha automática sem lista de buscas
          bloqueadas paga clique de quem procura emprego, curso ou produto grátis.</li>
          <li><strong>Anunciar para a cidade inteira.</strong> Se o cliente não atravessa a cidade para ir até
          você, anunciar para ela toda só encarece o clique.</li>
          <li><strong>Levar o anúncio para a página inicial.</strong> A pessoa que clicou num serviço precisa
          cair numa página sobre aquele serviço.</li>
          <li><strong>Não medir o WhatsApp.</strong> Sem saber quantas conversas vieram de cada campanha, a
          decisão de aumentar ou cortar verba vira palpite.</li>
        </ul>

        <h2>Quanto tempo esperar antes de julgar</h2>
        <p>As primeiras semanas são de aprendizado: a plataforma testa públicos, e a gestão bloqueia buscas erradas e
        ajusta lances. Julgar a campanha em poucos dias costuma levar a decisão errada. O que dá para cobrar desde o
        começo é medição: quantas conversas vieram, de qual campanha e quanto custou cada uma.</p>

        <p>Se você quer ajuda para calcular a verba do seu caso e montar a primeira campanha, veja como funciona a
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}. E se ainda está decidindo entre anúncio
        e Google orgânico, leia {link('/blog/seo-ou-trafego-pago-empresa-local/', 'SEO ou tráfego pago para empresa local')}.</p>
""",
        "faq": [
            ("Quanto devo investir em tráfego pago no começo?",
             "O suficiente para juntar cliques que permitam aprender — em geral algumas dezenas por semana na "
             "campanha principal. Comece em um canal e um serviço, meça quantas conversas vieram e aumente só o "
             "que dá retorno. O valor exato depende do custo do clique no seu ramo e na sua cidade."),
            ("A verba do anúncio está incluída no valor da gestão?",
             "Não. A verba é paga direto ao Google ou ao Meta, no seu cartão. A gestão é o trabalho de montar e "
             "acompanhar as campanhas, cobrado à parte."),
            ("Quanto tempo leva para o tráfego pago dar resultado?",
             "Os primeiros contatos podem vir nos primeiros dias, mas as primeiras semanas são de aprendizado e "
             "ajuste. Julgar a campanha cedo demais costuma levar a decisão errada."),
            ("Se eu aumentar a verba, vou ter mais clientes?",
             "Só se a campanha já estiver convertendo. Se a conta não fecha — muitos cliques, poucas conversas —, "
             "o problema está na página, nas buscas ou no atendimento, e mais verba só aumenta o prejuízo."),
        ],
        "cta": ("Quer saber quanto investir em anúncio no seu caso? Me conte o que você vende e quanto vale um cliente "
                "para você. Em até 24 horas eu te mando uma sugestão de verba inicial e o orçamento da gestão.",
                wa("Olá, Renan! Quero saber quanto investir em tráfego pago no meu negócio."),
                "Quero calcular minha verba"),
    },

    # ------------------------------------------------------------------ limpeza: conseguir clientes
    # Etapa 6 do plano de nichos (04/10/2026). Busca do DONO: "como conseguir clientes para empresa
    # de limpeza". Fonte: ajuda do Perfil da Empresa (area de cobertura).
    {
        "slug": "como-conseguir-clientes-para-empresa-de-limpeza",
        "h1": "Como conseguir clientes para empresa de limpeza: condomínios, empresas e contrato mensal",
        "title": "Como conseguir clientes para empresa de limpeza",
        "desc": ("Como conseguir clientes para empresa de limpeza: onde estão os contratos mensais, como chegar a "
                 "síndicos e empresas e a proposta que fecha o negócio."),
        "cat": "Limpeza e terceirização",
        "data": "2026-10-04",
        "trilha_extra": ("/marketing-para-empresa-de-limpeza/", "Marketing para empresa de limpeza"),
        "corpo": f"""
        <p>Para conseguir clientes para uma empresa de limpeza, o caminho mais seguro é mirar o contrato mensal —
        condomínios, escritórios, clínicas, lojas — e estar onde quem decide esse contrato procura: no Google, no
        mapa da região e na indicação de quem já confia em você. Faxina avulsa ajuda no caixa, mas é o contrato
        recorrente que dá estabilidade para a empresa crescer.</p>

        {caixa('<p><strong>Resposta rápida:</strong> escolha o tipo de cliente que você quer (condomínio ou '
               'empresa), apareça no Google Meu Negócio com a área que atende, tenha uma página para cada serviço, '
               'responda o pedido de proposta no mesmo dia e mande uma proposta clara, com rotina, equipe e '
               'supervisão.</p>')}

        <h2>1. Decida qual cliente sustenta a sua empresa</h2>
        <p>Condomínio, escritório e casa de família são clientes diferentes. O condomínio decide em assembleia e
        compara propostas; a empresa decide pelo gerente administrativo e quer alguém que não dê trabalho; a casa
        de família decide rápido, mas troca fácil. Escolher o foco muda o texto do site, do anúncio e até o
        uniforme da equipe. Quem tenta falar com todo mundo ao mesmo tempo acaba não convencendo ninguém.</p>

        <h2>2. Condomínios: chegue ao síndico e à administradora</h2>
        <p>Em condomínio, quem pesquisa e indica costuma ser o síndico ou a administradora. Por isso vale ter uma
        página no site só para condomínios, explicando a rotina de limpeza das áreas comuns, a supervisão e o que
        acontece quando alguém da equipe falta. Administradoras de condomínio cuidam de vários prédios ao mesmo
        tempo — um bom relacionamento com uma delas pode abrir mais de um contrato.</p>

        <h2>3. Empresas: fale com quem resolve o problema do dia a dia</h2>
        <p>Escritórios, clínicas, academias e lojas contratam limpeza para não ter dor de cabeça. O gerente quer
        saber se a equipe chega no horário, se é sempre a mesma pessoa, se há supervisão e se a empresa cuida das
        obrigações com os funcionários. Mostre isso no site e na proposta, com clareza, e você sai da disputa só
        por preço.</p>

        <h2>4. Apareça no Google Meu Negócio com a área que você atende</h2>
        <p>Empresa de limpeza vai até o cliente. A ajuda do Google sobre
        <a href="https://support.google.com/business/answer/9157481?hl=pt-BR" target="_blank" rel="noopener noreferrer">áreas de cobertura</a>
        usa justamente os prestadores de serviços de limpeza como exemplo de empresa de serviço local: o perfil
        mostra a região atendida, e o endereço deve sair se você não recebe clientes nele. Com área, serviços,
        fotos da equipe e avaliações, a empresa passa a aparecer para quem procura no bairro. Veja a
        {link('/google-perfil-empresa/', 'otimização do Google Perfil da Empresa')}.</p>

        <h2>5. Tenha uma página para cada serviço</h2>
        <p>Limpeza de condomínio, limpeza de escritório, limpeza pós-obra e terceirização de equipe são buscas
        diferentes. Cada uma merece a sua página, com o que está incluído, como funciona a rotina e um botão para
        pedir proposta. É isso que faz o Google entender o que você faz e mostrar a página certa para cada busca.</p>

        <h2>6. Monte uma proposta que facilite o "sim"</h2>
        <p>Quem compara três propostas escolhe a mais clara, não só a mais barata. Uma boa proposta de limpeza
        traz: escopo (o que é limpo e com que frequência), quantidade de pessoas e horários, quem supervisiona,
        como é a reposição de faltas, quem fornece os materiais, prazo para começar e as condições do contrato.
        Para o síndico, uma versão fácil de apresentar na assembleia ajuda muito.</p>

        <h2>7. Anuncie para quem já quer terceirizar</h2>
        <p>Buscas como "terceirização de limpeza para empresas" ou "empresa de limpeza de condomínio" vêm de quem
        está perto de decidir. Um anúncio no Google bem montado coloca você na frente dessa pessoa — com um cuidado
        essencial: bloquear as buscas de vaga de emprego, muito comuns nesse ramo. Veja como funciona a
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>

        <h2>8. Responda o pedido de proposta no mesmo dia</h2>
        <p>Quem pede proposta de limpeza normalmente pede para mais de uma empresa. Responder rápido, marcar a
        visita técnica e mandar a proposta no prazo combinado já coloca você na frente de boa parte da
        concorrência.</p>

        <h2>9. Cuide de quem já é cliente para ganhar o próximo</h2>
        <p>O cliente que você já tem é a melhor fonte do próximo contrato. Um síndico satisfeito comenta com o
        síndico do prédio vizinho; um gerente que muda de empresa leva o fornecedor de confiança junto. Para isso
        acontecer, o serviço precisa ser visível: uma conversa curta todo mês para saber se está tudo certo, um
        canal direto para reclamações e a resposta rápida quando algo sai do combinado.</p>
        <p>Vale também registrar o que foi feito — um relatório simples com as rotinas cumpridas, as
        substituições de equipe e os ajustes pedidos. Ele ajuda na renovação do contrato, mostra profissionalismo
        para a próxima assembleia e vira argumento quando você pede uma avaliação ou uma indicação.</p>

        {tabela(
            ["Cliente", "Quem decide", "O que precisa ver"],
            [
                ["Condomínio", "Síndico, conselho e administradora", "Rotina, supervisão e reposição de faltas"],
                ["Escritório e comércio", "Gerente administrativo ou dono", "Pontualidade, equipe fixa e obrigações em dia"],
                ["Pós-obra", "Construtora ou dono do imóvel", "Prazo de entrega e acabamento"],
            ])}

        <h2>Por onde começar a conseguir clientes de limpeza?</h2>
        <p>Comece pelo perfil no Google com a área de atendimento e por uma página para o seu cliente principal,
        condomínio ou empresa. Depois, organize a proposta e, se quiser pedidos mais rápido, um anúncio no Google.
        As frentes juntas estão em {link('/marketing-para-empresa-de-limpeza/', 'marketing para empresas de limpeza')},
        e ideias práticas em {link('/blog/como-divulgar-empresa-de-limpeza/', 'como divulgar empresa de limpeza')}.</p>
""",
        "faq": [
            ("Qual o melhor cliente para empresa de limpeza?",
             "Para estabilidade, o contrato mensal: condomínios, escritórios, clínicas e lojas. Faxina avulsa ajuda no "
             "caixa, mas troca de fornecedor com facilidade."),
            ("Como conseguir contrato de limpeza com condomínio?",
             "Estar no Google quando o síndico pesquisa, ter uma página para condomínios explicando rotina e "
             "supervisão, cultivar relação com administradoras e mandar uma proposta clara para a assembleia."),
            ("Vale a pena anunciar empresa de limpeza no Google?",
             "Vale para quem procura terceirizar ou contratar limpeza de condomínio e escritório, desde que as buscas "
             "de vaga de emprego sejam bloqueadas."),
            ("O que colocar na proposta de limpeza?",
             "Escopo e frequência, equipe e horários, supervisão, reposição de faltas, materiais, prazo para começar e "
             "condições do contrato."),
        ],
        "cta": ("Tem uma empresa de limpeza e quer mais contratos mensais? Me conte as cidades que você atende e o "
                "tipo de cliente. Em até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho uma empresa de limpeza e quero conseguir mais clientes. Pode me ajudar?"),
                "Quero mais clientes de limpeza"),
    },

    # ------------------------------------------------------------------ limpeza: divulgar
    # Etapa 6 do plano de nichos (04/10/2026). Busca do DONO: "como divulgar minha empresa de limpeza".
    {
        "slug": "como-divulgar-empresa-de-limpeza",
        "h1": "Como divulgar empresa de limpeza: 10 ideias para fechar mais contratos",
        "title": "Como divulgar empresa de limpeza: 10 ideias práticas",
        "desc": ("Como divulgar empresa de limpeza: 10 ideias práticas para o dono — equipe identificada, antes e "
                 "depois, parcerias, avaliações e anúncio no Google."),
        "cat": "Limpeza e terceirização",
        "data": "2026-10-04",
        "trilha_extra": ("/marketing-para-empresa-de-limpeza/", "Marketing para empresa de limpeza"),
        "corpo": f"""
        <p>Para divulgar uma empresa de limpeza, o dono precisa mostrar duas coisas que o cliente não vê antes de
        contratar: que a equipe é de confiança e que o serviço é bem feito. As ideias abaixo fazem isso de forma
        prática, sem depender de verba alta, e todas levam o interessado a pedir uma proposta.</p>

        {caixa('<p><strong>Resposta rápida:</strong> identifique a equipe e o carro, mostre antes e depois (com '
               'autorização), peça avaliações a clientes empresariais, faça parceria com administradoras, '
               'imobiliárias e construtoras, tenha uma apresentação pronta para síndicos e anuncie no Google para '
               'quem já procura terceirizar.</p>')}

        <h2>1. Equipe e carro identificados</h2>
        <p>Uniforme com o nome da empresa e carro adesivado transformam cada atendimento em propaganda no
        condomínio e na rua. Além disso, passam segurança para quem abre a porta para a sua equipe.</p>

        <h2>2. Antes e depois de verdade</h2>
        <p>Limpeza pós-obra, limpeza pesada e higienização rendem fotos que falam sozinhas. Registre o antes e o
        depois, peça autorização ao cliente e publique no
        {link('/google-perfil-empresa/', 'Google Perfil da Empresa')} e no site. Foto real da sua equipe convence
        mais que imagem de banco.</p>

        <h2>3. Avaliações de clientes empresariais</h2>
        <p>Uma avaliação no Google de um síndico ou de um gerente de escritório pesa muito para o próximo gestor que
        está decidindo. Peça depois do primeiro mês de contrato, quando o cliente já viu a rotina funcionando, e
        responda a todas.</p>

        <h2>4. Parceria com administradoras de condomínio</h2>
        <p>Administradoras cuidam de vários prédios e são consultadas pelos síndicos. Apresente a empresa, deixe
        material com a forma de trabalho e combine por escrito como funciona a indicação.</p>
        <p>A parceria só dura se a administradora não passar vergonha com a indicação. Atenda o primeiro condomínio
        indicado com cuidado redobrado, mantenha o síndico informado e avise a administradora quando o contrato
        começar. Um retorno simples, como "começamos segunda e está tudo certo", mostra que indicar você é seguro.</p>

        <h2>5. Parceria com imobiliárias e construtoras</h2>
        <p>Imobiliária precisa de limpeza na troca de inquilino; construtora precisa de limpeza pós-obra para
        entregar o imóvel. Os dois são fontes de serviço recorrente para quem responde rápido e entrega no prazo.
        Combine antes como o pedido chega, quem libera a chave e em quanto tempo o imóvel fica pronto — é essa
        previsibilidade que faz o parceiro voltar a chamar você.</p>

        <h2>6. Apresentação pronta para síndicos</h2>
        <p>Um material curto — quem é a empresa, como funciona a rotina, supervisão, reposição de faltas e
        contatos — facilita a vida do síndico que precisa levar a proposta para a assembleia. Quem facilita a
        decisão costuma ser escolhido.</p>

        <h2>7. Uma página para cada serviço no site</h2>
        <p>Limpeza de condomínio, de escritório, pós-obra e terceirização de equipe são buscas diferentes no Google.
        Cada página bem feita é uma porta de entrada a mais. As frentes juntas estão em
        {link('/marketing-para-empresa-de-limpeza/', 'marketing para empresas de limpeza')}.</p>

        <h2>8. Anúncio no Google para quem já quer terceirizar</h2>
        <p>Para quem pesquisa "terceirização de limpeza" ou "empresa de limpeza para escritório", o anúncio na
        pesquisa do Google coloca você na frente na hora da decisão. Bloqueie as buscas de vaga de emprego e leve o
        clique para uma página de pedido de proposta. Detalhes na
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>

        <h2>9. Associação comercial e grupos do bairro</h2>
        <p>Associação comercial, grupos de empresários e eventos do bairro aproximam você de donos de comércio e
        escritório — exatamente quem contrata limpeza mensal. Leve a apresentação e saia com visitas marcadas.</p>

        <h2>10. WhatsApp com consentimento, não como spam</h2>
        <p>Use a lista de transmissão para quem pediu para receber: clientes e interessados que já pediram
        proposta. Disparo para números comprados afasta o cliente e, sem base legal para usar os dados, esbarra na
        <a href="https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm" target="_blank" rel="noopener noreferrer">LGPD (Lei 13.709/2018)</a>.</p>

        <h2>O que evitar ao divulgar uma empresa de limpeza?</h2>
        <p>Alguns atalhos parecem baratos, mas custam caro depois. O primeiro é competir só por preço: quem anuncia
        "a limpeza mais barata da cidade" atrai o cliente que troca de fornecedor por qualquer diferença e deixa de
        fora o síndico que procura estabilidade. Fale de rotina, supervisão e reposição de faltas, que é o que o
        gestor quer saber.</p>
        <p>O segundo é prometer o que a operação não sustenta, como atender qualquer bairro no mesmo dia ou montar
        equipe para amanhã. Uma falha no primeiro mês apaga o efeito de toda a divulgação. O terceiro é usar fotos de
        banco de imagem ou de outra empresa: o cliente percebe, e a confiança — que é exatamente o que você precisa
        provar — vai embora.</p>
        <p>Por fim, não espalhe a divulgação em canais demais ao mesmo tempo. É melhor manter o perfil no Google
        atualizado, o site claro e duas parcerias ativas do que abrir dez frentes e abandonar todas no segundo
        mês.</p>

        {tabela(
            ["Ideia", "Custo", "Melhor para"],
            [
                ["Equipe e carro identificados", "Baixo, uma vez", "Ser lembrado no bairro"],
                ["Antes e depois e avaliações", "Tempo da equipe", "Convencer quem está comparando"],
                ["Parcerias", "Comissão combinada", "Serviço recorrente"],
                ["Anúncio no Google", "Verba paga ao Google", "Pedidos de proposta rápidos"],
            ])}

        <h2>Por onde começar a divulgar a sua empresa de limpeza?</h2>
        <p>Se for para fazer três coisas agora: perfil no Google com fotos e avaliações, uma parceria com uma
        administradora ou imobiliária e a apresentação pronta para síndicos. Para entender onde estão os contratos
        mensais e como fechar, leia
        {link('/blog/como-conseguir-clientes-para-empresa-de-limpeza/', 'como conseguir clientes para empresa de limpeza')}.</p>
""",
        "faq": [
            ("Qual a forma mais barata de divulgar empresa de limpeza?",
             "Equipe e carro identificados, fotos de antes e depois com autorização, avaliações no Google e parcerias "
             "com administradoras e imobiliárias. Custam pouco e o resultado acumula."),
            ("Vale a pena panfletar para divulgar limpeza?",
             "Pode ajudar no bairro, mas o contrato mensal costuma vir de quem pesquisa no Google ou recebe indicação. "
             "Priorize perfil no Google, site e parcerias."),
            ("Posso postar foto do serviço feito na casa ou na empresa do cliente?",
             "Pode, com autorização do cliente. Evite mostrar endereço, documentos ou pessoas sem permissão."),
            ("Como divulgar para síndicos?",
             "Com uma apresentação curta e clara, presença no Google quando ele pesquisa e relacionamento com as "
             "administradoras de condomínio."),
        ],
        "cta": ("Tem uma empresa de limpeza e quer divulgar do jeito certo? Me conte as cidades que você atende. Em "
                "até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho uma empresa de limpeza e quero divulgar melhor. Pode me ajudar?"),
                "Quero divulgar minha empresa"),
    },

    # ------------------------------------------------------------------ advocacia: conseguir clientes
    # Etapa 8 do plano de nichos (05/10/2026). Busca do DONO: "como conseguir clientes na advocacia".
    # Fonte unica das regras: Provimento 205/2021 do CFOAB e seu Anexo Unico (lidos em 05/10/2026).
    # O Renan e bacharel em Direito, nao advogado.
    {
        "slug": "como-conseguir-clientes-na-advocacia",
        "h1": "Como conseguir clientes na advocacia sem ferir as regras da OAB",
        "title": "Como conseguir clientes na advocacia dentro da OAB",
        "desc": ("Como conseguir clientes na advocacia dentro do Provimento 205/2021: Google Meu Negócio, página por "
                 "área de atuação, conteúdo, Google Ads e indicação."),
        "cat": "Advocacia",
        "data": "2026-10-05",
        "trilha_extra": ("/marketing-para-advogados/", "Marketing para advogados"),
        "corpo": f"""
        <p>Para conseguir clientes na advocacia sem ferir as regras da OAB, o caminho é ser encontrado por quem já
        está procurando ajuda — e não correr atrás de quem não pediu. A pessoa com um problema jurídico pesquisa no
        Google antes de ligar para qualquer escritório; quem aparece ali, com informação clara e sóbria, entra na
        conversa. É o que o {PROV_205} chama de marketing de conteúdos jurídicos.</p>

        {caixa('<p><strong>Resposta rápida:</strong> escolha as áreas e a região onde quer crescer, complete o '
               'Google Meu Negócio do escritório, tenha uma página para cada área de atuação, publique conteúdo que '
               'explica direitos sem prometer resultado, use o Google Ads só para quem já pesquisa o tema e responda '
               'o primeiro contato no mesmo dia.</p>')}

        <h2>1. Por que a indicação sozinha deixa de bastar?</h2>
        <p>Indicação continua sendo a melhor fonte de cliente na advocacia, porque chega com confiança. O problema é
        que ela cresce até onde a sua rede alcança — e depois para. Além disso, até o cliente indicado pesquisa o nome
        do advogado no Google antes da primeira conversa. Se ele não encontra nada, ou encontra um perfil abandonado,
        a indicação perde força. Aparecer bem no Google não substitui a indicação: dá a ela um lugar para pousar.</p>

        <h2>2. Escolha as áreas e a região que você quer fazer crescer</h2>
        <p>"Atuação em todas as áreas do Direito" não responde nenhuma pesquisa. Quem tem um problema procura algo
        específico: "advogado trabalhista", "inventário extrajudicial", "revisão de aposentadoria". Escolha as duas ou
        três áreas que você quer fazer crescer e a região onde atende. Essa decisão orienta tudo o que vem depois: o
        perfil no Google, as páginas do site, os artigos e o anúncio.</p>

        <h2>3. Complete o Google Meu Negócio do escritório</h2>
        <p>O perfil do escritório no Google é o que aparece no mapa quando alguém pesquisa advogado na região. Nome
        correto, endereço, horário, telefone, fotos do escritório e da equipe — que o art. 5º, § 2º, do Provimento
        permite — e a descrição das áreas de atuação, em tom informativo. Avaliações de clientes ajudam quem pesquisa
        a confiar; ao responder, nunca comente detalhes do caso, por causa do sigilo profissional. Veja a
        {link('/google-perfil-empresa/', 'otimização do Google Perfil da Empresa')}.</p>

        <h2>4. Tenha uma página para cada área de atuação</h2>
        <p>Cada área merece a sua página no site, explicando em linguagem simples o que a pessoa precisa saber antes
        de procurar um advogado: quais são os direitos, quais documentos costumam ser pedidos, quais prazos existem.
        É isso que faz o Google mostrar a página certa para cada pesquisa. Atenção ao art. 3º, III: sem título
        certificado ou notória especialização, a página fala em "área de atuação", não em "especialista". Veja a
        {link('/criacao-de-site-para-advogado/', 'criação de site para advogado')}.</p>

        <h2>5. Publique conteúdo que explica, não que vende</h2>
        <p>O Anexo Único do Provimento orienta que a criação de conteúdo, palestras e artigos tenha caráter técnico
        informativo, sem divulgação de resultados concretos, clientes, valores ou gratuidade. Na prática, funciona
        bem: um artigo que explica "quais são os direitos de quem foi demitido sem justa causa" responde exatamente o
        que a pessoa pesquisou e mostra que você entende do assunto, sem nenhuma frase de venda.</p>

        <h2>6. Anuncie só para quem já está procurando</h2>
        <p>O mesmo Anexo permite a aquisição de palavra-chave, a exemplo do Google Ads, quando o anúncio responde a
        uma busca iniciada pelo potencial cliente e as palavras escolhidas respeitam a ética. Ou seja: anunciar para
        quem pesquisou "advogado previdenciário" é possível; anúncio ostensivo em plataforma de vídeo, não. O anúncio
        leva para a página da área, com o mesmo tom informativo. Veja
        {link('/trafego-pago-para-advogados/', 'tráfego pago para advogados')}.</p>

        <h2>7. Responda o primeiro contato no mesmo dia</h2>
        <p>Quem tem um problema jurídico costuma falar com mais de um escritório. Responder rápido, com educação e
        dizendo quais documentos levar para a primeira conversa já coloca você na frente. O Anexo permite usar
        chatbot no site para responder as primeiras dúvidas ou encaminhar informações sobre a atuação do escritório —
        desde que não afaste a pessoalidade do atendimento nem substitua a decisão do advogado.</p>

        <h2>8. Cuide da rede de indicação, sem mala direta</h2>
        <p>Relacionamento continua valendo: colegas de outras áreas que encaminham casos, contadores, corretores e
        clientes antigos. O que o Anexo veda é o envio de cartas e comunicados a uma coletividade, a chamada mala
        direta; comunicações para clientes e pessoas do seu relacionamento, ou que pediram para receber, são
        possíveis, sem caráter mercantilista. Grupos de WhatsApp também são permitidos quando reúnem pessoas
        determinadas, das relações do advogado.</p>

        {tabela(
            ["Canal", "O que o Provimento diz", "Como usar"],
            [
                ["Google (busca orgânica)", "Publicidade passiva: atinge quem buscou (art. 2º, VII)", "Página por área de atuação"],
                ["Google Ads", "Permitido se responde a uma busca do potencial cliente (Anexo)", "Anúncio por área, sem promessa"],
                ["Artigos e vídeos", "Conteúdo técnico informativo, sem resultados, clientes ou valores (Anexo)", "Explicar direitos e prazos"],
                ["Redes sociais", "Presença permitida; impulsionar sem oferta de serviço (Anexo)", "Conteúdo educativo"],
                ["Mala direta", "Vedado o envio a uma coletividade (Anexo)", "Só para clientes e relacionamento"],
            ],
            "Resumo informativo do Provimento 205/2021 e do Anexo Único. Não substitui a leitura da norma nem a "
            "orientação da sua seccional.")}

        <h2>O que não fazer para conseguir clientes na advocacia?</h2>
        <p>Algumas táticas comuns no marketing de outros ramos são vedadas na advocacia: falar de honorários,
        gratuidade ou desconto como forma de captar cliente (art. 3º, I); usar expressões persuasivas, de
        autoengrandecimento ou de comparação (art. 3º, IV); prometer resultado ou usar caso concreto para oferecer
        serviço (art. 6º); pagar para aparecer em ranking ou prêmio (art. 5º, § 1º); e ostentar bens (art. 6º,
        parágrafo único). Fora o risco disciplinar, nenhuma delas é necessária para aparecer no Google.</p>

        <h2>Por onde começar a conseguir clientes na advocacia?</h2>
        <p>Comece pelo perfil do escritório no Google e por uma página para a área que você mais quer fazer crescer.
        Depois, publique os primeiros artigos dessa área e, se quiser contatos mais rápido, um anúncio no Google para
        quem pesquisa o tema. As frentes juntas estão em
        {link('/marketing-para-advogados/', 'marketing e SEO para advogados')}, e as regras em detalhe em
        {link('/blog/advogado-pode-fazer-marketing/', 'advogado pode fazer marketing?')}.</p>
        <p>Uma observação: sou bacharel em Direito e consultor de SEO, não advogado. Escrevo com o Provimento aberto,
        mas a responsabilidade pela publicidade é de quem está inscrito na OAB (art. 1º, § 1º).</p>
""",
        "faq": [
            ("Qual a melhor forma de conseguir clientes na advocacia?",
             "Combinar indicação com presença no Google: perfil do escritório completo, uma página por área de atuação "
             "e conteúdo informativo. Assim, quem pesquisa o problema encontra você."),
            ("Advogado pode anunciar no Google?",
             "Pode. O Anexo Único do Provimento 205/2021 permite a aquisição de palavra-chave, como no Google Ads, "
             "quando o anúncio responde a uma busca iniciada pelo potencial cliente e respeita a ética."),
            ("Posso dizer no site que a primeira consulta é gratuita?",
             "Não como forma de captar cliente: o art. 3º, I, do Provimento veda a referência a gratuidade, valores, "
             "forma de pagamento ou descontos com esse fim."),
            ("Advogado recém-formado consegue clientes pelo Google?",
             "Consegue, porque a disputa acontece por área de atuação e por região. Escolher bem a área e ter páginas "
             "claras sobre ela costuma pesar mais do que o tamanho do escritório."),
        ],
        "cta": ("É advogado e quer ser encontrado por quem procura a sua área? Me conte as áreas e a cidade. Em até "
                "24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Sou advogado(a) e quero conseguir mais clientes pelo Google, dentro da OAB."),
                "Quero ser encontrado no Google"),
    },

    # ------------------------------------------------------------------ advocacia: pode fazer marketing?
    # Etapa 8 do plano de nichos (05/10/2026). Busca do DONO: "advogado pode fazer marketing",
    # "provimento 205 marketing". Fonte: Provimento 205/2021 e Anexo Unico (lidos em 05/10/2026).
    {
        "slug": "advogado-pode-fazer-marketing",
        "h1": "Advogado pode fazer marketing? O que o Provimento 205/2021 da OAB permite e proíbe",
        "title": "Advogado pode fazer marketing? O que diz o Provimento 205",
        "desc": ("Advogado pode fazer marketing? Sim, dentro do Provimento 205/2021 da OAB. Veja o que é permitido, o "
                 "que é vedado e como fica o Google, o Instagram e o anúncio."),
        "cat": "Advocacia",
        "data": "2026-10-05",
        "trilha_extra": ("/marketing-para-advogados/", "Marketing para advogados"),
        "corpo": f"""
        <p>Sim, advogado pode fazer marketing. O art. 1º do {PROV_205} do Conselho Federal da OAB diz, com todas as
        letras, que "é permitido o marketing jurídico", desde que compatível com o Estatuto, o Regulamento Geral e o
        Código de Ética. O que muda em relação a outros ramos é o tom: a publicidade do advogado precisa ser
        informativa, discreta e sóbria, sem captar clientela nem tratar a advocacia como mercadoria.</p>

        {caixa('<p><strong>Resposta rápida:</strong> pode ter site, perfil no Google, redes sociais, artigos, vídeos, '
               'lives e até anúncio no Google para quem pesquisa o tema. Não pode falar de honorários ou gratuidade '
               'para captar cliente, prometer resultado, usar caso concreto, se dizer especialista sem título, se '
               'comparar com colegas nem mandar mala direta.</p>')}

        <h2>O que é marketing jurídico para a OAB?</h2>
        <p>O art. 2º do Provimento define os termos. Marketing jurídico é o uso de estratégias planejadas para
        alcançar objetivos do exercício da advocacia (inciso I). Marketing de conteúdos jurídicos é criar e divulgar
        conteúdo para informar o público e consolidar o nome do advogado ou do escritório (inciso II). E captação de
        clientela é o uso de mecanismos de marketing que, de forma ativa, induzem à contratação ou estimulam o
        litígio (inciso VIII) — é isso que fica de fora.</p>

        <h2>Qual a diferença entre publicidade ativa e passiva?</h2>
        <p>Essa distinção explica muito do que pode e do que não pode. Publicidade ativa é a que atinge um número
        indeterminado de pessoas, mesmo que elas não tenham procurado nada (art. 2º, VI). Publicidade passiva é a que
        atinge só quem buscou informações sobre o advogado ou o tema, ou quem concordou antes em receber (art. 2º,
        VII). Quando alguém pesquisa "advogado de família" no Google e encontra a página do seu escritório, é desse
        segundo tipo que se trata. O art. 6º, por exemplo, traz vedações específicas para a publicidade ativa, como
        informar dimensões ou estrutura física do escritório.</p>

        <h2>O que o advogado pode fazer no marketing?</h2>
        <p>Pelo Provimento e pelo Anexo Único, entre outras coisas, o advogado pode:</p>
        <ul>
          <li>usar anúncios, pagos ou não, nos meios de comunicação não vedados pelo Código de Ética (art. 5º);</li>
          <li>usar logomarca, identidade visual e fotos dos advogados e do escritório — mas não a logomarca nem os
          símbolos oficiais da OAB (art. 5º, § 2º);</li>
          <li>participar de vídeos e lives, sem usar casos concretos nem apresentar resultados (art. 5º, § 3º);</li>
          <li>informar qualificações e títulos verdadeiros e comprováveis (art. 4º, § 1º);</li>
          <li>estar nas redes sociais e no YouTube, respeitando o Código de Ética (Anexo);</li>
          <li>usar chatbot no site para as primeiras dúvidas, sem afastar a pessoalidade do atendimento (Anexo).</li>
        </ul>

        <h2>O que o advogado não pode fazer no marketing?</h2>
        <p>As vedações principais estão no art. 3º e no art. 6º, e o Anexo detalha alguns meios:</p>
        <ul>
          <li>falar de honorários, forma de pagamento, gratuidade ou descontos como forma de captar clientes (art. 3º, I);</li>
          <li>divulgar informação que possa induzir a erro (art. 3º, II);</li>
          <li>anunciar especialidade sem título certificado ou notória especialização (art. 3º, III);</li>
          <li>usar expressões persuasivas, de autoengrandecimento ou de comparação (art. 3º, IV);</li>
          <li>distribuir material de forma indiscriminada em locais públicos, presenciais ou virtuais (art. 3º, V);</li>
          <li>pagar para aparecer em rankings, prêmios ou honrarias (art. 5º, § 1º);</li>
          <li>prometer resultado ou usar caso concreto para oferecer serviço, e ostentar bens (art. 6º);</li>
          <li>mandar mala direta para uma coletividade e usar aplicativo que responda consultas automaticamente a
          quem não é cliente (Anexo).</li>
        </ul>

        {tabela(
            ["Situação", "Pode?", "Onde está"],
            [
                ["Site com páginas por área de atuação", "Sim, com tom informativo", "Art. 1º e art. 5º"],
                ["Anúncio no Google para quem pesquisa o tema", "Sim, se responde a uma busca do potencial cliente", "Anexo Único"],
                ["Impulsionar post no Instagram", "Sim, se não contém oferta de serviços jurídicos", "Anexo Único"],
                ["“Primeira consulta grátis” para atrair cliente", "Não", "Art. 3º, I"],
                ["“Especialista em” sem título", "Não", "Art. 3º, III"],
                ["Contar caso ganho para atrair cliente", "Não", "Art. 6º"],
                ["Mala direta para uma lista de desconhecidos", "Não", "Anexo Único"],
            ],
            "Resumo informativo. Não substitui a leitura do Provimento nem a orientação da sua seccional.")}

        <h2>Advogado pode impulsionar post no Instagram?</h2>
        <p>Pode, com uma condição: o Anexo Único permite patrocínio e impulsionamento nas redes sociais "desde que não
        se trate de publicidade contendo oferta de serviços jurídicos". Um post que explica um direito pode ser
        impulsionado; um post que oferece o serviço do escritório, não. E o art. 4º, § 5º, veda o uso de meios ou
        ferramentas que influam de forma fraudulenta no impulsionamento ou no alcance.</p>

        <h2>E o anúncio no Google, como fica?</h2>
        <p>O Anexo trata do tema pelo nome: a aquisição de palavra-chave, a exemplo do Google Ads, é permitida quando
        responde a uma busca iniciada pelo potencial cliente e as palavras estão de acordo com a ética; anúncios
        ostensivos em plataformas de vídeo são proibidos. É por isso que o anúncio de advocacia funciona melhor na
        pesquisa do Google, ligado a uma página informativa da área. Veja como isso é montado em
        {link('/trafego-pago-para-advogados/', 'tráfego pago para advogados')}.</p>

        <h2>Quem responde se a publicidade passar do limite?</h2>
        <p>O próprio advogado. O art. 1º, § 1º, diz que as informações divulgadas devem ser objetivas e verdadeiras e
        são de responsabilidade exclusiva das pessoas identificadas — e, no caso de sociedade, dos sócios
        administradores. Por isso vale escolher quem cuida do seu marketing com cuidado: agência que trata advocacia
        como loja expõe o escritório a um risco que ela não vai assumir.</p>

        <h2>Como fazer marketing jurídico na prática?</h2>
        <p>Comece pelo que é claramente permitido e traz resultado: perfil do escritório completo no Google, uma
        página por área de atuação e artigos que explicam direitos. O passo a passo está em
        {link('/blog/como-conseguir-clientes-na-advocacia/', 'como conseguir clientes na advocacia')}, e as frentes
        juntas em {link('/marketing-para-advogados/', 'marketing e SEO para advogados')}.</p>
        <p>Sou bacharel em Direito e consultor de SEO, não advogado. Este artigo resume o texto oficial do Provimento
        205/2021 e do Anexo Único; em caso de dúvida sobre uma situação específica, consulte a sua seccional.</p>
""",
        "faq": [
            ("Advogado pode fazer marketing digital?",
             "Pode. O art. 1º do Provimento 205/2021 permite o marketing jurídico, desde que informativo, discreto e "
             "sóbrio, sem captação de clientela nem mercantilização."),
            ("Advogado pode fazer anúncio pago?",
             "Pode usar anúncios, pagos ou não, nos meios não vedados pelo Código de Ética (art. 5º). No Google Ads, o "
             "Anexo Único exige que o anúncio responda a uma busca iniciada pelo potencial cliente."),
            ("Advogado pode postar resultado de processo?",
             "Não para oferecer serviço: o art. 6º veda a promessa de resultados e o uso de casos concretos, e o art. "
             "5º, § 3º, proíbe apresentar resultados em vídeos e lives."),
            ("Advogado pode usar a logomarca da OAB?",
             "Não. O art. 5º, § 2º, permite logomarca e fotos do advogado e do escritório, mas veda a logomarca e os "
             "símbolos oficiais da OAB."),
        ],
        "cta": ("Quer fazer o marketing do escritório dentro do Provimento 205/2021? Me conte as suas áreas e a cidade. "
                "Em até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Sou advogado(a) e quero fazer o marketing do escritório dentro das regras da OAB."),
                "Quero começar do jeito certo"),
    },
]
