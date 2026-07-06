# ============================================================
# AULA 43 - ACUMULADORES E CONTADORES
# Objetivo: somar e contar valores dentro de um laco de repeticao.
# ============================================================

quantidade = int(input("Quantas notas voce vai digitar? >> "))

soma = 0        # ACUMULADOR: vai somando as notas (comeca em 0)
contador = 0    # CONTADOR: conta quantas notas ja foram digitadas

for c in range(quantidade):
    nota = float(input(f"Digite a nota {c + 1} >> "))
    soma = soma + nota          # acumula o valor da nota
    contador = contador + 1     # conta mais uma nota

media = soma / contador
print(f"Soma das notas: {soma}")
print(f"Quantidade digitada: {contador}")
print(f"Media: {media:.2f}")
