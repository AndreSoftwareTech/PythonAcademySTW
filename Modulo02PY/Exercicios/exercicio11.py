# ============================================================
# EXERCICIO 11 - "O PROJETO ARRUMADO"
# Base: Aula 11 (Organizando o projeto em pastas)
# ------------------------------------------------------------
# Contexto:
#   Projetos grandes viram bagunca se tudo fica em um arquivo so.
#   A solucao e separar responsabilidades em pastas (pacotes).
#
# Sua missao (versao completa, com pastas):
#   1) Crie uma pasta 'controller' com um arquivo
#      'produto_controller.py' contendo cadastrar(nome) e listar().
#   2) Crie um 'main.py' que importe assim:
#         from controller.produto_controller import cadastrar, listar
#   3) Nao esqueca do __init__.py dentro da pasta controller.
#
# Regras (validando a Aula 11):
#   - O controller deve morar em sua propria pasta (pacote).
#
# OBS: o gabarito abaixo mostra a LOGICA em um arquivo so. O
#      desafio real e reproduzir a estrutura de pastas da aula 11.
# ============================================================

# --- GABARITO DO PROFESSOR (logica; monte a estrutura de pastas) ---
produtos = []

def cadastrar(nome):
    produtos.append(nome)
    return "Produto cadastrado"

def listar():
    return produtos

print(cadastrar("Caneta"))
print(cadastrar("Caderno"))
print("Produtos:", listar())
