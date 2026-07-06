# ============================================================
# MODULO 03 - AULA 06: ENCAPSULAMENTO (GETTERS E SETTERS)
# ------------------------------------------------------------
# Objetivo: esconder atributos com __ (dois underscores) para
# que nao sejam acessados diretamente de fora. Getters e setters
# controlam COMO os dados sao lidos e alterados.
# ============================================================

class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = int(numero)
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        if titular.strip():
            self.__titular = titular
        else:
            print("Titular nao pode ser vazio.")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = float(saldo)
        else:
            print("Saldo nao pode ser negativo.")

    def get_limite(self):
        return self.__limite

    def __str__(self):
        return f"{self.__titular} | Conta {self.__numero} | R$ {self.__saldo:.2f}"
