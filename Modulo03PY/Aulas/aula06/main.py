# ============================================================
# MODULO 03 - AULA 06: MAIN (acesso controlado)
# ============================================================

from conta import Conta

conta = Conta("Carlos", 2001, 800.0, 300.0)
print(conta)

# Acesso via getters (nao conseguimos ler __saldo direto de fora)
print("Titular:", conta.get_titular())
print("Saldo:", conta.get_saldo())

conta.set_saldo(950.0)
conta.set_saldo(-100)   # tentativa invalida
print("Saldo apos ajuste:", conta.get_saldo())
