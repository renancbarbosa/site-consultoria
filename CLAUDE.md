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

O que resolve: apagar o **deployment de preview** no painel (Workers & Pages → projeto →
Deployments → entrada do branch → Delete). Apagar o branch no GitHub não basta — o deployment
sobrevive ao branch.

Risco de SEO: baixo, porque o preview sai com `noindex`. Mas evite criar branches remotos neste
repositório só para backup: o histórico do `main` já preserva tudo (`2507c42` continua alcançável),
e há a tag local `divisao-competitiva-backup`.

## Como trabalhar neste projeto

- Renan não é técnico: sempre explicar em português simples, passo a passo, sem jargão sem explicar.
- Pedir OK antes de qualquer commit/push (regra global do CLAUDE.md pessoal) — nesta rodada de 15/07 ele autorizou publicar tudo de uma vez.
- HTML é estático e escrito à mão (sem build step) — cada página tem seu próprio `<head>` com meta tags e schema JSON-LD duplicados; ao editar textos/títulos, é preciso editar title, meta description, og:title, og:description, twitter:title, twitter:description E o schema JSON-LD todos manualmente (não há fonte única).
- CSS/JS globais: `/styles.css`, `/script.js`. Navbar e footer são blocos HTML repetidos em cada página (copiar/colar ao criar página nova — ver `scripts/gerar-paginas-cidades.py` para o padrão `NAVBAR`/`rodape()` reutilizável em Python).
- gtag/GA4 já configurado com consent mode; eventos de conversão seguem padrão `data-event="cta_click" data-location="..." data-page="..."`.
