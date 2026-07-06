# ============================================================
# AULA 49 - VALIDACAO DE ENTRADA (while True + break)
# Objetivo: repetir a pergunta ATE o usuario digitar um valor valido.
# ============================================================

# while True cria um laco "infinito" que so termina quando usamos break.
while True:
    idade = int(input("Digite sua idade (de 1 a 120) >> "))
    if idade >= 1 and idade <= 120:
        break   # valor valido: sai do laco
    print("Idade invalida! Tente novamente.")

print(f"Idade registrada: {idade}")
