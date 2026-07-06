# ============================================================
# EXERCICIO 19 - "O JUIZ DAS COMPARACOES"
# Base: Aula 19 (Operadores relacionais)
# ------------------------------------------------------------
# Contexto:
#   Antes de tomar decisoes, o computador precisa COMPARAR valores.
#   O resultado de uma comparacao e sempre um booleano: True ou False.
#
# Sua missao:
#   Peca dois numeros ao usuario e mostre o resultado (True/False) de
#   todas as comparacoes possiveis entre eles:
#     igual, diferente, maior, menor, maior ou igual, menor ou igual.
#
# Regras (validando a Aula 19):
#   - Use os operadores ==, !=, >, <, >= e <=.
# ============================================================

# --- GABARITO DO PROFESSOR ---
a = int(input("Primeiro numero >> "))
b = int(input("Segundo numero >> "))

print("Sao iguais?", a == b)
print("Sao diferentes?", a != b)
print("A e maior que B?", a > b)
print("A e menor que B?", a < b)
print("A e maior ou igual a B?", a >= b)
print("A e menor ou igual a B?", a <= b)
