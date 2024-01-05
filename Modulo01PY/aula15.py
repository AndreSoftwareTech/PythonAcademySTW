# conceitos de importacao otimizada

# Raiz quadrada
from math import sqrt

num = int(input("Digite o numero que voce deseja saber a raiz >>"))

raiz = sqrt(num)

print(raiz)

# Resto da divisao 7 e 3
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resto = num1 % num2

print("O resto da divisão entre", num1, "e", num2, "é", resto)

# calculando Resto da divisao diretamente
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resto = num1 - (num1 // num2) * num2

print("O resto da divisão é:", resto)

