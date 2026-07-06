# ============================================================
# EXERCICIO 20 - "O PORTEIRO DA BALADA"
# Base: Aula 20 (Operadores logicos: and, or, not)
# ------------------------------------------------------------
# Contexto:
#   As decisoes da vida real quase nunca dependem de uma condicao so.
#   "Pode entrar SE for maior de idade E estiver na lista, OU se for
#   convidado VIP." E ai que entram os operadores logicos.
#
# Sua missao:
#   Crie o cerebro de um porteiro digital. Pergunte:
#     - a idade da pessoa
#     - se o nome esta na lista (sim/nao)
#     - se e VIP (sim/nao)
#   A pessoa PODE ENTRAR se:
#     (tiver 18 anos ou mais  E  estiver na lista)  OU  for VIP.
#   Imprima True ou False para a liberacao.
#
# Regras (validando a Aula 20):
#   - Combine and, or (e, se quiser, not) em UMA expressao.
# ============================================================

# --- GABARITO DO PROFESSOR ---
idade = int(input("Idade >> "))
na_lista = input("Esta na lista? (sim/nao) >> ").lower() == "sim"
vip = input("E VIP? (sim/nao) >> ").lower() == "sim"

pode_entrar = (idade >= 18 and na_lista) or vip
print("Liberado para entrar?", pode_entrar)
