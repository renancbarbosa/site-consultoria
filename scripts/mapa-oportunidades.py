# -*- coding: utf-8 -*-
"""Gera o mapa de oportunidades e a lista de paginas protegidas da auditoria.

Cruza tres fontes:
  1. Search Console (data/audit/raw_90d_*.json) - o que o dominio JA recebe.
  2. Keyword Planner (buckets passados pelo Renan) - demanda e pressao comercial.
  3. SERP conferida ao vivo em 18/08/2026 e o inventario de URLs do repositorio.

Saida:
  data/audit/opportunity_pages.csv
  data/audit/protected_pages.csv
"""
import csv
import io
import json
import os

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "audit")


def carregar(nome):
    with io.open(os.path.join(D, nome), encoding="utf-8") as f:
        return json.load(f).get("rows", []) or []


def curta(u):
    return u.replace("https://rcbseo.com.br", "") or "/"


GSC_PAGINA = {curta(r["keys"][0]): r for r in carregar("raw_90d_page.json")}

# query, intencao, bucket/mes (Planner; "-" = nao medido), CPC ref, URL atual, status, acao
LINHAS = [
    (u"consultor seo goiânia", u"comercial local", u"50", u"R$ 22,34", u"/consultor-seo-goiania/",
     u"PROTEGER",
     u"4a posicao organica conferida na SERP. Nao alterar nada. E a prova de que a RCB "
     u"ganha SERP local de baixa concorrencia."),
    (u"criação de site goiânia", u"comercial local", u"500", u"R$ 17,61", u"/criacao-de-sites-goiania/",
     u"CRIAR (feito nesta rodada)",
     u"Maior demanda local medida e zero impressao ate hoje. Pagina criada em 18/08/2026."),
    (u"criação de sites goiânia", u"comercial local", u"500", u"R$ 17,61", u"/criacao-de-sites-goiania/",
     u"CRIAR (feito nesta rodada)",
     u"Mesma pagina atende as duas variantes. Nao criar URL separada."),
    (u"seo goiânia", u"comercial local", u"50", u"R$ 22,34", u"/seo-local-goiania/",
     u"ATACAR",
     u"RCB fora do top 9 na SERP; GSC marca posicao 60 a 109 para 'seo em goiania'. "
     u"A pagina existe e tem so 20 links internos editoriais. Reforcar antes de criar nada."),
    (u"seo para clínicas de estética", u"comercial nacional", u"-", u"-", u"/seo-para-clinicas-de-estetica/",
     u"REFORMULAR",
     u"417 impressoes em 90 dias, posicao 43,8, ZERO clique. Maior gerador de impressao "
     u"inutil do site. Sem backlink nao se ganha SERP nacional de nicho."),
    (u"seo para clínicas / consultório", u"comercial nacional", u"-", u"-", u"/seo-para-clinicas/",
     u"REFORMULAR",
     u"321 impressoes, posicao 69,5, zero clique. Mesmo diagnostico da de estetica."),
    (u"negócio local perto de mim brasil", u"local generica", u"-", u"-", u"/para-comercios-locais/",
     u"QUASE LA",
     u"101 impressoes na posicao 8,8 e nenhum clique. Melhor posicao real do site fora a "
     u"marca. Titulo e description nao respondem a essa busca - e problema de CTR, nao de rank."),
    (u"seo para dentista", u"comercial nacional", u"-", u"-", u"/seo-para-dentistas/",
     u"ATACAR",
     u"109 impressoes na posicao 25. A melhor colocada das paginas de nicho. Vale reforco "
     u"antes das outras de saude."),
    (u"como saber se meu site está indexado", u"dor / leiga", u"-", u"-",
     u"/blog/como-saber-se-meu-site-esta-indexado/",
     u"QUASE LA",
     u"157 impressoes na posicao 9,4 e 2 cliques - a pagina que mais clique gera fora a home. "
     u"Falta caminho comercial: ela nao leva a lugar nenhum que venda."),
    (u"por que minha empresa não aparece no google", u"dor / leiga", u"-", u"-",
     u"/blog/por-que-minha-empresa-nao-aparece-no-google/",
     u"QUASE LA",
     u"133 impressoes na posicao 10,3, zero clique. Um degrau da primeira pagina."),
    (u"como responder avaliações do google", u"dor / leiga", u"-", u"-",
     u"/blog/como-responder-avaliacoes-google-clinica/",
     u"QUASE LA",
     u"116 impressoes na posicao 7,2 e zero clique. Ja esta na primeira pagina e nao "
     u"converte atencao em visita - title e description nao batem com a pergunta."),
    (u"google meu negócio não aparece", u"dor / leiga", u"-", u"-", u"/blog/google-meu-negocio-nao-aparece/",
     u"QUASE LA",
     u"95 impressoes na posicao 11,6. Mesmo caso: perto do topo, sem clique."),
    (u"aparecer no google", u"dor / leiga", u"-", u"-", u"/como-aparecer-no-google/",
     u"ATACAR",
     u"101 impressoes na posicao 52,8. Consulta enorme e generica; a pagina existe mas nao "
     u"tem forca. Alvo natural do trabalho off-page."),
    (u"como aparecer no google maps", u"dor / leiga", u"-", u"-", u"/blog/como-aparecer-no-google-maps/",
     u"ATACAR",
     u"161 impressoes, posicao 62,6. Tema de maior volume do grupo de dor."),
    (u"otimização google meu negócio", u"comercial nacional", u"-", u"-", u"/google-perfil-empresa/",
     u"ATACAR",
     u"171 impressoes na posicao 77,6 apesar de 244 links internos. Prova de que link "
     u"interno sozinho nao vence SERP nacional."),
    (u"seo para pequenas empresas", u"comercial nacional", u"-", u"-", u"/seo-para-pequenas-empresas/",
     u"CANIBALIZACAO",
     u"A pagina comercial (posicao 34,4) e o artigo /blog/vale-a-pena-seo-para-pequena-empresa/ "
     u"(posicao 69) disputam o termo exato. Definir dono: a comercial."),
    (u"seo para consultorios", u"comercial nacional", u"-", u"-", u"/seo-para-medicos/",
     u"CANIBALIZACAO",
     u"/seo-para-medicos/ em 18,1 e /seo-para-clinicas/ em 72,2 na mesma consulta. "
     u"Dono deve ser /seo-para-medicos/, que ja esta muito melhor colocada."),
    (u"seo para contabilidade", u"comercial nacional", u"-", u"-", u"/seo-para-contadores/",
     u"CANIBALIZACAO",
     u"Tres URLs na mesma consulta e a comercial e a PIOR colocada (67,5) - os dois artigos "
     u"estao em 40 e 42,7. Sinal invertido."),
    (u"consultoria seo local", u"comercial nacional", u"-", u"-", u"/consultoria-seo-local/",
     u"CANIBALIZACAO",
     u"/guia-seo-local/ aparece em 20,5 e a pagina comercial em 42 - o guia informacional "
     u"esta ganhando da pagina de venda, apesar dos 249 links internos dela."),
    (u"site profissional / site para empresa goiânia", u"comercial local", u"-", u"-",
     u"/criacao-de-sites-goiania/",
     u"OBSERVAR",
     u"Coberto pela pagina nova. Nao criar URL separada antes de ver o Search Console em 60 dias."),
    (u"divulgar empresa no google", u"dor / leiga", u"-", u"-",
     u"/blog/como-divulgar-minha-empresa-no-google/",
     u"SEM SINAL",
     u"1 impressao na posicao 11 em 90 dias. Tema citado no briefing, mas a demanda nao "
     u"aparece nos dados do dominio. Nao investir agora."),
    (u"desentupimento, dedetização, chaveiro, topografia etc.", u"nicho novo", u"-", u"-",
     u"(nao existe)",
     u"IGNORAR POR ORA",
     u"Nenhuma impressao, nenhuma SERP conferida, nenhum case. Servem como exemplo dentro "
     u"da pagina de criacao de site e como lista de prospeccao - nao como landing page."),
]

PROTEGIDAS = [
    (u"/consultor-seo-goiania/",
     u"4a posicao organica para 'consultor seo goiania' (SERP conferida em 18/08/2026, "
     u"google.com.br, gl=br, sem personalizacao)",
     u"47 impressoes / 2 cliques / posicao media 16,5 em 90 dias",
     u"NAO alterar URL, title, H1, headings, canonical, schema, conteudo, template nem os "
     u"links internos recebidos. Nao entrou no menu novo nem na troca de CTA."),
    (u"/",
     u"Maior fonte de clique do dominio",
     u"224 impressoes / 6 cliques / posicao media 5,4",
     u"Alterada nesta rodada apenas em metadados, cartoes de nicho e um link novo, com "
     u"autorizacao explicita do Renan. H1 e estrutura preservados."),
    (u"/blog/como-saber-se-meu-site-esta-indexado/",
     u"2a maior fonte de clique",
     u"157 impressoes / 2 cliques / posicao media 9,4",
     u"Nao mexer em title, H1 nem URL. So acrescentar caminho comercial no fim do texto."),
]


def main():
    caminho = os.path.join(D, "opportunity_pages.csv")
    with io.open(caminho, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["query", "intencao", "bucket_planner_mes", "cpc_ref", "url_atual",
                    "gsc_impressoes_90d", "gsc_cliques_90d", "gsc_posicao_90d",
                    "status", "acao"])
        for q, intencao, bucket, cpc, url, status, acao in LINHAS:
            g = GSC_PAGINA.get(url)
            w.writerow([q, intencao, bucket, cpc, url,
                        g["impressions"] if g else "",
                        g["clicks"] if g else "",
                        round(g["position"], 1) if g else "",
                        status, acao])
    print("gerado: %s (%d linhas)" % (caminho, len(LINHAS)))

    caminho = os.path.join(D, "protected_pages.csv")
    with io.open(caminho, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["url", "por_que_e_protegida", "numeros_90d", "regra"])
        for linha in PROTEGIDAS:
            w.writerow(list(linha))
    print("gerado: %s (%d linhas)" % (caminho, len(PROTEGIDAS)))


if __name__ == "__main__":
    main()
