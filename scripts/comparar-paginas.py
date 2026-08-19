# -*- coding: utf-8 -*-
import re,os,sys,io,json,glob,subprocess
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
ALVOS=["consultor-seo-goiania","seo-local-goiania","consultoria-seo-local","seo-para-clinicas-de-estetica",
       "seo-para-clinicas","para-comercios-locais","google-perfil-empresa","como-aparecer-no-google",
       "seo-para-contadores","site-otimizado-para-seo","site-para-clinica","seo-para-dentistas"]
def txt(h):
    h=re.sub(r"(?is)<(script|style|template)[^>]*>.*?</\1>"," ",h)
    h=re.sub(r"(?s)<!--.*?-->"," ",h); h=re.sub(r"<[^>]+>"," ",h)
    return re.sub(r"\s+"," ",h).strip()
# links internos recebidos (fora nav/rodape/barra) — conta ocorrencias no site inteiro
todos=[p for p in glob.glob("**/index.html",recursive=True) if "node_modules" not in p and "graphify-out" not in p]
def corpo(h):
    h=re.sub(r"(?is)<nav.*?</nav>"," ",h); h=re.sub(r"(?is)<footer.*?</footer>"," ",h)
    h=re.sub(r"(?is)<!-- RCB:CTA-MOBILE.*?-->.*?<!-- /RCB:CTA-MOBILE.*?-->"," ",h)
    h=re.sub(r'(?is)<div class="cta-mobile".*?</div>\s*</div>'," ",h)
    return h
cache={p:open(p,encoding="utf-8",errors="ignore").read() for p in todos}
print(f"{'pagina':32s} {'pal':>5} {'H2':>3} {'H3':>3} {'lk-in':>6} {'lkOut':>6} {'schema':>7} {'goiania':>8} {'1a mod':>12}")
for a in ALVOS:
    p=os.path.join(a,"index.html")
    if not os.path.exists(p): print(f"{a:32s}  --- nao existe ---"); continue
    h=cache[p]; t=txt(corpo(h))
    pal=len(t.split())
    h2=len(re.findall(r"(?i)<h2",h)); h3=len(re.findall(r"(?i)<h3",h))
    schema=len(re.findall(r'application/ld\+json',h))
    tipos=",".join(sorted(set(re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"',h))))
    goi=len(re.findall(r"(?i)goi[âa]nia",t))
    lkin=sum(len(re.findall(rf'href="[^"]*/{re.escape(a)}/"',corpo(v))) for k,v in cache.items() if k!=p)
    lkout=len(set(re.findall(r'href="(https?://(?!rcbseo)[^"]+)"',corpo(h))))
    data=subprocess.run(["git","log","-1","--diff-filter=A","--format=%ad","--date=short","--",p],capture_output=True,text=True).stdout.strip()
    print(f"{a:32s} {pal:5d} {h2:3d} {h3:3d} {lkin:6d} {lkout:6d} {schema:7d} {goi:8d} {data:>12}")
    print(f"     tipos schema: {tipos}")
    print(f"     title: {re.search(r'(?is)<title>(.*?)</title>',h).group(1).strip()[:110]}")
    m=re.search(r"(?is)<h1[^>]*>(.*?)</h1>",h)
    print(f"     H1   : {re.sub(r'<[^>]+>','',m.group(1)).strip()[:110] if m else 'SEM H1'}")
