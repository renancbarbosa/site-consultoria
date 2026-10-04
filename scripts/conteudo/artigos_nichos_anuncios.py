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
        "trilha_extra": ("/gestao-de-trafego-pago-goiania/", "Tráfego pago"),
        "corpo": f"""
        <p>Para conseguir clientes de energia solar hoje, a integradora precisa estar onde o cliente pesquisa
        antes de pedir orçamento: no <strong>Google Maps</strong>, num <strong>site que explica o sistema na
        língua dele</strong> e em <strong>anúncios no Google e no Instagram</strong> bem segmentados por região.
        Indicação continua importante, mas sozinha ela não enche a agenda de visitas técnicas.</p>

        <p>O mercado de energia solar ficou mais disputado. Em muitas cidades existem dezenas de integradoras
        oferecendo o mesmo kit, e o cliente compara três ou quatro orçamentos antes de fechar. Quem aparece
        primeiro, passa confiança e responde rápido sai na frente — mesmo sem ser o mais barato.</p>

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

        <h2>Por onde começar a conseguir clientes de energia solar</h2>
        <p>Se a sua empresa ainda depende só de indicação, comece pelo que traz resultado mais rápido: Perfil da
        Empresa organizado e um anúncio no Google bem feito para a sua cidade, levando para uma página específica.
        Em paralelo, construa o site com as páginas certas — é ele que vai trazer cliente de graça daqui a alguns
        meses. Se você quer ajuda com a parte dos anúncios, veja como funciona o
        {link('/trafego-pago-para-energia-solar/', 'tráfego pago para energia solar')}.</p>
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
        {link('/blog/como-conseguir-clientes-energia-solar/', 'como conseguir clientes de energia solar')}.</p>

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

    # ------------------------------------------------------------------ 3
    {
        "slug": "trafego-pago-para-clinicas",
        "h1": "Tráfego pago para clínicas: Google Ads e Meta Ads dentro das regras",
        "title": "Tráfego pago para clínicas: Google Ads e Meta Ads",
        "desc": ("Tráfego pago para clínicas e consultórios: como anunciar no Google e no Instagram dentro das "
                 "regras do CFM e do CFO, sem queimar verba e sem risco ao registro."),
        "cat": "Clínicas",
        "data": DATA,
        "trilha_extra": ("/gestao-de-trafego-pago-goiania/", "Tráfego pago"),
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
        {link('/gestao-de-trafego-pago-goiania/', 'gestão de tráfego pago')} — e, para consultório
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
        "trilha_extra": ("/gestao-de-trafego-pago-goiania/", "Tráfego pago"),
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
        {link('/gestao-de-trafego-pago-goiania/', 'gestão de tráfego pago')}. E se ainda está decidindo entre anúncio
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
]
