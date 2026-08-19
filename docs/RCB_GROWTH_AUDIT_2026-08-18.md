# Auditoria de crescimento RCB — 18/08/2026

Auditoria orientada a dados reais do próprio domínio, com implementação. Commit de
partida: `c02a985`. Nada foi enviado para produção — os três commits desta rodada são
locais.

Fontes: Search Console via CLI `seo` (propriedade `https://rcbseo.com.br/`, 90 dias:
20/05 a 17/08/2026), SERP do Google conferida ao vivo em 18/08/2026 sem personalização,
Keyword Planner (buckets passados pelo Renan) e o próprio repositório.

Dados brutos e planilhas: `data/audit/`.

---

## Resumo em uma página

O site está tecnicamente correto e comercialmente mal apontado.

Em 90 dias: **4.179 impressões, 21 cliques, posição média 35,3**. O CTR do domínio
inteiro é 0,5%.

Três descobertas mudam a estratégia:

1. **A página mais bem colocada disputa uma busca que quase ninguém faz.**
   `/consultor-seo-goiania/` apareceu em **4ª posição orgânica numa consulta pontual de
   SERP** feita em 18/08/2026 para o termo exato "consultor seo goiania". Ainda assim,
   rendeu **47 impressões em 90 dias**. Ganhar essa disputa específica não gera negócio;
   o que ela sugere é *que tipo* de disputa a RCB parece conseguir ganhar hoje.
   ⚠️ Ver a ressalva metodológica logo abaixo: **4ª posição e posição média 16,5 não são
   a mesma métrica e não devem ser comparadas.**

2. **65% das impressões vêm de páginas que nunca vão gerar clique.** As páginas
   nacionais de nicho de saúde somam mais de 1.000 impressões em posições 43 a 93, com
   **zero clique em 90 dias**. Ninguém clica na página 5.

3. **A maior demanda comercial local do levantamento não tinha URL nenhuma.**
   "criação de site(s) Goiânia" — bucket ~500/mês cada variante, lance de referência
   R$ 17,61 — e **zero impressão** no Search Console, porque não existia página.
   Foi criada nesta rodada.

Autoridade externa (backlinks) é uma **hipótese forte** de gargalo, mas não a única — e
não foi provada aqui. Dentro do que dá para fazer no site, a aposta desta rodada foi
deixar de disputar SERP nacional de nicho e ocupar a SERP local onde a RCB **aparenta**
ter mais chance.

---

## Ressalva metodológica — leia antes das tabelas

Este relatório mistura duas fontes que **não são comparáveis entre si**, e vale deixar
explícito para ninguém tirar conclusão errada depois:

1. **"4ª posição" é uma observação pontual de SERP.** Foi uma busca única, feita em
   18/08/2026, de um IP fora de Goiânia, com `gl=br` e `pws=0`, para o termo exato
   "consultor seo goiania". É uma fotografia de um instante, de um lugar, de uma
   consulta. Pode variar por dia, por cidade, por dispositivo e por histórico do usuário.

2. **"Posição média 16,5" é outra coisa.** É a média que o Search Console calcula
   ponderando **todas** as impressões da página em **todas** as consultas dos 90 dias —
   inclusive consultas ruins, consultas em que a página apareceu na posição 60, e
   consultas que o Google não mostra por privacidade.

**As duas não se contradizem e não se confirmam.** Uma página pode estar em 4º numa
consulta e ter média 16,5 porque aparece mal em dezenas de outras. Nenhum número deste
relatório deve ser lido como "a página subiu de 16,5 para 4".

Da mesma forma, **causalidade não foi estabelecida em nenhum ponto**. Os padrões abaixo
são correlações observadas numa amostra pequena (6 páginas, um domínio, um período).
Estão escritos como hipóteses de trabalho, não como leis.

---

## A. Situação real no Search Console

| Período | Cliques | Impressões | Posição média | URLs com impressão |
|---|---:|---:|---:|---:|
| 90 dias (20/05–17/08) | 21 | 4.179 | 35,3 | 175 |
| 28 dias (21/07–17/08) | 11 | 2.159 | 33,9 | 148 |
| 28 dias anteriores (23/06–20/07) | 9 | 1.715 | 39,2 | 86 |

A comparação entre os dois períodos de 28 dias é a única notícia boa medida: impressões
+26%, posição média de 39,2 para 33,9 e o número de URLs com impressão saltou de 86 para
148. As rodadas de julho e agosto (semântica, poda de cidades, intenções leigas) estão
funcionando — devagar, e ainda longe da faixa de clique.

**Cliques por URL em 90 dias:** home 6, `/blog/como-saber-se-meu-site-esta-indexado/` 2,
`/consultor-seo-goiania/` 2, e mais 11 URLs com 1 clique cada. É isso.

## B. Bing

Não foi possível cruzar: o Bing Webmaster Tools **não está conectado a nenhuma
ferramenta desta máquina** (registrado no handoff de 12/08 e reconfirmado agora — não há
API, nem export, nem credencial). O que existe do Bing no projeto é o IndexNow, que é
envio, não leitura. Para ter dado do Bing seria preciso o Renan conectar a conta e
exportar; até lá, qualquer número seria inventado.

## C. URLs vencedoras

| URL | Impr. 90d | Cliques | Posição | Situação |
|---|---:|---:|---:|---|
| `/` | 224 | 6 | 5,4 | Vencedora de marca ("rcb", "rcb marketing", "google") |
| `/blog/como-saber-se-meu-site-esta-indexado/` | 157 | 2 | 9,4 | Vencedora informacional |
| `/consultor-seo-goiania/` | 47 | 2 | 16,5 | **Vencedora comercial — protegida** |
| `/blog/como-responder-avaliacoes-google-clinica/` | 116 | 0 | 7,2 | 1ª página, sem clique |
| `/blog/por-que-minha-empresa-nao-aparece-no-google/` | 133 | 0 | 10,3 | Um degrau abaixo |
| `/para-comercios-locais/` | 255 | 0 | 27,8 | Posição 8,8 na sua melhor consulta |

## D. Queries vencedoras

Fora as de marca ("rcb", "rcb marketing", "rcb whatsapp"), as posições reais boas são:

- `negócio local perto de mim brasil` — **101 impressões, posição 8,8**, zero clique
- `perfil google sem resultado` — 10 impressões, posição 10,3
- `serviço local perto de mim brasil` — 6 impressões, posição 7,8
- `consultor seo` — 2 impressões, posição 7,0
- `como receber mais orçamento pelo whatsapp` — 7 impressões, posição 19,9

Chama atenção que a melhor consulta não-marca do domínio (`negócio local perto de mim
brasil`, posição 8,8) é uma busca genérica que o site atende por acidente, não por
projeto.

## E. Estudo da página `/consultor-seo-goiania/`

**Confirmação primeiro.** O Search Console **não** mostra a consulta "consultor seo
goiânia": em 90 dias ela tem zero impressão registrada. Isso poderia significar que a
página não ranqueia. Por isso a SERP foi conferida ao vivo:

> Busca `consultor seo goiania` em google.com.br, `gl=br`, `pws=0` (sem personalização),
> 18/08/2026 — resultados orgânicos na ordem:
> 1. divia.com.br · 2. antonioseo.com.br · 3. agenciakaizen.com.br ·
> **4. rcbseo.com.br/consultor-seo-goiania/** · 5. digitallevolution.com.br ·
> 6. michelferreira.com.br · 7. agathosagencia.com.br · 8. brainstormmarketingdigital.com.br ·
> 9. pulse62.com

**A alegação se sustenta nesta observação** — 4º lugar numa busca pontual, feita de fora
de Goiânia; de dentro da cidade pode ser melhor, o que explicaria a percepção de 2º/3º.
E o Search Console não contradiz isso: a consulta praticamente não é feita. **A página
aparece bem colocada nessa consulta específica; a busca é que quase não existe.**

Vale repetir: uma única checagem de SERP não é medição de ranking. Para afirmar posição
com segurança seria preciso acompanhar a mesma consulta ao longo de dias, de Goiânia, em
celular e desktop.

### Anatomia da página

| Sinal | Valor |
|---|---|
| Criada em | 20/06/2026 (mais nova que quase todas as páginas fracas) |
| Palavras | **1.285 — a menor de todas as comerciais analisadas** |
| H2 / H3 | 8 / 16 |
| Links internos editoriais recebidos | **15 — o menor número entre as comerciais** |
| Links externos de autoridade | 8 |
| Menções a "Goiânia" | **18 — o maior número** |
| Title | `Consultor de SEO em Goiânia \| Renan Carvalho Barbosa \| RCB` |
| H1 | `Consultor de SEO em Goiânia` — **correspondência exata, sem enfeite** |
| Schema | Person + LocalBusiness + PostalAddress + Service + Offer + FAQPage + Breadcrumb |
| NAP | Endereço completo de Goiânia no schema e no rodapé |

### Comparação: vencedora × quase × fracassadas

| Página | Palavras | Links int. | H2/H3 | "Goiânia" | Posição 90d | Cliques |
|---|---:|---:|---:|---:|---:|---:|
| **`/consultor-seo-goiania/`** (vence) | **1.285** | **15** | 8/16 | **18** | 16,5 | 2 |
| `/consultoria-seo-local/` (quase) | 1.566 | 261 | 11/16 | 11 | 12,8 | 1 |
| `/seo-para-dentistas/` (quase) | 2.217 | 211 | 10/24 | 5 | 25,0 | 0 |
| `/seo-para-clinicas-de-estetica/` (fracassa) | 2.541 | 210 | 12/30 | 4 | 43,8 | 0 |
| `/google-perfil-empresa/` (fracassa) | 1.329 | **244** | 9/22 | 0 | 77,6 | 0 |
| `/seo-para-clinicas/` (fracassa) | **2.951** | **228** | 16/35 | 6 | 69,5 | 0 |

### F. O que a amostra mostra — e o que ela não permite afirmar

**O que está medido (fatos da amostra de 6 páginas):**

- **Mais palavras não acompanharam melhor desempenho.** A melhor colocada é a mais curta
  (1.285 palavras); a pior colocada (`/seo-para-clinicas/`, 69,5) é a mais longa (2.951).
- **Mais links internos não acompanharam melhor desempenho.** A melhor colocada tem 15
  links; `/google-perfil-empresa/` tem 244 e está em 77,6.
- **Schema e estrutura de headings não separam os grupos.** Todas têm conjunto
  equivalente de schema, e as piores colocadas até têm mais H2 e H3.

**O que isso NÃO prova.** Nada disso demonstra que conteúdo, link interno ou schema sejam
irrelevantes. A leitura correta é mais modesta: **isoladamente, e nesta amostra, nenhuma
dessas variáveis explicou a diferença de desempenho.** É perfeitamente possível que elas
sejam necessárias e não suficientes — ou que estejam mal aplicadas nas páginas fracas
(intenção errada, texto que não responde à consulta, arquitetura que dilui). Seis páginas
de um único domínio não sustentam conclusão causal.

**Hipóteses de trabalho, em ordem de plausibilidade:**

1. **Nível de concorrência da consulta.** É a hipótese mais provável para o desempenho de
   `/consultor-seo-goiania/`: a SERP de "consultor seo goiania" é disputada por agências
   locais pequenas, enquanto a de "seo para clínicas de estética" reúne concorrentes
   maiores. Provável contribuição — não causa isolada demonstrada.
2. **Correspondência exata entre consulta e H1/title**, curtos e sem subtítulo grudado.
3. **Densidade geográfica** — 18 menções a Goiânia, contra 0 a 6 nas piores colocadas.
4. **Entidade nomeada** — pessoa real no title, `Person` + `LocalBusiness` + endereço
   verificável.
5. **Autoridade externa (backlinks).** Hipótese importante, **não testada aqui**: não há
   ferramenta de backlink nesta máquina, então a diferença de perfil de links entre a RCB
   e os concorrentes é suposição, não medição.

**Fatores que ainda não foram avaliados e podem pesar tanto quanto os acima:** intenção
de busca de cada página (a página responde mesmo o que a pessoa perguntou?), CTR
(há 602 impressões de primeira página com 1 clique — isso é sintoma de algo), arquitetura
e relevância tópica do site como um todo. Qualquer conclusão sobre "o gargalo" precisa
considerar esse conjunto, não só backlink.

> **Aposta desta rodada (não regra comprovada):** o padrão sugere que, no estágio atual, a
> RCB tem mais chance em SERP local de menor concorrência com correspondência exata do que
> em SERP nacional de nicho. A página nova de criação de sites foi construída seguindo esse
> molde — é uma aposta a ser verificada com dados em 60–90 dias, não uma certeza.

## G. Páginas quase chegando (QUASE LÁ)

Todas com posição de primeira página ou perto, e **zero clique**:

| URL | Posição | Impressões | Diagnóstico |
|---|---:|---:|---|
| `/blog/como-responder-avaliacoes-google-clinica/` | 7,2 | 116 | Está na 1ª página e não é clicada — problema de title/description, não de rank |
| `/para-comercios-locais/` (`negócio local perto de mim brasil`) | 8,8 | 101 | Idem |
| `/blog/por-que-minha-empresa-nao-aparece-no-google/` | 10,3 | 133 | Um degrau |
| `/blog/google-meu-negocio-nao-aparece/` | 11,6 | 95 | Um degrau |
| `/blog/por-que-meu-site-nao-aparece-no-google/` | 11,4 | 65 | Um degrau |
| `/consultoria-seo-local/` | 12,8 | 92 | Comercial mais bem colocada |

**Este é o grupo de maior retorno por esforço do site inteiro.** Seis páginas na
primeira página ou colada nela, somando 602 impressões e **um único clique**. Não é
problema de posição — é de título e descrição não responderem à pergunta que a pessoa
fez. Corrigir isso é trabalho de CTR e independe de conseguir backlink.

## H. Páginas fracassadas

| URL | Impressões | Posição | Cliques |
|---|---:|---:|---:|
| `/seo-para-clinicas-de-estetica/` | 417 | 43,8 | 0 |
| `/seo-para-clinicas/` | 321 | 69,5 | 0 |
| `/google-perfil-empresa/` | 171 | 77,6 | 0 |
| `/blog/como-aparecer-no-google-maps/` | 161 | 62,6 | 0 |
| `/como-aparecer-no-google/` | 149 | 58,5 | 0 |
| `/seo-para-contadores/` | 140 | 65,2 | 0 |

Somadas: **1.359 impressões, zero clique.** São consultas nacionais de nicho, onde o site
não consegue chegar perto do topo. O que se pode afirmar com segurança: **texto (rodada
de 08/08), links internos (12/08) e preço (09 e 10/08) já foram tentados nessas páginas e
não moveram a posição.** O que *ainda não* se pode afirmar é a causa — autoridade externa
é a hipótese mais citada, mas intenção de busca e relevância tópica do domínio inteiro
para esses temas também são explicações plausíveis e não foram isoladas.

**Sem sinal:** 20 artigos do blog e duas páginas comerciais (`/conteudo-para-seo/`,
`/site-para-clinica/`) com zero impressão em 90 dias. Vários são recentes (15/08), então
ainda é cedo para julgar.

## I. Canibalizações medidas

Quatro casos reais, com as duas URLs aparecendo na **mesma** consulta:

| Consulta | URL melhor colocada | URL pior colocada | Problema |
|---|---|---|---|
| `seo para contabilidade` | `/blog/seo-para-contadores/` (40,0) | `/seo-para-contadores/` (67,5) | **Sinal invertido:** o artigo ganha da página de venda |
| `consultoria seo local` | `/guia-seo-local/` (20,5) | `/consultoria-seo-local/` (42,0) | **Sinal invertido**, apesar dos 249 links internos da comercial |
| `seo para consultorios` | `/seo-para-medicos/` (18,1) | `/seo-para-clinicas/` (72,2) | Definir dono: médicos |
| `seo para pequenas empresas` | `/seo-para-pequenas-empresas/` (34,4) | `/blog/vale-a-pena-seo-para-pequena-empresa/` (69,0) | Ordem correta, mas as duas fracas |

Os dois primeiros são os que importam: **a página que vende está perdendo para o artigo
que só explica.** É o oposto do que a arquitetura de 12/08 pretendia.

## J. Lacunas de palavra-chave (Planner × Search Console × URL)

| Tema | Bucket | CPC ref. | Impressões GSC | URL | Conclusão |
|---|---|---|---:|---|---|
| criação de site(s) Goiânia | 500 + 500 | R$ 17,61 | **0** | não existia | **Criar** — feito |
| SEO para sites | 50 | R$ 30,03 | ~0 | `/site-otimizado-para-seo/` (6 impr.) | Existe, sem força |
| SEO Goiânia | 50 | R$ 22,34 | 3 | `/seo-local-goiania/` | Atacar a existente |
| SEO Local | 50 | R$ 14,11 | 29 (pos. 29,6) | `/consultoria-seo-local/` | Atacar |
| consultor SEO | 50 | alta conc. | 2 (pos. 7,0) | `/consultor-seo-goiania/` | Proteger |
| agência SEO | 50 | alta conc. | ~0 | nenhuma | **Ignorar** — a RCB não é agência |

A leitura comercial mais importante: **"criação de site Goiânia" tem cerca de 10× o
volume de "SEO Goiânia"**, e um CPC de R$ 17,61 significa que existe gente pagando por
esse clique todo dia. É a única entrada local com volume real.

## K. Oportunidade de criação de site — verificação antes de criar

Checagens feitas antes de escrever uma linha, na ordem exigida:

- **Search Console:** zero impressão para qualquer variante do tema em 90 dias.
- **URL existente:** só `/site-otimizado-para-seo/` (nacional, sem geo, 6 impressões,
  posição 6,7 — sem volume). Não cobre a busca local.
- **Canibalização:** nenhuma. Intenção diferente (local × nacional) e termo diferente
  ("criação de site" × "site otimizado"). As duas foram ligadas por link.
- **SERP (18/08, `gl=br`, sem personalização):** `goianiacriacaodesite.com.br`,
  `siteway.com.br`, `criacaodesitegoiania.com.br`, `webdesignbrasil.org`, `youweb.com.br`,
  `atualint.com.br`, `buenosites.com`, `soub.digital`, `logicsite.com.br`. Dois anúncios
  no topo (`agenciaspin.com`, `sites.grupog3n.com.br`).
  **Perfil da concorrência: domínios de correspondência exata e agências pequenas — o
  mesmo perfil da SERP que a RCB já ganha.**

Foi criada `/criacao-de-sites-goiania/`, seguindo o molde da vencedora: H1 curto de
correspondência exata (`Criação de sites em Goiânia`), densidade geográfica, entidade
nomeada com endereço, e linguagem de leigo do começo ao fim.

## L. Oportunidades de dor em linguagem leiga

O grupo já existe e **já traz impressão**: "por que minha empresa não aparece no google"
(133), "google meu negócio não aparece" (95), "por que meu site não aparece no google"
(65), "aparecer no google" (101), "como aparecer no google maps" (161). Somando o
cluster: ~600 impressões.

O problema não é falta de página — é que **as páginas boas do grupo já estão na primeira
página e não são clicadas**, e as de volume grande estão em posição 50–70.

**Não criar mais artigos deste tema agora.** O trabalho é de título/descrição nas seis
páginas do grupo QUASE LÁ, e de caminho comercial: hoje quem lê
`/blog/como-saber-se-meu-site-esta-indexado/` (a 2ª página que mais clique gera) não tem
para onde ir depois.

## M. Arquitetura comercial recomendada

Três frentes, com prioridade nesta ordem:

1. **Local Goiânia (o que dá para ganhar hoje).** `/criacao-de-sites-goiania/` +
   `/consultor-seo-goiania/` + `/seo-local-goiania/`. É onde a concorrência é do tamanho
   da autoridade da RCB. Toda energia de conteúdo novo deveria ir para cá.
2. **Dor em linguagem leiga (o que já tem atenção).** O cluster de "não apareço no
   Google". Trabalho de CTR e de caminho até a venda, não de volume de artigo.
3. **Nichos nacionais (onde três tentativas já não moveram nada).** Congelar produção.
   As páginas ficam no ar, mas não recebem mais esforço até que algo mude no quadro —
   seja autoridade externa, seja uma revisão de intenção de busca dessas páginas.

Por segmento de cliente, a home passou a falar com comércios, prestadores de serviço,
profissionais liberais e clínicas — nessa ordem — em vez de três recortes de saúde.

## N. Alterações executadas

Três commits **locais**, nenhum enviado.

**`6609b1a` — cria `/criacao-de-sites-goiania/` e liga o cluster de site**
- Página nova (~1.500 palavras), schema completo, 4 pacotes, FAQ de 6 perguntas.
- 9 links internos editoriais com âncoras variadas, vindos de páginas que já falam de
  site e/ou de Goiânia.
- Sitemap: 144 → 145 URLs.
- Scripts de análise do Search Console + dados brutos em `data/audit/`.

**`a28d0ec` — o CTA principal deixa de ser o diagnóstico e vira WhatsApp**
- 63 botões que apontavam para `/diagnostico-presenca-digital/` passam a abrir o
  WhatsApp com a mensagem pronta (36 arquivos).
- 70 botões que já iam ao WhatsApp mas usavam o texto antigo foram padronizados (68
  arquivos).
- `gerar-paginas-cidades.py` ensinado **antes** de regerar; 199 cidades + hub regeradas.
- A página do diagnóstico **não foi apagada** (24 impressões, posição 16,7) e continua
  alcançável por 313 links de menu e 401 de rodapé/texto.

**`f3b484c` — home deixa de ser "SEO para clínicas"**
- Title, description, og e twitter: sai "para Clínicas".
- Cartões de nicho: de 3 de saúde + 1 comércio para comércios, prestadores,
  profissionais liberais e clínicas.
- Linha nova `.nichos-extra` mantém o link da home para os oito nichos que saíram dos
  cartões — `/seo-para-dentistas/` está em posição 25 e é alvo de ataque, não de abandono.
- Link da home para a página nova.

## O. Alterações ainda recomendadas (não executadas)

Por ordem de retorno sobre esforço:

1. **Reescrever title e description das 6 páginas QUASE LÁ.** 602 impressões na primeira
   página com 1 clique. É a maior oportunidade sem depender de backlink. Não foi feito
   nesta rodada porque cada uma exige decisão de copy caso a caso.
2. **Resolver os dois sinais invertidos de canibalização** (`seo para contabilidade` e
   `consultoria seo local`): a página de venda tem de passar o artigo.
3. **Dar caminho comercial ao topo do funil.** As duas páginas que mais recebem clique
   são artigos que não levam a nenhuma página de venda.
4. **Trocar o CTA da página protegida.** Ela ainda tem 2 botões de "diagnóstico
   gratuito" — a oferta que não converte. **Depende da sua autorização** (item T).
5. **Off-page.** Segue como a hipótese de gargalo mais citada e a mais barata de testar —
   mas deve ser perseguida **junto** com CTR, intenção e arquitetura, não no lugar delas.
   Item 1 desta lista, por exemplo, pode melhorar tráfego sem nenhum backlink novo.
6. **CNPJ e razão social no rodapé** — pendente desde 09/08, esperando o número.

## P. Riscos

- **Risco de perder a 4ª posição:** nulo nesta rodada. `git diff` de
  `/consultor-seo-goiania/` está vazio; os scripts abortam se algum alvo for ela; o menu
  (sitewide) não foi alterado justamente para não mexer no HTML dela.
- **Risco da troca de CTA:** o WhatsApp pode gerar mais conversa de baixa qualidade que o
  formulário do diagnóstico. Reversível — os scripts são idempotentes e o commit isola a
  mudança.
- **Risco de o diagnóstico perder indexação:** baixo. Continua com 313 links de menu e
  401 de rodapé e texto.
- **Risco da página nova não ranquear:** real. Domínio de correspondência exata é
  adversário duro em SERP local, e o domínio tem quase zero backlink. Prazo honesto para
  avaliar: 60 a 90 dias.
- **O que este trabalho não resolve:** o funil continua quase vazio. Melhorar conversão
  de quem quase não chega não muda faturamento por si só.
- **Risco de conclusão precipitada:** o maior risco deste relatório é ele ser lido como
  prova de que "conteúdo e link interno não importam" ou de que "só falta backlink".
  Nenhuma das duas coisas foi demonstrada. A amostra é pequena, é de um único domínio e
  de um único período, e variáveis importantes (intenção, CTR, relevância tópica,
  concorrência) não foram isoladas umas das outras.

## Q. Testes executados

- 36 links internos da página nova conferidos em servidor local: **todos 200**.
- Página nova no navegador: 1 H1, 1 `#pacotes` (sem a duplicação que já aconteceu na
  home), 1 barra de celular, 6 FAQ, JSON-LD válido, **sem estouro horizontal**, nenhuma
  imagem quebrada.
- Home no navegador após a mudança: 8 links na linha de nichos, zero botão apontando
  para o diagnóstico, layout sem estouro, grade de nichos inalterada (4 cartões antes e
  depois).
- `scripts/conferir-conversao.py`: 314 páginas, 233 com preço, 311 com barra e menu novo,
  145 URLs no sitemap, **1 problema — pré-existente** (jargão "on-page" em
  `/seo-local-goiania/`, confirmado por `git stash` que já existia antes).
- Auditoria técnica própria (`scripts/auditoria-tecnica.py`): **0 contradições
  noindex×sitemap, 0 canonical divergente, 0 title duplicado, 0 description duplicada,
  0 página sem H1.** As duas sem canonical são `/404.html` e a demo em JS, ambas de
  propósito.
- HTML balanceado (`<a>`/`</a>`) nas páginas tocadas.
- Todos os scripts rodados **duas vezes**: segunda execução reporta 0 alterações.

## R. `git status`

Árvore limpa, exceto `.github/` que já estava fora do versionamento antes desta sessão
(não faz parte deste trabalho).

## S. Commits locais

```
f3b484c  feat(home): tira a identidade de "SEO para clinicas" e abre para empresa local
a28d0ec  feat(conversao): CTA principal deixa de ser o diagnostico e vira WhatsApp
6609b1a  feat(seo): cria /criacao-de-sites-goiania/ e liga o cluster de site
c02a985  (baseline desta auditoria)
```

**Nenhum push. Nenhum deploy.**

## T. Itens que exigem sua autorização

1. **Publicar** (`git push origin main`) — o Cloudflare Pages publica sozinho depois.
2. **IndexNow** — só depois de confirmar HTTP 200 na URL nova. Chave fixa
   `19341b29c6054af601879d85a34d62c5`, nunca gerar outra.
3. **Reenviar o `sitemap.xml`** no Search Console — agora 145 URLs, **1 nova**. Manual,
   feito por você.
4. **Pedir indexação manual** de `/criacao-de-sites-goiania/` no Search Console.
5. **Trocar os 2 botões de "diagnóstico gratuito" da página protegida** — não fiz.
6. **Colocar "Criação de sites" no menu** — daria muita força à página nova, mas
   reescreve o `<nav>` da página protegida. Você optou por não fazer agora; vale
   reavaliar em 30–60 dias com dados.

---

## Anexos

- `data/audit/query_url_matrix.csv` — 274 pares consulta × URL, 90 dias
- `data/audit/url_baseline_90d.csv` — 175 URLs com desempenho e melhor consulta
- `data/audit/opportunity_pages.csv` — mapa de oportunidades (22 linhas, com status e ação)
- `data/audit/protected_pages.csv` — páginas protegidas e a regra de cada uma
- `data/audit/raw_*.json` — respostas brutas do Search Console

## Verificações de escopo que fecharam sem ação

- **`renancbarbosa.com.br`**: responde **301 para `https://rcbseo.com.br/`** em http,
  https e www. O Wayback Machine e o `gau` (Wayback + Common Crawl + OTX + URLScan) não
  retornam **nenhuma** URL histórica do domínio. Não há página antiga para mapear nem
  autoridade a preservar — **o redirect atual está correto e não há nada a fazer.**
- **Páginas de cidade**: a poda de 12/08 continua coerente — 168 em `noindex`, 31
  indexáveis + hub no sitemap. Dessas, só `/consultoria-seo/rio-de-janeiro/` (28
  impressões) tem sinal relevante e 21 têm zero impressão. **Nenhuma justifica voltar, e
  nenhuma justifica novo corte agora.** Reavaliar junto com a revisão de setembro.
- **Indexação técnica**: sem contradição entre `noindex` e sitemap, sem canonical
  errado, sem duplicidade de metadados. `robots.txt` continua liberando os robôs de IA
  de propósito.
- **Perfil da Empresa da RCB**: não auditado. Exigiria acesso ao painel do Google
  Business Profile, que não está disponível a partir daqui. Fica para você conferir
  categoria, serviços, descrição e avaliações — ou me passar as informações.
