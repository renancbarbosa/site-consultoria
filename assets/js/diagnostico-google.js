(function () {
  "use strict";

  var form = document.getElementById("seo-check");
  var result = document.getElementById("seo-check-result");
  if (!form || !result) return;

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var total = form.querySelectorAll('input[name="item"]:checked').length;
    var score = Math.round((total / 8) * 100);
    var title;
    var text;
    var link;

    if (total <= 3) {
      title = "A base ainda está incompleta";
      text = "Priorize perfil verificado, dados corretos e indexação do site. Criar mais conteúdo antes disso tende a espalhar esforço.";
      link = '<a href="/blog/como-colocar-minha-empresa-no-google/">Começar pelo cadastro e pela verificação</a>';
    } else if (total <= 6) {
      title = "A empresa já existe no Google, mas há lacunas";
      text = "Feche os pontos não marcados e conecte perfil, páginas de serviço, avaliações e medição. É aqui que muita empresa fica parada.";
      link = '<a href="/blog/como-melhorar-posicionamento-empresa-google/">Ver o plano para melhorar o posicionamento</a>';
    } else {
      title = "A base parece forte; agora o problema é competitivo";
      text = "Investigue intenção de busca, páginas concorrentes, diferença local, cliques e conversão. Repetir o básico provavelmente não será suficiente.";
      link = '<a href="/diagnostico-presenca-digital/">Pedir uma análise dos concorrentes e das prioridades</a>';
    }

    result.innerHTML = '<strong>' + score + '/100 — ' + title + '</strong><p>' + text + '</p><p>' + link + '</p>';
    result.hidden = false;
    result.focus({ preventScroll: true });
    result.scrollIntoView({ behavior: "smooth", block: "nearest" });
  });
}());
