# Reposicionamento SEO — RCB Consultoria

> **O que é este documento.** Registro das decisões estratégicas do reposicionamento do site
> da RCB e o mapa de URLs (manter / criar / renomear / consolidar / deixar para depois).
> Serve de referência para todas as ondas de execução.
>
> **Data desta versão:** 23 de junho de 2026 · **Mantido por:** Renan + Claude Code
> **Documentos irmãos:** `ROTEIRO-CONTEXTO.md` (mapa de intenções) · `AUDITORIA-CONSULTORIA.md` (auditoria técnica de 30/05/2026).

---

## 1. Decisão do eixo

**Eixo amplo, com saúde como nicho mais maduro.**

- O site deixa de se posicionar como consultoria **vertical em saúde** e passa a se posicionar como
  consultoria de **SEO local e presença digital para negócios locais e profissionais de serviço**
  que querem aparecer melhor no Google, melhorar o Google Perfil da Empresa, organizar o site para
  ranquear e receber mais contatos pelo WhatsApp/orçamento.
- **Saúde não é diluída nem descartada.** Clínicas, dentistas, estética, médicos e emagrecimento
  continuam como o nicho mais forte e maduro — agora apresentados como *aplicações do método*,
  não como o único posicionamento.
- **Home, menu e páginas-dinheiro** são amplos, organizados por **intenção de busca e problema do
  cliente** (aparecer no Google / no Maps, melhorar o Perfil da Empresa, site que não aparece,
  gerar contatos pelo WhatsApp).
- **Novos nichos** entram com cuidado, sem páginas rasas. Prioridade futura: empresas locais,
  prestadores de serviço, contadores, manutenção/reformas/instalação, advogados, oficinas/automotivo,
  segurança eletrônica, pet/veterinárias.

## 2. Decisão sobre Automação (n8n / IA)

**Automação deixa de ser eixo principal.** Vira **diferencial complementar e upsell operacional**:
"depois que o SEO começa a gerar demanda, a RCB também pode ajudar a organizar leads, planilhas,
relatórios e acompanhamentos". Onde aparece: bloco secundário na home, futura página de
acompanhamento SEO e diagnóstico. **Não** vira cluster nem item de destaque no menu principal.
A página `/automacao-de-processos/` é **preservada** (sem exclusão).

## 3. Regra de naming — "Google Meu Negócio" × "Google Perfil da Empresa"

- O nome oficial atual é **Google Perfil da Empresa** (antigo Google Meu Negócio). O texto novo
  usa "Google Perfil da Empresa" como nome principal e menciona "(antigo Google Meu Negócio)".
- **Exceção de SEO:** o termo "Google Meu Negócio" ainda tem muito volume de busca no Brasil, então
  é mantido propositalmente em **title tags, URLs já indexadas e rótulos de menu** para não perder
  tráfego. A troca de URL para `/google-perfil-empresa/` é feita criando uma **página nova**
  (ver mapa de URLs), sem renomear a página de clínica.

---

## 4. Mapa de URLs

Legenda: **MANTER** (URL e papel preservados) · **CRIAR** (página nova) · **RENOMEAR 301** (URL nova + redirect) ·
**CONSOLIDAR** · **DEPOIS** (decisão adiada).

### 4.1 Páginas atuais — o que fazer com cada uma

| URL atual | Decisão | Observação |
|-----------|---------|------------|
| `/` (home) | **MANTER + reposicionar** | Feito na ONDA 1 (eixo amplo + saúde como nicho). |
| `/consultoria-seo-local/` | **MANTER** = página-mãe do serviço SEO local | Papel: hub de venda de SEO local. |
| `/consultor-seo-goiania/` | **MANTER** = página local/profissional | Papel: "consultor SEO em Goiânia" (pessoa/cidade). |
| `/seo-local-goiania/` | **MANTER** = página local da solução na cidade | Papel: "SEO local Goiânia" (serviço na cidade). |
| `/google-meu-negocio-para-clinicas/` | **MANTER** (ativo de saúde) | NÃO transformar em genérica. Vai linkar para a futura `/google-perfil-empresa/` e vice-versa. |
| `/site-para-clinica/` | **MANTER** (ativo de saúde) | NÃO transformar em genérica. Vira aplicação da futura página genérica de site. |
| `/diagnostico-gratuito/` | ✅ **RENOMEADO 301** → `/diagnostico-presenca-digital/` (ONDA 2B) | Reposicionado como "Diagnóstico de Presença Digital". Redirect 301 no `_redirects`. |
| `/diagnostico-gratuito/exemplo/` | ✅ **MOVIDO 301** → `/diagnostico-presenca-digital/exemplo/` (ONDA 2B) | Página `noindex`, movida junto via `git mv`. |
| `/automacao-de-processos/` | **MANTER** (rebaixada) | Diferencial secundário, fora do menu principal. |
| `/cases/` | **MANTER** | Prova social (1 case hoje). |
| `/para-advogados/` | **DEPOIS** (manter vs. `/seo-para-advogados/`) | Recomendação em §4.3. Por ora mantida. |
| `/para-comercios-locais/` | **MANTER** | Hub de nicho não-saúde. |
| `/para-profissionais-liberais/` | **MANTER** | Hub de nicho não-saúde. |
| `/seo-para-clinicas/` · `/seo-para-dentistas/` · `/seo-para-clinicas-de-estetica/` · `/seo-para-medicos/` · `/seo-para-clinicas-de-emagrecimento/` | **MANTER** | Nichos de saúde — fortalecer na ONDA 5. |
| `/sobre/` · `/contato/` · `/privacidade/` · `/cookies/` · `/blog/` + artigos | **MANTER** | — |

### 4.2 Páginas-dinheiro a CRIAR (ONDA 2)

> ✅ **ONDA 2A executada:** `/auditoria-seo/`, `/google-perfil-empresa/`, `/site-otimizado-para-seo/`,
> `/conteudo-para-seo/` e `/acompanhamento-seo/` criadas. ✅ **ONDA 2B executada:**
> `/diagnostico-presenca-digital/` (renomeação do diagnóstico). Pendente: wiring no menu global
> (dropdown "Serviços") + interlinking a partir das páginas antigas (home/rodapé) — ONDA 3.

| Nova URL | Papel | Liga-se a |
|----------|-------|-----------|
| `/google-perfil-empresa/` | Página genérica de Google Perfil da Empresa (universal) | ↔ `/google-meu-negocio-para-clinicas/` (aplicação em clínica) |
| `/site-otimizado-para-seo/` (URL preferida; alternativa `/criacao-de-sites-seo/`) | Página genérica de site como ativo de ranqueamento | ↔ `/site-para-clinica/` (aplicação em clínica) |
| `/auditoria-seo/` | Vender auditoria técnica/estratégica (indexação, Search Console, sitemap, robots) | captura "por que meu site não aparece no Google" |
| `/conteudo-para-seo/` | Vender conteúdo/clusters/blog estratégico (serviço S4) | hub do cluster de conteúdo |
| `/acompanhamento-seo/` | Vender continuidade mensal | menciona automação como upsell |
| `/diagnostico-presenca-digital/` *(se aprovado em §4.3)* | Porta de conversão principal | substitui/renomeia `/diagnostico-gratuito/` |
| `/guia-seo-local/` | Hub/índice editorial (não é página de serviço) que organiza por tema os conteúdos do blog e aponta para as páginas-dinheiro — criado na **ONDA 4C** | ↔ `/blog/` (8 clusters por âncora) e as 7 páginas-dinheiro |

> **Decisão de URL do site genérico:** preferir `/site-otimizado-para-seo/` por bater melhor com a
> intenção de busca ("site otimizado para SEO") e ter menor risco de canibalizar `/site-para-clinica/`.

> **Nota (atualização):** o `/guia-seo-local/` foi criado na ONDA 4C como hub/índice editorial, não
> como página de serviço, e está fora do menu principal por ora (link no topo do `/blog/` e no rodapé
> das 7 páginas-dinheiro). O histórico detalhado das ondas de conteúdo (3A–3I) e de organização
> interna (4A–4E-1) está no `ROTEIRO-CONTEXTO.md`.

### 4.3 Decisões adiadas (precisam do seu OK antes de executar)

**A) `/diagnostico-gratuito/` → `/diagnostico-presenca-digital/`?** ✅ **EXECUTADO na ONDA 2B.**
Pasta renomeada via `git mv` (index + `/exemplo/`). Redirects 301 no `_redirects` (4 linhas,
incluindo `*`/`:splat`). Todos os `href="/diagnostico-gratuito/"` (159) trocados, link de `/exemplo/`
ajustado, `sitemap.xml` e `llms.txt` atualizados, página reposicionada como "Diagnóstico de Presença
Digital" (análise inicial e gratuita). Rótulo do menu mantido como "Diagnóstico gratuito" (apelo de
conversão), apontando para a nova URL.

**B) `/para-advogados/` → `/seo-para-advogados/`?**
Três opções: (A) manter `/para-advogados/`; (B) criar `/seo-para-advogados/` + 301; (C) apenas
ajustar title/H1/conteúdo da URL atual. Recomendação inicial: **(C) por ora** (ajustar on-page),
e avaliar (B) só quando houver cluster de apoio para advogados. **Não executado na ONDA 1.**

**C) Trio local (`/consultoria-seo-local/`, `/consultor-seo-goiania/`, `/seo-local-goiania/`).**
Papéis definidos em §4.1 para evitar canibalização. Se a sobreposição persistir, ajustar
títulos/metas/canonical antes de pensar em consolidação. **Sem redirecionamento sem aprovação.**

---

## 5. Riscos de canibalização monitorados

1. **Trio "SEO local Goiânia"** — três páginas próximas; mitigado por papéis distintos (§4.1).
2. **Diagnóstico** — criar nova URL sem 301 canibalizaria a atual; por isso a regra é renomear com 301.
3. **Advogados** — `/para-advogados/` vs. `/seo-para-advogados/`; não criar duplicata.
4. **GBP e Site genéricos × recortes de clínica** — mitigado com interlinking explícito
   (genérica = método; clínica = aplicação), canonical próprio em cada uma.
5. **Artigos "consultor x agência x sozinho"** — já há 4 peças muito próximas; não adicionar mais
   sem consolidar.

---

## 6. O que foi feito na ONDA 1 (reposicionamento estrutural)

**Arquivos alterados:** `index.html` (home) + menu global em 38 páginas + este documento.

- **Home (`index.html`):**
  - Hero: nova headline ("Faça sua empresa aparecer melhor no Google e receba mais contatos pelo
    WhatsApp") e subheadline ampla; "paciente" → "cliente".
  - Dor: "Seu cliente procura no Google, mas encontra seus concorrentes?".
  - Solução: serviços apresentados de forma ampla; "Google Meu Negócio" → "Google Perfil da Empresa
    (antigo Google Meu Negócio)".
  - Nichos: reposicionados como aplicações do método; saúde declarada como nicho mais maduro;
    adicionados cards de comércios locais, profissionais liberais e advogados.
  - Automação: rebaixada de seção principal para **diferencial complementar / upsell operacional**.
  - FAQ ajustado (visível + schema JSON-LD espelhado).
  - Schema `LocalBusiness`/`ProfessionalService`: descrição ampliada.
- **Menu global (38 páginas):** versão ampla e segura — apenas links de páginas existentes.
  Automação saiu do topo (rebaixada, permanece no rodapé). Adicionado "Consultoria SEO Local".
  Dropdown "SEO e Site" virou "Nichos" com saúde + não-saúde.

**Não feito na ONDA 1 (de propósito):** nenhum redirect, nenhuma exclusão de URL, nenhuma página
nova, nenhum commit, nenhum push. As páginas-dinheiro novas e a renomeação do diagnóstico ficam
para a ONDA 2 — assim o menu é reescrito uma única vez já apontando para páginas reais.

## 7. Histórico de execução das ondas

| Onda | Commit | O que entrou |
|------|--------|--------------|
| ONDA 1 | `076ead5` | Reposiciona home e menu (eixo amplo, saúde como nicho) |
| ONDA 2A | `a1825c4` | 5 páginas-dinheiro de serviço |
| ONDA 2B | `750e1cd` | Renomeia diagnóstico → `/diagnostico-presenca-digital/` com 301 |
| ONDA 2C | `f5c1286` | Menu "Serviços", rodapé e interlinking das páginas-dinheiro |
| ONDA 2D | *(docs)* | Atualiza `ROTEIRO-CONTEXTO.md` (eixo amplo) e este checklist |

**Push/deploy:** feito em 23/06/2026 (`b6dd007..f5c1286 → main`). Cloudflare Pages publicou sem erro.

## 8. Checklist pós-deploy (validado em produção — 23/06/2026)

### 8.1 URLs novas publicadas (todas 200 em produção)
- `/diagnostico-presenca-digital/` · `/diagnostico-presenca-digital/exemplo/`
- `/auditoria-seo/` · `/google-perfil-empresa/` · `/site-otimizado-para-seo/`
- `/conteudo-para-seo/` · `/acompanhamento-seo/`

### 8.2 Redirects 301 confirmados em produção
- `/diagnostico-gratuito/` → `/diagnostico-presenca-digital/` ✅ 301
- `/diagnostico-gratuito/exemplo/` → `/diagnostico-presenca-digital/exemplo/` ✅ 301
- Regras no `_redirects` (Cloudflare Pages): mãe com/sem barra + `/exemplo/` + `*`/`:splat`.

### 8.3 Sitemap / llms / links
- `sitemap.xml`: 6 URLs novas presentes; antiga `/diagnostico-gratuito/` removida. ✅
- `llms.txt`: atualizado com as páginas-dinheiro e a nova URL do diagnóstico. ✅
- Links internos: **0 quebrados** (2.183 verificados em 45 páginas).

### 8.4 Ações pendentes no Google Search Console (fazer quando possível)
- [ ] **Inspecionar e solicitar indexação** de `/diagnostico-presenca-digital/` e das 5 páginas-dinheiro novas.
- [ ] **Inspecionar `/diagnostico-gratuito/`** para confirmar que o Google registra o **301**.
- [ ] **Reenviar o sitemap** (`https://rcbseo.com.br/sitemap.xml`) para acelerar a descoberta.
- [ ] Acompanhar, nas semanas seguintes, se a URL antiga sai do índice e a nova entra.

### 8.5 Próximos passos (ONDA 3 — conteúdo)
1. Produzir o **primeiro lote** de artigos amplos/comerciais (ver `ROTEIRO-CONTEXTO.md` §5).
   Lote inicial recomendado: #1 "Por que minha empresa não aparece no Google?", #2 "Como aparecer
   no Google Maps?", #4 "Por que meu site não aparece no Google?", #8 "Site ou Instagram para
   empresa local?".
2. **Resolver canibalização de preço:** ampliar `/blog/quanto-custa-consultoria-seo-local/` como
   genérico em vez de criar um post novo de "quanto custa SEO local".
3. Interligar cada novo artigo à sua página-dinheiro (hub do cluster) + diagnóstico/contato.
4. (Opcional, cosmético) Padronizar os dois `id="diagnostico-gratuito"` (âncoras de seção em
   `/para-comercios-locais/` e `/para-profissionais-liberais/`) para `id="cta-diagnostico"`.

---

*Documento de planejamento e registro. Reflete o estado publicado em produção em 23/06/2026.*
