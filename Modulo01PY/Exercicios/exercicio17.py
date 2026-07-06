# ============================================================
# EXERCICIO 17 - "O ENGENHEIRO E A ESCADA"
# Base: Aula 17 (Modulo math: sqrt e resto da divisao)
# ------------------------------------------------------------
# Contexto:
#   O Python nao faz tudo sozinho: funcoes especiais moram em
#   modulos que importamos quando precisamos. O modulo math guarda
#   a matematica mais avancada, como a raiz quadrada.
#
# Sua missao:
#   Uma escada esta apoiada em uma parede. Voce sabe a altura que ela
#   alcanca na parede e a distancia da base ate a parede. Descubra o
#   COMPRIMENTO da escada (a hipotenusa!) usando raiz quadrada.
#     comprimento = raiz de (altura^2 + distancia^2)
#
# Regras (validando a Aula 17):
#   - Importe sqrt do modulo math.
# ============================================================

# --- GABARITO DO PROFESSOR ---
from math import sqrt

altura = float(input("Altura na parede (m) >> "))
distancia = float(input("Distancia da base a parede (m) >> "))

comprimento = sqrt(altura ** 2 + distancia ** 2)
print(f"A escada precisa ter {comprimento:.2f} metros.")
