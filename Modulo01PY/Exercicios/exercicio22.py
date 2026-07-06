# ============================================================
# EXERCICIO 22 - "O CONVERSOR DE CONCEITOS"
# Base: Aula 22 (Condicional por faixas de valor)
# ------------------------------------------------------------
# Contexto:
#   Muitas decisoes acontecem por FAIXAS: notas viram conceitos,
#   salarios viram faixas de imposto, pontos viram medalhas.
#
# Sua missao:
#   Pergunte a nota de um aluno (de 0 a 100) e converta para
#   conceito, seguindo as faixas:
#     90 a 100 -> A
#     80 a 89  -> B
#     70 a 79  -> C
#     60 a 69  -> D
#     abaixo de 60 -> F
#   Se a nota for invalida (menor que 0 ou maior que 100), avise.
#
# Regras (validando a Aula 22):
#   - Use if/elif encadeados aproveitando a ordem das faixas.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nota = int(input("Digite a nota (0 a 100) >> "))

if nota < 0 or nota > 100:
    print("Nota invalida!")
elif nota >= 90:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
else:
    print("Conceito: F")
