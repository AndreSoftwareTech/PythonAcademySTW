# ============================================================
# EXERCICIO 30 - "QUEM LEVA O PREMIO?"
# Base: Aula 30 (Sorteio combinado com condicionais)
# ------------------------------------------------------------
# Contexto:
#   Sortear e legal, mas o programa fica mais inteligente quando
#   REAGE ao resultado do sorteio. Aqui unimos aleatoriedade + decisao.
#
# Sua missao:
#   Pergunte 3 nomes, sorteie um vencedor e, usando condicionais,
#   anuncie QUAL posicao (primeiro, segundo ou terceiro) foi a
#   sorteada, alem do nome.
#
# Regras (validando a Aula 30):
#   - Use choice() e depois if/elif/else para descobrir a posicao.
# ============================================================

# --- GABARITO DO PROFESSOR ---
from random import choice

nome1 = input("Nome 1 >> ")
nome2 = input("Nome 2 >> ")
nome3 = input("Nome 3 >> ")

participantes = [nome1, nome2, nome3]
vencedor = choice(participantes)

print("=" * 30)
if vencedor == nome1:
    print(f"O 1o participante venceu: {vencedor}")
elif vencedor == nome2:
    print(f"O 2o participante venceu: {vencedor}")
else:
    print(f"O 3o participante venceu: {vencedor}")
