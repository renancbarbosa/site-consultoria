# scripts/deprecated — scripts aposentados

Os arquivos desta pasta **não devem ser executados**. Eles não foram apagados
porque guardam trabalho aproveitável, mas rodá-los hoje quebra o site no ar.

Nada aqui é importado por outro script. Pasta sem `__init__.py` de propósito.

---

## `atualizar-nav-rodape.py` — aposentado em 11/08/2026

**O que fazia:** espalhava o menu (`rcb_base.NAV_MENU`) e a coluna de rodapé
"SEO Nacional" (`rcb_base.FOOTER_COL_NACIONAL`) para as ~305 páginas HTML do
site. Servia como "fonte única" do menu num site que é HTML estático escrito à
mão.

**Por que não pode mais rodar:** a divisão "SEO Nacional / mercados
competitivos" foi **revertida em 08/08/2026** (commit `122735d`) — as 73 URLs
dela respondem 404 de propósito. Mas o `rcb_base.py` foi preservado com o menu
antigo intacto:

- `rcb_base.py:172` — dropdown "SEO Nacional", com links que hoje são 404;
- `rcb_base.py:191` — botão "Diagnóstico gratuito", substituído por
  "Ver preços" na rodada de conversão de 09/08/2026.

Rodar o script hoje reescreveria o menu das 305 páginas com links quebrados e
desfaria o botão "Ver preços" do site inteiro. O código não tem nenhuma trava
que impeça isso.

**Se um dia a divisão voltar:** republique a divisão primeiro
(`git revert 122735d` ou `git merge divisao-seo-nacional`), confira que as URLs
respondem HTTP 200, **corrija `rcb_base.py:191` para "Ver preços"** e só então
traga o script de volta para `scripts/`.

**O que usar no lugar, hoje:** não há substituto — e não precisa haver. O menu
atual está correto nas 305 páginas e ninguém o altera em massa desde 09/08/2026.
Se um dia for preciso mudar o menu do site inteiro de novo, escreva um script
novo a partir do menu **que está no ar**, não do `rcb_base.py`.

---

## Nota sobre o `scripts/indexnow.py` (esse **não** foi aposentado)

A auditoria de 11/08/2026 pediu para aposentar o `indexnow.py` junto. **Decisão
do Renan: não.** Só o modo `--novas` era perigoso — ele montava a lista
importando os módulos da divisão revertida e mandaria ~73 URLs 404 para o Bing.
Esse modo foi **removido do código**. Os modos `--sitemap` e "URLs avulsas"
continuam em `scripts/indexnow.py`, porque são usados no fim de toda publicação.
