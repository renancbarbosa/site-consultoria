# -*- coding: utf-8 -*-
"""Desfaz a corrupcao de encoding introduzida no commit 9bfb637 (20/08/2026).

Sintoma: cada caractere do arquivo ficou precedido por U+00E1 ("a" com acento).
O comeco do arquivo virou "a<a!aDaOaCaTaYaPaE" em vez de "<!DOCTYPE".
O texto verdadeiro esta intacto nos caracteres de indice impar.

Seguranca: so mexe no arquivo se TODOS os caracteres de indice par forem U+00E1
E o resultado comecar com "<!DOCTYPE". Qualquer arquivo fora desse padrao e
deixado como esta e listado no fim.

Uso: python scripts/corrigir-encoding-cidades.py [--aplicar]
Sem --aplicar, so relata (modo seguro).
"""
import io
import os
import sys

MARCA = u"á"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    aplicar = "--aplicar" in sys.argv
    corrigidos, intactos, suspeitos = [], [], []

    for root, _dirs, files in os.walk(RAIZ):
        if ".git" in root or "node_modules" in root:
            continue
        for nome in files:
            if not nome.endswith(".html"):
                continue
            caminho = os.path.join(root, nome)
            texto = io.open(caminho, encoding="utf-8", errors="replace").read()
            pares = set(texto[0::2])
            if pares != {MARCA}:
                if MARCA * 2 in texto[:40]:
                    suspeitos.append(caminho)
                else:
                    intactos.append(caminho)
                continue
            recuperado = texto[1::2]
            if not recuperado.startswith("<!DOCTYPE"):
                suspeitos.append(caminho)
                continue
            if aplicar:
                io.open(caminho, "w", encoding="utf-8", newline="").write(recuperado)
            corrigidos.append(caminho)

    rel = os.path.relpath
    print("arquivos corrigidos:" if aplicar else "arquivos a corrigir:", len(corrigidos))
    for c in corrigidos[:5]:
        print("   ", rel(c, RAIZ))
    if len(corrigidos) > 5:
        print("    ... e mais", len(corrigidos) - 5)
    print("arquivos ja intactos:", len(intactos))
    if suspeitos:
        print("ATENCAO - fora do padrao, nao tocados:", len(suspeitos))
        for s in suspeitos:
            print("   ", rel(s, RAIZ))
    if not aplicar:
        print("\n(modo relatorio - rode com --aplicar para gravar)")


if __name__ == "__main__":
    main()
