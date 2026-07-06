# ============================================================
# EXERCICIO 11 - "MOTOR NOVO, MESMO CARRO"
# Base: Aula 11 (Composicao: Carro TEM UM Motor, nao HERDA)
# ------------------------------------------------------------
# Contexto:
#   Heranca e "e um" (Carro E UM Veiculo). Composicao e "tem um"
#   (Carro TEM UM Motor). Trocar o motor nao exige herdar de Motor —
#   basta substituir o objeto dentro do carro.
#
# Sua missao:
#   1) Classe Motor com potencia (cv) e metodo ligar() que retorna
#      uma mensagem tipo "Motor Xcv ligado!".
#   2) Classe Carro com modelo e um atributo motor (instancia de Motor).
#   3) Carro.ligar() delega ao motor e imprime modelo + mensagem.
#   4) Troque o motor do carro por outro mais potente e ligue de novo.
#
# Regras (validando a Aula 11):
#   - Carro NAO deve herdar de Motor; use composicao (self.motor = ...).
#   - Demonstre ligar antes e depois da troca de motor.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return f"Motor {self.potencia}cv ligado!"


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def ligar(self):
        print(f"{self.modelo}: {self.motor.ligar()}")


carro = Carro("Fusca", 65)
carro.ligar()

carro.motor = Motor(80)
carro.ligar()
