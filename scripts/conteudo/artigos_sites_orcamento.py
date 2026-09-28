# -*- coding: utf-8 -*-
"""
Artigos de preço de site (28/09/2026).

Decisão do Renan: o site não mostra preço fechado de site, landing page ou loja.
Estes artigos respondem "quanto custa" com FAIXAS DE MERCADO e levam ao
orçamento sob medida no WhatsApp. Nenhum valor aqui é tabela da RCB.

Canibalização: este artigo mira a busca nacional ("quanto custa um site",
"valor de um site"). A busca local ("quanto custa um site em Goiânia") é da
página /criacao-de-sites-goiania/, que este artigo linka.
"""
from rcb_artigo import caixa, tabela, link

DATA = "2026-09-28"
WHATS_ORCAMENTO = ("https://wa.me/5562991161040?text=Ol%C3%A1%2C%20Renan%21%20Li%20o%20artigo%20"
                   "sobre%20quanto%20custa%20um%20site%20e%20quero%20um%20or%C3%A7amento%20para%20o%20meu.")


ARTIGOS = [
    {
        "slug": "quanto-custa-um-site",
        "h1": "Quanto custa um site em 2026? Valores reais e o que muda o preço",
        "title": "Quanto custa um site em 2026? Valores e o que muda o preço",
        "desc": ("Quanto custa um site em 2026: de uns R$ 100 por mês a mais de R$ 10 mil. Veja as faixas de "
                 "preço, os custos escondidos e como pedir um orçamento justo."),
        "cat": "Criação de sites",
        "data": DATA,
        "trilha_extra": ("/criacao-de-sites-goiania/", "Criação de sites"),
        "corpo": f"""
        <p>Um site custa de <strong>uns R$ 100 por mês</strong>, quando é montado em plataforma pronta, até
        <strong>mais de R$ 10 mil</strong>, quando é um projeto grande com muitas páginas, loja virtual ou
        integrações. A maior parte dos sites de empresas locais fica no meio desse caminho, na faixa de alguns
        milhares de reais.</p>

        <p>A diferença não é capricho de quem cobra. Ela aparece no que o site entrega: quantas páginas ele
        tem, quem escreve os textos, se ele foi montado para aparecer no Google e se continua recebendo
        cuidado depois de publicado.</p>

        {caixa('<p><strong>Resposta rápida:</strong> site de plataforma pronta sai a partir de uns R$ 100 por mês. '
               'Site institucional próprio costuma ficar na casa de alguns milhares de reais. Site com muitas '
               'páginas de serviço, loja virtual ou integrações passa de R$ 5 mil e pode chegar a R$ 10 mil ou mais. '
               'O valor certo só sai depois de entender o projeto — por isso orçamento sério começa com perguntas, '
               'não com tabela.</p>')}

        <h2>Quanto custa um site: as faixas de preço do mercado</h2>

        <p>As faixas abaixo são o que você vai encontrar ao pedir orçamento no Brasil hoje. Elas não são uma
        tabela oficial — ninguém regula preço de site — mas ajudam a entender se um valor está fora da
        realidade para o que foi prometido.</p>

        {tabela(
            ["Tipo de site", "Faixa comum", "O que costuma entregar"],
            [
                ["Plataforma pronta (mensalidade)", "A partir de uns R$ 100/mês",
                 "Modelo pronto, uma página, pouca personalização. Some se a mensalidade parar."],
                ["Landing page", "De algumas centenas a alguns milhares de reais",
                 "Página única focada em uma oferta, usada em campanha de anúncio."],
                ["Site institucional", "Alguns milhares de reais",
                 "Início, serviços, sobre e contato no seu domínio, com botão de WhatsApp."],
                ["Site feito para aparecer no Google", "De R$ 5 mil a R$ 10 mil ou mais",
                 "Uma página por serviço e por região, textos pensados para a busca, acompanhamento."],
                ["Loja virtual", "Varia muito com o catálogo",
                 "Produtos, carrinho, pagamento e frete configurados."],
            ],
            "Faixas aproximadas de mercado, sem incluir domínio, hospedagem e anúncios pagos.")}

        <h2>O que muda o preço de um site</h2>

        <p>Dois orçamentos para "um site" podem estar falando de coisas completamente diferentes. Estes são
        os pontos que mais mexem no valor — e que você deve perguntar a quem está orçando.</p>

        <h3>1. Quantas páginas o site precisa ter</h3>
        <p>Uma clínica com oito especialidades precisa de oito páginas de serviço para ser encontrada em cada
        uma delas. Um profissional liberal pode precisar de três. Cada página é texto, estrutura e revisão.
        Veja {link('/blog/paginas-que-empresa-local-precisa-no-site/', 'quais páginas uma empresa local precisa ter')}.</p>

        <h3>2. Quem escreve os textos e produz as fotos</h3>
        <p>Se você entrega tudo pronto, o trabalho é montar. Se a agência escreve do zero, pesquisa o que o seu
        cliente procura e produz imagens, o trabalho é outro. É aqui que muitos orçamentos baratos economizam:
        o site vem com texto genérico, igual ao de centenas de outras empresas.</p>

        <h3>3. Se o site é feito para aparecer no Google</h3>
        <p>Site bonito e site encontrado são coisas diferentes. Para aparecer, o site precisa dizer com clareza o
        que a empresa faz e onde atende, carregar rápido no celular e estar ligado ao Google Perfil da Empresa.
        Isso dá mais trabalho — e é o que separa o site que traz cliente do site que fica parado. Entenda
        {link('/blog/site-bonito-nao-aparece-no-google/', 'por que site bonito nem sempre aparece no Google')}.</p>

        <h3>4. Funções extras</h3>
        <p>Agendamento online, área do cliente, integração com sistema, catálogo com centenas de produtos,
        pagamento pelo site. Cada função é um pedaço de projeto à parte e aumenta o preço.</p>

        <h3>5. O que acontece depois da entrega</h3>
        <p>Alguns orçamentos entregam o site e encerram. Outros incluem ajustes, novos textos e acompanhamento
        mensal. Os dois modelos são válidos, mas é preciso comparar igual com igual. Sobre esse ponto, leia
        {link('/blog/quanto-custa-manter-site-otimizado-seo/', 'quanto custa manter um site depois de pronto')}.</p>

        <h2>Custos que quase ninguém coloca no orçamento</h2>

        <p>O valor da criação não é o único gasto. Antes de fechar, pergunte quem paga cada um destes itens:</p>
        <ul>
          <li><strong>Domínio</strong> — o endereço do site. Um ".com.br" é registrado no
          <a href="https://registro.br/" target="_blank" rel="noopener noreferrer">Registro.br</a> e tem
          renovação anual. Ele deve ficar no <strong>seu nome</strong>, não no da agência.</li>
          <li><strong>Hospedagem</strong> — o lugar onde o site fica guardado. Pode ser mensal ou anual.</li>
          <li><strong>E-mail profissional</strong> — o "contato@suaempresa.com.br", quando você quer.</li>
          <li><strong>Mensalidade de plataforma</strong> — em sites de modelo pronto, se parar de pagar, o site
          sai do ar.</li>
          <li><strong>Anúncios</strong> — se o site for usado em campanha de Google Ads ou Meta Ads, a verba do
          anúncio é paga à parte, direto para o Google ou para o Meta.</li>
        </ul>

        {caixa('<p><strong>Atenção:</strong> peça por escrito que o domínio e o acesso ao site fiquem em seu nome. '
               'Empresa que perde o acesso ao próprio domínio quando troca de fornecedor perde junto o que '
               'conquistou no Google.</p>')}

        <h2>Site barato vale a pena?</h2>

        <p>Às vezes vale. Se a sua empresa só precisa de um cartão de visita na internet — um endereço para
        mandar no WhatsApp — um site simples resolve. O problema é comprar o site barato esperando que ele traga
        cliente pelo Google. Ele quase nunca traz, porque não foi feito para isso. Tem uma análise completa em
        {link('/blog/site-barato-empresa-local-vale-a-pena/', 'site barato: quando vale e quando é dinheiro jogado fora')}.</p>

        <p>O mesmo raciocínio vale para plataforma pronta contra site próprio. Compare as opções em
        {link('/blog/site-wix-wordpress-ou-site-otimizado-seo/', 'Wix, WordPress ou site feito para o Google')}.</p>

        <h2>Quanto custa uma landing page e uma loja virtual</h2>

        <p><strong>Landing page</strong> é uma página única, feita para uma oferta só, geralmente para receber quem
        clica num anúncio. Por ser uma página, costuma custar menos que um site completo — mas o texto precisa
        ser muito bem escrito, porque cada clique do anúncio é pago. Landing page ruim faz o anúncio
        parecer caro. Veja como funciona a
        {link('/criacao-de-landing-page-goiania/', 'criação de landing page')}.</p>

        <p><strong>Loja virtual</strong> é o projeto com maior variação de preço. Uma loja com vinte produtos e uma
        com dois mil são trabalhos diferentes. Entram na conta: cadastro dos produtos, fotos, formas de
        pagamento, cálculo de frete e as páginas de produto pensadas para aparecer no Google. Veja como funciona a
        {link('/criacao-de-loja-virtual-goiania/', 'criação de loja virtual')}.</p>

        <h2>Como pedir um orçamento de site e comparar direito</h2>

        <p>O jeito mais rápido de receber um orçamento justo é mandar as informações certas logo na primeira
        mensagem. Com isso, quem orça consegue dizer o valor sem chutar:</p>
        <ol>
          <li>O que a sua empresa faz e quais serviços dão mais dinheiro.</li>
          <li>Em que cidade ou região você quer ser encontrado.</li>
          <li>Se já tem site, Instagram ou perfil no Google — mande os endereços.</li>
          <li>Se precisa de alguma função extra: agendamento, loja, área do cliente.</li>
          <li>Se você tem textos e fotos ou se precisa que sejam produzidos.</li>
        </ol>

        <p>Na hora de comparar, coloque os orçamentos lado a lado e confira: quantas páginas cada um entrega,
        quem escreve os textos, se o domínio fica no seu nome, o que acontece depois da entrega e se o site
        foi pensado para aparecer no Google. Preço sozinho não diz qual é o mais barato — o site que não traz
        cliente é o mais caro de todos.</p>

        <h2>Quanto custa um site na RCB</h2>

        <p>Na RCB, site sob medida, landing page e loja virtual são orçados projeto a projeto, porque dois
        projetos nunca são iguais, e preço de tabela obriga a cobrar a mais de quem precisa de pouco ou entregar
        a menos para quem precisa de muito. Funciona assim: você me chama no WhatsApp, conta o que a empresa faz, e em até 24 horas recebe o valor
        exato do seu projeto — junto com uma olhada em quem está aparecendo na sua frente no Google hoje.</p>

        <p>Se a sua empresa é de Goiânia ou região, veja como funciona a
        {link('/criacao-de-sites-goiania/', 'criação de sites em Goiânia')}, com site, landing page e loja virtual.</p>
""",
        "faq": [
            ("Quanto custa um site simples?",
             "Um site simples de plataforma pronta sai a partir de uns R$ 100 por mês. Um site institucional "
             "próprio, com poucas páginas, costuma ficar na faixa de alguns milhares de reais. O valor exato "
             "depende de quantas páginas, de quem escreve os textos e se o site é feito para aparecer no Google."),
            ("Quanto custa um site profissional para empresa?",
             "Um site profissional para empresa, com uma página por serviço e textos pensados para o Google, "
             "costuma passar de R$ 5 mil e pode chegar a R$ 10 mil ou mais em projetos maiores. O orçamento certo "
             "sai depois de entender quantos serviços, cidades e funções o site precisa ter."),
            ("Além da criação, o site tem custo mensal?",
             "Sim. Domínio e hospedagem são pagos todo ano ou todo mês, e sites de plataforma pronta cobram "
             "mensalidade. Se o site tiver acompanhamento, com novos textos e ajustes, esse serviço também é "
             "cobrado à parte. Anúncios pagos no Google ou no Meta são outro gasto, pago direto às plataformas."),
            ("Quanto custa uma landing page?",
             "Uma landing page costuma custar menos que um site completo, por ser uma página só. Fica na faixa "
             "de algumas centenas a alguns milhares de reais, conforme o texto, o design e as integrações com "
             "anúncio e WhatsApp."),
            ("Por que os orçamentos de site variam tanto?",
             "Porque \"site\" pode ser uma página de modelo pronto ou um projeto com dezenas de páginas escritas "
             "do zero. A diferença está na quantidade de páginas, na produção de textos e fotos, nas funções "
             "extras e no trabalho para o site aparecer no Google."),
        ],
        "cta": ("Quer saber quanto fica o seu site? Me conte o que a sua empresa faz e em que região atende. "
                "Em até 24 horas você recebe o valor do seu projeto e uma análise de quem aparece na sua frente "
                "no Google.",
                WHATS_ORCAMENTO, "Pedir meu orçamento grátis"),
    },
]
