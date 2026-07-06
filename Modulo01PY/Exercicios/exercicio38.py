# ============================================================
# EXERCICIO 38 - "DE CINCO EM CINCO"
# Base: Aula 38 (for: com passo)
# ------------------------------------------------------------
# Contexto:
#   O range() aceita um terceiro numero: o PASSO, que decide de
#   quanto em quanto a contagem anda.
#
# Sua missao:
#   Imprima todos os multiplos de 5 de 0 ate 50 (0, 5, 10, ... 50)
#   usando o passo do range.
#
# Regras (validando a Aula 38):
#   - Use for com range(inicio, fim, passo).
#
# Desafio logico:
#   Faca uma segunda contagem, agora de 2 em 2, de 0 ate 20.
# ============================================================

# --- GABARITO DO PROFESSOR ---
print("Multiplos de 5:")
for numero in range(0, 51, 5):
    print(numero)

# Desafio: de 2 em 2
print("De 2 em 2:")
for numero in range(0, 21, 2):
    print(numero)
