# ============================================================
# EXERCICIO 12 - "O VALIDADOR DE FORMULARIO"
# Base: Aula 12 (Metodos booleanos de string)
# ------------------------------------------------------------
# Contexto:
#   Todo sistema que recebe dados precisa "interrogar" o que foi
#   digitado: isso e numero? tem so letras? tem espaco? O Python
#   responde a essas perguntas com metodos que devolvem True/False.
#
# Sua missao:
#   Pergunte um dado qualquer ao usuario e gere um "laudo" dizendo:
#     - se contem apenas numeros
#     - se contem apenas letras
#     - se e alfanumerico
#     - se possui algum espaco
#
# Regras (validando a Aula 12):
#   - Use os metodos isnumeric(), isalpha(), isalnum() e isspace().
# ============================================================

# --- GABARITO DO PROFESSOR ---
dado = input("Digite qualquer coisa para analise >> ")

print("Somente numeros?", dado.isnumeric())
print("Somente letras?", dado.isalpha())
print("Alfanumerico?", dado.isalnum())
print("Contem espaco?", dado.isspace())
