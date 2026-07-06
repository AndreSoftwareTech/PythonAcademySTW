# ============================================================
# EXERCICIO 04 - "A RECEPCIONISTA VIRTUAL"
# Base: Aula 04 (Entrada de dados com input)
# ------------------------------------------------------------
# Contexto:
#   Ate agora os dados eram fixos. Chegou a hora de o programa
#   CONVERSAR com quem esta do outro lado da tela.
#
# Sua missao:
#   Crie uma recepcionista digital que pergunte ao visitante:
#     - o nome
#     - a cidade de onde ele vem
#     - o ano em que nasceu
#   Em seguida, devolva uma mensagem repetindo os 3 dados recebidos.
#
# Regras (validando a Aula 04):
#   - Toda entrada deve vir de input().
#   - Guarde cada resposta em uma variavel antes de imprimir.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome = input("Bem-vindo(a)! Qual e o seu nome? >> ")
cidade = input("De qual cidade voce chegou? >> ")
ano_nascimento = input("Em que ano voce nasceu? >> ")

print("Registrando visitante:", nome, "-", cidade, "-", ano_nascimento)
