"""Remove a oferta "Garantia de 30 dias" do site inteiro (decisao do Renan, 04/10/2026).

Tira a OFERTA da RCB (cartoes de pacote, selos, FAQ, faixa da home, llms.txt e as
fontes que geram essas paginas). NAO mexe nas frases educativas do tipo
"ninguem pode garantir posicao no Google" -- essas continuam.

Idempotente: a 2a execucao tem que dizer "alterados: 0" e "sobrou: 0".
    python scripts/remover-garantia-2026-10-04.py
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = re.S

# (regex, substituto) aplicados em todo index.html e no llms.txt
TROCAS_HTML = [
    # 1. ultima linha de cada cartao de pacote (232 paginas, 4 cartoes cada)
    (re.compile(r'\r?\n[ \t]*<li class="pacote-garantia">Garantia de 30 dias</li>'), ''),
    # 2. selo das paginas de servico
    (re.compile(r'<span class="pill">Garantia de 30 dias</span>'),
     '<span class="pill">Prazo por escrito</span>'),
    # 3. rotulo acima da chamada final das paginas de nicho
    (re.compile(r'<div class="section-tag">Garantia de 30 dias</div>'),
     '<div class="section-tag">Análise gratuita</div>'),
    # 4. "E se voce fechar: ... eu refaco tudo sem custo adicional."
    (re.compile(r'<strong>E se você fechar:</strong> se em 30 dias[^<]*?sem custo adicional\.\s*'), ''),
    (re.compile(r'\s*E se você fechar: se em 30 dias[^<"]*?sem custo adicional\.'), ''),
    (re.compile(r'\r?\n[ \t]*<p>\s*</p>'), ''),
    # 5. pergunta do FAQ -- cartao simples
    (re.compile(r'\s*<div class="faq-card">\s*<h3>Como funciona a garantia de 30 dias\?</h3>\s*<p>.*?</p>\s*</div>', S), ''),
    # 6. pergunta do FAQ -- acordeao (home e /para-comercios-locais/)
    (re.compile(r'\s*<div class="faq-item"[^>]*>\s*<button[^>]*>\s*(?:<span>)?\s*Como funciona a garantia de 30 dias\?'
                r'.*?</button>\s*<div class="faq-(?:panel|answer)"[^>]*>\s*<div class="faq-(?:panel-body|answer-inner)">'
                r'(?:(?!<div).)*?</div>\s*</div>\s*</div>', S), ''),
    # 7. pergunta do FAQ -- dados estruturados (FAQPage)
    (re.compile(r',\s*\{\s*"@type":\s*"Question",\s*"name":\s*"Como funciona a garantia de 30 dias\?",'
                r'\s*"acceptedAnswer":\s*\{[^{}]*\}\s*\}'), ''),
    (re.compile(r'\{\s*"@type":\s*"Question",\s*"name":\s*"Como funciona a garantia de 30 dias\?",'
                r'\s*"acceptedAnswer":\s*\{[^{}]*\}\s*\}\s*,\s*'), ''),
    # 8. home: linha da proposta, item de prova e a faixa inteira da garantia
    (re.compile(r'Orçamento grátis em até 24 horas, prazo por escrito e garantia de 30 dias\.'),
     'Orçamento grátis em até 24 horas e prazo por escrito.'),
    (re.compile(r'\s*<div class="hero-proof-item">(?:(?!</div>).)*?<strong>Garantia de 30 dias</strong>.*?</div>', S), ''),
    (re.compile(r'\s*<section class="garantia-band".*?</section>', S), ''),
    # 9. frases soltas
    (re.compile(r'Pagamento por Pix, combinado no WhatsApp, e garantia de 30 dias\.'),
     'Pagamento por Pix, combinado no WhatsApp.'),
    (re.compile(r', garantia de satisfação de 30 dias e foco'), ' e foco'),
    (re.compile(r'Qual é a garantia caso em 30 dias eu não perceba melhora na minha visibilidade\?'),
     'O orçamento e o prazo vêm por escrito antes de começar?'),
    # 10. llms.txt
    (re.compile(r'\r?\n- Garantia: se em 30 dias o cliente não notar diferença[^\n]*'), ''),
]

# fontes que geram paginas -- para a garantia nao voltar numa regeracao
TROCAS_FONTES = {
    "scripts/rcb_pacotes.py": [
        (re.compile(r'\r?\n[ \t]*# A garantia fecha os tres cartoes:[^\n]*\r?\n[ \t]*#[^\n]*'
                    r'\r?\n[ \t]*itens \+= \'\\n\s*<li class="pacote-garantia">Garantia de 30 dias</li>\''), ''),
    ],
    "scripts/conteudo/servicos_marketing.py": [(re.compile(r'"Garantia de 30 dias"'), '"Prazo por escrito"')],
    "scripts/conteudo/servicos_nichos.py": [(re.compile(r'"Garantia de 30 dias"'), '"Prazo por escrito"')],
    "scripts/conteudo/cidades_piloto.py": [
        (re.compile(r'Pagamento por Pix, combinado no WhatsApp, e garantia de 30 dias\.'),
         'Pagamento por Pix, combinado no WhatsApp.')],
    "scripts/gerar-criacao-sites-goiania.py": [
        (re.compile(r'<span class="pill">Garantia de 30 dias</span>'), '<span class="pill">Prazo por escrito</span>')],
    "scripts/faq-precos-nichos.py": [
        (re.compile(r'\s*\(\s*"Como funciona a garantia de 30 dias\?",.*?% negocio,\s*\),', S), '')],
}

# o que ainda conta como oferta de garantia se sobrar
SOBRA = re.compile(r'garantia de 30 dias|garantia de satisfa|pacote-garantia|garantia-band|'
                   r'refaço tudo sem custo|refeito sem custo|E se você fechar:', re.I)


def ler(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def gravar(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def jsonld_ok(h):
    for b in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, S):
        try:
            json.loads(b)
        except Exception:
            return False
    return True


def main():
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "**", "index.html"), recursive=True)
             if not os.path.relpath(p, RAIZ).startswith(("scripts", "docs", "node_modules", ".git"))]
    alvos.append(os.path.join(RAIZ, "llms.txt"))
    alterados, erros, sobrou = 0, [], []
    for p in alvos:
        t0 = ler(p)
        t = t0
        for rx, novo in TROCAS_HTML:
            t = rx.sub(novo, t)
        rel = os.path.relpath(p, RAIZ)
        ok = True
        if p.endswith(".html") and t != t0:
            if not t.lstrip().lower().startswith("<!doctype"):
                erros.append(rel + ": perdeu o <!DOCTYPE>"); ok = False
            if not jsonld_ok(t):
                erros.append(rel + ": JSON-LD invalido"); ok = False
        if SOBRA.search(t):
            sobrou.append(rel)
        if t != t0 and ok:
            gravar(p, t)
            alterados += 1
    for rel, trocas in TROCAS_FONTES.items():
        p = os.path.join(RAIZ, rel)
        t0 = ler(p)
        t = t0
        for rx, novo in trocas:
            t = rx.sub(novo, t)
        if t != t0:
            gravar(p, t)
            alterados += 1
        if SOBRA.search(t):
            sobrou.append(rel)
    print("arquivos conferidos:", len(alvos) + len(TROCAS_FONTES))
    print("alterados          :", alterados)
    print("sobrou             :", len(sobrou))
    for s in sobrou:
        print("   ", s)
    if erros:
        print("ERROS (esses arquivos NAO foram gravados):")
        for e in erros:
            print("   ", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
