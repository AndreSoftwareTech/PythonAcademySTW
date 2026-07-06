# ============================================================
# AULA 42 - break e continue
# Objetivo: controlar o andamento de um laco de repeticao.
# ============================================================

# break -> INTERROMPE o laco imediatamente
for numero in range(1, 11):
    if numero == 5:
        print("Encontrei o 5, parando o laco!")
        break
    print(numero)

print("-" * 20)

# continue -> PULA para a proxima repeticao, ignorando o resto do bloco
for numero in range(1, 11):
    if numero % 2 == 0:
        continue           # para os pares, nao chega no print abaixo
    print("Impar:", numero)
