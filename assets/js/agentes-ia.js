/* ==========================================================================
   agentes-ia.js — dá vida às simulações da linha "Agentes de IA".

   Duas coisas, só:
     1. O celular que "conversa sozinho" (troca de cenário, digitando, balões).
     2. As calculadoras de perda (faltas na clínica / carrinho abandonado).

   Regras que valem sempre:
     - Nada aqui envia dado para lugar nenhum. É tudo desenho na tela.
     - A conversa do primeiro cenário já vem escrita no HTML pelo gerador.
       Se o JavaScript não rodar, o visitante ainda lê a conversa inteira.
     - Quem pediu menos movimento no sistema vê tudo de uma vez, parado.
     - Roda dentro de uma IIFE: nenhum nome vaza para o escopo global.
       (Já derrubamos o /script.js uma vez por colisão de nome em
       /para-comercios-locais/. Não repetir.)
   ========================================================================== */
(function () {
  "use strict";

  var semMovimento = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------------ */
  /* Utilidades                                                          */
  /* ------------------------------------------------------------------ */

  function criar(tag, classe, texto) {
    var el = document.createElement(tag);
    if (classe) el.className = classe;
    if (texto != null) el.textContent = texto;
    return el;
  }

  var CHECK_AZUL =
    '<svg class="wa-check" width="15" height="11" viewBox="0 0 16 11" fill="none" ' +
    'aria-hidden="true"><path d="M1 5.5 4.2 8.7 10.2 1" stroke="currentColor" ' +
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>' +
    '<path d="M5.8 5.5 9 8.7 15 1" stroke="currentColor" stroke-width="1.6" ' +
    'stroke-linecap="round" stroke-linejoin="round"/></svg>';

  /* ------------------------------------------------------------------ */
  /* 1. O celular                                                        */
  /* ------------------------------------------------------------------ */

  function montarDemo(raiz) {
    var fonte = raiz.querySelector("[data-wa-roteiro]");
    var thread = raiz.querySelector("[data-wa-thread]");
    if (!fonte || !thread) return;

    var roteiro;
    try {
      roteiro = JSON.parse(fonte.textContent);
    } catch (e) {
      return; // roteiro quebrado: fica o HTML estático que já está na tela
    }
    var cenarios = roteiro.cenarios || [];
    if (!cenarios.length) return;

    var botoes = [].slice.call(raiz.querySelectorAll("[data-cenario]"));
    var nota = raiz.querySelector("[data-wa-nota]");
    var replay = raiz.querySelector("[data-wa-replay]");
    var relogios = [];
    var atual = 0;

    function limparRelogios() {
      relogios.forEach(clearTimeout);
      relogios = [];
    }

    function balao(msg) {
      var enviada = msg.de === "agente";
      var linha = criar("div", "wa-linha " + (enviada ? "wa-linha--enviada" : "wa-linha--recebida"));
      var b = criar("div", "wa-balao");

      String(msg.texto || "").split("\n").forEach(function (par) {
        if (par.trim()) b.appendChild(criar("p", null, par));
      });

      if (msg.opcoes && msg.opcoes.length) {
        var ul = criar("ul", "wa-opcoes");
        msg.opcoes.forEach(function (o) { ul.appendChild(criar("li", null, o)); });
        b.appendChild(ul);
      }

      var meta = criar("div", "wa-meta");
      meta.appendChild(document.createTextNode(msg.hora || ""));
      if (enviada) meta.insertAdjacentHTML("beforeend", CHECK_AZUL);
      b.appendChild(meta);

      linha.appendChild(b);
      return linha;
    }

    function digitando() {
      var linha = criar("div", "wa-linha wa-linha--enviada wa-digitando");
      var b = criar("div", "wa-balao");
      for (var i = 0; i < 3; i++) b.appendChild(criar("span", "wa-ponto"));
      linha.appendChild(b);
      return linha;
    }

    function aoFim() {
      thread.scrollTop = thread.scrollHeight;
    }

    function tocar(indice) {
      limparRelogios();
      atual = indice;
      var cenario = cenarios[indice];
      if (!cenario) return;

      botoes.forEach(function (b, i) {
        b.setAttribute("aria-selected", i === indice ? "true" : "false");
        b.tabIndex = i === indice ? 0 : -1;
      });
      if (nota) nota.innerHTML = cenario.nota || "";

      thread.innerHTML = "";
      if (roteiro.dia) thread.appendChild(criar("div", "wa-dia", roteiro.dia));

      var mensagens = cenario.mensagens || [];

      // Sem animação: tudo de uma vez.
      if (semMovimento) {
        mensagens.forEach(function (m) { thread.appendChild(balao(m)); });
        aoFim();
        return;
      }

      var acumulado = 0;
      mensagens.forEach(function (msg, i) {
        var ehAgente = msg.de === "agente";
        var pausa = msg.espera != null ? msg.espera : (i === 0 ? 250 : 900);
        acumulado += pausa;

        if (ehAgente) {
          var tempoDigitando = Math.min(1500, 380 + String(msg.texto || "").length * 11);
          var marcaDigitando = acumulado;
          relogios.push(setTimeout(function () {
            var d = digitando();
            d.setAttribute("data-digitando", "1");
            thread.appendChild(d);
            aoFim();
          }, marcaDigitando));
          acumulado += tempoDigitando;
        }

        var marcaBalao = acumulado;
        relogios.push(setTimeout(function () {
          var d = thread.querySelector("[data-digitando]");
          if (d) d.remove();
          thread.appendChild(balao(msg));
          aoFim();
        }, marcaBalao));
      });
    }

    /* trocar de cenário pelos botões (com setas do teclado, como aba) */
    botoes.forEach(function (btn, i) {
      btn.addEventListener("click", function () { tocar(i); });
      btn.addEventListener("keydown", function (ev) {
        var passo = ev.key === "ArrowRight" ? 1 : ev.key === "ArrowLeft" ? -1 : 0;
        if (!passo) return;
        ev.preventDefault();
        var alvo = (i + passo + botoes.length) % botoes.length;
        botoes[alvo].focus();
        tocar(alvo);
      });
    });

    if (replay) {
      replay.addEventListener("click", function () { tocar(atual); });
    }

    /* só começa quando o celular aparece na tela — senão a conversa
       termina antes de o visitante chegar nela */
    if ("IntersectionObserver" in window) {
      var jaComecou = false;
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (e) {
          if (e.isIntersecting && !jaComecou) {
            jaComecou = true;
            tocar(0);
            obs.disconnect();
          }
        });
      }, { threshold: 0.35 });
      obs.observe(raiz);
    } else {
      tocar(0);
    }
  }

  /* ------------------------------------------------------------------ */
  /* 2. Calculadoras                                                     */
  /* ------------------------------------------------------------------ */

  var emReais = new Intl.NumberFormat("pt-BR", {
    style: "currency", currency: "BRL", maximumFractionDigits: 0
  });

  function montarCalculadora(raiz) {
    var campos = [].slice.call(raiz.querySelectorAll("input[type=range]"));
    var saidaNumero = raiz.querySelector("[data-calc-numero]");
    var saidaObs = raiz.querySelector("[data-calc-obs]");
    if (!campos.length || !saidaNumero) return;

    function valor(nome) {
      var el = raiz.querySelector('input[data-campo="' + nome + '"]');
      return el ? Number(el.value) : 0;
    }

    function atualizar() {
      campos.forEach(function (c) {
        var eco = raiz.querySelector('[data-eco="' + c.getAttribute("data-campo") + '"]');
        if (!eco) return;
        eco.textContent = c.getAttribute("data-formato") === "reais"
          ? emReais.format(Number(c.value))
          : c.value + (c.getAttribute("data-sufixo") || "");
      });

      var tipo = raiz.getAttribute("data-calc");
      var perdaMes = 0;
      var obs = "";

      if (tipo === "faltas") {
        var atendimentos = valor("atendimentos");
        var faltas = valor("faltas");          // em %
        var ticket = valor("ticket");
        var qtdFaltas = Math.round(atendimentos * (faltas / 100));
        perdaMes = qtdFaltas * ticket;
        obs = "São cerca de <strong>" + qtdFaltas + " horários vagos por mês</strong> — " +
              "aproximadamente " + emReais.format(perdaMes * 12) + " ao longo de um ano.";
      } else if (tipo === "carrinho") {
        var carrinhos = valor("carrinhos");
        var ticketProd = valor("ticket");
        perdaMes = carrinhos * ticketProd;
        obs = "Se apenas <strong>1 em cada 10</strong> dessas pessoas voltasse e comprasse, " +
              "seriam " + emReais.format(perdaMes * 0.1) + " a mais no mês. " +
              "Esse 1 em 10 é uma conta de exemplo, não uma promessa de resultado.";
      }

      saidaNumero.textContent = emReais.format(perdaMes);
      if (saidaObs) saidaObs.innerHTML = obs;
    }

    campos.forEach(function (c) {
      c.addEventListener("input", atualizar);
      c.addEventListener("change", atualizar);
    });
    atualizar();
  }

  /* ------------------------------------------------------------------ */

  function iniciar() {
    [].slice.call(document.querySelectorAll("[data-wa-demo]")).forEach(montarDemo);
    [].slice.call(document.querySelectorAll("[data-calc]")).forEach(montarCalculadora);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciar);
  } else {
    iniciar();
  }
})();
