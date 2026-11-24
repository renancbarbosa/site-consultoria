# -*- coding: utf-8 -*-
"""
Artigos de apoio dos 5 nichos de 23/11/2026 (um por nicho, ligado à página principal dele).

  /blog/como-atrair-clientes-para-salao-de-beleza/   -> /marketing-para-salao-de-beleza/
  /blog/como-atrair-clientes-para-oficina-mecanica/  -> /marketing-para-oficina-mecanica/
  /blog/como-atrair-clientes-para-loja/              -> /marketing-para-loja/
  /blog/landing-page-para-construtora/               -> /marketing-para-construtoras/
  /blog/google-ads-para-arquitetos/                  -> /marketing-para-arquitetos/

Buscas (planejador do Google Ads, 10/11/2026): "como atrair clientes para loja" 100 a 1 mil;
"como atrair clientes para salão de beleza" (várias formas), "como atrair clientes para oficina
mecanica", "landing page construtora" e "google ads para arquitetos" de 10 a 100 cada.

Regras: público é o DONO; sem preço da RCB; nenhum resultado prometido; fatos só com fonte
oficial (as mesmas conferidas para as páginas, em 23/11/2026); todo artigo termina no WhatsApp.
Gerador: scripts/gerar-nichos-2026-11-23.py
"""
from urllib.parse import quote

from rcb_artigo import caixa, tabela, link

DATA = "2026-11-23"


def wa(texto):
    return "https://wa.me/5562991161040?text=" + quote(texto, safe="")


def _a(href, texto):
    return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (href, texto)


def _cnae(codigo, texto):
    return _a("https://cnae.ibge.gov.br/?subclasse=%s&amp;tipo=cnae&amp;versao=10&amp;view=subclasse" % codigo, texto)


CDC_URL = "https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm"
LGPD = _a("https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm", "LGPD (Lei 13.709/2018)")
HORARIO = _a("https://support.google.com/business/answer/3039617?hl=pt-BR", "horário principal e o horário especial")
LEI_SALAO = _a("https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12592.htm", "Lei 12.592/2012")
LEI_INCORP = _a("https://www.planalto.gov.br/ccivil_03/leis/l4591.htm", "Lei 4.591/1964")
CAU_75 = _a("https://transparencia.caubr.gov.br/resolucao75/", "Resolução CAU/BR nº 75/2014")
CAU_52 = _a("https://transparencia.caubr.gov.br/resolucao52/", "Código de Ética e Disciplina do CAU/BR")

ARTIGOS = [
    # ------------------------------------------------------------------ 1. SALÃO
    {
        "slug": "como-atrair-clientes-para-salao-de-beleza",
        "h1": "Como atrair clientes para salão de beleza: 10 caminhos para encher a agenda",
        "title": "Como atrair clientes para salão de beleza: 10 caminhos",
        "desc": ("Como atrair clientes para salão de beleza e barbearia: Google Maps com fotos e botão de agendar, "
                 "avaliações, cliente que volta e parcerias no bairro."),
        "cat": "Salão de beleza",
        "data": DATA,
        "trilha_extra": ("/marketing-para-salao-de-beleza/", "Marketing para salão de beleza"),
        "corpo": f"""
        <p>Para atrair clientes para salão de beleza, o caminho mais seguro é aparecer bem no Google Maps do seu
        bairro, com fotos reais do seu trabalho, avaliações recentes e um jeito fácil de marcar horário, e fazer a
        cliente que já veio voltar na época certa. O Instagram mostra o seu trabalho para quem já segue você; quem
        ainda não conhece o salão costuma começar a procura no Google.</p>

        {caixa('<p><strong>Resposta rápida:</strong> deixe o perfil do salão no Google com fotos atuais do seu '
               'trabalho, cada serviço cadastrado e o horário real, inclusive o de sábado. Ponha um botão de '
               'agendar, peça avaliação logo depois do atendimento, lembre a cliente de voltar no tempo certo de '
               'cada serviço e faça parcerias com negócios do bairro que atendem o mesmo público.</p>')}

        <h2>1. Entenda como a cliente escolhe um salão novo</h2>
        <p>Ninguém troca de salão por acaso. A cliente se mudou, a profissional antiga saiu, ou ela quer um
        serviço que o salão de sempre não faz. Nessa hora ela pesquisa "salão perto de mim", "escova no bairro"
        ou "barbearia aberta agora", olha as fotos, confere as estrelas e escolhe quem parece mais confiável e
        mais fácil de marcar. E a concorrência é grande: pelos dados públicos de CNPJ de novembro de 2026, o
        código {_cnae("9602501", "9602-5/01")} (cabeleireiros, manicure e pedicure) reunia 954.042 empresas
        ativas, com 45.725 abertas em 90 dias. Quem não aparece bem no próprio bairro fica invisível.</p>

        <h2>2. Fotos reais do seu trabalho, com autorização</h2>
        <p>Foto é o que vende salão. Mostre cortes, cores, mechas, unhas, sobrancelhas e barbas feitos por você,
        com luz boa e fundo limpo, sempre com a autorização de quem foi atendido. Mostre também o espaço, a
        recepção e a equipe: a cliente quer saber onde vai passar as próximas duas horas. Fotos novas com
        frequência mostram que o salão está vivo, e fotos antigas, de cinco anos atrás, passam a impressão
        contrária. Banco de imagem não serve: a cliente percebe, e o Google também prefere o que é real.</p>

        <h2>3. Cada serviço com o nome que a cliente pesquisa</h2>
        <p>O perfil no Google permite cadastrar os serviços um por um. Quem lista só "cabeleireiro" perde a
        cliente que pesquisa "progressiva", "luzes", "design de sobrancelha", "alongamento de unha" ou "barba".
        Use o nome que a cliente usa, não o nome técnico do produto, e descreva em uma frase o que está incluído.
        No site, uma página por serviço principal faz o mesmo trabalho e ainda responde às dúvidas mais comuns,
        como tempo de duração e cuidados depois. Veja a {link('/google-perfil-empresa/', 'otimização do Google Perfil da Empresa')}.</p>

        <h2>4. Deixe a cliente marcar sem esperar resposta</h2>
        <p>Muita agenda vazia é mensagem respondida tarde. A cliente pergunta o horário às nove da noite e, se a
        resposta chega no dia seguinte, ela já marcou em outro lugar. O perfil do salão no Google aceita link de
        agendamento: a ajuda do Google sobre
        {_a("https://support.google.com/business/answer/6218037?hl=pt-BR", "links de empresas locais")} mostra
        onde ele aparece, e as {_a("https://support.google.com/business/answer/13769188?hl=pt-BR", "diretrizes de links")}
        explicam o que cada categoria aceita. Se você ainda marca tudo pelo WhatsApp, deixe respostas prontas
        para as perguntas de sempre e combine quem responde em cada turno. Veja os
        {link('/blog/erros-no-whatsapp-que-perdem-orcamento/', 'erros no WhatsApp que perdem cliente')}.</p>

        <h2>5. Peça avaliação no momento certo</h2>
        <p>O melhor momento é logo depois do atendimento, quando a cliente está se olhando no espelho e gostou
        do resultado. Mande o link direto para a avaliação pelo WhatsApp no mesmo dia, com uma frase simples.
        Responda todas as avaliações, agradecendo pelo nome do serviço feito, e responda também as críticas,
        com educação e sem discutir: quem lê a resposta é a próxima cliente. Nunca compre, troque ou dê desconto
        em troca de avaliação, porque as regras do Google proíbem e um perfil suspenso apaga todo o trabalho.
        Veja como {link('/blog/responder-avaliacoes-google-sem-parecer-automatico/', 'responder avaliações sem parecer automático')}.</p>

        <h2>6. Horário de verdade, inclusive sábado e feriado</h2>
        <p>Salão vive de sábado, de véspera de feriado e de dezembro. Se o perfil mostra "fechado" num dia em que
        você abre, a cliente nem tenta. O Google permite definir o {HORARIO}, e vale cadastrar com antecedência
        as datas de mais movimento, como o fim de ano e as semanas de formatura. O mesmo cuidado vale para quem
        fecha: aparecer "aberto" e a cliente encontrar a porta fechada vira avaliação ruim.</p>

        <h2>7. Faça a cliente voltar no tempo de cada serviço</h2>
        <p>Cabelo, unha, sobrancelha e barba crescem. Cada serviço tem um tempo natural de retorno, e você sabe
        qual é na sua clientela melhor do que qualquer tabela. Com autorização da cliente, guarde o contato, o
        serviço feito e a profissional que atendeu, e mande um lembrete perto da data, oferecendo um horário com
        quem ela já gosta. A {LGPD} pede que a cliente saiba para que o contato será usado e possa sair da lista
        quando quiser. Um lembrete na hora certa enche a agenda sem baixar o preço do seu trabalho.</p>

        {tabela(
            ["Quem é", "Como chega", "O que faz ela escolher você"],
            [
                ["Cliente nova do bairro", "Pesquisa no Google Maps", "Fotos reais, avaliações recentes e botão de agendar"],
                ["Noiva e madrinhas", "Indicação, Google e fornecedores de casamento", "Fotos de penteados e maquiagens, teste antes do dia e horário combinado por escrito"],
                ["Cliente que já veio", "Lembrete no WhatsApp", "A profissional preferida e um horário que cabe na rotina"],
                ["Quem procura barbearia", "Busca por barbearia perto de casa", "Agendamento rápido, sem fila, e o estilo de corte nas fotos"],
            ])}

        <h2>8. Faça parcerias com quem atende o mesmo público</h2>
        <p>Lojas de roupa, lojas de noiva, fotógrafos, cerimonialistas, academias e estúdios de pilates falam
        todos os dias com a sua cliente. Uma parceria simples, em que um indica o outro com um cartão ou um
        convite, traz clientes que já chegam confiando em você. Noivas e eventos merecem atenção à parte: o
        mesmo atendimento costuma levar madrinhas, mães e amigas, e o portfólio de penteados e maquiagens é o
        que fecha esse tipo de serviço.</p>

        <h2>9. Anuncie só o que dá margem e só no seu raio</h2>
        <p>Anúncio no Google funciona para salão quando aparece para quem procura um serviço específico, perto do
        salão. Faz sentido para os serviços de mais valor, como mechas, tratamentos, noivas e alongamentos, e
        para encher os horários que costumam ficar vazios. Limite o anúncio ao raio que a cliente aceita ir e
        bloqueie as buscas que não viram horário marcado: curso de cabeleireiro, vaga de manicure, compra de
        produto. Veja a {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>

        <h2>10. Mostre a biossegurança e prometa só o que cumpre</h2>
        <p>A {LEI_SALAO} reconhece as profissões de cabeleireiro, barbeiro, esteticista, manicure, pedicure,
        depilador e maquiador e determina, no art. 4º, que esses profissionais sigam as normas sanitárias, com
        esterilização de materiais e utensílios. Mostrar esse cuidado no perfil e no site responde a um medo que
        a cliente raramente fala. Na outra ponta, evite promessas como "liso por seis meses": o resultado depende
        do fio e do cuidado em casa, e o
        {_a(CDC_URL, "Código de Defesa do Consumidor (art. 37)")} proíbe publicidade que induza o consumidor a
        erro. Foto real e atendimento pontual convencem mais do que frase de efeito.</p>

        <h2>Por onde começar a atrair clientes para o salão?</h2>
        <p>Comece pelo perfil no Google com fotos novas, serviços completos e horário certo, porque é ali que a
        cliente nova decide. Em seguida, a rotina de avaliações e o botão de agendar. Com isso funcionando, o
        lembrete para a cliente voltar e, por último, o anúncio para os serviços que dão margem. As frentes
        juntas estão em {link('/marketing-para-salao-de-beleza/', 'marketing para salão de beleza')}.</p>
""",
        "faq": [
            ("Como divulgar salão de beleza no Google?",
             "Com o perfil do salão no Google completo: fotos reais do trabalho, cada serviço cadastrado, horário "
             "certo, avaliações recentes respondidas e um botão de agendar."),
            ("Salão de beleza precisa de site?",
             "Ajuda quem quer agendamento online e quer aparecer para serviços específicos. O perfil no Google traz "
             "a maioria das clientes novas; o site é onde ela confere os serviços e marca."),
            ("Como fazer a cliente voltar ao salão?",
             "Com autorização dela, guarde o serviço feito e mande um lembrete perto da data de retorno, oferecendo "
             "horário com a profissional preferida."),
            ("Posso dar desconto em troca de avaliação no Google?",
             "Não. As regras do Google proíbem oferecer vantagem em troca de avaliação. Peça a avaliação logo depois "
             "do atendimento, com o link direto, e responda todas."),
        ],
        "cta": ("Tem um salão ou uma barbearia e quer a agenda mais cheia? Me conte o bairro e os serviços que você "
                "mais quer vender. Em até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho um salão de beleza e quero atrair mais clientes."),
                "Quero a agenda cheia"),
    },

    # ------------------------------------------------------------------ 2. OFICINA
    {
        "slug": "como-atrair-clientes-para-oficina-mecanica",
        "h1": "Como atrair clientes para oficina mecânica: confiança antes do orçamento",
        "title": "Como atrair clientes para oficina mecânica: 10 caminhos",
        "desc": ("Como atrair clientes para oficina mecânica: avaliações, orçamento por escrito, Google Maps, "
                 "lembrete de revisão, frotas e parcerias com guinchos."),
        "cat": "Oficina mecânica",
        "data": DATA,
        "trilha_extra": ("/marketing-para-oficina-mecanica/", "Marketing para oficina mecânica"),
        "corpo": f"""
        <p>Para atrair clientes para oficina mecânica, o que mais pesa é tirar o medo do motorista antes de ele
        chegar: avaliações boas e recentes, fotos da oficina por dentro, orçamento por escrito e a peça trocada
        mostrada ao cliente. Com a confiança resolvida, o resto é estar no Google Maps da sua região, lembrar o
        cliente da próxima revisão e conquistar frotas e parceiros que mandam carro toda semana.</p>

        {caixa('<p><strong>Resposta rápida:</strong> complete o perfil da oficina no Google com serviços, horário e '
               'fotos de dentro, peça avaliação na entrega do carro, mande orçamento por escrito pelo WhatsApp, '
               'mostre a peça trocada, avise o cliente da próxima revisão e faça parceria com guinchos, autopeças, '
               'lava-jatos e empresas com frota.</p>')}

        <h2>1. Entenda o medo de quem procura oficina</h2>
        <p>Quase todo motorista já ouviu a história do serviço que não precisava ser feito ou da conta que
        dobrou no fim. Por isso, a escolha de uma oficina nova começa pela desconfiança: a pessoa pesquisa, lê
        avaliações e procura sinais de que não vai ser enganada. Concorrência existe: pelos dados públicos de
        CNPJ de novembro de 2026, o código {_cnae("4520001", "4520-0/01")} (manutenção e reparação mecânica de
        veículos) reunia 286.679 empresas ativas, com 51.471 abertas em 12 meses. Ganha quem mostra, antes do
        primeiro contato, que trabalha às claras.</p>

        <h2>2. Mostre a oficina por dentro</h2>
        <p>Foto da fachada ajuda o motorista a achar o lugar; foto de dentro é o que passa confiança. Mostre o
        pátio organizado, os elevadores, os equipamentos de diagnóstico, a equipe trabalhando e a área onde o
        cliente espera. Oficina limpa e organizada na foto sugere serviço cuidadoso no carro. Atualize as fotos
        de vez em quando e responda às perguntas que aparecem no perfil, porque elas ficam à vista de todo mundo
        que pesquisa depois.</p>

        <h2>3. Cadastre os serviços com o nome que o motorista usa</h2>
        <p>O motorista não pesquisa "reparação de sistema de frenagem": pesquisa "troca de pastilha de freio",
        "alinhamento e balanceamento", "ar-condicionado do carro" ou "luz da injeção acesa". Cadastre no perfil
        do Google cada serviço com esse nome e, no site, explique os sintomas que o cliente reconhece, como
        barulho ao frear, carro puxando para um lado ou ar que não gela. Quem se reconhece na descrição liga.
        Veja a {link('/google-perfil-empresa/', 'otimização do Google Perfil da Empresa')}.</p>

        <h2>4. Faça do orçamento por escrito uma marca da oficina</h2>
        <p>O {_a(CDC_URL, "Código de Defesa do Consumidor")} manda entregar orçamento prévio com o valor da mão
        de obra, das peças, as condições de pagamento e as datas de início e de término (art. 40), e chama de
        prática abusiva fazer serviço sem orçamento e sem autorização do cliente (art. 39, VI). Transforme a
        obrigação em argumento: mande o orçamento pelo WhatsApp, com foto ou vídeo curto da peça gasta, e
        separe o que precisa ser feito agora do que pode esperar. Diga isso no perfil e no site.</p>

        <h2>5. Entregue a peça trocada na mão do cliente</h2>
        <p>Mostrar a peça velha é a prova mais simples de que o serviço foi feito. O Código de Defesa do
        Consumidor também presume o uso de peças originais e novas, ou que mantenham a especificação do
        fabricante, salvo autorização em contrário do cliente (art. 21). Se o cliente preferir uma peça
        alternativa para economizar, registre a escolha dele por escrito. Transparência na hora da entrega
        vira avaliação boa no mesmo dia.</p>

        <h2>6. Peça avaliação na entrega da chave</h2>
        <p>O momento certo é quando o cliente pega o carro funcionando. Mande o link direto da avaliação pelo
        WhatsApp e, se possível, peça que ele conte o serviço feito: "troquei a embreagem", "resolveram o
        barulho". Avaliação com detalhe convence mais o próximo motorista. Responda todas, inclusive as
        críticas, com calma e sem expor o cliente. E nunca compre nem troque avaliação: é contra as regras do
        Google e pode derrubar o perfil.</p>

        <h2>7. Lembre o cliente da próxima revisão</h2>
        <p>Troca de óleo, filtros, correia, alinhamento e revisão têm prazo por quilometragem ou por tempo. Com
        autorização do cliente e de acordo com a {LGPD}, registre o modelo do carro, a quilometragem e o serviço
        feito, e mande um aviso quando a próxima troca estiver perto. Esse cliente custa quase nada para trazer
        de volta, porque já conhece o seu trabalho, e é o que segura o movimento nos meses fracos.</p>

        {tabela(
            ["Cliente", "Como chega", "O que precisa ver"],
            [
                ["Motorista com o carro com problema", "Busca no Google Maps perto de onde está", "Aberto agora, avaliações recentes e botão de ligar"],
                ["Cliente da revisão", "Lembrete no WhatsApp", "Orçamento claro, prazo combinado e a mesma equipe"],
                ["Frota de empresa e motorista de aplicativo", "Visita, indicação e site", "Agendamento, carro parado pouco tempo e nota fiscal"],
                ["Indicação de parceiro", "Guincho, autopeças e lava-jato", "Pontualidade e o mesmo cuidado com o cliente indicado"],
            ])}

        <h2>8. Conquiste frotas e motoristas de aplicativo</h2>
        <p>Empresas com carros, locadoras e motoristas de aplicativo precisam de manutenção constante e, acima
        de tudo, de carro parado o menor tempo possível. Uma página no site falando com esse público, com
        agendamento, prazo, nota fiscal e atendimento combinado, abre uma porta que o motorista particular não
        abre. Visite as empresas da região, deixe o contato e cumpra o prazo: um bom cliente de frota vale
        muitos atendimentos avulsos.</p>

        <h2>9. Faça parceria com quem atende o mesmo motorista</h2>
        <p>Guinchos, lojas de autopeças, lava-jatos e funilarias falam todos os dias com quem precisa de
        oficina. Só a lavagem de veículos reunia 116.101 empresas ativas em novembro de 2026, pelos dados
        públicos de CNPJ do código {_cnae("4520005", "4520-0/05")}. Uma indicação de confiança entre vizinhos
        traz clientes que já chegam acreditando em você. Para o lado do guincho, veja o
        {link('/marketing-para-empresa-de-guincho/', 'marketing para empresas de guincho')}.</p>

        <h2>10. Anuncie para a urgência e prometa só o que cumpre</h2>
        <p>Quem pesquisa oficina geralmente está com o problema agora, então o anúncio no Google funciona bem
        quando aparece só no raio da oficina, no horário em que alguém atende, e bloqueia buscas de curso, vaga
        e compra de peça. Na mensagem, nada de "pronto em duas horas" ou "garantia total": o Código de Defesa do
        Consumidor proíbe publicidade enganosa (art. 37) e já fixa prazos para o cliente reclamar de defeito
        aparente, de 30 dias para serviço e produto não durável e de 90 dias para serviço e produto durável
        (art. 26). Prometa garantia por escrito, com prazo e o que ela cobre. Veja a
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')}.</p>

        <h2>Por onde começar a atrair clientes para a oficina?</h2>
        <p>Comece pela confiança: perfil no Google com fotos de dentro e serviços completos, avaliação pedida em
        toda entrega e orçamento por escrito como regra. Depois, o lembrete de revisão para quem já é cliente e
        as visitas a frotas e parceiros. O anúncio entra quando o atendimento já está pronto para responder
        rápido. As frentes juntas estão em {link('/marketing-para-oficina-mecanica/', 'marketing para oficina mecânica')}.</p>
""",
        "faq": [
            ("Como divulgar oficina mecânica?",
             "Perfil no Google com serviços e fotos de dentro, avaliações pedidas na entrega do carro, orçamento por "
             "escrito, lembrete de revisão e parcerias com guinchos, autopeças e frotas."),
            ("Por quanto tempo vale o orçamento da oficina?",
             "Pelo Código de Defesa do Consumidor (art. 40, § 1º), salvo combinação diferente, o orçamento vale por "
             "10 dias a partir de quando o cliente o recebe."),
            ("Vale a pena anunciar oficina no Google?",
             "Vale, porque quem pesquisa está com o problema agora. O cuidado é anunciar só no raio da oficina e "
             "bloquear buscas de curso, vaga e compra de peça."),
            ("Como conseguir clientes de frota para a oficina?",
             "Com uma página no site para empresas, visitas às frotas da região e atendimento com agendamento, prazo "
             "curto e nota fiscal."),
        ],
        "cta": ("Tem uma oficina e quer mais carros no elevador? Me conte a sua cidade e os serviços que mais dão "
                "margem. Em até 24 horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho uma oficina mecânica e quero atrair mais clientes."),
                "Quero mais clientes"),
    },

    # ------------------------------------------------------------------ 3. LOJA
    {
        "slug": "como-atrair-clientes-para-loja",
        "h1": "Como atrair clientes para loja: 10 ideias para encher a loja física",
        "title": "Como atrair clientes para loja: 10 ideias que funcionam",
        "desc": ("Como atrair clientes para loja: Google Maps com produtos, vitrine, horário especial, datas "
                 "comemorativas, lista de clientes e anúncio no raio da loja."),
        "cat": "Lojas e varejo",
        "data": DATA,
        "trilha_extra": ("/marketing-para-loja/", "Marketing para loja"),
        "corpo": f"""
        <p>Para atrair clientes para loja, o primeiro passo é ser encontrado por quem procura perto de casa: um
        perfil no Google Maps com fotos, produtos e horário certo. Depois vêm a vitrine que faz quem passa
        entrar, as datas comemorativas preparadas com antecedência e a lista de clientes que já compraram, com
        autorização, para avisar das novidades. Promoção ajuda, desde que seja verdadeira e esteja em estoque.</p>

        {caixa('<p><strong>Resposta rápida:</strong> complete o perfil da loja no Google com fotos da fachada, da '
               'vitrine e de dentro, cadastre os produtos principais, ajuste o horário nos feriados, prepare as '
               'datas que vendem um mês antes, faça eventos na loja, peça avaliação no caixa e monte uma lista de '
               'clientes com autorização para avisar das novidades.</p>')}

        <h2>1. A compra começa no celular, mesmo na loja de rua</h2>
        <p>Antes de sair de casa, o cliente pesquisa "loja de calçados perto de mim", "papelaria aberta agora" ou
        o nome do produto que quer. Ele vê quem aparece no mapa, confere o horário, olha as fotos e pede a rota.
        A disputa é grande: só no vestuário, o código {_cnae("4781400", "4781-4/00")} reunia 1.020.178 empresas
        ativas em novembro de 2026, com 40.731 abertas em 90 dias, pelos dados públicos de CNPJ. A loja que não
        aparece nessa pesquisa depende de quem passa na calçada.</p>

        <h2>2. Mostre os produtos no Google</h2>
        <p>O perfil da empresa no Google tem um
        {_a("https://support.google.com/business/answer/9124203?hl=pt-BR", "Editor de produtos")} para mostrar
        o que você vende, com foto e descrição, e a ajuda do Google explica como
        {_a("https://support.google.com/business/answer/9934993?hl=pt-BR", "mostrar os produtos disponíveis na loja")}
        na Pesquisa e no Maps. Comece pelos produtos que mais vendem e pelos que o cliente costuma procurar pelo
        nome. Quem vê que o item está na sua loja, a dez minutos de casa, deixa de comprar fora.</p>

        <h2>3. Fachada fácil de reconhecer e vitrine que muda</h2>
        <p>Foto da fachada no perfil ajuda o cliente a achar a loja na rua; letreiro legível e entrada livre
        fazem o resto. A vitrine é o anúncio de quem passa a pé: trocada com frequência, com poucos produtos bem
        arrumados e preço visível quando fizer sentido, ela dá motivo para entrar. Vitrine que não muda há meses
        some na paisagem, mesmo que a loja tenha novidade lá dentro.</p>

        <h2>4. Horário certo, principalmente no feriado</h2>
        <p>Nada derruba uma venda como o Google mostrar "fechado" no dia em que a loja está aberta. O Google
        permite definir o {HORARIO}, e vale cadastrar os feriados, o horário estendido de fim de ano e as datas
        de inventário com antecedência. O contrário também é ruim: o cliente que encontra a porta fechada depois
        de ver "aberto" no mapa não volta e ainda pode deixar uma avaliação negativa.</p>

        <h2>5. Prepare as datas que vendem um mês antes</h2>
        <p>Dia das Mães, Dia dos Namorados, Dia dos Pais, Dia das Crianças, Black Friday e Natal costumam
        concentrar a procura no varejo, e a pesquisa por presente começa antes da data. Atualize produtos e
        fotos no perfil e no site, ajuste o horário especial, avise a sua lista de clientes e, se for anunciar,
        ligue o anúncio com antecedência. Quem se prepara aparece para quem ainda está escolhendo; quem deixa
        para a véspera disputa os atrasados.</p>

        <h2>6. Faça a loja ser motivo de visita</h2>
        <p>Evento dentro da loja traz gente que ainda não conhece o seu espaço: lançamento de coleção, dia de
        prova, oficina rápida, degustação, encontro com um fornecedor. Divulgue com antecedência no perfil do
        Google, que permite publicar novidades e eventos, e para a lista de clientes. Uma parceria com o
        negócio vizinho, como o café ao lado ou o salão da esquina, divide o público e o trabalho.</p>

        {tabela(
            ["Quem é", "Onde procura", "O que faz entrar na loja"],
            [
                ["Morador do bairro", "Google Maps", "Aberto agora, rota fácil e fotos de dentro"],
                ["Quem procura um produto", "Busca pelo nome do produto", "O produto à vista no perfil ou no site"],
                ["Cliente que já comprou", "Lista no WhatsApp", "Novidade, convite para evento e atendimento conhecido"],
                ["Quem passa na calçada", "A vitrine", "Vitrine trocada, entrada livre e letreiro legível"],
            ])}

        <h2>7. Monte uma lista de clientes, com autorização</h2>
        <p>O cliente que já comprou é o mais fácil de trazer de volta. Pergunte no caixa se ele quer receber as
        novidades pelo WhatsApp e anote o que ele costuma comprar. A {LGPD} pede que ele saiba para que o
        contato será usado e possa sair da lista quando quiser. Mande pouco e com motivo: chegada de coleção,
        reposição do produto que ele procura, convite para um evento. Mensagem demais vira bloqueio.</p>

        <h2>8. Venda também fora do balcão, com regra clara</h2>
        <p>Catálogo pelo WhatsApp, retirada na loja e um site com os produtos principais pegam o cliente que não
        tem tempo de passar. Quem vende fora da loja precisa deixar troca e devolução claras: o
        {_a(CDC_URL, "Código de Defesa do Consumidor (art. 49)")} dá ao cliente 7 dias para desistir da compra
        feita fora do estabelecimento. Para vender para outras cidades, com pagamento e frete, veja a
        {link('/criacao-de-loja-virtual-goiania/', 'criação de loja virtual')}.</p>

        <h2>9. Peça avaliação no caixa</h2>
        <p>Entre duas lojas parecidas no mapa, o cliente escolhe a que tem mais avaliações recentes e boas. Um
        cartão com o link no caixa, um aviso na sacola ou uma mensagem depois da compra lembram o cliente de
        avaliar. Responda todas, agradecendo e citando o que ele comprou quando der. Nunca troque avaliação por
        desconto ou brinde: é contra as regras do Google. Veja como
        {link('/blog/usar-avaliacoes-google-confianca-conversao/', 'usar as avaliações do Google para ganhar confiança')}.</p>

        <h2>10. Anuncie no raio da loja, com promoção de verdade</h2>
        <p>O anúncio no Google funciona para loja quando aparece para quem está perto e procura o que você tem.
        Limite o anúncio à região da loja e bloqueie buscas de atacado, vaga de emprego e "grátis". Na mensagem,
        cuidado com "tudo pela metade do preço" e "o mais barato da cidade": o Código de Defesa do Consumidor
        diz que a oferta anunciada obriga a loja a cumprir (art. 30) e proíbe publicidade enganosa (art. 37).
        Anuncie o que está em estoque, com a condição e o prazo claros.</p>

        <h2>Por onde começar a atrair clientes para a loja?</h2>
        <p>Comece pelo perfil no Google: fotos, produtos principais e horário certo, porque é o que o cliente vê
        antes de sair de casa. Depois, a vitrine, a lista de clientes e o calendário das datas que vendem. O
        anúncio entra para reforçar as datas e os produtos de mais margem. As frentes juntas estão em
        {link('/marketing-para-loja/', 'marketing para loja')}, e para aparecer no mapa do bairro veja o
        {link('/para-comercios-locais/', 'SEO para comércio local')}.</p>
""",
        "faq": [
            ("Como atrair clientes para loja de roupa?",
             "Perfil no Google com fotos de dentro e das peças, vitrine trocada com frequência, lista de clientes no "
             "WhatsApp com autorização e as datas comemorativas preparadas com antecedência."),
            ("Como divulgar loja no Google de graça?",
             "Com o perfil da empresa no Google completo: fotos, produtos no Editor de produtos, horário certo e "
             "avaliações respondidas."),
            ("Loja física precisa de site?",
             "Ajuda quem quer vender fora do balcão ou ser achado pelo nome do produto. Para vender para outras "
             "cidades, o caminho é a loja virtual."),
            ("Vale a pena fazer promoção para atrair clientes?",
             "Vale, se for verdadeira e estiver em estoque. A oferta anunciada obriga a loja a cumprir (Código de "
             "Defesa do Consumidor, art. 30)."),
        ],
        "cta": ("Tem uma loja e quer mais gente entrando? Me conte o que você vende e onde a loja fica. Em até 24 "
                "horas eu te digo por onde começar.",
                wa("Olá, Renan! Tenho uma loja e quero atrair mais clientes."),
                "Quero vender mais"),
    },

    # ------------------------------------------------------------------ 4. CONSTRUTORA
    {
        "slug": "landing-page-para-construtora",
        "h1": "Landing page para construtora: o que a página de cada empreendimento precisa ter",
        "title": "Landing page para construtora: o que a página precisa ter",
        "desc": ("Landing page para construtora: localização, plantas, estágio da obra, registro da incorporação, "
                 "formulário que qualifica e contato direto ao corretor."),
        "cat": "Construtoras",
        "data": DATA,
        "trilha_extra": ("/marketing-para-construtoras/", "Marketing para construtoras"),
        "corpo": f"""
        <p>Uma landing page para construtora é a página de um empreendimento só: mostra o imóvel certo para quem
        clicou no anúncio, passa confiança e entrega o contato na hora para o corretor. Ela precisa ter, logo no
        topo, a localização, o tipo de imóvel e o estágio da obra; mais abaixo, plantas, áreas comuns, o registro
        da incorporação e um formulário curto que ajuda o corretor a saber com quem está falando.</p>

        {caixa('<p><strong>Resposta rápida:</strong> uma página por empreendimento, com localização, tipologia e '
               'estágio da obra no topo, plantas e metragens iguais às do projeto registrado, o número do registro '
               'da incorporação à vista, prova de obras entregues, formulário curto com aviso de uso dos dados e '
               'contato que chega na hora para quem vai atender.</p>')}

        <h2>1. Por que a página inicial do site não serve para o anúncio</h2>
        <p>Quem clica num anúncio de "apartamento de 2 quartos no bairro" e cai na página inicial da construtora
        precisa procurar o imóvel no meio de todos os lançamentos, das obras entregues e da história da empresa.
        A maioria desiste antes. A página do empreendimento resolve isso: mostra só aquele imóvel, responde às
        primeiras dúvidas e tem um único objetivo, o contato. E a disputa pela atenção é grande: pelos dados
        públicos de CNPJ de novembro de 2026, o código {_cnae("4120400", "4120-4/00")} (construção de
        edifícios, que inclui também reformas) reunia 183.307 empresas ativas.</p>

        <h2>2. O topo: onde fica, o que é e em que fase está</h2>
        <p>A primeira tela precisa responder a três perguntas sem rolar: onde fica o empreendimento, que tipo de
        imóvel é (quantos quartos, metragem, casa ou apartamento) e em que fase está a obra, lançamento, em
        construção ou pronto para morar. Uma boa foto ou perspectiva e um botão de contato completam o topo.
        Quem não encontra essas respostas em poucos segundos volta para o resultado da busca.</p>

        <h2>3. Plantas e metragens iguais às do projeto registrado</h2>
        <p>Plantas, áreas comuns e acabamentos são o que o comprador mais olha, e é aqui que mora o maior risco.
        O {_a(CDC_URL, "Código de Defesa do Consumidor")} diz que a oferta anunciada obriga a empresa a cumprir
        (art. 30) e proíbe publicidade que induza o comprador a erro (art. 37). Imagem ilustrativa precisa dizer
        que é ilustrativa, e metragens, vagas e itens de lazer precisam bater com o projeto. Uma página honesta
        evita a reclamação que aparece meses depois, na entrega das chaves.</p>

        <h2>4. O registro da incorporação à vista</h2>
        <p>A {LEI_INCORP} diz que o incorporador só pode vender as futuras unidades depois do registro do
        memorial de incorporação no cartório de imóveis (art. 32), e que o número desse registro, com a
        indicação do cartório, deve constar dos anúncios, impressos, publicações, propostas e contratos, salvo
        nos classificados (art. 32, § 3º). Coloque essa informação num lugar visível da página, não escondida no
        rodapé. Para o comprador mais cuidadoso, ela é um sinal de seriedade.</p>

        <h2>5. Localização que ajuda a decidir</h2>
        <p>Mapa com o endereço do empreendimento e do decorado, e uma lista do que existe por perto: escolas,
        mercados, parques, vias de acesso. Use só informação verdadeira e confirmável, sem "a poucos minutos de
        tudo". Para muita família, o bairro decide antes do imóvel, e mostrar a vizinhança com clareza poupa o
        corretor de explicar tudo de novo a cada contato.</p>

        <h2>6. Formulário curto, que qualifica sem afastar</h2>
        <p>Formulário com dez campos espanta; formulário só com nome e telefone entrega ao corretor um contato
        sem nenhuma pista. O meio-termo são duas ou três perguntas que ajudam no atendimento: que tipo de imóvel
        a pessoa procura, para quando pretende comprar e como prefere ser contatada. Junto do botão, um aviso
        simples sobre o uso dos dados, porque a {LGPD} pede que a pessoa saiba para que eles servem.</p>

        {tabela(
            ["Parte da página", "O que mostrar", "Por que importa"],
            [
                ["Topo", "Localização, tipologia, fase da obra e botão de contato", "Responde em segundos se é o imóvel que a pessoa procura"],
                ["Plantas e áreas comuns", "Plantas, metragens e lazer iguais ao projeto", "A oferta anunciada obriga a empresa (CDC, art. 30)"],
                ["Registro", "Número do registro da incorporação e cartório", "Exigido nos anúncios pela Lei 4.591/1964 (art. 32, § 3º)"],
                ["Prova", "Obras entregues, prazos cumpridos, decorado", "É o que o comprador confere antes de visitar"],
                ["Contato", "Formulário curto, WhatsApp e aviso de uso dos dados", "Contato que chega rápido e com contexto vende mais"],
            ])}

        <h2>7. Contato que chega na hora para o corretor</h2>
        <p>Interesse em imóvel esfria rápido. O contato que cai num e-mail que ninguém olha é verba de anúncio
        jogada fora. Ele precisa chegar na hora para quem vai atender, com o nome do empreendimento e de onde a
        pessoa veio, e a primeira resposta precisa sair no mesmo dia, de preferência em minutos. Um botão de
        WhatsApp com a mensagem já escrita, citando o empreendimento, ajuda quem prefere conversar a preencher
        formulário. Veja como {link('/blog/como-receber-orcamentos-whatsapp-site/', 'receber contatos pelo WhatsApp do site')}.</p>

        <h2>8. Prova de que a construtora entrega</h2>
        <p>Comprar na planta é confiar que a obra vai ficar pronta. Mostre as obras entregues, com fotos reais e
        o ano de entrega, o andamento da obra atual com fotos datadas e o endereço do decorado para visita.
        Avaliações de quem já comprou no perfil da construtora no Google reforçam a mesma mensagem. Nada disso
        precisa de frase de efeito: a prova fala sozinha.</p>

        <h2>9. Página leve, pensada para o celular</h2>
        <p>Boa parte de quem clica no anúncio está no celular, muitas vezes com internet fraca. Fotos pesadas,
        vídeo que toca sozinho e excesso de efeitos deixam a página lenta, e a pessoa desiste antes de ver o
        imóvel. Fotos bem comprimidas, texto curto e botão de contato sempre à vista fazem mais diferença do que
        qualquer animação.</p>

        <h2>10. Medição por anúncio e por página</h2>
        <p>Cada contato precisa chegar com a origem marcada: qual anúncio, qual página, qual empreendimento. Sem
        isso, a construtora continua pagando pelos anúncios que não trazem visita ao decorado e não descobre os
        que trazem. Com a medição, o investimento vai para o que funciona. Veja a
        {link('/gestao-de-trafego-pago/', 'gestão de tráfego pago')} para o lado dos anúncios.</p>

        <h2>Por onde começar a landing page da construtora?</h2>
        <p>Comece pelo empreendimento que mais precisa vender agora: uma página com o topo certo, as plantas
        conferidas com o projeto, o registro da incorporação à vista e o contato chegando na hora para o
        corretor. Com ela medindo bem, vale repetir o modelo nos próximos lançamentos. Veja a
        {link('/criacao-de-landing-page/', 'criação de landing page para anúncios')} e as frentes juntas em
        {link('/marketing-para-construtoras/', 'marketing para construtoras')}.</p>
""",
        "faq": [
            ("Construtora precisa de uma landing page para cada empreendimento?",
             "Para anunciar, sim: a página de cada empreendimento mostra o imóvel certo, filtra quem não é o público "
             "e mede cada contato. O site institucional fica para a história e as obras entregues."),
            ("O que não pode faltar na página de lançamento?",
             "Localização, tipologia, fase da obra, plantas iguais às do projeto, o registro da incorporação, prova "
             "de obras entregues e um contato que chega rápido ao corretor."),
            ("A página precisa mostrar o número do registro da incorporação?",
             "A Lei 4.591/1964 (art. 32, § 3º) exige o número do registro e o cartório nos anúncios, impressos e "
             "publicações da incorporação, salvo nos classificados."),
            ("Landing page ou site institucional?",
             "Os dois têm papéis diferentes. O anúncio leva para a página do empreendimento; o site institucional "
             "conta a história da construtora e reúne todos os empreendimentos."),
        ],
        "cta": ("Tem um empreendimento para vender? Me conte qual é e a região. Em até 24 horas eu te digo como "
                "ficaria a página dele e por onde começar.",
                wa("Olá, Renan! Quero uma landing page para um empreendimento da minha construtora."),
                "Quero a página do empreendimento"),
    },

    # ------------------------------------------------------------------ 5. ARQUITETOS
    {
        "slug": "google-ads-para-arquitetos",
        "h1": "Google Ads para arquitetos: quando vale anunciar e o que o CAU exige",
        "title": "Google Ads para arquitetos: quando vale e o que o CAU exige",
        "desc": ("Google Ads para arquitetos: que buscas anunciar, quais bloquear, a página certa para cada serviço "
                 "e as regras do CAU para a divulgação do escritório."),
        "cat": "Arquitetura",
        "data": DATA,
        "trilha_extra": ("/marketing-para-arquitetos/", "Marketing para arquitetos"),
        "corpo": f"""
        <p>Google Ads para arquitetos vale a pena quando o escritório tem espaço na agenda para novos projetos,
        uma página clara para cada serviço e alguém para responder rápido. O anúncio coloca você na frente de
        quem pesquisa "arquiteto na cidade" ou "projeto de casa" no momento em que está decidindo. A divulgação
        precisa seguir as regras do CAU, que pedem o responsável técnico, o título e o registro em toda peça
        dirigida ao público.</p>

        {caixa('<p><strong>Resposta rápida:</strong> anuncie só os serviços que você quer vender, na região em que '
               'atende, para buscas de quem quer contratar. Bloqueie buscas de curso, vaga, planta grátis e '
               'programa de desenho. Leve cada anúncio para a página do serviço, com portfólio e contato à vista, '
               'e siga a Resolução CAU/BR nº 75/2014 na divulgação.</p>')}

        <h2>1. Quando o anúncio faz sentido para um escritório</h2>
        <p>O anúncio acelera o que já funciona; ele não conserta um escritório sem tempo para atender ou sem
        página para mostrar. Faz sentido quando existe capacidade para novos projetos, um serviço bem definido
        para vender, como projeto residencial, reforma ou interiores, e uma página que explica esse serviço com
        portfólio. A concorrência pelo cliente que está decidindo existe: pelos dados públicos de CNPJ de
        novembro de 2026, o código {_cnae("7111100", "7111-1/00")} (serviços de arquitetura) reunia 45.584
        empresas ativas, sem contar quem atua como pessoa física.</p>

        <h2>2. As buscas que valem e as que só gastam</h2>
        <p>Vale anunciar para quem procura contratar: "arquiteto em [cidade]", "projeto de casa", "projeto de
        interiores", "reforma de apartamento com arquiteto", "projeto comercial". Não vale pagar por quem
        procura estudar ou fazer sozinho: curso de arquitetura, faculdade, salário, vaga, estágio, planta pronta,
        planta grátis e programa de desenho. O Google Ads permite bloquear essas palavras, e esse bloqueio é o
        que separa uma verba bem usada de uma verba que some em cliques de estudante.</p>

        {tabela(
            ["Busca", "Vale anunciar?", "Por quê"],
            [
                ["arquiteto em [sua cidade]", "Sim", "Quem pesquisa assim quer contratar alguém da região"],
                ["projeto de casa térrea", "Sim, com a página de projeto residencial", "A pessoa vai construir e procura quem projete"],
                ["design de interiores para apartamento", "Sim, se você faz interiores", "Serviço definido, com começo e fim"],
                ["quanto custa projeto de arquitetura", "Sim, com página que explica do que depende o valor", "Quem pergunta o preço está perto de decidir"],
                ["planta de casa grátis", "Não", "Procura um modelo pronto, não um projeto"],
                ["curso de arquitetura", "Não", "É estudante, não cliente"],
            ])}

        <h2>3. Anuncie só onde você atende</h2>
        <p>Projeto de arquitetura costuma exigir visita, reunião e acompanhamento. Anunciar para o estado inteiro
        traz contato de quem você não vai conseguir atender bem. Limite o anúncio à sua cidade e às cidades
        vizinhas onde você realmente trabalha, e ajuste o horário dos anúncios ao horário em que alguém pode
        responder.</p>

        <h2>4. Uma página para cada serviço anunciado</h2>
        <p>Quem clica em "projeto de interiores" e cai na página inicial do escritório, cheia de projetos de
        casas de campo, vai embora. Cada anúncio precisa levar para a página do serviço anunciado, com projetos
        daquele tipo, explicação simples de como funciona o trabalho, as etapas e o tempo médio, e o contato à
        vista. Essa página, a landing page, é a peça que mais muda o resultado do anúncio. Veja a
        {link('/criacao-de-landing-page/', 'criação de landing page para anúncios')}.</p>

        <h2>5. O que o CAU exige na divulgação</h2>
        <p>A {CAU_75} determina que a divulgação de projeto, obra ou serviço de arquitetura em qualquer meio
        dirigido ao público traga o responsável técnico, o título profissional, o número de registro no CAU e a
        atividade desenvolvida (art. 11), com letras no mínimo do mesmo tamanho das usadas para os demais
        profissionais da peça (art. 12). Na página de destino essas informações cabem com folga. Para anúncios
        de texto curto, vale confirmar com o CAU do seu estado a melhor forma de aplicar a regra.</p>

        <h2>6. Transparência no lugar da reserva técnica</h2>
        <p>O {CAU_52} proíbe receber comissão, vantagem ou presente de fornecedores dos seus clientes (regra
        3.2.16), a chamada reserva técnica. Isso pode virar argumento no anúncio e na página: honorário
        combinado com o cliente, por escrito, e indicação de fornecedores feita pelo que é melhor para o
        projeto. Para muita gente que vai construir pela primeira vez, essa clareza pesa na escolha.</p>

        <h2>7. Portfólio que convence quem clicou</h2>
        <p>A página do anúncio precisa mostrar projetos parecidos com o que a pessoa procura, com fotos de
        qualidade e o contexto de cada um: qual era o problema, o que foi feito e como ficou. Mostrar projeto de
        cliente pede autorização por escrito, e as fotos da obra pronta também. Portfólio organizado por tipo de
        projeto deixa claro, em poucos segundos, que você já resolveu um caso como o dela.</p>

        <h2>8. Quanto investir para começar</h2>
        <p>A verba do anúncio é paga direto ao Google, e o valor certo depende da cidade, da concorrência e do
        serviço anunciado. O mais seguro é começar com um valor que você aceita usar como teste por algumas
        semanas, medir quantos contatos de verdade chegaram e só então aumentar. Escritório que anuncia tudo ao
        mesmo tempo, com verba pequena, não aprende nada. Veja
        {link('/blog/quanto-investir-em-trafego-pago/', 'quanto investir em tráfego pago')}.</p>

        <h2>9. Responda rápido e meça cada contato</h2>
        <p>Quem pede orçamento para projeto costuma falar com mais de um escritório. Responder no mesmo dia,
        de preferência em minutos, já coloca você na frente. Cada mensagem, ligação e formulário precisa chegar
        com a origem marcada, para saber qual anúncio e qual página trazem reunião marcada, e não apenas
        cliques. É essa medição que mostra se o anúncio está pagando o próprio custo.</p>

        <h2>10. O anúncio não substitui a reputação</h2>
        <p>Quando o anúncio para, os contatos param. O que continua trabalhando é o perfil do escritório no
        Google, com fotos dos projetos e avaliações de quem já contratou, e o site com uma página por serviço,
        que o Google mostra de graça para quem pesquisa. O melhor cenário é o anúncio trazendo os primeiros
        projetos enquanto essa reputação cresce. Veja o {link('/site-otimizado-para-seo/', 'site otimizado para o Google')}.</p>

        <h2>Por onde começar a anunciar o escritório de arquitetura?</h2>
        <p>Escolha um serviço só para começar, o que você mais quer vender. Monte a página desse serviço com
        portfólio e as informações que o CAU pede, defina a região e as buscas a bloquear e comece com uma verba
        de teste. Com os primeiros contatos medidos, ajuste e só então amplie. As frentes juntas estão em
        {link('/marketing-para-arquitetos/', 'marketing para arquitetos')}.</p>
""",
        "faq": [
            ("Arquiteto pode anunciar no Google Ads?",
             "Pode. A Resolução CAU/BR nº 75/2014 pede que a divulgação traga o responsável técnico, o título "
             "profissional, o registro no CAU e a atividade desenvolvida."),
            ("Quanto um arquiteto deve investir em Google Ads?",
             "Depende da cidade e da concorrência. A verba é paga direto ao Google; o mais seguro é começar com um "
             "valor de teste, medir os contatos e só então aumentar."),
            ("Google Ads ou Instagram para arquiteto?",
             "O Google Ads aparece para quem já está procurando um arquiteto; o Instagram mostra o trabalho para "
             "quem ainda não está procurando. Para contato rápido, a busca no Google costuma vir primeiro."),
            ("Quais buscas o arquiteto deve bloquear no anúncio?",
             "As de quem não vai contratar: curso, faculdade, vaga, estágio, salário, planta grátis, planta pronta e "
             "programa de desenho."),
        ],
        "cta": ("Tem um escritório de arquitetura e quer mais projetos? Me conte a sua cidade e o serviço que você "
                "mais quer vender. Em até 24 horas eu te digo se o anúncio faz sentido e por onde começar.",
                wa("Olá, Renan! Sou arquiteto e quero anunciar o meu escritório no Google."),
                "Quero mais projetos"),
    },
]
