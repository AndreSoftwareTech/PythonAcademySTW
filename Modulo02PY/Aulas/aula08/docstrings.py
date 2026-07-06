# ============================================================
# MODULO 02 - AULA 08: DOCSTRINGS - DOCUMENTANDO FUNCOES  [NOVO]
# ------------------------------------------------------------
# Objetivo: aprender a DOCUMENTAR uma funcao com uma docstring:
# um texto entre aspas triplas na PRIMEIRA linha da funcao,
# explicando o que ela faz, o que recebe e o que devolve.
# ============================================================

def calcular_imc(peso, altura):
    """Calcula o IMC (Indice de Massa Corporal).

    peso: massa em quilos (float)
    altura: altura em metros (float)
    retorna: o valor do IMC (float)
    """
    return peso / (altura ** 2)

imc = calcular_imc(80, 1.80)
print(f"IMC calculado: {imc:.2f}")

# A docstring fica acessivel via .__doc__ (ou pela funcao help()).
print("--- Documentacao da funcao ---")
print(calcular_imc.__doc__)
