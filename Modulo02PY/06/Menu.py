from Controller import saudacao, Create, relatorioHospedes, realotorioHospede, FazerCheckout, upcliente

def menu():
    menu = 1
    while menu != 0:
        saudacao()
        print("Você deseja cadastrar uma pessoa?")
        var = int(input("Digite 1 para cadastrar,\n 2 para relatório de todos os hóspedes,\n 3 para relatório de um hóspede,\n 4 para deletar um hóspede,\n 5 para atualizar informações de um hóspede: "))

        match var:
            case 1:
                pessoa = {}
                validacao = False
                while not validacao:
                    nome = input("Digite o seu nome: ").capitalize()
                    sobrenome = input("Digite seu sobrenome: ").capitalize()
                    idade = input("Digite sua idade: ")
                    
                    if nome.strip() == "" or sobrenome.strip() == "":
                        print("Erro: Nome e sobrenome não podem estar vazios.")
                    elif not idade.isdigit():
                        print("Erro: Idade inválida. Digite um número válido.")
                    else:
                        pessoa["Nome"] = nome
                        pessoa["Sobrenome"] = sobrenome
                        pessoa["Idade"] = int(idade)
                        pessoa["Telefone"] = input("Digite seu telefone: ")
                        validacao = True
                        
                Create(pessoa)

            case 2:
                relatorioHospedes()

            case 3:
                pessoa = input("Digite o nome do hóspede que deseja pesquisar: ").capitalize()
                realotorioHospede(pessoa)

            case 4:
                pessoa = input("Digite o nome do hóspede que deseja deletar: ").capitalize()
                FazerCheckout(pessoa)

            case 5:
                pessoa = input("Digite o nome do hóspede que deseja atualizar as informações: ").capitalize()
                upcliente(pessoa)

            case _:
                print("Opção inválida. Tente novamente.")

        menu = int(input("Você deseja sair?\nDigite 0 para sair\nDigite 1 para continuar: "))

menu()
