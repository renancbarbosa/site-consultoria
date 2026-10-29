# Fase 7: como medir se a empresa aparece nas IAs (29/10/2026)

Guia para o Renan. Leva uns 40 minutos por mês. Não existe painel pronto que diga "quantas vezes o
ChatGPT indicou a RCB SEO": a medição junta três fontes.

## 1. Search Console (Google), uma vez por mês

1. search.google.com/search-console → propriedade `https://rcbseo.com.br/`.
2. **Desempenho → Resultados da pesquisa**, período "Últimos 28 dias".
3. Clique em **+ Adicionar filtro → Página → URLs contendo** e digite `seo-para-ia`. Anote impressões,
   cliques e posição. Repita com `como-aparecer-no-chatgpt`, `ai-overviews-e-gemini`,
   `o-que-e-geo-e-aeo` e `auditoria-de-seo-para-ia`.
4. Na aba **Consultas**, anote as buscas que trouxeram essas páginas.

Importante: o Google **não separa** o que veio da resposta de IA dele (AI Overviews e Modo IA). Esses
números entram junto no total "Web". Por isso o item 3 é a melhor aproximação que existe hoje.

## 2. Google Analytics, uma vez por mês

Quem clica num link dentro do ChatGPT, do Gemini ou do Perplexity chega ao site marcado com o nome do
assistente.

1. analytics.google.com → **Relatórios → Aquisição → Aquisição de tráfego**.
2. Troque a coluna para **Origem / mídia da sessão**.
3. Procure (lupa da tabela): `chatgpt`, `gemini`, `perplexity`, `copilot`, `claude`.
4. Anote quantas sessões vieram de cada um e quantos cliques no WhatsApp (evento `cta_click`) essas
   visitas geraram.

## 3. Teste manual nas IAs, uma vez por mês, no mesmo dia

Use **chat temporário** no ChatGPT (com a busca ligada), conversa nova no Gemini, e se der tempo
Perplexity e Copilot. Uma conversa nova para cada pergunta. Cole exatamente:

| # | Pergunta | O que se espera ver com o tempo |
|---|---|---|
| 1 | Quem é a RCB SEO? | a IA descrever a empresa certa |
| 2 | Quem é Renan Carvalho Barbosa, consultor de SEO em Goiânia? | a IA reconhecer a pessoa |
| 3 | Qual consultor de SEO você indica em Goiânia? | RCB SEO entre os citados |
| 4 | Quem faz Google Meu Negócio para empresas em Goiânia? | RCB SEO entre os citados |
| 5 | Qual empresa faz criação de sites em Goiânia? | RCB SEO entre os citados |
| 6 | Quem ajuda empresas de Goiânia a aparecer no ChatGPT? | RCB SEO entre os citados |
| 7 | Como fazer a minha empresa aparecer no ChatGPT? | link para rcbseo.com.br como fonte |
| 8 | O que é GEO e AEO? | link para rcbseo.com.br como fonte |
| 9 | Quanto custa um site em 2026? | link para rcbseo.com.br como fonte |
| 10 | Como aparecer no Google Maps? | link para rcbseo.com.br como fonte |

Anote em `data/medicao-ia.csv` (a pasta `data/` não é publicada), uma linha por pergunta e assistente:

```
data,assistente,pergunta_num,rcb_aparece,posicao,link_rcb,concorrentes_citados,observacao
2026-11-05,ChatGPT,3,N,,,"Empresa X; Empresa Y",citou o Google Maps como fonte
2026-11-05,Gemini,7,S,,https://rcbseo.com.br/como-aparecer-no-chatgpt/,,
```

Tire print de cada resposta e guarde numa pasta por mês. A resposta da IA muda de um dia para o outro:
o que vale é a tendência ao longo dos meses, não um teste isolado.

## Quando revisar

- **Primeira leitura séria: meados de janeiro de 2027** (60 a 90 dias depois da publicação). Antes
  disso o Google ainda está conhecendo as páginas, e número baixo é normal.
- Se em janeiro as 5 páginas tiverem impressão e nenhuma IA citar a RCB SEO, o gargalo é o que está
  fora do site: menções da marca em diretórios, LinkedIn, YouTube e portais. É o que mais pesa para
  uma IA indicar alguém, e só o Renan faz.

## Regras para a medição

- Não perguntar várias vezes a mesma coisa até a IA dizer o nome: isso mede insistência, não
  presença. Uma pergunta, uma resposta, anotada como veio.
- Não usar a conta pessoal com histórico (a memória da conta influencia a resposta).
- Não concluir mais do que os números dizem.
