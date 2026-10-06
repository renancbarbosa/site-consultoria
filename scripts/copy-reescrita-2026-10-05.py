"""Reescrita a mao dos trechos tecnicos demais para o leigo (pedido do Renan, 05/10/2026). Idempotente.

Complementa scripts/copy-humana-2026-10-05.py (travessao, palavras de IA e glossario automatico).
Aqui ficam as frases que precisavam ser reescritas por uma pessoa: jargao de agencia (handoff,
overhead, kickoff, GBP, gaps, briefing, engajamento, retainer...), o topo da home e a explicacao
de SEO com a analogia da vitrine. Cada troca e uma frase inteira; se a frase antiga nao existir
mais (ja trocada), o script segue em frente.

    python scripts/copy-reescrita-2026-10-05.py
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TROCAS = {
    "consultoria-seo-local/index.html": [
        ('SEO local (o trabalho de fazer o Google mostrar a sua empresa de graça para quem procura o que você vende) melhora a presença de negócios em buscas com intenção de localidade, "dentista" com o nome da cidade, "clínica próxima a mim", "restaurante perto de mim". A diferença do modelo RCB: consultor independente sem agência intermediando, atendimento online para todo o Brasil (e presencial em Goiânia e região), com diagnóstico, plano e implementação assistida no mesmo engajamento.',
         'SEO local é o trabalho de fazer a sua empresa aparecer no Google quando alguém da sua região procura o que você vende, como "dentista em Campinas" ou "restaurante perto de mim". Funciona como a vitrine de uma loja de rua: quem está bem arrumado e na frente recebe a visita. Comigo você fala direto com quem faz o trabalho, sem agência no meio: eu analiso, monto o plano e executo junto com você. Atendo online em todo o Brasil e presencialmente em Goiânia e região.'),
        ('<span class="pill">Diagnóstico + implementação</span>', '<span class="pill">Análise + execução</span>'),
        ('<li>Diagnóstico, plano e implementação no mesmo contrato.</li>', '<li>Análise, plano e execução no mesmo contrato.</li>'),
        ('<li>Interlocutor único do início ao fim.</li>', '<li>Você fala sempre com a mesma pessoa.</li>'),
        ('Com consultor independente, quem faz o diagnóstico é quem executa o plano. Não há handoff entre equipes, não há cliente sendo passado de vendedor para analista após a assinatura. A decisão é rápida e o trabalho começa sem perda de contexto.',
         'Com um consultor independente, quem analisa o seu caso é a mesma pessoa que faz o trabalho. Você não é passado de um vendedor para outra pessoa depois de assinar. É como levar o carro a um mecânico de confiança em vez de uma oficina grande: quem ouve o problema é quem coloca a mão no motor.'),
        ('A contrapartida: capacidade de execução paralela menor. Para projetos que exigem produção em escala de conteúdo, design pesado ou desenvolvimento avançado, a agência tem mais braços. Para o porte de uma clínica, consultório ou negócio local, a velocidade de decisão e o custo menor tendem a compensar.',
         'O lado negativo: uma pessoa só não toca dez projetos grandes ao mesmo tempo. Se você precisa de muito texto por mês, design complexo ou um sistema feito sob medida, uma agência tem mais gente. Para uma clínica, um consultório ou um negócio local, decidir rápido e pagar menos costuma valer mais.'),
        ('<li>Interlocutor único, do diagnóstico à implementação.</li>', '<li>Uma pessoa só cuida do seu caso, da análise à execução.</li>'),
        ('<li>Custo menor, sem overhead de estrutura de agência.</li>', '<li>Custo menor, porque você não paga a estrutura de uma agência.</li>'),
        ('<li>Capacidade paralela limitada, adequado para clínicas e negócios locais.</li>', '<li>Atendo poucos clientes ao mesmo tempo, o que combina com clínicas e negócios locais.</li>'),
        ('A maioria dos acompanhamentos funcionam 100% remotamente. A reunião presencial agrega mais valor em momentos específicos: kickoff, apresentação do diagnóstico e alinhamento de estratégia. Não é um diferencial vendido: é uma opção real para quem está na região e prefere encontros presenciais.',
         'A maioria dos clientes é atendida 100% online. A reunião presencial ajuda mais em três momentos: no começo do trabalho, na apresentação da análise e quando é preciso combinar os próximos passos. Não é um extra cobrado à parte: é uma opção para quem está na região e prefere conversar pessoalmente.'),
        ('<h2 class="section-title">O que está incluso em cada engajamento</h2>', '<h2 class="section-title">O que está incluído no trabalho</h2>'),
        ('A consultoria não entrega relatório e encerra. O formato envolve diagnóstico, execução assistida e acompanhamento contínuo:',
         'A consultoria não termina na entrega de um relatório. Ela inclui a análise, a execução feita junto com você e o acompanhamento todo mês:'),
        ('<li>Diagnóstico inicial em PDF, GBP, site, concorrentes diretos e palavras-chave (as palavras que o cliente digita no Google) priorizadas.</li>',
         '<li>Análise inicial em PDF: seu perfil no Google Maps, seu site, seus concorrentes e as palavras que o seu cliente digita no Google.</li>'),
        ('<li>Gestão e otimização do Google Business Profile.</li>', '<li>Cuidado e ajuste do seu perfil no Google Maps (o Google Meu Negócio).</li>'),
        ('<li>Revisão de páginas existentes com orientações de conteúdo e SEO.</li>', '<li>Revisão das páginas do seu site, com o que mudar em cada uma.</li>'),
        ('<li>Briefing de novas páginas, redação fica a cargo do cliente ou contratada separadamente.</li>',
         '<li>Roteiro das páginas novas que valem a pena criar. O texto pode ser escrito por você ou contratado à parte.</li>'),
        ('<li>Estratégia de avaliações: fluxo de coleta e orientação de respostas.</li>', '<li>Um jeito simples de pedir avaliações aos clientes e de responder a elas.</li>'),
        ('<li>Relatório mensal de indicadores: posição, GBP insights e visitas que chegam do Google sem anúncio.</li>',
         '<li>Relatório mensal: em que posição você aparece, quantas pessoas viram seu perfil no Maps e quantas visitas o site recebeu do Google sem anúncio.</li>'),
        ('<h2 class="section-title">Cronograma típico de um engajamento</h2>', '<h2 class="section-title">Quanto tempo leva, fase por fase</h2>'),
        ('Diagnóstico, GBP, site, concorrentes, palavras-chave e gaps de conteúdo.',
         'Análise do perfil no Google, do site, dos concorrentes, das palavras que o cliente digita e do que falta no seu site.'),
        ('Otimização do GBP + entrega do plano de ação priorizado.', 'Ajuste do perfil no Google Maps e entrega do plano, em ordem de prioridade.'),
        ('Implementação assistida, ajustes de site, páginas novas, estrutura técnica e estratégia de avaliações.',
         'Execução junto com você: ajustes no site, páginas novas, correções técnicas e rotina de avaliações.'),
        ('Primeiros movimentos de ranqueamento (a posição em que o Google mostra a página) + ajustes baseados nos dados reais.',
         'A empresa começa a subir nas buscas, e o plano é ajustado com base nos números reais.'),
        ('Consolidação e manutenção, refinamento contínuo com base nos indicadores.', 'A posição se firma, e o trabalho vira manutenção e melhoria contínua.'),
        ('<div class="section-tag">Fit</div>', '<div class="section-tag">Para quem é</div>'),
        ('que já tem demanda presencial mas some no Google', 'que já atende bem, mas não aparece no Google'),
        ('para negócio local em cidade de médio porte competindo por', 'para negócio local em cidade de médio porte que disputa espaço no'),
        ('e ter entrada orgânica (o resultado gratuito, que aparece abaixo dos anúncios)', 'e receber clientes que chegam sozinhos pelo Google, sem anúncio'),
        ('e quer base sólida antes de escalar', 'e quer deixar a casa arrumada antes de gastar mais'),
        ('<p><strong>Não faz sentido</strong> para e-commerce sem componente local, SEO local não é a estratégia certa; para negócio sem nenhuma presença digital estabelecida ainda (há um passo anterior à SEO); para quem precisa de resultado em menos de 60 dias, SEO local não é mídia paga; para quem quer relatório bonito sem implementação real.</p>',
         '<p><strong>Não faz sentido</strong> para loja que só vende pela internet, sem atendimento na região (aí o caminho é outro); para quem ainda não tem nada no Google, nem perfil nem site (antes é preciso montar o básico); para quem precisa de cliente em menos de 60 dias (para isso, o certo é anúncio); e para quem quer só um relatório bonito, sem mudar nada de verdade.</p>'),
        ('A consultoria começa sempre com diagnóstico gratuito, uma análise inicial do Google Business Profile, do site e da concorrência local da clínica. O diagnóstico aponta o que está travando a presença no Google Maps e na busca local e indica o caminho de correção.',
         'A consultoria começa sempre com uma análise gratuita do seu perfil no Google Maps, do seu site e dos concorrentes da sua região. A análise mostra o que está impedindo você de aparecer e o que fazer para corrigir.'),
        ('<h3>Otimização inicial: projeto pontual</h3>', '<h3>Arrumação inicial: um projeto com começo e fim</h3>'),
        ('Correção do que foi identificado no diagnóstico: ajustes no Google Business Profile (categorias, atributos, fotos, NAP (nome, endereço e telefone)), revisão técnica do site, criação ou ajuste de páginas-chave, plano de avaliações. Entregue em prazo definido, sem mensalidade.',
         'Correção do que a análise encontrou: ajuste do perfil no Google Maps (categorias, fotos e o mesmo nome, endereço e telefone em todo lugar), revisão do site, criação ou ajuste das páginas principais e plano de avaliações. Prazo combinado e sem mensalidade.'),
        ('<h3>Acompanhamento mensal: retainer</h3>', '<h3>Acompanhamento mensal</h3>'),
        ('Inclui gestão contínua do GBP, novas páginas de conteúdo, monitoramento de posições, relatórios mensais e reunião de acompanhamento.',
         'Inclui o cuidado contínuo do perfil no Google Maps, páginas novas no site, acompanhamento da sua posição no Google, relatório e reunião todo mês.'),
        ('O valor de cada formato é definido após o diagnóstico, conforme o escopo real da clínica.',
         'O valor de cada formato sai depois da análise, de acordo com o tamanho do trabalho.'),
        ('Cidades com menos de 50 mil habitantes costumam ter o GBP como principal ferramenta.',
         'Cidades com menos de 50 mil habitantes costumam ter o perfil no Google Maps como principal ferramenta.'),
        ('É possível trabalhar GBP e avaliações sem site.', 'É possível trabalhar o perfil no Google Maps e as avaliações sem ter site.'),
        ('Relatório mensal com GBP insights, posição orgânica e tráfego do Analytics.',
         'Relatório mensal com quantas pessoas viram seu perfil no Maps, sua posição no Google e quantas visitas o site recebeu.'),
        ('Análise inicial cobre GBP, site, concorrentes diretos e prioridades, gratuita e sem compromisso.',
         'A análise inicial olha seu perfil no Google Maps, seu site e seus concorrentes, e diz por onde começar. É gratuita e sem compromisso.'),
    ],
    "google-perfil-empresa/index.html": [
        ("Preços publicados, escopo e uma conta simples para avaliar o investimento.",
         "O que define o valor e uma conta simples para avaliar o investimento."),
    ],
    "conteudo-para-seo/index.html": [
        ("redação pela RCB, pela sua equipe via briefing, ou em conjunto.",
         "texto escrito por mim, pela sua equipe a partir de um roteiro que eu entrego, ou pelos dois juntos."),
        ("A redação pode ser da RCB, da sua equipe via briefing, ou em conjunto,",
         "O texto pode ser escrito por mim, pela sua equipe a partir de um roteiro que eu entrego, ou pelos dois juntos,"),
    ],
    "site-otimizado-para-seo/index.html": [
        ("<li><strong>Conversão e rastreamento:</strong> botões de chamada, WhatsApp e eventos de acompanhamento.</li>",
         "<li><strong>Contatos medidos:</strong> botões de chamada, WhatsApp e a contagem de cada clique.</li>"),
        ("formulário e rastreamento básico dos contatos", "formulário e a contagem dos contatos"),
        ("CTAs claros, botão de WhatsApp", "botões de chamada claros, botão de WhatsApp"),
    ],
    "seo-local-goiania/index.html": [
        ("Base on-page forte reduz dependência externa.", "Um site bem arrumado por dentro depende menos de fatores de fora."),
    ],
    "blog/como-escolher-consultoria-seo-goiania/index.html": [
        ("<li><strong>Relatórios com métricas de vaidade:</strong> Impressões brutas não pagam contas.",
         "<li><strong>Relatórios com números que só enfeitam:</strong> Quantas vezes você apareceu no Google não paga as contas."),
    ],
    "blog/seo-para-clinicas-vale-a-pena/index.html": [
        ("<strong>Ticket Médio de um Paciente:</strong>", "<strong>Quanto vale um paciente:</strong>"),
    ],
    "blog/por-que-minha-clinica-odontologica-nao-aparece-no-google/index.html": [
        ("Não é apenas preencher qualquer campo: é organizar o perfil", "Não basta preencher os campos: é preciso organizar o perfil"),
        ("Não se trata apenas de buscar quantidade. É preciso ter rotina,", "Não adianta só buscar quantidade. É preciso ter rotina,"),
    ],
    "blog/quais-servicos-merecem-pagina-propria/index.html": [
        ("<p>A verdade é que <strong>nem todo serviço", "<p>Na prática, <strong>nem todo serviço"),
    ],
    "blog/o-que-e-diagnostico-presenca-digital/index.html": [
        ("</a>, o mergulho detalhado.", "</a>, a análise detalhada."),
    ],
    "blog/seo-para-clinicas-por-que-aparecer-no-google-vale-mais-que-indicacao/index.html": [
        ("E o melhor primeiro passo é entender onde sua clínica está hoje.", "O primeiro passo é entender onde sua clínica está hoje."),
    ],
    "blog/melhorar-site-atual-ou-fazer-um-novo/index.html": [
        ("design e, fundamental, o que dizem os dados do", "design e, o mais importante, o que dizem os dados do"),
    ],
    "index.html": [
        ("O cliente procura o que você vende, e encontra seu concorrente", "O cliente procura o que você vende e encontra o seu concorrente"),
        ("Clientes pelo Google: anúncio para o resultado rápido, SEO e Google Meu Negócio para o resultado duradouro, site e landing page para converter.",
         "Eu faço a sua empresa aparecer no Google quando alguém procura o que você vende. O anúncio traz cliente já nesta semana. O Google Maps e o site trazem cliente todo mês, sem pagar por clique."),
        ("Sua empresa no mapa e nas buscas do Google, trazendo cliente sem pagar por clique. É o resultado que dura.",
         "É como ter a vitrine na rua mais movimentada da cidade: sua empresa aparece no mapa e nas buscas do Google, e o cliente chega sem você pagar por clique. É o resultado que dura."),
        ("A página que transforma o clique do anúncio em conversa no WhatsApp, e o site próprio que aparece no Google.",
         "O site da sua empresa, feito para aparecer no Google, e a página de anúncio, que transforma o clique em conversa no WhatsApp."),
    ],
}


def main():
    alterados = trocas = 0
    for rel, pares in TROCAS.items():
        p = os.path.join(RAIZ, rel)
        s = io.open(p, encoding="utf-8", newline="").read()
        n = s
        for velho, novo in pares:
            if velho in n:
                n = n.replace(velho, novo)
                trocas += 1
            elif novo not in n:
                print("AVISO: nao achei em %s: %s" % (rel, velho[:70]))
        if n != s:
            io.open(p, "w", encoding="utf-8", newline="").write(n)
            alterados += 1
    print("arquivos alterados: %d  trocas: %d" % (alterados, trocas))


if __name__ == "__main__":
    main()
