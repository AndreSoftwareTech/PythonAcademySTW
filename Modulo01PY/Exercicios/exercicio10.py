# ============================================================
# EXERCICIO 10 - "A NOTA FISCAL CAPRICHADA"
# Base: Aula 10 (F-strings formatadas: .2f, milhar, %)
# ------------------------------------------------------------
# Contexto:
#   Dinheiro na tela SEMPRE aparece com 2 casas decimais. Um sistema
#   que mostra "R$ 9.9" em vez de "R$ 9.90" passa falta de cuidado.
#
# Sua missao:
#   Crie um mini recibo. Defina o preco de um produto (com muitas
#   casas, ex.: 1999.9) e uma taxa de desconto (ex.: 0.15). Imprima:
#     - o preco formatado com 2 casas decimais
#     - o preco formatado com separador de milhar
#     - o desconto exibido como porcentagem
#     - o valor final ja com o desconto aplicado (2 casas)
#
# Regras (validando a Aula 10):
#   - Use os formatadores :.2f , :,.2f e :.0% ou :.1% nas f-strings.
# ============================================================

# --- GABARITO DO PROFESSOR ---
preco = 1999.9
desconto = 0.15

valor_final = preco - (preco * desconto)

print(f"Preco: R$ {preco:.2f}")
print(f"Preco (milhar): R$ {preco:,.2f}")
print(f"Desconto aplicado: {desconto:.0%}")
print(f"Valor final: R$ {valor_final:,.2f}")
