# ============================================================
# EXERCICIO 01 - "A FABRICA DE BANNERS"
# Base: Aula 01 (Definindo e chamando funcoes)
# ------------------------------------------------------------
# Contexto:
#   Voce vai criar uma "maquina" reaproveitavel: uma funcao que
#   desenha um banner de abertura. Depois de pronta, e so chamar.
#
# Sua missao:
#   1) Crie uma funcao chamada 'banner' que imprima 3 linhas:
#      uma linha de simbolos, um titulo, outra linha de simbolos.
#   2) Chame a funcao DUAS vezes seguidas.
#
# Regras (validando a Aula 01):
#   - O texto do banner deve estar DENTRO da funcao.
#   - A funcao so pode aparecer na tela quando for CHAMADA.
# ============================================================

# --- GABARITO DO PROFESSOR ---
def banner():
    print("=" * 30)
    print("      PYTHON ACADEMY")
    print("=" * 30)

banner()
banner()
