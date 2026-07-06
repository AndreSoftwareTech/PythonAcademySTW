# ============================================================
# EXERCICIO 37 - "O INTERVALO PERSONALIZADO"
# Base: Aula 37 (for: intervalo inicio-fim)
# ------------------------------------------------------------
# Contexto:
#   O range() pode comecar e terminar onde voce mandar. Lembre-se do
#   detalhe classico: o numero final NAO entra na contagem.
#
# Sua missao:
#   Pergunte ao usuario dois numeros: um inicio e um fim. Imprima
#   todos os numeros desse intervalo, INCLUINDO o numero final
#   (cuidado: o range para antes do fim, entao ajuste!).
#
# Regras (validando a Aula 37):
#   - Use for com range(inicio, fim) e resolva o "fim que nao entra".
# ============================================================

# --- GABARITO DO PROFESSOR ---
inicio = int(input("Numero inicial >> "))
fim = int(input("Numero final >> "))

# somamos +1 no fim para que o proprio numero final apareca
for numero in range(inicio, fim + 1):
    print(numero)
