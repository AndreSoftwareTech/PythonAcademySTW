nome = input("Digite seu nome >> ")
cor = input("Digite sua cor >> ")
sexo = input("Digite seu sexo >>")
tamanho = float(input("Digite sua altura >>"))
peso = float(input("Digite seu peso >>"))
nacionalidade = input("Digite onde voce nasceu")
idioma = input("Digite seu idioma principal >> ")

pessoa = {
    "Nome": nome, 
    "Cor": cor,
    "Sexo": sexo,
    "Tamanho": tamanho,
    "Peso": peso,
    "Pais": nacionalidade,
    "Idioma": idioma
    }

cond = int(input(
''' Digite o numero que representa a caracterisca que deseja saber
\n1- Nome
\n2- Cor
\n3- Sexo
\n4- Tamanho
\n5- Peso
\n6- Pais
\n7- Idioma
\n8- Completo
\n >>>>> '''
))

if cond == 1:
    print(f" O Nome que voce desejava saber é {pessoa['Nome']}")

elif cond == 2:
    print(f" A COr que voce desejava saber é {pessoa['Cor']}")

elif cond == 3:
    print(f" A Sexo que voce desejava saber é {pessoa['Sexo']}")

elif cond == 4:
    print(f" A altura que voce desejava saber é {pessoa['Tamanho']}")

elif cond == 5:
    print(f" o peso que voce desejava saber é {pessoa['Peso']}")

elif cond == 6:
    print(f" o pais que voce desejava saber é { pessoa [ 'Pais' ] } ")

elif cond == 7:
    print(f" O idioma que voce desejava saber é {pessoa['Idioma']}")

elif cond == 8:
    print(pessoa)