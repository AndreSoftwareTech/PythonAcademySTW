# ============================================================
# MODULO 03 - AULA 02: ATRIBUTOS, METODOS E __str__
# ------------------------------------------------------------
# Objetivo: entender que a classe define ATRIBUTOS (dados) e
# METODOS (comportamentos). O metodo __str__ define como o
# objeto aparece quando usamos print(objeto).
# ============================================================

class Conta:
    titular: str
    numero: int
    saldo: float
    limite: float

    def extrato(self):
        print(f"Conta {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def __str__(self):
        return f"{self.titular} - {self.numero} - Saldo: R$ {self.saldo:.2f}"
