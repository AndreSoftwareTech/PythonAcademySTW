# ============================================================
# EXERCICIO 09 - "A CAIXA DE FERRAMENTAS"
# Base: Aula 09 (Separando funcoes em arquivos / import)
# ------------------------------------------------------------
# Contexto:
#   Em projetos reais, funcoes ficam em arquivos separados e sao
#   IMPORTADAS onde forem necessarias.
#
# Sua missao (versao completa, com pastas):
#   1) Crie um arquivo 'ferramentas.py' com as funcoes:
#      dobrar(n), triplicar(n) e ao_quadrado(n).
#   2) Crie um 'main.py' que IMPORTE essas funcoes e as utilize.
#
# Regras (validando a Aula 09):
#   - As funcoes devem morar em outro arquivo e ser importadas.
#
# OBS: o gabarito abaixo esta em UM arquivo so, para voce conferir
#      a logica. O desafio de verdade e SEPARAR em dois arquivos,
#      exatamente como fizemos na aula (calculadora.py + main.py).
# ============================================================

# --- GABARITO DO PROFESSOR (logica; separe em 2 arquivos) ---

# >>> conteudo que iria em ferramentas.py:
def dobrar(n):
    return n * 2

def triplicar(n):
    return n * 3

def ao_quadrado(n):
    return n ** 2

# >>> conteudo que iria em main.py (usando "from ferramentas import ..."):
print("Dobro de 5:", dobrar(5))
print("Triplo de 5:", triplicar(5))
print("5 ao quadrado:", ao_quadrado(5))
