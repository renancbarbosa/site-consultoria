import re

with open("scripts/rcb_base.py", "r", encoding="utf-8") as f:
    code = f.read()

# Update footer bio
old_bio = '<p class="footer-bio">Com base em Goiânia e atendimento online para clínicas e negócios locais em todo o Brasil.</p>'
new_bio = '<p class="footer-bio">Atendimento presencial em Goiânia, Aparecida de Goiânia e Anápolis. Consultoria estratégica online para clínicas e empresas locais em todo o Brasil.</p>'
code = code.replace(old_bio, new_bio)

with open("scripts/rcb_base.py", "w", encoding="utf-8") as f:
    f.write(code)

print("rcb_base.py atualizado.")
