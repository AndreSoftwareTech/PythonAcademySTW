# ============================================================
# MODULO 03 - AULA 13: CRUD OOP COM JSON
# ------------------------------------------------------------
# Objetivo: juntar OOP + persistencia. A classe Cliente e o MODEL;
# o controller grava/lê JSON (seguro, sem eval()).
#
# CORRECAO da versao antiga: controller usava dict com chaves
# 'Nome'/'Idade' mas main passava objeto Cliente -> TypeError.
# Agora usamos cliente.to_dict() / Cliente.from_dict().
# ============================================================

class Cliente:
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def to_dict(self):
        return {
            "titular": self.__titular,
            "numero": self.__numero,
            "saldo": self.__saldo,
            "limite": self.__limite,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["titular"], dados["numero"], dados["saldo"], dados["limite"])

    def __str__(self):
        return f"{self.titular} | Conta {self.numero} | R$ {self.saldo:.2f}"
