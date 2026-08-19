# -*- coding: utf-8 -*-
"""Le os JSON brutos do Search Console em data/audit/ e gera as matrizes da auditoria."""
import json, csv, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = "data/audit"

def load(name):
    with open(os.path.join(D, name), encoding="utf-8") as f:
        return json.load(f).get("rows", []) or []

def short(u):
    return u.replace("https://rcbseo.com.br", "") or "/"

def totals(rows):
    c = sum(r["clicks"] for r in rows); i = sum(r["impressions"] for r in rows)
    pos = (sum(r["position"] * r["impressions"] for r in rows) / i) if i else 0
    return c, i, pos

for label, fn in [("90d", "raw_90d_page.json"), ("28d", "raw_28d_page.json"), ("prev28", "raw_prev28_page.json")]:
    rows = load(fn); c, i, p = totals(rows)
    print(f"{label}: clicks={c} impr={i} pos_media_ponderada={p:.1f} urls={len(rows)}")

qp = load("raw_90d_query_page.json")
qp.sort(key=lambda r: (-r["impressions"], -r["clicks"]))
with open(os.path.join(D, "query_url_matrix.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["query", "url", "clicks", "impressions", "ctr_%", "position"])
    for r in qp:
        w.writerow([r["keys"][0], short(r["keys"][1]), r["clicks"], r["impressions"],
                    round(r["ctr"] * 100, 1), round(r["position"], 1)])

best = {}
for r in qp:
    u = short(r["keys"][1])
    if u not in best or r["impressions"] > best[u]["impressions"]:
        best[u] = {"q": r["keys"][0], "impressions": r["impressions"], "position": r["position"]}
pages = load("raw_90d_page.json"); pages.sort(key=lambda r: -r["impressions"])
with open(os.path.join(D, "url_baseline_90d.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["url", "clicks", "impressions", "ctr_%", "position", "melhor_query", "impr_dessa_query", "pos_dessa_query"])
    for r in pages:
        u = short(r["keys"][0]); b = best.get(u, {})
        w.writerow([u, r["clicks"], r["impressions"], round(r["ctr"] * 100, 1), round(r["position"], 1),
                    b.get("q", ""), b.get("impressions", ""), round(b["position"], 1) if b else ""])

print("\n=== TOP 30 URLs por impressao (90d) ===")
for r in pages[:30]:
    print(f'{r["impressions"]:6d} imp {r["clicks"]:3d} cl pos {r["position"]:5.1f}  {short(r["keys"][0])}')

print("\n=== TOP 40 QUERIES por impressao (90d) ===")
qs = load("raw_90d_query.json"); qs.sort(key=lambda r: -r["impressions"])
for r in qs[:40]:
    print(f'{r["impressions"]:6d} imp {r["clicks"]:3d} cl pos {r["position"]:5.1f}  {r["keys"][0]}')

print("\n=== QUERIES pos <= 20 (90d) ===")
for r in sorted([x for x in qs if x["position"] <= 20], key=lambda r: r["position"]):
    print(f'pos {r["position"]:5.1f} {r["impressions"]:5d} imp {r["clicks"]:3d} cl  {r["keys"][0]}')

byq = {}
for r in qp:
    byq.setdefault(r["keys"][0], []).append(r)
print("\n=== CANIBALIZACAO (query com mais de 1 URL, 90d) ===")
for q, rs in sorted(byq.items(), key=lambda kv: -sum(x["impressions"] for x in kv[1])):
    if len(rs) > 1:
        print(f'"{q}" ({sum(x["impressions"] for x in rs)} imp)')
        for x in sorted(rs, key=lambda r: r["position"]):
            print(f'    pos {x["position"]:5.1f} {x["impressions"]:4d} imp {x["clicks"]:2d} cl  {short(x["keys"][1])}')
