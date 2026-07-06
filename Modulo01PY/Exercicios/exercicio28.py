# ============================================================
# EXERCICIO 28 - "EMBARALHANDO A ORDEM"
# Base: Aula 28 (Aleatoriedade: shuffle)
# ------------------------------------------------------------
# Contexto:
#   As vezes nao queremos UM item, mas sim BAGUNCAR a ordem de todos.
#   E o que o shuffle() faz: embaralha a lista inteira no lugar.
#
# Sua missao:
#   Monte uma lista com a ordem de apresentacao de 5 equipes de um
#   seminario e embaralhe para definir a ordem sorteada. Mostre a
#   lista antes e depois de embaralhar.
#
# Regras (validando a Aula 28):
#   - Use shuffle() do modulo random.
# ============================================================

# --- GABARITO DO PROFESSOR ---
from random import shuffle

equipes = ["Equipe A", "Equipe B", "Equipe C", "Equipe D", "Equipe E"]

print("Ordem original:", equipes)
shuffle(equipes)
print("Ordem sorteada:", equipes)
