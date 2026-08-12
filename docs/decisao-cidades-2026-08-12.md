# Decisão sobre as 199 páginas de cidade — 12/08/2026

> **Fonte de verdade executável:** `scripts/rcb_cidades.py`.
> Este documento explica a decisão; o código a aplica. As listas abaixo são
> conferidas contra o código pelo teste 7 de `scripts/testar-cidades.py` — se
> divergirem, o teste falha. Não editar uma sem a outra.

## Dados que embasaram a decisão

| Item | Valor |
|---|---|
| Fonte | Google Search Console, API Search Analytics (propriedade `https://rcbseo.com.br/`) |
| Ferramenta | CLI `seo` v0.2.33, comando `gsc-query` |
| Período analisado | **12/05/2026 a 09/08/2026** (90 dias; 09/08 é o último dia com dado final) |
| Período de comparação | 11/02 a 11/05/2026 — **0 linhas**, as páginas ainda não existiam |
| Data de criação das páginas | **15/07/2026** (commit `d0b6222`) |
| Exposição real dentro da janela | **25 dias**, não 90 |

## O que os dados mostraram

| Métrica | Valor |
|---|---|
| Páginas de cidade publicadas | **199** |
| Com alguma impressão | **33** |
| Com clique | **0** |
| Sem nenhum sinal | **166** |
| Impressões do cluster | 101 (mais 12 no hub) |
| Participação no site | 3,1% das impressões, 0% dos cliques |
| Rendimento por página/dia | ~18x pior que o resto do site, já ajustado pela idade menor |
| Indexação (amostra de 14 via URL Inspection) | 10 indexadas, 4 em "Descoberta — não indexada" |

O dado que fechou a decisão foi o da indexação: as páginas **estão indexadas** e
mesmo assim não competem. Não é problema de descoberta.

## Ressalva — leia antes de citar estes números

**25 dias é uma janela curta.** Esta decisão **não** afirma que zero impressão em
25 dias prova incapacidade de ranquear. Não prova, e seria desonesto dizer que sim.

O que ela faz é outra coisa: **reduzir o footprint de páginas quase idênticas.**
Duas cidades quaisquer do template antigo são ~90% iguais palavra a palavra
(medido: 90,4% entre Aracaju e Botucatu). São 199 páginas assim, dois terços do
site. Esse padrão é o que a documentação do Google descreve como página-porta, e
o risco recai sobre o domínio inteiro — não só sobre as páginas fracas.

Retirar 168 delas do índice não custa clique nenhum, porque não há clique nenhum
a perder. É uma decisão de risco e higiene, **não** uma alavanca de tráfego.
`noindex` é uma meta tag: reversível numa linha, sem apagar arquivo.

## O que foi aplicado

- **31 páginas** continuam indexáveis e no sitemap.
- **168 páginas** receberam `<meta name="robots" content="noindex, follow">`.
  - **sem** `nofollow` — os links seguem valendo para o leitor e para o rastreamento;
  - **sem** bloqueio no `robots.txt` — com `Disallow` o Google nunca leria a tag;
  - **sem** redirect, **sem** exclusão, **sem** mudança de canonical;
  - continuam respondendo **HTTP 200** e continuam linkadas pelo hub, de propósito:
    o Google precisa rastrear a página para ver o `noindex` e retirá-la do índice.
- **Sitemap: 305 → 137 URLs.**

## As 3 páginas-piloto

Recebem conteúdo local próprio (não é o template ampliado). Texto em
`scripts/conteudo/cidades_piloto.py`, para sobreviver à regeração.

| Cidade | Sinal que justificou | Ângulo local da página |
|---|---|---|
| **Rio de Janeiro** | 28 impressões, 6 consultas comerciais | A busca se divide quase meio a meio entre "RJ" e "Rio de Janeiro"; disputa por zona, não por município |
| **Campinas** | 6 impressões, 3 consultas comerciais | Cliente na RMC (22 cidades); a praça procura "agência" e a RCB não é agência |
| **Palmas (TO)** | 2 consultas de intenção local pura — as únicas do cluster | Endereço por quadra (ARSO/ACSU/QI) que o Google Maps não interpreta |

Similaridade medida depois da reescrita (mesma metodologia do raio-X):
**90,4% no controle antigo → 35,8% a 39,1% nos pilotos.**

## Correção de dado: Palmas

`/consultoria-seo/palmas/` **é Palmas do Tocantins** (60.127 empresas ativas), e
sempre foi — título, schema e números publicados são de TO. A triagem de
`docs/triagem-cidades.md` a classificou por engano como Palmas/PR (5.393
empresas, score 3), porque o gerador desambiguava as duas cidades homônimas para
`palmas-to` e `palmas-pr` e nenhuma casava com a pasta publicada `palmas/` — a
página ficava órfã da geração. Resolvido em `rcb_cidades.SLUG_CANONICO`; o teste
6 impede a volta do problema.

## As 31 indexáveis

**Piloto (3)** — reescritas nesta rodada:

<!-- RCB:CIDADES-PILOTO:INICIO -->
`campinas`, `palmas`, `rio-de-janeiro`
<!-- RCB:CIDADES-PILOTO:FIM -->

**Congeladas (28)** — continuam indexáveis e no sitemap, **sem reescrita**, em
observação. São o grupo A da triagem (maiores praças) mais `brusque` e
`mogi-das-cruzes`, que tiveram sinal comercial acima do ruído apesar do score.
**Prazo: sem impressão até meados de outubro/2026, descem para `noindex`.**

<!-- RCB:CIDADES-CONGELADAS:INICIO -->
`anapolis`, `aparecida-de-goiania`, `balneario-camboriu`, `belo-horizonte`, `brasilia`, `brusque`, `campo-grande`, `contagem`, `cuiaba`, `curitiba`, `florianopolis`, `guarulhos`, `joinville`, `londrina`, `luziania`, `maringa`, `mogi-das-cruzes`, `niteroi`, `petrolina`, `porto-alegre`, `presidente-prudente`, `ribeirao-preto`, `rio-verde`, `sao-bernardo-do-campo`, `sao-paulo`, `sorocaba`, `uberlandia`, `vitoria`
<!-- RCB:CIDADES-CONGELADAS:FIM -->

## As 168 com `noindex`

Uma delas merece nota: **`duque-de-caxias` tinha 5 impressões** e mesmo assim
desceu. Motivo: ranqueava para `consultoria seo rio de janeiro` (pos. 87) e
`consultor seo rj` (pos. 83) — as mesmas consultas de `/rio-de-janeiro/`, e atrás
dela. Duas páginas nossas disputando a mesma SERP. A decisão foi concentrar.

<!-- RCB:CIDADES-NOINDEX:INICIO -->
`alvorada`, `americana`, `ananindeua`, `angra-dos-reis`, `aracaju`, `aracatuba`, `araguaina`, `arapiraca`, `arapongas`, `araraquara`, `araras`, `araucaria`, `atibaia`, `barra-mansa`, `barretos`, `barueri`, `bauru`, `belem`, `belford-roxo`, `bento-goncalves`, `betim`, `birigui`, `blumenau`, `boa-vista`, `botucatu`, `braganca-paulista`, `cabo-frio`, `cachoeirinha`, `cachoeiro-de-itapemirim`, `camacari`, `camboriu`, `campina-grande`, `campos-dos-goytacazes`, `canoas`, `caraguatatuba`, `carapicuiba`, `cariacica`, `caruaru`, `cascavel`, `caucaia`, `caxias-do-sul`, `chapeco`, `colombo`, `cotia`, `criciuma`, `diadema`, `divinopolis`, `dourados`, `duque-de-caxias`, `embu-das-artes`, `erechim`, `fazenda-rio-grande`, `feira-de-santana`, `fortaleza`, `foz-do-iguacu`, `franca`, `governador-valadares`, `gravatai`, `guarapari`, `guarapuava`, `guaruja`, `hortolandia`, `imperatriz`, `indaiatuba`, `ipatinga`, `itaborai`, `itabuna`, `itajai`, `itapema`, `itapetininga`, `itapevi`, `itaquaquecetuba`, `itu`, `jaboatao-dos-guararapes`, `jacarei`, `jaragua-do-sul`, `joao-pessoa`, `juazeiro-do-norte`, `juiz-de-fora`, `jundiai`, `lages`, `lauro-de-freitas`, `limeira`, `linhares`, `macae`, `macapa`, `maceio`, `mage`, `manaus`, `maraba`, `marica`, `marilia`, `maua`, `mogi-guacu`, `montes-claros`, `mossoro`, `natal`, `nova-friburgo`, `nova-iguacu`, `nova-lima`, `novo-hamburgo`, `olinda`, `osasco`, `palhoca`, `parauapebas`, `parnamirim`, `passo-fundo`, `patos-de-minas`, `paulista`, `pelotas`, `petropolis`, `pindamonhangaba`, `pinhais`, `piracicaba`, `pocos-de-caldas`, `ponta-grossa`, `porto-seguro`, `porto-velho`, `pouso-alegre`, `praia-grande`, `recife`, `ribeirao-das-neves`, `rio-branco`, `rio-claro`, `rio-das-ostras`, `rio-grande`, `rondonopolis`, `salvador`, `santa-barbara-d-oeste`, `santa-cruz-do-sul`, `santa-luzia`, `santa-maria`, `santana-de-parnaiba`, `santarem`, `santo-andre`, `santos`, `sao-caetano-do-sul`, `sao-carlos`, `sao-goncalo`, `sao-joao-de-meriti`, `sao-jose`, `sao-jose-do-rio-preto`, `sao-jose-dos-campos`, `sao-jose-dos-pinhais`, `sao-leopoldo`, `sao-luis`, `sao-vicente`, `serra`, `sertaozinho`, `sete-lagoas`, `sinop`, `sorriso`, `sumare`, `suzano`, `taboao-da-serra`, `taubate`, `teresina`, `teresopolis`, `toledo`, `tubarao`, `uberaba`, `valinhos`, `varginha`, `varzea-grande`, `viamao`, `vila-velha`, `vitoria-da-conquista`, `volta-redonda`
<!-- RCB:CIDADES-NOINDEX:FIM -->

## Autoridade interna recalculada

As 168 páginas com `noindex` continuam linkando para as money pages — o link
ainda serve ao leitor. Mas **eles não contam mais como fundamento da estratégia
de autoridade interna.** Números medidos por `scripts/contar-links-money.py`
(links editoriais, fora de navbar, rodapé e barra de CTA):

| Money page | Vindos de páginas indexáveis | Vindos das 168 noindex | Total bruto |
|---|---:|---:|---:|
| `/consultoria-seo-local/` | **101** | 168 | 269 |
| `/google-perfil-empresa/` | **81** | 168 | 249 |
| `/cases/` | **44** | 168 | 212 |
| `/seo-local-goiania/` | **22** | 0 | 22 |
| `/consultor-seo-goiania/` | **18** | 0 | 18 |
| `/diagnostico-presenca-digital/` | **140** | 0 | 140 |

`/cases/` é a que mais perde (212 → 44). **Não foi reforçada artificialmente**:
além dos 44 links editoriais, ela tem link fixo na navbar de todas as ~305
páginas do site. Não está subalimentada, e inflar o número com links plantados
repetiria o erro que esta rodada está corrigindo.

## Guard-rails

`python scripts/testar-cidades.py` — falha (código 1) se:

1. página da lista noindex estiver sem a meta robots;
2. página indexável estiver com noindex;
3. página noindex aparecer no sitemap;
4. página indexável faltar no sitemap;
5. cidade nova aparecer sem autorização (total diferente de 199, ou slug indexável sem pasta);
6. a colisão Palmas/TO x Palmas/PR voltar;
7. as listas deste documento divergirem de `rcb_cidades.py`;
8. o `robots.txt` passar a bloquear `/consultoria-seo/`.

## Baseline no momento do deploy

Registro do estado **imediatamente anterior** à mudança, para comparação futura.
Não interpretar movimento das próximas semanas como resultado.

- **Deploy:** _(preenchido após a publicação)_
- **Cluster inteiro (12/05–09/08):** 101 impressões, 0 cliques, 33 páginas com sinal.
- **Hub `/consultoria-seo/`:** 12 impressões, posição média 25,8.

| Piloto | Impressões | Cliques | Posição média | Consultas registradas |
|---|---:|---:|---:|---|
| `/rio-de-janeiro/` | 28 | 0 | 44,2 | consultoria seo rj (8); consultoria seo rio de janeiro (7); consultor seo rj (5); consultoria de seo no rio de janeiro (2); seo rio de janeiro (2); consultor seo em rj (1); falar com consultor de seo em rj (1); agência de seo rio de janeiro (1); agência de seo no rio de janeiro (1) |
| `/campinas/` | 6 | 0 | 65,0 | agência de seo em campinas (3); consultor seo campinas (1); agencia seo campinas (1) |
| `/palmas/` | 3 | 0 | 41,3 | seo local palmas (2); otimização para google meu negócio palmas (1) |

## Próxima revisão

Meados de **outubro/2026** (60 dias). Duas perguntas:

1. As 3 pilotos ganharam impressão e posição? Se sim, a tese de página geográfica
   com conteúdo real se sustenta e vale escolher a próxima leva.
2. Alguma das 28 congeladas continua em zero? Se sim, desce para `noindex`.

**A prioridade número 1 continua sendo off-page.** Esta rodada não muda isso: o
site teve 16 cliques em 90 dias, 7 deles na home. O funil está vazio na entrada.
