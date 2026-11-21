"""Gera os graficos da pagina /cases/ a partir dos dados reais do Search Console.

Fonte: data/cases/<projeto>-dias.json (export diario do Search Console, dimensao date).
Para atualizar no futuro:
  seo auth refresh
  seo gsc-query --site "sc-domain:naluprado.com.br" --start-date 2025-01-01 \
      --end-date AAAA-MM-DD --dimensions date --limit 25000 --json > data/cases/naluprado-dias.json
  (idem radardecnpj.com.br -> radar-dias.json, imuneconsultoriosrioverde.com.br -> imune-dias.json)
  python scripts/gerar-graficos-cases.py

O script troca o SVG entre os marcadores <!-- RCB:GRAFICO:<id> --> e <!-- /RCB:GRAFICO:<id> -->
em cases/index.html. Idempotente. Os NUMEROS escritos no texto da pagina nao sao atualizados
por aqui: ele imprime o resumo para conferir e reescrever o texto a mao.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data" / "cases"
PAGINA = RAIZ / "cases" / "index.html"

W, H = 600, 340
ML, MR, MT, MB = 58, 30, 34, 46  # margens

OURO = "#C9A84C"
TEXTO = "#9fb0c3"
GRADE = "rgba(255,255,255,0.08)"
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def carregar(nome):
    rows = json.loads((DADOS / f"{nome}-dias.json").read_text(encoding="utf-8"))["rows"]
    i0 = next(i for i, r in enumerate(rows) if r["impressions"] > 0)
    return rows[i0:]


def semanas(rows):
    """Blocos de 7 dias a partir do 1o dia com dados; descarta a ultima semana incompleta."""
    out = []
    for i in range(0, len(rows) - 6, 7):
        b = rows[i:i + 7]
        im = sum(r["impressions"] for r in b)
        out.append({
            "inicio": b[0]["keys"][0],
            "cliques": sum(r["clicks"] for r in b),
            "impressoes": im,
            "posicao": (sum(r["position"] * r["impressions"] for r in b) / im) if im else None,
        })
    return out


def rotulo(data):
    _, m, d = data.split("-")
    return f"{int(d)} {MESES[int(m) - 1]}"


def fmt(n):
    return f"{n:,.0f}".replace(",", ".")


def virgula(v):
    return f"{v:.1f}".replace(".", ",")


def grafico(gid, serie, campo, titulo, desc, invertido=False, faixa_top10=False):
    vals = [s[campo] for s in serie]
    n = len(vals)
    pw, ph = W - ML - MR, H - MT - MB
    if invertido:  # posicao: 1 em cima
        lo, hi = 1, max(20, int(max(vals)) + 2)
    else:
        lo = 0
        alvo = max(vals) * 1.1 / 4
        mag = 10 ** len(str(int(alvo)))  / 10
        passo = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= alvo)
        hi = passo * 4

    def x(i):
        return ML + (pw * i / (n - 1))

    def y(v):
        t = (v - lo) / (hi - lo)
        return MT + (t * ph if invertido else (1 - t) * ph)

    pts = [(x(i), y(v)) for i, v in enumerate(vals)]
    linha = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    base = y(hi) if invertido else y(0)
    area = (f"M{pts[0][0]:.1f},{base:.1f} L" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            + f" L{pts[-1][0]:.1f},{base:.1f} Z")

    p = [f'<svg class="case-chart-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{gid}-t {gid}-d" '
         f'xmlns="http://www.w3.org/2000/svg">',
         f'<title id="{gid}-t">{titulo}</title><desc id="{gid}-d">{desc}</desc>',
         f'<defs><linearGradient id="{gid}-g" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{OURO}" stop-opacity="{0.05 if invertido else 0.35}"/>'
         f'<stop offset="1" stop-color="{OURO}" stop-opacity="{0.35 if invertido else 0.02}"/></linearGradient></defs>']
    if faixa_top10:
        y10 = y(10.5)
        p.append(f'<rect x="{ML}" y="{MT}" width="{pw}" height="{y10 - MT:.1f}" fill="rgba(76,201,120,0.08)"/>')
        p.append(f'<text x="{ML + pw / 2:.1f}" y="{MT + 22}" text-anchor="middle" fill="#6fd39a" font-size="17" '
                 f'font-weight="700">1ª página do Google</text>')
    for k in range(5):
        v = lo + (hi - lo) * k / 4
        gy = y(v)
        p.append(f'<line x1="{ML}" x2="{W - MR}" y1="{gy:.1f}" y2="{gy:.1f}" stroke="{GRADE}"/>')
        txt = f"{v:.0f}º" if invertido else fmt(v)
        p.append(f'<text x="{ML - 8}" y="{gy + 6:.1f}" text-anchor="end" fill="{TEXTO}" font-size="17">{txt}</text>')
    for i in sorted({0, n // 2, n - 1}):
        anc = "start" if i == 0 else ("end" if i == n - 1 else "middle")
        p.append(f'<text x="{x(i):.1f}" y="{H - 12}" text-anchor="{anc}" fill="{TEXTO}" font-size="17">'
                 f'{rotulo(serie[i]["inicio"])}</text>')
    p.append(f'<path d="{area}" fill="url(#{gid}-g)"/>')
    p.append(f'<polyline points="{linha}" fill="none" stroke="{OURO}" stroke-width="4" '
             f'stroke-linejoin="round" stroke-linecap="round"/>')
    for i, anc in ((0, "start"), (n - 1, "end")):
        px, py = pts[i]
        txt = f"{virgula(vals[i])}º" if invertido else fmt(vals[i])
        p.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="#0D1B2A" stroke="{OURO}" stroke-width="3"/>')
        ty = py + 30 if py < MT + 40 else py - 16
        p.append(f'<text x="{px:.1f}" y="{ty:.1f}" text-anchor="{anc}" fill="#fff" font-size="22" '
                 f'font-weight="800">{txt}</text>')
    p.append("</svg>")
    return "".join(p)


def injetar(html, gid, svg):
    ini, fim = f"<!-- RCB:GRAFICO:{gid} -->", f"<!-- /RCB:GRAFICO:{gid} -->"
    pad = re.compile(re.escape(ini) + r".*?" + re.escape(fim), re.S)
    if not pad.search(html):
        sys.exit(f"marcador {ini} nao encontrado em cases/index.html")
    return pad.sub(lambda m: ini + svg + fim, html)


def resumo(nome, rows):
    def agg(rr):
        c = sum(r["clicks"] for r in rr)
        im = sum(r["impressions"] for r in rr)
        return c, im, round(sum(r["position"] * r["impressions"] for r in rr) / im, 1)
    print(f"{nome}: {rows[0]['keys'][0]} a {rows[-1]['keys'][0]} | 1as 4 semanas {agg(rows[:28])} | "
          f"ultimas 4 semanas {agg(rows[-28:])} | total {agg(rows)}  (cliques, aparicoes, posicao)")


def main():
    html = PAGINA.read_text(encoding="utf-8")
    nalu, radar, imune = carregar("naluprado"), carregar("radar"), carregar("imune")
    for nome, r in (("naluprado", nalu), ("radar", radar), ("imune", imune)):
        resumo(nome, r)

    s = semanas(nalu)
    html = injetar(html, "nalu", grafico(
        "nalu", s, "impressoes", "Nalu Prado: vezes que o site apareceu no Google, por semana",
        f"De {fmt(s[0]['impressoes'])} aparições na primeira semana para {fmt(s[-1]['impressoes'])} "
        f"na semana de {rotulo(s[-1]['inicio'])}. Dados do Google Search Console."))
    s = semanas(radar)
    html = injetar(html, "radar", grafico(
        "radar", s, "cliques", "Radar de CNPJ: visitas vindas do Google, por semana",
        f"De {fmt(s[0]['cliques'])} visitas na primeira semana para {fmt(s[-1]['cliques'])} "
        f"na semana de {rotulo(s[-1]['inicio'])}. Dados do Google Search Console."))
    s = semanas(imune)
    html = injetar(html, "imune", grafico(
        "imune", s, "posicao",
        "Imune Consultórios: posição média no Google, por semana (quanto mais alto, melhor)",
        f"Da posição {virgula(s[0]['posicao'])} na primeira semana para {virgula(s[-1]['posicao'])} "
        f"na semana de {rotulo(s[-1]['inicio'])}. Dados do Google Search Console.",
        invertido=True, faixa_top10=True))
    PAGINA.write_text(html, encoding="utf-8", newline="")
    print("graficos atualizados em cases/index.html")


if __name__ == "__main__":
    main()
