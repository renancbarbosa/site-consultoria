# -*- coding: utf-8 -*-
"""
Títulos e descrições com mais clique (28/09/2026).

Base: Search Console, 29/08 a 26/09/2026. Estas páginas já aparecem entre a 3ª e a
17ª posição e tiveram ZERO clique em 28 dias — o resultado aparece, mas não convence.
Troca title + meta description (e og/twitter/JSON-LD, que repetem os mesmos textos).

Regras mantidas: termo de busca no início (auditoria de 08/08), title <= 65,
description <= 160, sem preço da RCB, e só prometer o que a página tem
("7 causas" e "modelo de resposta" foram conferidos no texto).

Troca a string INTEIRA do title antigo (com o sufixo), nunca a "base" — assim não
atinge H1/H2 que tenham o mesmo começo (armadilha registrada em 08/08).
Artigos gerados por módulo: a mesma troca é aplicada na fonte.
Idempotente.
"""
import io
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MODULO = RAIZ / "scripts" / "conteudo" / "artigos_visibilidade_google.py"

TROCAS = {
    "blog/quanto-custa-otimizar-google-meu-negocio": (
        "Quanto custa otimizar o Google Meu Negócio? | RCB",
        "Quanto Custa Otimizar o Google Meu Negócio? O que é Grátis",
        "Quanto custa otimizar o Google Meu Negócio? Veja o que é gratuito, o que muda o valor, o que entra no serviço e como calcular se o investimento se paga.",
        "Quanto custa otimizar o Google Meu Negócio: o que você faz de graça, o que vale pagar e como saber se o investimento volta. Sem enrolação.",
    ),
    "blog/como-saber-se-meu-site-esta-indexado": (
        "Como Saber se Meu Site Está Indexado no Google | RCB",
        "Como Saber se Meu Site Está Indexado no Google em 1 Minuto",
        "Como saber se meu site está indexado no Google: comando site:, Search Console, sitemap, canonical e noindex. Guia prático.",
        "Como saber se seu site está indexado no Google em 1 minuto: o teste do site:, o Search Console e os erros que escondem a sua página.",
    ),
    "blog/como-responder-avaliacoes-google-clinica": (
        "Como Responder Avaliações no Google para Clínicas | RCB",
        "Como Responder Avaliações no Google da Clínica (com Modelo)",
        "Como responder avaliações no Google da sua clínica sem violar o sigilo do paciente, atrair mais pacientes e fortalecer a reputação na busca local.",
        "Como responder avaliações no Google da clínica sem ferir o sigilo do paciente: o que dizer, o que nunca dizer e modelo pronto para avaliação negativa.",
    ),
    "blog/google-meu-negocio-nao-aparece": (
        "Google Meu Negócio não aparece: o que pode ser? | RCB",
        "Google Meu Negócio Não Aparece? 7 Causas e Como Resolver",
        "Seu Google Meu Negócio não aparece ou sumiu do Maps? Veja as causas mais comuns — verificação, suspensão, categoria — e como resolver.",
        "Google Meu Negócio não aparece ou sumiu do Maps? As 7 causas mais comuns — verificação, suspensão, categoria, distância — e o que fazer primeiro.",
    ),
    "consultoria-seo-local": (
        "Consultoria de SEO Local para Empresas | Todo o Brasil | RCB",
        "Consultoria de SEO Local: Consultor Direto, Sem Agência | RCB",
        "Consultoria de SEO Local com consultor independente para empresas de todo o Brasil (online) e Goiânia (presencial). Diagnóstico, plano e implementação.",
        "Consultoria de SEO local com consultor direto, sem agência no meio: Google Meu Negócio, site e conteúdo para a sua empresa aparecer. Orçamento em 24h.",
    ),
    "para-profissionais-liberais": (
        "SEO para Profissionais Liberais: Apareça no Google | RCB",
        "SEO para Profissionais Liberais: Clientes pelo Google | RCB",
        "SEO para profissionais liberais que querem ser encontrados no Google: Google Meu Negócio, site e conteúdo. Diagnóstico gratuito.",
        "SEO para profissionais liberais: seja o nome que aparece quando o cliente pesquisa no Google e no Maps. Perfil, site e conteúdo. Orçamento grátis em 24h.",
    ),
    "seo-para-psicologos": (
        "SEO para Psicólogos: Seja Encontrado por Pacientes | RCB",
        "SEO para Psicólogos: Mais Pacientes pelo Google, Dentro do CFP",
        "SEO para psicólogos dentro da ética do CFP: Google Meu Negócio, site por especialidade e conteúdo que acolhe quem procura terapia.",
        "SEO para psicólogos dentro da ética do CFP: apareça para quem procura terapia na sua cidade, com perfil, site e conteúdo que acolhem. Orçamento grátis.",
    ),
    "seo-para-pequenas-empresas": (
        "SEO para Pequenas Empresas: Apareça no Google sem Anúncios | RCB",
        "SEO para Pequenas Empresas: Clientes do Google Sem Pagar Clique",
        "SEO para pequenas empresas: apareça no Google sem pagar por clique, mesmo competindo com empresas maiores. Consultoria direta.",
        "SEO para pequenas empresas: apareça no Google e no Maps sem pagar por clique, mesmo contra concorrentes maiores. Plano simples e orçamento grátis em 24h.",
    ),
    "seo-para-veterinarios": (
        "SEO para Veterinários e Pet Shops: Apareça no Google | RCB",
        "SEO para Veterinários e Pet Shops: Mais Tutores pelo Google",
        "SEO para veterinários e pet shops: apareça no Google nas buscas de urgência e de rotina do tutor. Maps, site e avaliações.",
        "SEO local para pet shop e clínica veterinária: apareça no Maps quando o tutor procura banho, consulta ou emergência. Orçamento grátis em 24h.",
    ),
    "blog/como-divulgar-minha-empresa-no-google": (
        "Como divulgar minha empresa no Google: guia prático | RCB",
        "Como Divulgar Minha Empresa no Google (Grátis e Pago): Guia",
        "Como divulgar sua empresa no Google com Perfil da Empresa, site, SEO e anúncios. Compare os canais e siga um plano prático de 30 dias.",
        "Como divulgar sua empresa no Google: o que fazer de graça, quando vale anunciar e um plano de 30 dias para aparecer na busca e no Maps.",
    ),
}


def main():
    alteradas = 0
    for slug, (t_velho, t_novo, d_velho, d_novo) in TROCAS.items():
        assert len(t_novo) <= 65, (slug, len(t_novo))
        assert len(d_novo) <= 160, (slug, len(d_novo))
        p = RAIZ / slug / "index.html"
        s = io.open(p, encoding="utf-8", newline="").read()
        orig = s
        if t_novo not in s:
            assert t_velho in s, ("title antigo nao achado", slug)
            s = s.replace(t_velho, t_novo)
        if d_novo not in s:
            assert d_velho in s, ("description antiga nao achada", slug)
            s = s.replace(d_velho, d_novo)
        if s != orig:
            io.open(p, "w", encoding="utf-8", newline="").write(s)
            alteradas += 1
            print("ok", slug)

    # fonte dos artigos gerados
    m = io.open(MODULO, encoding="utf-8", newline="").read()
    orig = m
    for slug, (t_velho, t_novo, d_velho, d_novo) in TROCAS.items():
        if ('"slug": "%s"' % slug.split("/")[-1]) not in m:
            continue
        for velho, novo in ((t_velho, t_novo), (d_velho, d_novo)):
            if novo in m:
                continue
            if velho in m:
                m = m.replace(velho, novo)
            else:
                print("  ! na fonte o texto esta quebrado em pedacos, ajustar a mao:", slug, velho[:50])
    if m != orig:
        io.open(MODULO, "w", encoding="utf-8", newline="").write(m)
        print("ok fonte:", MODULO.name)
    print("paginas alteradas:", alteradas)


if __name__ == "__main__":
    sys.exit(main())
