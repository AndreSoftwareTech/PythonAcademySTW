# ============================================================
# EXERCICIO 11 - "A MOLDURA ASCII"
# Base: Aula 11 (Operador de repeticao em strings)
# ------------------------------------------------------------
# Contexto:
#   Antes das interfaces graficas, tudo era desenhado com texto.
#   Multiplicar uma string por um numero e um truque poderoso para
#   criar linhas, molduras e barras de separacao.
#
# Sua missao:
#   Pergunte uma palavra ao usuario e exiba-a "emoldurada", assim:
#
#       ##############
#       #  PYTHON  #
#       ##############
#
#   As linhas de cima e de baixo devem ser feitas com repeticao de
#   caractere (nada de digitar varios # na mao).
#
# Regras (validando a Aula 11):
#   - Use o operador * para construir as bordas.
# ============================================================

# --- GABARITO DO PROFESSOR ---
palavra = input("Digite uma palavra >> ")

borda = "#" * (len(palavra) + 6)
print(borda)
print("#  " + palavra + "  #")
print(borda)
