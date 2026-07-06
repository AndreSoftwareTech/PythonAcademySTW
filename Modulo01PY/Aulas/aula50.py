# ============================================================
# AULA 50 - TRATAMENTO DE ERROS (try / except)
# Objetivo: evitar que o programa QUEBRE quando algo da errado.
# ============================================================

# O codigo "arriscado" fica dentro do try.
# Se der erro, o Python pula para o except correspondente.
try:
    numero = int(input("Digite um numero inteiro >> "))
    resultado = 10 / numero
    print(f"10 dividido por {numero} = {resultado}")

except ValueError:
    print("Erro: voce nao digitou um numero inteiro valido.")

except ZeroDivisionError:
    print("Erro: nao e possivel dividir por zero.")

print("O programa continuou funcionando, mesmo que tenha dado erro.")
