"""Aplica a marca oficial "RCB SEO" no site inteiro (decisao do Renan, 04/10/2026).

Fonte unica dos dados: data/marca.json (lida por scripts/rcb_marca.py).

O que faz em cada pagina:
  1. Fichas JSON-LD: no da empresa vira "RCB SEO" com alternateName, geo, hasMap e
     sameAs; WebSite, publisher, provider e author que apontam para a empresa
     passam a usar o mesmo nome; "#localbusiness" passa a ser "#business".
  2. Titulos (<title>, og:title, twitter:title e o nome da pagina no JSON-LD):
     sufixo "| RCB", "| RCB Consultoria", "— RCBSEO" vira "| RCB SEO". Os que
     passariam de 65 caracteres tem o RESTO encurtado (nunca a marca).
  3. Texto visivel, og:site_name, alt, rodape: nome antigo da marca vira "RCB SEO".
     "consultoria de SEO" (o servico) nao e tocado: so casa "RCB Consultoria".
  4. /contato/: mapa so de endereco vira o mapa do perfil no Google (cid).
  5. llms.txt: nome novo + linha com os nomes alternativos.

NAO toca: paginas de cidade em noindex (ficam como estao), URLs, pastas e imagens.
Mantido de proposito: assunto e remetente do e-mail de lead do formulario da home
(podem ter filtro de e-mail configurado).

Idempotente: a 2a execucao tem que dizer "alterados: 0".
    python scripts/aplicar-marca-2026-10-04.py
"""
import glob
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import rcb_marca as M  # noqa: E402

RAIZ = os.path.dirname(AQUI)
S = re.S

# titulos que passariam de 65 com a marca nova, SEM trafego no Search Console
# (28 dias ate 01/10/2026: zero clique e posicao pior que 20): encurta o resto, nunca a marca
ENCURTAR = {
    "Como saber se sua empresa está perdendo clientes no Google":
        "Empresa perdendo clientes no Google: como saber",
    "Como Aparecer no Google: o Passo a Passo para Sua Empresa":
        "Como Aparecer no Google: Passo a Passo para Sua Empresa",
    "Vale a Pena Contratar um Consultor de Google Meu Negócio?":
        "Vale a Pena Contratar Consultor de Google Meu Negócio?",
    "SEO para prestadores de serviço: como aparecer no Google":
        "SEO para prestadores de serviço: apareça no Google",
}
# titulos COM trafego (clique ou posicao ate 20): o texto original nao muda.
# A marca nao cabe em 65 caracteres, entao o titulo fica sem marca (decisao do Renan).
MANTER_SEM_MARCA = {
    "Otimização do Google Perfil da Empresa (Google Meu Negócio)",
    "Erros que impedem uma empresa local de aparecer no Google",
    "Vale a pena contratar consultor de SEO ou fazer sozinho?",
    "Por que Minha Clínica Odontológica Não Aparece no Google",
    "Consultoria de SEO em Joinville (SC) | Apareça no Google",
}
LIMITE_TITULO = 65

TIPOS_EMPRESA = ("Organization", "LocalBusiness", "ProfessionalService")
ID_LOCAL = "https://rcbseo.com.br/#localbusiness"
IDS_EMPRESA = (M.ID_EMPRESA, ID_LOCAL, "https://rcbseo.com.br/#organization")
# a pagina protegida tem @id proprio: recebe nome e dados, o @id fica
ID_PROTEGIDA = "https://rcbseo.com.br/consultor-seo-goiania/#business"

# ficam com o nome antigo de proposito (listados no relatorio)
INTENCIONAIS = [
    re.compile(r'name="subject" value="Novo lead — RCB Consultoria \(site\)"'),
    re.compile(r'name="from_name" value="Site RCB Consultoria"'),
]


def ler(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def gravar(p, t):
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def tipos(no):
    t = no.get("@type")
    return t if isinstance(t, list) else [t]


def eh_empresa(no):
    if no.get("@id") in IDS_EMPRESA or no.get("@id") == ID_PROTEGIDA:
        return True
    nome = no.get("name")
    return any(t in TIPOS_EMPRESA for t in tipos(no)) and isinstance(nome, str) and "RCB" in nome


def novo_titulo(t):
    """Marca nova no sufixo e, se passar de 65, o resto encurtado."""
    n = M.titulo(t)
    if len(n) > LIMITE_TITULO:
        m = re.match(r'^(.*?)(\s[|—–-]\s' + re.escape(M.NOME) + r')$', n)
        if m:
            corpo, suf = m.group(1), m.group(2)
            if corpo in MANTER_SEM_MARCA:
                return corpo
            corpo = ENCURTAR.get(corpo, corpo)
            if len(corpo + suf) > LIMITE_TITULO:  # paginas de cidade
                corpo = re.sub(r' \| Apareça no Google$', '', corpo)
            n = corpo + suf
    return n


def trata_no(no):
    """Percorre o JSON-LD trocando a marca (altera no lugar)."""
    if isinstance(no, list):
        return [trata_no(x) for x in no]
    if isinstance(no, str):
        return M.texto(no)
    if not isinstance(no, dict):
        return no
    if eh_empresa(no):
        if no.get("@id") == ID_LOCAL:
            no["@id"] = M.ID_EMPRESA
        if "name" in no:  # referencia curta ({"@id": ...}) continua curta
            no["name"] = M.NOME
        if any(k in no for k in ("address", "telephone", "openingHoursSpecification")):
            no.update(M.extras_empresa())
            for k in ("legalName", "taxID", "priceRange", "offers"):
                no.pop(k, None)
    elif "WebSite" in tipos(no):
        no["name"] = M.NOME
    for k, v in list(no.items()):
        if k == "alternateName":
            continue
        if k in ("name", "headline") and isinstance(v, str):
            no[k] = M.texto(novo_titulo(v))
        else:
            no[k] = trata_no(v)
    return no


def trata_jsonld(bloco):
    d = json.loads(bloco)
    antes = json.dumps(d, ensure_ascii=False, sort_keys=True)
    d = trata_no(d)
    if json.dumps(d, ensure_ascii=False, sort_keys=True) == antes:
        return bloco
    if "\n" in bloco.strip():
        base = re.match(r'\s*', bloco).group(0)
        recuo_base = base.split("\n")[-1]
        ind = re.search(r'\n([ \t]+)"', bloco)
        passo = max(1, len(ind.group(1)) - len(recuo_base)) if ind else 2
        out = json.dumps(d, ensure_ascii=False, indent=passo)
        out = out.replace("\n", "\n" + recuo_base)
        return base + out + re.search(r'\s*$', bloco).group(0)
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))


def trata_texto(t, rel):
    def _tit(m):
        return m.group(1) + novo_titulo(m.group(2)) + m.group(3)
    t = re.sub(r'(<title>)(.*?)(</title>)', _tit, t, flags=S)
    t = re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")([^"]*)(")', _tit, t)
    t = re.sub(r'(<meta property="og:site_name" content=")[^"]*(")', r'\g<1>' + M.NOME + r'\2', t)
    # privacidade: o nome da marca tinha ganho um link de "fonte oficial" no meio
    t = re.sub(r'operando como RCB Consultoria de <a [^>]*>SEO</a>', 'operando como ' + M.NOME, t)
    if rel.replace("\\", "/") == "contato/index.html":
        t = re.sub(r'(<iframe src=")https://www\.google\.com/maps\?q=[^"]*(")',
                   r'\g<1>' + M.MARCA["mapa_embed"].replace("&", "&amp;") + r'\2', t)
        t = t.replace('title="Mapa: localização da RCB Consultoria em Goiânia"',
                      'title="Mapa: perfil da %s no Google, em Goiânia"' % M.NOME)
    guardados = []

    def _guarda(m):
        guardados.append(m.group(0))
        return "\x00%d\x00" % (len(guardados) - 1)
    for rx in INTENCIONAIS:
        t = rx.sub(_guarda, t)
    t = M.texto(t)
    return re.sub(r'\x00(\d+)\x00', lambda m: guardados[int(m.group(1))], t)


def trata_html(h, rel, avisos):
    # JSON-LD primeiro e em separado: o nome do no nao pode virar "RCB SEO - SEO Local..."
    partes = re.split(r'(<script[^>]+application/ld\+json[^>]*>)(.*?)(</script>)', h, flags=S)
    saida = []
    for i, parte in enumerate(partes):
        if i % 4 == 2:
            try:
                parte = trata_jsonld(parte)
            except Exception as e:  # noqa: BLE001
                avisos.append("%s: JSON-LD nao abriu (%s) - bloco nao tocado" % (rel, e))
        elif i % 4 == 0:
            parte = trata_texto(parte, rel)
        saida.append(parte)
    return "".join(saida)


def trata_llms(t):
    nl = "\r\n" if "\r\n" in t else "\n"
    # tira a linha de nomes alternativos antes da troca (senao ela vira "RCB SEO, ..., RCB SEO")
    t = re.sub(r'(?:\r?\n)*Também conhecida como:[^\n]*\n?', nl, t)
    t = M.texto(t)
    linha = "Também conhecida como: " + ", ".join(M.ALTERNATIVOS) + "."
    t = re.sub(r'^(# ' + re.escape(M.NOME) + r')(?:\r?\n)+', lambda m: m.group(1) + nl + nl + linha + nl + nl, t, count=1)
    return t


def eh_cidade_escondida(rel, h):
    rel = rel.replace("\\", "/")
    return (rel.startswith("consultoria-seo/") and rel != "consultoria-seo/index.html"
            and re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', h, re.I))


def main():
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True)
             if not os.path.relpath(p, RAIZ).startswith(("scripts", "docs", "node_modules", ".git", "data"))]
    alterados, pulados, avisos, erros = 0, 0, [], []
    for p in sorted(alvos):
        rel = os.path.relpath(p, RAIZ)
        h0 = ler(p)
        if eh_cidade_escondida(rel, h0):
            pulados += 1  # recebem a marca (decisao do Renan, 04/10); o noindex nao e tocado
        h = trata_html(h0, rel, avisos)
        if eh_cidade_escondida(rel, h0) and not eh_cidade_escondida(rel, h):
            erros.append(rel + ": perdeu o noindex")
            continue
        if h == h0:
            continue
        if h0.lstrip().lower().startswith("<!doctype") and not h.lstrip().lower().startswith("<!doctype"):
            erros.append(rel + ": perdeu o <!DOCTYPE>")
            continue
        ok = True
        for b in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h, S):
            try:
                json.loads(b)
            except Exception:  # noqa: BLE001
                erros.append(rel + ": JSON-LD invalido depois da troca")
                ok = False
                break
        if ok:
            gravar(p, h)
            alterados += 1
    p = os.path.join(RAIZ, "llms.txt")
    t0 = ler(p)
    t = trata_llms(t0)
    if t != t0:
        gravar(p, t)
        alterados += 1
    print("paginas conferidas       :", len(alvos))
    print("cidades em noindex (marca aplicada, noindex mantido):", pulados)
    print("alterados                :", alterados)
    for a in avisos:
        print("AVISO:", a)
    if erros:
        print("ERROS (arquivos NAO gravados):")
        for e in erros:
            print("   ", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
