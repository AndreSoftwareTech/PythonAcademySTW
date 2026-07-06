# ============================================================
# AULA 25 - LISTAS: CRIAR, INDEXAR E FATIAR
# Objetivo: guardar varios valores dentro de uma unica variavel.
# ============================================================

# Uma lista e criada com colchetes [ ] e itens separados por virgula
frutas = ["maca", "banana", "uva", "laranja"]

print(frutas)          # a lista inteira
print(frutas[0])       # primeiro item: maca
print(frutas[-1])      # ultimo item: laranja
print(frutas[1:3])     # fatiamento: ['banana', 'uva']
print("Total de frutas:", len(frutas))

# Alterando um item pelo seu indice
frutas[1] = "morango"
print(frutas)

# Verificando se um item existe na lista
print("uva" in frutas)
