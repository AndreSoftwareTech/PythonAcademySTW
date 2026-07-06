# ============================================================
# MODULO 03 - AULA 02: MAIN (objeto vazio + atributos externos)
# ------------------------------------------------------------
# Objetivo: mostrar que podemos criar um objeto e preencher os
# atributos depois, sem usar __init__. Tambem vemos __str__ em acao.
# ============================================================

from conta import Conta

conta = Conta()
conta.titular = input("Titular >> ")
conta.numero = int(input("Numero >> "))
conta.saldo = float(input("Saldo >> "))
conta.limite = float(input("Limite >> "))

print(conta)          # chama __str__ automaticamente
conta.extrato()       # chama um metodo da instancia
