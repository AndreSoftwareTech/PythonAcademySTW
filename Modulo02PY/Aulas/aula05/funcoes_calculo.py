# ============================================================
# MODULO 02 - AULA 05: PARAMETROS TIPADOS E FUNCOES DE CALCULO
# ------------------------------------------------------------
# Objetivo: criar funcoes que RECEBEM valores e RETORNAM o
# resultado de um calculo. Vamos tambem ANOTAR o tipo esperado
# de cada parametro (a: int) para deixar o codigo mais claro.
#
# Importante: a anotacao (: int) e apenas uma DICA de leitura;
# ela nao obriga nem converte o tipo automaticamente.
# ============================================================

def soma(a: int, b: int):
    return a + b

def subtracao(a: int, b: int):
    return a - b

def multiplicacao(a: int, b: int):
    return a * b

def divisao(a: int, b: int):
    return a / b

print("Soma:", soma(10, 5))
print("Subtracao:", subtracao(10, 5))
print("Multiplicacao:", multiplicacao(10, 5))
print("Divisao:", divisao(10, 5))
