# ============================================================
# EXERCICIO 04 - "O MENOR E O MAIOR"
# Base: Aula 04 (Retornando varios valores)
# ------------------------------------------------------------
# Contexto:
#   Uma funcao pode devolver mais de um resultado de uma vez, e
#   nos "desempacotamos" em varias variaveis.
#
# Sua missao:
#   Crie uma funcao 'analisar' que receba TRES numeros e retorne,
#   ao mesmo tempo, o MENOR e o MAIOR deles. Desempacote os dois
#   retornos e imprima.
#
# Regras (validando a Aula 04):
#   - Retorne os dois valores na mesma linha de return.
#   - Dica: existem as funcoes prontas min() e max().
# ============================================================

# --- GABARITO DO PROFESSOR ---
def analisar(a, b, c):
    return min(a, b, c), max(a, b, c)

menor, maior = analisar(7, 2, 9)
print("Menor:", menor)
print("Maior:", maior)
