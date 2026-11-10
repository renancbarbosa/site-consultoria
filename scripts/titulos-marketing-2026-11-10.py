# -*- coding: utf-8 -*-
"""
"Marketing para X" na frente de "SEO para X" em 3 paginas de nicho (10/11/2026).

Base: planejador de palavras-chave do Google Ads (Brasil, 12 meses):
  marketing medico ............ 1 mil a 10 mil buscas/mes
  marketing para dentistas .... 100 a 1 mil      marketing odontologico ... 100 a 1 mil
  marketing imobiliario ....... 100 a 1 mil
O dono do negocio digita "marketing para", nao "SEO para". As paginas ja aparecem para
"seo para ..." (imobiliaria na posicao 19, medicos na 61), entao o termo antigo CONTINUA no
titulo e no H1: so passa para o segundo lugar. A URL nao muda.

Decisao do Renan (10/11/2026): "esquece decisao de manter SEO ... tem que trabalhar com dado".
Substitui, para estas 3 paginas, a decisao editorial 1 da rodada de 09/08/2026.

Troca: <title>, og:title, twitter:title, meta description, og:description,
twitter:description, as copias desses textos no JSON-LD e o H1. Idempotente.
    python scripts/titulos-marketing-2026-11-10.py
"""
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# slug: ([(titulo antigo, titulo novo), ...] da string mais longa para a mais curta, descricao nova, H1 antigo, H1 novo)
TROCAS = {
    "seo-para-medicos": (
        [("SEO para Médicos: Apareça no Google e Atraia Pacientes",
          "Marketing Médico e SEO para Médicos: Apareça no Google")],
        "Marketing médico dentro das regras do CFM: SEO para médicos, Google Meu Negócio e site por "
        "especialidade para o paciente encontrar você. Orçamento grátis.",
        "SEO para médicos: apareça no Google quando o paciente procura sua especialidade",
        "Marketing médico e SEO para médicos: apareça no Google quando o paciente procura sua especialidade",
    ),
    "seo-para-dentistas": (
        [("SEO para Dentistas: Apareça no Google | Orçamento Grátis",
          "Marketing Odontológico e SEO para Dentistas | Orçamento Grátis")],
        "Marketing para dentistas com orçamento grátis: SEO, site e Google Meu Negócio para o consultório "
        "aparecer quando o paciente procura implante ou aparelho.",
        "SEO para dentistas: seu consultório aparece no Google quando o paciente procura implante?",
        "Marketing para dentistas e SEO: seu consultório aparece no Google quando o paciente procura implante?",
    ),
    "seo-para-imobiliarias": (
        [("SEO para Imobiliárias e Corretores: Apareça no Google | RCB SEO",
          "Marketing Imobiliário e SEO para Imobiliárias | RCB SEO"),
         ("SEO para Imobiliárias e Corretores: Apareça no Google",
          "Marketing Imobiliário e SEO para Imobiliárias")],
        "Marketing imobiliário e SEO para imobiliárias e corretores: gere contatos próprios no Google, sem "
        "depender só dos portais. Orçamento grátis em 24h.",
        "SEO para imobiliárias: gere leads próprios, sem depender só dos portais",
        "Marketing imobiliário e SEO para imobiliárias: gere leads próprios, sem depender só dos portais",
    ),
}
_METAS = (r'(<meta name="description" content=")[^"]*(")',
          r'(<meta property="og:description" content=")[^"]*(")',
          r'(<meta name="twitter:description" content=")[^"]*(")')


def main():
    alteradas = 0
    for slug, (titulos, d_novo, h1_velho, h1_novo) in TROCAS.items():
        assert len(d_novo) <= 160, (slug, "descricao", len(d_novo))
        p = RAIZ / slug / "index.html"
        s = io.open(p, encoding="utf-8", newline="").read()
        orig = s
        d_velho = re.search(_METAS[0], s)
        d_velho = s[d_velho.start(1) + len(d_velho.group(1)):d_velho.end() - 1]
        for velho, novo in titulos:
            if novo not in s:
                assert velho in s, ("titulo antigo nao achado", slug, velho)
            s = s.replace(velho, novo)
        for rx in _METAS:
            s = re.sub(rx, lambda m: m.group(1) + d_novo + m.group(2), s, count=1)
        if d_velho != d_novo:
            s = s.replace('"%s"' % d_velho, '"%s"' % d_novo)  # copias no JSON-LD
        if h1_novo not in s:
            assert s.count(">%s</h1>" % h1_velho) == 1, ("H1 antigo nao achado", slug)
            s = s.replace(">%s</h1>" % h1_velho, ">%s</h1>" % h1_novo)
        t = re.search(r"<title>([^<]*)</title>", s).group(1)
        assert len(t) <= 65, (slug, "title", len(t), t)
        assert s.count("<h1") == 1 and s.startswith("<!DOCTYPE"), slug
        for bloco in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            json.loads(bloco)
        if s != orig:
            io.open(p, "w", encoding="utf-8", newline="").write(s)
            alteradas += 1
        print("ok  /%s/  title=%d  desc=%d  | %s" % (slug, len(t), len(d_novo), t))
    print("paginas alteradas:", alteradas)


if __name__ == "__main__":
    sys.exit(main())
