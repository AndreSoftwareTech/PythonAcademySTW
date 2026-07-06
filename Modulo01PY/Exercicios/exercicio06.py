# ============================================================
# EXERCICIO 06 - "O DETETIVE DE TIPOS"
# Base: Aula 06 (Descobrindo o tipo com type())
# ------------------------------------------------------------
# Contexto:
#   Nem sempre e obvio de que tipo e um dado, principalmente quando
#   ele vem de fora. O detetive type() revela a verdade.
#
# Sua missao:
#   Crie 4 variaveis com valores DIFERENTES (um texto, um inteiro,
#   um decimal e um booleano) e, para cada uma, imprima o valor
#   JUNTO com o seu tipo, usando type().
#
# Regras (validando a Aula 06):
#   - Use type() em todas as 4 variaveis.
#
# Desafio logico:
#   Guarde o numero 10 dentro de aspas ("10") e mostre o type().
#   Ele e int ou str? Deixe um comentario explicando o porque.
# ============================================================

# --- GABARITO DO PROFESSOR ---
titulo = "Python"
ano = 1991
versao = 3.12
open_source = True

print(titulo, type(titulo))
print(ano, type(ano))
print(versao, type(versao))
print(open_source, type(open_source))

# Desafio: numero entre aspas e TEXTO (str), nao numero.
# O que define o tipo sao as aspas, e nao o conteudo parecer um numero.
numero_falso = "10"
print(numero_falso, type(numero_falso))
