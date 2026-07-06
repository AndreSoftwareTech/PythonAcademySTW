# ============================================================
# MODULO 03 - AULA 05: METODOS DE INSTANCIA (CONTA BANCARIA)
# ------------------------------------------------------------
# Objetivo: metodos sao funcoes DENTRO da classe que operam
# sobre os dados do objeto (self). Aqui simulamos deposito,
# saque, extrato e transferencia entre contas.
# ============================================================

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = int(numero)
        self.saldo = float(saldo)
        self.limite = float(limite)

    def extrato(self):
        print(f"Conta {self.numero} | {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de deposito invalido.")
            return
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque invalido.")
            return
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente (mesmo com limite).")

    def transferir(self, valor, destino):
        if self.saldo >= valor:
            self.sacar(valor)
            destino.depositar(valor)
            print(f"Transferencia de R$ {valor:.2f} para conta {destino.numero}.")
        else:
            print("Transferencia negada: saldo insuficiente.")

    def __str__(self):
        return f"{self.titular} - Conta {self.numero} - R$ {self.saldo:.2f}"
