# -*- coding: utf-8 -*-
import re,os,sys,io,glob,collections
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
sm=set(re.findall(r"<loc>(.*?)</loc>",open("sitemap.xml",encoding="utf-8").read()))
smp=set(u.replace("https://rcbseo.com.br","") or "/" for u in sm)
paginas=[p for p in glob.glob("**/*.html",recursive=True)
         if not any(x in p for x in("node_modules","graphify-out","scripts/","Projetos/",".playwright"))]
def url(p):
    u="/"+p.replace("\\","/")
    return u.replace("/index.html","/") if u.endswith("index.html") else u
titles=collections.defaultdict(list); descs=collections.defaultdict(list)
noindex_no_sitemap=[]; sitemap_noindex=[]; sem_canonical=[]; canon_errado=[]; sem_desc=[]; sem_h1=[]
for p in paginas:
    h=open(p,encoding="utf-8",errors="ignore").read(); u=url(p)
    ni=bool(re.search(r'(?i)<meta[^>]+robots[^>]+noindex',h))
    if ni and u in smp: sitemap_noindex.append(u)
    if not ni and u not in smp: noindex_no_sitemap.append(u)
    c=re.search(r'(?i)<link[^>]+rel="canonical"[^>]+href="([^"]+)"',h)
    if not c: sem_canonical.append(u)
    elif c.group(1).replace("https://rcbseo.com.br","").rstrip() not in (u,u.rstrip("/")): canon_errado.append((u,c.group(1)))
    t=re.search(r"(?is)<title>(.*?)</title>",h); d=re.search(r'(?is)name="description"\s+content="(.*?)"',h)
    if t and not ni: titles[t.group(1).strip()].append(u)
    if d and not ni: descs[d.group(1).strip()].append(u)
    elif not d: sem_desc.append(u)
    if not re.search(r"(?i)<h1",h): sem_h1.append(u)
print(f"paginas analisadas: {len(paginas)} | sitemap: {len(smp)}")
print(f"\n[A] noindex MAS no sitemap (contradicao grave): {len(sitemap_noindex)}"); [print("   ",u) for u in sitemap_noindex[:15]]
print(f"\n[B] indexavel MAS fora do sitemap: {len(noindex_no_sitemap)}"); [print("   ",u) for u in noindex_no_sitemap[:20]]
print(f"\n[C] sem canonical: {len(sem_canonical)}"); [print("   ",u) for u in sem_canonical[:10]]
print(f"\n[D] canonical divergente: {len(canon_errado)}"); [print("   ",u,"->",c) for u,c in canon_errado[:10]]
print(f"\n[E] sem meta description: {len(sem_desc)}"); [print("   ",u) for u in sem_desc[:10]]
print(f"\n[F] sem H1: {len(sem_h1)}"); [print("   ",u) for u in sem_h1[:10]]
print("\n[G] TITLES DUPLICADOS (paginas indexaveis):")
for t,us in titles.items():
    if len(us)>1: print(f'   "{t[:70]}" -> {us}')
print("\n[H] DESCRIPTIONS DUPLICADAS (paginas indexaveis):")
n=0
for d,us in descs.items():
    if len(us)>1: print(f'   "{d[:70]}..." -> {len(us)} paginas: {us[:4]}'); n+=1
print(f"   total de grupos duplicados: {n}")
