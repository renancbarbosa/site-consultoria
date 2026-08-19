# -*- coding: utf-8 -*-
import json, os, sys, io, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D="data/audit"
def load(n):
    return json.load(open(os.path.join(D,n),encoding="utf-8")).get("rows",[]) or []
def s(u): return u.replace("https://rcbseo.com.br","") or "/"
def norm(t):
    return "".join(c for c in unicodedata.normalize("NFD",t.lower()) if unicodedata.category(c)!="Mn")

for per,f in [("90d","raw_90d_query_page.json"),("28d","raw_28d_query_page.json")]:
    rows=load(f)
    print(f"\n########## {per} — queries com 'goian'/'goias' ##########")
    for r in sorted([x for x in rows if "goian" in norm(x["keys"][0]) or "goias" in norm(x["keys"][0])],key=lambda r:-r["impressions"]):
        print(f'  pos {r["position"]:5.1f} {r["impressions"]:4d} imp {r["clicks"]:2d} cl | "{r["keys"][0]}" -> {s(r["keys"][1])}')
    print(f"\n########## {per} — todas as queries das paginas de Goiania / consultor ##########")
    alvo=["/consultor-seo-goiania/","/seo-local-goiania/","/consultoria-seo-local/"]
    for r in sorted([x for x in rows if s(x["keys"][1]) in alvo],key=lambda r:-r["impressions"]):
        print(f'  {s(r["keys"][1]):26s} pos {r["position"]:5.1f} {r["impressions"]:4d} imp {r["clicks"]:2d} cl | "{r["keys"][0]}"')
