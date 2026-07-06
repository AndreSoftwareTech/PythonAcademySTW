# ============================================================
# EXERCICIO 16 - "SOMANDO O QUE VEM DE FORA"
# Base: Aula 16 (Soma com conversao da entrada)
# ------------------------------------------------------------
# Contexto:
#   Cuidado: tudo que vem do input() e TEXTO. Se voce somar dois
#   textos, o Python apenas "cola" um no outro ("2" + "3" = "23").
#   Para fazer conta de verdade, e preciso CONVERTER para numero.
#
# Sua missao:
#   Peca a idade de duas pessoas e mostre a soma correta das idades.
#
# Regras (validando a Aula 16):
#   - Converta as entradas com int() ANTES de somar.
#
# Desafio logico:
#   Faca um comentario explicando o que apareceria na tela se voce
#   NAO usasse int() (ou seja, somando os textos direto).
# ============================================================

# --- GABARITO DO PROFESSOR ---
idade1 = int(input("Idade da pessoa 1 >> "))
idade2 = int(input("Idade da pessoa 2 >> "))

print("Soma das idades:", idade1 + idade2)

# Desafio: sem int(), "20" + "30" resultaria em "2030" (textos colados),
# e nao em 50, porque a soma de strings e uma concatenacao.
