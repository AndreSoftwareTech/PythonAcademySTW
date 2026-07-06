# ============================================================
# MODULO 03 - AULA 11: COMPOSICAO VS HERANCA [NOVO]
# ------------------------------------------------------------
# Objetivo: heranca e "e um" (Carro E UM Veiculo). Composicao e
# "tem um" (Carro TEM UM Motor). Composicao costuma ser mais flexivel
# que herdar demais.
# ============================================================

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor {self.potencia}cv ligado!"

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)   # COMPOSICAO: Carro TEM UM Motor

    def ligar(self):
        print(f"{self.modelo}: {self.motor.ligar()}")

carro = Carro("Fusca", 65)
carro.ligar()

# Se Motor quebrar, trocamos o motor sem herdar de Motor:
carro.motor = Motor(80)
carro.ligar()
