# ============================================================
# EXERCICIO 03 - "A CALCULADORA DE AREA"
# Base: Aula 03 (Retorno de valores com return)
# ------------------------------------------------------------
# Contexto:
#   Diferente do print (que so mostra), o return DEVOLVE o
#   resultado para ser guardado e reutilizado.
#
# Sua missao:
#   Crie uma funcao 'area_retangulo' que receba base e altura e
#   RETORNE a area (base * altura). Guarde o retorno em uma
#   variavel e so depois imprima.
#
# Regras (validando a Aula 03):
#   - A funcao deve usar return (nao pode imprimir por dentro).
# ============================================================

# --- GABARITO DO PROFESSOR ---
def area_retangulo(base, altura):
    return base * altura

resultado = area_retangulo(5, 3)
print("Area do retangulo:", resultado)
