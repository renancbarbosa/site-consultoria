import glob
import re

fixes = {
    'Goiǽnia': 'Goiânia',
    'Anǭpolis': 'Anápolis',
    'nǜo': 'não',
    'conteǧdo': 'conteúdo',
    'Diagnstico': 'Diagnóstico',
    'Aparea': 'Apareça',
    'Negcio': 'Negócio',
    'vocꞀ': 'você',
    'sǜo': 'são',
    'atravꞀs': 'através',
    'AlꞀm': 'Além',
    'VocꞀ': 'Você',
    'Nǜo': 'Não',
    'regiǜo': 'região',
    'estratega': 'estratégia',
    'Sǜo Paulo': 'São Paulo',
    'Vitria': 'Vitória',
    'Braslia': 'Brasília',
    'Maringǭ': 'Maringá',
    'Cuiabǭ': 'Cuiabá',
    'Macei': 'Maceió',
    'Sǜo Lus': 'São Luís',
    'BelꞀm': 'Belém',
    'Goiǭs': 'Goiás',
    'Paranǭ': 'Paraná',
    'Cearǭ': 'Ceará',
    'Joǜo Pessoa': 'João Pessoa',
    'Florianpolis': 'Florianópolis',
    'Sǜo Bernardo do Campo': 'São Bernardo do Campo',
    'Ribeirǜo Preto': 'Ribeirão Preto',
    'Uberlndia': 'Uberlândia',
    'MacaꞀ': 'Macaé',
    'Sǜo JosꞀ': 'São José',
    'Balneǭrio Camboriǧ': 'Balneário Camboriú',
    '': 'á',  # fallback for some unknown chars if needed, but let's stick to explicit
}

count = 0
for filepath in glob.iglob('consultoria-seo/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    changed = False
    for bad, good in fixes.items():
        if bad in html:
            html = html.replace(bad, good)
            changed = True
            
    # More robust fix for generic mojibake if possible? We'll see.
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f"Corrigidos caracteres estranhos em {count} páginas de cidades.")
