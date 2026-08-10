# site-consultoria (rcbseo.com.br)

Site estático (HTML puro, sem framework) da consultoria de SEO local do Renan Carvalho Barbosa, publicado no **Cloudflare Pages** (deploy automático a cada `git push origin main`, sem workflow do GitHub Actions). Domínio: rcbseo.com.br. Repo GitHub: renancbarbosa/site-consultoria, branch `main`, remote `origin` (URL SSH usa o alias de host `github-renan` — o push é `git push origin main`).

## Contexto do negócio

- Renan é consultor de SEO local e Google Meu Negócio, marca RCB Consultoria, baseado em Goiânia/GO. Não é programador.
- Site lançado em 26/04/2026 (domínio novo — SEO orgânico leva meses para maturar).
- Também existe um segundo projeto irmão: `C:/Users/renan/SITE-DADOS` (Radar de CNPJ, Astro, dados públicos de CNPJ por cidade — 2000+ páginas, ~metade indexada pelo Google). Serviu de fonte de dados para as páginas de cidade deste projeto.

## Decisão estratégica de 15/07/2026: reposicionamento nacional

Motivo: Search Console (3 meses) mostrou 1.470 impressões, 8 cliques, **posição média 38,9** (página 4). As consultas que geram impressão são quase todas nacionais e em linguagem leiga de dor ("como aparecer no google maps", "seo para pequenas empresas"), não "SEO Goiânia". Conclusão: o site estava travado num raio geográfico pequeno demais e falava a língua técnica errada para o público (leigo, com dor, não SEO/dev).

**Decisão confirmada com o Renan:** Google Meu Negócio (perfil no Maps) **continua 100% local em Goiânia** — mudar para "Brasil" tiraria o perfil do mapa local sem ganhar mapa nenhum em outro lugar. Só o *site* (conteúdo orgânico) foi nacionalizado.

### O que foi feito (commit d0b6222, publicado e no ar)

1. **7 páginas nacionalizadas** (title/meta/OG/Twitter/H1/schema sem "em Goiânia", mantendo "online Brasil, presencial Goiânia"):
   - seo-para-dentistas, seo-para-medicos, seo-para-clinicas-de-estetica, seo-para-clinicas-de-emagrecimento, google-meu-negocio-para-clinicas, site-para-clinica, **consultoria-seo-local** (esta virou a página nacional do serviço — resolve canibalização com as duas páginas de Goiânia que continuam locais: `/consultor-seo-goiania/` = o profissional, `/seo-local-goiania/` = o serviço em Goiânia).
2. **199 páginas de cidade + 1 hub** em `/consultoria-seo/<slug>/` e `/consultoria-seo/`, geradas por `scripts/gerar-paginas-cidades.py`. Fonte de dados: `C:/Users/renan/SITE-DADOS/data/cidades/*.json` (CNPJ público: empresas ativas, aberturas 90d/12m/mês, ramos que mais crescem, bairros). Goiânia é **pulada de propósito** no script (já tem páginas próprias — evita concorrência interna).
   - Para regenerar após o SITE-DADOS atualizar os dados: `python scripts/gerar-paginas-cidades.py` (idempotente, sobrescreve).
3. **2 páginas em linguagem 100% leiga** (a pedido explícito do Renan — "não vendo para SEO, vendo para quem tem a dor"): `/marketing-para-clinicas/` e `/como-atrair-mais-pacientes/`.
4. Sitemap.xml: 88 → 290 URLs. Links internos adicionados na home (seção "local-section" e footer) e nos rodapés das páginas novas.

### Pendências / próximos passos combinados

- **Autoridade / backlinks** (trabalho manual do Renan, não código): diretórios locais (GuiaMais, Apontador, TeleListas, Solutudo, ACIEG/CDL), LinkedIn (perfil + página de empresa), transformar cases (Nalu Prado, Docevidade) em posts marcando clientes, guest posts em portais de Goiás, HARO/EnvieMe.
- **Revisão em ~60–90 dias** (por volta de meados de setembro/2026): checar Search Console para ver se as páginas de cidade estão indexando e gerando impressão. Se sim → fase 2 (mais cidades, script já pronto). Padrão de referência: o SITE-DADOS indexou só ~metade das páginas geradas de uma vez; aqui foram geradas 199 de uma vez também, então espera-se indexação parcial gradual, não imediata.
- Renan pediu para publicar tudo direto (sem pedir OK página por página) nesta rodada — já autorizado e publicado.

## Rodada de 18/07/2026: checklist de SEO + correções em massa (publicada — commit 35b313f)

Auditoria feita contra checklist externo (@danielsocrates.seo) + intenção de busca. Executado:

1. **Títulos ≤65 e descrições ≤160** em todo o site (84 títulos e 250 descrições encurtados; cidades corrigidas no script gerador e regeneradas).
2. **Imagem social nova** `assets/img/og-rcb-1200x628.png` (gerada por HTML+screenshot) aplicada como og:image/twitter:image em todas as páginas que usavam o logo 600×120; schema BlogPosting dos posts também atualizado.
3. **Endereço físico adicionado** (decisão do Renan: residencial — Rua 18-A, nº 256, Goiânia - GO, CEP 74070-060): schema PostalAddress (streetAddress/postalCode), rodapé de todas as páginas, llms.txt e página de contato com **mapa do Google incorporado** (iframe embed).
4. **Links externos de autoridade** nas páginas de nicho: OAB Provimento 205/2021, CFM 2.314/2022 e 1.974/2011, CFO códigos, CFP código de ética, CFMV, ANVISA.
5. **8 artigos de apoio novos** (2 por nicho novo): contadores (como-conseguir-clientes-de-contabilidade, marketing-para-escritorio-de-contabilidade), psicólogos (psicologo-pode-anunciar-no-google, como-conseguir-pacientes-de-psicologia), veterinários (como-atrair-clientes-clinica-veterinaria, pet-shop-como-aparecer-no-google), imobiliárias (como-gerar-leads-imobiliaria-sem-portais, google-meu-negocio-para-corretor-de-imoveis). Integrados: índice do blog, sitemap (305 URLs), bloco "Leia também" nas 4 páginas de nicho.
6. **10 capas ilustradas** nos artigos estratégicos do blog: Renan gerou com os prompts entregues, Claude converteu (JPEG 1200×675, 48–81 KB, nome = slug do artigo em `assets/img/blog/`), inseriu no lugar do `.artigo-capa-placeholder` com alt descritivo, og:image própria por artigo, schema e dateModified atualizados.
7. Pendente: trabalho off-page (diretórios, LinkedIn, posts de cases) segue como maior prioridade — posição média 38,9.

Renan confirmou: Bing Webmaster Tools feito, sitemap reenviado no Search Console.

## Passos manuais que o Renan precisa fazer no Search Console (ainda pendente, ele mesmo faz)

1. Sitemaps → reenviar `sitemap.xml`.
2. Inspeção de URL → solicitar indexação manual para `/consultoria-seo/`, `/marketing-para-clinicas/`, `/como-atrair-mais-pacientes/` (as 199 cidades o Google descobre sozinho via hub + sitemap).

## Rodada de 23/07/2026: Bing Webmaster Tools + IndexNow

- Confirmado que o site roda no **Cloudflare Pages**, não GitHub Pages (corrigido acima) — descoberto pelos headers do servidor (`Server: cloudflare`) e pelos arquivos `_headers`/`_redirects` na raiz (convenção do Cloudflare Pages).
- Verificação do Bing: não há `BingSiteAuth.xml`, meta tag nem TXT no DNS, mas o sitemap já era aceito no Bing — indicando verificação feita por outro caminho (provável importação automática via Google Search Console, que não deixa rastro no site). Nada a fazer aqui.
- **IndexNow configurado** (commit 2fa53f6): chave `19341b29c6054af601879d85a34d62c5` publicada em `/19341b29c6054af601879d85a34d62c5.txt` na raiz. POST enviado ao Bing com as 305 URLs do sitemap — aceito (HTTP 200). Reutilizar essa mesma chave em envios futuros de IndexNow, não gerar uma nova.
- Existe um arquivo antigo não identificado na raiz, `2f4b7f42-ccc9-4f5d-9e72-9a208bdebcc7.txt` (formato UUID com hífens, não é hex puro — não serve como chave IndexNow). Origem desconhecida, não mexer sem investigar antes.
- Cloudflare "Crawler Hints" (Caching → Configuration): já estava ligado.
- Cloudflare "AI Crawl Control" → **"Managed robots.txt": decidido manter DESLIGADO.** Esse botão faria o Cloudflare reescrever o `robots.txt` para bloquear crawlers de IA — mas o `robots.txt` atual permite de propósito GPTBot, ClaudeBot, Google-Extended, PerplexityBot, Applebot-Extended e CCBot (estratégia de visibilidade em IA/GEO). Ligar esse botão entraria em conflito direto com isso.

## Rodada de 06/08/2026: nova divisão "SEO Nacional / mercados competitivos" (publicada — commit 1e2949e)

Segunda frente do site, independente do SEO local e sem canibalizá-lo. **63 URLs novas** (23 páginas
comerciais + 40 artigos). Plano completo e matriz de canibalização: `docs/seo-mercados-competitivos-plan.md`
(documento interno, fora do sitemap).

### Arquitetura de geração (importante)
O conteúdo novo é gerado por script, no mesmo espírito de `gerar-paginas-cidades.py`. **O texto de cada
página é único e escrito à mão dentro dos módulos** — o script só cuida do invólucro.

- `scripts/rcb_base.py` — head, navbar, rodapé, schema e blocos de seção. **Fonte única do navbar e da
  coluna "SEO Nacional" do rodapé.** Mexeu aqui? Rode `atualizar-nav-rodape.py` depois.
- `scripts/rcb_artigo.py` — renderizador dos artigos do blog.
- `scripts/conteudo/cluster_*.py` — conteúdo das páginas comerciais (central, iptv, bets, dominios).
- `scripts/conteudo/artigos_*.py` — conteúdo dos artigos.
- `scripts/gerar-paginas-competitivas.py` / `gerar-artigos-competitivos.py` — executores (idempotentes).
- `scripts/atualizar-nav-rodape.py` — propaga navbar/rodapé para as 328 páginas com navbar.
- `scripts/atualizar-blog-index.py` — insere os 2 agrupamentos novos no índice do blog (usa marcadores
  HTML `<!-- RCB:CLUSTERS-NACIONAIS:... -->`, então pode rodar de novo sem duplicar).
- `scripts/atualizar-sitemap.py`, `scripts/links-internos-divisao.py`, **`scripts/validar-site.py`**.

`validar-site.py` é o script de conferência geral do site (links quebrados, metadados duplicados,
órfãs, sitemap) — vale rodar antes de qualquer publicação daqui em diante.

### Política editorial da divisão — inegociável
Está detalhada no §2 do plano. Os pontos que não podem ser afrouxados:
1. **Nunca prometer** primeira página/posição/prazo garantidos, backlinks ilimitados, ou que domínio
   expirado transmite autoridade / que migração preserva posições.
2. **Black hat e PBN** aparecem só em posição explicativa. Não são serviço, não há tutorial operacional.
3. **Cluster IPTV**: no Brasil essa busca mistura operação licenciada com distribuição irregular. Toda
   página do cluster declara que a RCB atende quem tem direito/autorização sobre o conteúdo, verificado
   na análise do projeto. **`/migracao-de-dominio-para-iptv/` não foi criada de propósito** — o recorte
   "IPTV + trocar domínio" atrai demanda de evasão de bloqueio judicial, que não é atendida.
4. **Cluster bets**: linguagem neutra quanto à regulação, sem conclusão jurídica, sem apelo ao jogo.

### Duas coisas que mudaram no site inteiro
- **Navbar**: entrou o dropdown "SEO Nacional" (8 itens). Para abrir espaço, o link de topo
  "Consultor SEO" **foi movido** para dentro do dropdown "Serviços" (não removido).
- **Rodapé**: entrou a coluna "SEO Nacional". Atenção: a home usa um rodapé próprio
  (`.site-footer` / `.footer-grid`), diferente do resto do site (`.footer` / `.footer-cols`) — os dois
  foram atualizados, e os dois grids do CSS passaram de 4 para 5 colunas.
- **CSS dos artigos**: as regras `.artigo-*` estavam duplicadas em `<style>` inline dentro de cada
  artigo (4,4 KB por arquivo, 13 variantes). Foram consolidadas no `styles.css`. Os artigos antigos
  mantêm o inline (que vence por vir depois) — o visual deles não mudou; os novos não repetem o bloco.

### Publicação (07/08/2026)
- Commit `1e2949e` enviado para `origin main`; Cloudflare Pages publicou automaticamente.
  As 63 URLs foram conferidas no ar (HTTP 200) antes do passo seguinte.
- **IndexNow enviado ao Bing com as 63 URLs novas — aceito (HTTP 200).** Reutilizada a chave
  `19341b29c6054af601879d85a34d62c5`, a mesma de 23/07/2026. **Nunca gerar chave nova.**
- Automatizado em `scripts/indexnow.py`: `--novas` (URLs da divisão), `--sitemap` (tudo) ou URLs
  avulsas. Regra: só enviar depois de confirmar HTTP 200, senão o Bing rastreia e acha 404.

### Pendências desta rodada
- **Falta o Renan fazer no Search Console:** reenviar o `sitemap.xml` (agora com 378 URLs) e pedir
  indexação manual de `/seo-para-mercados-competitivos/`, `/seo-para-iptv/`, `/seo-para-bets/` e
  `/analise-de-projeto/`. Os artigos o Google descobre pelo índice do blog + sitemap.
- **Backlog zerado em 07/08/2026:** os 10 artigos restantes foram produzidos (módulos `*_lote2.py`),
  fechando os 50 planejados (~39.400 palavras). O ângulo que diferencia cada um do conteúdo já
  existente está no cabeçalho dos módulos e no §5.1 do plano.
- `scripts/ligar-artigos-lote2.py` inseriu 19 links do restante do site para os artigos novos —
  editando os **módulos de conteúdo**, para sobreviverem a regeração. Depois de rodá-lo, é preciso
  regerar páginas e artigos.
- Achados pré-existentes, não corrigidos por serem fora do escopo desta rodada:
  `/consultoria-seo/palmas/` é página órfã (nenhum link aponta para ela — provável resíduo de colisão
  de slug do gerador de cidades), e 20 páginas antigas têm meta description entre 161 e 170 caracteres.

## Rodada de 08/08/2026: divisão competitiva REVERTIDA (fora do ar)

**Estado atual do site: a divisão "SEO Nacional / mercados competitivos" NÃO está publicada.**
A seção acima (06/08) descreve o que foi feito, mas o resultado foi retirado do ar um dia depois.

- Motivo: decisão do Renan — reavaliar se IPTV, bets e domínios expirados combinam com o
  posicionamento da marca RCB. Não foi problema técnico nem de SEO.
- Como foi feito: `git revert` dos commits `1e2949e`, `9e106e4` e `2507c42` (commit `122735d`).
  O HTML voltou byte a byte ao estado de `980fe74`. Sitemap de volta a **305 URLs**, navbar sem o
  dropdown "SEO Nacional", rodapé sem a coluna nova, `styles.css` sem o grid de 5 colunas.
- **Preservados de propósito:** `scripts/` (incluindo `rcb_base.py`, `rcb_artigo.py`,
  `conteudo/*.py`, os geradores, `indexnow.py`, `validar-site.py`) e
  `docs/seo-mercados-competitivos-plan.md`. Não são páginas públicas, não têm link e não estão no
  sitemap — guardam todo o texto das 73 URLs.
- **Backup congelado:** branch `divisao-seo-nacional` no GitHub, apontando para `2507c42`.
- **Para republicar tudo:** `git revert 122735d` (ou `git merge divisao-seo-nacional`), conferir
  HTTP 200 e só então rodar `python scripts/indexnow.py --novas`.
- As 73 URLs agora respondem 404 de propósito. Não criar redirect 301 delas para a home nem 410 —
  a decisão pode ser revista.
- Search Console: o Renan precisa reenviar o `sitemap.xml` (305 URLs). Nada a pedir de remoção;
  o Google tira as 404 sozinho em algumas semanas.
- Atenção ao `scripts/validar-site.py` daqui em diante: ele foi escrito para o site com a divisão.
  Rodar sobre o site revertido pode acusar como quebrado o que na verdade foi removido de propósito.
- IndexNow: enviadas ao Bing as 69 URLs já confirmadas em 404 — aceito (HTTP 200), mesma chave.

### Armadilha descoberta em 08/08/2026: branch novo = deployment de preview no Cloudflare Pages
Ao criar o branch de backup `divisao-seo-nacional` (apontando para `2507c42`), o Cloudflare Pages
gerou automaticamente um **deployment de preview** dele. Quatro URLs removidas
(`/seo-para-iptv/`, `/seo-para-bets/`, `/analise-de-projeto/`,
`/blog/backlinks-para-iptv-funcionam/`) continuaram respondendo **HTTP 200 no domínio de produção**,
servindo o build pré-reversão.

Como reconhecer: a resposta traz `x-robots-tag: noindex` (marca de preview do Pages),
`Cache-Control: public, s-maxage=604800` e um `Age` que **cresce e nunca zera**. As páginas
corretas retornam `404` com `Cache-Control: no-store`, sem `noindex`.

O que NÃO resolve: "Purge Everything", "Purge by URL", commit vazio, novo deployment de produção,
`Cache-Control: no-cache` no pedido. Nenhum deles zera o `Age`. "Always Online" foi descartado
(sempre esteve desligado).

O deployment de preview foi apagado no painel (Workers & Pages → projeto → Deployments → linha com
etiqueta "Preview" → Delete). Isso mata a origem — o preview `0724c7c2.site-consultoria-59m.pages.dev`
passou a dar 404 — **mas não solta a cópia já grudada no roteamento do domínio**: mesmo depois disso,
um novo "Purge by URL" não zerou o `Age`. Ou seja, apagar o branch e apagar o deployment são passos
necessários, e ainda assim nenhum purge alcança o objeto.

Desfecho: decidido **deixar expirar sozinho** (s-maxage de 7 dias a partir de ~08/08/2026 08:20 —
vence por volta de **15/08/2026**). Impacto aceito como nulo por causa do `noindex`. As 4 URLs
**ainda não foram enviadas ao IndexNow** — mandar agora faria o Bing encontrar 200. Enviar depois
de 15/08, conferindo antes que respondem 404.

Nome real do projeto no Cloudflare Pages: **`site-consultoria-59m`** (produção em
`site-consultoria-59m.pages.dev`). Útil para conferir se um problema é da produção ou do domínio:
durante todo esse episódio a produção já respondia 404 corretamente.

Risco de SEO: baixo, porque o preview sai com `noindex`. Mas evite criar branches remotos neste
repositório só para backup: o histórico do `main` já preserva tudo (`2507c42` continua alcançável),
e há a tag local `divisao-competitiva-backup`.

## Rodada de 08/08/2026: auditoria semântica — termo de busca no início (publicada — commit 176b11b)

Auditoria das 307 páginas cruzando cada uma com o termo de busca que ela deveria disputar, checando
se o termo aparece — **e se aparece no começo** — em title, meta description, H1, H2 e primeiro
parágrafo. Pedido do Renan: "o termo tem que estar em tudo, sempre no início".

### Achado principal
As **199 páginas de cidade estavam 100% corretas** (o gerador já embute a regra) e não foram tocadas.
O problema estava só no conteúdo escrito à mão: **101 das 108 páginas restantes** falhavam em algo.
A falha sistemática era o **primeiro H2 do DOM**, que em quase toda página é o rótulo do painel
`<aside class="page-hero-panel">` — "Em uma frase", "O que a estratégia cobre", "Dores comuns",
"O que inclui", "Problemas comuns". O Google lê esse H2 como o 2º sinal mais forte depois do H1.

### O que foi aplicado (98 arquivos, 298 linhas — só texto, nenhuma URL mudou)
- 74 primeiros H2 passaram a carregar o termo.
- 63 H2 de FAQ: `Perguntas frequentes` → `Perguntas frequentes sobre <termo>`. Ganho duplo (termo em
  H2 + elegibilidade para o bloco de perguntas na SERP).
- 47 meta descriptions reescritas: termo na frente e **todas dentro de 160 caracteres**.
- 30 aberturas de texto com o termo na primeira frase; 7 H1 e 4 titles realinhados; 9 H2 extras.

### Decisões editoriais — não afrouxar sem motivo
1. **Listas numeradas**: em artigos cujo 1º H2 é "1. Site no ar", "2. Google Perfil" etc., o termo
   **não** foi enfiado no item 1 (fica artificial e lê como forçação). Nesses, o termo entrou no H2
   do FAQ e num H2 de fechamento. Sobraram 29 páginas assim, de propósito.
2. **Aberturas com gancho editorial** (15 páginas): narrativa (`/blog/como-aparecer-google-clinica-estetica-goiania/`
   abre com uma cena) ou resposta direta (`/blog/quanto-tempo-leva-seo-local-clinicas/` abre com
   "entre 3 e 6 meses" — formato que ganha o quadro de resposta). Mantidas como estão.
3. Em `/para-advogados/`, `/para-comercios-locais/` e `/para-profissionais-liberais/` o subtítulo do
   hero **voltou ao original**: o H1 já abre com o termo e repetir a mesma frase na linha de baixo é
   repetição excessiva.

### Canibalização resolvida
`/blog/seo-para-contadores/` disputava o **termo exato** de `/seo-para-contadores/` (página de venda).
O artigo foi realinhado para **"Como o escritório de contabilidade aparece no Google"** — title, H1,
description, og/twitter, schema, cartão no índice do blog, `guia-seo-local` e `llms.txt`. **A URL não
mudou** (já indexada). A página comercial ficou dona sozinha do termo.

### Medido antes → depois (fora as cidades)
| | antes | depois |
|---|---|---|
| páginas sem nenhum H2 com o tema | 56 | **0** |
| aberturas sem o tema | 42 | **15** (propositais) |
| primeiros H2 sem o tema | 88 | **29** (listas numeradas) |
| descriptions acima de 160 caracteres | 21 | **0** |

### Publicação
- Commit `176b11b` → `origin main`; Cloudflare publicou (~1 min). As **97 URLs conferidas: HTTP 200**,
  e conferido por amostragem que é o HTML novo no ar (não cache antigo).
- **IndexNow enviado ao Bing com as 97 URLs — aceito (HTTP 200).** Mesma chave
  `19341b29c6054af601879d85a34d62c5`. **Nunca gerar chave nova.**
- Falta o Renan reenviar o `sitemap.xml` no Search Console (305 URLs, nenhuma URL nova nesta rodada).

### Notas
- `/diagnostico-presenca-digital/exemplo/` não tem H1 nem description **de propósito**: é `noindex,
  nofollow`, fora do sitemap, e é uma demo em JS do relatório de diagnóstico. Não tratar como erro.
- Cuidado ao trocar títulos por script: substituir a "base" do title no arquivo inteiro pode atingir
  H1/H2 que contêm o mesmo texto como prefixo. Aconteceu em
  `/blog/como-aparecer-google-clinica-estetica-goiania/` e foi corrigido. Sempre conferir o `git diff`.
- Regex de meta description **para no primeiro apóstrofo** se o padrão for `content=["\'](.*?)["\']`
  e o texto contiver `'`. Quebrou a description de `/cases/` e foi corrigido.
- **Prioridade nº 1 continua sendo off-page** (backlinks, diretórios, LinkedIn, posts de case).
  Posição média 38,9 — organização semântica sozinha não resolve isso.

## Rodada de 09/08/2026: refatoração de conversão — preço público e venda por WhatsApp/Pix

Mudança de modelo comercial, não de SEO. Pedido do Renan: o site nunca gerou procura, e o
diagnóstico era o problema — falava a língua errada (SEO/técnica) e não tinha preço, então
ninguém chegava ao WhatsApp. **O site passou a ter tabela de preço pública.**

### A oferta (fonte única: `scripts/rcb_pacotes.py`)
- **Presença — R$ 997, pagamento único.** Site até 5 páginas, GMN configurado, 10 fotos,
  avaliações. Entrega em 7 dias úteis.
- **Crescimento — R$ 1.497/mês, mínimo 3 meses.** Presença + 2 textos/mês + gestão de
  avaliações + relatório mensal + ajustes.
- **Dominação — R$ 2.497/mês, mínimo 3 meses.** Crescimento + 4 textos/mês + página por
  serviço + 3 concorrentes monitorados + prioridade.
- **Garantia de 30 dias**: sem diferença notada na presença no Google, refaz sem custo.
- Pagamento por **Pix combinado no WhatsApp**. Não há gateway. Não incluir Instagram, redes
  sociais nem automação nos pacotes — são produto separado.

**Mexeu em preço ou no que cada pacote inclui? Edite só `scripts/rcb_pacotes.py` e rode
`python scripts/aplicar-conversao.py` + `python scripts/gerar-paginas-cidades.py`.** Editar o
HTML de uma cidade à mão não adianta: a regeração sobrescreve.

### O que mudou no site inteiro
- **232 páginas com a tabela de preço** (comerciais, de nicho, de serviço, as 199 cidades, o
  hub e o artigo `/blog/quanto-custa-consultoria-seo-local/`). Blog e institucionais não
  repetem a tabela — o menu e a barra deles apontam para `/#pacotes`.
- **303 páginas com barra fixa de CTA no celular** (`.cta-mobile`: "Ver preços" + "Falar no
  WhatsApp"). Ela exige `class="tem-cta-mobile"` no `<body>`; o botão flutuante do WhatsApp
  é escondido no celular por CSS para não brigar com ela.
- **Menu: "Diagnóstico gratuito" → "Ver preços"** nas 303 páginas com navbar.
- **Home reescrita do zero**: H1 de dor, 4 nichos só (clínicas, dentistas, estética,
  comércios), 3 passos, garantia, FAQ leigo e formulário → WhatsApp. Saíram da copy: SEO,
  schema, cluster, on-page, "9+ anos como empresário", automação e os nichos que pagam menos
  (as páginas deles continuam no ar e linkadas pelo rodapé).
- **Formulário da home** (`#rcbLeadForm`): grava o lead no Web3Forms e abre o WhatsApp com a
  mensagem pronta. **Reutiliza a chave do Radar de CNPJ** (`b9f6b538-d4a7-4e5a-8ee9-5f8310832733`),
  decisão do Renan — os leads caem no mesmo e-mail, diferenciados pelo assunto
  "Novo lead — RCB Consultoria (site)". Se o Web3Forms falhar, o botão do WhatsApp é liberado
  mesmo assim: a conversa não pode ser perdida por causa do registro.
- **Diagnóstico gratuito continua existindo**, mas virou passo 2 do funil: 53 botões dourados
  foram rebaixados para contorno. Só `/diagnostico-presenca-digital/` mantém o seu como principal.
- **`llms.txt` ganhou seção de preços** — é o que ChatGPT/Claude/Perplexity leem.
- Schema: `Offer` com os três preços dentro do nó `Service`. Onde não havia `Service`, o
  script cria um. Pode fazer o preço aparecer direto no resultado do Google.

### Scripts desta rodada
- `scripts/rcb_pacotes.py` — **fonte única do preço.** Não duplicar em outro lugar.
- `scripts/aplicar-conversao.py` — aplica em todas as páginas escritas à mão. Idempotente
  (marcadores `<!-- RCB:PACOTES:INICIO -->` e `<!-- RCB:CTA-MOBILE -->`).
  Aceita `--so-comerciais` / `--so-apoio`.
- `scripts/conferir-conversao.py` — **rodar antes de qualquer publicação daqui em diante.**
  Checa HTML balanceado, JSON-LD, links, âncoras, coerência de preço texto×schema, jargão e
  frases que contradizem o preço. Diferente do `validar-site.py`, que foi escrito para a
  divisão competitiva revertida e acusa falso positivo neste site.
- `scripts/gerar-paginas-cidades.py` — agora importa o `rcb_pacotes` e embute preço + barra
  nas cidades **e no hub**. Cuidado: `pagina_cidade()` e `pagina_hub()` são funções separadas;
  mexer só numa deixa a outra para trás (aconteceu nesta rodada).

### Armadilhas encontradas
- **`/para-comercios-locais/` tinha o `/script.js` morto** desde sempre: o script inline da
  página declarava `navbar`, `navToggle`, `navMenu`, `toggleMenu` e `fadeObserver` no escopo
  global, colidindo com o `script.js` e derrubando-o inteiro com SyntaxError. **Nenhum clique
  era medido no GA4 nessa página.** Corrigido: o inline ficou só com o que é exclusivo dela
  (observador das classes próprias e o acordeão `.faq-question`, que o resto do site não usa),
  dentro de uma IIFE. Ao mexer em página com script inline, conferir colisão de nomes.
- **Regerar as cidades desfaz alteração manual.** O `aplicar-conversao.py` rodou nelas e
  depois a regeração sobrescreveu — só não deu problema porque o gerador já tinha sido
  ensinado. Ordem correta: ensinar o gerador → regerar.
- `/consultoria-seo/palmas/` continua órfã e **não é produzida pelo gerador** (198 geradas,
  199 no disco). Ela recebe as mudanças pelo `aplicar-conversao.py`, não pela regeração.
- `diagnostico-presenca-digital/exemplo/` monta o HTML por JavaScript: contar tag aberta e
  fechada nela não faz sentido. Está na lista `FORA_DA_CONFERENCIA` do conferidor.
- Heredoc no Bash (`<< 'EOF'`) quebrou várias vezes com aspas e CSS. Para script com muito
  texto, escrever o `.py` num arquivo e rodar — não colar no terminal.

### Decisões editoriais — não afrouxar sem falar com o Renan
1. **O termo "SEO para X" ficou nos títulos e H1 das páginas de nicho.** O endereço da página
   é `/seo-para-dentistas/` e a rodada de 08/08 colocou o termo no início de propósito. O
   jargão saiu do *corpo* do texto; o título continua servindo à busca. O H1 virou pergunta
   na língua do cliente ("...seu consultório aparece no Google quando o paciente procura
   implante?").
2. **Instagram e os nichos secundários continuam no rodapé** das 300 páginas, apesar do
   pedido de tirar da home. Motivo: o rodapé é igual no site inteiro (mexer só na home cria
   divergência) e o link do Instagram é sinal de NAP para o perfil local. Fácil de reverter.
3. Título da home ficou com **70 caracteres** (texto exato pedido pelo Renan). O Google corta
   por volta de 65 — ele foi avisado e manteve.

### Publicação (09/08/2026)
- Commit `3fdddb0` enviado para `origin main`; Cloudflare publicou em ~1 min (313 arquivos,
  24.313 linhas). Conferidas no ar: home, as 4 páginas de nicho, médicos, hub de cidades,
  duas cidades, dois artigos, contato e cases — todas HTTP 200 com preço, barra e menu novo.
- **IndexNow enviado ao Bing com as 305 URLs do sitemap — aceito (HTTP 200).** Mesma chave
  `19341b29c6054af601879d85a34d62c5`. **Nunca gerar chave nova.** Foram todas as URLs porque
  o conteúdo mudou em praticamente todas, mesmo sem endereço novo.
- `.github/` continua fora do versionamento — não faz parte desta rodada.

### Pendências
- Falta o Renan reenviar o `sitemap.xml` no Search Console (**305 URLs, nenhuma nova** —
  nenhum endereço foi criado ou removido nesta rodada).
- **Off-page continua sendo a prioridade nº 1.** Posição média 38,9: a home nova converte
  melhor quem chega, mas chega pouca gente. Backlinks, diretórios, LinkedIn e posts de case
  são o que enche o funil — trabalho manual do Renan.

## Rodada de 09/08/2026 (2a leva): auditoria de conversao e correcao dos defeitos de montagem

Auditoria completa da home (copy, funil, conversao, preco, SEO, performance) medida no site no ar.
Nota geral 73/100. Publicada nos commits `3a7e77b` e `b284769`.

### Os tres defeitos que ninguem tinha visto - todos na home, todos da mesma origem
A home foi reescrita a mao em 09/08 **e** continuou na lista de alvos do `aplicar-conversao.py`.
Resultado: o script injetava uma segunda copia de tudo o que a home ja tinha.

1. **Tabela de precos duplicada** - dois `id="pacotes"` na mesma pagina, com botoes que faziam
   coisas diferentes (a de cima ia para `#falar`, a de baixo abria o WhatsApp). No GA4 os dois
   disparavam o mesmo evento.
2. **Barra fixa de CTA duplicada** - a copia injetada caiu dentro de `<div class="hero-actions">`.
   Como um ancestral cria bloco de contencao, ela ignorava `bottom: 0` e aparecia **flutuando no
   meio da apresentacao** no celular, em 663 px em vez de 770 px.
3. **O aviso de cookies cobria a barra de CTA** - banner com 139 px e camada 9999 contra barra de
   74 px na camada 940, ambos no rodape. Atingia **todo visitante novo**, ou seja, todo mundo que
   vem do Google. Corrigido com `body.tem-cta-mobile .cookie-banner { bottom: 4.9rem; }` (o aviso
   empilha em cima da barra, os dois clicaveis). Conferido com teste de clique real, nao so por CSS.

### O que mais mudou na home
- H1 de 90 para 52 caracteres ("Seu cliente procura no Google e acha seu concorrente."). No celular
  caiu de 6 para 4 linhas (223 para 149 px) e o botao principal subiu de 611 px para 507 px.
- Saiu o paragrafo que repetia o subtitulo; entrou a linha da UVP (`.hero-uvp`).
- **Nova ordem do funil:** precos -> conta de retorno -> garantia -> resultados -> nichos -> como
  funciona -> local -> formulario -> FAQ -> apoio. A garantia estava 5.000 px depois do preco.
- Bloco novo **"Faz sentido pagar isso?"** (`.roi-section`) com a conta de retorno.
- Depoimentos ganharam **2 cartoes de resultado com numero** (`.resultado-card`), puxados de /cases/.
- FAQ: entraram "E caro?" e "Nao da para fazer sozinho?" (no texto e no `FAQPage`).
- `title` de 70 para 58 caracteres; preco de entrada na meta description.
- Chamada no rodape (`.footer-cta`) - **so na home**, o resto do site nao tem.

### Erro de fato no pedido, corrigido antes de publicar
O pedido mandava criar um cartao "312 avaliacoes - organizadas no perfil do cliente". **As 312
avaliacoes sao da Richesse, uma CONCORRENTE** que a Docevidade superou; a Docevidade tem 4. O
cartao publicado usa o numero verdadeiro, que e mais forte: "1o lugar no Google Maps para
'macarrons Goiania' - com 4 avaliacoes, a frente de concorrentes que tinham 47 e 312".
**Sempre conferir numero de case contra a pagina de origem antes de publicar.**

### Schema Review - com ressalva importante
Os 3 depoimentos reais foram marcados como `Review` + `AggregateRating` no no `Service`.
**Nao crie expectativa de estrelinha na busca:** desde 2019 o Google nao exibe review rich result
para avaliacao que a propria empresa publica sobre si (self-serving, `LocalBusiness`/`Organization`).
Serve para IA/GEO e para o entendimento da entidade, nao para estrela na SERP.
Os 3 depoimentos foram **mantidos visiveis** (o pedido era deixar 1): marcar review que nao esta
visivel na pagina e violacao da politica de dados estruturados.

### Mudancas nos scripts - leia antes de mexer em preco
1. **A home saiu da lista de alvos do `aplicar-conversao.py`.** Era a origem da duplicacao. A home
   tem tabela, barra e menu proprios, escritos a mao.
2. **`aplicar-conversao.py` agora ATUALIZA bloco ja existente.** Antes ele pulava toda pagina que
   ja tivesse `RCB:PACOTES:INICIO` - ou seja, **mexer no `rcb_pacotes.py` nao chegava em pagina
   nenhuma ja feita**. A instrucao que estava escrita aqui no CLAUDE.md nao funcionava de verdade.
   Agora funciona: mudou preco -> `python scripts/aplicar-conversao.py` propaga.
3. **Mas ele NAO toca em `consultoria-seo/*`.** O gerador escreve o nome da cidade dentro da
   mensagem do WhatsApp ("Tenho um negocio **em Anapolis**"); reescrever de fora apagava isso.
   Quem atualiza preco nas cidades e o `gerar-paginas-cidades.py`. **Ordem: rode os dois.**
4. **O flag `comercial` so decide quem GANHA a tabela, nao quem a mantem em dia.**
   `/blog/quanto-custa-consultoria-seo-local/` tem a tabela e nao e "comercial" - ficou sem o selo
   de garantia na primeira publicacao e foi corrigido no commit seguinte.
5. **`FECHOS`** (no `aplicar-conversao.py`): a ultima frase da linha de apoio da tabela, quando a
   pagina fala na lingua do nicho ("...que a sua clinica pode dar agora"). Saiu do HTML e virou
   dado no script - antes a regeracao apagava. Hoje sao 4 paginas.
6. `rcb_pacotes.py` ganhou `FECHO_PADRAO` e o parametro `fecho` em `bloco_pacotes()`, e passou a
   fechar os tres cartoes com `<li class="pacote-garantia">Garantia de 30 dias</li>`.

**Teste que vale sempre:** rodar `aplicar-conversao.py` duas vezes seguidas. A segunda tem que
dizer "paginas alteradas: 0". Se alterar, alguma coisa esta sendo sobrescrita.

### Efeito colateral registrado
Em 5 paginas o `data-page` do GA4 foi normalizado para bater com a URL
(`seo-dentistas` -> `seo-para-dentistas`, `blog-quanto-custa` -> `blog-quanto-custa-consultoria-seo-local`,
e semelhantes em clinicas, estetica e comercios). Muda o rotulo do evento no relatorio, nada mais.

### Publicacao (09/08/2026)
- `3a7e77b` (234 arquivos) e `b284769` (o artigo do blog) -> `origin main`. Cloudflare publicou em
  ~1 min cada. **As 232 URLs com HTML alterado foram conferidas uma a uma: todas HTTP 200.**
- **IndexNow enviado ao Bing com as 232 URLs - aceito (HTTP 200).** Mesma chave
  `19341b29c6054af601879d85a34d62c5`. **Nunca gerar chave nova.** Foram so as 232 com HTML
  alterado (nao as 305 do sitemap): as outras mudaram apenas de CSS.
- Cuidado ao conferir o site por script: **o Cloudflare devolve 403 para o user-agent padrao do
  `urllib` do Python.** Use `curl` ou mande um user-agent de navegador. Tambem da para pegar
  resposta em cache logo depois do deploy - reconferir antes de concluir que algo falhou.

### Pendencias
- **CNPJ e razao social no rodape: falta o numero.** E o unico item da auditoria nao executado.
  Nao foi colocado texto de espera no lugar - CNPJ falso no ar e pior que CNPJ nenhum.
- Chamada no rodape existe so na home; propagar para o resto do site e opcional.
- Nao foi criado pacote de entrada abaixo de R$ 997: a pesquisa de concorrentes mostrou que em
  Goiania os projetos comecam por volta de R$ 2.500/mes e quase ninguem publica preco - o R$ 997
  ja e a entrada mais barata e mais transparente do mercado local.
- **Off-page continua sendo a prioridade no 1.** A auditoria foi clara: com posicao media 38,9 e
  8 cliques em 3 meses, melhorar a conversao de quem quase nao chega nao muda o faturamento.
  Backlinks, diretorios, LinkedIn e posts de case sao o que enche o funil.

## Rodada de 10/08/2026: linha de confianca no rodape — ADICIONADA E DESFEITA no mesmo dia

**Estado atual do rodape: sem a linha, em pagina nenhuma.** O rodape esta byte a byte igual ao
que era em `f7574c2` (conferido com `git diff`). Registro aqui so para nao se refazer sem querer.

O texto era, como ultimo elemento do `<footer>`:

> Atendimento presencial em Goiania e regiao. Consultoria individual — nao e agencia.

Linha do tempo: entrou nas 305 paginas (`eec4c54`) → saiu da home por repetir informacao que o
rodape dela ja dava (`55a1609`) → saiu das outras 304 (`378e9cd`). Motivo da retirada final:
decisao do Renan. Nao foi problema tecnico — a linha funcionava e estava conferida no ar.

### O que voltou ao normal
- 305 paginas HTML, `styles.css` (regra `.rodape-confianca` removida) e os dois geradores
  (`gerar-paginas-cidades.py`, `rcb_base.py`, que tinham sido ensinados a embutir a linha).
- Nenhum vestigio de `rodape-confianca` sobrou em HTML, CSS ou script.
- **IndexNow reenviado ao Bing com as 305 URLs — aceito (HTTP 200).** Mesma chave
  `19341b29c6054af601879d85a34d62c5`. **Nunca gerar chave nova.** Nenhuma URL foi criada nem
  removida em nenhum momento desta rodada; so mudou HTML dentro delas.

### O que vale guardar, se um dia voltar o assunto
1. **A home tem `<footer>` aninhado** dentro dos cartoes de depoimento. Qualquer script que mexa
   no rodape por texto precisa mirar no **ultimo** `</footer>` do arquivo, nunca no primeiro.
2. **Nao pendurar nada dentro de `.footer-bottom-inner`**: e flex com `space-between`, entao um
   paragrafo novo vira mais uma coluna da fileira em vez de uma linha propria.
3. **O rodape do site e escuro.** `border-top: 1px solid #eee` (que veio no pedido) vira um risco
   quase branco atravessando o rodape; o tom que combina e algo como
   `rgba(255,255,255,0.06)`.
4. **No celular a barra fixa de CTA nao atrapalha** um elemento no fim do rodape: o `body` tem
   208 px de `padding-bottom`, e a linha ficava ~130 px acima da barra (conferido com clique real
   via `elementFromPoint`, nao so no olho).
5. **Ao remover por regex, cuidado com o `\s*` antes do `</footer>`**: ele engole a quebra de
   linha original e junta duas linhas que eram separadas. Aconteceu em 72 arquivos; foi visto no
   `git diff` contra o commit anterior e corrigido com `git checkout` desses arquivos.
6. `404.html` nao tem rodape nenhum, e `diagnostico-presenca-digital/exemplo/` monta o HTML por
   JavaScript — os dois ficam de fora de qualquer mexida em rodape.

### Pendente / em aberto
- CNPJ e razao social no rodape continuam faltando (item da auditoria de 09/08 ainda nao feito).
  Renan ainda nao passou o numero; **nao por CNPJ de mentira no ar**.

### Armadilha de ferramenta (nao e do projeto)
Heredoc do PowerShell (`@'...'@`) **nao funciona na ferramenta Bash** — o `@` entra literalmente
na mensagem do commit. Para commit com varias linhas no Bash, usar `git commit -F - <<'EOF'`.

## Rodada de 10/08/2026: reposicionamento de preco + Pacote Presenca Lite (publicada — commit f0d4ff7)

Mudanca comercial, nao de SEO. Nenhuma URL foi criada nem removida — **sitemap segue com 305 URLs**.

| Pacote | Antes | Agora |
|---|---|---|
| **Presenca Lite** (NOVO, 1o da fila) | — | **R$ 1.997** pagamento unico |
| Presenca | R$ 997 | **R$ 2.497** pagamento unico |
| Crescimento | R$ 1.497/mes | **R$ 2.997/mes** |
| Dominacao | R$ 2.497/mes | **R$ 4.997/mes** |

O Lite e para quem **ja tem site** e so precisa do Google Meu Negocio: GMN otimizado, 10 fotos,
avaliacoes organizadas, **"Perfil entregue em 7 dias uteis"** e garantia de 30 dias. O item veio
escrito como "Site entregue" no pedido; foi trocado para "Perfil" com o OK do Renan — prometer
site num pacote que nao entrega site gera cobranca depois.

O pedido original tambem mandava mexer em selos, FAQ, garantia e copy de ROI; uma segunda parte
do mesmo pedido cancelou tudo isso ("apenas precos + pacote novo"). Valeu a segunda. O preco do
Lite veio divergente (1.497 x 1.997) e o Renan confirmou **R$ 1.997**.

### O que mudou, alem do numero
- 232 paginas com a tabela (home, nichos, 199 cidades, hub, `/blog/quanto-custa-consultoria-seo-local/`).
- Titles/descriptions/og/twitter com "a partir de R$ 997" -> "R$ 1.997"; `priceRange`; schema
  `Offer`; `llms.txt`; `<select>` e o mapa `VALOR` do formulario da home.
- **"Tres formas de comecar"** -> "Quatro formas", e "qual dos tres" -> "dos quatro". Nao era
  pedido, mas o texto contradizia os 4 cartoes na tela.
- **CSS**: `.pacotes-grid` era `repeat(3, 1fr)` fixo. Com o 4o cartao a grade **estourava o
  container** (colunas de 303/297/287/315px em 1366px). Agora 1 coluna / 2x2 em 760px / 4 em
  1080px, e **`minmax(0, 1fr)`** — com `1fr` puro a coluna nao encolhe abaixo do conteudo.
  Conferido no navegador em 390, 820 e 1366px: sem estouro horizontal.

### Dois defeitos de propagacao corrigidos de passagem (valem para sempre)
1. **`aplicar-conversao.py` so INSERIA `offers` no schema quando a pagina nao tinha nenhum.**
   Ou seja: mexer no `rcb_pacotes.py` nunca chegava ao schema de quem ja tinha preco — so ao
   texto visivel. Agora sobrescreve. Sintoma que denunciaria: preco novo na tela e preco velho
   na ficha do Google.
2. **A injecao de schema so rodava em pagina "comercial"**, entao
   `/blog/quanto-custa-consultoria-seo-local/` (apoio, mas tem tabela) ficava com preco velho no
   JSON-LD. Agora a condicao e "e comercial **ou** tem a tabela".
3. **`/consultoria-seo/palmas/`** (a orfa que o gerador nao produz) estava fora dos dois
   caminhos e ia congelar no preco antigo. Virou excecao explicita no `aplicar-conversao.py`.

### Script novo
`scripts/atualizar-precos-2026-08-10.py` — cuida do que fica **fora** do bloco
`RCB:PACOTES`: title, meta, FAQ escrita a mao, `priceRange` e `llms.txt`. Faz trocas de frase
inteira (da mais longa para a mais curta) e, no fim, **varre o site atras de preco antigo que
tenha sobrado** e reclama. Atencao ao escrever esse tipo de varredura: `997.00` casa dentro de
`1997.00`, e `R$ 2.497` deixou de ser preco velho (virou o Presenca) — as bordas do regex sao
o que impede falso positivo e falso negativo.

**Ordem correta de execucao daqui em diante:**
```
python scripts/aplicar-conversao.py
python scripts/gerar-paginas-cidades.py
python scripts/atualizar-precos-2026-08-10.py
python scripts/conferir-conversao.py
```

### Publicacao (10/08/2026)
- Commit `f0d4ff7` -> `origin main` (239 arquivos). Cloudflare publicou em ~1 min.
- **As 305 URLs do sitemap conferidas uma a uma: todas HTTP 200.** Amostra conferida por
  conteudo (home, nichos, cidades, hub, contato, cases): preco novo no ar, nenhum "R$ 997".
- **IndexNow enviado ao Bing com as 305 URLs — aceito (HTTP 200).** Mesma chave
  `19341b29c6054af601879d85a34d62c5`. **Nunca gerar chave nova.** Foram as 305 porque o preco
  mudou em praticamente todas.
- Logo depois do deploy, `/seo-para-clinicas/` ainda respondeu com o HTML antigo por alguns
  segundos. Era propagacao, nao falha — reconferir antes de concluir que algo deu errado.

### Pendencias
- Falta o Renan reenviar o `sitemap.xml` no Search Console (**305 URLs, nenhuma nova**).
- CNPJ e razao social no rodape continuam faltando (item aberto desde 09/08).
- **Off-page continua sendo a prioridade no 1.** Preco mais alto so piora a conta se o funil
  continuar vazio: posicao media 38,9. Backlinks, diretorios, LinkedIn e posts de case.

## Como trabalhar neste projeto

- Renan não é técnico: sempre explicar em português simples, passo a passo, sem jargão sem explicar.
- Pedir OK antes de qualquer commit/push (regra global do CLAUDE.md pessoal) — nesta rodada de 15/07 ele autorizou publicar tudo de uma vez.
- HTML é estático e escrito à mão (sem build step) — cada página tem seu próprio `<head>` com meta tags e schema JSON-LD duplicados; ao editar textos/títulos, é preciso editar title, meta description, og:title, og:description, twitter:title, twitter:description E o schema JSON-LD todos manualmente (não há fonte única).
- CSS/JS globais: `/styles.css`, `/script.js`. Navbar e footer são blocos HTML repetidos em cada página (copiar/colar ao criar página nova — ver `scripts/gerar-paginas-cidades.py` para o padrão `NAVBAR`/`rodape()` reutilizável em Python).
- gtag/GA4 já configurado com consent mode; eventos de conversão seguem padrão `data-event="cta_click" data-location="..." data-page="..."`.
