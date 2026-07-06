# ============================================================
# EXERCICIO 44 - "A TABUADA INSTANTANEA"
# Base: Aula 44 (Tabuada com for)
# ------------------------------------------------------------
# Contexto:
#   O classico dos classicos. Se voce entende como gerar uma tabuada
#   com um laco, voce entendeu de verdade o poder da repeticao.
#
# Sua missao:
#   Pergunte um numero e imprima a tabuada dele, de 1 a 10, no
#   formato:  "7 x 1 = 7".
#
# Regras (validando a Aula 44):
#   - Use um for de 1 a 10 e monte a linha com f-string ou format.
# ============================================================

# --- GABARITO DO PROFESSOR ---
numero = int(input("Tabuada de qual numero? >> "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
