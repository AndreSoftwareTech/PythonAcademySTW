# ============================================================
# MODULO 02 - AULA 02: FUNCOES COM PARAMETROS
# ------------------------------------------------------------
# Objetivo: fazer a funcao receber "entradas" (parametros) para
# trabalhar com valores diferentes a cada chamada.
# ============================================================

# 'nome' e um PARAMETRO: um valor que a funcao recebe de fora.
def saudacao(nome):
    print(f"Ola, {nome}! Bem-vindo(a).")

# O que passamos entre parenteses e o ARGUMENTO.
saudacao("Andre")
saudacao("Maria")
