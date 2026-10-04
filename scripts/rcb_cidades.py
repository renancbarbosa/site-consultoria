# -*- coding: utf-8 -*-
"""
FONTE ÚNICA DE VERDADE da poda do cluster de cidades (decisão de 12/08/2026).

Quem depende deste arquivo:
  - scripts/gerar-paginas-cidades.py  -> decide meta robots e o que entra no sitemap
  - scripts/testar-cidades.py         -> guard-rails contra regressão
  - scripts/atualizar-sitemap.py      -> impede que as noindex voltem ao sitemap
  - docs/decisao-cidades-2026-08-12.md -> registro humano (o teste confere que bate)

NÃO duplicar estas listas em outro lugar. Se uma cidade mudar de estado, muda AQUI.

Regra: quem está em INDEXAVEIS recebe `index, follow` e entra no sitemap.

ATUALIZAÇÃO 04/10/2026: as 168 cidades que estavam fora de INDEXAVEIS (em `noindex`
desde 12/08) foram EXCLUÍDAS do site — 0 cliques de 13/08 a 01/10/2026. Hoje só
existem as 31 de INDEXAVEIS. O gerador não cria nenhuma cidade fora desta lista e
o testar-cidades.py falha se alguma reaparecer. A lista das excluídas fica no
bloco RCB:CIDADES-EXCLUIDAS de docs/decisao-cidades-2026-08-12.md.

Base da decisão: Search Console 12/05–09/08/2026 (páginas criadas em 15/07/2026,
portanto 25 dias de exposição). 199 páginas, 33 com impressão, 0 cliques.
Ver docs/decisao-cidades-2026-08-12.md.
"""

# As três que recebem conteúdo local de verdade nesta rodada.
# Critério: sinal comercial real no Search Console + mercado que justifica o esforço.
PILOTO = {
    "rio-de-janeiro",  # 28 impressões, 6 consultas comerciais distintas
    "campinas",        # 6 impressões, 3 consultas comerciais
    "palmas",          # Palmas/TO: únicas consultas de intenção local pura do cluster
}

# Continuam indexáveis e no sitemap. Receberam uma camada local diferenciada em
# 15/08/2026, baseada nos dados públicos já usados pelo gerador (sem inventar
# unidade, equipe, case ou presença física). O nome CONGELADAS foi preservado
# para não quebrar os imports e a decisão registrada em 12/08.
# São as maiores praças (grupo A da triagem) mais duas com sinal acima do ruído.
# Prazo: sem impressão até meados de outubro/2026, descem para noindex.
CONGELADAS = {
    "anapolis",
    "aparecida-de-goiania",
    "balneario-camboriu",
    "belo-horizonte",
    "brasilia",
    "brusque",              # 6 impressoes, intencao comercial (grupo C, sinal venceu o score)
    "campo-grande",
    "contagem",
    "cuiaba",
    "curitiba",
    "florianopolis",
    "guarulhos",
    "joinville",
    "londrina",
    "luziania",
    "maringa",
    "mogi-das-cruzes",      # 3 impressoes, intencao comercial
    "niteroi",
    "petrolina",
    "porto-alegre",
    "presidente-prudente",
    "ribeirao-preto",
    "rio-verde",
    "sao-bernardo-do-campo",
    "sao-paulo",
    "sorocaba",
    "uberlandia",
    "vitoria",
}

# Cidades onde o atendimento e PRESENCIAL (Renan vai ate a empresa), confirmado
# pelo Renan em 09/09/2026. Bate com o FAQ de /seo-local-goiania/.
# Goiania nao entra aqui porque nao e gerada por este script (tem pagina propria).
# ATENCAO: Anapolis NAO e presencial - so consultoria online.
PRESENCIAL = {
    "aparecida-de-goiania",
}

INDEXAVEIS = PILOTO | CONGELADAS

# Slug publicado -> (cidade, UF) que a URL realmente representa.
# Existem Palmas/TO (60.127 empresas, capital) e Palmas/PR (5.393). A URL
# /consultoria-seo/palmas/ sempre foi a do TOCANTINS — o titulo, o schema e os
# numeros publicados sao de TO. O gerador, porem, desambiguava as duas para
# `palmas-to` e `palmas-pr`, e nenhuma casava com a pasta `palmas/`: por isso a
# pagina ficava orfa da geracao e congelada. Este mapa resolve a colisao.
SLUG_CANONICO = {
    ("palmas", "TO"): "palmas",
}


def eh_indexavel(slug):
    """True se a pagina da cidade deve ser indexavel e entrar no sitemap."""
    return slug in INDEXAVEIS


def total_esperado_noindex(slugs_publicados):
    """Quantas das paginas publicadas devem receber noindex."""
    return len([s for s in slugs_publicados if s not in INDEXAVEIS])
