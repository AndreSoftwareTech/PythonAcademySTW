# ============================================================
# EXERCICIO 45 - "O ARQUITETO DE PIRAMIDES"
# Base: Aula 45 (Laco aninhado: for dentro de for)
# ------------------------------------------------------------
# Contexto:
#   Um laco dentro de outro abre um universo: tabelas, tabuleiros,
#   matrizes e desenhos. E aqui que a logica comeca a ficar bonita.
#
# Sua missao:
#   Pergunte uma altura ao usuario e desenhe uma piramide de
#   asteriscos alinhada a esquerda, assim (altura 4):
#       *
#       **
#       ***
#       ****
#
# Regras (validando a Aula 45):
#   - Voce pode resolver com laco aninhado OU com repeticao de string.
#     Se conseguir das DUAS formas, melhor ainda!
#
# Desafio logico:
#   Depois da piramide crescente, desenhe uma DECRESCENTE (de cima
#   larga ate 1 asterisco).
# ============================================================

# --- GABARITO DO PROFESSOR ---
altura = int(input("Altura da piramide >> "))

# Versao 1: laco aninhado (montando a linha asterisco por asterisco)
for linha in range(1, altura + 1):
    estrelas = ""
    for coluna in range(linha):
        estrelas = estrelas + "*"
    print(estrelas)

print("---")

# Desafio: piramide decrescente (usando repeticao de string)
for linha in range(altura, 0, -1):
    print("*" * linha)
