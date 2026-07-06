# ============================================================
# MODULO 02 - AULA 04: RETORNANDO VARIOS VALORES
# ------------------------------------------------------------
# Objetivo: uma funcao pode devolver MAIS DE UM valor ao mesmo
# tempo. O Python junta tudo em uma tupla e nos podemos
# "desempacotar" em varias variaveis de uma vez.
#
# OBS: a versao antiga desta aula tinha um bug (chamava uma
# funcao passando uma variavel que ainda nao existia). Aqui a
# ordem esta correta: primeiro coletamos, depois usamos.
# ============================================================

def coletar_dados():
    nome = input("Digite seu nome >> ")
    sobrenome = input("Digite seu sobrenome >> ")
    idade = input("Digite sua idade >> ")
    return nome, sobrenome, idade   # devolve os 3 de uma vez

# desempacotando os tres valores retornados em tres variaveis:
nome, sobrenome, idade = coletar_dados()

print(f"Nome: {nome} | Sobrenome: {sobrenome} | Idade: {idade}")
