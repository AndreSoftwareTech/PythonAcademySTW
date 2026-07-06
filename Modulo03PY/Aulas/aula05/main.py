# ============================================================
# MODULO 03 - AULA 05: MAIN (operacoes bancarias)
# ============================================================

from conta import Conta

conta1 = Conta("Andre", 1001, 1000.0, 500.0)
conta2 = Conta("Maria", 1002, 500.0, 200.0)

conta1.extrato()
conta1.depositar(200)
conta1.sacar(150)
conta1.transferir(300, conta2)

print("--- Apos operacoes ---")
conta1.extrato()
conta2.extrato()
