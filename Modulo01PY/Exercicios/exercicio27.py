# ============================================================
# EXERCICIO 27 - "O SORTEIO DO AMIGO SECRETO"
# Base: Aula 27 (Aleatoriedade: random.choice)
# ------------------------------------------------------------
# Contexto:
#   Deixar o computador escolher por nos e util e divertido. O
#   choice() pesca um item aleatorio de dentro de uma lista.
#
# Sua missao:
#   Pergunte 4 nomes de participantes, coloque-os em uma lista e
#   sorteie UM deles para ser o "organizador oficial" da festa.
#
# Regras (validando a Aula 27):
#   - Importe e use choice() do modulo random.
# ============================================================

# --- GABARITO DO PROFESSOR ---
from random import choice

nome1 = input("Participante 1 >> ")
nome2 = input("Participante 2 >> ")
nome3 = input("Participante 3 >> ")
nome4 = input("Participante 4 >> ")

participantes = [nome1, nome2, nome3, nome4]
organizador = choice(participantes)

print(f"O organizador oficial sorteado foi: {organizador}")
