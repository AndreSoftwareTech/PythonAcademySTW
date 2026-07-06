# ============================================================
# MODULO 03 - AULA 01: MAIN (instanciando a classe Conta)
# ------------------------------------------------------------
# Objetivo: importar a classe e criar um OBJETO a partir dela.
# Cada objeto e uma instancia independente da classe.
# ============================================================

from conta import Conta

conta = Conta(
    input("Numero da conta >> "),
    input("Titular >> "),
    input("CPF >> "),
    input("Saldo inicial >> "),
    input("Limite >> "),
)

print("Dados da conta:")
print(conta.titular, conta.numero, conta.saldo)
