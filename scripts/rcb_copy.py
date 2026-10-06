"""Copy humana e para leigo (pedido do Renan, 05/10/2026). Fonte unica das regras de texto do site.

humanizar(html) faz, so no TEXTO (nunca em URL, classe, codigo ou estilo):
  1. tira os travessoes (— e –): vira virgula, dois-pontos, ponto ou parenteses, conforme a frase;
     intervalo de numero ("1–2") vira "1 a 2"; no <title> vira " | ".
  2. troca palavras com cara de texto de IA ("jornada", "essencial", "alavanca", "Alem disso"...);
  3. troca jargao que tem equivalente simples ("lead" -> "contato", "CTA" -> "botao de chamada");
  4. explica o termo tecnico na PRIMEIRA vez que ele aparece no corpo da pagina (paragrafo ou item
     de lista), entre parenteses, em palavras simples. Titulo, H1, H2, menu e links nao sao tocados:
     o termo de busca continua neles (decisao do Renan: "SEO" fica nos titulos).

Idempotente: rodar de novo nao muda nada. Usado na gravacao pelos geradores (rcb_base.escrever,
gerar-servicos-marketing.py, gerar-paginas-cidades.py) e aplicado ao site por
scripts/copy-humana-2026-10-05.py.
"""
import re

TRAV = "—–"  # — e –

# ------------------------------------------------------------------ 1. travessoes
_INICIO_FRASE = {"Não", "É", "O", "A", "Os", "As", "Você", "Eu", "Isso", "Isto", "Se", "Quem", "Para",
                 "Mas", "E", "Nada", "Tudo", "Sem", "Com", "Cada", "Nenhum", "Nenhuma", "Ninguém", "Aqui"}


# depois do travessao vem uma explicacao da primeira parte: dois-pontos le melhor que virgula
_EXPLICA = {"é", "ela", "ele", "eles", "elas", "isso", "você", "eu", "documenta", "são"}


# palavras que continuam a frase: em titulo de secao o travessao antes delas vira virgula, nao dois-pontos
_EMENDA = {"e", "ou", "mas", "sem", "com", "desde", "inclusive", "porque", "que", "nem"}


def _limpa(t):
    t = re.sub(r"\s+,", ",", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r",\s*([.!?;:)])", r"\1", t)
    t = re.sub(r"([:(])\s*,\s*", r"\1 ", t)
    t = re.sub(r":\s*:", ":", t)
    t = re.sub(r"\(\s+", "(", t)
    t = re.sub(r"(\S)[ \t]{2,}", r"\1 ", t)
    return t


def _troca_par(m):
    dentro = m.group(2).strip()
    if "," in dentro or len(dentro.split()) > 12:
        return "%s (%s)%s" % (m.group(1).rstrip(), dentro, m.group(3))
    return "%s, %s,%s" % (m.group(1).rstrip(), dentro, m.group(3))


def _troca_simples(antes, depois, sep):
    antes_r = antes.rstrip()
    depois_l = depois.lstrip()
    if not antes_r.strip():
        return antes[:len(antes) - len(antes.lstrip())] + depois_l
    if not depois_l:
        # travessao no fim do trecho: o que vem depois esta em outra tag ("Ramo — <strong>44</strong>")
        return antes_r + (": " if antes_r[-1] not in "?!.:;,(" else " ")
    if antes_r[-1] in "?!.:;,(":
        return antes_r + " " + depois_l
    primeira = re.match(r"[\wÀ-ÿ]+", depois_l)
    if sep == ": " and primeira and primeira.group(0).lower() in _EMENDA:
        return antes_r + ", " + depois_l  # "Avaliações — e respostas" vira "Avaliações, e respostas"
    if sep:
        return antes_r + sep + depois_l
    primeira = re.match(r"[\wÀ-ÿ]+", depois_l)
    if primeira and primeira.group(0) in _EXPLICA and len(antes_r.split()) > 3:
        return antes_r + ": " + depois_l
    if primeira and primeira.group(0) in _INICIO_FRASE and len(antes_r.split()) > 5:
        return antes_r + ". " + depois_l
    return antes_r + ", " + depois_l


def sem_travessao(t, sep=None):
    """sep=None: decide entre virgula e ponto; sep=": " em cabecalho/botao; sep=" | " no <title>."""
    if not any(c in t for c in TRAV):
        return t
    t = re.sub(r"(\d)\s*[%s]\s*(\d)" % TRAV, r"\1 a \2", t)
    t = re.sub(r"(\w)[%s](\w)" % TRAV, r"\1 a \2", t)  # Seg–Sex, 9h–18h
    # travessao no comeco do trecho (o texto anterior esta em outra tag): ": " antes de numero, senao ", "
    m = re.match(r"\s*[%s]\s*" % TRAV, t)
    if m:
        t = (": " if t[m.end():m.end() + 1].isdigit() else ", ") + t[m.end():]
    if sep is None:
        # ";" e ":" tambem fecham o trecho: sem isso o par pegava "— x; y; z —" e embaralhava os parenteses
        par = re.compile(r"([^%s.!?;:]*?)\s[%s]\s([^%s.!?;:()]+?)\s[%s](\s?)" % (TRAV, TRAV, TRAV, TRAV))
        for _ in range(5):
            novo = par.sub(_troca_par, t, count=1)
            if novo == t:
                break
            t = novo
    for _ in range(30):
        m = re.search(r"\s*[%s]\s*" % TRAV, t)
        if not m:
            break
        t = _troca_simples(t[:m.start()], t[m.end():], sep)
    return _limpa(t)


# ------------------------------------------------------------------ 2. palavras de IA
_ART_JORNADA = {"a": "o", "da": "do", "na": "no", "pela": "pelo", "toda a": "todo o", "sua": "seu", "essa": "esse",
                "esta": "este", "uma": "um", "nessa": "nesse", "nesta": "neste", "dessa": "desse", "desta": "deste"}


def _jornada(m):
    art = m.group(1)
    novo = _ART_JORNADA.get(art.lower(), art)
    if art[:1].isupper():
        novo = novo[:1].upper() + novo[1:]
    return novo + " caminho" + ("s" if m.group(2) else "")


IA = [
    (re.compile(r"\b(toda a|nessa|nesta|dessa|desta|pela|da|na|sua|essa|esta|uma|a)\s+jornada(s?)\b", re.I), _jornada),
    (re.compile(r"\bjornada(s?)\b"), lambda m: "caminho" + m.group(1)),
    (re.compile(r"\b([Oo]) essencial\b"), lambda m: m.group(1) + " básico"),
    (re.compile(r"\bessenciais\b"), "importantes"),
    (re.compile(r"\bessencial\b"), "importante"),
    (re.compile(r"\bEssencial\b"), "Importante"),
    (re.compile(r"\bAlém disso,\s*"), "Também "),
    (re.compile(r"\balém disso,\s*"), "também "),
    (re.compile(r"\balavancas\b"), "ferramentas"),
    (re.compile(r"\balavanca\b"), "ferramenta"),
    (re.compile(r"\bDescubra\b"), "Veja"),
    (re.compile(r"\bdescubra\b"), "veja"),
    (re.compile(r"\bEm resumo:"), "Resumindo:"),
    (re.compile(r"\bEm resumo,\s*"), "Resumindo, "),
    (re.compile(r"\bA verdade é que (\w)"), lambda m: m.group(1).upper()),
    (re.compile(r"\brobustos\b"), "completos"),
    (re.compile(r"\brobusta\b"), "completa"),
    (re.compile(r"\brobusto\b"), "completo"),
    (re.compile(r"\bpotencializa\b"), "fortalece"),
    (re.compile(r"\bpotencializar\b"), "fortalecer"),
    (re.compile(r"\bé fundamental\b"), "é muito importante"),
    (re.compile(r"\bmergulho técnico aprofundado\b"), "análise técnica detalhada"),
    (re.compile(r"\bVale destacar\b"), "Vale falar"),
    (re.compile(r"\bvale destacar\b"), "vale falar"),
]


def sem_ia(t):
    for rx, novo in IA:
        t = rx.sub(novo, t)
    return t


# ------------------------------------------------------------------ 3. jargao com troca direta
JARGAO = [
    (re.compile(r"\bleads\b"), "contatos"),
    (re.compile(r"\bLeads\b"), "Contatos"),
    (re.compile(r"\blead\b"), "contato"),
    (re.compile(r"\bLead\b"), "Contato"),
    (re.compile(r"\bCTAs\b"), "botões de chamada"),
    (re.compile(r"\bCTA\b"), "botão de chamada"),
    (re.compile(r"\btráfego orgânico\b"), "visitas que chegam do Google sem anúncio"),
]


def sem_jargao(t):
    for rx, novo in JARGAO:
        t = rx.sub(novo, t)
    return t


# ------------------------------------------------------------------ 4. explicacao do termo (1a vez)
GLOSSARIO = [
    ("seo", re.compile(r"(?<!RCB )\bSEO(?: [Ll]ocal)?\b"),
     "o trabalho de fazer o Google mostrar a sua empresa de graça para quem procura o que você vende"),
    ("gmn", re.compile(r"\bGoogle (?:Meu Negócio|Perfil da Empresa)\b"),
     "a ficha da sua empresa no Google Maps, com endereço, horário, fotos e avaliações"),
    ("landing", re.compile(r"\blanding pages?\b", re.I),
     "uma página feita só para receber quem clicou no anúncio e levar a pessoa a chamar no WhatsApp"),
    ("ads", re.compile(r"\bGoogle Ads\b"), "os anúncios que aparecem no topo da pesquisa do Google"),
    ("trafego", re.compile(r"\btráfego pago\b", re.I), "anúncio pago, como no Google ou no Instagram"),
    ("indexacao", re.compile(r"\b(?:indexad[oa]s?|indexação|indexar)\b"),
     "quando o Google guarda a página no catálogo dele e passa a poder mostrá-la"),
    ("ranque", re.compile(r"\b(?:ranqueamento|ranquear|ranqueia|ranqueiam)\b"),
     "a posição em que o Google mostra a página"),
    ("organico", re.compile(r"\borgânic[oa]s?\b"), "o resultado gratuito, que aparece abaixo dos anúncios"),
    ("conversao", re.compile(r"\bconvers(?:ão|ões)\b"), "quando a visita vira contato"),
    ("nap", re.compile(r"\bNAP\b"), "nome, endereço e telefone"),
    ("console", re.compile(r"\bSearch Console\b"),
     "a ferramenta gratuita do Google que mostra como o site aparece nas buscas"),
    ("palavra", re.compile(r"\bpalavras?-chave\b"), "as palavras que o cliente digita no Google"),
    ("algoritmo", re.compile(r"\balgoritmo\b"), "as regras que o Google usa para decidir quem aparece primeiro"),
    ("schema", re.compile(r"\b(?:dados estruturados|schema)\b"),
     "uma ficha escondida no site que conta ao Google quem é a empresa"),
    ("cluster", re.compile(r"\bclusters?\b"), "um grupo de textos sobre o mesmo assunto"),
]


def _explica(t, ja):
    for chave, rx, expl in GLOSSARIO:
        if chave in ja:
            continue
        m = rx.search(t)
        if not m:
            continue
        ja.add(chave)
        resto = t[m.end():]
        # ja explicado ali mesmo: "(...)" logo depois, ou a frase define o termo ("SEO local é ...")
        if resto.lstrip().startswith("(") or re.match(r"\s+(?:é|são|significa|quer dizer)\b", resto):
            continue
        t = t[:m.end()] + " (" + expl + ")" + resto
    return t


# ------------------------------------------------------------------ montagem
_TAG = re.compile(r"(<!--.*?-->|<[^>]+>)", re.S)
_ATRIB = re.compile(r'((?:content|alt|title|aria-label|placeholder)=")([^"]*)(")')
CORPO = ("p", "li", "td", "dd", "blockquote", "figcaption")
FORA_GLOSS = ("a", "h1", "h2", "h3", "h4", "h5", "h6", "button", "title", "summary", "label", "nav", "footer",
              "header", "strong", "th", "option", "dt", "head")
ROTULO = ("h1", "h2", "h3", "h4", "h5", "h6", "button", "th", "dt", "summary", "label", "option")
VAZIAS = ("br", "img", "meta", "link", "input", "hr", "source", "wbr", "col", "area", "base", "embed", "param", "track")


def _ja_explicados(html):
    return {chave for chave, rx, expl in GLOSSARIO if "(" + expl + ")" in html}


_ENT = re.compile(r"&(?:mdash|#8212|#x2014);|&(?:ndash|#8211|#x2013);", re.I)

# Pagina protegida (4o lugar no Google): o Renan autorizou SO tirar travessao (05/10/2026).
# Nela nao entram explicacao entre parenteses nem troca de jargao.
PROTEGIDAS = ('rel="canonical" href="https://rcbseo.com.br/consultor-seo-goiania/"',)


def humanizar(html):
    # travessao escrito como codigo HTML (&mdash;, &#8212;...) vira o caractere, para ser tratado igual
    html = _ENT.sub(lambda m: "—" if ("m" in m.group(0).lower() or "8212" in m.group(0)
                                           or "2014" in m.group(0)) else "–", html)
    protegida = any(m in html for m in PROTEGIDAS)
    pilha = {}
    ja = _ja_explicados(html)
    script_ld = em_script = em_style = False
    saida = []
    for parte in _TAG.split(html):
        if not parte:
            continue
        if parte.startswith("<!--"):
            saida.append(parte)
            continue
        if parte.startswith("<"):
            m = re.match(r"<\s*(/?)\s*([a-zA-Z0-9]+)", parte)
            if m:
                fecha, nome = m.group(1) == "/", m.group(2).lower()
                if nome == "script":
                    em_script = not fecha
                    script_ld = (not fecha) and "ld+json" in parte
                elif nome == "style":
                    em_style = not fecha
                elif nome not in VAZIAS and not parte.endswith("/>"):
                    pilha[nome] = max(0, pilha.get(nome, 0) + (-1 if fecha else 1))
                if not fecha and nome not in ("script", "style", "link"):
                    sep = " | " if (nome == "meta" and re.search(r'(?:og|twitter):title"', parte)) else None
                    parte = _ATRIB.sub(lambda a: a.group(1) + sem_ia(sem_travessao(a.group(2), sep)) + a.group(3),
                                       parte)
            saida.append(parte)
            continue
        if em_style or (em_script and not script_ld):
            saida.append(parte)
            continue
        if script_ld:
            saida.append(sem_ia(sem_travessao(parte)))
            continue
        if pilha.get("title"):
            saida.append(sem_ia(sem_travessao(parte, " | ")))
            continue
        sep = ": " if any(pilha.get(n) for n in ROTULO) else None
        t = sem_ia(sem_travessao(parte, sep))
        if not protegida and any(pilha.get(n) for n in CORPO) and not any(pilha.get(n) for n in FORA_GLOSS):
            t = _explica(sem_jargao(t), ja)
        saida.append(t)
    return "".join(saida)


def texto(t):
    """Texto puro (llms.txt, llms-full.txt): travessao e palavras de IA. Em item de lista
    "nome: url — descricao", o travessao vira dois-pontos."""
    linhas = []
    for linha in t.split("\n"):
        if re.match(r"\s*[-*]\s", linha):
            linha = re.sub(r"\s[%s]\s" % TRAV, ". ", linha)
        linhas.append(sem_ia(sem_travessao(linha)))
    return "\n".join(linhas)
