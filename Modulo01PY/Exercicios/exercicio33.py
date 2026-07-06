# ============================================================
# EXERCICIO 33 - "A FICHA DO PERSONAGEM"
# Base: Aula 33 (Dicionarios: criar e acessar)
# ------------------------------------------------------------
# Contexto:
#   Listas guardam valores por POSICAO. Dicionarios guardam por NOME
#   (a chave). E como uma ficha: "nome", "idade", "classe"... cada
#   rotulo aponta para uma informacao.
#
# Sua missao:
#   Monte a ficha de um personagem em um dicionario com, no minimo,
#   as chaves: "nome", "classe", "nivel" e "arma". Depois, acesse e
#   imprima cada informacao usando a chave.
#
# Regras (validando a Aula 33):
#   - Crie o dicionario com {} e acesse os valores por dicionario[chave].
# ============================================================

# --- GABARITO DO PROFESSOR ---
personagem = {
    "nome": "Aria",
    "classe": "Maga",
    "nivel": 12,
    "arma": "Cajado de Cristal"
}

print("Nome:", personagem["nome"])
print("Classe:", personagem["classe"])
print("Nivel:", personagem["nivel"])
print("Arma:", personagem["arma"])
