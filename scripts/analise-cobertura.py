# -*- coding: utf-8 -*-
"""Cruza as URLs do sitemap com o desempenho do Search Console (90d)."""
import json,os,re,sys,io,csv
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
D="data/audit"
def load(n): return json.load(open(os.path.join(D,n),encoding="utf-8")).get("rows",[]) or []
def s(u): return u.replace("https://rcbseo.com.br","") or "/"
sitemap=[s(m) for m in re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml",encoding="utf-8").read())]
gsc={s(r["keys"][0]):r for r in load("raw_90d_page.json")}
qp=load("raw_90d_query_page.json")
bestq={}
for r in qp:
    u=s(r["keys"][1])
    if u not in bestq or r["impressions"]>bestq[u]["impressions"]: bestq[u]=r

cidades=[u for u in sitemap if u.startswith("/consultoria-seo/")]
outros=[u for u in sitemap if not u.startswith("/consultoria-seo/")]
print(f"sitemap={len(sitemap)} | cidades={len(cidades)} | demais={len(outros)}")

def linha(u):
    g=gsc.get(u); b=bestq.get(u)
    if not g: return f'  {"":>6} {"":>4} {"":>6}  {u}   << SEM SINAL'
    return f'  {g["impressions"]:6d}i {g["clicks"]:3d}c pos{g["position"]:6.1f}  {u}' + (f'   | "{b["keys"][0]}"' if b else "")

print("\n===== PAGINAS DO SITEMAP (fora cidades) — ordenadas por impressao =====")
for u in sorted(outros,key=lambda u:-(gsc[u]["impressions"] if u in gsc else -1)): print(linha(u))
print("\n===== CIDADES INDEXAVEIS NO SITEMAP =====")
for u in sorted(cidades,key=lambda u:-(gsc[u]["impressions"] if u in gsc else -1)): print(linha(u))

fora=[u for u in gsc if u not in sitemap and gsc[u]["impressions"]>=5]
print("\n===== URLs COM IMPRESSAO QUE NAO ESTAO NO SITEMAP (>=5 imp) =====")
for u in sorted(fora,key=lambda u:-gsc[u]["impressions"]): print(linha(u))
