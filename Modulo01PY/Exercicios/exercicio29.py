# ============================================================
# EXERCICIO 29 - "A MESA DE RPG"
# Base: Aula 29 (Aleatoriedade: randint)
# ------------------------------------------------------------
# Contexto:
#   Todo bom jogo precisa de dados. O randint() sorteia numeros
#   inteiros dentro de um intervalo, perfeito para simular dados.
#
# Sua missao:
#   Simule a rolagem de DOIS dados de 6 lados. Mostre o valor de
#   cada dado e a SOMA dos dois.
#
# Regras (validando a Aula 29):
#   - Use randint(1, 6) para cada dado.
#
# Desafio logico:
#   Se os dois dados derem o MESMO valor, imprima "DOBROU!".
# ============================================================

# --- GABARITO DO PROFESSOR ---
from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)

print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Soma:", dado1 + dado2)

# Desafio: dados iguais
if dado1 == dado2:
    print("DOBROU!")
