# -*- coding: utf-8 -*-
"""
E1 — /analise-de-projeto/

Formulário de qualificação de lead de alto valor. É o CTA principal das 22
páginas da divisão de mercados competitivos.

Diferença em relação ao restante do site: o /diagnostico-presenca-digital/
continua sendo a conversão do SEO local (gratuito, negócio local, poucos campos).
Este formulário qualifica projeto nacional por segmento, escopo, prazo e faixa de
investimento — informação sem a qual nenhuma proposta faria sentido.

Envio pelo WhatsApp, mesmo padrão do formulário de diagnóstico: monta a mensagem,
dispara o evento generate_lead e abre a conversa. Sem back-end, compatível com
Cloudflare Pages.
"""
from rcb_base import (
    BASE_URL, WHATS, head_comum, montar, breadcrumb_html, sec_texto, lista,
    sec_faq, grafo, schema_webpage, schema_breadcrumb, schema_faq, esc,
)

HOJE = "2026-08-06"


def _campo(id_, rotulo, tipo="text", ph="", req=False, opcoes=None, rows=None, ajuda=""):
    marca = ' <span class="required">*</span>' if req else ' <span class="opcional">(opcional)</span>'
    atr_req = " required" if req else ""
    dica = f'<span class="form-ajuda">{ajuda}</span>' if ajuda else ""
    erro = f'<span class="form-error" id="{id_}-error" role="alert"></span>' if req else ""

    if opcoes:
        ops = "".join(
            f'<option value="{esc(v)}"{" disabled selected" if v == "" else ""}>{t}</option>'
            for v, t in opcoes
        )
        campo = f'<select id="form-{id_}" name="{id_}"{atr_req}>{ops}</select>'
    elif rows:
        campo = (f'<textarea id="form-{id_}" name="{id_}" rows="{rows}" '
                 f'placeholder="{esc(ph)}"{atr_req}></textarea>')
    else:
        campo = (f'<input type="{tipo}" id="form-{id_}" name="{id_}" '
                 f'placeholder="{esc(ph)}"{atr_req}>')

    return (f'<div class="form-row"><label for="form-{id_}">{rotulo}{marca}</label>'
            f'{dica}{campo}{erro}</div>')


def _bloco(titulo, descricao, campos_html, grid=True):
    classe = "form-grid-2" if grid else ""
    return (f'<fieldset class="form-bloco"><legend class="form-bloco-titulo">{titulo}</legend>'
            f'<p class="form-bloco-desc">{descricao}</p>'
            f'<div class="{classe}">{campos_html}</div></fieldset>')


def e1_analise_de_projeto():
    slug = "analise-de-projeto"
    canonical = f"{BASE_URL}/{slug}/"
    titulo = "Análise de projeto de SEO nacional | RCB Consultoria"
    desc = ("Formulário de qualificação para projetos de SEO em mercados competitivos: segmento, "
            "objetivo, prazo e faixa de investimento. Resposta em até 24h úteis.")
    page_id = "analise-projeto"

    faq = [
        ("A análise é gratuita?",
         "A primeira leitura é. Você recebe a avaliação inicial do cenário, a leitura da concorrência nos "
         "termos indicados e a indicação de escopo e faixa de investimento. Análises mais profundas — "
         "auditoria completa, triagem de domínios, mapeamento extenso de palavras-chave — são serviços "
         "contratados, e isso é dito antes."),
        ("Por que preciso informar faixa de investimento?",
         "Porque sem isso qualquer proposta seria chute. Em mercado competitivo, o resultado depende de "
         "atingir um patamar mínimo de execução: saber a faixa permite dizer se o objetivo é viável com "
         "esse orçamento, propor um alvo mais realista ou avisar que não faz sentido começar agora."),
        ("Ainda não tenho site nem marca. Posso preencher?",
         "Pode, e é o caso de boa parte dos projetos desta divisão. Marque que o projeto começa do zero e "
         "descreva a ideia — a análise leva em conta que a construção faz parte do escopo."),
        ("Em quanto tempo recebo resposta?",
         "Em até 24h úteis, pelo WhatsApp ou e-mail informado. Se faltar alguma informação essencial, a "
         "primeira resposta será uma pergunta objetiva, não uma proposta genérica."),
        ("O que acontece se o meu projeto não for atendido?",
         "Você recebe a resposta com o motivo. Os casos mais comuns são operação sem direito sobre o "
         "conteúdo distribuído, demanda de contorno de bloqueio judicial ou administrativo, e objetivo "
         "incompatível com o orçamento disponível — nesse último caso, com sugestão de alternativa."),
    ]

    schema = grafo(
        schema_webpage(canonical, titulo, desc, HOJE),
        schema_breadcrumb([("Início", f"{BASE_URL}/"),
                           ("SEO para mercados competitivos", f"{BASE_URL}/seo-para-mercados-competitivos/"),
                           ("Análise de projeto", canonical)]),
        schema_faq(faq),
    )

    trilha = breadcrumb_html([("Início", "/"),
                              ("Mercados competitivos", "/seo-para-mercados-competitivos/"),
                              ("Análise de projeto", canonical)])

    # ---------- blocos do formulário ----------
    b_contato = _bloco(
        "1. Contato",
        "Para eu conseguir responder e endereçar a análise a você.",
        _campo("nome", "Nome", req=True, ph="Seu nome")
        + _campo("whatsapp", "WhatsApp", tipo="tel", req=True, ph="(00) 90000-0000")
        + _campo("email", "E-mail", tipo="email", req=True, ph="seu@email.com")
        + _campo("empresa", "Empresa ou nome do projeto", ph="Como o projeto se chama (ou vai se chamar)"),
    )

    b_projeto = _bloco(
        "2. O projeto",
        "O que você faz e em que estágio a operação está hoje.",
        _campo("segmento", "Segmento", req=True, opcoes=[
            ("", "Selecione o segmento"),
            ("IPTV / TV por internet", "IPTV / TV por internet"),
            ("Streaming e plataformas de conteúdo", "Streaming e plataformas de conteúdo"),
            ("Bets / apostas (operador)", "Bets / apostas (operador)"),
            ("Afiliado de apostas / portal", "Afiliado de apostas / portal"),
            ("iGaming B2B (plataforma, provedor)", "iGaming B2B (plataforma, provedor)"),
            ("Jogos online / games", "Jogos online / games"),
            ("Produto digital / SaaS", "Produto digital / SaaS"),
            ("E-commerce nacional", "E-commerce nacional"),
            ("Serviços online nacionais", "Serviços online nacionais"),
            ("Outro", "Outro"),
        ])
        + _campo("estagio", "Estágio atual", req=True, opcoes=[
            ("", "Selecione o estágio"),
            ("Ainda não existe — começando do zero", "Ainda não existe — começando do zero"),
            ("Tenho site, mas não tenho tráfego orgânico", "Tenho site, mas não tenho tráfego orgânico"),
            ("Tenho tráfego e quero crescer", "Tenho tráfego e quero crescer"),
            ("Perdi tráfego e quero recuperar", "Perdi tráfego e quero recuperar"),
            ("Vou migrar de domínio ou plataforma", "Vou migrar de domínio ou plataforma"),
        ])
        + _campo("descricao", "Descrição do produto ou serviço", rows=3, req=True,
                 ph="O que você vende ou distribui, para quem, e como a operação funciona hoje.")
        + _campo("site", "URL atual", ph="https://... (deixe em branco se ainda não existe)")
        + _campo("alcance", "Atendimento", opcoes=[
            ("", "Selecione o alcance"),
            ("Nacional — todo o Brasil", "Nacional — todo o Brasil"),
            ("Nacional + internacional", "Nacional + internacional"),
            ("Regional (alguns estados)", "Regional (alguns estados)"),
            ("Local — uma cidade", "Local — uma cidade"),
        ], ajuda="Se você atende só uma cidade, a consultoria de SEO local resolve melhor e mais barato."),
        grid=False,
    )

    b_objetivo = _bloco(
        "3. Objetivo",
        "O que você quer que aconteça, e em quanto tempo.",
        _campo("objetivo", "Objetivo principal", opcoes=[
            ("", "Selecione o objetivo"),
            ("Posicionar termos principais do nicho", "Posicionar termos principais do nicho"),
            ("Gerar contatos e vendas pelo orgânico", "Gerar contatos e vendas pelo orgânico"),
            ("Reduzir dependência de tráfego pago", "Reduzir dependência de tráfego pago"),
            ("Lançar um projeto novo já posicionado", "Lançar um projeto novo já posicionado"),
            ("Recuperar tráfego perdido", "Recuperar tráfego perdido"),
            ("Construir autoridade / backlinks", "Construir autoridade / backlinks"),
        ])
        + _campo("prazo", "Prazo desejado", opcoes=[
            ("", "Selecione o prazo"),
            ("Até 3 meses", "Até 3 meses"),
            ("3 a 6 meses", "3 a 6 meses"),
            ("6 a 12 meses", "6 a 12 meses"),
            ("Mais de 12 meses", "Mais de 12 meses"),
            ("Sem prazo definido", "Sem prazo definido"),
        ])
        + _campo("palavra_chave", "Palavra-chave prioritária", ph="O termo que você mais quer ranquear",
                 ajuda="Se souber mais de um, separe por vírgula. É por aqui que eu leio a concorrência."),
    )

    b_escopo = _bloco(
        "4. Escopo",
        "O que precisa ser construído além da estratégia de posicionamento.",
        _campo("precisa_marca", "Precisa de criação de marca?", opcoes=[
            ("", "Selecione"), ("Sim", "Sim"), ("Não — já tenho marca", "Não — já tenho marca"),
            ("Não sei ainda", "Não sei ainda"),
        ])
        + _campo("precisa_site", "Precisa de desenvolvimento do site?", opcoes=[
            ("", "Selecione"), ("Sim — do zero", "Sim — do zero"),
            ("Sim — reconstruir o atual", "Sim — reconstruir o atual"),
            ("Não — só estratégia e conteúdo", "Não — só estratégia e conteúdo"),
        ])
        + _campo("tem_dominio", "Já possui domínio?", opcoes=[
            ("", "Selecione"), ("Sim", "Sim"), ("Não", "Não"),
            ("Tenho, mas quero trocar", "Tenho, mas quero trocar"),
        ])
        + _campo("dominio_expirado", "Interesse em domínio expirado?", opcoes=[
            ("", "Selecione"),
            ("Sim — quero avaliar opções", "Sim — quero avaliar opções"),
            ("Já comprei um e quero analisar", "Já comprei um e quero analisar"),
            ("Não", "Não"),
            ("Não sei o que é", "Não sei o que é"),
        ]),
    )

    faixas = [
        ("", "Selecione a faixa"),
        ("Até R$ 10 mil", "Até R$ 10 mil"),
        ("De R$ 10 mil a R$ 20 mil", "De R$ 10 mil a R$ 20 mil"),
        ("De R$ 20 mil a R$ 50 mil", "De R$ 20 mil a R$ 50 mil"),
        ("De R$ 50 mil a R$ 100 mil", "De R$ 50 mil a R$ 100 mil"),
        ("Acima de R$ 100 mil", "Acima de R$ 100 mil"),
        ("Ainda não defini", "Ainda não defini"),
    ]

    b_investimento = _bloco(
        "5. Investimento",
        "Sem isso, qualquer proposta seria chute. A faixa orienta o escopo — e me permite avisar "
        "quando o objetivo não cabe no orçamento, em vez de vender um projeto que não vai entregar.",
        _campo("investimento_inicial", "Investimento inicial disponível", req=True, opcoes=faixas)
        + _campo("investimento_mensal", "Investimento mensal disponível", opcoes=faixas),
    )

    b_obs = _bloco(
        "6. Observações",
        "Qualquer contexto que ajude a entender o caso.",
        _campo("observacoes", "Observações", rows=3,
               ph="Concorrentes que você acompanha, o que já tentou, restrições, prazos fixos..."),
        grid=False,
    )

    formulario = f"""<form class="formulario-diagnostico formulario-projeto" id="analiseProjetoForm" novalidate aria-label="Formulário de análise de projeto">
              <h2 class="form-titulo">Solicitar análise do projeto</h2>
              <p class="form-intro">Campos marcados com <span class="required">*</span> são obrigatórios.
              O restante é opcional — quanto mais contexto, mais útil é a resposta.</p>
              {b_contato}
              {b_projeto}
              {b_objetivo}
              {b_escopo}
              {b_investimento}
              {b_obs}
              <button type="submit" class="btn btn-primary form-submit" data-event="cta_click" data-location="formulario_analise" data-page="{page_id}">Enviar análise pelo WhatsApp</button>
              <p class="form-disclaimer">Ao enviar, o WhatsApp abre com a mensagem já preenchida —
              você confere antes de mandar. Resposta em até 24h úteis, sem compromisso de contratação.</p>
            </form>"""

    corpo = f"""
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          {trilha}
          <div class="eyebrow">Projetos nacionais e competitivos</div>
          <h1 class="page-title">Análise de projeto</h1>
          <p class="page-subtitle">Antes de qualquer proposta, eu preciso entender o mercado que você quer
          disputar, o estágio da sua operação e o orçamento disponível. É isso que este formulário levanta —
          e é o que permite devolver uma resposta específica em vez de um orçamento genérico.</p>
          <div class="pill-row">
            <span class="pill">Resposta em até 24h úteis</span>
            <span class="pill">Sem compromisso</span>
            <span class="pill">Atendimento nacional</span>
          </div>
        </div>
        <aside class="page-hero-panel">
          <h2>O que você recebe</h2>
          <ul class="audit-list">
            <li>Leitura da concorrência nos termos que você indicar.</li>
            <li>Indicação de escopo — o que o projeto precisa ter.</li>
            <li>Cenário de prazo, com as premissas explícitas.</li>
            <li>Faixa de investimento compatível com o objetivo.</li>
            <li>Um parecer honesto quando o alvo não compensa.</li>
          </ul>
          <p class="section-desc" style="font-size:.85rem;margin-top:.75rem;">Nenhum prazo ou posição é
          garantido — nem aqui, nem em qualquer fornecedor sério.</p>
        </aside>
      </div>
    </section>

    <section class="contato" id="formulario" aria-labelledby="form-secao-titulo">
      <div class="container contato-grid">
        <div class="contato-info">
          <div class="section-tag">Como funciona</div>
          <h2 id="form-secao-titulo" class="section-title">Três etapas até saber se faz sentido</h2>
          <p>Este formulário não gera proposta automática. Ele organiza a informação para que a primeira
          conversa já seja sobre o seu caso concreto.</p>
{lista([
    "<strong>1. Você envia o contexto.</strong> Segmento, estágio, objetivo, prazo e faixa de investimento.",
    "<strong>2. Eu leio o mercado.</strong> Quem ocupa as posições que você quer e o que seria preciso para disputá-las.",
    "<strong>3. Você recebe o parecer.</strong> Escopo, cenário de prazo e faixa — ou o motivo de não fazer sentido agora.",
])}
          <p>Se o seu caso for local — atendimento em uma cidade, cliente que precisa ir até você —, o
          caminho certo é o <a href="/diagnostico-presenca-digital/">diagnóstico de presença digital</a>,
          que é gratuito e mais adequado. Este formulário é para disputa nacional.</p>
          <div class="contato-canais">
            <a class="canal-item canal-whatsapp" href="https://wa.me/{WHATS}?text=Ol%C3%A1%2C%20Renan.%20Quero%20conversar%20sobre%20um%20projeto%20de%20SEO%20em%20mercado%20competitivo." data-event="cta_click" data-location="canal_whatsapp" data-page="{page_id}" target="_blank" rel="noopener noreferrer">
              <div><span class="canal-label">Prefere conversar antes?</span><span class="canal-value">(62) 99116-1040</span></div>
            </a>
            <a class="canal-item" href="mailto:contato@rcbseo.com.br">
              <div><span class="canal-label">E-mail</span><span class="canal-value">contato@rcbseo.com.br</span></div>
            </a>
          </div>
        </div>
        <div class="contato-form-wrap">
          {formulario}
        </div>
      </div>
    </section>"""

    corpo += sec_texto(
        "Critério de atendimento",
        "O que é verificado antes de qualquer proposta",
        lista([
            "<strong>Direito sobre o que é distribuído.</strong> Nos segmentos de conteúdo — IPTV, "
            "streaming, TV online — a análise verifica se a operação possui direito ou autorização sobre o "
            "conteúdo distribuído. Operações sem isso não são atendidas.",
            "<strong>Ausência de demanda de evasão.</strong> Projetos cujo objetivo seja contornar bloqueio "
            "judicial ou administrativo estão fora do escopo, em qualquer nicho e qualquer faixa de investimento.",
            "<strong>Uso legítimo de marca.</strong> Projetos baseados em marca de terceiros sem autorização "
            "não são atendidos — é um problema jurídico que nenhum trabalho de SEO resolve.",
            "<strong>Compatibilidade entre objetivo e orçamento.</strong> Se o alvo indicado exigir um "
            "patamar de execução acima da faixa informada, isso é dito na resposta, com alternativas: mirar "
            "termos menos disputados, faseamento ou adiar o início.",
            "<strong>Situação regulatória.</strong> Em setores regulados, cada empresa deve verificar a "
            "própria situação com assessoria jurídica. A RCB atua em comunicação e posicionamento, e não "
            "presta orientação jurídica.",
        ]),
        "criterio-titulo",
        desc="Este filtro existe para não desperdiçar o tempo de ninguém — e porque projeto construído "
             "sobre base instável não sustenta investimento de longo prazo.",
    )

    corpo += sec_faq(faq, "Perguntas frequentes sobre a análise")

    script = """
  <script>
  (function () {
    var form = document.getElementById('analiseProjetoForm');
    if (!form) return;

    var obrigatorios = ['nome', 'whatsapp', 'email', 'segmento', 'estagio', 'descricao', 'investimento_inicial'];

    function campo(nome) { return form.elements[nome]; }

    function erro(nome, msg) {
      var el = campo(nome);
      var box = document.getElementById(nome + '-error');
      if (el) el.classList.add('invalid');
      if (box) box.textContent = msg;
    }

    function limpar(nome) {
      var el = campo(nome);
      var box = document.getElementById(nome + '-error');
      if (el) el.classList.remove('invalid');
      if (box) box.textContent = '';
    }

    obrigatorios.forEach(function (nome) {
      var el = campo(nome);
      if (el) {
        el.addEventListener('input', function () { limpar(nome); });
        el.addEventListener('change', function () { limpar(nome); });
      }
    });

    function valida() {
      var ok = true;
      var primeiro = null;
      obrigatorios.forEach(function (nome) { limpar(nome); });

      obrigatorios.forEach(function (nome) {
        var el = campo(nome);
        if (!el) return;
        var v = (el.value || '').trim();
        if (!v) {
          erro(nome, 'Campo obrigatório.');
          ok = false;
          if (!primeiro) primeiro = el;
        }
      });

      var email = (campo('email').value || '').trim();
      if (email && !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {
        erro('email', 'E-mail inválido.');
        ok = false;
        if (!primeiro) primeiro = campo('email');
      }

      var tel = (campo('whatsapp').value || '').replace(/\\D/g, '');
      if (tel && tel.length < 10) {
        erro('whatsapp', 'Informe o WhatsApp com DDD.');
        ok = false;
        if (!primeiro) primeiro = campo('whatsapp');
      }

      if (primeiro && primeiro.focus) {
        primeiro.focus();
        primeiro.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      return ok;
    }

    function val(nome) {
      var el = campo(nome);
      return el ? (el.value || '').trim() : '';
    }

    function linha(rotulo, nome) {
      var v = val(nome);
      return v ? '*' + rotulo + ':* ' + v : '';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!valida()) return;

      var partes = [
        'Olá, Renan. Quero solicitar a análise de um projeto de SEO em mercado competitivo.',
        '',
        '*— Contato —*',
        linha('Nome', 'nome'),
        linha('WhatsApp', 'whatsapp'),
        linha('E-mail', 'email'),
        linha('Empresa/projeto', 'empresa'),
        '',
        '*— Projeto —*',
        linha('Segmento', 'segmento'),
        linha('Estágio', 'estagio'),
        linha('Descrição', 'descricao'),
        linha('Site atual', 'site'),
        linha('Alcance', 'alcance'),
        '',
        '*— Objetivo —*',
        linha('Objetivo', 'objetivo'),
        linha('Prazo desejado', 'prazo'),
        linha('Palavra-chave prioritária', 'palavra_chave'),
        '',
        '*— Escopo —*',
        linha('Criação de marca', 'precisa_marca'),
        linha('Desenvolvimento do site', 'precisa_site'),
        linha('Já possui domínio', 'tem_dominio'),
        linha('Domínio expirado', 'dominio_expirado'),
        '',
        '*— Investimento —*',
        linha('Inicial', 'investimento_inicial'),
        linha('Mensal', 'investimento_mensal'),
        '',
        linha('Observações', 'observacoes')
      ];

      var texto = partes.filter(function (l) { return l !== ''; }).join('\\n');
      var url = 'https://wa.me/5562991161040?text=' + encodeURIComponent(texto);

      if (typeof window.rcbTrackEvent === 'function') {
        window.rcbTrackEvent('generate_lead', {
          method: 'analise_projeto_whatsapp',
          contact_method: 'whatsapp',
          form_id: 'analiseProjetoForm',
          segmento: val('segmento'),
          faixa_investimento: val('investimento_inicial'),
          page_location: window.location.href,
          page_path: window.location.pathname
        });
      }

      window.open(url, '_blank', 'noopener,noreferrer');

      var btn = form.querySelector('button[type="submit"]');
      var original = btn.innerHTML;
      btn.innerHTML = 'Mensagem preparada — confira no WhatsApp';
      btn.disabled = true;
      setTimeout(function () {
        btn.innerHTML = original;
        btn.disabled = false;
      }, 4000);
    });
  })();
  </script>"""

    head = head_comum(titulo, desc, canonical, schema)
    return f"{slug}/index.html", montar(head, corpo, page_id, scripts_extra=script)


PAGINAS = [e1_analise_de_projeto]
