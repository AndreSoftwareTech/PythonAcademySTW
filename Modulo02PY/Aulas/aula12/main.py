# ============================================================
# MODULO 02 - AULA 12: main.py
# ------------------------------------------------------------
# Salva um nome no arquivo e depois le tudo o que ja foi salvo.
# Rode varias vezes: os nomes das execucoes anteriores continuam la!
# ============================================================

from controller import create, read

nome = input("Digite um nome para salvar >> ")
create(nome)

print("Nomes salvos no arquivo:", read())
