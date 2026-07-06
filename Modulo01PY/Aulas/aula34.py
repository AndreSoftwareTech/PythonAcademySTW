# ============================================================
# AULA 34 - DICIONARIOS: PERCORRER E ALTERAR
# Objetivo: trabalhar com dados no formato chave -> valor.
# ============================================================

aluno = {"nome": "Andre", "idade": 25, "curso": "Python"}

# Acessando um valor pela sua chave
print(aluno["nome"])

# Adicionando uma nova chave e alterando uma existente
aluno["nota"] = 9.5     # nova chave
aluno["idade"] = 26     # altera a chave que ja existia

# Percorrendo apenas as CHAVES
for chave in aluno.keys():
    print("Chave:", chave)

# Percorrendo apenas os VALORES
for valor in aluno.values():
    print("Valor:", valor)

# Percorrendo CHAVE e VALOR ao mesmo tempo (items)
for chave, valor in aluno.items():
    print(f"{chave} = {valor}")

# Removendo uma chave
del aluno["curso"]
print(aluno)
