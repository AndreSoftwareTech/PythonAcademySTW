# ============================================================
# MODULO 02 - AULA 11: ORGANIZANDO O PROJETO EM PASTAS
# ------------------------------------------------------------
# Este arquivo fica DENTRO da pasta 'controller'. Separar cada
# responsabilidade em sua propria pasta deixa projetos grandes
# organizados e faceis de manter. A pasta vira um "pacote" gracas
# ao arquivo __init__.py que colocamos ao lado.
# ============================================================

pessoas = []

def cadastrar(nome):
    pessoas.append(nome)
    return "Pessoa cadastrada com sucesso"

def listar():
    return pessoas
