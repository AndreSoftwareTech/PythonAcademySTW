# ============================================================
# EXERCICIO 23 - "APROVADO, RECUPERACAO OU REPROVADO?"
# Base: Aula 23 (Decisao com media de notas)
# ------------------------------------------------------------
# Contexto:
#   Vamos unir tudo o que voce ja sabe: entrada, conversao, calculo
#   de media e decisao. Este e o tipico problema de "boletim".
#
# Sua missao:
#   Peca 2 notas, calcule a media e informe a situacao:
#     - media >= 7            -> "Aprovado"
#     - media >= 5 e menor 7  -> "Recuperacao"
#     - media < 5             -> "Reprovado"
#
# Regras (validando a Aula 23):
#   - Calcule a media com parenteses e decida com if/elif/else.
# ============================================================

# --- GABARITO DO PROFESSOR ---
n1 = float(input("Primeira nota >> "))
n2 = float(input("Segunda nota >> "))

media = (n1 + n2) / 2

if media >= 7:
    print(f"Media {media:.1f} - Aprovado")
elif media >= 5:
    print(f"Media {media:.1f} - Recuperacao")
else:
    print(f"Media {media:.1f} - Reprovado")
