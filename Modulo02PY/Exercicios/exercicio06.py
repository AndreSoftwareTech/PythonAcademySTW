# ============================================================
# EXERCICIO 06 - "O COFRE COMPARTILHADO"
# Base: Aula 06 (Escopo de variaveis: local x global)
# ------------------------------------------------------------
# Contexto:
#   Um cofre (saldo) precisa ser acessado por varias funcoes:
#   uma deposita, outra saca. Como todas mexem no MESMO saldo,
#   ele precisa ser uma variavel global.
#
# Sua missao:
#   Crie uma variavel global 'saldo' iniciando em 0. Faca duas
#   funcoes: 'depositar(valor)' e 'sacar(valor)', que ALTERAM o
#   saldo global. Faca alguns depositos/saques e mostre o saldo.
#
# Regras (validando a Aula 06):
#   - Use a palavra 'global' dentro das funcoes que alteram o saldo.
#
# Desafio logico:
#   No saque, so permita se houver saldo suficiente; caso contrario
#   imprima "Saldo insuficiente".
# ============================================================

# --- GABARITO DO PROFESSOR ---
saldo = 0

def depositar(valor):
    global saldo
    saldo = saldo + valor

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo = saldo - valor
    else:
        print("Saldo insuficiente")

depositar(100)
sacar(30)
sacar(500)   # deve avisar saldo insuficiente
print("Saldo final:", saldo)
