# Plano interno — Divisão "SEO para mercados competitivos"

> **Documento interno. Não publicado no site.** Não entra no sitemap, não é linkado por nenhuma página.
> Criado em 06/08/2026. Fonte de verdade da arquitetura de conteúdo da nova divisão.

---

## 1. Decisão estratégica

O site tinha uma única frente: **SEO local** (Goiânia + 199 páginas de cidade + nichos de saúde/serviços).
Esta rodada cria uma **segunda frente**, independente e sem canibalizar a primeira:

| Frente | Público | Páginas âncora | Intenção |
|---|---|---|---|
| **SEO local** (existente) | clínicas, comércios, profissionais liberais | `/consultoria-seo-local/`, `/seo-local-goiania/`, `/consultoria-seo/<cidade>/` | "aparecer no Google da minha cidade" |
| **Mercados competitivos** (nova) | operadores digitais, afiliados, investidores, plataformas | `/seo-para-mercados-competitivos/` | "disputar o Brasil inteiro num nicho concorrido" |

**Separação de canibalização entre as duas frentes:** nenhuma página nova usa "SEO local", "Goiânia",
"Google Meu Negócio" ou "Maps" como termo-alvo. Nenhuma página local passa a mirar termos nacionais
competitivos. A ponte entre as frentes é feita por **um artigo** (`seo-local-ou-seo-nacional`) e por links
contextuais, não por sobreposição de termo-alvo.

---

## 2. Política editorial da divisão (limites inegociáveis)

Aplicada a **todas** as páginas e artigos desta divisão.

### 2.1 Nunca prometer
- primeira posição / primeira página garantida
- prazo garantido de ranqueamento
- resultado garantido pelo Google
- backlinks ilimitados
- que domínio expirado "transmite" autoridade automaticamente
- que trocar de domínio preserva posições

### 2.2 Sempre usar
"objetivo do projeto", "meta de posicionamento", "estimativa", "potencial", "cenário esperado",
"acompanhamento contínuo", "prazo sujeito à concorrência e à resposta dos mecanismos de busca".

### 2.3 Termos permitidos e como tratá-los
`black hat`, `gray hat`, `PBN`, `SEO agressivo`, `domínio expirado` — podem ser usados em artigos,
FAQs e comparativos, **sempre em posição explicativa//analítica**, nunca como serviço vendido.
A RCB explica o que são, o risco de cada um, e o que faz no lugar.

### 2.4 Nunca publicar
Tutorial operacional de: invasão, cloaking, spam, redirecionamento enganoso, falsificação de conteúdo
ou marca, uso de conteúdo de terceiros sem autorização, **contorno de bloqueio judicial ou administrativo**.

### 2.5 Qualificação de conteúdo licenciado (cluster IPTV/streaming) — **crítico**
No Brasil, a busca por "IPTV" mistura operação legítima de streaming/OTT com distribuição irregular
de conteúdo protegido. Toda página do cluster IPTV/streaming carrega um **bloco de critério de
atendimento** declarando que a RCB atende **operadores, plataformas e distribuidores que possuam
direito ou autorização sobre o conteúdo que distribuem**, e que a análise de projeto verifica isso.

**Consequência arquitetural:** a página `/migracao-de-dominio-para-iptv/` **não foi criada**. O ângulo
"trocar de domínio porque o domínio caiu" é, nesse nicho, majoritariamente uma demanda de evasão de
bloqueio — e além disso teria >60% de sobreposição com `/migracao-de-dominio-seo/`. A necessidade
legítima (rebrand, perda de registro, consolidação de sites) é atendida pela página geral.

### 2.6 Cluster bets/iGaming
Linguagem neutra quanto à regulação. Não afirmar que qualquer empresa pode operar apostas
legalmente no Brasil. Não dar conclusão jurídica. Orientar o leitor a verificar a situação regulatória
da própria operação. Sem apelo a jogo, sem promessa de ganho, sem público menor de idade.

### 2.7 Dados
Nenhum número inventado. Sem cases, depoimentos, clientes, volumes de tráfego, percentuais de
crescimento ou prazos de posicionamento fabricados. Faixas de investimento aparecem como
**faixas de projeto**, não como resultado prometido.

---

## 3. Inventário de páginas comerciais

Campos: URL · tipo · cluster · intenção · KW principal · KWs secundárias · funil · CTA · recebe links de · aponta para · risco de canibalização · diferenciação.

### Cluster A — Central

#### A1. `/seo-para-mercados-competitivos/`
- **Tipo:** pilar / hub da divisão
- **Intenção:** comercial investigativa — "quem resolve SEO em nicho difícil"
- **KW principal:** seo para mercados competitivos
- **KWs secundárias:** seo para mercados concorridos, seo para nichos difíceis, agência de seo para nicho competitivo, projeto completo de seo
- **Funil:** meio→fundo
- **CTA principal:** Solicitar análise do projeto (`/analise-de-projeto/`)
- **Recebe links de:** home (nova seção), navbar, rodapé, todas as 22 páginas do cluster, artigos 28/30/45/47
- **Aponta para:** A2, A3, A4, A5, B1, C1, D1, D2, D5, `/analise-de-projeto/`
- **Canibalização:** com A3 (`nichos competitivos`) — mitigada: A1 vende o **projeto completo** (marca+site+conteúdo+autoridade), A3 explica o **diagnóstico de dificuldade do nicho** e quando SEO comum não basta. A1 é hub, A3 é conceitual/metodológica.
- **Diferenciação:** única página que apresenta a divisão inteira e faz o roteamento para os clusters.

#### A2. `/seo-nacional/`
- **Tipo:** comercial de serviço
- **Intenção:** comercial — "aparecer no Brasil inteiro"
- **KW principal:** seo nacional
- **KWs secundárias:** seo para todo o brasil, diferença seo local e nacional, seo nacional para empresas, posicionamento nacional no google
- **Funil:** meio
- **CTA:** análise do projeto · CTA secundário: artigo 46
- **Recebe links de:** A1, home, rodapé, `/consultoria-seo-local/`, `/consultoria-seo/` (hub de cidades), artigos 46/28
- **Aponta para:** A1, A3, D3, `/consultoria-seo-local/` (rota inversa para quem é local)
- **Canibalização:** com `/consultoria-seo-local/` — **resolvida na origem**: A2 nunca usa "local/cidade/Maps"; a página local nunca usa "nacional". Cada uma linka para a outra como desambiguação ("se o seu caso é X, veja Y").
- **Diferenciação:** único conteúdo que explica a mecânica de disputa nacional (volume, SERP, autoridade, prazo).

#### A3. `/seo-para-nichos-competitivos/`
- **Tipo:** comercial / metodológica
- **Intenção:** informacional-comercial — "por que meu SEO não sai do lugar"
- **KW principal:** seo para nichos competitivos
- **KWs secundárias:** seo para nicho concorrido, seo não funciona no meu nicho, como competir em nicho difícil
- **Funil:** topo→meio
- **CTA:** análise do projeto
- **Recebe links de:** A1, A4, D3, artigos 47/48/45
- **Aponta para:** A1, A4, D3, D4
- **Canibalização:** com A1 e A4 — mitigada por ângulo: A3 = diagnóstico ("seu nicho é difícil por quê"), A4 = intensidade de execução, A1 = oferta.
- **Diferenciação:** traz o método de leitura de dificuldade da SERP.

#### A4. `/seo-agressivo/`
- **Tipo:** comercial / posicionamento
- **Intenção:** comercial — busca por execução rápida e intensa
- **KW principal:** seo agressivo
- **KWs secundárias:** seo rápido, estratégia agressiva de seo, seo intensivo, quanto tempo para primeira página
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** A1, A3, artigos 30/31/29
- **Aponta para:** A1, A3, D3, artigos 30/31/32/33
- **Canibalização:** com A3 — A4 fala **ritmo e volume de execução**; A3 fala **dificuldade do mercado**.
- **Diferenciação:** é a página que separa "velocidade" de "imprudência" — trata black hat/PBN de forma explicativa e diz o que a RCB faz no lugar. Página de descompressão de objeção.

#### A5. `/seo-para-negocios-digitais/`
- **Tipo:** comercial de segmento
- **Intenção:** comercial — produto digital / assinatura / plataforma
- **KW principal:** seo para negócios digitais
- **KWs secundárias:** seo para produto digital, seo para saas, seo para plataforma, seo para negócio por assinatura
- **Funil:** meio
- **CTA:** análise do projeto
- **Recebe links de:** A1, home, B6, C6
- **Aponta para:** A1, A2, B6, C6, D5
- **Canibalização:** baixa — é o guarda-chuva para segmentos digitais fora de IPTV/bets.
- **Diferenciação:** único conteúdo sobre aquisição orgânica de produto digital (ciclo, LTV, conteúdo de fundo).

---

### Cluster B — IPTV e streaming
> Todas as páginas deste cluster carregam o bloco de critério de atendimento (§2.5).

#### B1. `/seo-para-iptv/`
- **Tipo:** pilar do cluster · **página comercial de maior prioridade do site**
- **Intenção:** comercial — projeto completo
- **KW principal:** seo para iptv
- **KWs secundárias:** posicionar iptv no google, iptv na primeira página, seo nacional para iptv, quanto custa seo para iptv, projeto de site iptv
- **Funil:** meio→fundo
- **CTA:** análise do projeto · secundário: WhatsApp
- **Recebe links de:** A1, home, navbar, rodapé, B2–B6, artigos 1–15
- **Aponta para:** B2, B3, B4, B5, B6, A2, D1, artigos 1/2/3/9
- **Canibalização:** absorve o que seria `/seo-nacional-para-iptv/` (ver §4).
- **Diferenciação:** é a única página que cobre o projeto ponta a ponta (marca→site→conteúdo→autoridade→acompanhamento).

#### B2. `/criacao-de-site-para-iptv/`
- **Tipo:** comercial de desenvolvimento
- **Intenção:** transacional — "quero o site"
- **KW principal:** criação de site para iptv
- **KWs secundárias:** site para iptv, site de iptv do zero, desenvolvimento de site iptv, site com planos e whatsapp
- **Funil:** fundo
- **CTA:** análise do projeto
- **Recebe links de:** B1, B3, artigos 4/10/15
- **Aponta para:** B1, B3, D1
- **Canibalização:** com B1 — separação clara: **B2 = entrega do site** (marca, layout, planos, velocidade, dispositivos, hospedagem, manutenção). **B1 = estratégia de posicionamento.** B2 quase não fala de ranking; B1 quase não fala de layout.
- **Diferenciação:** única página de desenvolvimento do cluster.

#### B3. `/seo-para-revendedor-iptv/`
- **Tipo:** comercial de subsegmento
- **Intenção:** comercial — revendedor sem estrutura própria
- **KW principal:** seo para revendedor de iptv
- **KWs secundárias:** site para revendedor iptv, revendedor iptv como divulgar, sair do instagram para site próprio
- **Funil:** meio
- **CTA:** análise do projeto
- **Recebe links de:** B1, B2, artigo 15
- **Aponta para:** B1, B2, artigos 15/10
- **Canibalização:** com B1/B2 — B3 é **porte e maturidade menores**: quem não tem marca, depende de rede social e quer estrutura própria. Ticket e escopo menores, linguagem menos corporativa.
- **Diferenciação:** único conteúdo sobre sair da dependência de rede social para ativo próprio.

#### B4. `/link-building-para-iptv/`
- **Tipo:** comercial de serviço dentro do nicho
- **KW principal:** link building para iptv · **secundárias:** backlinks para iptv, autoridade para site de iptv
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** B1, D3, artigos 7/8
- **Aponta para:** B1, D3, D4, artigos 7/8/38
- **Canibalização:** com D3 (`link-building-para-nichos-competitivos`) — **B4 é aplicação no nicho** (que tipo de veículo aceita o tema, relevância temática, ritmo); **D3 é a metodologia geral**. B4 linka para D3 como aprofundamento.
- **Diferenciação:** trata a dificuldade específica de conseguir menções num nicho sensível.

#### B5. `/dominio-expirado-para-iptv/`
- **Tipo:** comercial de serviço dentro do nicho
- **KW principal:** domínio expirado para iptv · **secundárias:** domínio com autoridade para iptv, comprar domínio expirado iptv, domínio com backlinks
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** B1, D1, artigos 5/6/14
- **Aponta para:** B1, D1, artigos 5/6/14/39/41
- **Canibalização:** com D1 (`analise-de-dominios-expirados`) — **B5 = por que o nicho procura isso e o que muda na análise nesse contexto**; **D1 = o serviço de análise em si** (triagem, critérios, entregável, custo). B5 é curta e roteia para D1.
- **Diferenciação:** trata expectativa do nicho ("domínio pronto resolve?") e desmonta o mito.

#### B6. `/seo-para-streaming-e-tv-online/`
- **Tipo:** comercial de segmento
- **KW principal:** seo para streaming · **secundárias:** seo para tv online, seo para plataforma de streaming, seo para serviço por assinatura, aquisição orgânica streaming
- **Funil:** meio
- **CTA:** análise do projeto
- **Recebe links de:** B1, A5, home
- **Aponta para:** A5, A2, B1, D5
- **Canibalização:** com B1 — B6 é **operação licenciada de plataforma/OTT** (catálogo, lançamento, assinatura, app), público corporativo; B1 é o projeto de posicionamento do nicho IPTV.
- **Diferenciação:** único conteúdo sobre ciclo de lançamento de catálogo e retenção de assinante via orgânico.

---

### Cluster C — Bets, apostas e iGaming

#### C1. `/seo-para-bets/`
- **Tipo:** pilar do cluster
- **KW principal:** seo para bets · **secundárias:** seo para bet, seo para casa de apostas, seo para site de apostas, quanto custa seo para bet, seo para cassino online
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** A1, home, navbar, rodapé, C2–C6, artigos 16–27
- **Aponta para:** C2, C3, C4, C5, C6, A2, D3, artigos 16/17/23
- **Canibalização:** absorve `/seo-para-cassino-online/` (ver §4) numa seção própria + artigo 23.
- **Diferenciação:** pilar de operação de marca de apostas.

#### C2. `/seo-para-igaming/`
- **Tipo:** comercial B2B
- **KW principal:** seo para igaming · **secundárias:** seo igaming brasil, marketing digital igaming, seo para provedor de jogos, expansão igaming brasil
- **Funil:** meio
- **CTA:** análise do projeto
- **Recebe links de:** C1, A5, artigos 18/25
- **Aponta para:** C1, A2, A5, artigos 18/25
- **Canibalização:** com C1 — **C2 é B2B** (plataformas, provedores, sistemas, pagamentos, CRM, empresa estrangeira entrando no Brasil, localização de conteúdo). **C1 é B2C** (marca que capta apostador). Públicos e SERPs diferentes.
- **Diferenciação:** único conteúdo sobre localização pt-BR e entrada de empresa estrangeira.

#### C3. `/seo-para-afiliados-de-apostas/`
- **Tipo:** pilar de subsegmento
- **KW principal:** seo para afiliados de apostas · **secundárias:** seo para afiliado de bet, portal de apostas, site de review de casa de apostas, site de bônus
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** C1, C4, C5, artigos 19/20/22/27
- **Aponta para:** C4, C5, C1, D3, artigos 20/22/27
- **Canibalização:** com C1 — **modelo de negócio diferente**: C3 é mídia/conteúdo (arquitetura por categoria, review, comparativo, bônus, rastreamento de comissão). C1 é operador.
- **Diferenciação:** único conteúdo sobre arquitetura de portal de conteúdo monetizado por afiliação.

#### C4. `/criacao-de-site-para-afiliado-de-bet/`
- **Tipo:** comercial de desenvolvimento
- **KW principal:** criação de site para afiliado de bet · **secundárias:** site para afiliado de apostas, cms para portal de apostas, site de comparação de casas de apostas
- **Funil:** fundo
- **CTA:** análise do projeto
- **Recebe links de:** C3, artigos 19/22
- **Aponta para:** C3, C1, D3
- **Canibalização:** com C3 — mesma separação de B1/B2: **C4 entrega o site** (estrutura de conteúdo, tabelas, filtros, comparativos, CTA, escalabilidade); C3 vende a **estratégia**.
- **Diferenciação:** única página do cluster sobre construção técnica.

#### C5. `/link-building-para-bets/`
- **Tipo:** comercial de serviço dentro do nicho
- **KW principal:** link building para bets · **secundárias:** backlinks para bets, autoridade para site de apostas, backlinks igaming
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** C1, C3, D3, artigo 21
- **Aponta para:** C1, D3, D4, artigos 21/36/37/38
- **Canibalização:** com D3 e B4 — mesma regra do B4: aplicação no nicho, roteando para D3 como metodologia.
- **Diferenciação:** trata custo e escassez de veículos no nicho, e leitura de risco.

#### C6. `/seo-para-jogos-online/`
- **Tipo:** comercial de segmento adjacente
- **KW principal:** seo para jogos online · **secundárias:** seo para plataforma de jogos, seo para portal de games, seo para app de jogos, lançamento de jogo
- **Funil:** topo→meio
- **CTA:** análise do projeto
- **Recebe links de:** C1, A5, artigo 24
- **Aponta para:** A5, A2, C1, artigo 24
- **Canibalização:** com C1 — **C6 não é aposta**: games, portais, apps, assinatura, comunidade, lançamento. Separado propositalmente para não misturar públicos.
- **Diferenciação:** único conteúdo sobre pico de lançamento e conteúdo de comunidade.

---

### Cluster D — Domínios, autoridade e recuperação

#### D1. `/analise-de-dominios-expirados/`
- **Tipo:** comercial de serviço (avulso e dentro de projeto)
- **KW principal:** análise de domínios expirados · **secundárias:** comprar domínio expirado, domínio expirado com backlinks, domínio premium, avaliar domínio antes de comprar
- **Funil:** fundo
- **CTA:** análise do projeto
- **Recebe links de:** A1, B5, home, rodapé, artigos 6/14/39/40/41/42
- **Aponta para:** D2, D4, B5, artigos 39/40/41/42
- **Canibalização:** com B5 — resolvida (§B5).
- **Diferenciação:** é o **serviço**: critérios de triagem, histórico, perfil de links, risco, recomendação de compra, registro em nome do cliente.

#### D2. `/migracao-de-dominio-seo/`
- **Tipo:** comercial técnica
- **KW principal:** migração de domínio · **secundárias:** trocar domínio sem perder seo, mudar de domínio, migração de site, perdi meu domínio, consolidar sites
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** A1, D1, D5, rodapé, artigos 11/12/13/43
- **Aponta para:** D5, D1, artigos 11/12/13/43
- **Canibalização:** absorve `/migracao-de-dominio-para-iptv/` (ver §4 e §2.5).
- **Diferenciação:** único conteúdo com o processo técnico completo (DNS, certificado, redirecionamento, sitemap, Search Console, Analytics, monitoramento, reconstrução).

#### D3. `/link-building-para-nichos-competitivos/`
- **Tipo:** comercial de serviço — metodologia
- **KW principal:** link building para nichos competitivos · **secundárias:** construção de autoridade, estratégia de backlinks, link building nacional
- **Funil:** meio
- **CTA:** análise do projeto
- **Recebe links de:** A1, A3, B4, C5, D4, artigos 36/37/38/48/49
- **Aponta para:** D4, A1, B4, C5, artigos 36/37/38/49/50
- **Canibalização:** com D4 — **D3 = construir** links novos. **D4 = auditar** o perfil existente. Verbos diferentes, entregáveis diferentes.
- **Diferenciação:** metodologia geral, reaproveitada pelas páginas de nicho.

#### D4. `/consultoria-de-backlinks/`
- **Tipo:** comercial de serviço — auditoria
- **KW principal:** consultoria de backlinks · **secundárias:** auditoria de backlinks, análise de perfil de links, links tóxicos, backlinks dos concorrentes
- **Funil:** meio→fundo
- **CTA:** análise do projeto
- **Recebe links de:** D3, D5, artigos 38/50
- **Aponta para:** D3, D5, artigos 38/50/36
- **Canibalização:** com D3 — resolvida (§D3).
- **Diferenciação:** entregável é diagnóstico + priorização, não execução.

#### D5. `/recuperacao-de-trafego-organico/`
- **Tipo:** comercial de serviço — emergência
- **KW principal:** recuperação de tráfego orgânico · **secundárias:** perdi tráfego no google, caí de posição, queda após atualização do google, site perdeu visibilidade
- **Funil:** fundo (urgência alta)
- **CTA:** análise do projeto
- **Recebe links de:** A1, D2, D4, rodapé, artigo 44
- **Aponta para:** D2, D4, D3, A3, artigo 44
- **Canibalização:** com D2 — D5 é **sintoma** (perdi tráfego, causa desconhecida); D2 é **projeto planejado** de troca de domínio. D5 lista migração como uma das causas e linka para D2.
- **Diferenciação:** única página organizada por diagnóstico diferencial de causa.

---

### Conversão

#### E1. `/analise-de-projeto/`
- **Tipo:** formulário de qualificação de alto valor
- **Intenção:** transacional
- **Indexação:** `index, follow` (é conteúdo útil e destino de CTA), mas sem disputa de KW própria
- **Recebe links de:** CTA principal de **todas** as 22 páginas da divisão + nova seção da home + navbar + rodapé
- **Aponta para:** A1, e para os pilares B1/C1/D1
- **Diferenciação:** único formulário do site que qualifica por segmento, prazo, faixa de investimento e escopo (marca/site/domínio). O restante do site converte por WhatsApp e diagnóstico gratuito — este é o funil de ticket alto.

---

## 4. Páginas planejadas e **consolidadas** (não criadas)

| URL planejada | Decisão | Motivo |
|---|---|---|
| `/seo-nacional-para-iptv/` | consolidada em `/seo-para-iptv/` (seção "Disputa nacional") + artigo 9 | ~75% de sobreposição de intenção com o pilar: quem busca "seo para iptv" já busca alcance nacional. Duas URLs disputariam a mesma SERP. |
| `/seo-para-cassino-online/` | consolidada em `/seo-para-bets/` (seção própria) + artigo 23 | Mesmo público (operador), mesmo serviço, mesma jornada. Diferenciação real ficaria abaixo de 40%. |
| `/migracao-de-dominio-para-iptv/` | consolidada em `/migracao-de-dominio-seo/` + artigo 12 | Dupla razão: (a) >60% de sobreposição com a página geral; (b) política §2.5 — o recorte "IPTV + trocar domínio" atrai demanda de evasão de bloqueio, que a RCB não atende. |

Se no futuro o Search Console mostrar volume próprio e distinto para esses termos, a decisão pode ser
revista — mas só com conteúdo genuinamente diferente, não com recorte de nicho sobre o mesmo texto.

---

## 5. Blog — clusters e artigos

Dois novos clusters no índice do blog (`/blog/`), integrados ao padrão `blog-cluster` existente:

- **`#mercados-competitivos`** — "SEO para mercados competitivos" (IPTV, bets, iGaming, projetos nacionais)
- **`#dominios-autoridade`** — "Domínios, autoridade e link building"

Categorias funcionam como **agrupamento no índice + metadado `artigo-cat`**, sem páginas de categoria
indexáveis próprias (evita página fraca com poucos itens — regra do briefing §12).

### Prioridade de produção
- **P1 (fundo de funil / objeção de compra):** 1, 2, 16, 17, 28, 29, 39, 44, 46
- **P2 (decisão técnica):** 5, 6, 9, 12, 20, 30, 32, 34, 36, 38, 43, 45, 47, 48
- **P3 (aprofundamento):** demais

### Índice numerado (referência de links internos usada acima)

**IPTV/streaming:** 1 quanto-custa-seo-para-iptv · 2 quanto-tempo-posicionar-site-iptv · 3 iptv-primeira-pagina-3-4-meses · 4 como-criar-site-para-iptv-do-zero · 5 dominio-novo-ou-expirado-para-iptv · 6 como-escolher-dominio-expirado-com-autoridade · 7 backlinks-para-iptv-funcionam · 8 quanto-investir-backlinks-iptv · 9 seo-nacional-para-iptv-o-que-muda · 10 estruturar-site-iptv-para-gerar-contatos · 11 o-que-acontece-com-seo-ao-trocar-dominio · 12 como-migrar-site-para-outro-dominio · 13 dominio-caiu-o-que-fazer · 14 como-analisar-historico-de-dominio-expirado · 15 site-para-revendedor-iptv-o-que-precisa-ter

**Bets/iGaming:** 16 quanto-custa-seo-para-sites-de-apostas · 17 quanto-tempo-para-posicionar-uma-bet · 18 como-funciona-seo-para-igaming · 19 como-criar-site-para-afiliado-de-apostas · 20 seo-para-afiliados-como-estruturar-projeto · 21 link-building-para-bets-o-que-avaliar · 22 como-criar-paginas-de-avaliacao-de-casas-de-apostas · 23 seo-para-cassino-online-desafios · 24 como-posicionar-portal-de-jogos-online · 25 seo-no-brasil-para-empresas-estrangeiras-de-igaming · 26 conteudo-autoridade-conversao-sites-de-apostas · 27 site-de-afiliado-competir-nacionalmente

**Autoridade/domínios/competitivo:** 28 quanto-custa-chegar-primeira-pagina · 29 e-possivel-garantir-primeira-pagina · 30 o-que-e-seo-agressivo · 31 seo-agressivo-funciona-em-nichos-concorridos · 32 o-que-e-black-hat-seo · 33 black-hat-gray-hat-white-hat-diferenca · 34 o-que-e-pbn-e-como-funciona · 35 pbn-ainda-funciona-para-seo · 36 comprar-backlinks-ajuda-no-posicionamento · 37 quanto-custa-um-backlink-de-qualidade · 38 como-avaliar-qualidade-de-um-backlink · 39 dominio-expirado-ainda-funciona-para-seo · 40 dominio-expirado-com-backlinks-vale-a-pena · 41 como-saber-se-dominio-expirado-foi-usado-para-spam · 42 dominio-premium-ou-dominio-expirado · 43 trocar-de-dominio-faz-perder-posicoes · 44 como-recuperar-trafego-organico-apos-queda · 45 por-que-alguns-projetos-de-seo-precisam-de-mais-investimento · 46 seo-local-ou-seo-nacional-diferenca · 47 como-funciona-projeto-de-seo-para-nichos-competitivos · 48 conteudo-ou-backlinks-onde-investir-primeiro · 49 quantos-backlinks-um-site-precisa · 50 como-analisar-backlinks-dos-concorrentes

---

## 5.1 Status de produção (06/08/2026)

**Publicados: 40 dos 50 artigos planejados** (~29.800 palavras). Todos completos, com FAQ visível,
schema `BlogPosting` + `BreadcrumbList` + `FAQPage`, CTA e links internos. Nenhum arquivo vazio ou
placeholder foi criado.

**Backlog — 10 artigos não produzidos.** A lista abaixo registra também por que cada um ficou por
último: em todos os casos a intenção já é atendida, no todo ou em parte, por um conteúdo publicado.
Isso significa que produzi-los exige um ângulo genuinamente novo — não uma reescrita do que já existe,
que só criaria canibalização.

| # | Slug | Intenção já coberta por | O que precisaria ter de novo |
|---|---|---|---|
| 3 | iptv-primeira-pagina-3-4-meses | artigo 2 (prazo) + FAQ dele | cenário numérico por faixa de dificuldade de termo |
| 6 | como-escolher-dominio-expirado-com-autoridade | artigo 14 (análise de histórico) | critérios de *escolha entre candidatos*, não de verificação |
| 7 | backlinks-para-iptv-funcionam | artigo 8 + página B4 | leitura de eficácia por tipo de veículo no nicho |
| 9 | seo-nacional-para-iptv-o-que-muda | seção "Disputa nacional" de B1 (consolidação §4) | só se o Search Console mostrar volume próprio |
| 11 | o-que-acontece-com-seo-ao-trocar-dominio | artigo 43 (perder posições) | mecânica técnica do que é reavaliado, mais a fundo |
| 13 | dominio-caiu-o-que-fazer | artigo 12 (migração) + D2 | **restrito por política §2.5** — só o recorte legítimo (perda de registro), nunca o de bloqueio |
| 20 | seo-para-afiliados-como-estruturar-projeto | página C3 (arquitetura completa) | roteiro de execução mês a mês |
| 21 | link-building-para-bets-o-que-avaliar | artigo 38 + página C5 | critérios específicos do mercado de links do setor |
| 26 | conteudo-autoridade-conversao-sites-de-apostas | página C1 (seção de conteúdo) | integração entre as três frentes, com métricas |
| 27 | site-de-afiliado-competir-nacionalmente | página C3 + artigo 19 | comparação de porte: afiliado pequeno × portal grande |

**Recomendação:** não produzir os 10 de uma vez. Esperar o Search Console mostrar quais termos dos 40
publicados geram impressão e priorizar o backlog por demanda observada — em vez de por completude da
lista original.

---

## 6. Ligação com o conteúdo antigo (links contextuais, sem reescrita artificial)

| Página existente | Link inserido | Gancho natural |
|---|---|---|
| `/consultoria-seo-local/` | → `/seo-nacional/` | desambiguação: "se você atende o Brasil todo e não uma cidade" |
| `/consultoria-seo/` (hub cidades) | → `/seo-nacional/` | mesmo gancho |
| `/site-otimizado-para-seo/` | → `/seo-para-negocios-digitais/` | criação de site para operação digital |
| `/auditoria-seo/` | → `/consultoria-de-backlinks/`, `/recuperacao-de-trafego-organico/` | auditoria → perfil de links / queda |
| `/conteudo-para-seo/` | → `/link-building-para-nichos-competitivos/` | conteúdo → autoridade |
| `/acompanhamento-seo/` | → `/recuperacao-de-trafego-organico/` | queda detectada no acompanhamento |
| blog `por-que-meu-site-nao-aparece-no-google` | → `/seo-para-nichos-competitivos/` | quando a causa é dificuldade de mercado |
| blog `quanto-tempo-demora-seo-local` | → artigo 46 | leitor confundindo local com nacional |
| blog `como-melhorar-posicionamento-empresa-google` | → `/seo-nacional/` | escala além da cidade |

Regra: **um link por página existente, dentro de frase já existente ou de uma frase nova coerente com o
parágrafo**. Nada de bloco "veja também" enxertado.

---

## 7. Regras técnicas de implementação

- Sem framework, sem build. HTML estático, mesmo padrão do restante do site.
- Geração por script Python (`scripts/rcb_base.py` + `scripts/gerar-paginas-competitivas.py` +
  `scripts/gerar-artigos-competitivos.py`), idempotente, no mesmo espírito de
  `scripts/gerar-paginas-cidades.py`. **O conteúdo de cada página é único e escrito à mão dentro do
  script** — o script cuida só do invólucro (head, navbar, rodapé, schema, breadcrumb).
- Navbar e rodapé atualizados em massa por `scripts/atualizar-nav-rodape.py` (bloco `nav-menu` tem
  variante única em 305 arquivos; rodapé tem duas âncoras: `Contato` e `Contato Direto`).
- Schema por tipo de página: `Service` + `BreadcrumbList` + `FAQPage` (comerciais);
  `BlogPosting` + `BreadcrumbList` (+ `FAQPage` quando houver FAQ visível) nos artigos.
- Todas as URLs novas entram no `sitemap.xml` e no `llms.txt`.
- Sem imagens novas: identidade visual por CSS já existente (cards, tabelas `case-table`, pills).
  OG image compartilhada `assets/img/og-rcb-1200x628.png`.
