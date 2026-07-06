# ============================================================
# EXERCICIO 05 - "O KIT DE CONVERSOES"
# Base: Aula 05 (Parametros tipados e funcoes de calculo)
# ------------------------------------------------------------
# Contexto:
#   Programadores criam "kits" de funcoes utilitarias que resolvem
#   pequenos calculos e sao reaproveitadas em varios lugares.
#
# Sua missao:
#   Crie um kit com pelo menos 3 funcoes que RETORNAM resultados:
#     - celsius_para_fahrenheit(c)  -> c * 9/5 + 32
#     - dobro(n)                    -> n * 2
#     - media(a, b)                 -> (a + b) / 2
#   Anote os tipos dos parametros e teste cada funcao.
#
# Regras (validando a Aula 05):
#   - Todas as funcoes usam return e recebem parametros.
# ============================================================

# --- GABARITO DO PROFESSOR ---
def celsius_para_fahrenheit(c: float):
    return c * 9 / 5 + 32

def dobro(n: int):
    return n * 2

def media(a: float, b: float):
    return (a + b) / 2

print("30C em F:", celsius_para_fahrenheit(30))
print("Dobro de 21:", dobro(21))
print("Media de 8 e 6:", media(8, 6))
