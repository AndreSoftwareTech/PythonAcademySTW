# ============================================================
# AULA 31 - TUPLAS
# Objetivo: conhecer uma colecao parecida com a lista, porem IMUTAVEL.
# ============================================================

# A tupla usa parenteses ( ). Depois de criada, NAO pode ser alterada.
ponto = (10, 20)
print("Coordenada X:", ponto[0])
print("Coordenada Y:", ponto[1])

cores = ("vermelho", "verde", "azul")
print(cores)
print("Quantidade de cores:", len(cores))

# Percorrendo os itens de uma tupla
for cor in cores:
    print("Cor:", cor)

# Usamos tuplas quando os dados NAO devem mudar (ex.: dias da semana).
