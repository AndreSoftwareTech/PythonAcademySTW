# ============================================================
# EXERCICIO 46 - "O CONTADOR TEIMOSO"
# Base: Aula 46 (while: introducao)
# ------------------------------------------------------------
# Contexto:
#   O for e otimo quando sabemos QUANTAS vezes repetir. Mas e quando
#   nao sabemos? Ai entra o while, que repete ENQUANTO uma condicao
#   for verdadeira. Cuidado: esqueca de atualizar a condicao e voce
#   cria um loop infinito!
#
# Sua missao:
#   Pergunte um numero N ao usuario e, usando while (NAO use for),
#   imprima a contagem de 1 ate N.
#
# Regras (validando a Aula 46):
#   - Inicie a variavel de controle ANTES do while.
#   - Nao esqueca de incrementa-la dentro do laco.
# ============================================================

# --- GABARITO DO PROFESSOR ---
n = int(input("Contar ate quanto? >> "))

contador = 1                 # inicia a variavel antes do while
while contador <= n:
    print(contador)
    contador = contador + 1  # atualiza para o laco poder terminar
