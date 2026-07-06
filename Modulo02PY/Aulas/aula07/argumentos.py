# ============================================================
# MODULO 02 - AULA 07: ARGUMENTOS PADRAO E *args  [NOVO]
# ------------------------------------------------------------
# Objetivo: deixar as funcoes mais flexiveis.
#   - Argumento PADRAO: valor usado quando quem chama nao informa.
#   - *args: recebe uma quantidade VARIAVEL de argumentos.
# ============================================================

# Argumento padrao: se nao passarmos "saudacao", vale "Ola".
def cumprimentar(nome, saudacao="Ola"):
    print(f"{saudacao}, {nome}!")

cumprimentar("Andre")               # usa o padrao -> Ola, Andre!
cumprimentar("Maria", "Bom dia")    # sobrescreve   -> Bom dia, Maria!

# *args: os argumentos extras chegam agrupados em uma tupla.
def somar_tudo(*numeros):
    total = 0
    for n in numeros:
        total = total + n
    return total

print("Soma de 3 numeros:", somar_tudo(1, 2, 3))          # 6
print("Soma de 4 numeros:", somar_tudo(10, 20, 30, 40))   # 100
