# ============================================================
# MODULO 03 - AULA 03: CONSTRUTOR COMPLETO
# ------------------------------------------------------------
# Objetivo: usar __init__ para OBRIGAR que todo objeto nasca
# ja com todos os dados preenchidos. Forma mais segura e profissional.
# ============================================================

class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        self.numero = int(numero)
        self.titular = titular
        self.cpf = cpf
        self.saldo = float(saldo)
        self.limite = float(limite)

    def __str__(self):
        return f"{self.titular} | Conta {self.numero} | CPF {self.cpf} | Saldo R$ {self.saldo:.2f}"
