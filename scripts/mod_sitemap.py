# -*- coding: utf-8 -*-
with open("scripts/atualizar-sitemap.py", "r", encoding="utf-8") as f:
    code = f.read()

# Add to ATUALIZADAS set if not already there
if '"/consultoria-seo/anapolis/"' not in code:
    code = code.replace(
        '    "/blog/",',
        '    "/blog/",\n    "/consultoria-seo/anapolis/",\n    "/consultoria-seo/aparecida-de-goiania/",'
    )

with open("scripts/atualizar-sitemap.py", "w", encoding="utf-8") as f:
    f.write(code)

print("atualizar-sitemap.py modificado!")
