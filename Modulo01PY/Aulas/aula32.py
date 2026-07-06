# ============================================================
# AULA 32 - CONJUNTOS (set)
# Objetivo: usar uma colecao SEM ordem e SEM elementos repetidos.
# ============================================================

# O conjunto usa chaves { }. Valores repetidos sao descartados.
numeros = {1, 2, 2, 3, 3, 3}
print("Os repetidos somem:", numeros)   # {1, 2, 3}

numeros.add(4)
print("Depois do add:", numeros)

# Operacoes classicas entre conjuntos:
a = {1, 2, 3}
b = {3, 4, 5}
print("Uniao (junta tudo):", a | b)
print("Intersecao (o que ha em comum):", a & b)
print("Diferenca (so em 'a'):", a - b)
