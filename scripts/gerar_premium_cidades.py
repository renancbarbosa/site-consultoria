# -*- coding: utf-8 -*-
import os
import shutil

base_html_path = "seo-local-goiania/index.html"
with open(base_html_path, "r", encoding="utf-8") as f:
    base_html = f.read()

def criar_pagina_cidade(slug, nome_cidade, polo_local, canonical_path):
    html = base_html
    
    # 1. Update URLs and Canonical
    html = html.replace('href="https://rcbseo.com.br/seo-local-goiania/"', f'href="https://rcbseo.com.br/{canonical_path}"')
    html = html.replace('"url": "https://rcbseo.com.br/seo-local-goiania/"', f'"url": "https://rcbseo.com.br/{canonical_path}"')
    html = html.replace('@id": "https://rcbseo.com.br/seo-local-goiania/#webpage"', f'@id": "https://rcbseo.com.br/{canonical_path}#webpage"')
    
    # 2. Update Titles and Meta
    html = html.replace('SEO Local em Goiânia | Apareça no Google e no Maps', f'SEO Local em {nome_cidade} | Apareça no Google e no Maps')
    html = html.replace('SEO local em Goiânia: sua clínica', f'SEO local em {nome_cidade}: sua clínica')
    
    # 3. Headers and Hero
    html = html.replace('<h1>Apareça para os clientes de <strong>Goiânia</strong> no momento exato em que eles buscam seu serviço</h1>', f'<h1>Apareça para os clientes de <strong>{nome_cidade}</strong> no momento exato em que eles buscam seu serviço</h1>')
    html = html.replace('especializada em negócios locais de Goiânia', f'especializada em negócios locais de {nome_cidade} e região ({polo_local})')
    
    # 4. Text modifications
    html = html.replace('você e seus concorrentes em Goiânia', f'você e seus concorrentes em {nome_cidade}')
    html = html.replace('Clínicas e negócios locais de Goiânia', f'Clínicas e negócios locais de {nome_cidade}')
    
    # Save
    out_dir = f"consultoria-seo/{slug}"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Página premium criada para {nome_cidade}")

criar_pagina_cidade("aparecida-de-goiania", "Aparecida de Goiânia", "próximo ao Polo Empresarial", "consultoria-seo/aparecida-de-goiania/")
criar_pagina_cidade("anapolis", "Anápolis", "próximo ao DAIA e Centro", "consultoria-seo/anapolis/")

