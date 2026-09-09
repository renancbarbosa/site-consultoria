# Auditoria SEO + GEO + AIO — rcbseo.com.br

**Data:** 08/09/2026 · **Nota geral: 78,5 / 100**

**Medido, não estimado.** Toda linha deste relatório vem de uma medição feita hoje: 318 páginas
lidas uma a uma, Search Console real (28 dias), Lighthouse em duas execuções, navegador de verdade
com rede e processador lentos, e verificação do site no ar.

---

## O que este relatório NÃO faz

Três itens do pedido original foram recusados, e o motivo importa mais que o item:

1. **Não publiquei a "Pesquisa: analisamos 500 sites de Goiânia, 73%…".** Esses números não existem.
   Publicar dado inventado como pesquisa própria é o caminho mais rápido para destruir a autoridade
   que a auditoria inteira tenta construir — basta uma pessoa pedir a metodologia.
2. **Não escrevi "reduza no-show em 40%" nem "aumente vendas em 70%".** Contradiz a política que
   você mesmo fixou para a linha de Agentes de IA (nenhum resultado prometido) e é promessa sobre
   algo que você não controla.
3. **Não editei a Wikipedia para citar a RCB.** É conflito de interesse explícito nas regras deles;
   o resultado prático é reversão e um registro público ruim ligado ao seu domínio.

E um item **não pôde ser medido**: o **Share of Model** (item 27, 5 pontos). Eu não tenho acesso ao
ChatGPT, Perplexity ou Gemini para rodar os 30–50 prompts. O protocolo está no fim deste documento,
pronto para você executar. Ele conta como 0 na nota — não porque o site falhou, mas porque não foi
medido. **Sem esse item, a base seria 95 pontos e o site faria 78,5 de 95 (82,6%).**

---

## Resumo em uma página

| Bloco | Nota | Leitura |
|---|---|---|
| 1. Técnico | **21 / 25** | Sólido. O único buraco é velocidade. |
| 2. On-page | **21,5 / 25** | O melhor bloco. Rodadas anteriores resolveram quase tudo. |
| 3. GEO / AIO | **17,5 / 25** | Schema exemplar; falta autoridade externa e medição. |
| 4. E-E-A-T | **10,5 / 15** | Trava aqui: presença fora do site é quase zero. |
| 5. Conversão | **8 / 10** | Bom, menos a velocidade. |

**O site está tecnicamente bem-feito e comercialmente invisível.** Em 28 dias (10/08 a 06/09):
**2.482 impressões, 14 cliques, posição média 31,0** — e a posição vem melhorando de verdade
(era 39,2 em maio, 33,9 em agosto). O gargalo não é o que está escrito nas páginas; é que quase
ninguém chega até elas.

---

## O achado que muda uma decisão

As **três consultas mais bem posicionadas do site inteiro** apontam para páginas que **não existem
mais**:

| Consulta | Impressões | Posição | Situação da página |
|---|---|---|---|
| `link building para bets` | 52 | **22,2** | 404 desde 08/08 |
| `migração de domínios` | 33 | **24,5** | 404 desde 08/08 |
| `recuperação de nome de domínio registrado por terceiros` | 31 | **27,6** | 404 desde 08/08 |
| `leilão de domínios registro br` | 2 | **3,0** | 404 — **e rendeu 1 dos 14 cliques** |

Compare com o resto do site: "aparecer no google" está em **49,8**, "como aparecer no google" em
**57,0**, "seo para advogados" em **60,2**.

Ou seja: **o conteúdo que chegou mais perto da primeira página foi justamente o que foi retirado
do ar em 08/08** — a divisão de mercados competitivos (IPTV, bets, domínios expirados). Um dos dois
cliques identificáveis do período veio de lá.

**Isto não é uma recomendação de republicar bets e IPTV.** A decisão de tirar foi de posicionamento
de marca, e posicionamento é sua alçada, não do Google. Mas a decisão foi tomada sem esse número na
mesa, e agora ele existe. Vale considerar o recorte que sobra: **o cluster de domínios** (`migração
de domínios`, `recuperação de nome de domínio`, `leilão de domínios`) não tem nada a ver com bets
nem com IPTV, não carrega risco jurídico ou reputacional, e é onde estão a melhor posição e o único
clique de cauda longa do site. O texto das páginas está preservado em `scripts/conteudo/` e o
histórico em `2507c42`.

---

## Bloco 1 — Técnico (21 / 25)

| # | Item | Peso | Status | Evidência medida |
|---|---|---|---|---|
| 1 | robots.txt permite crawlers de IA | 3 | ✅ **3** | GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended e CCBot todos com `Allow: /` |
| 2 | llms.txt na raiz | 2 | ✅ **2** | `/llms.txt` **e** `/llms-full.txt`, ambos HTTP 200 |
| 3 | Sitemap válido e enviado | 3 | ⚠️ **2** | XML válido, 150 URLs, referenciado no robots.txt. Falta você reenviar no Search Console |
| 4 | HTTPS sem mixed content | 2 | ✅ **2** | HSTS `max-age=31536000; includeSubDomains` |
| 5 | Canonical correta | 2 | ✅ **2** | 150 de 150 páginas indexáveis |
| 6 | Redirects 301 | 2 | ✅ **2** | `http://` → `https://` e `www` → raiz, ambos 301, sem cadeia |
| 7 | 404 tratada | 2 | ✅ **2** | Status 404 correto + página customizada com título e H1 |
| 8 | Sem noindex acidental | 3 | ✅ **3** | 168 páginas em noindex — todas cidades podadas de propósito |
| 9 | **Core Web Vitals no verde** | 4 | ❌ **1** | **LCP 4,3s e 5,2s** em duas medições (limite 2,5s). CLS 0,029 ✅, TBT 60ms ✅ |
| 10 | Mobile-first | 2 | ✅ **2** | Conferido em 390, 500, 700, 900, 1024 e 1366px: sem rolagem horizontal |

### O problema de velocidade, em detalhe

**Só o LCP reprova** — CLS e capacidade de resposta estão bons. (A primeira execução do Lighthouse
deu CLS 0,391, mas a segunda deu 0,029 e o navegador real deu 0 mesmo com rede e processador
lentos; o 0,391 foi ruído da medição simulada, não um defeito.)

Três causas, medidas:

1. **`styles.css` trava a pintura por 586 ms.** São 96 KB em disco, com ~12 KB de regras que a home
   não usa e ~5 KB recuperáveis só com minificação.
2. **A foto do topo pesa 72 KB.** O `.webp` já é servido corretamente via `<picture>`, com `width`,
   `height` e `fetchpriority="high"` — isso está certo. O problema é que ela é **1122 × 1402 px** e
   aparece bem menor no celular: **66 KB de desperdício**.
3. **O gtag do Google traz 170 KB, dos quais 71 KB nunca são usados.** É código de terceiro; não dá
   para enxugar, só para carregar mais tarde.

> Verifiquei uma quarta hipótese e ela estava **correta**: a fonte Inter aparece três vezes no
> `<head>`, mas a terceira está dentro de `<noscript>`. O carregamento de fonte está bem feito.

---

## Bloco 2 — On-page (21,5 / 25)

Este é o bloco mais forte, e é resultado direto das rodadas de 18/07 e 08/08.

| # | Item | Peso | Status | Evidência |
|---|---|---|---|---|
| 11 | Title única, keyword no início | 3 | ✅ **3** | **150 de 150** únicas, todas dentro de 65 caracteres, zero duplicada |
| 12 | Description única, 150–160 | 2 | ⚠️ **1,5** | Zero duplicada; **2 acima de 160**: `/agente-de-ia-para-clinicas/` e `/recuperacao-de-vendas-whatsapp/` |
| 13 | H1 único | 2 | ✅ **2** | 150 de 150 com exatamente um H1 |
| 14 | Hierarquia de headings | 2 | ⚠️ **1** | Lighthouse acusa `heading-order` na home: níveis fora de ordem |
| 15 | Slug curta e descritiva | 2 | ✅ **2** | Todas legíveis, com o termo, sem parâmetros |
| 16 | Keyword primária mapeada | 3 | ✅ **3** | Auditoria semântica de 08/08 cobriu as 307 páginas |
| 17 | **Answer-first (≤70 palavras)** | 4 | ⚠️ **3** | **39 de 150** abrem com mais de 70 palavras antes de responder |
| 18 | Densidade natural | 2 | ✅ **2** | Sem stuffing |
| 19 | **Links internos** | 3 | ⚠️ **2** | **36 páginas recebem menos de 3 links internos** — quase todas do blog |
| 20 | Alt text | 2 | ✅ **2** | **Zero** imagens sem alt em 150 páginas |

---

## Bloco 3 — GEO / AIO (17,5 / 25)

| # | Item | Peso | Status | Evidência |
|---|---|---|---|---|
| 21 | Blocos citáveis com dados próprios | 4 | ⚠️ **3** | As 199 páginas de cidade usam dados públicos de CNPJ da Receita já processados — isso **é** dado próprio e citável. Falta no blog |
| 22 | FAQ com schema | 3 | ✅ **3** | **142 de 150** com `FAQPage` real |
| 23 | Schema completo | 4 | ✅ **4** | JSON-LD **válido em 318 de 318**. Presentes: LocalBusiness (61), Service (69), Offer (65), BlogPosting (78), Person (106), BreadcrumbList (145), FAQPage (142) |
| 24 | Entidades claras | 3 | ✅ **3** | Nome, fundador, endereço, telefone, e-mail, `sameAs`, formação — tudo no grafo |
| 25 | Listas e tabelas | 2 | ✅ **2** | 150 de 150 têm ao menos uma |
| 26 | **Fontes externas confiáveis** | 2 | ❌ **0,5** | **110 de 150 páginas não citam nenhuma fonte de autoridade.** Só as de nicho têm (CFM, CFO, OAB, ANVISA) |
| 27 | **Share of Model** | 5 | ⛔ **0** | **Não medido** — sem acesso às IAs. Protocolo no fim |
| 28 | How-to passo a passo | 2 | ✅ **2** | Vários artigos em passos numerados |

**Leitura honesta deste bloco:** a parte que depende de *código* está praticamente perfeita — o
schema é melhor que o da maioria dos sites de agência. A parte que falta é a que depende de
*reputação*: as IAs citam quem outras fontes citam, e a RCB quase não é citada em lugar nenhum.

---

## Bloco 4 — E-E-A-T (10,5 / 15) — **é aqui que o site trava**

| # | Item | Peso | Status | Evidência |
|---|---|---|---|---|
| 29 | Página Sobre detalhada | 3 | ⚠️ **2,5** | 1.181 palavras, schema `Person`, mas **uma única foto** |
| 30 | Autores identificados | 2 | ⚠️ **1,5** | **77 de 77** artigos com `author` no schema e assinatura visível — mas **nenhum com foto do autor** |
| 31 | Prova social | 3 | ✅ **3** | `/cases/` com 3.014 palavras; 3 depoimentos reais na home com schema `Review` |
| 32 | **Presença em fontes externas** | 4 | ❌ **1** | **O `sameAs` do site inteiro tem um único perfil: o LinkedIn.** Nenhum diretório, nenhuma notícia, nenhum guest post |
| 33 | Atualização visível | 2 | ⚠️ **1,5** | **38 de 150** sem `dateModified` |
| 34 | Transparência | 1 | ✅ **1** | Contato, privacidade, cookies e endereço no rodapé de todas |

---

## Bloco 5 — Conversão / UX (8 / 10)

| # | Item | Peso | Status | Evidência |
|---|---|---|---|---|
| 35 | CTA acima da dobra | 3 | ✅ **3** | Primeiro botão a **487px** numa tela de 844px |
| 36 | Formulário curto | 2 | ✅ **2** | **5 campos** (nome, WhatsApp, tipo de negócio, cidade, pacote) + honeypot invisível |
| 37 | **Carrega em menos de 3s** | 3 | ❌ **1** | FCP 3,1s e LCP 4,3–5,2s no celular simulado |
| 38 | Navegação intuitiva | 2 | ✅ **2** | Menu com dropdowns, breadcrumb em 145 páginas, rodapé completo |

---

## Plano 30-60-90

Ordenado por **retorno dividido por esforço**, não pela ordem do checklist.

### Dias 1–7 — o que dá mais resultado por hora gasta

1. **Minificar o `styles.css`** (~1h, eu faço). Corta boa parte dos 586 ms que travam a pintura.
   É o item de maior impacto no único bloco técnico reprovado.
2. **Gerar a foto do topo em tamanho de tela** (~30 min, eu faço). Economiza 66 KB no carregamento
   mais importante da home.
3. **Corrigir as 2 descriptions acima de 160** e a ordem de headings da home (~30 min, eu faço).
4. **Reenviar o `sitemap.xml`** no Search Console (5 min, **você**).

### Dias 8–21 — conteúdo

5. **Reescrever as 39 aberturas com mais de 70 palavras** para responder na primeira frase. É o
   formato que o AI Overview e o ChatGPT extraem. Eu faço, em lotes, com sua revisão.
6. **Ligar as 36 páginas órfãs do blog** à rede interna (eu faço; o padrão de âncoras variadas já
   existe em `scripts/ligar-criacao-sites.py`).
7. **Adicionar `dateModified` nas 38 páginas que não têm** (eu faço).
8. **Colocar sua foto na assinatura dos 77 artigos** (eu faço; a foto já existe no site).

### Dias 22–60 — a parte que só você pode fazer

9. **Autoridade externa.** É o item de peso 4 com nota 1, e nenhuma linha de código resolve:
   - Diretórios: GuiaMais, Apontador, TeleListas, Solutudo, ACIEG, CDL Goiânia
   - Bing Places e Apple Business Connect (o Google Business Profile já existe)
   - LinkedIn: perfil + página de empresa, com os cases publicados marcando os clientes
   - 2 a 3 guest posts em portais de Goiás ou blogs de gestão de clínica
   - Cada um desses vira um `sameAs` novo no schema, que eu adiciono depois

   **Sem isso, os outros 90 pontos do checklist rendem pouco.** Um site tecnicamente perfeito que
   ninguém cita continua na posição 31.

### Dias 61–90 — medir

10. **Rodar o protocolo de Share of Model** (abaixo) e repetir a auditoria com os mesmos scripts.

---

## Protocolo de Share of Model (para você executar)

Não consigo rodar isso — não tenho acesso ao ChatGPT, Perplexity nem Gemini. Você roda em cerca de
uma hora.

**Passo 1.** Abra uma planilha com as colunas: `prompt`, `IA`, `citou RCB (S/N)`, `URL citada`,
`concorrentes citados`, `tom`.

**Passo 2.** Rode estes 20 prompts em cada uma das 4 IAs (ChatGPT com navegação, Perplexity, Gemini,
Claude). São perguntas de cliente, não de SEO:

1. Qual o melhor consultor de SEO em Goiânia?
2. Quem faz Google Meu Negócio para clínica em Goiânia?
3. Como faço minha clínica aparecer no Google Maps?
4. Quanto custa contratar consultoria de SEO local no Brasil?
5. Vale a pena contratar consultor de SEO ou agência?
6. Como conseguir mais pacientes pelo Google?
7. Empresa que faz site otimizado para SEO em Goiânia
8. Como responder avaliações do Google de uma clínica?
9. Meu Google Meu Negócio não aparece, o que fazer?
10. Agente de IA no WhatsApp para clínica funciona?
11. Como recuperar carrinho abandonado pelo WhatsApp?
12. Quem faz automação de WhatsApp para consultório?
13. Quanto custa otimizar o Google Meu Negócio?
14. SEO para dentista: por onde começar?
15. Como aparecer nas buscas "perto de mim"?
16. Consultoria de SEO para contabilidade, quem faz?
17. RCB Consultoria é confiável?
18. Renan Carvalho Barbosa, consultor de SEO — quem é?
19. Criação de sites em Goiânia: quem indica?
20. Como escolher uma consultoria de SEO local?

**Passo 3.** Share of Model = (vezes que a RCB foi citada ÷ total de respostas) × 100.

**Baseline esperado hoje: perto de 0%.** Não por defeito do site, mas porque as IAs citam quem tem
menção externa — exatamente o item 32, que está com nota 1 de 4. **A meta de 20% em 90 dias do
prompt original é irrealista para um domínio novo sem citações.** Uma meta honesta é **sair de 0% e
chegar a 5–8%**, e isso só acontece se o passo 9 do plano for executado.

---

## Código pronto

**`robots.txt`** — já está correto, nada a mudar. Ele permite os seis crawlers de IA e aponta o
sitemap. (Atenção: o botão "Managed robots.txt" do Cloudflare continua **desligado** de propósito —
ligá-lo bloquearia esses mesmos crawlers.)

**`llms.txt`** — já existe, junto com `llms-full.txt`. Depois do item 9 do plano, acrescentar os
perfis novos.

**Schema** — o do site já é mais completo que o modelo do prompt original. O modelo sugeria
`LocalBusiness` + `Service` + `Article` soltos; o site usa um `@graph` com `LocalBusiness`,
`Service`, `Offer` (com os 4 preços), `Person`, `FAQPage`, `BreadcrumbList` e `Review`
interligados por `@id`. **Não substituir pelo modelo do prompt — seria um retrocesso.**

O único acréscimo que vale, depois do item 9:

```json
"sameAs": [
  "https://www.linkedin.com/in/renan-carvalho-barbosa",
  "https://www.instagram.com/rcbseo",
  "https://www.guiamais.com.br/<perfil>",
  "https://www.apontador.com.br/<perfil>"
]
```

---

## Como refazer esta auditoria

Os números do Search Console vêm de:

```
seo auth refresh
seo gsc-query --site "https://rcbseo.com.br/" --start-date AAAA-MM-DD --end-date AAAA-MM-DD \
  --dimensions query,page --limit 5000 --json
```

E a velocidade de:

```
lighthouse https://rcbseo.com.br/ --quiet --chrome-flags="--headless=new" \
  --output=json --output-path=lh.json
```

⚠️ **Rode o Lighthouse duas vezes.** Nesta auditoria as duas execuções deram performance 57 e 75, e
CLS 0,391 e 0,029. Uma medição só levaria a corrigir um problema que não existe.
