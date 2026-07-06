# ============================================================
# EXERCICIO 07 - "MONTANDO A FRASE"
# Base: Aula 07 (Concatenacao na saida)
# ------------------------------------------------------------
# Contexto:
#   Juntar pedacos de texto e uma das tarefas mais comuns do dia a
#   dia. Existem dois caminhos: separar por virgula dentro do print
#   ou "colar" textos com o operador +.
#
# Sua missao:
#   Pergunte ao usuario o nome e o sobrenome. Depois, imprima o nome
#   completo de DUAS formas diferentes:
#     1) usando virgulas dentro do print
#     2) usando o operador + para colar as palavras (cuidado com o
#        espaco entre elas!)
#
# Regras (validando a Aula 07):
#   - Mostre que voce entende a diferenca entre virgula e +.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome = input("Digite seu nome >> ")
sobrenome = input("Digite seu sobrenome >> ")

# 1) com virgula (o print ja coloca um espaco entre os itens)
print("Nome completo:", nome, sobrenome)

# 2) com + (precisamos colocar o espaco " " na mao)
print("Nome completo: " + nome + " " + sobrenome)
