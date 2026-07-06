# ============================================================
# EXERCICIO 13 - "O GERADOR DE CODINOME"
# Base: Aula 13 (Strings: indexacao e fatiamento)
# ------------------------------------------------------------
# Contexto:
#   Uma string e uma fileira de caracteres numerados. Sabendo a
#   posicao de cada letra, voce recorta e remonta textos como quiser.
#
# Sua missao:
#   Pergunte o nome do usuario e gere:
#     - a PRIMEIRA letra (a inicial)
#     - a ULTIMA letra
#     - as 3 primeiras letras
#     - o nome escrito de TRAS PARA FRENTE
#
# Regras (validando a Aula 13):
#   - Use indices e fatiamento (colchetes []). Nada de metodos aqui.
#
# Desafio logico:
#   Junte a primeira letra + a ultima letra para formar um "codinome"
#   curto e imprima-o.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome = input("Digite seu nome >> ")

print("Inicial:", nome[0])
print("Ultima letra:", nome[-1])
print("Tres primeiras:", nome[0:3])
print("Ao contrario:", nome[::-1])

# Desafio: codinome com a primeira e a ultima letra
print("Codinome:", nome[0] + nome[-1])
