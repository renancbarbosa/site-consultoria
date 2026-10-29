# Fase 0: auditoria antes do pilar "Visibilidade em IA"

Data: 28/10/2026 · Branch local: `pilar-visibilidade-ia` · Base: `3a301e93`
Nenhum arquivo do site foi alterado nesta fase.

## 1. Como o site funciona

| Item | Situação |
|---|---|
| Tecnologia | HTML estático escrito à mão e por geradores Python (`scripts/`). Sem framework, sem CMS. |
| Publicação | Cloudflare Pages, publica sozinho a cada `git push origin main`. |
| Renderização | O conteúdo vem pronto no HTML. Nada importante depende de JavaScript (bom para robô de IA, que quase nunca roda JS). |
| CSS / JS | `styles.css` (edita) → `styles.min.css` (gerado), `script.js`. |
| Arquivos internos | `functions/_middleware.js` responde 404 para `/docs`, `/scripts`, `/data` etc. Por isso os relatórios desta rodada ficam em `docs/visibilidade-ia/`, e não na raiz como o prompt pedia. |
| Geradores reaproveitáveis | `scripts/gerar-servicos-marketing.py` (`montar()`, copia o esqueleto vivo de `/criacao-de-sites-goiania/`), `scripts/rcb_copy.py` (`humanizar()`), `scripts/rcb_menu.py` (menu e rodapé), `scripts/indexnow.py`, `scripts/conferir-conversao.py`. |

## 2. Inventário do sitemap

**181 URLs. As 181 têm arquivo, DOCTYPE, title de até 65 caracteres, description de até 160,
exatamente um H1 e JSON-LD válido.** Nenhum problema encontrado.
Tabela completa (URL, title, description, H1, tipos de schema): `inventario-sitemap.md`, nesta pasta.

## 3. O que o prompt achava que faltava e já existe

| Pedido do prompt | Situação real |
|---|---|
| robots.txt liberando robôs de IA | Já libera GPTBot, ClaudeBot, Google-Extended, PerplexityBot, Applebot-Extended, CCBot. Faltam explícitos: OAI-SearchBot, ChatGPT-User, Claude-User (hoje caem no `User-agent: *`, que também libera). |
| `/llms.txt` e `/llms-full.txt` | Existem e foram alinhados em `c7ea293c`. Falta só o 5º pilar. |
| `ProfessionalService` + `Person` + `hasOfferCatalog` na home | Já existem. `Person` tem `knowsAbout`, mas sem GEO/AEO; `ProfessionalService` tem 3 `sameAs`, `Person` tem 1. |
| IndexNow | Funciona (`scripts/indexnow.py`, chave de sempre). |
| "Página de criação de sites publica preço" | **Não publica.** Mostra faixa de **mercado**, sem preço da RCB. Regra mantida: nenhum preço da RCB no site. |
| Página por cidade (Goiânia, Aparecida, Anápolis) | Existem `/consultoria-seo/anapolis/`, `/consultoria-seo/aparecida-de-goiania/` e outras indexáveis. O pilar novo terá só Goiânia, como o prompt manda. |

## 4. Mapa de canibalização (páginas que já falam de IA)

Busca em todo o HTML por ChatGPT, Gemini, Perplexity, AI Overviews, "inteligência artificial", " IA ", GEO, AEO:

| Página | O que diz sobre IA | Decisão |
|---|---|---|
| `/seo-para-youtube/` | Seção "Google e IA": assistentes de IA leem título, descrição e transcrição do vídeo. | **(a) Manter.** Ganha um link para o pilar. Ângulo é vídeo, não compete. |
| `/blog/velocidade-sites-clinicas-goiania/` | Cita "construtor com IA" como ferramenta de fazer site. | **(a) Manter.** Assunto é velocidade, não visibilidade em IA. Sem link (seria forçado). |
| Qualquer outra página | Nenhuma cita ChatGPT, Gemini ou Perplexity (0 de 181). | n/a |

**Nenhum caso (b) ou (c).** Nada a fundir, nada a redirecionar. O campo está vazio.

## 5. Procura medida (Search Console, 29/07 a 26/10/2026)

- Site inteiro (com consulta identificada): 4.225 impressões, 4 cliques.
- Buscas sobre IA: **2 impressões** ("agente de ia para clinicas" e "geo para clinicas"), 0 cliques.
- Conclusão: não há demanda chegando hoje. O pilar é aposta em busca nova, não correção de algo
  que já tem tráfego. Por isso a pesquisa própria (Fase 2, item 4) é a peça mais importante: é o que
  faz uma IA citar o site sem depender de posição no Google.

## 6. Velocidade no celular (Lighthouse 13 local, 2 rodadas, produção)

Celular simulado (rede e processador lentos). Nota de 0 a 100; LCP = tempo até aparecer o maior
bloco da tela (o Google quer até 2,5 s); CLS = quanto a página "pula" enquanto carrega (até 0,1).

| Página | Nota (1ª / 2ª) | LCP | CLS | Bloqueio (TBT) |
|---|---|---|---|---|
| Home | 73 / 69 | 4,6 s / 5,3 s | 0,008 / 0 | 230 / 250 ms |
| `/servicos/` | 75 / 77 | 4,9 s / 4,7 s | 0,001 | 140 / 120 ms |
| `/blog/quanto-custa-um-site/` | 76 / 96* | 4,8 s / 2,1 s* | 0,04 / 0,08 | 80 / 100 ms |
| `/blog/seo-para-clinicas-vale-a-pena/` | 72 / 72 | 5,8 s / 5,8 s | 0,036 | 100 / 70 ms |
| `/blog/por-que-minha-empresa-nao-aparece-no-google/` | 74 / 75 | 5,4 s / 5,1 s | 0,014 | 90 / 70 ms |

\* Rodada fora da curva (provável cache quente). Vale a 1ª.

**Leitura:** a página não "pula" (CLS ótimo) e não trava (TBT baixo). O problema é só um: **o
LCP fica entre 4,6 s e 5,8 s**, quase o dobro do limite. Nas três páginas analisadas o maior bloco é
**texto** (o H1 na home, o subtítulo em `/servicos/`), não imagem. Duas causas medidas:

1. `styles.min.css` trava a pintura por 400 a 575 ms (17 KB).
2. O atraso de pintura do elemento (`elementRenderDelay`) é de 900 a 1.350 ms depois do servidor
   responder. Hipótese mais provável, **a confirmar com teste**: a fonte Inter vem do Google Fonts
   de forma assíncrona com `display=swap`; quando ela chega, o texto é redesenhado e o Google conta
   esse redesenho como o novo LCP. Ou seja, o LCP mede a chegada da fonte.

Correção a testar na Fase 5 (vale para o site inteiro, não só para as páginas novas): servir a
Inter do próprio site (só os pesos usados, em woff2, com `preload`) e colocar no HTML o CSS do topo
da página. Medir de novo duas vezes antes de afirmar que resolveu. A meta do prompt (≥ 85 nas
páginas novas) depende disso, porque elas vão usar o mesmo esqueleto.

## 7. Onde estão as peças que a Fase 6 vai mexer

**Cartões "Valor sob medida"** — `servicos/index.html`, seção `#orcamento` (linhas 427 a 470):
três `<article class="pacote-card">` ("Aparecer no Google", "Clientes agora com anúncio",
"Site ou landing page"), texto em `<p class="pacote-condicao">` nas linhas 438, 451 e 463. Cada um
já tem botão de WhatsApp com mensagem própria. Decisão do Renan: **continua sem preço**.

**Formulário em dois passos** — `index.html`:
- Formulário `#rcbLeadForm`, linha 770. Campos: nome, WhatsApp, tipo de negócio, cidade, pacote.
- Passo 2 `#rcbLeadOk` ("Recebi seus dados! Agora é só apertar o botão"), linhas 835 a 844.
- Script, linhas 1090 a 1248: valida, envia ao Web3Forms (`fetch`, linha 1220) e só então mostra o
  passo 2 com o botão do WhatsApp.
- Decisão do Renan: **só WhatsApp, sem registro**. Sai o Web3Forms e o passo 2; o botão abre o
  WhatsApp no mesmo clique (se esperar o servidor, o celular bloqueia a janela).

**Achados de passagem no formulário (desatualizados):**
1. O campo "pacote" ainda oferece os pacotes antigos ("Presença Lite", "Presença", "Crescimento",
   "Dominação"), que saíram do site com o preço em 28/09.
2. O campo "tipo de negócio" só lista clínicas, dentista, estética e comércio; o site hoje fala com
   dono de negócio em geral.
3. O mapa `VALOR` do script ainda carrega os preços antigos (1.997 a 4.997). O visitante não vê,
   mas vai para o GA4 como valor da conversão.
4. `subject` e `from_name` ainda dizem "RCB Consultoria"; a marca é RCB SEO.

Proposta para a Fase 6: trocar "pacote" por "o que você precisa" com os 5 serviços (incluindo
visibilidade em IA), ampliar "tipo de negócio", e tirar o mapa de preços antigo.

## 8. Outros achados

- `/blog/link-building-para-bets-o-que-avaliar/` (divisão retirada em agosto) ainda teve 65
  impressões em 90 dias. Responde **410** (removida de vez), então o Google vai tirar sozinho.
  Nada a fazer.
- Páginas com mais impressão (90 dias), candidatas ao ajuste de abertura da Fase 4:
  `/como-aparecer-no-google/` (736), `/seo-para-contadores/` (392),
  `/seo-para-clinicas-de-estetica/` (377), `/criacao-de-sites-goiania/` (240),
  `/seo-para-clinicas/` (240), `/seo-para-pequenas-empresas/` (165), `/google-perfil-empresa/` (161),
  `/para-comercios-locais/` (158), `/seo-para-imobiliarias/` (153), `/guia-seo-local/` (113).
  `/consultor-seo-goiania/` (82) fica de fora: é protegida.

## Decisões pendentes do Renan

1. Aprovar a troca dos campos do formulário da home (item 7).
2. Aprovar a lista das 10 páginas da Fase 4 (item 8).
