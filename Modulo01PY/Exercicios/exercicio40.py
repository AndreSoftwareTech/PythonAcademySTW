# ============================================================
# EXERCICIO 40 - "O ECO PROGRAMAVEL"
# Base: Aula 40 (for: com entrada do usuario)
# ------------------------------------------------------------
# Contexto:
#   O poder do for fica ainda maior quando e o USUARIO quem decide
#   quantas vezes o laco vai rodar.
#
# Sua missao:
#   Pergunte ao usuario uma mensagem e QUANTAS vezes ela deve ser
#   repetida. Depois, imprima a mensagem esse tanto de vezes,
#   numerando cada repeticao.
#
# Regras (validando a Aula 40):
#   - A quantidade de repeticoes deve vir do input e controlar o range.
# ============================================================

# --- GABARITO DO PROFESSOR ---
mensagem = input("Qual mensagem repetir? >> ")
vezes = int(input("Quantas vezes? >> "))

for numero in range(1, vezes + 1):
    print(f"{numero}: {mensagem}")
