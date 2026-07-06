# ============================================================
# EXERCICIO 47 - "A ENERGIA QUE ACABA"
# Base: Aula 47 (while: incremento e condicao de parada)
# ------------------------------------------------------------
# Contexto:
#   O while brilha quando a parada depende de uma REGRA, e nao de uma
#   contagem fixa. Ele repete ate a condicao deixar de ser verdadeira.
#
# Sua missao:
#   Um jogador comeca com 100 pontos de energia. A cada rodada ele
#   perde 15 de energia. Usando while, mostre a energia a cada rodada
#   ENQUANTO ela for maior que 0. No final, avise "Energia esgotada".
#
# Regras (validando a Aula 47):
#   - Use while com uma variavel que muda a cada volta.
# ============================================================

# --- GABARITO DO PROFESSOR ---
energia = 100

while energia > 0:
    print(f"Energia atual: {energia}")
    energia = energia - 15

print("Energia esgotada!")
