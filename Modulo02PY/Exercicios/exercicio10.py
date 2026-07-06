# ============================================================
# EXERCICIO 10 - "A AGENDA DE CONTATOS"
# Base: Aula 10 (CRUD em memoria com funcoes)
# ------------------------------------------------------------
# Contexto:
#   Antes de salvar em arquivo, precisamos dominar o CRUD na
#   memoria: criar, listar e remover itens de uma colecao.
#
# Sua missao:
#   Crie uma agenda (lista) e as funcoes:
#     - adicionar(nome)   -> adiciona um contato
#     - listar()          -> devolve todos os contatos
#     - remover(nome)     -> remove um contato pelo nome
#     - total()           -> quantidade de contatos
#   Faca uma pequena demonstracao chamando as funcoes.
#
# Regras (validando a Aula 10):
#   - Os dados ficam em uma lista na memoria, manipulada por funcoes.
# ============================================================

# --- GABARITO DO PROFESSOR ---
contatos = []

def adicionar(nome):
    contatos.append(nome)
    return "Contato adicionado"

def listar():
    return contatos

def remover(nome):
    if nome in contatos:
        contatos.remove(nome)
        return "Contato removido"
    return "Contato nao encontrado"

def total():
    return len(contatos)

print(adicionar("Andre"))
print(adicionar("Maria"))
print(adicionar("Joao"))
print("Contatos:", listar())
print(remover("Maria"))
print("Contatos:", listar())
print("Total:", total())
