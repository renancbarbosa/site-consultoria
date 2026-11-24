# -*- coding: utf-8 -*-
"""
Mede a velocidade no celular de uma lista de sites, do mesmo jeito do teste das clínicas (28/10/2026):
Lighthouse (o motor do PageSpeed Insights do Google), modo celular padrão (4G lento simulado e
processador 4x mais lento), 3 testes por site, valor do meio de cada número.

Uso:
  python scripts/medir-velocidade-sites.py SELECAO.json SAIDA.json [--bruto PASTA] [--ate SEGUNDOS]
  ex.: python scripts/medir-velocidade-sites.py data/benchmark-construtoras-selecao.json data/benchmark-construtoras.json

SELECAO.json: {"consulta", "fonte", "regra", "empresas": [{"nome", "cidade", "url"} | {"nome", ..., "fora": "motivo"}]}
SAIDA.json (o gerador da página lê este formato):
  {"data", "mostrar_nomes", "metodo", "fonte", "regra",
   "fora": [{"nome", "url", "motivo"}],
   "resultados": [{"nome", "cidade", "url", "score", "notas", "lcp", "lcps", "peso_mb", "video_mb",
                   "lcp_elemento", "plataforma", "sinais", "gerador", "whatsapp", "https", "https_obs", "obs"}]}

Para cada site:
  1. Lighthouse 3 vezes, UM DE CADA VEZ: rodar em paralelo divide o processador e derruba a nota.
     Teste que falha é repetido (até 5 tentativas para juntar 3 válidos). Sem 3 válidos, o site vai
     para "fora", com o motivo.
  2. Cadeado: o endereço com https abre com certificado válido? O endereço sem https leva até ele?
  3. Chrome sem janela, em tela de celular, espera os scripts rodarem: procura link ou botão de
     WhatsApp e sinais da plataforma (WordPress, Wix...) no HTML já montado.
Site sem cadeado (endereço http://): desde o Chrome 154 (outubro de 2026) o navegador pede permissão
antes de abrir site público sem https (https://blog.google/security/https-by-defau/), e o teste
termina na tela de aviso. Para medir a página, só nesses endereços o Chrome do teste roda com
--disable-features=HttpsFirstBalancedModeAutoEnable (a opção que o guia do Chromium indica para testes
automáticos), como o visitante que clica em continuar. O resultado marca "aviso_chrome": true.
O Lighthouse sai com código 1 no Windows mesmo quando dá certo (falha ao apagar a pasta temporária do
Chrome): o script julga pelo relatório gravado, nunca pelo código de saída.
Retoma de onde parou: relatório que já está em --bruto não é medido de novo.
--ate SEGUNDOS: para sozinho perto desse tempo, grava o que tem e sai com código 3 (rodar de novo continua).
Serve para medir em blocos em primeiro plano: em 24/11/2026 a medição em segundo plano foi encerrada pelo
Claude Code por falta de memória no computador.
Grava a saída depois de cada site, para não perder nada se parar no meio.
"""
import http.client
import io
import json
import os
import re
import shutil
import ssl
import statistics
import subprocess
import sys
import tempfile
import time
import urllib.parse
from collections import defaultdict

LH = shutil.which("lighthouse")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
UA_PC = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/131.0.0.0 Safari/537.36")
UA_CEL = ("Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/131.0.0.0 Mobile Safari/537.36")
TESTES, TENTATIVAS = 3, 5
SEM_AVISO_HTTP = "--disable-features=HttpsFirstBalancedModeAutoEnable"


def sem_cadeado(url):
    return url.lower().startswith("http://")

# WhatsApp de CONTATO = link com número (wa.me/55..., ...send?phone=55...) ou encurtador wa.link.
# Link sem número (wa.me/?text=, send?text=) é botão de COMPARTILHAR e não conta.
_FONE = r"(?:\+|%2B)?\d{8,}"
WA_CONTATO = re.compile(r"""href\s*=\s*["']([^"']*(?:wa\.me/%s|wa\.link/\w+|(?:api|web)\.whatsapp\.com/send/?\?"""
                        r"""[^"']*phone=%s|whatsapp://send/?\?[^"']*phone=%s))""" % (_FONE, _FONE, _FONE), re.I)
WA_QUALQUER = re.compile(r"""href\s*=\s*["']([^"']*(?:wa\.me/|whatsapp\.com/|whatsapp://)[^"']*)""", re.I)
WA_BOTAO = re.compile(r"""(?:class|id)\s*=\s*["']([^"']*(?:whats|joinchat|wpp)[^"']*)""", re.I)
PLATAFORMAS = [
    ("Wix", r"static\.parastorage\.com|wixstatic\.com|_wixCssImports"),
    ("Webflow", r"data-wf-site|webflow\.js"),
    ("WordPress", r"/wp-content/|/wp-includes/|/wp-json"),
    ("Next.js", r"__NEXT_DATA__|/_next/static"),
    ("Nuxt", r"__NUXT__|/_nuxt/"),
    ("Gatsby", r"___gatsby"),
    ("Angular", r"\sng-version="),
]


def nos(x, achados):
    """Todos os nós de HTML ("type": "node") dentro de um trecho do relatório."""
    if isinstance(x, dict):
        if x.get("type") == "node":
            achados.append(x)
        for v in x.values():
            nos(v, achados)
    elif isinstance(x, list):
        for v in x:
            nos(v, achados)
    return achados


def ler(caminho):
    """Resumo de um relatório do Lighthouse; None se não existe; {"erro"} se o teste falhou."""
    try:
        d = json.load(io.open(caminho, encoding="utf-8"))
    except Exception:
        return None
    nota = (d.get("categories", {}).get("performance") or {}).get("score")
    if d.get("runtimeError") or nota is None:
        return {"erro": (d.get("runtimeError") or {}).get("code", "sem nota")}
    a = d["audits"]
    tipos = defaultdict(int)
    for it in a.get("network-requests", {}).get("details", {}).get("items", []):
        tipos[it.get("resourceType") or "Outro"] += it.get("transferSize") or 0
    no = nos(a.get("lcp-breakdown-insight", {}).get("details", {}), [])
    trecho = no[0].get("snippet", "") if no else ""
    tag = re.match(r"<(\w+)", trecho)
    return {
        "versao": d.get("lighthouseVersion"), "score": round(nota * 100),
        "lcp": a["largest-contentful-paint"]["numericValue"] / 1000,
        "fcp": a["first-contentful-paint"]["numericValue"] / 1000,
        "tbt": a["total-blocking-time"]["numericValue"],
        "cls": a["cumulative-layout-shift"]["numericValue"],
        "peso": a["total-byte-weight"]["numericValue"], "video": tipos.get("Media", 0),
        "imagens": tipos.get("Image", 0), "scripts": tipos.get("Script", 0),
        "lcp_tag": tag.group(1).lower() if tag else "", "lcp_trecho": trecho[:220],
        "final": d.get("finalDisplayedUrl") or "", "avisos": d.get("runWarnings") or [],
    }


class Pausa(Exception):
    """Acabou o tempo dado em --ate: grava o que já tem e para. Rodar de novo continua dali."""


FIM = None  # hora limite (time.time()) quando se usa --ate


def folga(normal, minimo):
    """Limite de tempo de um passo: o normal, ou o que sobra até FIM (e se foi cortado por isso).
    Sem 'minimo' segundos livres, nem começa: Pausa."""
    if FIM is None:
        return normal, False
    sobra = FIM - time.time()
    if sobra < minimo:
        raise Pausa()
    return (normal, False) if sobra >= normal else (sobra, True)


def rodar(cmd, limite, saida=False):
    """Roda cmd por até 'limite' segundos. Estourou: mata a árvore inteira de processos e devolve None.
    (No Windows, matar só o primeiro processo deixa o node do Lighthouse e o Chrome rodando soltos,
    disputando o processador com o teste seguinte.)"""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE if saida else subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        return p.communicate(timeout=limite)[0] or b""
    except subprocess.TimeoutExpired:
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            p.communicate(timeout=30)
        except subprocess.TimeoutExpired:
            pass
        return None


def lighthouse(url, destino):
    r = ler(destino)
    if r and "erro" not in r:
        return r
    limite, cortado = folga(240, 100)
    flags = "--headless=new" + (" " + SEM_AVISO_HTTP if sem_cadeado(url) else "")
    cmd = [LH, url, "--quiet", "--only-categories=performance", "--output=json",
           "--output-path=" + destino, "--chrome-flags=" + flags, "--disable-full-page-screenshot"]
    if rodar(cmd, limite) is None and cortado:
        raise Pausa()
    return ler(destino) or {"erro": "o teste não terminou em 4 minutos"}


def requisitar(url):
    """Um GET sem seguir redirecionamento: (status, Location) ou (None, motivo do erro)."""
    u = urllib.parse.urlsplit(url)
    if u.scheme == "https":
        c = http.client.HTTPSConnection(u.hostname, u.port or 443, timeout=20, context=ssl.create_default_context())
    else:
        c = http.client.HTTPConnection(u.hostname, u.port or 80, timeout=20)
    try:
        c.request("GET", u.path or "/", headers={"User-Agent": UA_PC, "Accept": "text/html"})
        r = c.getresponse()
        return r.status, r.getheader("Location") or ""
    except ssl.SSLCertVerificationError as ex:
        return None, "certificado: %s" % (ex.verify_message or ex)
    except Exception as ex:
        return None, "%s: %s" % (type(ex).__name__, str(ex)[:80])
    finally:
        c.close()


def cadeado(url):
    """'sim' (https válido e o endereço sem https leva até ele), 'parcial' (https válido, mas sem
    levar) ou 'não' (https não abre com certificado válido)."""
    host = urllib.parse.urlsplit(url).hostname
    st, info = requisitar("https://%s/" % host)
    if st is None:
        return "não", info
    atual, leva = "http://%s/" % host, False
    for _ in range(6):
        st2, loc = requisitar(atual)
        if st2 in (301, 302, 303, 307, 308) and loc:
            atual = urllib.parse.urljoin(atual, loc)
            if atual.startswith("https://"):
                leva = True
                break
            continue
        break
    return ("sim", "") if leva else ("parcial", "o endereço sem https não leva para a versão com cadeado")


def montado(url, perfil):
    """HTML da página depois que os scripts rodam (Chrome sem janela, tela de celular)."""
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
           "--user-data-dir=" + perfil, "--window-size=412,915", "--user-agent=" + UA_CEL,
           "--virtual-time-budget=15000"] + ([SEM_AVISO_HTTP] if sem_cadeado(url) else []) + ["--dump-dom", url]
    limite, cortado = folga(120, 30)
    out = rodar(cmd, limite, saida=True)
    if out is None:
        if cortado:
            raise Pausa()
        return ""
    return out.decode("utf-8", "replace")


def whatsapp(h):
    """('link' | 'botão' | '', prova). 'link' = contato com número; 'botão' = elemento de WhatsApp sem link
    com número (conferir a prova à mão); '' = nada, ou só botão de compartilhar."""
    m = WA_CONTATO.search(h)
    if m:
        return "link", re.sub(r"\d{6,}", "<número>", m.group(1))[:120]
    m = WA_BOTAO.search(h)
    if m:
        outro = WA_QUALQUER.search(h)
        return "botão", ("classe: %s | link: %s" % (m.group(1)[:60], outro.group(1)[:60] if outro else "-"))
    outro = WA_QUALQUER.search(h)
    return "", ("só compartilhar: %s" % outro.group(1)[:80]) if outro else ""


def analisar_html(h):
    sinais = [nome for nome, pad in PLATAFORMAS if re.search(pad, h, re.I)]
    gerador = re.search(r"""<meta[^>]+name=["']generator["'][^>]+content=["']([^"']+)""", h, re.I)
    wa, prova = whatsapp(h)
    return sinais, (gerador.group(1)[:80] if gerador else ""), wa, prova


def mediana(xs):
    return statistics.median(xs)


def main():
    global FIM
    if "--ate" in sys.argv:
        FIM = time.time() + float(sys.argv[sys.argv.index("--ate") + 1])
    if len(sys.argv) < 3 or not LH:
        sys.exit(__doc__ if LH else "lighthouse não encontrado no PATH")
    selecao, saida = sys.argv[1], sys.argv[2]
    bruto = (sys.argv[sys.argv.index("--bruto") + 1] if "--bruto" in sys.argv
             else os.path.join(tempfile.gettempdir(), "medir-velocidade",
                               os.path.splitext(os.path.basename(saida))[0]))
    os.makedirs(bruto, exist_ok=True)
    perfil = os.path.join(bruto, "perfil-chrome")
    sel = json.load(io.open(selecao, encoding="utf-8"))
    antigo = json.load(io.open(saida, encoding="utf-8")) if os.path.exists(saida) else {}
    if "--so-paginas" in sys.argv:  # refaz só WhatsApp e plataforma, sem repetir os testes de velocidade
        for r in antigo.get("resultados", []):
            h = montado(r["url"], perfil)
            if not h:
                print("SEM HTML  %s" % r["nome"], flush=True)
                continue
            r["sinais"], r["gerador"], r["whatsapp"], r["whatsapp_prova"] = analisar_html(h)
            r["html_montado_kb"] = len(h) // 1024
            print("%-34s wa=%-6s %-70s %s" % (r["nome"][:34], r["whatsapp"] or "-", r["whatsapp_prova"][:70],
                                             ",".join(r["sinais"]) or "-"), flush=True)
        io.open(saida, "w", encoding="utf-8", newline="\n").write(json.dumps(antigo, ensure_ascii=False, indent=1) + "\n")
        return
    res = {"data": antigo.get("data") or time.strftime("%Y-%m-%d"),
           "mostrar_nomes": bool(antigo.get("mostrar_nomes", False)),
           "metodo": antigo.get("metodo", ""), "fonte": sel.get("fonte"), "regra": sel.get("regra"),
           "fora": [], "resultados": []}
    prev = {r["url"]: r for r in antigo.get("resultados", [])}
    prev_fora = {f["nome"]: f for f in antigo.get("fora", [])}
    versao, pausou = "", False
    print("relatórios brutos em", bruto, flush=True)
    for n, emp in enumerate(sel["empresas"]):
        if emp.get("fora"):
            res["fora"].append({"nome": emp["nome"], "url": emp.get("site_informado") or "", "motivo": emp["fora"]})
            continue
        url, base = emp["url"], re.sub(r"[^a-z0-9]+", "-", emp["nome"].lower()).strip("-")
        try:
            item = medir_site(emp, url, base, bruto, perfil, prev.get(url) or {})
        except Pausa:  # o que não deu tempo de fazer agora fica como estava no arquivo
            pausou = True
            for resto in sel["empresas"][n:]:
                if resto.get("fora"):
                    res["fora"].append({"nome": resto["nome"], "url": resto.get("site_informado") or "",
                                        "motivo": resto["fora"]})
                elif resto["url"] in prev:
                    res["resultados"].append(prev[resto["url"]])
                elif resto["nome"] in prev_fora:
                    res["fora"].append(prev_fora[resto["nome"]])
            item = None
        if item and "motivo" in item:
            res["fora"].append(item)
            print("FORA  %-34s %s" % (emp["nome"], item["motivo"]), flush=True)
        elif item:
            versao = item.pop("_versao")
            res["resultados"].append(item)
            print("ok    %-34s nota %3d %-13s LCP %5.1fs  peso %5.1f MB  vídeo %4.1f MB  %-6s wa=%-6s https=%-7s %s" % (
                emp["nome"][:34], item["score"], str(item["notas"]), item["lcp"], item["peso_mb"], item["video_mb"],
                item["lcp_elemento"], item["whatsapp"] or "-", item["https"], ",".join(item["sinais"]) or "-"),
                flush=True)
        if versao:
            res["metodo"] = ("Lighthouse %s (o motor do PageSpeed Insights), modo celular padrão: 4G lento simulado e "
                             "processador 4x mais lento. 3 testes por site, um de cada vez, e o valor do meio de cada "
                             "número. Cadeado conferido por conexão direta; WhatsApp e plataforma conferidos no HTML "
                             "montado pelo Chrome em tela de celular." % versao)
        io.open(saida, "w", encoding="utf-8", newline="\n").write(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
        if pausou:
            print("PAUSA: acabou o tempo de --ate (%d medidos até aqui). Rode o mesmo comando de novo para continuar."
                  % len(res["resultados"]), flush=True)
            sys.exit(3)
    print("medidos: %d | fora: %d | gravado em %s" % (len(res["resultados"]), len(res["fora"]), saida), flush=True)


def medir_site(emp, url, base, bruto, perfil, velho):
    """3 testes bons (até 5 tentativas) + cadeado + página montada. Devolve o resultado, ou
    {"nome", "url", "motivo"} quando o site fica fora. A página já conferida com a regra atual do
    WhatsApp (tem "whatsapp_prova") não é aberta de novo, e o que foi preenchido à mão é mantido."""
    bons, erros = [], []
    for i in range(1, TENTATIVAS + 1):
        if len(bons) == TESTES:
            break
        r = lighthouse(url, os.path.join(bruto, "%s-%d.json" % (base, i)))
        (erros if "erro" in r else bons).append(r)
    if len(bons) < TESTES:
        return {"nome": emp["nome"], "url": url, "motivo": "o teste não conseguiu abrir a página (%s)"
                % ", ".join(sorted(set(e["erro"] for e in erros)))}
    if "whatsapp_prova" in velho and velho["whatsapp"] != "não conferido":
        https, https_obs, html_kb = velho["https"], velho["https_obs"], velho["html_montado_kb"]
        sinais, gerador, wa, wa_prova = velho["sinais"], velho["gerador"], velho["whatsapp"], velho["whatsapp_prova"]
    else:
        folga(60, 60)
        https, https_obs = cadeado(bons[0]["final"] or url)
        # 2 tentativas: em 24/11/2026 as 5 primeiras leituras de um bloco voltaram vazias e,
        # repetidas logo depois, funcionaram
        h = montado(url, perfil) or montado(url, perfil)
        sinais, gerador, wa, wa_prova = analisar_html(h) if h else ([], "", "não conferido", "")
        html_kb = len(h) // 1024
    tags = [b["lcp_tag"] for b in bons if b["lcp_tag"]]
    return {
        "nome": emp["nome"], "cidade": emp.get("cidade", ""), "url": url,
        "score": round(mediana([b["score"] for b in bons])), "notas": [b["score"] for b in bons],
        "lcp": round(mediana([b["lcp"] for b in bons]), 1), "lcps": [round(b["lcp"], 1) for b in bons],
        "fcp": round(mediana([b["fcp"] for b in bons]), 1),
        "tbt_ms": round(mediana([b["tbt"] for b in bons])),
        "cls": round(mediana([b["cls"] for b in bons]), 3),
        "peso_mb": round(mediana([b["peso"] for b in bons]) / 1048576, 1),
        "imagens_mb": round(mediana([b["imagens"] for b in bons]) / 1048576, 1),
        "scripts_mb": round(mediana([b["scripts"] for b in bons]) / 1048576, 1),
        "video_mb": round(mediana([b["video"] for b in bons]) / 1048576, 1),
        "lcp_elemento": max(set(tags), key=tags.count) if tags else "",
        "lcp_trecho": bons[0]["lcp_trecho"],
        "plataforma": velho.get("plataforma", ""), "sinais": sinais, "gerador": gerador,
        "whatsapp": wa, "whatsapp_prova": wa_prova,
        "https": https, "https_obs": https_obs, "aviso_chrome": sem_cadeado(url),
        "html_montado_kb": html_kb,
        "avisos": sorted(set(w for b in bons for w in b["avisos"]))[:3], "obs": velho.get("obs", ""),
        "_versao": bons[0]["versao"],
    }


if __name__ == "__main__":
    main()
