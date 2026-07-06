# ============================================================
# AULA 26 - LISTAS: METODOS PRINCIPAIS
# Objetivo: adicionar, remover e organizar itens de uma lista.
# ============================================================

numeros = [5, 2, 8, 1]

numeros.append(10)      # adiciona um item no FIM
print("Depois do append:", numeros)

numeros.insert(0, 99)   # adiciona um item na posicao 0
print("Depois do insert:", numeros)

numeros.remove(8)       # remove o item de VALOR 8
print("Depois do remove:", numeros)

ultimo = numeros.pop()  # remove e DEVOLVE o ultimo item
print("Removido com pop:", ultimo)

numeros.sort()          # ordena a lista em ordem crescente
print("Ordenada:", numeros)

# Funcoes uteis que trabalham com listas de numeros:
print("Quantidade:", len(numeros))
print("Soma:", sum(numeros))
print("Maior:", max(numeros), "| Menor:", min(numeros))
