# ============================================================
# MODULO 03 - AULA 07: ENCAPSULAMENTO COM @property
# ------------------------------------------------------------
# Objetivo: @property e a forma PYTHONICA de encapsular. Permite
# usar conta.saldo como se fosse atributo publico, mas por baixo
# passa pelo getter/setter que voce definiu.
# ============================================================

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = int(numero)
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if valor.strip():
            self.__titular = valor

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = float(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor >= 0:
            self.__limite = float(valor)

    def __str__(self):
        return f"{self.titular} | {self.numero} | R$ {self.saldo:.2f} | Limite R$ {self.limite:.2f}"
