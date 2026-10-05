# Projeto: foco em SEO + nichos nacionais (outubro/2026)

> **Se a sessão reiniciar, leia este arquivo primeiro e continue de onde parou.**
> Uma etapa por vez. Ao fim de cada uma: PARAR, mostrar o relatório e esperar
> "aprovado, siga". Nunca publicar sem "pode publicar".

> **Próxima etapa (anotado em 05/10/2026): 9b — Guincho.** Página principal "Marketing para empresas de guincho" + 1 artigo "Como conseguir clientes para guincho". Mesmo modelo da 9a (servicos_marketing.py + artigos_nichos_anuncios.py, gerar-servicos-marketing.py e RCB_ARTIGO_SLUG=... gerar-artigos-sites.py; reverter as 3 páginas que o gerador mexe na ficha da empresa: loja virtual, site para contador e site para dentista).

## Status das etapas (plano revisado de 04/10/2026)

| Etapa | Escopo | Status |
|---|---|---|
| — | Marca RCB SEO + exclusão das 168 cidades noindex | **publicada** 04/10/2026 (`f27d12c`, `5487081`; IndexNow 166 + 168 URLs aceito) |
| 0 | Diagnóstico e mapa (só leitura) | **concluída** (plano + linha de base em `bbc8f4f`) |
| 1 | Limpeza de foco (agentes de IA, IPTV/apostas 410, home/menu/rodapé/ficha/llms nos 4 serviços) | **publicada** 04/10/2026 (`90d3bc3`; 410 e 301 conferidos no ar; IndexNow 162 + 32 URLs aceito) |
| 2 | Landing page para anúncios (urgente) + modelo demonstrativo | **publicada** 04/10/2026 (`5f0e869`; página, 301 e modelo conferidos no ar; IndexNow 163 URLs aceito) |
| 3 | Tráfego pago empresarial (reorganizar as 7 páginas) | **publicada** 04/10/2026 (`0e619b73`; principal, 301 e 4 nichos conferidos no ar; IndexNow 163 URLs aceito) |
| 4 | Energia solar (marketing completo) | **publicada** 04/10/2026 (`2e818aea`; página e 2 artigos conferidos no ar; IndexNow aceito) |
| 5 | SEO para YouTube | **publicada** 04/10/2026 (`328ff9bb`; página, menu, cartão da home e rodapé conferidos no ar; IndexNow aceito) |
| 6 | Limpeza empresarial | **publicada** 05/10/2026 (`feacb175`; 3 URLs conferidas em 200; IndexNow 4 URLs aceito) |
| 7 | Fortalecer estética e pequenas empresas | **publicada** 05/10/2026 (`982b8134`; 9 URLs conferidas em 200 com o conteúdo novo; IndexNow 9 URLs aceito) |
| 8 | Advocacia (juntar em /marketing-para-advogados/) | **publicada** 05/10/2026 (`7360a547`; 6 URLs em 200, /para-advogados/ /para-advogados e .html em 301 para a nova; IndexNow 7 URLs aceito) |
| 9a | Higienização de estofados | **publicada** 05/10/2026 (`b202226b`; 2 URLs novas + blog, sitemap e llms.txt em 200 com o conteúdo novo; IndexNow 3 URLs aceito) |
| 9b–9d | Serviços de rua: guincho, reformas, dedetização | pendente |
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

## Etapa 2 — o que foi feito (prévia local, 04/10/2026)
- Decisão do Renan: a página de Goiânia virou **nacional** em `/criacao-de-landing-page/`,
  com 301 de `/criacao-de-landing-page-goiania/` (1 impressão em 28 dias, posição 104).
- Conteúdo em `scripts/conteudo/servicos_marketing.py`; gerador `gerar-servicos-marketing.py`
  ganhou campos opcionais (só para quem usa): `data` (autor + data visíveis e no schema),
  `nacional` (areaServed Brasil), `publico` (audience BusinessAudience), `faq_titulo` e a
  seção `chamada`. As outras 10 páginas do gerador não mudaram (restauradas e conferidas).
- Modelo demonstrativo: `/modelos/landing-page-energia-solar/` — "Sua Empresa Solar"
  (fictícia), noindex, fora do sitemap, faixa "Modelo demonstrativo — empresa fictícia",
  botões de WhatsApp levam ao WhatsApp da RCB SEO, formulário só demonstrativo.
  Fora do `conferir-conversao.py` (lista FORA_DA_CONFERENCIA).
- Menu, rodapé, home e llms.txt apontam para o endereço novo (`PROVISORIO["landing"]`).
- Prazo (decisão do Renan): "primeira versão em até 5 dias úteis depois de receber as informações da empresa (textos, fotos e logo)". Modelo usa o WhatsApp do Renan (aprovado).
- ATENÇÃO ao regerar: `gerar-servicos-marketing.py` reescreve as 11 páginas; restaurar as outras do git apaga mudanças locais ainda não commitadas nelas (aconteceu com o link da landing em /gestao-de-trafego-pago-goiania/). Rodar `foco-etapa1-2026-10-04.py` e conferir links depois.

## Etapa 3 — o que foi feito (prévia local, 04/10/2026)
- Decisão do Renan: página **nacional** `/gestao-de-trafego-pago/` ("Gestão de Tráfego Pago para
  Empresas (Google Ads)"), com 301 de `/gestao-de-trafego-pago-goiania/` (0 impressão em 28 dias).
- 4 páginas de nicho (advogados, dentistas, energia solar, imobiliárias): texto próprio por nicho em
  `TRAFEGO_EXTRA`/`_EXTRA2` (`scripts/conteudo/servicos_nichos.py`), Google Ads primeiro e Meta como
  complemento, fonte oficial de cada uma (OAB Provimento 205/2021, CFO-196/2019, COFECI 458/1995,
  Lei 14.300/2022 + CDC art. 37) e link para a página de SEO do nicho. Semelhança entre elas:
  de 51–56% para 34–39%.
- Imobiliárias: saiu a menção a "políticas de habitação do Google e do Meta" (não confirmada para o
  Brasil); entrou a regra verificada do COFECI (CRECI no anúncio).
- `/blog/seo-ou-trafego-pago-empresa-local/`: corrigida a frase "não vendo gestão de tráfego pago"
  (contradizia o serviço novo) e incluído link para a página principal.

## Etapa 4 — o que foi feito (prévia local, 04/10/2026)
- Página principal nova `/marketing-para-energia-solar/` (servicos_marketing.py): Google Meu Negócio,
  site/SEO, Google Ads e landing page para integradores; liga com /trafego-pago-para-energia-solar/,
  os 3 artigos e o modelo demonstrativo.
- Artigo fortalecido `/blog/como-conseguir-clientes-energia-solar/` (frase sem fonte trocada pelo dado
  IBGE/CNPJ; seção de sazonalidade com ANEEL; links para a principal e o artigo novo).
- Artigo novo `/blog/como-divulgar-empresa-de-energia-solar/` (10 ideias práticas).
- Fontes: Lei 14.300/2022, CDC art. 37, ANEEL bandeiras tarifárias, IBGE/Concla CNAE 4321-5/00
  (inclui instalação de painéis fotovoltaicos), CNPJ público jun/2026 (328.524 ativas, 17.358
  abertas em 90 dias — código inclui eletricistas em geral, dito na página), LGPD.
- Sitemap 162 → 164; llms.txt ganhou a seção "## Energia solar" com links.

## Etapa 5 — o que foi feito (prévia local, 04/10/2026)
- Página nova `/seo-para-youtube/` (servicos_marketing.py). Fontes: "Como funciona a busca do YouTube"
  (relevância, engajamento, qualidade), ajuda do YouTube (capítulos, transcrição automática, miniatura
  personalizada) e guia de SEO para vídeo do Google. Sem promessa de inscritos/visualizações.
- Sobre IA: escrito que buscadores e IAs "dependem muito do texto que acompanha o vídeo" (sem afirmar
  que "não assistem ao vídeo", por falta de fonte).
- Menu: `MOSTRAR_YOUTUBE = True` e destino `/seo-para-youtube/` em `rcb_menu.py`; cartão da home com link;
  "SEO para YouTube" também no rodapé (lista de serviços); llms.txt e sitemap (164 → 165).

## Etapa 6 — o que foi feito (prévia local, 05/10/2026)
- Página nova `/marketing-para-empresa-de-limpeza/` (servicos_marketing.py) e artigos
  `/blog/como-conseguir-clientes-para-empresa-de-limpeza/` e `/blog/como-divulgar-empresa-de-limpeza/`
  (artigos_nichos_anuncios.py). Ângulos: contrato mensal, condomínios e empresas, proposta comercial,
  Google Meu Negócio com área de atendimento (sem endereço quando o cliente não vai ao local) e
  "terceirização de limpeza" como argumento de anúncio.
- Fontes: ajuda do Google sobre áreas de atendimento (cita prestadores de limpeza), Lei 6.019/1974
  (redação da Lei 13.429/2017), CNAE 8121-4/00 no IBGE e LGPD. CNPJ (fotografia jun/2026):
  8121-4/00 = 15.874 ativas, 466 abertas em 90 dias.
- Índice do blog (+2 cartões, categoria "Limpeza e terceirização"), sitemap (165 → 168) e llms.txt
  (seção "Limpeza e terceirização").
- Conferido: semelhança máx. 38,9% (página principal × energia solar; artigos 15,8% e 24,6%), títulos
  47–59 e descrições 146–157 sem duplicar, fichas válidas (Service com BusinessAudience / BlogPosting +
  BreadcrumbList + FAQPage), lychee 0 erros, conferidor só com os 3 avisos antigos, cidades ok.

## Etapa 7 — o que foi feito (prévia local, 05/10/2026)
- Script `scripts/etapa7-estetica-pequenas-2026-10-05.py` (idempotente; 2ª execução "alterados: 0").
  O mapa detalhado da Etapa 0 não estava salvo; foi reconstruído pelo Search Console (linha de base).
- Títulos de páginas com tráfego NÃO mudaram (/seo-para-clinicas-de-estetica/ 84 impr.,
  /seo-para-pequenas-empresas/ 136 impr. pos. 15, /para-comercios-locais/ 34 impr.).
- Retitulado (URL mantida): /blog/como-aparecer-google-clinica-estetica-goiania/ →
  "Como Atrair Clientes para Clínica de Estética em Goiânia" (fala com a dona). Título antigo trocado
  também no índice do blog, em 2 artigos que o linkavam e no llms.txt. Saíram a caixa de nota interna
  ("artigo satélite", "cluster") e 2 promessas de "próximo artigo" que nunca saiu.
- Estética: corrigida frase falsa ("os dois cases são de estética" — são confeitaria e orquestra);
  fontes Lei 13.643/2018 e Res. CFM 2.336/2023; público BusinessAudience; autor + data visíveis;
  FAQ "SEO x anúncio" equilibrada (o site vende anúncio); cartões de landing page e Google Ads.
- /criacao-de-site-para-clinica-de-estetica/: FAQ sem "em Goiânia", autor/data, público, relacionados
  com checklist e landing page (via `servicos_nichos.py`; regerar mexe em 4 outras páginas só na ficha
  da empresa — revertidas por estar fora do escopo).
- Pequenas empresas: seção nova "SEO, anúncio no Google ou landing page: por onde a pequena empresa
  começa?" (4 serviços), fonte oficial do Google sobre ranking local, tabela de equilíbrio sem valor
  de investimento ("cada R$ 1.000"), card "refém do boleto" reescrito, botão duplicado de WhatsApp
  virou "Ver os pacotes", autor/data e público.
- CSS: `.cluster-grid-4` (1 / 2x2 / 4 colunas), só nos 2 blocos novos; `styles.min.css` regerado.
- Conferido: JSON-LD válido, títulos 48–63 e descrições 127–153 sem duplicar, lychee 0 erros,
  conferidor só com os 3 avisos antigos, celular 390 px e computador 1366 px sem estouro.

## Etapa 8 — o que foi feito (prévia local, 05/10/2026)
- Linha de base: /para-advogados/ tinha 60 impressões (buscas "seo para advogados", posição 48–56) e o link
  do menu em 168 páginas; /marketing-para-advogados/ tinha 0 impressão e 2 links. Nenhum artigo de advocacia.
- /marketing-para-advogados/ refeita como principal em `servicos_marketing.py` ("Marketing e SEO para
  Advogados nas Normas da OAB" — "SEO" no title/H1/H2 para herdar as buscas da página antiga).
  /para-advogados/ apagada, com 301 no `_redirects` (e /para-advogados.html aponta direto para a nova).
- Fonte: texto oficial do Provimento 205/2021 e Anexo Único no site da OAB (lido em 05/10/2026). Pontos usados:
  art. 1º (marketing permitido), art. 2º II/VI/VII/VIII, art. 3º I–V, art. 4º §1º e §5º, art. 5º, art. 6º;
  Anexo: Google Ads permitido "quando responsivo a uma busca iniciada pelo potencial cliente", impulsionamento
  sem oferta de serviço, mala direta vedada, chatbot permitido. Página e artigos dizem que o Renan é bacharel
  em Direito, NÃO advogado.
- NÃO trazidos da página antiga (sem como confirmar): "exclusividade por área do direito e região", "você
  assina ciente das regras e tem documentação de respaldo", "apresentação com dados do mercado de advocacia".
- Artigos novos: /blog/como-conseguir-clientes-na-advocacia/ (1.206 palavras) e
  /blog/advogado-pode-fazer-marketing/ (1.138). Índice do blog (categoria "Advocacia"), sitemap 168 → 169,
  llms.txt (seção "## Advocacia").
- Site e tráfego para advogados ligados à principal e aos artigos; FAQ do site sem "em Goiânia".
- `scripts/etapa8-advocacia-2026-10-05.py` trocou href="/para-advogados/" em 177 arquivos (menu, rodapés,
  textos e os geradores rcb_base/rcb_menu/gerar-paginas-cidades). Página protegida /consultor-seo-goiania/:
  só os 3 links "Advogados" mudaram de endereço.
- Conferido: fichas válidas, títulos 48–63, descrições 149–159, sem duplicados, semelhança máx. 16,4%,
  lychee 0 erros, conferidor com os 3 avisos antigos, celular 390 px sem estouro.
- Depois de publicar: conferir no ar que /para-advogados/ responde 301 para a nova.

- Decisão do Renan (05/10/2026): manter "graduado em Gestão de TI pela FIAP" no site (está se formando).
  Não perguntar de novo.

## Etapa 9a — o que foi feito (prévia local, 05/10/2026)
- Página nova `/marketing-para-empresa-de-higienizacao-de-estofados/` (servicos_marketing.py) e artigo
  `/blog/como-conseguir-clientes-para-higienizacao-de-estofados/` (artigos_nichos_anuncios.py, 1.220 palavras).
  Ângulos: decisão rápida (orçamento por foto no WhatsApp), antes e depois organizado e com autorização,
  não prometer "remove 100% das manchas" (CDC art. 37), produtos saneantes (Lei 6.360/1976 + página da Anvisa),
  área de atendimento no Google Meu Negócio, clientes empresariais (hotel, clínica, aluguel por temporada),
  cliente que volta (lembrete com LGPD), Google Ads com bloqueio de buscas de curso/máquina/emprego.
- **Sem número de CNPJ de propósito:** a API de CNAE do IBGE (conferida em 05/10/2026) não tem código próprio
  para estofados; o mais próximo descrito é o 9601-7/01 (lavagem de tapetes, carpetes e cortinas "inclusive na
  residência do cliente"). Contar as empresas desse código seria contar lavanderias — por isso não há número.
- Índice do blog (categoria "Higienização de estofados"), sitemap 169 → 171, llms.txt (seção nova).
- O gerador mexeu na ficha da empresa de 3 páginas fora do escopo (loja virtual, site para contador, site para
  dentista): revertidas com git.
- Conferido: títulos 50 e 54, descrições 158 e 134, 1 H1, fichas válidas (Service + BusinessAudience + FAQPage;
  BlogPosting + BreadcrumbList + FAQPage), sem R$, semelhança máx. 14,1% (× limpeza), lychee interno 0 erros,
  conferidor só com os 3 avisos antigos, celular 390 px sem estouro.

## Decisões anteriores (04/10/2026)
- Marca oficial "RCB SEO"; dados só em `data/marca.json`.
- 168 cidades noindex excluídas; ficam as 31 indexáveis.
- Perfil do Google não será renomeado agora — não lembrar de novo.
- Fidelidade (decisão do Renan, 04/10/2026, vale para todos os serviços): "Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições vão por escrito junto com o orçamento." Script `scripts/fidelidade-2026-10-04.py`. Nunca mais escrever "compromisso de 3 meses" ou "fidelidade mínima".
- Etapa 5: o Renan NÃO faz gravação nem edição de vídeo — o serviço é só a parte de ser encontrado (tema, título, descrição, capítulos, transcrição, miniatura). Nunca sugerir produção de vídeo. Vídeo e IA: usar a versão segura ("dependem muito do texto que acompanha o vídeo").
- Etapa 4: número de CNPJ do CNAE 4321-5/00 aprovado (com a ressalva de que inclui eletricistas); sazonalidade aprovada como observação ("costuma"/"tende a"), nunca como dado medido.
- Etapa 3: regra do COFECI em imobiliárias aprovada; frase "bacharel em Direito" em advogados aprovada.
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

