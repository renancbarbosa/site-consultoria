# -*- coding: utf-8 -*-
"""
Tira TODO preco da RCB do site (decisao do Renan, 28/09/2026).

O que faz, em todas as paginas .html + llms.txt:
  1. Paginas de cidade e hub (/consultoria-seo/): troca o bloco RCB:PACOTES
     pela versao sem preco, preservando a cidade na mensagem do WhatsApp.
     (O aplicar-conversao.py nao toca nelas de proposito; e o gerador de
     cidades nao e regerado aqui porque ja apagou trabalho manual antes.)
  2. Troca rotulos e mensagens que falam de preco ("Ver preços" etc.).
  3. Troca frases inteiras com valor por copy de orcamento (tabela FRASES).
  4. No fim VARRE o site atras de preco da RCB que tenha sobrado e lista.

Idempotente: rodar duas vezes seguidas, a segunda diz "alterados: 0".
Uso:  python scripts/remover-precos-2026-09-28.py            (aplica)
      python scripts/remover-precos-2026-09-28.py --so-varrer
"""
import io
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from rcb_pacotes import MARCA_FIM, MARCA_INI, bloco_pacotes  # noqa: E402

RAIZ = AQUI.parent
PULAR = ("node_modules", ".git", "docs", "data", "scripts", ".playwright-mcp", "graphify-out")

# Rotulos/mensagens curtas (valem no site inteiro).
ROTULOS = [
    ('>Ver preços<', '>Orçamento grátis<'),
    ('aria-label="Ver preços"', 'aria-label="Pedir orçamento grátis"'),
    ("Ol%C3%A1%21%20Vi%20seu%20site%20e%20quero%20saber%20como%20fa%C3%A7o%20para%20aparecer%20no%20Google.",
     "Ol%C3%A1%21%20Vi%20seu%20site%20e%20quero%20um%20or%C3%A7amento%20para%20aparecer%20no%20Google."),
]

# Frases inteiras com preco -> copy de orcamento. Preenchida a partir da
# varredura (secao 4). Da mais longa para a mais curta.
SOB_MEDIDA = ("O valor é sob medida: depende do tamanho do negócio, da concorrência na sua região e do "
              "que já existe hoje — e costuma sair bem mais em conta do que as pessoas imaginam. "
              "O orçamento é grátis e sai em até 24 horas pelo WhatsApp.")
QUANTO_CUSTA_PACOTES = ("Depende do tamanho do seu negócio, da concorrência na sua cidade e do que você já tem "
                        "hoje — e costuma sair bem mais em conta do que as pessoas imaginam. Tem quem precise só "
                        "arrumar o Google Meu Negócio e tem quem precise de site completo com acompanhamento "
                        "mensal. Por isso o valor é sob medida: você me conta o seu caso no WhatsApp e recebe o "
                        "orçamento em até 24 horas, sem compromisso.")
FRASES = [
    # nichos (seo-para-clinicas, estetica, dentistas) — FAQ "Quanto custa?"
    ("São quatro pacotes com preço fechado: Presença Lite por R$ 1.997 e Presença por R$ 2.497, os dois em "
     "pagamento único; Crescimento por R$ 2.997 por mês e Dominação por R$ 4.997 por mês. Os dois mensais têm "
     "mínimo de 3 meses. O preço está nesta página — você não precisa pedir orçamento para saber quanto é.",
     QUANTO_CUSTA_PACOTES),
    # pagina protegida /consultor-seo-goiania/ (autorizado: "nao quero mais preco em nada no meu site")
    ("Meu preço é fechado e está nesta página: R$ 1.997 ou R$ 2.497 em pagamento único, ou R$ 2.997 e "
     "R$ 4.997 por mês. No mercado em geral, porém,",
     "Meu valor é sob medida: depende do porte do negócio, da concorrência e do que já existe hoje — e costuma "
     "sair bem mais em conta do que se imagina. No mercado em geral,"),
    ("O preço está publicado nesta página: R$ 1.997 ou R$ 2.497 em pagamento único, ou R$ 2.997 e R$ 4.997 "
     "por mês. Antes de você pagar qualquer coisa eu olho seu Google de graça e digo qual dos quatro faz "
     "sentido — inclusive se for o mais barato.",
     SOB_MEDIDA + " Antes de você investir qualquer coisa eu olho seu Google de graça e digo qual dos quatro "
     "pacotes faz sentido — inclusive se for o mais simples."),
    # para-advogados e restos do mesmo texto
    ("O preço está publicado nesta página: R$ 1.997 ou R$ 2.497 em pagamento único, ou R$ 2.997 e R$ 4.997 "
     "por mês.", SOB_MEDIDA),
    # para-comercios-locais
    ("Cabe sim, e o preço está publicado nesta página: R$ 1.997 no Presença Lite, R$ 2.497 no Pacote Presença, "
     "R$ 2.997 por mês no Crescimento e R$ 4.997 por mês no Dominação.",
     "Cabe sim. O valor é sob medida para o tamanho do seu comércio — e costuma sair bem mais em conta do que "
     "se imagina. O orçamento é grátis e sai em até 24 horas pelo WhatsApp."),
    (" Você não precisa pedir orçamento para saber quanto é.", ""),
    # para-profissionais-liberais
    ("O menor pacote é R$ 1.997 em pagamento único, sem mensalidade. Se nem esse couber agora,",
     "O valor é sob medida para o seu tamanho, e o pacote de entrada é pagamento único, sem mensalidade — "
     "costuma caber bem mais do que se imagina. Se nem assim couber agora,"),
    # seo-para-pequenas-empresas
    ("O preço está publicado nesta página e começa em R$ 1.997, em pagamento único.",
     "O valor é sob medida e o orçamento é grátis, em até 24 horas pelo WhatsApp."),
    ("<th>Investimento de R$ 1.997</th>", "<th>Investimento de R$ 2 mil (exemplo)</th>"),
    ("<th>Investimento de R$ 2.997</th>", "<th>Investimento de R$ 3 mil (exemplo)</th>"),
    # marketing-para-advogados e marketing-para-clinicas
    ("O preço está publicado nesta página: a partir de R$ 1.997.",
     "O valor é sob medida e o orçamento é grátis, em até 24 horas pelo WhatsApp."),
    # cidades piloto (campinas, palmas, rio-de-janeiro)
    ("a partir de R$ 1.997 no pacote de entrada, que arruma o Google Perfil da Empresa de quem já tem site.",
     "o orçamento é sob medida e grátis, e o pacote de entrada, que arruma o Google Perfil da Empresa de quem "
     "já tem site, costuma sair mais em conta do que se imagina."),
    ("Online, a partir de R$ 1.997.", "Online, com orçamento grátis."),
    # titulos e descricoes dos nichos
    (" | A partir de R$ 1.997", " | Orçamento Grátis"),
    ("com preço fechado, a partir de R$ 1.997.", "com orçamento sob medida e grátis."),
    (", com preço fechado a partir de R$ 1.997.", ", com orçamento sob medida e grátis."),
    (", preço fechado a partir de R$ 1.997,", ", com orçamento sob medida e grátis,"),
    # blog/quanto-custa-consultoria-seo-local
    ("A resposta honesta, no meu caso, está publicada: eu trabalho com preço de tabela — R$ 1.997 ou R$ 2.497 "
     "em pagamento único, ou R$ 2.997 e R$ 4.997 por mês. Mas o mercado",
     "A resposta honesta é: depende do tamanho do negócio, da concorrência e do que já existe hoje. No meu caso "
     "o orçamento é sob medida e grátis. E o mercado"),
    ("Pacotes com preço fechado de site e Google Meu Negócio para negócios locais. Pagamento por Pix.",
     "Site e Google Meu Negócio para negócios locais, com orçamento sob medida e grátis."),
    # blog/quanto-custa-otimizar-google-meu-negocio
    ("O Pacote Presença Lite da RCB custa R$ 1.997 e inclui configuração",
     "Na RCB, a otimização tem orçamento sob medida e grátis, e inclui configuração"),
    ("Veja o que é gratuito, preços da RCB, o que entra no serviço",
     "Veja o que é gratuito, o que muda o valor, o que entra no serviço"),
    ("O trabalho começa em R$ 1.997 no Pacote Presença Lite, em pagamento único.",
     "O valor é sob medida e o orçamento é grátis, em até 24 horas pelo WhatsApp."),
    ("<td>R$ 1.997, uma vez</td>", "<td>Sob medida, pagamento único</td>"),
    ("<td>R$ 2.497, uma vez</td>", "<td>Sob medida, pagamento único</td>"),
    ("<td>R$ 2.997/mês, mínimo de 3 meses</td>", "<td>Sob medida, mensal (mínimo de 3 meses)</td>"),
    ("<td>R$ 4.997/mês, mínimo de 3 meses</td>", "<td>Sob medida, mensal (mínimo de 3 meses)</td>"),
    ("<th>Clientes para cobrir R$ 1.997</th>", "<th>Clientes para cobrir R$ 2 mil (exemplo)</th>"),
    ("Quando R$ 1.997 se paga?", "Quando o investimento se paga?"),
    # blog/seo-para-clinicas-vale-a-pena
    ("Pacote Presença RCB = R$ 2.497 (pagamento único).",
     "projeto de entrada, com orçamento sob medida — para a conta, use R$ 3 mil como exemplo."),
    # blog/vale-a-pena-seo-para-pequena-empresa
    ("No meu caso o preço é fechado e está publicado no site: a partir de R$ 1.997 em pagamento único.",
     "No meu caso o orçamento é sob medida e grátis — e costuma sair mais em conta do que se imagina."),
    # llms.txt
    # (uma troca por linha: o llms.txt usa quebra de linha do Windows)
    ("## Preços (tabela pública, sem orçamento sob consulta)", "## Pacotes (orçamento sob medida)"),
    ("Os valores abaixo são fechados e estão publicados no site em https://rcbseo.com.br/#pacotes. "
     "Pagamento por Pix, combinado pelo WhatsApp. Não há gateway de pagamento no site.",
     "A RCB não publica preço: cada projeto tem orçamento sob medida, grátis, enviado em até 24 horas pelo "
     "WhatsApp (+55 62 99116-1040). Os pacotes descrevem o que cada formato entrega. Pagamento por Pix, "
     "combinado pelo WhatsApp."),
    ("- Pacote Presença Lite — R$ 1.997, pagamento único:", "- Pacote Presença Lite — pagamento único:"),
    ("- Pacote Presença — R$ 2.497, pagamento único:", "- Pacote Presença — pagamento único:"),
    ("- Pacote Crescimento — R$ 2.997 por mês, mínimo de 3 meses:", "- Pacote Crescimento — mensal, mínimo de 3 meses:"),
    ("- Pacote Dominação — R$ 4.997 por mês, mínimo de 3 meses:", "- Pacote Dominação — mensal, mínimo de 3 meses:"),
    ("preços publicados pela RCB e como estimar retorno", "o que muda o valor e como estimar retorno"),
]

# O que conta como "preco da RCB" na varredura.
PRECO_RCB = re.compile(
    r'R\$\s?(?:1\.997|2\.497|2\.997|4\.997|997|1\.497)(?![\d.,])'
    r'|(?<![\d.])(?:1997|2497|2997|4997)\.00'
    r'|a partir de R\$'
    r'|tabela pública|valores abaixo são fechados'
    r'|"priceRange"|"offers"\s*:'
    r'|(?<!um )[Pp]reço (?:fechado|publicado|está (?:na tela|publicado))'  # "nao mostram um preco fechado" e legitimo
    r'|[Pp]agamento por Pix pelo WhatsApp\.<'   # fecho antigo da tabela (Pix em si nao e preco)
    r'|class="valor"'
)


# Modulos de conteudo que geram paginas: recebem as mesmas FRASES, senao a
# proxima regeracao traria o preco de volta.
FONTES = [
    AQUI / "conteudo" / "artigos_visibilidade_google.py",
    AQUI / "conteudo" / "cidades_piloto.py",
]


def arquivos():
    for f in sorted(RAIZ.rglob("*.html")):
        rel = f.relative_to(RAIZ).as_posix()
        if rel.startswith(PULAR):
            continue
        yield f
    yield RAIZ / "llms.txt"
    yield from FONTES


def ler(f):
    return io.open(f, encoding="utf-8", newline="").read()


def gravar(f, s):
    io.open(f, "w", encoding="utf-8", newline="").write(s)


def bloco_cidade(h, rel):
    if MARCA_INI not in h or not rel.startswith("consultoria-seo/"):
        return h
    m = re.search(r"Tenho%20um%20neg%C3%B3cio%20em%20(.*?)%20e%20", h)
    onde = ""
    if m:
        from urllib.parse import unquote
        onde = " em " + unquote(m.group(1))
    dp = "hub-cidades" if rel == "consultoria-seo/index.html" else "cidade-" + rel.split("/")[1]
    novo = bloco_pacotes("um negócio", dp, onde)
    # As paginas de cidade misturam \n e \r\n logo depois do marcador.
    padrao = re.compile(r'[ \t]*%s.*?%s\r?\n' % (re.escape(MARCA_INI), re.escape(MARCA_FIM)), re.S)
    return padrao.sub(lambda _: novo, h, count=1)


def main():
    so_varrer = "--so-varrer" in sys.argv
    alterados = 0
    if not so_varrer:
        for f in arquivos():
            if not f.exists():
                continue
            rel = f.relative_to(RAIZ).as_posix()
            h = ler(f)
            novo = bloco_cidade(h, rel)
            for velho, bom in (FRASES if f in FONTES else ROTULOS + FRASES):
                novo = novo.replace(velho, bom)
            if novo != h:
                gravar(f, novo)
                alterados += 1
        print("alterados:", alterados)

    sobras = 0
    for f in arquivos():
        if not f.exists():
            continue
        rel = f.relative_to(RAIZ).as_posix()
        h = ler(f)
        for m in PRECO_RCB.finditer(h):
            sobras += 1
            a = max(0, m.start() - 90)
            trecho = " ".join(h[a:m.end() + 60].split())
            print("  PRECO  %s | %s" % (rel, trecho))
    print("preco da RCB que sobrou:", sobras)
    return 1 if sobras else 0


if __name__ == "__main__":
    sys.exit(main())
