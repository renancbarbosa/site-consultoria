import re

def linkar_cidades(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Link no hero
    html = html.replace(
        'Atendimento Presencial: Goiânia, Aparecida e Anápolis',
        'Atendimento Presencial: <a href="/seo-local-goiania/" style="color:inherit;text-decoration:underline;">Goiânia</a>, <a href="/consultoria-seo/aparecida-de-goiania/" style="color:inherit;text-decoration:underline;">Aparecida</a> e <a href="/consultoria-seo/anapolis/" style="color:inherit;text-decoration:underline;">Anápolis</a>'
    )
    
    # Link no Footer bio (que atualizamos em 233 páginas)
    # Actually, modifying 233 pages again is easy.
    pass

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace('Goiânia, Aparecida e Anápolis |', '<a href="/seo-local-goiania/" style="color:inherit;text-decoration:underline;">Goiânia</a>, <a href="/consultoria-seo/aparecida-de-goiania/" style="color:inherit;text-decoration:underline;">Aparecida</a> e <a href="/consultoria-seo/anapolis/" style="color:inherit;text-decoration:underline;">Anápolis</a> |')
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("seo-local-goiania/index.html", "r", encoding="utf-8") as f:
    html2 = f.read()
html2 = html2.replace('Goiânia, Aparecida e Anápolis |', '<a href="/seo-local-goiania/" style="color:inherit;text-decoration:underline;">Goiânia</a>, <a href="/consultoria-seo/aparecida-de-goiania/" style="color:inherit;text-decoration:underline;">Aparecida</a> e <a href="/consultoria-seo/anapolis/" style="color:inherit;text-decoration:underline;">Anápolis</a> |')
with open("seo-local-goiania/index.html", "w", encoding="utf-8") as f:
    f.write(html2)

print("Links adicionados no hero!")
