import re

def aggressive_replace(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Hero Badge
    html = html.replace('Goiânia presencial • Brasil inteiro online', 'Atendimento Presencial: Goiânia, Aparecida e Anápolis • Brasil Online')

    # 2. Schema description
    html = html.replace('Atendimento presencial em Goiânia e online em todo o Brasil.', 'Atendimento presencial no eixo Goiânia, Aparecida e Anápolis, e consultoria online em todo o Brasil.')

    # 3. FAQ
    html = html.replace('Você atende fora de Goiânia?', 'Você atende fora de Goiânia, Aparecida e Anápolis?')
    html = html.replace('Em Goiânia e região eu atendo presencialmente.', 'No eixo Goiânia, Aparecida de Goiânia e Anápolis eu realizo reuniões e atendimento presencial.')
    html = html.replace('em Goiânia e região metropolitana', 'em Goiânia, Aparecida, Anápolis e região metropolitana')
    html = html.replace('da região (Goiânia e cidades vizinhas)', 'do eixo central de Goiás (Goiânia, Aparecida de Goiânia e Anápolis)')

    # 4. Add Anápolis to areaServed in Schema if not present
    if '"name": "Aparecida de Goiânia"' in html and '"name": "Anápolis"' not in html:
        anapolis_schema = '''        {
          "@type": "City",
          "name": "Anápolis",
          "containedInPlace": {
            "@type": "State",
            "name": "Goiás"
          }
        },
'''
        html = html.replace('        {\n          "@type": "City",\n          "name": "Aparecida de Goiânia"', anapolis_schema + '        {\n          "@type": "City",\n          "name": "Aparecida de Goiânia"')

    # 5. Entity injection in footers / descriptions
    html = html.replace('Atendemos todo o Brasil.', 'Atendemos presencialmente em Goiânia, Aparecida de Goiânia e Anápolis. Consultoria avançada online para todo o Brasil.')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Modificado: {file_path}")

aggressive_replace("index.html")
aggressive_replace("seo-local-goiania/index.html")
