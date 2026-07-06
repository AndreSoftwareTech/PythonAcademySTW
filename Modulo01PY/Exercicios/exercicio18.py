# ============================================================
# EXERCICIO 18 - "A MEDIA QUE NAO MENTE"
# Base: Aula 18 (Precedencia aritmetica e media)
# ------------------------------------------------------------
# Contexto:
#   Em matematica, a ordem das operacoes importa. No Python tambem:
#   multiplicacao e divisao acontecem ANTES da soma. Se voce esquecer
#   os parenteses no calculo de uma media, o resultado vem errado.
#
# Sua missao:
#   Peca 3 notas ao usuario e calcule a media aritmetica correta.
#
# Regras (validando a Aula 18):
#   - Use parenteses para garantir que a SOMA aconteca antes da
#     divisao por 3.
#
# Desafio logico:
#   Em um comentario, explique por que "n1 + n2 + n3 / 3" (sem
#   parenteses) daria um resultado errado.
# ============================================================

# --- GABARITO DO PROFESSOR ---
n1 = float(input("Nota 1 >> "))
n2 = float(input("Nota 2 >> "))
n3 = float(input("Nota 3 >> "))

media = (n1 + n2 + n3) / 3
print(f"Media: {media:.2f}")

# Desafio: sem parenteses, so o n3 seria dividido por 3 (precedencia),
# somando n1 + n2 + (n3/3), o que NAO e a media.
