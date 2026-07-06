# ============================================================
# EXERCICIO 31 - "AS COORDENADAS DO TESOURO"
# Base: Aula 31 (Tuplas: colecao imutavel)
# ------------------------------------------------------------
# Contexto:
#   Alguns dados NAO podem mudar depois de definidos: as coordenadas
#   de um ponto no mapa, uma data de nascimento, as cores de uma
#   bandeira. Para isso existe a tupla, a "lista trancada a chave".
#
# Sua missao:
#   O mapa do tesouro guarda a coordenada (latitude, longitude) em
#   uma tupla. Crie essa tupla, mostre a latitude e a longitude
#   separadamente e informe quantos valores a coordenada possui.
#
# Regras (validando a Aula 31):
#   - Use uma tupla (parenteses) e acesse por indice.
#
# Desafio logico:
#   Em um comentario, explique o que aconteceria se voce tentasse
#   fazer coordenada[0] = outro_valor (por que a tupla nao deixa?).
# ============================================================

# --- GABARITO DO PROFESSOR ---
coordenada = (-27.5954, -48.5480)   # (latitude, longitude)

print("Latitude:", coordenada[0])
print("Longitude:", coordenada[1])
print("Valores na coordenada:", len(coordenada))

# Desafio: coordenada[0] = 0 daria TypeError, pois a tupla e IMUTAVEL;
# depois de criada, seus valores nao podem ser alterados.
