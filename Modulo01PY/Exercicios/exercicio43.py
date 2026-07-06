# ============================================================
# EXERCICIO 43 - "O CAIXA DO MERCADO"
# Base: Aula 43 (Acumuladores e contadores)
# ------------------------------------------------------------
# Contexto:
#   Somar valores que chegam um a um e o coracao de qualquer caixa,
#   boletim ou placar. O segredo e ter uma variavel que ACUMULA e
#   outra que CONTA.
#
# Sua missao:
#   Simule um caixa. Pergunte quantos produtos o cliente comprou e,
#   para cada um, pergunte o preco. No final, mostre:
#     - o total da compra
#     - a quantidade de itens
#     - o valor MEDIO por item
#
# Regras (validando a Aula 43):
#   - Use um acumulador (total) dentro de um for.
# ============================================================

# --- GABARITO DO PROFESSOR ---
quantidade = int(input("Quantos produtos? >> "))

total = 0.0
for item in range(1, quantidade + 1):
    preco = float(input(f"Preco do produto {item} >> "))
    total = total + preco

media = total / quantidade
print(f"Total da compra: R$ {total:.2f}")
print(f"Itens: {quantidade}")
print(f"Valor medio por item: R$ {media:.2f}")
