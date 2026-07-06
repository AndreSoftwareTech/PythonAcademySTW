# ============================================================
# EXERCICIO 08 - "O MANUAL DA FUNCAO"
# Base: Aula 08 (Docstrings)
# ------------------------------------------------------------
# Contexto:
#   Codigo profissional e documentado. A docstring explica, em
#   poucas linhas, o que a funcao faz, o que recebe e o que devolve.
#
# Sua missao:
#   Crie uma funcao 'converter_reais_para_dolar(reais, cotacao)'
#   que RETORNE o valor em dolar. Escreva uma docstring completa
#   explicando os parametros e o retorno. Ao final, imprima a
#   docstring da funcao usando .__doc__.
#
# Regras (validando a Aula 08):
#   - A docstring deve ser a primeira coisa dentro da funcao.
# ============================================================

# --- GABARITO DO PROFESSOR ---
def converter_reais_para_dolar(reais, cotacao):
    """Converte um valor de reais para dolar.

    reais: valor em reais (float)
    cotacao: quanto vale 1 dolar em reais (float)
    retorna: o valor equivalente em dolar (float)
    """
    return reais / cotacao

print(f"Valor em dolar: {converter_reais_para_dolar(500, 5.0):.2f}")
print(converter_reais_para_dolar.__doc__)
