# -*- coding: utf-8 -*-
"""
Acrescenta as perguntas de dinheiro (preco, pagamento, prazo, garantia) no FAQ
das paginas de nicho - no texto visivel E na ficha do Google (JSON-LD), para
os dois nunca ficarem contando historias diferentes.

Tambem corrige respostas antigas do tipo "o investimento depende", que ficaram
erradas agora que o preco esta publicado.

Idempotente: nao duplica pergunta ja existente.
"""
import html as html_mod
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Respostas antigas que contradizem o preco publicado -> texto novo.
CORRIGIR = {
    "O investimento depende do momento, da concorrência e do escopo. O diagnóstico gratuito ajuda a entender se faz sentido agora.":
        "Cabe sim, e o preço está publicado nesta página: R$ 997 em pagamento único no Pacote Presença, "
        "R$ 1.497 por mês no Crescimento e R$ 2.497 por mês no Dominação. Você não precisa pedir "
        "orçamento para saber quanto é.",
}


def perguntas(negocio, pronome):
    """negocio: 'sua clínica' / 'seu comércio'. pronome: 'ela' / 'ele'."""
    return [
        (
            "Quanto custa?",
            "São três pacotes com preço fechado: Presença por R$ 997 em pagamento único, "
            "Crescimento por R$ 1.497 por mês e Dominação por R$ 2.497 por mês. Os dois mensais "
            "têm mínimo de 3 meses. O preço está nesta página — você não precisa pedir orçamento "
            "para saber quanto é.",
        ),
        (
            "Como eu pago?",
            "Por Pix, direto pelo WhatsApp. Não tem cartão, não tem boleto e não tem fidelidade de "
            "um ano. Nos pacotes mensais o compromisso é de 3 meses, que é o tempo mínimo para o "
            "Google reagir ao trabalho e você conseguir julgar o resultado.",
        ),
        (
            "Em quanto tempo o site fica pronto?",
            "Sete dias úteis, contados a partir do dia em que você me manda as informações e as "
            "fotos. Se você não tiver fotos boas, eu aviso antes e a gente resolve isso primeiro — "
            "foto ruim derruba o resultado.",
        ),
        (
            "Como funciona a garantia de 30 dias?",
            "Se em 30 dias você não notar diferença na presença %s no Google, eu refaço tudo sem "
            "custo adicional. Você me diz o que não mudou e eu volto ao trabalho." % negocio,
        ),
    ]


PAGINAS = [
    ("seo-para-dentistas", "card", "do seu consultório"),
    ("seo-para-clinicas-de-estetica", "card", "da sua clínica"),
    ("seo-para-clinicas", "card", "da sua clínica"),
    ("para-comercios-locais", "accordion", "do seu comércio"),
]

SVG_MAIS = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">\n'
    '                  <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>\n'
    '                </svg>'
)


def card(p, r):
    return ('          <div class="faq-card">\n'
            '            <h3>%s</h3>\n'
            '            <p>%s</p>\n'
            '          </div>\n' % (html_mod.escape(p), html_mod.escape(r)))


def accordion(p, r):
    return ('          <div class="faq-item">\n'
            '            <button class="faq-question" aria-expanded="false">\n'
            '              %s\n'
            '              <span class="faq-icon" aria-hidden="true">\n'
            '                %s\n'
            '              </span>\n'
            '            </button>\n'
            '            <div class="faq-answer">\n'
            '              <div class="faq-answer-inner">\n'
            '                %s\n'
            '              </div>\n'
            '            </div>\n'
            '          </div>\n\n' % (html_mod.escape(p), SVG_MAIS, html_mod.escape(r)))


def aplicar(slug, formato, negocio):
    caminho = RAIZ / slug / "index.html"
    texto = caminho.read_text(encoding="utf-8")
    original = texto
    novas = perguntas(negocio, "ela")
    relato = []

    # --- corrige respostas antigas que contradizem o preco ----------------
    for velho, novo in CORRIGIR.items():
        if velho in texto:
            texto = texto.replace(velho, novo)
            relato.append("resposta antiga de preco corrigida")

    # --- texto visivel ----------------------------------------------------
    marcador = '<div class="faq-grid">' if formato == "card" else '<div class="faq-list">'
    i = texto.find(marcador)
    if i == -1:
        relato.append("! nao achei a lista de FAQ visivel")
    else:
        corte = i + len(marcador)
        bloco = ""
        for p, r in novas:
            if p in texto:
                continue  # ja existe, nao duplica
            bloco += (card if formato == "card" else accordion)(p, r)
        if bloco:
            sep = "\n" if formato == "card" else "\n\n"
            texto = texto[:corte] + sep + bloco + texto[corte:]
            relato.append("%d perguntas no texto" % bloco.count("faq-card" if formato == "card" else "faq-item"))

    # --- ficha do Google (JSON-LD) ---------------------------------------
    def injeta(m):
        try:
            dados = json.loads(m.group(1))
        except ValueError:
            return m.group(0)
        alvos = dados.get("@graph") if isinstance(dados, dict) and "@graph" in dados else [dados]
        mudou = False
        for no in alvos:
            if not isinstance(no, dict) or no.get("@type") != "FAQPage":
                continue
            existentes = {q.get("name") for q in no.get("mainEntity", [])}
            add = [
                {"@type": "Question", "name": p,
                 "acceptedAnswer": {"@type": "Answer", "text": r}}
                for p, r in novas if p not in existentes
            ]
            if add:
                no["mainEntity"] = add + no.get("mainEntity", [])
                mudou = True
        if not mudou:
            return m.group(0)
        return ('<script type="application/ld+json">'
                + json.dumps(dados, ensure_ascii=False, indent=2)
                + "</script>")

    antes = texto
    texto = re.sub(r'<script type="application/ld\+json">(.*?)</script>',
                   injeta, texto, flags=re.S)
    if texto != antes:
        relato.append("perguntas no schema")

    if texto != original:
        caminho.write_text(texto, encoding="utf-8")
    return relato


for slug, formato, negocio in PAGINAS:
    print("==", slug)
    r = aplicar(slug, formato, negocio)
    print("   " + (", ".join(r) if r else "nada a fazer (ja aplicado)"))
