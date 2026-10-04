"""Regra unica de fidelidade no site inteiro (decisao do Renan, 04/10/2026).

"Nao existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedencia.
As demais condicoes vao por escrito junto com o orcamento."

Antes o site se contradizia: "compromisso de 3 meses nos pacotes mensais" (home e
paginas de nicho), "fidelidade minima de 6 meses com multa" (/para-advogados/) e
"sem fidelidade, mes a mes" (consultoria, contato, sobre, acompanhamento).
Troca no HTML (texto e JSON-LD), no llms.txt e nos modulos de conteudo.
Idempotente.  python scripts/fidelidade-2026-10-04.py
"""
import glob
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGRA = ("Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. "
         "As demais condições vão por escrito junto com o orçamento.")

TROCAS = [
    # FAQ de pagamento (home e paginas de nicho), com as variacoes de final
    (re.compile(r"não tem fidelidade de um ano\. Nos pacotes mensais o compromisso é de 3 meses[^.<\"]*\."),
     "não existe fidelidade: para cancelar, basta avisar com 30 dias de antecedência."),
    # /para-advogados/
    (re.compile(r"Trabalho com fidelidade mínima de 6 meses, justamente porque SEO precisa de tempo para entregar "
                r"resultado\. Antes disso, multa proporcional\. Após 6 meses, você fica livre para sair quando quiser\."),
     REGRA),
    # /acompanhamento-seo/ (FAQ visivel e JSON-LD)
    (re.compile(r"O formato é mensal, sem amarrar você a contratos longos\. A continuidade faz sentido porque SEO é "
                r"construção, mas a decisão de seguir é revista a cada período, com base nos relatórios e na evolução real\."),
     REGRA + " A continuidade faz sentido porque SEO é construção, e a decisão de seguir é revista com base nos relatórios."),
    (re.compile(r"O formato é mensal, sem contratos longos\. A continuidade é revista a cada período, com base nos "
                r"relatórios e na evolução real\."),
     REGRA + " A continuidade é revista com base nos relatórios."),
    # /gestao-de-trafego-pago/ (FAQ)
    (re.compile(r"As condições vão por escrito junto com o orçamento, antes de você decidir\. A conta do Google Ads "
                r"fica no nome da sua empresa\."),
     REGRA + " A conta do Google Ads fica no nome da sua empresa."),
    # pacotes (ficha da home, tabela do artigo, llms.txt)
    (re.compile(r"Mínimo de 3 meses\."), "Sem fidelidade: aviso de 30 dias para cancelar."),
    (re.compile(r"Sob medida, mensal \(mínimo de 3 meses\)"), "Sob medida, mensal (sem fidelidade)"),
    (re.compile(r"mensal, mínimo de 3 meses:"), "mensal, sem fidelidade (aviso de 30 dias para cancelar):"),
    # frases que ja diziam "sem fidelidade": acrescenta o aviso de 30 dias
    (re.compile(r"Sem fidelidade — mês a mês\."), "Sem fidelidade — para cancelar, basta avisar com 30 dias de antecedência."),
    (re.compile(r"Sem prazo mínimo de contratação, sem cláusula de fidelidade\."),
     "Sem prazo mínimo de contratação e sem fidelidade: para cancelar, basta avisar com 30 dias de antecedência."),
]

MODULOS = ["scripts/conteudo/servicos_marketing.py", "scripts/conteudo/artigos_visibilidade_google.py"]
# o FAQ do modulo de trafego esta quebrado em varias linhas de string: troca direta
TRAFEGO_MOD_ANTIGO = ('"As condições vão por escrito junto com o orçamento, antes de você decidir. A conta do Google Ads fica "\n'
                      '             "no nome da sua empresa."')
TRAFEGO_MOD_NOVO = ('"Não existe fidelidade. Para cancelar, basta avisar com 30 dias de antecedência. As demais condições "\n'
                    '             "vão por escrito junto com o orçamento. A conta do Google Ads fica no nome da sua empresa."')


def ler(p):
    with io.open(p, encoding="utf-8", newline="") as f:
        return f.read()


def gravar(p, t):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def main():
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)
             if not os.path.relpath(p, RAIZ).replace("\\", "/").startswith(("scripts/", "docs/", "data/", "graphify-out/", ".playwright"))]
    alvos += [os.path.join(RAIZ, "llms.txt")] + [os.path.join(RAIZ, m) for m in MODULOS]
    alterados = 0
    for p in alvos:
        t0 = ler(p)
        t = t0.replace(TRAFEGO_MOD_ANTIGO, TRAFEGO_MOD_NOVO)
        for rx, novo in TROCAS:
            t = rx.sub(novo, t)
        if t != t0:
            gravar(p, t)
            alterados += 1
            print("  ", os.path.relpath(p, RAIZ))
    sobra = []
    for p in alvos:
        t = ler(p)
        for rx in (r"compromisso é de 3 meses", r"fidelidade mínima", r"multa proporcional", r"mínimo de 3 meses",
                   r"Mínimo de 3 meses", r"fidelidade de um ano"):
            if re.search(rx, t):
                sobra.append((os.path.relpath(p, RAIZ), rx))
    print("alterados:", alterados)
    print("sobrou regra antiga:", sobra or "nada")
    if sobra:
        sys.exit(1)


if __name__ == "__main__":
    main()
