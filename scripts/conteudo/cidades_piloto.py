# -*- coding: utf-8 -*-
"""
Conteúdo local das 3 páginas-piloto de cidade (decisão de 12/08/2026).

Por que este arquivo existe: `gerar-paginas-cidades.py` sobrescreve as páginas a
cada execução. Texto escrito à mão dentro do HTML seria apagado na primeira
regeração. Então o texto único mora AQUI e o gerador o injeta.

Regra editorial destas páginas (não afrouxar):
  - Nada de escritório, endereço, equipe, cliente, case, depoimento ou número
    inventado na cidade. A RCB atende de Goiânia, online, e isso é dito.
  - Os cases reais (Goiânia) aparecem como prova de CAPACIDADE, com a praça
    explicitada — nunca sugerindo que aconteceram na cidade da página.
  - As consultas do Search Console são matéria-prima do texto, não enfeite:
    cada página responde à intenção que ela de fato recebeu.

Cada entrada é uma função que recebe o contexto da cidade (números de CNPJ já
formatados, blocos de bairros/ramos e os links para as money pages) e devolve o
dicionário que o gerador renderiza.
"""


# ---------------------------------------------------------------------------
# RIO DE JANEIRO
# Sinal real (GSC 12/05-09/08/2026): 28 impressões, 6 consultas comerciais.
# "consultoria seo rj" (8) x "consultoria seo rio de janeiro" (7) — a busca se
# divide quase meio a meio entre a sigla e o nome por extenso. Esse é o gancho
# que nenhuma outra cidade do cluster tem.
# ---------------------------------------------------------------------------
def rio_de_janeiro(ctx):
    return {
        "titulo": "Consultoria de SEO no Rio de Janeiro (RJ) | RCB",
        "desc": (
            "Consultoria de SEO no Rio de Janeiro: no Maps, quem decide é a zona, "
            "não a cidade. Google Perfil da Empresa, site e conteúdo. Online, a partir de R$ 1.997."
        ),
        "eyebrow": "Rio de Janeiro · RJ",
        "h1": "Consultoria de SEO no Rio de Janeiro: quem aparece na busca da sua zona leva o cliente",
        "subtitulo": (
            "No Rio, aparecer “na cidade” não quer dizer quase nada. Quem procura dentista, "
            "clínica ou serviço no Google recebe resultados do próprio pedaço — e um cliente de "
            "Copacabana não atravessa a cidade para resolver o que resolve na esquina. "
            "A consultoria organiza sua presença para a busca que realmente acontece: a da sua zona."
        ),
        "painel_titulo": "O que a busca do Rio tem de diferente",
        "painel_html": f"""
          <ul class="audit-list">
            <li><strong>“RJ” e “Rio de Janeiro”</strong> são duas buscas, com volumes parecidos.</li>
            <li>A disputa real acontece <strong>por zona</strong>, não pelo município inteiro.</li>
            <li><strong>{ctx['ativas']}</strong> empresas ativas — concorrência densa em quase todo ramo.</li>
            <li>Endereço em sala comercial compartilhada é o erro nº 1 no Maps.</li>
          </ul>""",
        "secoes": [
            f"""
    <section class="solution-section" aria-labelledby="rj-sigla">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Achado dos nossos próprios dados</div>
          <h2 id="rj-sigla" class="section-title">“RJ” e “Rio de Janeiro” são duas buscas diferentes — e muita empresa só atende uma</h2>
          <p>Esta página está no ar desde julho de 2026 e o Search Console mostrou uma coisa que
          vale para qualquer negócio carioca: entre as pessoas que chegaram até aqui pesquisando
          consultoria de SEO, <strong>metade escreveu “RJ” e metade escreveu “Rio de Janeiro”</strong>.
          A busca se divide quase meio a meio entre a sigla e o nome por extenso.</p>
          <p>Parece detalhe, mas não é. A maior parte dos sites e perfis do Google escreve só uma
          das formas — quase sempre a extensa. Quem faz isso conversa com metade da demanda e
          entrega a outra metade para o concorrente, sem nunca saber que perdeu.</p>
          <p>A correção é simples e não é truque: o nome do negócio no
          {ctx['link_gmn']}, o título das páginas do site e o texto precisam usar as duas formas
          <em>naturalmente</em>, cada uma no lugar em que soa normal. Repetir “RJ RJ Rio de Janeiro RJ”
          na mesma frase não ajuda — o Google entende sinônimo há anos, e o texto forçado espanta
          o leitor, que é quem de fato liga.</p>
        </div>
        <div class="diagnostic-card">
          <h3>O que revisar hoje no seu material</h3>
          <ul class="audit-list">
            <li>Nome e descrição do perfil no Google.</li>
            <li>Título e subtítulo da página inicial.</li>
            <li>Rodapé com endereço completo.</li>
            <li>Textos de contato e de “onde atendemos”.</li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:1rem;">Fonte da divisão entre
          “RJ” e “Rio de Janeiro”: Search Console da própria RCB, consultas que trouxeram visitantes
          a esta página entre 12/05 e 09/08/2026.</p>
        </div>
      </div>
    </section>""",
            """
    <section class="metodo" aria-labelledby="rj-zona">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Geografia da busca</div>
          <h2 id="rj-zona" class="section-title">No Rio, “concorrente” depende da zona — e o Google sabe disso</h2>
          <p class="section-desc">A cidade é dividida em Zona Sul, Centro, Zona Norte e Zona Oeste,
          separadas por túneis, morros e, do outro lado da baía, Niterói. Quando alguém pesquisa um
          serviço no celular, o Google mostra o que está por perto de quem pesquisa. Por isso duas
          empresas do mesmo ramo, ambas “no Rio de Janeiro”, muitas vezes nem se cruzam nos
          resultados: elas disputam pedaços diferentes da cidade.</p>
        </div>
        <div class="metodo-steps">
          <div class="metodo-step"><div class="step-number">1</div><h3>Descubra sua zona real</h3><p>De onde vêm seus clientes hoje? Zona Sul, Barra, Centro, Zona Norte? A resposta muda tudo o que vem depois.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">2</div><h3>Ajuste o raio</h3><p>Perfil com área de atendimento larga demais dilui o sinal. Um negócio de bairro compete melhor sendo do bairro.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">3</div><h3>Fale a língua do lugar</h3><p>Página que cita a rua, o ponto de referência e o acesso converte mais que página que só repete “Rio de Janeiro”.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">4</div><h3>Meça por origem</h3><p>Relatório que mostra de onde vieram as ligações e os pedidos de rota, não só quantos foram.</p></div>
        </div>
      </div>
    </section>""",
            f"""
    <section class="solution-section" aria-labelledby="rj-erros">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">Problemas comuns no Rio</div>
          <h2 id="rj-erros" class="section-title">O que mais derruba empresa carioca no Google Maps</h2>
          <p><strong>Sala comercial dividida com dezenas de CNPJs.</strong> É comum no Centro e na
          Barra: vários negócios registrados no mesmo número, mesmo andar, às vezes na mesma sala.
          O Google trata endereço repetido com desconfiança e pode suspender ou esconder o perfil.
          Quem trabalha assim precisa deixar claro sala e andar, e manter o dado idêntico em todo
          lugar onde a empresa aparece.</p>
          <p><strong>Horário que não corresponde à realidade.</strong> Feriado municipal, verão,
          dia de jogo, dia de chuva forte com trânsito parado. Perfil que diz
          “aberto” e não atende gera avaliação ruim — e avaliação ruim por horário errado é o tipo
          de estrago que leva meses para limpar.</p>
          <p><strong>Categoria genérica.</strong> “Clínica” em vez de “Clínica odontológica”;
          “Loja” em vez do que a loja de fato vende. A categoria é o campo que mais pesa para o
          Google decidir em quais buscas você aparece — e é o mais negligenciado.</p>
          <p><strong>Avaliação sem resposta.</strong> Num mercado tão disputado, o perfil que
          responde todas as avaliações — inclusive as ruins, com educação — passa na frente do que
          tem nota parecida e silêncio.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Onde novas empresas estão abrindo no Rio</h3>
          {ctx['bairros_lista']}
          <h3 style="margin-top:1.25rem;">Ramos que mais abriram (90 dias)</h3>
          <ul class="audit-list">
{ctx['ramos_html']}
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Fonte: <a href="https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj" target="_blank" rel="noopener noreferrer">dados públicos de CNPJ da Receita Federal</a>, referência {ctx['ref']}. Concentração de aberturas indica onde nasce concorrência — não mede quem aparece no Google.</p>
        </div>
      </div>
    </section>""",
            f"""
    <section class="solution-section" aria-labelledby="rj-agencia">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Agência ou consultor</div>
          <h2 id="rj-agencia" class="section-title">O Rio tem muita agência de SEO. Isto aqui é outra coisa</h2>
          <p class="section-desc">A RCB não é agência: é um consultor só, o Renan, que atende um
          número limitado de clientes por vez. Na prática isso significa três diferenças. Quem
          analisa o seu caso é quem executa — não há passagem de bastão para outra pessoa depois
          da reunião de venda. O preço é
          <a href="#pacotes">público e está nesta página</a>, sem proposta de trinta slides. E o
          atendimento ao Rio é online, por vídeo, com acesso aos seus dados reais do Google.</p>
          <p class="section-desc">Não existe escritório da RCB no Rio de Janeiro, nem equipe na
          cidade — e você não precisa disso. O trabalho de SEO local acontece dentro do seu perfil
          do Google, do seu site e do seu conteúdo, e é feito igual à distância. O que muda de
          cidade para cidade é a leitura da concorrência, e essa leitura eu faço com os dados da
          sua praça. Se o que você procura é alguém para visitar sua loja toda semana, sou honesto:
          não é o meu serviço.</p>
          <p class="section-desc">Como prova de capacidade, os {ctx['link_cases']} são de clientes
          atendidos em Goiânia — inclusive um primeiro lugar no Google Maps em disputa contra
          concorrentes muito maiores em número de avaliações. São casos de Goiânia, não do Rio, e
          estão descritos com os números reais.</p>
        </div>
      </div>
    </section>""",
        ],
        "faq": [
            ("Consultoria de SEO no Rio de Janeiro funciona sendo feita de fora da cidade?",
             "Funciona, porque o trabalho acontece onde o cliente pesquisa: no seu perfil do Google, no seu site e no seu conteúdo. O que exige conhecimento local é a leitura da concorrência — quem aparece hoje na sua zona, com qual categoria e com quantas avaliações —, e isso se analisa com os dados da própria busca. O que eu não faço é fingir presença física: não há escritório nem equipe da RCB no Rio."),
            ("Devo aparecer para “Rio de Janeiro” ou para o meu bairro?",
             "Para os dois, em camadas. O perfil do Google e a página principal do site cobrem a cidade; páginas e conteúdos específicos cobrem a sua zona e os bairros de onde vêm seus clientes. Tentar aparecer para a cidade inteira sem base de bairro costuma ser mais caro e mais lento — e, num mercado do tamanho do Rio, quase sempre perde para quem é claramente do pedaço."),
            ("Minha empresa fica em sala comercial com outros CNPJs. Isso atrapalha?",
             "Pode atrapalhar, e é comum no Centro e na Barra. O Google desconfia de endereços repetidos e chega a suspender perfis nesses casos. Dá para trabalhar direito assim: informar sala e andar, manter o endereço idêntico em todos os lugares onde a empresa aparece e comprovar a operação quando o Google pedir verificação. É um dos primeiros pontos que eu checo no diagnóstico."),
            ("Quanto tempo até aparecer melhor no Rio de Janeiro?",
             "Os primeiros sinais no Maps costumam surgir em semanas — perfil arrumado, categoria certa, fotos e avaliações organizadas rendem rápido. Ganhar posição em buscas disputadas leva meses e depende do quanto seus concorrentes já fazem. No Rio, em ramos como estética, odontologia e advocacia, a concorrência já é bem trabalhada: quem promete primeira página em 30 dias está vendendo o que não pode entregar."),
        ],
        "cta_titulo": "Sua empresa aparece na busca da sua zona no Rio?",
        "cta_texto": (
            "Peça o diagnóstico gratuito. Eu analiso seu perfil no Google, seu site e os "
            "concorrentes que aparecem na frente da sua empresa na sua região do Rio — e te digo "
            "o que priorizar, antes de qualquer proposta."
        ),
        "whats": "Olá, Renan. Tenho uma empresa no Rio de Janeiro e quero um diagnóstico gratuito para aparecer melhor no Google.",
    }


# ---------------------------------------------------------------------------
# CAMPINAS
# Sinal real (GSC): "agência de seo em campinas" (3), "agencia seo campinas" (1),
# "consultor seo campinas" (1). A praça procura AGÊNCIA — e a RCB não é agência.
# A página trata isso de frente, em vez de fingir que a consulta não existe.
# ---------------------------------------------------------------------------
def campinas(ctx):
    return {
        "titulo": "Consultoria de SEO em Campinas (SP) | RCB",
        "desc": (
            "Consultoria de SEO em Campinas: seu cliente pode estar em Valinhos ou Sumaré. "
            "Perfil no Google, site e conteúdo para a RMC. Online, a partir de R$ 1.997."
        ),
        "eyebrow": "Campinas · SP",
        "h1": "Consultoria de SEO em Campinas: apareça para toda a região, não só para o município",
        "subtitulo": (
            "Quem vende em Campinas raramente vende só em Campinas. O cliente mora em Valinhos, "
            "trabalha em Hortolândia, compra em Barão Geraldo. Se o seu Google está configurado "
            "como se a cidade acabasse na divisa, você está invisível para boa parte de quem "
            "poderia comprar de você."
        ),
        "painel_titulo": "O mercado de Campinas e da região",
        "painel_html": f"""
          <ul class="audit-list">
            <li><strong>{ctx['ativas']}</strong> empresas ativas só no município.</li>
            <li>A Região Metropolitana reúne <strong>22 cidades</strong> e mais de <strong>451 mil</strong> pequenos negócios.</li>
            <li>Serviços é o setor mais numeroso da região.</li>
            <li>Polo de tecnologia: concorrente aqui costuma já fazer SEO.</li>
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Dados da RMC: <a href="https://www.crsaopaulo.com.br/noticia/regiao-de-campinas-reune-mais-de-451-mil-pequenos-negocios-56-7-sao-meis" target="_blank" rel="noopener noreferrer">levantamento sobre pequenos negócios da região</a>.</p>""",
        "secoes": [
            f"""
    <section class="solution-section" aria-labelledby="cps-rmc">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">O erro que custa mais caro aqui</div>
          <h2 id="cps-rmc" class="section-title">Em Campinas, seu cliente pode estar em Valinhos — e o seu Google precisa saber disso</h2>
          <p>A Região Metropolitana de Campinas junta 22 cidades e mais de 451 mil pequenos
          negócios, com o setor de serviços à frente. Na prática, a vida econômica ignora a divisa:
          gente que mora em Valinhos ou Vinhedo faz compras e consultas em Campinas, e empresas de
          Campinas atendem Sumaré, Hortolândia, Indaiatuba e Paulínia todo dia.</p>
          <p>O Google só entende isso se você contar. E há duas formas de contar, que servem a
          negócios diferentes:</p>
          <p><strong>Se o cliente vai até você</strong> (clínica, loja, escritório), o perfil precisa
          ter endereço fixo e visível. Nesse caso, quem manda é a distância entre quem pesquisa e a
          sua porta — e o caminho para crescer é ser forte no seu pedaço de Campinas antes de sonhar
          com a região inteira.</p>
          <p><strong>Se você vai até o cliente</strong> (serviços, manutenção, consultoria, obra), o
          perfil pode declarar área de atendimento e listar as cidades que você realmente cobre.
          O erro clássico aqui é marcar a região inteira “por garantia”: área larga demais dilui o
          sinal e você acaba não aparecendo bem em lugar nenhum.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Onde novas empresas estão abrindo em Campinas</h3>
          {ctx['bairros_lista']}
          <h3 style="margin-top:1.25rem;">Ramos que mais abriram (90 dias)</h3>
          <ul class="audit-list">
{ctx['ramos_html']}
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Fonte: <a href="https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj" target="_blank" rel="noopener noreferrer">dados públicos de CNPJ da Receita Federal</a>, referência {ctx['ref']}.</p>
        </div>
      </div>
    </section>""",
            f"""
    <section class="metodo" aria-labelledby="cps-tech">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Concorrência</div>
          <h2 id="cps-tech" class="section-title">Campinas é polo de tecnologia — o que isso muda para o seu SEO</h2>
          <p class="section-desc">A cidade abriga um dos maiores parques tecnológicos da América
          Latina e centenas de startups no entorno da Unicamp. Isso tem um efeito colateral direto
          para quem tem negócio local aqui: <strong>a régua é mais alta</strong>. É bem mais
          provável que o seu concorrente de Campinas já tenha site rápido, perfil do Google
          organizado e alguém cuidando disso do que em uma cidade média do interior.</p>
          <p class="section-desc">Isso não é motivo para desistir — é motivo para parar de fazer
          pela metade. Em mercado trabalhado, quem ganha não é quem faz uma ação genial, é quem faz
          o básico completo e não abandona: perfil sempre atualizado, avaliações pedidas de forma
          sistemática, páginas que respondem perguntas reais, e medição mensal do que mudou.</p>
        </div>
        <div class="metodo-steps">
          <div class="metodo-step"><div class="step-number">1</div><h3>Mapa da disputa</h3><p>Quem aparece hoje nas buscas do seu serviço em Campinas, com quantas avaliações e qual categoria.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">2</div><h3>Perfil e alcance</h3><p>{ctx['link_gmn']}, com decisão consciente entre endereço fixo e área de atendimento na RMC.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">3</div><h3>Páginas por serviço</h3><p>Uma página boa por serviço vale mais que dez páginas iguais com o nome de dez cidades trocado.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">4</div><h3>Rotina</h3><p>Relatório mensal simples: quem viu, quem ligou, quem pediu rota, quem chamou no WhatsApp.</p></div>
        </div>
      </div>
    </section>""",
            f"""
    <section class="solution-section" aria-labelledby="cps-agencia">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Transparência</div>
          <h2 id="cps-agencia" class="section-title">Em Campinas quase todo mundo procura “agência de SEO”. Eu não sou agência</h2>
          <p class="section-desc">Isso não é suposição: as buscas que trouxeram gente até esta
          página no último trimestre foram, em sua maioria, alguma variação de “agência de SEO em
          Campinas”. Então vale ser direto sobre a diferença, para você decidir com informação.</p>
          <p class="section-desc"><strong>Agência</strong> costuma ter equipe, atender muitas contas
          ao mesmo tempo, cobrar por contrato mais longo e distribuir seu projeto entre pessoas
          diferentes. Faz sentido quando o volume de trabalho é grande e constante — campanhas,
          várias unidades, produção pesada de conteúdo.</p>
          <p class="section-desc"><strong>Consultor</strong> — o caso da RCB — é uma pessoa só, com
          poucos clientes por vez. Quem analisa é quem executa, o preço está
          <a href="#pacotes">publicado nesta página</a> e você fala direto comigo, sem intermediário.
          Faz sentido para negócio local que precisa de presença bem feita e acompanhada, não de uma
          estrutura de agência.</p>
          <p class="section-desc">A {ctx['link_consultoria']} é a mesma dos atendimentos presenciais
          em Goiânia; para Campinas ela roda online, por vídeo. Os {ctx['link_cases']} publicados são
          de clientes de Goiânia — não tenho cliente em Campinas para citar, e não vou inventar um.</p>
        </div>
      </div>
    </section>""",
        ],
        "faq": [
            ("Consultor de SEO em Campinas atende também a região metropolitana?",
             "Sim, e para a maioria dos negócios essa é a decisão mais importante da configuração. Se você atende no seu endereço, o trabalho começa pelo seu pedaço de Campinas e cresce a partir dali. Se você se desloca até o cliente, o perfil do Google pode declarar as cidades da RMC que você realmente cobre — Valinhos, Sumaré, Hortolândia, Indaiatuba, Paulínia e as demais. O que não funciona é marcar a região inteira sem atender de verdade: dilui o sinal e piora o resultado."),
            ("Qual a diferença entre contratar uma agência de SEO em Campinas e um consultor?",
             "Agência tem equipe e atende muitas contas ao mesmo tempo; costuma valer quando o volume é grande e contínuo. Consultor é uma pessoa só, com poucos clientes por vez: quem analisa é quem executa, o preço é público e você fala direto com ele. A RCB é o segundo caso. Para negócio local que precisa do básico bem feito e mantido, costuma render mais por real investido."),
            ("Meu concorrente em Campinas já faz SEO. Ainda vale começar agora?",
             "Vale, mas com expectativa correta. Campinas é polo de tecnologia e a régua local é mais alta que a média do interior — é provável que seus concorrentes já tenham site decente e perfil organizado. Nesse cenário, ganho não vem de uma tacada, vem de constância: perfil sempre atualizado, avaliações pedidas de forma sistemática e páginas que respondem o que o cliente pergunta. Quem faz isso por seis meses seguidos passa quem fez tudo em um mês e abandonou."),
            ("Quanto custa a consultoria de SEO para uma empresa de Campinas?",
             "O mesmo dos demais atendimentos, sem taxa por distância, porque o trabalho é online: a partir de R$ 1.997 no pacote de entrada, que arruma o Google Perfil da Empresa de quem já tem site. Os quatro pacotes, com o que cada um inclui, estão nesta mesma página. Pagamento por Pix, combinado no WhatsApp, e garantia de 30 dias."),
        ],
        "cta_titulo": "Quer aparecer no Google em Campinas e na região?",
        "cta_texto": (
            "Peça o diagnóstico gratuito. Eu olho seu perfil no Google, seu site e quem está "
            "aparecendo na sua frente em Campinas e na RMC — e te mostro o que priorizar primeiro."
        ),
        "whats": "Olá, Renan. Tenho uma empresa em Campinas/SP e quero um diagnóstico gratuito para aparecer melhor no Google.",
    }


# ---------------------------------------------------------------------------
# PALMAS / TOCANTINS
# Sinal real (GSC): "seo local palmas" (2, pos 28,5) e "otimização para google
# meu negócio palmas" (1). São as ÚNICAS consultas de intenção local pura de todo
# o cluster de 199 cidades — e as mais próximas do que a RCB de fato vende.
# Por isso esta página é a única do cluster construída em torno do Perfil da
# Empresa, e não da consultoria genérica.
# ---------------------------------------------------------------------------
def palmas(ctx):
    return {
        "titulo": "SEO Local em Palmas (TO) e Google Perfil da Empresa | RCB",
        "desc": (
            "SEO local em Palmas (TO): endereço de quadra pode confundir o Google Maps. "
            "Perfil da Empresa configurado corretamente. Online, a partir de R$ 1.997."
        ),
        "eyebrow": "Palmas · TO",
        "h1": "SEO local em Palmas (TO): comece pelo endereço que o Google não entende",
        "subtitulo": (
            "Palmas é uma capital planejada, e o endereço daqui não se parece com o de nenhuma "
            "outra cidade grande do país: ARSO, ARNE, ACSU, quadra interna, conjunto, lote. "
            "Para o Google Maps, isso é fonte de erro — e endereço que o Google entende errado "
            "é empresa que o cliente não acha."
        ),
        "painel_titulo": "Por que o Maps erra tanto em Palmas",
        "painel_html": f"""
          <ul class="audit-list">
            <li>Endereço por <strong>quadra, conjunto e lote</strong>, não por rua e número.</li>
            <li>Siglas <strong>ARSO, ARNO, ARSE, ARNE e ACSU</strong> confundem quem não é da cidade.</li>
            <li>Os Correios já alertaram: endereço incompleto faz encomenda voltar.</li>
            <li><strong>{ctx['ativas']}</strong> empresas ativas na capital.</li>
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Sobre o endereçamento: <a href="https://conexaoto.com.br/2021/01/08/moradores-de-palmas-devem-utilizar-os-enderecos-atualizados-segundo-o-correios" target="_blank" rel="noopener noreferrer">orientação dos Correios sobre os endereços de Palmas</a>.</p>""",
        "secoes": [
            f"""
    <section class="solution-section" aria-labelledby="pal-endereco">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">O problema nº 1 da cidade</div>
          <h2 id="pal-endereco" class="section-title">O endereço de Palmas quebra o Google Maps — e quase ninguém corrige isso</h2>
          <p>Palmas foi planejada do zero e organizada em quadras. Um endereço comercial típico
          daqui tem esta cara: <em>ACSU-SE 40, Conjunto 1, Lote 5</em> — ou uma ARSO, ARNO, ARSE,
          ARNE, com quadra interna (QI) e lote. Não há “rua tal, número tal” na forma a que o resto
          do Brasil está acostumado.</p>
          <p>Os próprios Correios já orientaram a população a usar as denominações corretas e
          informar o número da quadra interna, porque objeto com endereço insuficiente volta.
          Se o serviço postal, que conhece a cidade, tem esse problema, imagine um sistema
          automático que tenta adivinhar coordenada a partir de texto.</p>
          <p>O resultado prático aparece no seu perfil do Google de três formas, e todas custam
          cliente:</p>
          <ul class="audit-list">
            <li><strong>Pino no lugar errado.</strong> O cliente segue a rota e para em outra quadra.</li>
            <li><strong>Endereço não validado.</strong> O Google não confirma o local e segura a exibição do perfil.</li>
            <li><strong>Empresa “não encontrada”.</strong> Quem pesquisa o nome não acha, porque o endereço cadastrado não bate com o que o mapa reconhece.</li>
          </ul>
          <p>A prefeitura mantém os mapas das quadras em um portal público de geoprocessamento —
          é de lá que sai a forma oficial do seu endereço, e é ela que deve ser usada em todos os
          lugares, sem variação.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Como arrumar, na ordem</h3>
          <ul class="audit-list">
            <li><strong>1.</strong> Levante a forma oficial do endereço no <a href="http://geo.palmas.to.gov.br/mapas/" target="_blank" rel="noopener noreferrer">portal de mapas da Prefeitura de Palmas</a>.</li>
            <li><strong>2.</strong> Escreva sempre igual: perfil do Google, site, redes, nota fiscal, assinatura de e-mail.</li>
            <li><strong>3.</strong> Corrija o pino do mapa à mão, arrastando até a porta real.</li>
            <li><strong>4.</strong> Use ponto de referência na descrição, do jeito que o cliente fala.</li>
            <li><strong>5.</strong> Confira no celular, pedindo rota como se fosse cliente.</li>
          </ul>
        </div>
      </div>
    </section>""",
            f"""
    <section class="metodo" aria-labelledby="pal-gmn">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Prioridade em Palmas</div>
          <h2 id="pal-gmn" class="section-title">Em Palmas, o Perfil da Empresa vem antes do site</h2>
          <p class="section-desc">Em cidade planejada e de porte médio, a maior parte das decisões
          de compra local passa pelo Maps antes de passar por qualquer site. Some isso ao problema
          de endereço e você tem a conclusão: arrumar o {ctx['link_gmn']} é o passo que muda mais
          coisa com menos esforço. Site importa, mas vem depois — e é assim que eu organizo o
          trabalho aqui.</p>
        </div>
        <div class="metodo-steps">
          <div class="metodo-step"><div class="step-number">1</div><h3>Endereço e pino</h3><p>Forma oficial da quadra, pino conferido na rota real, dado idêntico em todo lugar.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">2</div><h3>Categoria e serviços</h3><p>Categoria certa e lista de serviços com o nome que o cliente de Palmas usa.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">3</div><h3>Fotos e avaliações</h3><p>Fotos que mostram fachada e quadra (ajudam o cliente a achar) e rotina de pedir avaliação.</p></div>
          <div class="metodo-arrow" aria-hidden="true"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          <div class="metodo-step"><div class="step-number">4</div><h3>Depois o site</h3><p>Com o perfil funcionando, o site passa a receber quem já está decidido a comprar.</p></div>
        </div>
      </div>
    </section>""",
            f"""
    <section class="solution-section" aria-labelledby="pal-mercado">
      <div class="container split-grid">
        <div class="split-copy">
          <div class="section-tag">O mercado da capital</div>
          <h2 id="pal-mercado" class="section-title">Palmas é uma capital jovem — e isso aparece na busca</h2>
          <p>São {ctx['ativas']} empresas ativas na cidade, com {ctx['n90']} abertas nos últimos
          90 dias. É um mercado em formação, e mercado em formação tem uma característica que joga
          a favor de quem se organiza cedo: <strong>muita empresa ainda não fez o básico</strong>.</p>
          <p>Enquanto em capitais mais antigas você disputa contra perfis maduros, com centenas de
          avaliações e anos de histórico, aqui é comum encontrar concorrente com perfil incompleto,
          sem categoria certa, sem foto recente e sem uma única resposta a avaliação. Quem arruma
          isso primeiro sai na frente com um esforço que, em São Paulo ou no Rio, não seria
          suficiente nem para empatar.</p>
          <p>É por isso que a estratégia aqui não é a mesma de uma capital grande. Em Palmas, o
          caminho curto é: endereço correto, perfil completo, avaliações em rotina. Só depois vem
          conteúdo e disputa por termos mais amplos.</p>
        </div>
        <div class="diagnostic-card">
          <h3>Onde novas empresas estão abrindo em Palmas</h3>
          {ctx['bairros_lista']}
          <h3 style="margin-top:1.25rem;">Ramos que mais abriram (90 dias)</h3>
          <ul class="audit-list">
{ctx['ramos_html']}
          </ul>
          <p class="section-desc" style="font-size:.8rem;margin-top:.75rem;">Fonte: <a href="https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica-cnpj" target="_blank" rel="noopener noreferrer">dados públicos de CNPJ da Receita Federal</a>, referência {ctx['ref']}.</p>
        </div>
      </div>
    </section>""",
            f"""
    <section class="solution-section" aria-labelledby="pal-atendimento">
      <div class="container">
        <div class="section-header">
          <div class="section-tag">Como é o atendimento</div>
          <h2 id="pal-atendimento" class="section-title">Atendimento a Palmas: online, sem fingir que estou aí</h2>
          <p class="section-desc">A RCB fica em Goiânia e atende Palmas 100% online, por vídeo,
          com acesso aos seus dados reais do Google. Não existe escritório, endereço nem equipe da
          RCB no Tocantins — e dizer o contrário seria mentira fácil de checar. O que existe é a
          mesma {ctx['link_consultoria']} usada nos atendimentos presenciais, com a diferença de que
          as reuniões acontecem por chamada de vídeo.</p>
          <p class="section-desc">Os {ctx['link_cases']} são de clientes atendidos em Goiânia, com
          números reais e verificáveis — entre eles um primeiro lugar no Google Maps conquistado
          contra concorrentes com muito mais avaliações. Servem para você julgar se eu sei fazer o
          trabalho, não para sugerir que já atendi alguém em Palmas: até aqui, não atendi.</p>
        </div>
      </div>
    </section>""",
        ],
        "faq": [
            ("Por que minha empresa de Palmas não aparece no Google Maps?",
             "Em Palmas, a causa mais frequente é o endereço. A cidade usa quadras (ARSO, ARNO, ARSE, ARNE, ACSU) com conjunto e lote, e não rua com número, o que confunde os sistemas automáticos de localização — os próprios Correios já orientaram a população a informar o endereço completo para evitar devolução. Se o Google não consegue validar seu endereço, ele posiciona o pino errado, segura a exibição do perfil ou simplesmente não mostra sua empresa. Corrigir o endereço na forma oficial e ajustar o pino à mão costuma ser o primeiro ganho real."),
            ("Como otimizar o Google Meu Negócio de uma empresa em Palmas?",
             "Na ordem: endereço na forma oficial da quadra, idêntico em todos os lugares onde a empresa aparece; pino conferido pedindo rota pelo celular; categoria principal correta e serviços listados com o nome que o cliente de Palmas usa; fotos que mostrem fachada e ponto de referência, porque aqui elas ajudam o cliente a chegar; e rotina de pedir e responder avaliações. O perfil (hoje chamado Google Perfil da Empresa) é o que mais rende em Palmas — mais até que o site, no começo."),
            ("Vocês ficam em Goiânia. Como atendem uma empresa de Palmas?",
             "Por vídeo, com acesso aos seus dados reais do Google, e com implementação guiada passo a passo. Não há escritório nem equipe da RCB em Palmas, e eu não vou dizer que há. O trabalho de SEO local acontece dentro do seu perfil, do seu site e do seu conteúdo — tudo isso se faz à distância. O que exige conhecimento da cidade é entender o endereçamento por quadras e ler a concorrência local, e isso está contemplado no diagnóstico."),
            ("Vale a pena investir em SEO local numa cidade do porte de Palmas?",
             "Costuma valer mais do que em capitais grandes, justamente por ser um mercado mais novo. Em Palmas é comum encontrar concorrente com perfil incompleto, sem categoria certa e sem responder avaliação. Fazer o básico completo aqui coloca você à frente com um esforço que, numa praça madura, não seria suficiente nem para empatar. O que não existe é resultado garantido ou instantâneo — em qualquer cidade."),
        ],
        "cta_titulo": "Sua empresa em Palmas está no lugar certo do mapa?",
        "cta_texto": (
            "Peça o diagnóstico gratuito. Eu confiro se o Google entende o endereço da sua quadra, "
            "como está seu perfil e quem aparece na sua frente em Palmas — e te digo o que corrigir primeiro."
        ),
        "whats": "Olá, Renan. Tenho uma empresa em Palmas/TO e quero um diagnóstico gratuito para aparecer melhor no Google.",
    }


PILOTOS = {
    "rio-de-janeiro": rio_de_janeiro,
    "campinas": campinas,
    "palmas": palmas,
}
