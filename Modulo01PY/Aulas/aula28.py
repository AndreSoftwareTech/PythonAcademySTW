from random import shuffle, choice

n1 = str(input("DIgite um nome >> "))
n2 = str(input("DIgite um nome >> "))
n3 = str(input("DIgite um nome >> "))
n4 = str(input("DIgite um nome >> "))
n5 = str(input("DIgite um nome >> "))
n6 = str(input("DIgite um nome >> "))
n7 = str(input("DIgite um nome >> "))


#Array
lista = [ n1, n2, n3, n4, n5, n6, n7]
shuffle(lista)
sorteio = choice(lista)
print(sorteio)