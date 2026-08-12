# HANDOFF SEO — 12/08/2026

Memória operacional para a próxima sessão. Leia isto antes de qualquer coisa.

---

## Estado atual

- **Branch:** `main`, limpo, sincronizado com `origin`.
- **Produção:** Cloudflare Pages, deploy automático a cada `git push origin main`.
  Domínio `rcbseo.com.br`. Projeto no painel: `site-consultoria-59m`.
- **Páginas:** 307 HTML no disco · **305 URLs no sitemap** (fora: `/404.html` e
  `/diagnostico-presenca-digital/exemplo/`, ambas de propósito).

### Commits desta sessão (11–12/08/2026)

| Hash | O quê |
|---|---|
| `285629d` | Bloco 1 técnico — scripts perigosos, conferidor de preço endurecido, contraste WCAG |
| `392abff` | Bloco 2 técnico — `<head>` reorganizado (307 pág.), honeypot, 5 headers de segurança |
| `c542d7a` | Arquitetura — redistribuição de links internos por intenção (211 arquivos) |
| `f0ceb8c` | Canibalização — donos de intenção comercial definidos |

Os quatro estão publicados em produção.

---

## Diagnóstico estrutural (medido, não estimado)

- **199 páginas de cidade** em `/consultoria-seo/<slug>/` — 65% do site inteiro.
- **89,5% de texto idêntico** entre duas cidades quaisquer (diff palavra a palavra,
  Aracaju × Botucatu). 63% dos blocos se repetem em 90%+ das páginas. O que muda:
  nome da cidade, sigla do estado e **quatro números**.
- Isso se encaixa na definição de **página-porta** do Google. É o maior passivo do site.
- **Expansão CONGELADA.** A trava `RCB_EXPANDIR_CIDADES` bloqueia as 182 cidades restantes
  do SITE-DADOS. O motivo está na docstring de `scripts/gerar-paginas-cidades.py`.
- **Triagem pronta:** `docs/triagem-cidades.md` — **28 manter · 124 reescrever ·
  47 candidatas a `noindex`**, por sinais locais (mercado, aberturas, bairros e ramos
  próprios, saúde no topo, proximidade de GO, links internos).
- ⚠️ **A decisão final de `noindex` depende do Search Console.** Falta exportar
  impressões/cliques/posição por URL de `/consultoria-seo/`. Cidade do grupo C **com**
  impressão sobe; cidade do grupo A **sem** impressão nenhuma desce. Não decidir sem isso.

**Linha de base:** Search Console (3 meses, antes desta sessão) — 1.470 impressões,
8 cliques, **posição média 38,9**. O gargalo é autoridade externa, não qualidade técnica.

---

## Arquitetura: intenção → URL dona

| Intenção | URL dona | Links int. |
|---|---|---:|
| consultor / especialista SEO Goiânia | `/consultor-seo-goiania/` | 16 |
| SEO local Goiânia · aparecer no Maps em Goiânia | `/seo-local-goiania/` | 20 |
| consultoria de SEO local (nacional, sem geo) | `/consultoria-seo-local/` | 249 |
| Google Perfil da Empresa / Google Meu Negócio | `/google-perfil-empresa/` | 242 |
| prova / resultados | `/cases/` | 206 |

`/consultor-seo-goiania/` absorve "especialista SEO Goiânia" e trata "agência SEO Goiânia"
num FAQ comparativo. **A RCB não é agência** — não escrever que é.

As três sobreposições que restam (`como escolher`, `quanto custa`, `como otimizar` + termo)
são consultas com modificador, com SERP própria. **Não são canibalização.**

---

## Alterações já executadas

Links internos editoriais (início da sessão → agora, fora de nav/rodapé/barra):

| URL | Antes | Depois |
|---|---:|---:|
| `/consultoria-seo-local/` | 48 | **249** |
| `/google-perfil-empresa/` | 37 | **242** |
| `/cases/` | 6 | **206** |
| `/seo-local-goiania/` | 11 | **20** |
| `/consultor-seo-goiania/` | 7 | **16** |
| `/diagnostico-presenca-digital/` | 289 | **91** |
| `/cookies/` | 305 | 305 (intocado) |

- **Cidades:** botão do hero passou de `/diagnostico-presenca-digital/` para `/cases/`;
  links contextuais para `/google-perfil-empresa/` e `/consultoria-seo-local/` no método.
  Anchors variam por hash do slug (4 variantes, distribuição 53/52/51/43).
- **Goiânia só em GO/DF.** As 4 cidades de Goiás + Brasília linkam para as páginas de
  Goiânia. As outras 195, não.
- **`/cases/` virou hub:** serviço → case → serviço.
- **Títulos reposicionados:** `/contato/`, `/cases/`, `/blog/`, `/acompanhamento-seo/`
  (também em `og:title` e `twitter:title`, que estavam divergentes do `<title>`).
- **Bloco 2 técnico:** charset primeiro, consentimento garantido antes do GA4, headers de
  segurança (HSTS 1 ano + subdomínios, **sem `preload`**), CSP parcial.
- **Scripts aposentados** em `scripts/deprecated/` (com README): `atualizar-nav-rodape.py`
  e `links-internos-divisao.py`. **Não rodar nenhum dos dois** — escrevem links para URLs
  que hoje respondem 404.

---

## Decisões que NÃO devem ser revertidas

1. **Não criar cidades em massa.** A expansão está congelada por medição, não por cautela.
2. **Não mandar as 199 cidades para as páginas de Goiânia.** Linkar "consultor em Goiânia"
   de uma página de Recife é incoerente e engrossa o footprint programático.
3. **Não usar `nofollow` no link de cookies** para "recuperar PageRank". Desde 2009 o Google
   descarta o valor em vez de redistribuir. Não funciona.
4. **Não recomeçar a auditoria cosmética** (skip links, hierarquia de headings, Lighthouse 100,
   escapes, flags de CLI). Nada disso move ranking com posição média 38,9.
5. **Não confundir palavra compartilhada com canibalização.** Artigo informacional pode e deve
   usar "SEO local". Só é canibalização quando duas páginas disputam a **mesma intenção comercial**.
6. **Foco atual:** ranking, tráfego comercial, autoridade e leads. Não elegância técnica.
7. **IndexNow:** reutilizar sempre a chave `19341b29c6054af601879d85a34d62c5`. **Nunca gerar
   outra.** Enviar só depois de confirmar HTTP 200.
8. **Preço:** fonte única em `scripts/rcb_pacotes.py`. Mexeu no preço? Rode
   `aplicar-conversao.py` → `gerar-paginas-cidades.py` → `atualizar-precos-2026-08-10.py` →
   `conferir-conversao.py`.

---

## PRÓXIMA FASE

> **AUTORIDADE EXTERNA / OFF-PAGE + dados reais de Search Console das páginas programáticas.**

**A. Off-page.** O site tem quase nenhum backlink; nenhum ajuste interno resolve isso.
Ordem sugerida: link dos dois clientes reais (Docevidade e Nalu Prado) → citações locais NAP
→ Google Business Profile ativo → case em LinkedIn/YouTube → imprensa local → niche edits pagos.

**B. Search Console.** Exportar impressões/cliques/posição por URL de `/consultoria-seo/`
para fechar a decisão de `noindex` das cidades.

**Alvos de backlink externo — reavaliar antes de executar.** A ordem que fazia sentido em
12/08: `/cases/`, `/google-perfil-empresa/`, `/seo-para-clinicas/`, `/consultoria-seo-local/`.
As duas páginas de Goiânia ganharam pouca força interna (16 e 20) e só viram bom alvo de
backlink depois de tração própria.

---

## Pendências que a próxima sessão precisa saber

- **Search Console:** o Renan precisa reenviar o `sitemap.xml` (305 URLs, nenhuma nova em
  nenhuma rodada desta sessão).
- **IndexNow não foi enviado nesta sessão.** O conteúdo mudou em ~310 páginas, mas nenhuma URL
  foi criada nem removida. Enviar as 305 do sitemap é opcional e seguro.
- **CNPJ e razão social no rodapé:** pendente desde 09/08. O Renan ainda não passou o número.
  **Não colocar CNPJ falso no ar.**
- **`/consultoria-seo/palmas/` é órfã e o gerador não a produz.** Causa descoberta em 12/08:
  existem **Palmas/TO e Palmas/PR** nos dados; o gerador desambigua para `palmas-to` e
  `palmas-pr`, e nenhuma casa com a pasta `palmas/` publicada. Recebe manutenção manual.
- **Case Nalu Prado é música ao vivo para eventos** (coral, orquestra), **não estética**.
  Um relatório anterior desta sessão errou isso.
- **Case Docevidade:** as **312 avaliações são da concorrente Richesse**. A Docevidade tem 4.
  O número verdadeiro é o mais forte: 1º no Maps para "macarrons Goiânia" com 4 avaliações,
  à frente de concorrentes com 47 e 312.
- **Cloudflare devolve 403 para o user-agent padrão do `urllib`.** Use `curl` ou mande
  user-agent de navegador ao conferir o site por script.
- **FAQ duplica texto no JSON-LD.** Ao editar resposta de FAQ, alterar HTML **e** schema — e
  ancorar sempre na versão com `</p>`, senão o replace atinge o schema.
- **CRLF e LF misturados** (106 e 201 arquivos). Preserve com `newline=""` ao reescrever.

---

## Referência no repositório

- `CLAUDE.md` — histórico completo, rodada por rodada.
- `docs/triagem-cidades.md` — as 199 cidades classificadas.
- `scripts/deprecated/README.md` — por que cada script aposentado não pode rodar.
- `scripts/conferir-conversao.py` — **rodar antes de qualquer publicação.**
