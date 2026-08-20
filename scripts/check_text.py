import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

matches = re.finditer(r'.{0,50}Goiânia.{0,50}', html)
for i, m in enumerate(matches):
    if i < 15:
        print(m.group(0).strip())

