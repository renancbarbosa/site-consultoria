# Triagem das 199 páginas de cidade

> Levantado em 12/08/2026. **Documento interno** — fora do sitemap, sem link no site.
> Nenhuma página foi alterada, marcada com `noindex` ou removida por causa deste relatório.
> A expansão de cidades novas está **suspensa** (ver docstring de
> `scripts/gerar-paginas-cidades.py`).

## O que este relatório decide — e o que ele não decide

Ele ordena as 199 páginas por **potencial**, usando só o que dá para medir dentro do
repositório. Ele **não** mede desempenho: impressões, cliques e posição por URL só existem
no Search Console, e não há exportação desses dados aqui.

**Decisões que dependem do Search Console e ficam pendentes:**

1. **Cidade com score alto mas zero impressão em 90 dias** desce para reescrever ou corte —
   mercado bom que não ranqueia indica que a página não compete, não que a praça é ruim.
2. **Cidade com score baixo mas impressão real** sobe para manter — dado de campo vence
   estimativa.
3. **Quais das 199 já foram indexadas.** O padrão do projeto irmão (SITE-DADOS) foi ~50% de
   indexação. Página nunca indexada não precisa de `noindex`: precisa sumir ou virar conteúdo
   de verdade.
4. **Consulta de marca por cidade** ("consultoria SEO em X") — se houver volume real em alguma
   praça, ela muda de faixa.

## Como o score foi montado

| Sinal | Peso | Por quê |
|---|---|---|
| UF = GO ou DF | +4 | atendimento presencial possível; mercado onde a RCB tem case e perfil local |
| Centro-Oeste (TO, MT, MS) | +1 | proximidade regional |
| ≥ 100 mil empresas ativas | +3 | mercado grande |
| 40–100 mil | +2 | |
| 15–40 mil | +1 | |
| ≥ 1.500 aberturas em 90 dias | +2 | demanda nova entrando no mercado |
| 500–1.500 | +1 | |
| ≥ 3 bairros com dado próprio | +2 | **é o que permite a página deixar de ser template** |
| 1–2 bairros | +1 | |
| ≥ 5 ramos com dado próprio | +1 | idem |
| ramos de saúde no topo | +2 | nicho maduro da RCB (clínicas, dentistas, estética, médicos) |
| ≥ 10 links internos | +1 | já tem alguma força interna |

O peso maior está em **dados únicos disponíveis** (bairros e ramos), não em tamanho da cidade.
Capital sem dado de bairro continua sendo template; cidade média com 5 bairros mapeados pode
virar uma página de verdade.

---

## A — Potencialmente MANTER (28 cidades, score ≥ 9)

Mercado relevante **e** dados suficientes para conteúdo próprio. Candidatas naturais ao grupo
de ~20 que recebem reescrita de verdade.

| Cidade | UF | Empresas ativas | Aberturas 90d | Bairros | Ramos | Saúde | Links int. | Score |
|---|---|---:|---:|---:|---:|:--:|---:|---:|
| Brasília | DF | 462.508 | 26.282 | 5 | 10 | — | 1 | 12 |
| Aparecida de Goiânia | GO | 83.644 | 5.565 | 5 | 10 | — | 4 | 11 |
| Anápolis | GO | 62.149 | 3.486 | 5 | 10 | — | 4 | 11 |
| Niterói | RJ | 97.925 | 4.381 | 5 | 10 | sim | 20 | 10 |
| Rio Verde | GO | 36.400 | 2.075 | 5 | 10 | — | 4 | 10 |
| São Paulo | SP | 2.718.845 | 131.945 | 5 | 10 | — | 58 | 9 |
| Rio de Janeiro | RJ | 1.024.643 | 48.867 | 5 | 10 | — | 20 | 9 |
| Belo Horizonte | MG | 534.862 | 24.803 | 5 | 10 | — | 18 | 9 |
| Curitiba | PR | 466.617 | 22.797 | 5 | 10 | — | 14 | 9 |
| Porto Alegre | RS | 288.142 | 12.978 | 5 | 10 | — | 16 | 9 |
| Campinas | SP | 229.177 | 10.296 | 5 | 10 | — | 58 | 9 |
| Guarulhos | SP | 202.792 | 11.799 | 5 | 10 | — | 58 | 9 |
| Florianópolis | SC | 160.120 | 7.911 | 5 | 10 | — | 15 | 9 |
| Ribeirão Preto | SP | 153.941 | 7.246 | 5 | 10 | — | 58 | 9 |
| Campo Grande | MS | 153.361 | 8.186 | 5 | 10 | — | 2 | 9 |
| Uberlândia | MG | 145.159 | 8.185 | 5 | 10 | — | 18 | 9 |
| Sorocaba | SP | 136.920 | 6.943 | 5 | 10 | — | 58 | 9 |
| Joinville | SC | 133.585 | 7.149 | 5 | 10 | — | 15 | 9 |
| São Bernardo do Campo | SP | 130.151 | 6.625 | 5 | 10 | — | 58 | 9 |
| Cuiabá | MT | 123.760 | 7.277 | 5 | 10 | — | 5 | 9 |
| Londrina | PR | 112.550 | 5.455 | 5 | 10 | — | 14 | 9 |
| Maringá | PR | 109.051 | 4.816 | 5 | 10 | — | 14 | 9 |
| Contagem | MG | 108.075 | 5.994 | 5 | 10 | — | 18 | 9 |
| Vitória | ES | 78.872 | 3.692 | 5 | 10 | sim | 7 | 9 |
| Balneário Camboriú | SC | 47.935 | 2.277 | 5 | 10 | sim | 1 | 9 |
| Presidente Prudente | SP | 43.843 | 1.883 | 5 | 10 | sim | 1 | 9 |
| Petrolina | PE | 42.418 | 2.260 | 5 | 10 | sim | 6 | 9 |
| Luziânia | GO | 22.025 | 1.352 | 5 | 10 | — | 4 | 9 |

---

## B — Potencialmente REESCREVER (124 cidades, score 6–8)

Têm base para conteúdo próprio, mas hoje são o mesmo template. Só valem o esforço depois que o
grupo A provar que a tese funciona. Enquanto isso, ficam como estão.

| Cidade | UF | Empresas ativas | Aberturas 90d | Bairros | Ramos | Saúde | Links int. | Score |
|---|---|---:|---:|---:|---:|:--:|---:|---:|
| Fortaleza | CE | 341.356 | 19.741 | 5 | 10 | — | 3 | 8 |
| Salvador | BA | 330.436 | 16.131 | 5 | 10 | — | 7 | 8 |
| Recife | PE | 217.658 | 10.021 | 5 | 10 | — | 6 | 8 |
| Manaus | AM | 215.938 | 13.442 | 5 | 10 | — | 1 | 8 |
| Belém | PA | 134.001 | 6.393 | 5 | 10 | — | 5 | 8 |
| João Pessoa | PB | 128.854 | 6.770 | 5 | 10 | — | 2 | 8 |
| Santo André | SP | 125.209 | 6.188 | 5 | 10 | — | 7 | 8 |
| São José dos Campos | SP | 122.567 | 6.700 | 5 | 10 | — | 1 | 8 |
| Osasco | SP | 114.429 | 6.334 | 5 | 10 | — | 1 | 8 |
| Maceió | AL | 113.075 | 6.108 | 5 | 10 | — | 2 | 8 |
| São Luís | MA | 111.552 | 5.820 | 5 | 10 | — | 2 | 8 |
| Natal | RN | 107.941 | 4.977 | 5 | 10 | — | 3 | 8 |
| São José do Rio Preto | SP | 105.924 | 4.754 | 5 | 10 | — | 1 | 8 |
| Teresina | PI | 103.219 | 5.066 | 5 | 10 | — | 1 | 8 |
| Duque de Caxias | RJ | 97.277 | 5.959 | 5 | 10 | — | 20 | 8 |
| São Gonçalo | RJ | 93.336 | 5.112 | 5 | 10 | — | 20 | 8 |
| Caxias do Sul | RS | 91.215 | 4.114 | 5 | 10 | — | 16 | 8 |
| Nova Iguaçu | RJ | 89.822 | 5.815 | 5 | 10 | — | 20 | 8 |
| Juiz de Fora | MG | 88.710 | 4.048 | 5 | 10 | — | 18 | 8 |
| Blumenau | SC | 84.382 | 4.146 | 5 | 10 | — | 15 | 8 |
| Itajaí | SC | 73.529 | 4.187 | 5 | 10 | — | 15 | 8 |
| Cascavel | PR | 70.136 | 3.714 | 5 | 10 | — | 14 | 8 |
| Ponta Grossa | PR | 62.690 | 2.873 | 5 | 10 | — | 14 | 8 |
| São José dos Pinhais | PR | 62.065 | 3.414 | 5 | 10 | — | 14 | 8 |
| Betim | MG | 60.867 | 3.697 | 5 | 10 | — | 18 | 8 |
| São José | SC | 60.628 | 3.430 | 5 | 10 | — | 15 | 8 |
| Canoas | RS | 58.221 | 3.011 | 5 | 10 | — | 16 | 8 |
| Montes Claros | MG | 57.653 | 2.920 | 5 | 10 | — | 18 | 8 |
| Chapecó | SC | 55.451 | 2.717 | 5 | 10 | — | 15 | 8 |
| Campos dos Goytacazes | RJ | 50.858 | 2.480 | 5 | 10 | — | 20 | 8 |
| Pelotas | RS | 47.906 | 2.311 | 5 | 10 | — | 16 | 8 |
| Novo Hamburgo | RS | 46.820 | 2.042 | 5 | 10 | — | 16 | 8 |
| Santa Maria | RS | 41.397 | 1.868 | 5 | 10 | — | 16 | 8 |
| Vila Velha | ES | 90.865 | 4.844 | 5 | 10 | — | 7 | 7 |
| Jundiaí | SP | 89.960 | 4.703 | 5 | 10 | — | 1 | 7 |
| Santos | SP | 87.756 | 3.759 | 5 | 10 | — | 1 | 7 |
| Serra | ES | 85.636 | 5.205 | 5 | 10 | — | 7 | 7 |
| Aracaju | SE | 82.099 | 4.181 | 5 | 10 | — | 1 | 7 |
| Barueri | SP | 81.522 | 4.609 | 5 | 10 | — | 1 | 7 |
| Feira de Santana | BA | 77.715 | 3.567 | 5 | 10 | — | 7 | 7 |
| Piracicaba | SP | 73.733 | 3.443 | 5 | 10 | — | 1 | 7 |
| Mogi das Cruzes | SP | 72.890 | 3.960 | 5 | 10 | — | 1 | 7 |
| Bauru | SP | 71.881 | 3.477 | 5 | 10 | — | 1 | 7 |
| Franca | SP | 71.131 | 4.078 | 5 | 10 | — | 1 | 7 |
| Praia Grande | SP | 62.514 | 3.933 | 5 | 10 | — | 1 | 7 |
| Jaboatão dos Guararapes | PE | 60.994 | 3.552 | 5 | 10 | — | 6 | 7 |
| Limeira | SP | 55.573 | 2.522 | 5 | 10 | — | 1 | 7 |
| Foz do Iguaçu | PR | 55.542 | 2.944 | 5 | 10 | — | 7 | 7 |
| Diadema | SP | 51.699 | 3.100 | 5 | 10 | — | 1 | 7 |
| Cariacica | ES | 51.479 | 2.747 | 5 | 10 | — | 7 | 7 |
| Porto Velho | RO | 51.428 | 3.372 | 5 | 10 | — | 1 | 7 |
| Campina Grande | PB | 50.567 | 2.357 | 5 | 10 | — | 2 | 7 |
| Indaiatuba | SP | 50.287 | 2.568 | 5 | 10 | — | 1 | 7 |
| Palhoça | SC | 50.043 | 3.063 | 5 | 10 | — | 7 | 7 |
| São Vicente | SP | 49.969 | 3.327 | 5 | 10 | — | 1 | 7 |
| Caruaru | PE | 49.756 | 2.572 | 5 | 10 | — | 6 | 7 |
| Uberaba | MG | 49.600 | 2.681 | 5 | 10 | — | 7 | 7 |
| Carapicuíba | SP | 48.806 | 3.212 | 5 | 10 | — | 1 | 7 |
| Vitória da Conquista | BA | 48.457 | 2.135 | 5 | 10 | — | 7 | 7 |
| Cotia | SP | 48.351 | 2.649 | 5 | 10 | — | 1 | 7 |
| Taubaté | SP | 48.153 | 2.629 | 5 | 10 | — | 1 | 7 |
| Mauá | SP | 47.309 | 2.907 | 5 | 10 | — | 1 | 7 |
| São Carlos | SP | 46.854 | 2.094 | 5 | 10 | — | 1 | 7 |
| Petrópolis | RJ | 46.629 | 1.702 | 5 | 10 | — | 7 | 7 |
| Guarujá | SP | 46.179 | 2.762 | 5 | 10 | — | 1 | 7 |
| Divinópolis | MG | 45.968 | 2.061 | 5 | 10 | — | 1 | 7 |
| Ananindeua | PA | 45.948 | 2.576 | 5 | 10 | — | 5 | 7 |
| Americana | SP | 45.829 | 2.011 | 5 | 10 | — | 1 | 7 |
| Marília | SP | 45.352 | 1.983 | 5 | 10 | — | 1 | 7 |
| Suzano | SP | 44.634 | 2.704 | 5 | 10 | — | 1 | 7 |
| São João de Meriti | RJ | 42.777 | 2.521 | 5 | 10 | — | 1 | 7 |
| Criciúma | SC | 42.192 | 2.275 | 5 | 10 | — | 1 | 7 |
| Sumaré | SP | 42.149 | 2.541 | 5 | 10 | — | 1 | 7 |
| Governador Valadares | MG | 41.171 | 1.919 | 5 | 10 | — | 1 | 7 |
| Araraquara | SP | 40.855 | 1.975 | 5 | 10 | — | 1 | 7 |
| Boa Vista | RR | 40.706 | 2.274 | 5 | 10 | — | 1 | 7 |
| Itaquaquecetuba | SP | 40.572 | 2.808 | 5 | 10 | — | 1 | 7 |
| Passo Fundo | RS | 40.560 | 1.904 | 5 | 10 | — | 7 | 7 |
| Belford Roxo | RJ | 40.556 | 2.683 | 5 | 10 | — | 1 | 7 |
| Lauro de Freitas | BA | 40.207 | 2.034 | 5 | 10 | — | 7 | 7 |
| Gravataí | RS | 40.032 | 2.246 | 5 | 10 | — | 1 | 7 |
| Várzea Grande | MT | 38.934 | 2.765 | 5 | 10 | — | 5 | 7 |
| Rondonópolis | MT | 38.657 | 2.224 | 5 | 10 | — | 5 | 7 |
| Sinop | MT | 38.035 | 2.437 | 5 | 10 | — | 5 | 7 |
| Dourados | MS | 37.349 | 1.768 | 5 | 10 | — | 2 | 7 |
| Imperatriz | MA | 33.505 | 1.489 | 5 | 10 | sim | 2 | 7 |
| Poços de Caldas | MG | 29.431 | 1.363 | 5 | 10 | sim | 1 | 7 |
| Mossoró | RN | 28.924 | 1.283 | 5 | 10 | sim | 3 | 7 |
| Tubarão | SC | 23.094 | 1.008 | 5 | 10 | sim | 1 | 7 |
| Erechim | RS | 21.666 | 868 | 5 | 10 | sim | 1 | 7 |
| Jaraguá do Sul | SC | 39.973 | 2.041 | 5 | 10 | — | 1 | 6 |
| Araçatuba | SP | 39.762 | 1.613 | 5 | 10 | — | 1 | 6 |
| Taboão da Serra | SP | 39.560 | 2.197 | 5 | 10 | — | 1 | 6 |
| São Caetano do Sul | SP | 39.504 | 1.554 | 5 | 10 | — | 1 | 6 |
| Colombo | PR | 37.949 | 2.210 | 5 | 10 | — | 1 | 6 |
| Olinda | PE | 37.859 | 1.967 | 5 | 10 | — | 6 | 6 |
| Hortolândia | SP | 37.194 | 2.181 | 5 | 10 | — | 1 | 6 |
| Ipatinga | MG | 37.015 | 1.822 | 5 | 10 | — | 1 | 6 |
| Ribeirão das Neves | MG | 36.773 | 2.502 | 5 | 10 | — | 1 | 6 |
| Maricá | RJ | 36.074 | 1.547 | 5 | 10 | — | 1 | 6 |
| Cabo Frio | RJ | 35.646 | 1.756 | 5 | 10 | — | 1 | 6 |
| Macapá | AP | 35.290 | 2.078 | 5 | 10 | — | 1 | 6 |
| Atibaia | SP | 35.177 | 1.566 | 5 | 10 | — | 1 | 6 |
| Jacareí | SP | 34.764 | 2.019 | 5 | 10 | — | 1 | 6 |
| Sete Lagoas | MG | 34.472 | 1.811 | 5 | 10 | — | 1 | 6 |
| Volta Redonda | RJ | 33.873 | 1.559 | 5 | 10 | — | 1 | 6 |
| Camaçari | BA | 33.700 | 1.867 | 5 | 10 | — | 7 | 6 |
| Bragança Paulista | SP | 33.583 | 1.500 | 5 | 10 | — | 1 | 6 |
| São Leopoldo | RS | 33.471 | 1.751 | 5 | 10 | — | 1 | 6 |
| Rio Branco | AC | 32.567 | 1.686 | 5 | 10 | — | 1 | 6 |
| Embu das Artes | SP | 32.121 | 2.108 | 5 | 10 | — | 1 | 6 |
| Macaé | RJ | 31.792 | 1.646 | 5 | 10 | — | 1 | 6 |
| Paulista | PE | 31.498 | 1.946 | 5 | 10 | — | 6 | 6 |
| Parnamirim | RN | 30.888 | 1.562 | 5 | 10 | — | 3 | 6 |
| Guarapuava | PR | 28.199 | 1.519 | 5 | 10 | — | 1 | 6 |
| Viamão | RS | 27.781 | 1.599 | 5 | 10 | — | 1 | 6 |
| Pinhais | PR | 27.462 | 1.522 | 5 | 10 | — | 1 | 6 |
| Santa Luzia | MG | 27.452 | 1.683 | 5 | 10 | — | 1 | 6 |
| Caucaia | CE | 27.139 | 1.908 | 5 | 10 | — | 3 | 6 |
| Itapevi | SP | 26.483 | 1.824 | 5 | 10 | — | 1 | 6 |
| Alvorada | RS | 24.749 | 1.511 | 5 | 10 | — | 1 | 6 |
| Araguaína | TO | 23.962 | 1.218 | 5 | 10 | — | 2 | 6 |
| Fazenda Rio Grande | PR | 23.831 | 1.572 | 5 | 10 | — | 1 | 6 |
| Sorriso | MT | 22.835 | 1.366 | 5 | 10 | — | 5 | 6 |

---

## C — Fortes candidatas a NOINDEX ou remoção (47 cidades, score < 6)

Mercado pequeno, poucos dados próprios, longe de Goiás e sem links internos relevantes. São as
que mais contribuem para o padrão de página-porta e menos têm chance de ranquear.

| Cidade | UF | Empresas ativas | Aberturas 90d | Bairros | Ramos | Saúde | Links int. | Score |
|---|---|---:|---:|---:|---:|:--:|---:|---:|
| Nova Friburgo | RJ | 32.987 | 1.366 | 5 | 10 | — | 1 | 5 |
| Rio Claro | SP | 31.433 | 1.397 | 5 | 10 | — | 1 | 5 |
| Santana de Parnaíba | SP | 30.897 | 1.499 | 5 | 10 | — | 1 | 5 |
| Santarém | PA | 30.522 | 1.339 | 5 | 10 | — | 5 | 5 |
| Brusque | SC | 30.069 | 1.485 | 5 | 10 | — | 1 | 5 |
| Cachoeiro de Itapemirim | ES | 29.892 | 1.282 | 5 | 10 | — | 7 | 5 |
| Patos de Minas | MG | 28.982 | 1.341 | 5 | 10 | — | 1 | 5 |
| Itu | SP | 27.895 | 1.284 | 5 | 10 | — | 1 | 5 |
| Toledo | PR | 27.550 | 1.287 | 5 | 10 | — | 1 | 5 |
| Itapema | SC | 27.275 | 1.410 | 5 | 10 | — | 1 | 5 |
| Santa Bárbara d'Oeste | SP | 26.560 | 1.343 | 5 | 10 | — | 1 | 5 |
| Juazeiro do Norte | CE | 26.521 | 1.263 | 5 | 10 | — | 3 | 5 |
| Teresópolis | RJ | 26.082 | 1.066 | 5 | 10 | — | 1 | 5 |
| Parauapebas | PA | 26.010 | 1.455 | 5 | 10 | — | 5 | 5 |
| Lages | SC | 25.914 | 1.228 | 5 | 10 | — | 1 | 5 |
| Bento Gonçalves | RS | 25.900 | 1.090 | 5 | 10 | — | 1 | 5 |
| Botucatu | SP | 25.781 | 1.259 | 5 | 10 | — | 1 | 5 |
| Valinhos | SP | 25.734 | 1.035 | 5 | 10 | — | 1 | 5 |
| Linhares | ES | 25.685 | 1.333 | 5 | 10 | — | 7 | 5 |
| Marabá | PA | 25.644 | 1.346 | 5 | 10 | — | 5 | 5 |
| Pouso Alegre | MG | 25.635 | 1.272 | 5 | 10 | — | 1 | 5 |
| Porto Seguro | BA | 24.710 | 1.221 | 5 | 10 | — | 7 | 5 |
| Magé | RJ | 24.670 | 1.477 | 5 | 10 | — | 1 | 5 |
| Rio Grande | RS | 24.313 | 1.093 | 5 | 10 | — | 1 | 5 |
| Araucária | PR | 24.200 | 1.449 | 5 | 10 | — | 1 | 5 |
| Cachoeirinha | RS | 24.147 | 1.203 | 5 | 10 | — | 1 | 5 |
| Itapetininga | SP | 23.867 | 1.171 | 5 | 10 | — | 1 | 5 |
| Guarapari | ES | 23.710 | 1.253 | 5 | 10 | — | 7 | 5 |
| Varginha | MG | 23.630 | 1.240 | 5 | 10 | — | 1 | 5 |
| Camboriú | SC | 23.483 | 1.416 | 5 | 10 | — | 1 | 5 |
| Santa Cruz do Sul | RS | 23.406 | 930 | 5 | 10 | — | 1 | 5 |
| Mogi Guaçu | SP | 23.279 | 1.174 | 5 | 10 | — | 1 | 5 |
| Itabuna | BA | 23.191 | 932 | 5 | 10 | — | 7 | 5 |
| Barretos | SP | 22.967 | 907 | 5 | 10 | — | 1 | 5 |
| Nova Lima | MG | 22.517 | 1.063 | 5 | 10 | — | 1 | 5 |
| Birigui | SP | 22.468 | 944 | 5 | 10 | — | 1 | 5 |
| Rio das Ostras | RJ | 22.403 | 1.242 | 5 | 10 | — | 1 | 5 |
| Itaboraí | RJ | 22.208 | 1.274 | 5 | 10 | — | 1 | 5 |
| Sertãozinho | SP | 22.166 | 1.018 | 5 | 10 | — | 1 | 5 |
| Araras | SP | 22.030 | 980 | 5 | 10 | — | 1 | 5 |
| Caraguatatuba | SP | 21.776 | 1.257 | 5 | 10 | — | 1 | 5 |
| Barra Mansa | RJ | 21.612 | 983 | 5 | 10 | — | 1 | 5 |
| Arapongas | PR | 21.524 | 1.030 | 5 | 10 | — | 1 | 5 |
| Pindamonhangaba | SP | 21.494 | 1.258 | 5 | 10 | — | 1 | 5 |
| Angra dos Reis | RJ | 21.404 | 1.051 | 5 | 10 | — | 1 | 5 |
| Arapiraca | AL | 21.393 | 1.060 | 5 | 10 | — | 2 | 5 |
| Palmas | PR | 5.393 | 231 | 5 | 10 | — | 0 | 3 |

---

## Recomendação de sequência

1. **Não mexer em nada agora.** Antes de `noindex`, exportar do Search Console a lista de URLs
   de `/consultoria-seo/` com impressões nos últimos 90 dias.
2. Cruzar com as três faixas acima. Cidade do grupo C **com** impressão sobe; cidade do grupo A
   **sem** impressão nenhuma desce.
3. Escolher ~20 do grupo A resultante e reescrever de verdade — bairros, ramos e concorrência
   local, não apenas o nome trocado.
4. `noindex` no grupo C. Os arquivos ficam; é uma meta tag, reversível numa linha.
5. Reavaliar em 90 dias.

## Ressalvas

- `/consultoria-seo/palmas/` **não é produzida pelo gerador** (198 geradas, 199 no disco) e é
  órfã: nenhuma página do site aponta para ela, mas está no sitemap. Recebe manutenção manual —
  foi alinhada à arquitetura nova em 12/08/2026 à mão.
- Cidades sem correspondência no SITE-DADOS aparecem com score −99.
- O SITE-DADOS tem **381 cidades**; 199 estão publicadas. As 182 restantes seguem bloqueadas
  pela trava `RCB_EXPANDIR_CIDADES`.
