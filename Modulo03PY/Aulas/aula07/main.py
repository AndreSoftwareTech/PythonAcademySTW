# ============================================================
# MODULO 03 - AULA 07: MAIN (@property em acao)
# CORRECAO: prompt incompleto da versao antiga ("Digite seu :> ").
# ============================================================

from conta import Conta

conta = Conta(
    input("Titular >> "),
    input("Numero da conta >> "),
    input("Saldo inicial >> "),
    input("Limite >> "),
)

print(conta)

# Parece atributo publico, mas passa pelo @property por baixo:
conta.limite = 3500.0
print("Novo limite:", conta.limite)
