from aula05 import soma, sub, multiplicacao, divisao

def menu():

    var = 1
    
    while var != 0:

        print("Digite Qual operacao Matemtica Voce deseja fazer")
        
        rato = int(input('''
        Digite O numero Para Operacao selecionada
        \n1 soma
        \n2 subtracao
        \n3 multiplicacao
        \n4 divisao
        '''))

        match rato:

            case 1:
                n1 = int(input("Digite o primeiro numero >> "))
                n2 = int(input("Digite o segundo numero >> "))

                print(soma(n1, n2))

            case 2: 
                n1 = int(input("Digite o primeiro numero >> "))
                n2 = int(input("Digite o segundo numero >> "))
                print(sub(n1, n2))

            case 3:
                n1 = int(input("Digite o primeiro numero >> "))
                n2 = int(input("Digite o segundo numero >> "))
                print(multiplicacao(n1, n2))

            case 4:
                n1 = int(input("Digite o primeiro numero >> "))
                n2 = int(input("Digite o segundo numero >> "))
                print(divisao(n1, n2))
 
        var = int(input("Digite 0 para sair ou digite 1 para continuar\n >>"))

print("Voce Finalizou seus Calculos")
     