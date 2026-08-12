# HANDOFF OFF-PAGE — 12/08/2026

Memória operacional da fase de autoridade externa. Leia antes de retomar.
Planilha de oportunidades: `docs/offpage-oportunidades.csv` (17 linhas, com score).

## Diagnóstico central

**A pegada externa da RCB é praticamente zero.** Buscas por `"RCB Consultoria"`,
`rcbseo.com.br` e `Renan Carvalho Barbosa SEO` retornam **apenas o próprio site**.
Não há menção sem link para converter em backlink — não há menção nenhuma.
Isso explica a posição média 38,9 melhor que qualquer ajuste on-page.

## Concorrentes encontrados

**Goiânia:** `atomdigital.com.br` (2013, Setor Bueno) · `ideiagoias.com.br` ·
`otimizemarketing.com.br` (marketing médico/odonto — **overlap direto de nicho**) ·
`agenciazig.com.br` (26 pessoas) · `webcer.digital` · `caixinhacriativa.com.br` ·
`salazardigital.com.br` · `digitalfinder.com.br` · `i2a.com.br` ·
`maxytetsu.com.br` · `controldigital.com.br` · `google.goiania.br`

**Fora de Goiânia, disputando o termo:** `hostconect.com.br` · `divia.com.br` ·
`agenciahelpu.com` · `serpup.com.br` · `cleberbarbosa.com.br` · `marcusbtc.com.br`

Ressalva: **não foi reproduzida SERP neutra de Goiânia** (ferramenta daqui é US-only /
busca semântica). A lista é "quem compete", não "quem está em que posição".

## Achado principal: Grupo Ideia Goiás

`ideiagoias.com.br/grupo-ideia-goias` anuncia abertamente **"imprensa própria"**,
**"17 jornais"**, "controle direto de distribuição digital", "geração de backlinks
naturais" e "presença simultânea em múltiplos sites". É uma rede de publicação
própria, focada em **marketing médico** — o nicho mais maduro da RCB.
É concorrente **e** fornecedor potencial de publicação paga.
Risco médio-alto: rede própria = footprint compartilhado entre muitos clientes.

## Concorrentes de fora com landing page para Goiânia

`hostconect.com.br/consultoria-seo-goiania/` tem telefone (11), é de São Paulo, roda
página de cidade para Goiânia e **publica preço de R$ 650 a R$ 1.200/mês**.
`divia.com.br` e `agenciahelpu.com` fazem o mesmo. Os pacotes da RCB começam em
R$ 2.997/mês recorrente. **Isso é questão de posicionamento comercial, não de SEO.**

## Nalu Prado — VERIFICAR PRIMEIRO

`naluprado.com.br` está no ar. **O site foi desenvolvido pelo Renan**, então é
possível que **já exista crédito/link para a RCB** — isso não foi verificado.
**Primeira tarefa da próxima sessão:** abrir o site e checar rodapé, página de
história e páginas internas atrás de link existente.
- Se já existe: confirmar se é follow e para qual URL aponta.
- Se não existe: pedir crédito editorial ("Site e SEO local por RCB Consultoria"),
  destino `/cases/`, onde o case dela já está documentado.

## Docevidade — oportunidade futura

`docevidade.com.br` **não resolve** — o cliente ainda não tem site. O case atual é de
Google Perfil da Empresa (Maps). **O site será desenvolvido pelo Renan**, então haverá
oportunidade legítima de crédito/backlink no lançamento. Deixar previsto no projeto.

## Top 10 ações propostas

1. Link da Nalu Prado (verificar se já existe; se não, pedir) → `/cases/` · R$ 0
2. Confirmar situação do site da Docevidade e prever crédito no desenvolvimento
3. Artigo no LinkedIn com o case da Nalu → `/cases/` (espaço vazio: maior
   concorrente local tem 1.646 seguidores)
4. Associar-se à ACIEG — `acieg.com.br/associados/`
5. Associar-se à CDL Goiânia, plano "Sou MEI" — `cdlgoiania.com.br/associe-se/`
6. Oferecer-se como fonte à Agência Sebrae Goiás — contato público:
   Adrianne Vitoreli, (62) 98144-2178
7. Propor entrevista ao Curta Mais (`curtamais.com.br/goiania/`) — formato já existe
8. Fechar 4 citações NAP: GuiaMais, Apontador, TeleListas, Solutudo (quase todas
   nofollow — ganho é para o Perfil da Empresa, não para o orgânico)
9. Vídeo no YouTube sobre erros de Google Meu Negócio em Goiânia →
   `/google-perfil-empresa/`
10. Avaliar (**não comprar**) publicação na rede do Ideia Goiás: pedir lista dos 17
    jornais e preços antes de decidir

## Oportunidades locais já verificadas

`acieg.com.br/associados/` · `cdlgoiania.com.br/associe-se/` ·
`go.agenciasebrae.com.br` · `curtamais.com.br/goiania/` · `ficomex.acieg.com.br` ·
`ideiagoias.com.br`. Detalhes, custo, contato e destino no CSV.

## O que NÃO foi pesquisado

- **Backlinks dos concorrentes** — não há ferramenta nesta máquina: Bing Webmaster
  não conectado, sem Ahrefs, sem DataForSEO. Só foram confirmados perfis do LinkedIn.
- **Marketplaces de guest post / niche edit** com preço.
- **Domínios expirados** — avaliar exige checar Archive.org, anchors históricos e
  sinais de spam um a um. Nada foi levantado; **não inventar candidato**.

## Próxima fase

1. **Verificar o backlink já existente da Nalu Prado** (tarefa nº 1, custo zero).
2. Seguir com prospecção off-page concreta, **um alvo por rodada**:
   (a) 20 oportunidades locais de GO com URL verificada, ou
   (b) marketplaces de guest post/niche edit com preço, ou
   (c) candidatos a domínio expirado com checagem de histórico.

**NÃO voltar para auditoria on-page agora.** A fase interna está encerrada: a poda
das cidades foi publicada em 12/08 (`docs/decisao-cidades-2026-08-12.md`) e o gargalo
medido é autoridade externa, não qualidade técnica.

## Ferramenta já configurada — não reinvestigar

O **CLI `seo` v0.2.33** (npm, pacote `seo`, mantenedor iannuttall) está **instalado
globalmente e autenticado no Google** como `renancb@gmail.com`, com escopo de
**leitura** do Search Console e do Analytics. App OAuth compartilhado do próprio CLI —
não foi criado projeto no Google Cloud nem `client_secret.json`.

- Propriedade correta: **`https://rcbseo.com.br/`** (a variante `sc-domain:` existe mas
  está como `siteUnverifiedUser` e não serve).
- Comando que dá dado bruto: `seo gsc-query --site "https://rcbseo.com.br/" --body-file <json>`
  — aceita corpo da Search Analytics API, então faz `page + query` na mesma linha
  (a interface do Search Console não faz isso).
- `seo url-inspect` funciona para checar indexação.
- Token expira em ~1h; renovar com `seo auth refresh`.
- **Não há comando de reenvio de sitemap ao Search Console** — isso continua manual.
- IndexNow: usar `scripts/indexnow.py` (chave fixa do projeto).
  **Não** usar `seo indexnow setup`, que geraria chave nova.
