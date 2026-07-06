# ============================================================
# EXERCICIO 39 - "LANCAMENTO DO FOGUETE"
# Base: Aula 39 (for: contagem decrescente)
# ------------------------------------------------------------
# Contexto:
#   Nem toda contagem sobe. Com um passo NEGATIVO, o range() conta
#   de tras para frente, perfeito para uma contagem regressiva.
#
# Sua missao:
#   Faca a contagem regressiva de 10 ate 1 e, ao final (fora do laco),
#   imprima "DECOLAR!".
#
# Regras (validando a Aula 39):
#   - Use for com range e passo negativo (-1).
# ============================================================

# --- GABARITO DO PROFESSOR ---
for contagem in range(10, 0, -1):
    print(contagem)

print("DECOLAR!")
