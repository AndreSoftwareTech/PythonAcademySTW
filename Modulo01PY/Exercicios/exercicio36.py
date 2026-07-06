# ============================================================
# EXERCICIO 36 - "CONTANDO CARNEIRINHOS"
# Base: Aula 36 (for: range basico)
# ------------------------------------------------------------
# Contexto:
#   Chegou a solucao para a repeticao: o laco for. Com o range() ele
#   repete um bloco quantas vezes voce quiser, sem esforco.
#
# Sua missao:
#   Use um unico for para imprimir 10 vezes a frase:
#       "Carneirinho numero X pulou a cerca"
#   trocando o X pelo numero da vez (de 1 a 10).
#
# Regras (validando a Aula 36):
#   - Use for com range(). Nada de 10 prints na mao.
# ============================================================

# --- GABARITO DO PROFESSOR ---
for numero in range(1, 11):
    print(f"Carneirinho numero {numero} pulou a cerca")
