# ============================================================
# EXERCICIO 26 - "O CARRINHO DE COMPRAS"
# Base: Aula 26 (Listas: metodos principais)
# ------------------------------------------------------------
# Contexto:
#   Uma lista viva muda o tempo todo: itens entram, itens saem,
#   tudo se reorganiza. Os metodos de lista sao suas ferramentas.
#
# Sua missao:
#   Simule um carrinho de compras (comece vazio) e:
#     - adicione 3 produtos (append)
#     - o cliente colocou um item errado: adicione e depois remova ele
#     - coloque um produto "urgente" na PRIMEIRA posicao (insert)
#     - ordene o carrinho em ordem alfabetica (sort)
#     - mostre o carrinho final e a quantidade de itens
#
# Regras (validando a Aula 26):
#   - Use append(), remove(), insert(), sort() e len().
# ============================================================

# --- GABARITO DO PROFESSOR ---
carrinho = []

carrinho.append("arroz")
carrinho.append("feijao")
carrinho.append("cafe")

carrinho.append("refrigerante")   # item errado
carrinho.remove("refrigerante")   # cliente desistiu

carrinho.insert(0, "leite")       # produto urgente na frente

carrinho.sort()

print("Carrinho final:", carrinho)
print("Itens no carrinho:", len(carrinho))
