# ============================================================
# EXERCICIO 02 - "O CODIGO QUE SE EXPLICA"
# Base: Aula 02 (Comentarios e boas praticas)
# ------------------------------------------------------------
# Contexto:
#   Um bom programador escreve codigo que outra pessoa entende
#   sem precisar ligar para ele as 3 da manha. Documentar e um
#   ato de respeito com o proximo (que pode ser voce no futuro).
#
# Sua missao:
#   Crie a "ficha tecnica" de um veiculo respeitando boas praticas:
#     1) Um comentario de UMA linha explicando o que o programa faz.
#     2) Um bloco de anotacao com aspas triplas (""" ... """).
#     3) Tres variaveis em snake_case (ex.: modelo_carro).
#     4) UMA constante em MAIUSCULO (ex.: VELOCIDADE_MAXIMA).
#     5) Imprima todos os dados no final.
#
# Regras (validando a Aula 02):
#   - Nomes de variaveis devem DESCREVER o conteudo (nada de x, y, a).
# ============================================================

# --- GABARITO DO PROFESSOR ---
# Programa que exibe a ficha tecnica de um veiculo.
"""
Ficha tecnica simples usada para treinar comentarios,
nomes descritivos (snake_case) e constantes (MAIUSCULO).
"""

modelo_carro = "Fusca 1975"
cor_do_veiculo = "Azul"
potencia_cavalos = 46
VELOCIDADE_MAXIMA = 130  # constante: nao muda durante o programa

print(modelo_carro, cor_do_veiculo, potencia_cavalos, VELOCIDADE_MAXIMA)
