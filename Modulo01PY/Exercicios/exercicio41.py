# ============================================================
# EXERCICIO 41 - "A BOMBA-RELOGIO (DO BEM)"
# Base: Aula 41 (for com sleep: pausa no tempo)
# ------------------------------------------------------------
# Contexto:
#   Ate agora tudo acontecia num piscar de olhos. Com o sleep()
#   podemos fazer o programa ESPERAR, criando suspense, cronometros
#   e animacoes simples.
#
# Sua missao:
#   Crie um cronometro dramatico: conte de 5 ate 1, esperando 1
#   segundo entre cada numero, e no final imprima "TEMPO ESGOTADO!".
#
# Regras (validando a Aula 41):
#   - Importe sleep de time e use dentro de um for decrescente.
# ============================================================

# --- GABARITO DO PROFESSOR ---
from time import sleep

for segundos in range(5, 0, -1):
    print(segundos)
    sleep(1)

print("TEMPO ESGOTADO!")
