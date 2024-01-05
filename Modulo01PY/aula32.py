numero = int(input("Digite um numero referente a tabuada que deseja saber >>"))

for c in range(1, 21):
    print("{} X {} = {}".format( numero, c, numero*c))