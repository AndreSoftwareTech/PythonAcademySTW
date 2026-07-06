# ============================================================
# AULA 29 - ALEATORIEDADE: NUMEROS COM randint
# Objetivo: sortear numeros inteiros aleatorios.
# ============================================================

from random import randint

# randint(a, b) sorteia um inteiro entre a e b (INCLUINDO os dois extremos)
dado = randint(1, 6)
print("Voce tirou no dado:", dado)

sorteio = randint(0, 100)
print("Numero sorteado de 0 a 100:", sorteio)
