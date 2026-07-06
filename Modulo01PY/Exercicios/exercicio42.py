# ============================================================
# EXERCICIO 42 - "O RADAR DE INTRUSO"
# Base: Aula 42 (break e continue)
# ------------------------------------------------------------
# Contexto:
#   Nem sempre queremos que o laco rode ate o fim. As vezes achamos
#   o que procuravamos (break) ou queremos pular um caso especifico
#   (continue). Sao os "freios e desvios" dos lacos.
#
# Sua missao:
#   Um radar varre os numeros de 1 a 20. Regras:
#     - se o numero for MULTIPLO de 3, o radar IGNORA (continue)
#     - se o numero for 17 (o "intruso"), o radar dispara o alarme,
#       imprime "INTRUSO DETECTADO!" e PARA a varredura (break)
#     - os demais numeros sao apenas impressos.
#
# Regras (validando a Aula 42):
#   - Use continue e break corretamente dentro de um for.
# ============================================================

# --- GABARITO DO PROFESSOR ---
for numero in range(1, 21):
    if numero % 3 == 0:
        continue                     # ignora multiplos de 3
    if numero == 17:
        print("INTRUSO DETECTADO!")
        break                        # para a varredura
    print("Verificando:", numero)
