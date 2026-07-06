# ============================================================
# EXERCICIO 21 - "O CLASSIFICADOR DE TEMPERATURA"
# Base: Aula 21 (Estrutura condicional if / elif / else)
# ------------------------------------------------------------
# Contexto:
#   Agora o programa comeca a TOMAR DECISOES. Dependendo da situacao,
#   ele segue por um caminho ou por outro.
#
# Sua missao:
#   Pergunte a temperatura (em graus) e classifique o clima:
#     - abaixo de 15  -> "Frio, pegue um casaco"
#     - de 15 a 25    -> "Agradavel"
#     - acima de 25   -> "Calor, beba agua"
#
# Regras (validando a Aula 21):
#   - Use if, elif e else (um unico bloco de decisao).
# ============================================================

# --- GABARITO DO PROFESSOR ---
temperatura = float(input("Qual a temperatura agora? >> "))

if temperatura < 15:
    print("Frio, pegue um casaco.")
elif temperatura <= 25:
    print("Agradavel.")
else:
    print("Calor, beba agua.")
