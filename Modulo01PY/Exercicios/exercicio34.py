# ============================================================
# EXERCICIO 34 - "O RELATORIO AUTOMATICO"
# Base: Aula 34 (Dicionarios: percorrer e alterar)
# ------------------------------------------------------------
# Contexto:
#   Acessar chave por chave e cansativo quando a ficha e grande. O
#   ideal e o programa PERCORRER o dicionario sozinho e cuspir tudo.
#
# Sua missao:
#   Comece com um dicionario de um produto ("nome", "preco",
#   "estoque"). Faca o seguinte:
#     - aumente o preco (altere a chave "preco")
#     - adicione uma nova chave "categoria"
#     - percorra o dicionario mostrando cada linha no formato
#       "chave: valor"
#     - remova a chave "estoque" e mostre o resultado final
#
# Regras (validando a Aula 34):
#   - Use um for com .items() e o comando del.
# ============================================================

# --- GABARITO DO PROFESSOR ---
produto = {"nome": "Teclado", "preco": 120.0, "estoque": 30}

produto["preco"] = 149.9        # alterando um valor existente
produto["categoria"] = "Perifericos"  # nova chave

print("--- Ficha do produto ---")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")

del produto["estoque"]
print("Apos remover o estoque:", produto)
