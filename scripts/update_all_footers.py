import os
import glob

old_bio = '<p class="footer-bio">Com base em Goiânia e atendimento online para clínicas e negócios locais em todo o Brasil.</p>'
new_bio = '<p class="footer-bio">Atendimento presencial em Goiânia, Aparecida de Goiânia e Anápolis. Consultoria estratégica online para clínicas e empresas locais em todo o Brasil.</p>'

count = 0
for filepath in glob.iglob('**/*.html', recursive=True):
    # skip node_modules etc if they exist
    if 'node_modules' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if old_bio in html:
        html = html.replace(old_bio, new_bio)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Atualizadas {count} páginas com a nova bio de rodapé.")
