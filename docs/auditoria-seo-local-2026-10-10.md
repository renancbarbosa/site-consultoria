# Auditoria de SEO local — rcbseo.com.br (10/10/2026)

Só diagnóstico: nenhum arquivo do site foi alterado, nada foi commitado nem publicado.
Fontes: os 182 arquivos HTML do projeto, o `sitemap.xml` (179 endereços), o `llms.txt`, o `llms-full.txt`,
o `data/marca.json` e as páginas baixadas do site no ar hoje (home, contato, sobre, `/consultor-seo-goiania/`,
`/seo-local-goiania/`, `/consultoria-seo-local/`), além de duas buscas na web pelo nome da marca e do Renan.

---

## Resumo em 5 linhas

1. **Nota geral: 50/100.** O site em si está bem montado para Goiânia; o que puxa a nota para baixo é o que acontece **fora** dele.
2. **Problema 1: avaliações.** O perfil tem 3 avaliações (dado do próprio projeto); o concorrente analisado tem 42. Avaliação é cerca de 20% do peso do mapa, e o site não tem nenhum botão "avalie no Google".
3. **Problema 2: o site não leva ao perfil do Google.** Nenhuma das 182 páginas tem um link clicável para o perfil no Maps. O mapa aparece só na página de contato.
4. **Problema 3: quase nenhuma presença fora do site.** Na busca, só aparece o próprio rcbseo.com.br: nenhum diretório (guia de empresas) e nenhum perfil de terceiros. É desses lugares que ChatGPT e Copilot tiram recomendação local.
5. De quebra, os arquivos que as IAs leem estão **desatualizados**: dizem que o perfil no Maps se chama "RCB Consultoria" (ele foi renomeado para "RCB SEO" em 06/10), e a cópia do site guardada pelo buscador ainda mostra preço ("a partir de R$ 1.997").

---

## Nota por área

| Área | Peso | Nota | Comentário curto |
|---|---|---|---|
| Ligação site ↔ perfil do Google | 25 | 12 | Ficha técnica aponta para o perfil, mas o visitante não tem onde clicar |
| Avaliações | 20 | 6 | 3 avaliações, sem botão para avaliar |
| Páginas locais (Goiânia e região) | 20 | 14 | Bons títulos e rodapé completo; falta página "Google Meu Negócio em Goiânia" |
| Nome, endereço e telefone + diretórios | 15 | 8 | Igual em todo o site; zero diretórios encontrados |
| Ficha técnica local (schema) | 10 | 8 | Completa; dois detalhes a acertar |
| Autoridade local (links de fora) | 10 | 2 | Só os 2 sites do próprio Renan linkam |
| **Total** | **100** | **50** | |

**Tipo de negócio detectado:** híbrido. Tem endereço físico na rua (residencial, atendimento com agendamento) e atende online o Brasil inteiro.
**Ramo:** serviço profissional de marketing (não se encaixa em saúde, jurídico, restaurante etc.).

---

## O que está bom (não mexer)

- **Nome, endereço e telefone iguais em 179 das 182 páginas.** O rodapé traz sempre "Rua 18-A, nº 256, Goiânia - GO, CEP 74070-060" e "(62) 99116-1040". As 3 páginas sem rodapé são de propósito (`404`, a demonstração do diagnóstico e o modelo de landing page, as duas em noindex).
- **Ficha técnica (schema) local completa** na home, contato e `/seo-local-goiania/`: tipo `ProfessionalService` + `LocalBusiness`, endereço, telefone, e-mail, coordenadas do mapa (latitude e longitude), link do perfil (`hasMap`), Instagram, horário, área atendida (Goiânia, Aparecida, Anápolis, Trindade, Senador Canedo e Brasil). JSON válido.
  - *Schema = um "cartão de visita" escondido no código que só o Google e as IAs leem.*
- **Telefone e WhatsApp sempre o mesmo número** (1.219 botões de WhatsApp, todos para 5562991161040).
- **Páginas de Goiânia com título e H1 certos:** `/consultor-seo-goiania/`, `/seo-local-goiania/`, `/criacao-de-sites-goiania/`, `/criacao-de-loja-virtual-goiania/` e a home ("Site e Google que Trazem Cliente | Goiânia | RCB SEO").
  - *H1 = o título grande que aparece no topo da página.*
- **Região metropolitana e interior com página própria:** Anápolis, Aparecida de Goiânia, Luziânia e Rio Verde.
- **Robôs de IA liberados:** o `robots.txt` permite GPTBot, ClaudeBot, PerplexityBot, Google-Extended, e todos recebem a página normalmente (testado hoje: resposta 200).
- **Mapa incorporado na página de contato**, com carregamento preguiçoso (não pesa a página).
- **Arquivos internos protegidos:** testei `count.py`, `count.js` e `graphify-out/`, todos respondem 404 no ar.

---

## Correções no SITE (em ordem de prioridade)

### 🔴 Urgente

**S1. Corrigir o nome do perfil nos arquivos que as IAs leem**
- **O que está errado:** o `llms.txt` (linha 3) e o `llms-full.txt` (linha 11) dizem: *"Também aparece como RCB Consultoria (nome atual do perfil no Google Maps)"*. O perfil foi renomeado para "RCB SEO" em 06/10/2026.
- **Por que importa:** esses arquivos são um resumo do negócio feito para ChatGPT, Claude e Perplexity. Se eles leem "o perfil se chama RCB Consultoria" e no Maps está "RCB SEO", a IA pode achar que são empresas diferentes, ou confundir com a outra "RCB Consultoria" de Anápolis.
- **Esforço:** 5 minutos (trocar uma frase em dois arquivos). Manter "RCB Consultoria" apenas como "nome antigo".

**S2. Colocar um link clicável para o perfil do Google e um botão "Avalie no Google"**
- **O que está errado:** nenhuma página tem link clicável para o perfil (`google.com/maps?cid=...`). O endereço do perfil existe só dentro da ficha técnica e no mapa da página de contato. Também não existe link para deixar avaliação.
- **Por que importa:** o site é o lugar natural para o cliente satisfeito chegar ao perfil e avaliar. E o link visível reforça para o Google que site e perfil são o mesmo negócio.
- **Esforço:** baixo (1–2 horas): link "Ver no Google Maps" no rodapé (que é repetido em todas as páginas por script) e um botão "Deixe sua avaliação" na página de contato e na de cases. O link de avaliação é gerado no painel do perfil ("Pedir avaliações"); preciso que você me mande esse link.

**S3. Acertar o horário: 8h ou 9h?**
- **O que está errado:** a página de contato diz, em texto, *"Segunda a sexta, das 9h às 18h"*. A ficha técnica de 11 páginas diz que abre às **08:00**.
- **Por que importa:** o Google cruza horário do site, da ficha técnica e do perfil. Informação diferente em cada lugar enfraquece a confiança nos dados. E "estar aberto na hora da busca" pesa no mapa.
- **Esforço:** 10 minutos, depois que você me disser qual é o horário certo (e qual está no perfil).

### 🟠 Importante

**S4. Criar uma página "Google Meu Negócio em Goiânia"**
- **O que está errado:** o serviço que é o coração do negócio (Google Meu Negócio) só tem páginas nacionais (`/google-perfil-empresa/`, `/consultoria-seo-local/`) ou de clínicas. Para Goiânia existem SEO local, consultor, site e loja virtual, mas não "Google Meu Negócio em Goiânia" / "otimização de perfil no Google em Goiânia".
- **Por que importa:** ter **uma página por serviço** é o fator nº 1 das buscas locais (pesquisa Whitespark 2026). O dono que busca "google meu negócio goiânia" hoje não encontra uma página feita para ele.
- **Esforço:** médio (meio dia, com o gerador que já existe). Cuidado para não brigar com `/seo-local-goiania/`: uma fala de "aparecer no Google e no Maps" no geral, a outra só do perfil.

**S5. Atualizar a cópia antiga que o buscador ainda guarda**
- **O que está errado:** a busca de hoje por "RCB SEO Goiânia" devolveu trechos antigos: *"a partir de R$ 1.997"*, *"site pronto em 7 dias"* e o título antigo da home ("SEO Local e Google Meu Negócio para Negócios Locais"). O site não tem mais preço desde 28/09.
- **Por que importa:** buscadores desse tipo alimentam as respostas do ChatGPT e do Copilot. Um cliente pode perguntar à IA e ouvir um preço que não existe mais.
- **Esforço:** baixo. Reenviar ao IndexNow as páginas principais (home, serviços, cidades de Goiás) e, no Bing Webmaster Tools, pedir novo rastreamento. Depois, paciência: pode levar semanas.

**S6. Deixar as páginas de cidade mais diferentes entre si**
- **O que está errado:** medi o texto de várias páginas de cidade de fora de Goiás: **Curitiba e Londrina têm 60% do texto igual; Cuiabá e Vitória, 63%.** O ideal é pelo menos 60% de texto **próprio**. As de Goiás (Anápolis, Aparecida, Rio Verde) estão melhores: 40–45% igual.
- **Por que importa:** o Google chama página que só troca o nome da cidade de "página porta" (doorway) e pode rebaixar o site inteiro. O teste é simples: se dá para trocar "Curitiba" por "Londrina" e o texto continua fazendo sentido, é risco.
- **Esforço:** alto (texto próprio por cidade). Sugestão: começar pelas 10 com mais impressões no Search Console; as de Goiás são as mais importantes para o perfil local.

**S7. Telefone clicável**
- **O que está errado:** o telefone aparece escrito em 185 lugares, mas **nenhum** é clicável para ligar (link `tel:`). Só o WhatsApp é clicável.
- **Por que importa:** no celular, quem prefere ligar precisa copiar o número. Pouca coisa no ranking, mas é um contato perdido.
- **Esforço:** baixo (trocar no rodapé por script).

### 🟢 Bom ter

**S8. Nome da marca no rodapé.** O rodapé mostra "RCB" (logo) + "Renan Carvalho Barbosa", e não "RCB SEO" escrito por extenso perto do endereço. Para o Google, o "N" do nome-endereço-telefone fica mais claro com "RCB SEO — Renan Carvalho Barbosa". Esforço: baixo.

**S9. Duas fichas de empresa diferentes.** A página `/consultor-seo-goiania/` declara a empresa com outro identificador (`.../consultor-seo-goiania/#business`), enquanto o resto do site usa `https://rcbseo.com.br/#business`. Para o Google pode parecer uma segunda empresa. **Essa página é protegida** — só mexer com sua autorização expressa. Esforço: 5 minutos.

**S10. Nota de avaliação na ficha técnica da home.** A home declara "nota 5, 3 avaliações" com os 3 depoimentos. Não está errado (os depoimentos estão visíveis), mas o Google **não mostra estrelinha** para avaliação que a própria empresa publica. Serve para IA, não para a busca. Só cuidado: quando o perfil tiver mais avaliações, esse número fica velho. Esforço: nenhum agora.

**S11. Endereço sem bairro.** Endereço aparece como "Rua 18-A, nº 256, Goiânia - GO". Se no perfil do Google aparece com o bairro, vale acrescentar igual no site. Preciso do print para conferir.

**S12. Link do perfil diferente no `llms-full.txt`.** Ele usa `share.google/sYd1qgUhLvw0u4cHL`; o resto do site usa `google.com/maps?cid=740760530295214944`. Provavelmente é o mesmo perfil, mas o ideal é um link só em todo lugar.

---

## Ajustes no PERFIL do Google Meu Negócio

Não consegui ver o painel do seu perfil, então os itens abaixo são **o que conferir**, não afirmações sobre o que está lá.
Do perfil eu só sei o que está registrado no projeto: nome "RCB SEO" (desde 06/10), 3 avaliações, descrição e serviços refeitos em 06/10 (31 + 3), produtos e postagens começados, links com etiqueta de rastreio (UTM).

### 🔴 Urgente

**P1. Plano de avaliações com ritmo constante**
- **O que fazer:** pedir avaliação a todos os clientes atendidos (Nalu Prado, Docevidade e os demais), mandando o link direto pelo WhatsApp. Meta: chegar a **10** (é a faixa em que o efeito costuma aparecer) e depois manter **pelo menos 2 por mês**, sem ficar semanas parado.
- **Por que importa:** avaliação pesa cerca de 20% no mapa. O concorrente que aparece na sua frente (Máximos Digital) ganha principalmente por ter 42.
- **Regras para não ser punido:** pedir para **todos** (não só para quem você sabe que está satisfeito — filtrar antes é proibido pelo Google), nunca oferecer nada em troca, nunca pedir para amigos que não foram clientes.
- **Esforço:** baixo, mas contínuo. É o item de maior retorno de toda a auditoria.

**P2. Responder todas as avaliações**, inclusive as antigas, citando o serviço feito ("obrigado pela confiança no projeto do site e do Google Meu Negócio"). Esforço: 10 minutos.

### 🟠 Importante

**P3. Categorias**
- A categoria principal é o fator nº 1 do mapa, e a errada é o fator negativo nº 1.
- Conferir se a principal é a que melhor descreve o serviço central (algo como "Consultor de marketing" ou "Serviço de otimização para mecanismos de busca", se existir na lista do Google em português) e usar até 4 secundárias que batam com o site: criação de sites, marketing na internet, publicidade. **Não use** categoria de algo que você não faz (social media, por exemplo).
- Preciso do print das categorias atuais para dizer se trocaria alguma.

**P4. Horário igual ao site** (ver S3). Escolher um só e usar nos três lugares.

**P5. Endereço visível ou escondido?**
- O endereço é residencial. Se no perfil ele está **escondido** (só área de atendimento), o site está mostrando um endereço que o perfil não mostra, e isso é uma divergência.
- Se está **visível**, está coerente com o site. Mas lembre: atendimento com hora marcada em casa é aceito pelo Google desde que você atenda lá de verdade.
- Preciso do print para saber qual é o caso.

**P6. Cadastro no Bing Places e no Apple Business**
- **Por que importa:** o ChatGPT e o Copilot **não leem o perfil do Google**. Eles usam o Bing. O Bing Places dá para importar direto do perfil do Google em poucos minutos. O Apple Business alimenta o Mapas do iPhone e a Siri.
- **Esforço:** 30 minutos cada.

**P7. Diretórios brasileiros** (já estava na lista de pendências do projeto): GuiaMais, Apontador, TeleListas, Solutudo, ACIEG/CDL, página de empresa no LinkedIn (o `marca.json` ainda está com `linkedin_empresa: null`). Usar **exatamente** o mesmo nome, endereço e telefone do site. Esforço: 2–3 horas, uma vez só.

### 🟢 Bom ter

**P8. Fotos novas todo mês**: de você trabalhando, reunião com cliente (com autorização), tela de resultado (sem dados de cliente). Perfis com fotos recebem bem mais pedidos de rota.

**P9. Postagem toda semana**, alternando os quatro serviços do site (SEO/Google Meu Negócio, sites e landing pages, Google Ads, SEO para YouTube). Postagem não sobe a posição sozinha, mas o Google às vezes mostra um trecho dela no resultado.

**P10. Perguntas e respostas:** o Google está desativando essa área. Coloque as perguntas mais comuns no FAQ do site (já existe) e no texto da descrição.

**P11. Link do site no perfil:** hoje aponta para a home com etiqueta de rastreio (UTM), o que está certo para um negócio de um endereço só. Não trocar sem motivo.

---

## O que eu preciso de você (prints do perfil)

Para fechar a parte do perfil sem chutar, me mande print de:

1. **Categorias** (principal e secundárias).
2. **Endereço**: se aparece para o público ou se está como "área de atendimento".
3. **Horário de funcionamento**.
4. **Avaliações**: número, nota e data da mais recente.
5. **Descrição** do perfil.
6. **Fotos**: quantas tem e de quando é a última.
7. **Link "Pedir avaliações"** (para o botão do item S2).
8. Se possível, a tela **"Desempenho"** dos últimos 3 meses (buscas, ligações, rotas, cliques no site).

---

## O que esta análise NÃO conseguiu avaliar

- **O painel do seu perfil no Google**: categorias, descrição, fotos, avaliações, horário, desempenho. Nada disso foi inventado aqui; tudo o que está na seção do perfil é "o que conferir".
- **Posição no mapa por bairro** (o chamado *geo-grid*: ver em que lugar você aparece no Maps em cada ponto da cidade). Exige ferramenta paga (Local Falcon, BrightLocal).
- **Lista completa de quem linka para o site** e força do domínio. Exige Ahrefs, Semrush ou Moz (pagos). Só sei dos 2 sites próprios (Nalu e Radar).
- **Diretórios um por um**: fiz duas buscas na web e não apareceu nenhum diretório. Isso indica ausência, mas não prova. Conferir à mão em cada guia.
- **O que as IAs respondem de fato** quando alguém pergunta "consultor de SEO em Goiânia" no ChatGPT, Gemini ou Perplexity: não tenho acesso a elas daqui. O protocolo de 20 perguntas para você testar está em `docs/AUDITORIA_SEO_GEO_AIO_2026-09-08.md`.
- **Dados novos do Search Console**: não puxei nesta rodada (o foco era SEO local, não posição orgânica).
- **Velocidade do site**: fora do escopo; a última medição está na auditoria de 08/09.

---

### Observação sobre o projeto

O `sitemap.xml` aparece como "modificado" no git, mas a única diferença é o tipo de quebra de linha (Windows × Linux), não o conteúdo. Não mexi nele.
