# Fase 3: entidade e schema (29/10/2026)

O schema é a "ficha" em código que o Google e as IAs leem para saber quem é a pessoa, qual é a empresa
e o que ela faz. Nesta fase a ficha passou a ser **a mesma em todo o site**.

Script: `scripts/entidade-ia-2026-10-29.py` (idempotente: rodou 2 vezes, a 2ª deu "alteradas: 0").
Fonte única: `data/marca.json` (`fundador.knowsAbout` é novo; `fundador.sameAs` e `sameAs` já existiam).

## O que mudou

| Item | Antes | Depois |
|---|---|---|
| O que o Renan sabe (`knowsAbout`) | 3 listas diferentes: home (8 itens), 9 páginas de nicho (5), /sobre/ (4) | 1 lista de 15 itens nas 11 páginas, com GEO, AEO, "Otimização para IA generativa" e "SEO para IA" |
| Itens ligados à Wikipédia | 3 | 5 (entraram GEO e AEO, links conferidos em 200) |
| Perfis do Renan (`sameAs` da Person) | home: LinkedIn; /sobre/: LinkedIn + Instagram; 9 nichos: nenhum | LinkedIn nas 11 (o Instagram é da empresa e já está na ficha dela) |
| Catálogo de serviços da home (`OfferCatalog`) | 4 pacotes | 4 pacotes + "SEO para IA", apontando para /seo-para-ia/, sem preço |
| Perfis da empresa no publisher de 21 artigos do blog | só YouTube | Google Maps + Instagram + YouTube (igual às outras 39 fichas da empresa) |

Saiu da lista do /sobre/ o item "Comunicação em saúde", que não aparecia em nenhuma outra página.

## Conferido (local, antes de publicar)

- 329 blocos de schema no site: todos são JSON válido e nenhum tem chave repetida.
- 11 fichas do Renan com a lista e os perfis exatamente iguais ao `marca.json`.
- 60 fichas da empresa com os mesmos perfis do `marca.json` (antes 21 diferiam).
- Nenhum `price`, `priceRange` ou `Offer` com valor em página nenhuma.
- `scripts/conferir-conversao.py`: "Nenhum problema encontrado".
- `/consultor-seo-goiania/` (protegida): sem nenhuma alteração.
- As 5 páginas novas têm: WebPage, BreadcrumbList, Service (pilar e auditoria) ou Article (guias),
  a ficha da empresa e FAQPage.

## Fica para depois da publicação (manual, Renan ou Claude)

Teste oficial do Google, uma página por vez (cole o endereço e clique em "Testar URL"):
https://search.google.com/test/rich-results

1. https://rcbseo.com.br/
2. https://rcbseo.com.br/sobre/
3. https://rcbseo.com.br/seo-para-ia/
4. https://rcbseo.com.br/como-aparecer-no-chatgpt/
5. https://rcbseo.com.br/auditoria-de-seo-para-ia/

O que esperar: "Perguntas frequentes" e "Navegação estrutural" como itens válidos. **Não esperar
estrelinhas de avaliação**: o Google não mostra estrela para avaliação que a própria empresa publica
sobre si (regra de 2019). As avaliações na ficha servem para o entendimento da empresa, não para a busca.
