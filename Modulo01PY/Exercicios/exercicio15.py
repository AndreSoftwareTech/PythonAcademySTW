# ============================================================
# EXERCICIO 15 - "A CALCULADORA COMPLETA"
# Base: Aula 15 (Operadores matematicos)
# ------------------------------------------------------------
# Contexto:
#   Toda linguagem comeca a ficar util quando faz contas. O Python
#   tem operadores para tudo: soma, subtracao, potencia, divisao
#   inteira e ate o resto da divisao.
#
# Sua missao:
#   Peca dois numeros inteiros ao usuario e mostre o resultado de
#   TODAS as operacoes entre eles:
#     soma, subtracao, multiplicacao, divisao, potencia,
#     divisao inteira e resto da divisao.
#
# Regras (validando a Aula 15):
#   - Use os operadores +, -, *, /, **, // e %.
# ============================================================

# --- GABARITO DO PROFESSOR ---
a = int(input("Digite o primeiro numero >> "))
b = int(input("Digite o segundo numero >> "))

print("Soma:", a + b)
print("Subtracao:", a - b)
print("Multiplicacao:", a * b)
print("Divisao:", a / b)
print("Potencia:", a ** b)
print("Divisao inteira:", a // b)
print("Resto da divisao:", a % b)
