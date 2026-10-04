# Projeto: foco em SEO + nichos nacionais (outubro/2026)

> **Se a sessão reiniciar, leia este arquivo primeiro e continue de onde parou.**
> Uma etapa por vez. Ao fim de cada uma: PARAR, mostrar o relatório e esperar
> "aprovado, siga". Nunca publicar sem "pode publicar".

## Status das etapas (plano revisado de 04/10/2026)

| Etapa | Escopo | Status |
|---|---|---|
| — | Marca RCB SEO + exclusão das 168 cidades noindex | **publicada** 04/10/2026 (`f27d12c`, `5487081`; IndexNow 166 + 168 URLs aceito) |
| 0 | Diagnóstico e mapa (só leitura) | **concluída** (plano + linha de base em `bbc8f4f`) |
| 1 | Limpeza de foco (agentes de IA, IPTV/apostas 410, home/menu/rodapé/ficha/llms nos 4 serviços) | **publicada** 04/10/2026 (`90d3bc3`; 410 e 301 conferidos no ar; IndexNow 162 + 32 URLs aceito) |
| 2 | Landing page para anúncios (urgente) + modelo demonstrativo | **em andamento** |
| 3 | Tráfego pago empresarial (reorganizar as 7 páginas) | pendente |
| 4 | Energia solar (marketing completo) | pendente |
| 5 | SEO para YouTube | pendente |
| 6 | Limpeza empresarial | pendente |
| 7 | Fortalecer estética e pequenas empresas | pendente |
| 8 | Advocacia (juntar em /marketing-para-advogados/) | pendente |
| 9a–9d | Serviços de rua: higienização, guincho, reformas, dedetização | pendente |
| 10 | Hubs "Serviços" e "Nichos que atendemos" | pendente |
| 11 | Medição (28 dias depois da Etapa 2) | pendente |

**Redirecionamento:** o site está no **Cloudflare Pages** (não GitHub Pages): 301 pelo
arquivo `_redirects` da raiz. Não usar meta refresh.

**Linha de base:** `reports/baseline/2026-10-04/` — Search Console 04/09 a 01/10/2026
(28 dias): 139 páginas com impressão, 2.140 impressões, 11 cliques.

## Etapa 1 — o que foi feito (prévia local, 04/10/2026)
- Menu e rodapé: fonte única em `scripts/rcb_menu.py` (`PROVISORIO` guarda os destinos
  temporários). Reaplicar: `python scripts/foco-etapa1-2026-10-04.py` (idempotente).
  Rótulo do 1º item encurtado para **"SEO e Google"** (o completo não cabe entre 1024 e
  1366 px; medido no navegador). Hambúrguer passou de 900 para **1000 px**.
- Blog, Cases e Sobre saíram do menu e foram para o rodapé (bloco `RCB:INSTITUCIONAL`).
- 4 páginas de agentes de IA/automação/recuperação apagadas; 301 no `_redirects`.
- IPTV e apostas: 28 endereços respondem **410** via `functions/_middleware.js`, limitado
  por `_routes.json` (o resto do site continua estático). Conferir no ar após publicar.
- Geradores (`rcb_base.py`, `gerar-paginas-cidades.py`) aplicam `rcb_menu.aplicar()` na
  gravação. Travados: `gerar-agentes-ia.py`, `rcb_agentes.py`, `menu-agentes-ia.py`,
  `menu-sites-anuncios.py`. Apagados: `assets/css/agentes-ia.css`, `assets/js/agentes-ia.js`.
- Provisórios até a etapa de cada um: "SEO para YouTube" → `/conteudo-para-seo/` (Etapa 5);
  "Tráfego Pago" → `/gestao-de-trafego-pago-goiania/` (Etapa 3); landing page →
  `/criacao-de-landing-page-goiania/` (Etapa 2).

## Decisões anteriores (04/10/2026)
- Marca oficial "RCB SEO"; dados só em `data/marca.json`.
- 168 cidades noindex excluídas; ficam as 31 indexáveis.
- Perfil do Google não será renomeado agora — não lembrar de novo.
- Etapa 1: menu com "SEO e Google" (aprovado); "SEO para YouTube" fora do menu até a Etapa 5 (`MOSTRAR_YOUTUBE` em `rcb_menu.py`); cartão da home sem link até lá.
- Etapa 0 respondida: agentes de IA redirecionar/excluir; tráfego pago, landing e loja ficam; IPTV e apostas 410; domínios fora; advocacia principal = /marketing-para-advogados/ (Etapa 8).

---

# DECISÕES DA ETAPA 0 + PLANO REVISADO (04/10/2026)

Substitui as etapas antigas no docs/plano-nichos-2026-10.md. Copie este plano para lá.
A marca RCB SEO e a exclusão das 168 cidades JÁ estão publicadas (f27d12c, 5487081).

## MUDANÇA DE ESCOPO

Tráfego pago FICA e vira serviço forte. O site passa a oferecer 4 serviços:
1. SEO (orgânico) e Google Meu Negócio
2. Sites e LANDING PAGES PARA ANÚNCIOS (prioridade URGENTE: tenho uma indicação agora)
3. TRÁFEGO PAGO EMPRESARIAL: anúncios no Google (Google Ads, rede de pesquisa) para
   empresas que querem cliente rápido. NÃO é "impulsionar post no Instagram": Meta Ads
   só como complemento, e sempre com landing page e medição de conversão.
4. SEO PARA YOUTUBE (crescer canal de empresa ou de profissional no YouTube)

Mensagem central do site: "trazer clientes pelo Google": anúncio para o resultado
rápido, SEO para o resultado duradouro, landing page e site para converter.
Continua fora: agentes de IA, automação e recuperação de vendas.
Continua valendo: nenhum preço no site (orçamento individual grátis pelo WhatsApp em
até 24 horas), nenhuma garantia, marca e contato só de data/marca.json.

Atualize a nota na memória do projeto para: "O site oferece SEO, Google Meu Negócio,
sites e landing pages, tráfego pago empresarial (Google Ads) e SEO para YouTube, para
DONOS de negócio. Sem agentes de IA, automação ou recuperação de vendas. Sem preço.
Público-alvo é o dono, nunca o cliente final do nicho."

## REGRA DE OURO (atualizada)

Quem deve achar o site é o DONO/EMPRESA procurando o NOSSO serviço: "landing page para
google ads", "criar landing page", "gestão de tráfego pago para empresas", "agência de
google ads", "marketing para energia solar", "seo para youtube", "como crescer canal no
youtube". Nunca o cliente final do nicho ("guincho perto de mim", "dedetizadora goiânia").
Título, H1, descrição, primeiro parágrafo e H2 falam sempre com o dono. Buscas do
cliente final só no meio do texto, entre aspas, como argumento. Nas fichas, o serviço é
o nosso, com público "empresas de [nicho]" (BusinessAudience).

## REGRA DE HONESTIDADE (nova)

Eu ainda não tenho cases de landing page nem de tráfego pago. É PROIBIDO inventar
portfólio, cliente, número de resultado ou depoimento. Use: processo, o que está
incluído, prazo, perguntas frequentes e MODELOS DEMONSTRATIVOS claramente marcados como
"Modelo demonstrativo — empresa fictícia".

## DECISÕES DA ETAPA 0 (respostas às suas perguntas)

1. Agentes de IA: SIM, como você propôs. /agentes-de-ia/ → home,
   /agente-de-ia-para-clinicas/ → /seo-para-clinicas/,
   /recuperacao-de-vendas-whatsapp/ → home (301 no _redirects);
   /automacao-de-processos/ excluir.
2. Tráfego pago: as 7 páginas FICAM (serão reorganizadas na Etapa 3).
   Landing page: FICA e vira prioridade (Etapa 2). Loja virtual: manter como está.
3. IPTV e apostas: SIM, responder 410 (removida de vez) em todos os endereços.
   Domínios: deixar fora, não republicar.
4. Advocacia: /marketing-para-advogados/ será a principal, com 301 de /para-advogados/
   (fazer na Etapa 8).

## AS REGRAS DO PLANO ANTERIOR CONTINUAM VALENDO

Uma etapa por vez; PARE no fim de cada uma; só publique com "pode publicar"; conteúdo
próprio (semelhança abaixo de 40%); fatos com fonte oficial; parágrafo-resposta, H2 em
pergunta, FAQ, fichas, autor Renan; título ≤ 65 e descrição ≤ 160; checar canibalização
antes de criar; sitemap e llms.txt com links nas seções; conferências de fichas,
lychee, limites, semelhança, regra de ouro e /claude-seo:seo page; relatório curto no
formato fixo; arquivo de progresso sempre atualizado.

## NOVAS ETAPAS (nesta ordem)

### ETAPA 1 - Limpeza de foco
- Retirar agentes de IA, automação e recuperação de vendas: menu, coluna do rodapé, os
  22 links dos artigos, a linha do llms.txt, os redirecionamentos e a exclusão acima;
  desativar gerar-agentes-ia.py, rcb_agentes.py, menu-agentes-ia.py, agentes-ia.css,
  agentes-ia.js e a linha em aplicar-conversao.py.
- IPTV e apostas: 410.
- Revisar a home, o menu, o rodapé, a ficha da empresa (lista de serviços oferecidos) e
  o llms.txt para os 4 serviços acima. Menu sugerido: SEO e Google Meu Negócio |
  Sites e Landing Pages | Tráfego Pago | SEO para YouTube | Nichos | Contato. Itens que
  ainda não têm página apontam para a página atual mais próxima até a etapa deles.
PARE.

### ETAPA 2 - LANDING PAGE PARA ANÚNCIOS (urgente)
a) Página de serviço NACIONAL "Criação de Landing Page para Anúncios (Google Ads)".
   Decida pela canibalização: transformar /criacao-de-landing-page-goiania/
   (1 impressão) em nacional, com 301, ou criar uma nova e manter a de Goiânia local.
   Proponha antes de fazer.
   Buscas-alvo do dono: "landing page para google ads", "criação de landing page",
   "landing page para anúncios", "landing page que converte", "quanto custa uma landing
   page" (responder sem preço: explicar o que define o orçamento).
   Conteúdo: o que é (em palavras simples), por que anúncio sem landing page desperdiça
   dinheiro, o que está incluído (página rápida no celular, botão de WhatsApp,
   formulário com aviso de LGPD, medição de conversão no Google Ads e no GA4, pixel da
   Meta quando houver, teste de velocidade, domínio e hospedagem orientados), prazo de
   entrega, como funciona passo a passo, perguntas frequentes, chamada para orçamento.
b) UM modelo demonstrativo de landing page de empresa fictícia (sugestão: integrador de
   energia solar), em endereço próprio, com noindex, marcado no topo como "Modelo
   demonstrativo — empresa fictícia". Bonito, rápido (meta: nota 90+ no Lighthouse no
   celular), para eu mandar a clientes. Link para ele a partir da página de serviço.
PARE (prévia local, com o resultado do Lighthouse). Depois do "pode publicar", publique.

### ETAPA 3 - TRÁFEGO PAGO EMPRESARIAL (reorganizar as 7 páginas)
a) Página principal NACIONAL "Gestão de Tráfego Pago para Empresas (Google Ads)".
   Proponha o endereço checando a canibalização com /gestao-de-trafego-pago-goiania/
   (a de Goiânia pode continuar local ou ser fundida com 301; me mostre a recomendação).
   Buscas-alvo: "gestão de tráfego pago para empresas", "agência de google ads",
   "gestor de tráfego google ads", "anúncios no google para empresas", "tráfego pago
   para empresas". Ângulo: anúncio na pesquisa do Google (pega quem já está procurando)
   é diferente de impulsionar post; sempre com landing page e medição; anúncio + SEO
   juntos. Ligar com a landing page da Etapa 2.
b) As 4 páginas "tráfego pago para [nicho]" (advogados, dentistas, energia solar,
   imobiliárias): manter, revisar para conteúdo próprio de cada nicho (ex.: advogados
   seguem as regras da OAB para anúncio; dentistas, as do CFO para publicidade; sempre
   com fonte oficial) e ligar cada uma à página de SEO do mesmo nicho e à principal.
c) Os 2 artigos do blog de tráfego pago: manter e ligar à principal.
PARE. Mesmo fluxo.

### ETAPA 4 - ENERGIA SOLAR (marketing completo)
Página principal /marketing-para-energia-solar/ cobrindo SEO, Google Meu Negócio,
anúncios e landing page para integradores. Integrar /trafego-pago-para-energia-solar/
e os 2 artigos existentes. Artigos: fortalecer "como conseguir clientes para energia
solar" e criar "como divulgar empresa de energia solar". Ângulos: Lei 14.300/2022 com
link oficial, números de CNPJ do ramo, sazonalidade, o cliente do integrador busca
economia na conta de luz (argumento, não alvo).
PARE. Mesmo fluxo.

### ETAPA 5 - SEO PARA YOUTUBE
Página de serviço "SEO para YouTube: como fazer seu canal crescer". Buscas-alvo:
"seo para youtube", "como crescer canal no youtube", "como ranquear vídeo no youtube",
"seo youtube empresa". Ângulos próprios: título, descrição, capítulos, transcrição e
miniatura; o ChatGPT e o Google leem a transcrição e a descrição, não assistem ao vídeo
(vídeo também precisa ser otimizado para ser citado por IA); YouTube como vitrine para
empresa local; ligar com SEO e Google Meu Negócio. Sem prometer números.
PARE. Mesmo fluxo.

### ETAPA 6 - LIMPEZA EMPRESARIAL (marketing completo)
Página principal "Marketing para empresas de limpeza e terceirização" + artigos
"Como conseguir clientes para empresa de limpeza" e "Como divulgar empresa de limpeza".
Ângulos: contrato mensal recorrente, condomínios e empresas, proposta comercial, Google
Meu Negócio para quem atende na região do cliente, anúncio no Google para
"terceirização de limpeza" (argumento).
PARE. Mesmo fluxo.

### ETAPA 7 - FORTALECER ESTÉTICA E PEQUENAS EMPRESAS
Como no mapa da Etapa 0, sem trocar títulos de páginas com tráfego; retitular o artigo
de estética com "Goiânia" no título para falar com a dona.
PARE. Mesmo fluxo.

### ETAPA 8 - ADVOCACIA
Juntar em /marketing-para-advogados/ (301 de /para-advogados/), ângulo Provimento
205/2021 da OAB com link oficial (o Renan é formado em Direito; não dizer que é
advogado); artigos do mapa da Etapa 0; ligar com /trafego-pago-para-advogados/.
PARE. Mesmo fluxo.

### ETAPA 9 - SERVIÇOS DE RUA (uma sub-etapa por vez, PARE em cada uma)
9a Higienização de estofados · 9b Guincho · 9c Reformas · 9d Dedetização (regras da
Anvisa, link oficial). Para cada um: página principal "Marketing para empresas de
[nicho]" + 1 artigo "Como conseguir clientes para [nicho]". Servem também de vitrine
para prospecção ativa.

### ETAPA 10 - PÁGINAS "SERVIÇOS" E "NICHOS QUE ATENDEMOS"
Hubs ligando os 4 serviços e todas as páginas de nicho, no menu e no rodapé.
PARE. Mesmo fluxo.

### ETAPA 11 - MEDIÇÃO (28 dias depois da Etapa 2)
Compare com a linha de base de 04/10/2026, por serviço e por nicho. Liste buscas de
cliente final que estiverem atraindo impressões e proponha a correção.

