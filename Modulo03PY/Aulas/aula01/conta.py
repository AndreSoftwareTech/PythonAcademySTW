# ============================================================
# MODULO 03 - AULA 01: CLASSES, SELF E __init__
# ------------------------------------------------------------
# Objetivo: criar a primeira CLASSE (molde) e instanciar OBJETOS.
# A palavra 'class' define o molde; __init__ e o "construtor"
# que roda automaticamente ao criar o objeto; 'self' e a referencia
# ao proprio objeto dentro da classe.
#
# CORRECAO da versao antiga: os parametros do __init__ DEVEM ser
# atribuidos a self (ex.: self.numero = numero). So anotar o tipo
# (self.numero : int) NAO guarda o valor!
# ============================================================

class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        print(f"Criando conta para {titular} (objeto: {self})")
        self.numero = int(numero)
        self.titular = titular
        self.cpf = cpf
        self.saldo = float(saldo)
        self.limite = float(limite)
