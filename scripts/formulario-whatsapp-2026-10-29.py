# -*- coding: utf-8 -*-
"""
Fase 6 do pilar SEO para IA (29/10/2026): conversão.

1. Home (#rcbLeadForm): o formulário abre o WhatsApp NO MESMO CLIQUE, com a mensagem pronta.
   Sai o Web3Forms (registro por e-mail, chave do Radar de CNPJ) e a 2ª tela (#rcbLeadOk).
   Decisão do Renan: "Só WhatsApp, sem registro". Motivo: esperar a resposta do servidor
   antes de abrir o WhatsApp faz o celular bloquear a janela, e a 2ª tela pede um clique a mais.
   - "Pacote de interesse" (4 pacotes antigos) vira "Serviço de interesse" (os 5 serviços).
   - "Tipo de negócio" passa de 5 para 11 opções (os nichos que o site atende).
   - Sai o mapa VALOR (preços antigos usados como valor de conversão no GA4).
   - Eventos do GA4 com os mesmos nomes (begin_lead, lead_error, generate_lead, cta_click).
2. /servicos/: os cartões de orçamento ficam mais concretos (dor + o que entra + botão com a
   ação) e entra o 4º cartão, "Aparecer nas IAs". Sem preço. A mesma mudança está no módulo
   scripts/conteudo/servicos_marketing.py, para uma regeração futura não desfazer.

Idempotente. Sem argumento só relata; --aplicar grava.
"""
import importlib.util
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
APLICAR = "--aplicar" in sys.argv

FORM_NOVO = '''<form class="wform" id="rcbLeadForm" novalidate>
            <div class="wform-linha">
              <label for="rcbNome">
                <span>Seu nome</span>
                <input type="text" id="rcbNome" name="nome" required maxlength="80" autocomplete="name" placeholder="Como posso te chamar">
              </label>
              <label for="rcbTelefone">
                <span>Seu WhatsApp</span>
                <input type="tel" id="rcbTelefone" name="whatsapp" required maxlength="30" autocomplete="tel" inputmode="tel" placeholder="(62) 9 9999-9999">
              </label>
            </div>

            <div class="wform-linha">
              <label for="rcbNegocio">
                <span>Tipo de negócio</span>
                <select id="rcbNegocio" name="tipo_de_negocio" required>
                  <option value="Clínica">Clínica ou consultório</option>
                  <option value="Dentista">Dentista ou clínica odontológica</option>
                  <option value="Estética">Clínica de estética</option>
                  <option value="Advocacia">Escritório de advocacia</option>
                  <option value="Contabilidade">Escritório de contabilidade</option>
                  <option value="Imobiliária">Imobiliária ou corretor</option>
                  <option value="Energia solar">Energia solar</option>
                  <option value="Serviço em domicílio">Serviço no local do cliente (limpeza, reformas, guincho...)</option>
                  <option value="Comércio local">Comércio local (loja, restaurante, salão...)</option>
                  <option value="Profissional liberal">Profissional liberal</option>
                  <option value="Outro">Outro</option>
                </select>
              </label>
              <label for="rcbCidade">
                <span>Sua cidade</span>
                <input type="text" id="rcbCidade" name="cidade" required maxlength="80" placeholder="Ex.: Goiânia - GO">
              </label>
            </div>

            <label for="rcbServico">
              <span>Serviço de interesse</span>
              <select id="rcbServico" name="servico" required>
                <option value="Aparecer no Google">Aparecer no Google e no Google Maps</option>
                <option value="Site ou landing page">Site ou landing page</option>
                <option value="Anúncio no Google">Anúncio no Google (Google Ads)</option>
                <option value="Aparecer nas IAs">Aparecer no ChatGPT e no Gemini</option>
                <option value="SEO para YouTube">Vídeos no YouTube que tragam cliente</option>
                <option value="Ainda não sei">Ainda não sei, quero sua opinião</option>
              </select>
            </label>

            <button type="submit" class="btn btn-whatsapp wform-enviar" data-event="cta_click" data-location="formulario" data-page="home">
              <span class="rotulo">Enviar pelo WhatsApp</span>
            </button>

            <div class="wform-passos" aria-label="O que acontece depois">
              <span>Eu olho seu Google</span>
              <span>Te digo o que está travando</span>
              <span>Você decide se quer seguir</span>
            </div>
            <p class="wform-privacidade">Isso não é uma compra. Nada fica gravado no site: os seus dados vão só na mensagem que você mesmo envia pelo WhatsApp. Veja a <a href="/privacidade/">Política de Privacidade</a>.</p>
            <p class="wform-erro" role="alert"></p>
            <p class="wform-aviso" id="rcbAviso" hidden>O WhatsApp não abriu? <a id="rcbWaBtn" href="https://wa.me/5562991161040" target="_blank" rel="noopener noreferrer" data-event="cta_click" data-location="pos_formulario" data-page="home">Toque aqui para enviar a mensagem</a>.</p>
          </form>'''

SCRIPT_NOVO = '''<!-- Formulário -> WhatsApp no mesmo clique (29/10/2026). Nada é enviado a servidor:
       a mensagem pronta abre no WhatsApp e quem envia é o próprio visitante. -->
  <script>
  (function () {
    var WHATSAPP = '5562991161040';
    var form = document.getElementById('rcbLeadForm');
    if (!form) return;

    var erro = form.querySelector('.wform-erro');
    var aviso = document.getElementById('rcbAviso');
    var waBtn = document.getElementById('rcbWaBtn');
    var selServico = document.getElementById('rcbServico');
    var selNegocio = document.getElementById('rcbNegocio');

    // Artigo certo para a frase "tenho um(a) ___".
    var ARTIGO = {
      'Clínica': 'uma clínica',
      'Dentista': 'uma clínica odontológica',
      'Estética': 'uma clínica de estética',
      'Advocacia': 'um escritório de advocacia',
      'Contabilidade': 'um escritório de contabilidade',
      'Imobiliária': 'uma imobiliária',
      'Energia solar': 'uma empresa de energia solar',
      'Serviço em domicílio': 'uma empresa que atende no local do cliente',
      'Comércio local': 'um comércio local',
      'Profissional liberal': 'um trabalho como profissional liberal',
      'Outro': 'um negócio'
    };
    var PEDIDO = {
      'Aparecer no Google': 'Quero que a minha empresa apareça no Google e no Google Maps',
      'Site ou landing page': 'Quero um site ou uma landing page',
      'Anúncio no Google': 'Quero anunciar a minha empresa no Google',
      'Aparecer nas IAs': 'Quero que a minha empresa apareça no ChatGPT e no Gemini',
      'SEO para YouTube': 'Quero que os meus vídeos no YouTube tragam cliente',
      'Ainda não sei': 'Ainda não sei por onde começar e queria a sua opinião'
    };

    function campo(nome) {
      var el = form.elements.namedItem(nome);
      return el && typeof el.value === 'string' ? el.value.trim() : '';
    }

    function medir(evento, extra) {
      var params = {
        page_location: window.location.href,
        page_path: window.location.pathname,
        form_id: 'rcbLeadForm',
        lead_pacote: selServico.value,
        lead_negocio: selNegocio.value
      };
      for (var k in (extra || {})) params[k] = extra[k];
      if (typeof window.rcbTrackEvent === 'function') window.rcbTrackEvent(evento, params);
      else if (typeof window.gtag === 'function') window.gtag('event', evento, params);
    }

    // Os botões dos pacotes da home já deixam o serviço certo escolhido.
    document.querySelectorAll('[data-pacote]').forEach(function (link) {
      link.addEventListener('click', function () {
        var mapa = { 'presenca-lite': 'Aparecer no Google', presenca: 'Site ou landing page',
                     crescimento: 'Aparecer no Google', dominacao: 'Aparecer no Google' };
        var alvo = mapa[link.getAttribute('data-pacote')];
        if (alvo) selServico.value = alvo;
      });
    });

    var comecou = false;
    form.addEventListener('focusin', function () {
      if (comecou) return;
      comecou = true;
      medir('begin_lead');
    });

    function mensagemWhats() {
      return 'Olá, Renan! Meu nome é ' + campo('nome') +
        ', tenho ' + (ARTIGO[campo('tipo_de_negocio')] || 'um negócio') +
        ' em ' + campo('cidade') + '. ' +
        (PEDIDO[campo('servico')] || 'Quero um orçamento') + '. ' +
        'Meu WhatsApp é ' + campo('whatsapp') + '.';
    }

    form.addEventListener('submit', function (evento) {
      evento.preventDefault();
      erro.textContent = '';

      if (!form.checkValidity()) {
        var invalido = form.querySelector(':invalid');
        medir('lead_error', { error_field: (invalido && (invalido.name || invalido.id)) || 'desconhecido' });
        form.reportValidity();
        return;
      }

      var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(mensagemWhats());
      waBtn.href = url;
      aviso.hidden = false;
      medir('generate_lead', { method: 'formulario_whatsapp' });
      // Abre dentro do próprio clique: se esperasse alguma resposta, o celular bloquearia a janela.
      var janela = window.open(url, '_blank', 'noopener');
      if (!janela) window.location.href = url;
    });
  })();
  </script>'''

# /servicos/: cartões de orçamento (nome, para quem, o que entra, mensagem, botão)
CARTOES = [
    ("Aparecer no Google", "Para quem o cliente procura e não acha.",
     ["Perfil no Google Maps completo e na frente", "Site que o Google entende",
      "Rotina para juntar avaliações de clientes"],
     "Olá, Renan! Quero que a minha empresa apareça no Google.", "Quero aparecer no Google"),
    ("Clientes agora com anúncio", "Para quem precisa de contato esta semana, não daqui a meses.",
     ["Anúncio no Google para quem já está procurando", "Página feita para o anúncio virar conversa",
      "Medição de cada contato que o anúncio trouxe"],
     "Olá, Renan! Quero anunciar a minha empresa no Google.", "Quero anunciar no Google"),
    ("Site ou landing page", "Para quem é encontrado, mas o visitante sai sem chamar.",
     ["Abre rápido no celular", "Botão de WhatsApp em cada parte da página", "Medição de quem chamou"],
     "Olá, Renan! Quero um site ou uma landing page para a minha empresa.", "Quero um site que traga contato"),
    ("Aparecer nas IAs", "Para quando o cliente pergunta ao ChatGPT ou ao Gemini quem indicar.",
     ["Auditoria pronta em 1 a 3 dias úteis", "Dados iguais em todo lugar onde a IA confere",
      "Páginas com respostas que a IA consegue citar"],
     "Olá, Renan! Quero que a minha empresa apareça nas respostas do ChatGPT e do Gemini.",
     "Quero aparecer nas IAs"),
]
CONDICAO_VELHA = '<p class="pacote-condicao">Valor sob medida para o tamanho do seu projeto</p>'
CONDICAO_NOVA = '<p class="pacote-condicao">Orçamento grátis e sob medida, em até 24 horas</p>'


def home(h):
    if "rcbLeadOk" not in h and "web3forms" not in h:
        return h
    ini = h.index('<form class="wform" id="rcbLeadForm" novalidate>')
    fim_ok = h.index('<div class="wform-ok" id="rcbLeadOk" hidden>')
    fim = h.index("</div>", h.index("</a>", fim_ok)) + len("</div>")
    h = h[:ini] + FORM_NOVO + h[fim:]
    s_ini = h.index("<!-- Formulário -> Web3Forms -> WhatsApp.")
    s_fim = h.index("</script>", s_ini) + len("</script>")
    return h[:s_ini] + SCRIPT_NOVO + h[s_fim:]


def servicos(h):
    spec = importlib.util.spec_from_file_location("servicos_ger", os.path.join(AQUI, "gerar-servicos-marketing.py"))
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    m = re.search(r'\n    <section class="pacotes-section" id="orcamento".*?</section>\n', h, re.S)
    d = {"titulo": "Por qual serviço a sua empresa quer começar?",
         "desc": "Escolha o ponto de partida. O orçamento é grátis e sai em até 24 horas pelo WhatsApp.",
         "destaque": 1, "itens": CARTOES}
    # o gerador ainda escreve um travessão na nota; a página no ar já tem a vírgula
    novo = (S.s_orcamento(d, "servicos").replace(CONDICAO_VELHA, CONDICAO_NOVA)
            .replace(" faz sentido — inclusive", " faz sentido, inclusive"))
    return h[:m.start()] + novo + h[m.end():]


def main():
    os.chdir(RAIZ)
    alterados = []
    for f, fn in (("index.html", home), (os.path.join("servicos", "index.html"), servicos)):
        h = io.open(f, encoding="utf-8").read()
        novo = fn(h)
        if novo != h:
            assert novo.lstrip().lower().startswith("<!doctype"), f
            alterados.append(f)
            if APLICAR:
                io.open(f, "w", encoding="utf-8", newline="").write(novo)
    print("%s: %d" % ("alterados" if APLICAR else "seriam alterados", len(alterados)))
    for f in alterados:
        print("  ", f)


if __name__ == "__main__":
    main()
