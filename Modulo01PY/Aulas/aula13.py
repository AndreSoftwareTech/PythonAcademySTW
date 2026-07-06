# ============================================================
# AULA 13 - STRINGS: INDEXACAO E FATIAMENTO
# Objetivo: acessar partes de um texto pela sua posicao.
# ============================================================

palavra = "Python"

# Cada caractere tem um INDICE, que comeca em 0
print(palavra[0])    # P  (primeiro)
print(palavra[1])    # y
print(palavra[-1])   # n  (indice negativo = de tras para frente)

# FATIAMENTO [inicio:fim]  -> o "fim" NAO entra
print(palavra[0:3])  # Pyt
print(palavra[:3])   # Pyt  (do comeco ate o indice 3)
print(palavra[3:])   # hon  (do indice 3 ate o fim)
print(palavra[::-1]) # nohtyP  (a palavra invertida)

# len() devolve o tamanho (quantidade de caracteres)
print("Tamanho:", len(palavra))
