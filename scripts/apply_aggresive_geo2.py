import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace hero badge
html = re.sub(r'Goiânia presencial.*?Brasil inteiro online', 'Atendimento Presencial: Goiânia, Aparecida e Anápolis | Brasil Online', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("seo-local-goiania/index.html", "r", encoding="utf-8") as f:
    html2 = f.read()

html2 = re.sub(r'Goiânia presencial.*?Brasil inteiro online', 'Atendimento Presencial: Goiânia, Aparecida e Anápolis | Brasil Online', html2)

with open("seo-local-goiania/index.html", "w", encoding="utf-8") as f:
    f.write(html2)

print("Hero badges e textos atualizados!")
