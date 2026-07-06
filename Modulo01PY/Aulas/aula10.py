# ============================================================
# AULA 10 - F-STRINGS FORMATADAS
# Objetivo: controlar COMO os numeros e textos aparecem na tela.
# ============================================================

preco = 1234.5
media = 7.6666666

# :.2f  -> mostra o numero com 2 casas decimais
print(f"Preco: R$ {preco:.2f}")
print(f"Media: {media:.2f}")

# :,.2f -> separador de milhar + 2 casas decimais
print(f"Valor: R$ {preco:,.2f}")

# Alinhamento em 10 espacos:  < esquerda   > direita   ^ centro
print(f"|{'esquerda':<10}|")
print(f"|{'direita':>10}|")
print(f"|{'centro':^10}|")

# :.1% -> transforma em porcentagem com 1 casa decimal
taxa = 0.157
print(f"Taxa: {taxa:.1%}")
