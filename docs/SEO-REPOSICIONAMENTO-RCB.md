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
| `/diagnostico-gratuito/` | **DEPOIS** (decisão de renomear) | Ver §4.3 — tendência: renomear para `/diagnostico-presenca-digital/` com 301. |
| `/diagnostico-gratuito/exemplo/` | **DEPOIS** (segue o diagnóstico) | Se renomear o pai, este vira `/diagnostico-presenca-digital/exemplo/` com 301. |
| `/automacao-de-processos/` | **MANTER** (rebaixada) | Diferencial secundário, fora do menu principal. |
| `/cases/` | **MANTER** | Prova social (1 case hoje). |
| `/para-advogados/` | **DEPOIS** (manter vs. `/seo-para-advogados/`) | Recomendação em §4.3. Por ora mantida. |
| `/para-comercios-locais/` | **MANTER** | Hub de nicho não-saúde. |
| `/para-profissionais-liberais/` | **MANTER** | Hub de nicho não-saúde. |
| `/seo-para-clinicas/` · `/seo-para-dentistas/` · `/seo-para-clinicas-de-estetica/` · `/seo-para-medicos/` · `/seo-para-clinicas-de-emagrecimento/` | **MANTER** | Nichos de saúde — fortalecer na ONDA 5. |
| `/sobre/` · `/contato/` · `/privacidade/` · `/cookies/` · `/blog/` + artigos | **MANTER** | — |

### 4.2 Páginas-dinheiro a CRIAR (ONDA 2)

| Nova URL | Papel | Liga-se a |
|----------|-------|-----------|
| `/google-perfil-empresa/` | Página genérica de Google Perfil da Empresa (universal) | ↔ `/google-meu-negocio-para-clinicas/` (aplicação em clínica) |
| `/site-otimizado-para-seo/` (URL preferida; alternativa `/criacao-de-sites-seo/`) | Página genérica de site como ativo de ranqueamento | ↔ `/site-para-clinica/` (aplicação em clínica) |
| `/auditoria-seo/` | Vender auditoria técnica/estratégica (indexação, Search Console, sitemap, robots) | captura "por que meu site não aparece no Google" |
| `/conteudo-para-seo/` | Vender conteúdo/clusters/blog estratégico (serviço S4) | hub do cluster de conteúdo |
| `/acompanhamento-seo/` | Vender continuidade mensal | menciona automação como upsell |
| `/diagnostico-presenca-digital/` *(se aprovado em §4.3)* | Porta de conversão principal | substitui/renomeia `/diagnostico-gratuito/` |

> **Decisão de URL do site genérico:** preferir `/site-otimizado-para-seo/` por bater melhor com a
> intenção de busca ("site otimizado para SEO") e ter menor risco de canibalizar `/site-para-clinica/`.

### 4.3 Decisões adiadas (precisam do seu OK antes de executar)

**A) `/diagnostico-gratuito/` → `/diagnostico-presenca-digital/`?**
Recomendação: **renomear com 301** (criar a nova, redirecionar a antiga), porque "diagnóstico de
presença digital" é mais profissional, mais claro e menos "isca grátis". Antes de executar, será
apresentado o pacote completo: está no sitemap (sim), links internos que apontam para ela (vários
CTAs na home e no rodapé de todas as páginas), tratamento de `/exemplo/`, linha do `_redirects` e
lista de links a atualizar. **Não executado na ONDA 1.**

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

## 7. Próximos passos (ONDA 2)

1. Aprovar o mapa de URLs (§4.2 e §4.3), em especial a renomeação do diagnóstico.
2. Criar as páginas-dinheiro: `/google-perfil-empresa/`, `/site-otimizado-para-seo/`,
   `/auditoria-seo/`, `/conteudo-para-seo/`, `/acompanhamento-seo/` (e `/diagnostico-presenca-digital/`
   se aprovado).
3. Atualizar menu (adicionar dropdown "Serviços" com as novas páginas), sitemap, canonical,
   breadcrumbs, schema e interlinking.
4. Atualizar `ROTEIRO-CONTEXTO.md` para refletir o eixo amplo.

---

*Documento de planejamento e registro. A ONDA 1 alterou a home e o menu; nenhum commit foi feito.*
