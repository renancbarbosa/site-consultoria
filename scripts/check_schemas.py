import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check for FAQ schema
print("FAQPage schema in index:", "FAQPage" in html)
# Check for Anapolis in text
print("Anápolis in index text:", "Anápolis" in html)

with open("seo-local-goiania/index.html", "r", encoding="utf-8") as f:
    html2 = f.read()

print("FAQPage schema in seo-local-goiania:", "FAQPage" in html2)
print("Anápolis in seo-local-goiania text:", "Anápolis" in html2)
