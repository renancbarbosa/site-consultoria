# Projeto: foco em SEO + nichos nacionais (outubro/2026)

> **Se a sessão reiniciar, leia este arquivo primeiro e continue de onde parou.**
> Regra de trabalho: uma etapa por vez. Ao fim de cada uma: PARAR, mostrar o relatório e
> esperar "aprovado, siga". Nunca publicar sem "pode publicar".

## Objetivo
Ser encontrado no Brasil inteiro pelo **dono de negócio** que procura SEO, Google Meu
Negócio, site ou "como conseguir clientes" para a empresa dele. Site 100% focado nisso.

## Regra de ouro
Nós **não** prestamos o serviço do nicho: prestamos SEO e marketing **para** quem presta.
- Busca-alvo é sempre a do DONO ("marketing para empresa de guincho"), nunca a do cliente
  final ("guincho perto de mim").
- Título, H1, descrição, 1º parágrafo e H2 falam com o dono. Buscas do cliente final só no
  meio do texto, entre aspas, como exemplo do que os clientes DELE digitam.
- Fichas de dados: serviço = SEO/marketing, `audience` = `BusinessAudience` "empresas de [nicho]".

## Regras fixas de todas as etapas
1. Marca e contato só de `data/marca.json` (RCB SEO). Autor Renan Carvalho Barbosa. Sem preço,
   sem garantia. Chamada: orçamento grátis pelo WhatsApp em até 24 horas.
2. Linguagem do dono leigo; termo técnico sempre explicado.
3. Conteúdo próprio por nicho; semelhança < 40% (método do raio-X das cidades).
4. Fato/lei só com fonte oficial. Nada inventado (estatística, caso, cliente, depoimento).
5. Página nova: resposta no topo (25–120 palavras), H2 em pergunta, FAQ, data visível +
   dateModified, fichas (Service/Article + BreadcrumbList + FAQPage), autor ligado ao Renan,
   links principal ↔ artigos, título ≤ 65, descrição ≤ 160, sem título duplicado.
6. Canibalização: se já existe página para a mesma busca, FORTALECER ou JUNTAR (301), não criar.
7. Sitemap e llms.txt atualizados; no llms.txt, links dentro da seção do nicho.
8. Conferências por etapa: JSON-LD sem erro, lychee sem link interno quebrado, limites de
   título/descrição, semelhança < 40%, regra de ouro, `/claude-seo:seo page` na página principal.
9. Sem mudança em lote além do escopo da etapa.

**Redirecionamento:** o site está no **Cloudflare Pages** (não GitHub Pages). Usar o arquivo
`_redirects` da raiz (301 de verdade, já usado no site). Não usar meta refresh.

## Status das etapas

| Etapa | Escopo | Status |
|---|---|---|
| — | Pendência anterior: troca de marca (RCB SEO) + exclusão das 168 cidades noindex | **aguardando "pode publicar"** (prontas localmente, não commitadas) |
| 0 | Diagnóstico e mapa (só leitura) | **aguardando aprovação** (04/10/2026) |
| 1 | Retirar agentes de IA, automação e recuperação de vendas | pendente |
| 2 | Energia solar (principal + 2 artigos) | pendente |
| 3 | Limpeza e terceirização (principal + 2 artigos) | pendente |
| 4 | Fortalecer estética e pequenas empresas (sem página nova) | pendente |
| 5 | Advocacia (fortalecer + resolver canibalização) | pendente |
| 6a | Higienização de estofados | pendente |
| 6b | Guincho | pendente |
| 6c | Reformas | pendente |
| 6d | Dedetização e controle de pragas | pendente |
| 7 | Hub "Nichos que atendemos" | pendente |
| 8 | Medição (28 dias depois da Etapa 2) | pendente |

## Linha de base
`reports/baseline/2026-10-04/` — Search Console 04/09 a 01/10/2026 (28 dias):
139 páginas com impressão, 2.140 impressões, **11 cliques**.

## Etapa 0 — achados principais (04/10/2026)
- Quase nenhuma busca de cliente final chega às páginas de nicho. O problema hoje é
  **posição** (buscas do dono entre a 25ª e a 60ª), não público errado.
- Agentes de IA/automação/recuperação: 4 páginas (18 impressões somadas, 0 cliques), item
  de menu e coluna de rodapé em 166 páginas, 22 links de rodapé antigo para
  `/automacao-de-processos/`, "automação de processos" no `llms.txt` (2 pontos).
  Nenhum link dos sites próprios (Nalu, Radar) para elas. Links de terceiros: não medido
  (sem ferramenta; conferir no Bing Webmaster → Links de entrada).
- Páginas da divisão revertida em 08/08 (bets, IPTV, domínios) **continuam recebendo
  impressão** mesmo respondendo 404 — inclusive 3 dos 11 cliques do período.
- Mapa de nichos e canibalizações: relatório da Etapa 0 (conversa de 04/10/2026).

## Decisões do Renan
- 04/10/2026: marca oficial "RCB SEO"; dados só em `data/marca.json`.
- 04/10/2026: 168 cidades noindex excluídas; ficam as 31 indexáveis.
- 04/10/2026: perfil do Google não será renomeado agora — não lembrar de novo.
- _(decisões da Etapa 0: preencher com as respostas)_
