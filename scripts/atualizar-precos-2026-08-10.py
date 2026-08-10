# -*- coding: utf-8 -*-
"""
Rodada de 10/08/2026: reposicionamento de preco.

  Presenca Lite  R$ 1.997  (NOVO, pagamento unico)
  Presenca       R$   997 -> R$ 2.497  (pagamento unico)
  Crescimento    R$ 1.497 -> R$ 2.997  (por mes)
  Dominacao      R$ 2.497 -> R$ 4.997  (por mes)

A tabela em si vem do rcb_pacotes.py e e reescrita pelo aplicar-conversao.py e
pelo gerar-paginas-cidades.py. Este script cuida do que ESTA FORA do bloco
marcado: title, meta description, og/twitter, FAQ escrita a mao, priceRange e
llms.txt -- textos que citam o valor no meio da frase e que nenhum gerador
alcanca.

Ordem certa de execucao:
    python scripts/aplicar-conversao.py
    python scripts/gerar-paginas-cidades.py
    python scripts/atualizar-precos-2026-08-10.py
    python scripts/conferir-conversao.py

Idempotente: as frases antigas somem depois da primeira passada, entao rodar de
novo nao muda nada.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

MARCA_INI = "<!-- RCB:PACOTES:INICIO -->"
MARCA_FIM = "<!-- RCB:PACOTES:FIM -->"

# Da frase mais longa para a mais curta: a primeira que casar vence, senao uma
# troca curta ("R$ 997") mutilaria a frase longa antes dela ser reconhecida.
TROCAS = [
    # --- ficha do Google -----------------------------------------------
    ('"priceRange": "R$ 997 - R$ 2.497"',
     '"priceRange": "R$ 1.997 - R$ 4.997"'),

    # --- FAQ "Quanto custa?" (nichos + home) ----------------------------
    ("São três pacotes com preço fechado: Presença por R$ 997 em pagamento único, "
     "Crescimento por R$ 1.497 por mês e Dominação por R$ 2.497 por mês.",
     "São quatro pacotes com preço fechado: Presença Lite por R$ 1.997 e Presença por "
     "R$ 2.497, os dois em pagamento único; Crescimento por R$ 2.997 por mês e "
     "Dominação por R$ 4.997 por mês."),

    # --- FAQ "cabe no meu bolso?" ---------------------------------------
    ("Cabe sim, e o preço está publicado nesta página: R$ 997 em pagamento único no "
     "Pacote Presença, R$ 1.497 por mês no Crescimento e R$ 2.497 por mês no Dominação.",
     "Cabe sim, e o preço está publicado nesta página: R$ 1.997 no Presença Lite, "
     "R$ 2.497 no Pacote Presença, R$ 2.997 por mês no Crescimento e R$ 4.997 por mês "
     "no Dominação."),

    # --- enumeracao curta dos tres valores -------------------------------
    ("R$ 997 em pagamento único, ou R$ 1.497 e R$ 2.497 por mês",
     "R$ 1.997 ou R$ 2.497 em pagamento único, ou R$ 2.997 e R$ 4.997 por mês"),

    # --- "o menor pacote" -> agora e o Lite ------------------------------
    ("O menor pacote é R$ 997 em pagamento único",
     "O menor pacote é R$ 1.997 em pagamento único"),

    # --- preco de entrada citado no meio do texto ------------------------
    ("a partir de R$ 997", "a partir de R$ 1.997"),
    ("A partir de R$ 997", "A partir de R$ 1.997"),  # titles e og:title
    ("começa em R$ 997", "começa em R$ 1.997"),

    # --- agora sao quatro -------------------------------------------------
    ("qual dos três faz sentido", "qual dos quatro faz sentido"),

    # --- llms.txt ---------------------------------------------------------
    ("- Pacote Presença — R$ 997, pagamento único:",
     "- Pacote Presença — R$ 2.497, pagamento único:"),
    ("- Pacote Crescimento — R$ 1.497 por mês",
     "- Pacote Crescimento — R$ 2.997 por mês"),
    ("- Pacote Dominação — R$ 2.497 por mês",
     "- Pacote Dominação — R$ 4.997 por mês"),
]

# Linha do pacote novo no llms.txt, inserida antes da linha do Presenca.
LLMS_ANCORA = "- Pacote Presença — R$ 2.497, pagamento único:"
LLMS_LITE = (
    "- Pacote Presença Lite — R$ 1.997, pagamento único: para quem já tem site. "
    "Google Meu Negócio configurado e otimizado, 10 fotos profissionais no perfil, "
    "avaliações organizadas e respostas configuradas. Perfil entregue em 7 dias úteis.\n"
)

# Sobra depois da passada = alguem escreveu o preco de um jeito nao previsto.
# Cuidado: "R$ 2.497" e "2497.00" agora sao validos (viraram o Presenca), e
# "997.00" aparece dentro de "1997.00". Por isso as bordas explicitas.
RESTO = re.compile(
    r"R\$ ?997\b"
    r"|R\$ ?1\.497"
    r"|R\$ ?2\.497 por mês"
    r"|(?<![\d.])997\.00"
    r"|(?<![\d.])1497\.00"
    r"|dos três faz sentido"
)


def fora_do_bloco(texto, func):
    """Aplica func so no que esta fora do bloco RCB:PACOTES (esse e regerado)."""
    saida = []
    resto = texto
    while True:
        i = resto.find(MARCA_INI)
        if i == -1:
            saida.append(func(resto))
            break
        j = resto.find(MARCA_FIM, i)
        if j == -1:
            saida.append(func(resto))
            break
        j += len(MARCA_FIM)
        saida.append(func(resto[:i]))
        saida.append(resto[i:j])
        resto = resto[j:]
    return "".join(saida)


def trocar(t):
    for velho, novo in TROCAS:
        t = t.replace(velho, novo)
    return t


def main():
    arquivos = sorted(RAIZ.glob("**/*.html")) + [RAIZ / "llms.txt"]
    mudados = 0
    sobras = []
    for caminho in arquivos:
        rel = caminho.relative_to(RAIZ).as_posix()
        if "diagnostico-presenca-digital/exemplo" in rel:
            continue  # demo montada por JavaScript, nao tem preco de verdade
        original = caminho.read_text(encoding="utf-8")
        novo = fora_do_bloco(original, trocar)

        if caminho.name == "llms.txt" and "Presença Lite" not in novo:
            novo = novo.replace(LLMS_ANCORA, LLMS_LITE + LLMS_ANCORA, 1)

        if novo != original:
            caminho.write_text(novo, encoding="utf-8")
            mudados += 1

        limpo = fora_do_bloco(novo, lambda t: t)
        for m in RESTO.finditer(re.sub(
                r"%s.*?%s" % (re.escape(MARCA_INI), re.escape(MARCA_FIM)), "", limpo, flags=re.S)):
            trecho = limpo[max(0, m.start() - 70):m.end() + 70].replace("\n", " ")
            sobras.append("%s: ...%s..." % (rel, re.sub(r"\s+", " ", trecho)))

    print("arquivos alterados:", mudados, "de", len(arquivos))
    if sobras:
        print("\nATENCAO - preco antigo que sobrou (conferir a mao):")
        for s in sobras:
            print("  -", s)
        return 1
    print("nenhum preco antigo sobrou fora do bloco de pacotes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
