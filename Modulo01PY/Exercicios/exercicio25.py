# ============================================================
# EXERCICIO 25 - "A PLAYLIST"
# Base: Aula 25 (Listas: criar, indexar e fatiar)
# ------------------------------------------------------------
# Contexto:
#   Uma variavel guarda UM valor. Uma lista guarda VARIOS de uma vez.
#   E o primeiro passo para lidar com colecoes de dados.
#
# Sua missao:
#   Crie uma playlist com pelo menos 5 musicas (a seu gosto) e:
#     - mostre a playlist inteira
#     - mostre a PRIMEIRA musica
#     - mostre a ULTIMA musica
#     - mostre as 3 primeiras musicas (fatiamento)
#     - troque a segunda musica por outra
#     - diga quantas musicas tem no total
#
# Regras (validando a Aula 25):
#   - Use indices, fatiamento e len().
# ============================================================

# --- GABARITO DO PROFESSOR ---
playlist = ["Bohemian Rhapsody", "Imagine", "Hotel California", "Thriller", "Yesterday"]

print("Playlist:", playlist)
print("Primeira:", playlist[0])
print("Ultima:", playlist[-1])
print("Top 3:", playlist[0:3])

playlist[1] = "Smells Like Teen Spirit"
print("Depois da troca:", playlist)

print("Total de musicas:", len(playlist))
