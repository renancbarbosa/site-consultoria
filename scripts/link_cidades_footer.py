import os
import glob

old_bio = '<p class="footer-bio">Atendimento presencial em Goiânia, Aparecida de Goiânia e Anápolis. Consultoria estratégica online para clínicas e empresas locais em todo o Brasil.</p>'
new_bio = '<p class="footer-bio">Atendimento presencial em <a href="/seo-local-goiania/">Goiânia</a>, <a href="/consultoria-seo/aparecida-de-goiania/">Aparecida de Goiânia</a> e <a href="/consultoria-seo/anapolis/">Anápolis</a>. Consultoria estratégica online para clínicas e empresas locais em todo o Brasil.</p>'

count = 0
for filepath in glob.iglob('**/*.html', recursive=True):
    if 'node_modules' in filepath: continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if old_bio in html:
        html = html.replace(old_bio, new_bio)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Footer atualizado com links em {count} páginas.")
