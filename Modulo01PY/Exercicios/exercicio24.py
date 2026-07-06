# ============================================================
# EXERCICIO 24 - "O CACADOR DE PARES"
# Base: Aula 24 (Par ou impar com resto da divisao)
# ------------------------------------------------------------
# Contexto:
#   O resto da divisao (%) e uma ferramenta magica: divida por 2 e,
#   se sobrar 0, o numero e par. Esse truque aparece o tempo todo em
#   logica de programacao.
#
# Sua missao:
#   Pergunte um numero e diga se ele e PAR ou IMPAR.
#
# Regras (validando a Aula 24):
#   - Use o operador % (resto da divisao).
#
# Desafio logico:
#   Alem de par/impar, avise TAMBEM se o numero e multiplo de 5
#   (dica: resto da divisao por 5 igual a zero).
# ============================================================

# --- GABARITO DO PROFESSOR ---
numero = int(input("Digite um numero >> "))

if numero % 2 == 0:
    print("O numero e PAR")
else:
    print("O numero e IMPAR")

# Desafio: multiplo de 5?
if numero % 5 == 0:
    print("E tambem e multiplo de 5!")
