# Pesquisa própria: "Quem a IA indica em Goiânia?"

Para o artigo `/blog/quem-a-ia-indica-em-goiania/`. **Quem roda as perguntas é o Renan**: daqui não há
acesso ao ChatGPT nem ao Gemini. O artigo só é gerado com dados reais (o gerador vai recusar planilha
vazia, como o do teste de velocidade das clínicas).

## Por que vale o esforço
É o tipo de conteúdo que as IAs e os jornalistas citam: dado original, de Goiânia, que ninguém mais tem.
Também vira assunto de conversa com cada empresa que aparecer (ou não) na tabela.

## Como fazer (uma tarde, cerca de 2 horas)

1. **ChatGPT:** abra um **chat temporário** (ícone no topo, "Chat temporário"), para a memória da sua
   conta não influenciar. Confira que a busca na internet está ligada.
2. **Gemini:** gemini.google.com, conversa nova.
3. Cole **exatamente** a pergunta da lista, uma por conversa (conversa nova a cada pergunta).
4. Anote na planilha: cada empresa citada, na ordem em que aparece, e o site que a IA mostrou como fonte
   (quando mostrar). Tire print de cada resposta e guarde numa pasta.
5. Se sobrar tempo, repita no Perplexity (perplexity.ai) e no Copilot (copilot.microsoft.com).
6. Faça tudo no **mesmo dia**. Data na planilha no formato AAAA-MM-DD.

## As 20 perguntas (sempre com "em Goiânia")

| # | Ramo | Pergunta |
|---|---|---|
| 1 | Dentista | Qual dentista você indica em Goiânia? |
| 2 | Clínica de estética | Qual clínica de estética é boa em Goiânia? |
| 3 | Advogado trabalhista | Qual advogado trabalhista você indica em Goiânia? |
| 4 | Contador | Qual escritório de contabilidade você indica em Goiânia para pequena empresa? |
| 5 | Psicólogo | Qual psicólogo você indica em Goiânia? |
| 6 | Veterinário | Qual clínica veterinária é boa em Goiânia? |
| 7 | Pet shop | Qual pet shop você indica em Goiânia? |
| 8 | Imobiliária | Qual imobiliária é confiável em Goiânia? |
| 9 | Energia solar | Qual empresa de energia solar você indica em Goiânia? |
| 10 | Eletricista | Qual eletricista você indica em Goiânia? |
| 11 | Dedetizadora | Qual dedetizadora é boa em Goiânia? |
| 12 | Guincho | Qual guincho 24 horas você indica em Goiânia? |
| 13 | Limpeza de estofados | Qual empresa de higienização de sofá você indica em Goiânia? |
| 14 | Reformas | Qual empresa de reformas é confiável em Goiânia? |
| 15 | Oficina mecânica | Qual oficina mecânica é boa em Goiânia? |
| 16 | Fisioterapia | Qual clínica de fisioterapia você indica em Goiânia? |
| 17 | Academia | Qual academia é boa em Goiânia? |
| 18 | Salão de beleza | Qual salão de beleza você indica em Goiânia? |
| 19 | Escola de idiomas | Qual escola de inglês é boa em Goiânia? |
| 20 | Confeitaria | Onde comprar macarons em Goiânia? |

(A nº 20 é a do case da Docevidade: mostra se o 1º lugar no Maps também vira indicação da IA.)

## Planilha

Arquivo: `data/pesquisa-ia-goiania.csv` (a pasta `data/` não é publicada). Uma linha por empresa citada.
Se a IA não citou nenhuma empresa, uma linha com `empresa_citada` vazio e a observação.

```
data,assistente,pergunta_num,posicao,empresa_citada,fonte_url,observacao
2026-11-05,ChatGPT,1,1,Clínica Exemplo,https://exemplo.com.br/,citou site e avaliações
2026-11-05,Gemini,1,,,,não citou empresa; mandou procurar no Google Maps
```

## O que o artigo vai mostrar (só com os dados em mãos)
- Em quantos ramos cada IA citou empresas com nome, e em quantos se recusou ou mandou "procurar no Maps".
- Quantas empresas foram citadas pelas duas IAs ao mesmo tempo.
- Que tipo de fonte apareceu mais (site da empresa, Google Maps, diretório, notícia).
- O que as empresas citadas têm em comum (site, perfil no Google completo, avaliações), conferido à mão.

Regras: sem conclusão que os números não sustentem; empresas citadas aparecem como a IA respondeu,
sem juízo sobre elas; nenhuma crítica a concorrente.
