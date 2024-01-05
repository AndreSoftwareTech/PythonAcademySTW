import random

n1 = str(input("DIgite um nome >> "))
n2 = str(input("DIgite um nome >> "))
n3 = str(input("DIgite um nome >> "))
n4 = str(input("DIgite um nome >> "))

#Array
lista = [ n1, n2, n3, n4 ]
print(lista)
sorteio = random.choice(lista)

print(sorteio)