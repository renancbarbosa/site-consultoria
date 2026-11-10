# Auditoria de SEO — 09/11/2026

Branch local: `auditoria-2026-11-09`. **Nada publicado.** Cada correção é um commit separado,
para o Renan aprovar ou desfazer um por um antes do `git push`.

## 1. Como foi medido
- siteone-crawler (243 URLs, crawl em baixa velocidade), lighthouse, pa11y, lychee.
- Search Console via CLI `seo`, 90 dias: **9.018 impressões, 58 cliques, posição média 24,3**.
- Código local e site no ar conferidos idênticos antes de começar.
- Linha de base de monitoramento (seo-drift) gravada em 10/11/2026 para 9 páginas do site no ar:
  `/`, `/consultor-seo-goiania/`, `/google-perfil-empresa/`, `/seo-local-goiania/`,
  `/criacao-de-sites-goiania/`, `/consultoria-seo-local/`, `/seo-para-dentistas/`,
  `/blog/quanto-custa-otimizar-google-meu-negocio/`, `/contato/`.
  Depois de publicar: `drift_compare.py <url> --skip-cwv` mostra o que mudou.

## 2. Notas (antes das correções)
| Área | Nota |
|---|---|
| Técnico | 92 |
| Conteúdo | 74 |
| SEO local | 50 |
| Visibilidade em IA | 66 |
| Velocidade | 76 |
| Acessibilidade | 96 |
| **Geral** | **≈ 73** |

O ponto fraco é o local: poucas avaliações, sinais de Maps espalhados, nenhum botão de ligar ou
avaliar fora da página de contato.

## 3. O que foi corrigido (commits locais)
| # | Commit | O que mudou |
|---|---|---|
| 1 | `2e31c263` | Preço da RCB que tinha sobrado ("R$ 1.997") saiu de `/google-perfil-empresa/` e de um artigo; conferidor de preço consertado (deixava passar "R$ 1.997,") |
| 2 | `63057f6e` | `llms.txt`: nome no Maps é RCB SEO; link `share.google` trocado pelo link fixo do Maps |
| 3 | `4c0aa0b9` | Rodapé local em 185 páginas: Ligar, Ver no Google Maps, Avaliar no Google, horário. Gerador de cidades parou de apagar o YouTube |
| 4 | `27e5f45b` | **Página nova** `/google-meu-negocio-goiania/` (2.108 palavras) + menu, rodapé, 22 caixas de texto ligando a ela e à página do consultor. Sitemap 186 → 187 |
| 5 | `4c6f4722` | **Página protegida** `/consultor-seo-goiania/`: fonte local (era a mais lenta do site), ficha técnica unificada com o resto do site, rodapé local, itens novos do menu. Título, H1 e textos intocados |
| 6 | `1a52601b` | Link "Início" quebrado em 2 artigos; arquivo de auditoria antigo movido da raiz para `docs/` |
| 7 | `63a4b94f` | Páginas que recebiam menos de 3 links internos: 19 → 0 |
| 8 | `c9446856` | Home: título aparece já na primeira pintura (o maior elemento medido era o aviso de cookies) |
| 9 | `655b3024` | Links no meio do texto agora dourados e sublinhados (antes não pareciam clicáveis). Contraste conferido em 9 páginas |

Todos os scripts são idempotentes e `conferir-conversao.py` diz "Nenhum problema encontrado".

## 4. Decisões tomadas sem consulta (o Renan pode mudar antes de publicar)
1. **Horário 8h às 18h.** A página de contato dizia 9h; as fichas técnicas e a home diziam 8h.
   Confira qual é o do Google Meu Negócio. Se for 9h, troca em `data/marca.json` e roda
   `python scripts/rodape-local-2026-11-09.py`.
2. **Link "Avaliar no Google"** hoje abre o perfil no Maps. O ideal é o link curto
   "Pedir avaliações" do painel do Perfil da Empresa: colocar em `link_avaliacao` no
   `data/marca.json` e rodar o mesmo script.
3. **Página protegida** mexida em commit próprio (`4c6f4722`): dá para desfazer só ela.
4. Pedido de black hat (avaliação falsa, nome com palavra-chave, PBN) não foi feito: o risco é
   suspender o perfil no Google.

## 5. Não feito, fica como proposta
- **Páginas de cidade com ~60% de texto parecido.** Item grande: reescrever trechos por cidade.
- **Velocidade:** testes em cópia local mostraram que os scripts (GA4 etc.) e o preload da fonte
  atrasam a primeira pintura (1,5 s → 0,6 s sem o preload). Mexer nisso afeta a medição do GA4 em
  188 páginas, por isso ficou para decisão do Renan.

## 6. Para publicar (depois da aprovação)
1. `git checkout main && git merge auditoria-2026-11-09 && git push origin main`.
2. Conferir HTTP 200 das páginas alteradas.
3. IndexNow com a chave de sempre (`19341b29c6054af601879d85a34d62c5`), só URLs indexáveis.
4. Search Console (manual): reenviar `sitemap.xml` (187 URLs) e pedir indexação de
   `/google-meu-negocio-goiania/`.
5. Rodar o `drift_compare` nas 9 páginas da linha de base.

## 7. Fora do código — continua sendo a prioridade nº 1
Avaliações reais no Google (meta: 10), diretórios locais e LinkedIn de empresa.
