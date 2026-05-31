# Auditoria do Site RCB Consultoria — rcbseo.com.br
**Data:** 30 de maio de 2026  
**Auditor:** Claude Code (análise de arquivos + Playwright + Exa)  
**Escopo:** SEO técnico, conteúdo/copy, SEO local, visual no navegador, comparativo com concorrentes

---

## O que já está bom

### SEO Técnico
- **Title tags:** únicas, descritivas e com palavras-chave em todas as páginas.
- **Meta descriptions:** presentes, dentro do tamanho ideal, com gancho de conversão.
- **H1:** um único por página, bem alinhado com a keyword principal.
- **Canonical:** presente e consistente em todas as URLs (apontando para `rcbseo.com.br`).
- **hreflang pt-BR:** declarado corretamente em todas as páginas.
- **robots.txt:** correto — permite indexação e aponta para o sitemap.
- **sitemap.xml:** completo, prioridades coerentes, datas atualizadas.
- **Schema markup:** robusto e bem estruturado — `LocalBusiness`, `Person`, `WebPage`, `FAQPage`, `BreadcrumbList`, `Service`, `BlogPosting`, `AggregateRating` e `Review` implementados.
- **Open Graph e Twitter Card:** presentes em todas as páginas.
- **Acessibilidade:** skip link, ARIA labels no menu e botões, `lang="pt-BR"` declarado.
- **Imagens:** alt text descritivo, `width` e `height` declarados, `loading="lazy"` nos elementos abaixo do dobramento, `loading="eager"` no hero, `decoding="async"` em todas.
- **Performance na home:** Google Fonts carrega de forma não-bloqueante (truque `media="print"` + `onload`), com fallback para `<noscript>`.
- **Consentimento de cookies:** Consent Mode v2 do Google implementado corretamente, com `analytics_storage: denied` por padrão até o usuário aceitar.
- **Analytics duplo:** GA4 (`G-K644KXR38G`) + Cloudflare Web Analytics como backup.
- **Favicons completos:** SVG, 32×32, 16×16, apple-touch-icon e webmanifest todos presentes.
- **Breadcrumbs visuais e em schema** em todas as subpáginas.

### Conteúdo e Copy
- **H1 da home** muito eficaz: "SEO Local e Google Meu Negócio para clínicas, dentistas e negócios de saúde".
- **Copy direto e sem enrolação:** a frase "Seu paciente já pesquisa no Google antes de marcar. A pergunta é: ele encontra você ou encontra seu concorrente?" é poderosa.
- **Seção de problemas:** 6 dores reais dos clientes, bem identificadas e descritas.
- **Método em 4 passos** explicado de forma clara — ajuda a reduzir objeções de quem não conhece SEO.
- **CTAs múltiplos e consistentes:** botão de diagnóstico no hero, na seção final, WhatsApp flutuante, formulário de contato — boa cobertura de intenções diferentes.
- **Case real** (Docevidade) com métricas concretas (posição #1, 1.969 visualizações, 12,8% conversão em rotas).
- **Diferenciação por nicho:** páginas específicas para clínicas, dentistas, estética, médicos, emagrecimento — isso é difícil de encontrar em concorrentes locais.

### SEO Local
- Nome/telefone/email consistentes em todas as páginas e no schema.
- Palavra-chave "Goiânia" bem posicionada em títulos, metas e conteúdo das páginas-chave.
- Schema `areaServed` inclui cidades vizinhas (Aparecida de Goiânia, Trindade, Senador Canedo).
- Badge "Goiânia presencial · Consultoria online no Brasil" no hero — sinal local visível imediatamente.

### Visual no Navegador (Playwright)
- **Desktop:** layout limpo, hierarquia visual clara, navbar com dropdown funcional, foto do Renan carregou rápido.
- **Mobile (390×844px):** responsivo, fonte legível, menu hambúrguer funcionando, badge do hero com quebra de linha correta.
- **Design dark navy + gold** é distintivo e transmite credibilidade — diferencial visual claro em relação aos concorrentes.

---

## Problemas por nível de impacto

---

### ALTO

#### 1. `logo.png` referenciado no schema mas o arquivo não existe no servidor

**Onde aparece:** campo `"logo": "https://rcbseo.com.br/logo.png"` dentro do schema `LocalBusiness` em todas as páginas (`index.html`, `seo-para-clinicas/`, `seo-para-dentistas/`, `seo-local-goiania/` e outras).  
**O problema:** O arquivo `logo.png` não existe na raiz do site. O arquivo real é `assets/img/logo-rcb-seo-local.png`. Quando o Google tenta validar o logo da empresa via schema, encontra um 404. Isso pode afetar exibição em rich results e o Knowledge Panel.  
**Ação:** Corrigir o caminho para `https://rcbseo.com.br/assets/img/logo-rcb-seo-local.png` em todos os arquivos, ou criar um `logo.png` na raiz apontando para a imagem correta.  
**Tipo:** Ganho rápido (busca e substituição em todos os HTMLs)

---

#### 2. Blog com apenas 2 artigos — volume de conteúdo insuficiente para construir autoridade

**O problema:** O blog tem só 2 posts publicados. Para um consultor de SEO que vende justamente a capacidade de "criar conteúdo e autoridade", isso é um ponto fraco visível. Concorrentes com mais artigos publicados constroem PageRank interno e sinal de especialista (E-E-A-T) mais rápido. Cada artigo publicado é também uma oportunidade de captura de tráfego informacional que pode se converter.  
**Ação:** Publicar artigos com regularidade (meta: 1 por mês), priorizando perguntas que os clientes fazem no diagnóstico. Exemplos de temas: "Por que minha clínica não aparece no Google Maps", "Quanto tempo leva o SEO local para funcionar", "Google Meu Negócio para dentistas: guia completo". Os 2 artigos existentes já têm boa estrutura — é questão de volume.  
**Tipo:** Trabalho maior (exige produção contínua)

---

#### 3. Sem endereço físico completo (rua/número/CEP) em nenhuma parte do site

**O problema:** O schema `LocalBusiness` só tem `addressLocality: Goiânia` e `addressRegion: GO`. O footer também não tem rua, número ou CEP. Para o Local Pack do Google e para o sinal de NAP (Nome + Endereço + Telefone), o endereço completo é um dos fatores mais fortes. Qualquer concorrente com endereço completo cadastrado tem vantagem direta neste sinal. Os concorrentes auditados (ex.: Luís Cláudio do Brainstorm Marketing) já têm endereço completo visível.  
**Ação:** Adicionar endereço completo no schema e no footer — mesmo que seja home office ou coworking. Se não há endereço fixo, um endereço de coworking usado com frequência resolve o problema para fins de SEO local.  
**Tipo:** Ganho rápido (edição de schema e footer)

---

### MÉDIO

#### 4. Subpáginas usam Google Fonts de forma bloqueante (peso 300 incluído)

**Onde aparece:** Todas as subpáginas (`seo-para-clinicas/`, `seo-para-dentistas/`, `blog/`, `cases/`, `sobre/`, `contato/`, `diagnostico-gratuito/` etc.) têm:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```
A home usa a versão não-bloqueante correta (com `media="print"` + `onload`). E o peso 300 que foi removido da home ainda está presente nas subpáginas (carrega ~10% a mais desnecessariamente).  
**Impacto:** Atraso no First Contentful Paint (FCP) e Largest Contentful Paint (LCP) nas subpáginas — métricas que o Google usa no Core Web Vitals.  
**Ação:** Substituir o `<link rel="stylesheet">` bloqueante por o mesmo padrão da home (`media="print"` + `onload` + `<noscript>`) em todas as subpáginas. Remover o weight `300` da lista.  
**Tipo:** Ganho rápido (edição em massa dos HTMLs das subpáginas)

---

#### 5. OG image incorreta em 7+ páginas (logo 600×120px com `summary_large_image`)

**Onde aparece:** `seo-para-dentistas/`, `blog/`, `blog/como-aparecer-google-clinica-estetica-goiania/`, `blog/por-que-minha-clinica-odontologica-nao-aparece-no-google/`, `diagnostico-gratuito/`, `contato/` — todas declaram `twitter:card: summary_large_image` mas usam `assets/img/logo-rcb-seo-local.png` (600×120px) como imagem.  
**O problema:** O Twitter/X exige pelo menos 1200×628px para `summary_large_image`. Imagens menores ou com proporção errada resultam em preview cortado, borrado ou não exibido — o que prejudica cliques quando alguém compartilha o link.  
**Ação:** Criar uma imagem OG padrão de fallback (1200×628px) com identidade visual do site para usar nessas páginas. Pode ser uma versão da foto do Renan com nome e slogan, ou uma imagem temática. Ou trocar o card type para `summary` nessas páginas.  
**Tipo:** Trabalho médio (criação de assets de imagem)

---

#### 6. Cookie banner bloqueia ~40% da tela mobile no primeiro acesso

**Observado em:** Playwright com viewport 390×844px (iPhone 14).  
**O problema:** O banner de cookies aparece sobreposto ao conteúdo da home e das subpáginas e cobre quase a metade inferior da tela. O usuário precisa clicar antes de ver o CTA principal e o texto do hero. Isso aumenta o tempo até o primeiro engajamento e pode aumentar a taxa de rejeição em mobile.  
**Ação:** Reduzir a altura do banner (condensar o texto em uma linha) ou posicioná-lo como uma barra menor fixa no topo/rodapé em vez de um overlay grande.  
**Tipo:** Ganho rápido (ajuste de CSS no cookie-consent.js)

---

#### 7. Dois depoimentos com sobrenome idêntico podem gerar descrédito

**Onde aparece:** Seção de depoimentos da home — Laís Breitenbach Simão (confeitaria) e Fátima Isabel Breitenbach Simão (comércio local). Ambas têm o mesmo sobrenome composto.  
**O problema:** Visitantes atentos podem perceber que os dois nomes parecem da mesma família, o que pode gerar dúvida sobre autenticidade — especialmente sendo 2 dos 3 depoimentos. No schema de `Review`, os dois nomes também aparecem.  
**Ação:** Se as duas pessoas realmente são da mesma família, adicionar o contexto (ex.: "mãe e filha, donas de negócios diferentes") para tornar a situação compreensível. Também vale buscar e adicionar mais depoimentos de outras pessoas para diversificar.  
**Tipo:** Ganho rápido (editorial)

---

#### 8. Apenas 1 rede social no schema `sameAs` (só Instagram)

**O problema:** O schema `sameAs` do `Person` e `LocalBusiness` referencia só o Instagram (`https://www.instagram.com/rcbseo`). LinkedIn em particular é um sinal forte de credibilidade E-E-A-T para o Google, especialmente para consultores individuais.  
**Ação:** Adicionar o perfil do LinkedIn, e qualquer outro perfil verificável (YouTube, Google Business Profile URL), ao array `sameAs` no schema.  
**Tipo:** Ganho rápido

---

### BAIXO

#### 9. Comentários TODO visíveis no HTML de produção

**Onde aparece:**
- `blog/index.html` linha 34: `<!-- TODO: substituir por og:image específica desta página -->`
- `diagnostico-gratuito/index.html` linha 35: `<!-- TODO: substituir por og:image específica desta página -->`

**O problema:** Comentários de desenvolvimento em produção são visíveis no código-fonte e passam uma impressão de inacabado para quem analisa o HTML.  
**Ação:** Remover os comentários TODO dos arquivos publicados.  
**Tipo:** Ganho rápido

---

#### 10. `consultoria-seo-local/` não aparece no menu principal

**O problema:** A página `/consultoria-seo-local/` é importante para a keyword "consultoria SEO local" mas não está acessível pelo menu — só por links internos nos cards da home. Isso reduz a autoridade de linkagem interna da página.  
**Ação:** Avaliar adicionar "Consultoria SEO Local" como item do menu, ou criar um link destacado no footer além do já existente.  
**Tipo:** Trabalho médio (decisão de arquitetura de navegação)

---

#### 11. LinkedIn não listado nos canais de contato

**O problema:** O footer e a página de Contato listam WhatsApp, email e Instagram, mas não LinkedIn. Para um consultor B2B que atende donos de clínicas, o LinkedIn é canal relevante de prospecção e prova social.  
**Ação:** Adicionar LinkedIn no footer, na página Sobre e na página Contato.  
**Tipo:** Ganho rápido

---

#### 12. Nenhuma indicação de faixa de preço ou pacotes no site

**Contexto:** O concorrente SEOMais exibe "projetos locais a partir de R$ 2.500/mês". Outros consultores do mercado também mostram alguma referência de investimento.  
**Observação:** Isso é uma decisão estratégica, não um erro. Não mostrar preço pode ser intencional para qualificar os contatos pelo diagnóstico. Mas ausência total de referência de valor pode fazer alguns clientes abandonarem sem entrar em contato — especialmente os que comparam preços antes de qualquer conversa.  
**Ação:** Avaliar se vale adicionar uma faixa indicativa ("investimento a partir de R$X/mês") ou uma seção de "para quem é e para quem não é" que ajude a pré-qualificar sem revelar preço exato.  
**Tipo:** Decisão estratégica (não necessariamente correção)

---

## Análise comparativa com concorrentes locais (via Exa)

| Concorrente | Ponto forte | Ponto fraco vs. Renan |
|---|---|---|
| **Leandro Coutinho** (agenciacoutinho.com.br) | Foco em GMB, simples e direto | Não especializado em clínicas, site mais simples |
| **Luís Cláudio — Brainstorm** (brainstormmarketingdigital.com.br) | Tem endereço físico completo (Setor Sudoeste), posicionamento "high-end" | Genérico — não foca em saúde, sem cases documentados |
| **Antônio Bastos** (antonioseo.com.br) | Presença no Google para "consultor SEO Goiânia" | SEO geral, sem nicho em clínicas, sem cases locais visíveis |
| **SEOMais** (seomais.com.br) | Agência com equipe, preços visíveis, cobertura regional ampla | É agência (não individual), sem especialidade em saúde |

**Diferencial competitivo do Renan:** é o único com especialização clara em clínicas de saúde + cases documentados com métricas reais + design profissional. Isso é difícil de copiar rapidamente. O risco principal é algum concorrente genérico começar a publicar conteúdo sobre clínicas e ocupar posições nas páginas pilares.

---

## As 5 ações de MAIOR impacto — em ordem de prioridade

| # | Ação | Impacto | Dificuldade |
|---|---|---|---|
| 1 | **Corrigir `logo.png` no schema** — substituir por `assets/img/logo-rcb-seo-local.png` em todos os arquivos | Alto (schema quebrado no Google) | Ganho rápido |
| 2 | **Adicionar endereço físico completo** no schema e footer (rua/número/CEP) | Alto (sinal de NAP local — vantagem direta no Local Pack) | Ganho rápido |
| 3 | **Padronizar Google Fonts nas subpáginas** — usar o padrão não-bloqueante da home, remover weight 300 | Médio (melhora Core Web Vitals nas subpáginas) | Ganho rápido |
| 4 | **Publicar mais artigos no blog** — pelo menos 1 por mês, priorizando perguntas dos clientes | Alto a longo prazo (constrói autoridade, E-E-A-T e tráfego informacional) | Trabalho maior (contínuo) |
| 5 | **Criar og:image adequada (1200×628px)** para as páginas que usam o logo como imagem social | Médio (melhora CTR quando links são compartilhados em redes sociais) | Trabalho médio (criação de asset) |

---

*Auditoria gerada em 30/05/2026. Nenhum arquivo do site foi modificado — este é apenas o diagnóstico.*
