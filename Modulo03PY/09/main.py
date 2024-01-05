from controller import cadastrar_cliente, listar_clientes, buscar_cliente, atualizar_cliente, excluir_cliente
from cliente import Cliente

def menu():
    opcao = -1
    while opcao != 0:
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar cliente")
        print("5 - Excluir cliente")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titular = input("Digite o nome do cliente: ")
            numero = input("Digite o número do cliente: ")
            saldo = float(input("Digite o saldo do cliente: "))
            limite = float(input("Digite o limite do cliente: "))
            cliente = Cliente(titular, numero, saldo, limite)
            cadastrar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao == 2:
            print("Lista de clientes:")
            listar_clientes()
        elif opcao == 3:
            nome = input("Digite o nome do cliente a ser buscado: ")
            buscar_cliente(nome)
        elif opcao == 4:
            nome = input("Digite o nome do cliente a ser atualizado: ")
            atributo = input("Digite o atributo a ser atualizado: ")
            novo_valor = input("Digite o novo valor: ")
            atualizar_cliente(nome, atributo, novo_valor)
            print("Cliente atualizado com sucesso!")
        elif opcao == 5:
            nome = input("Digite o nome do cliente a ser excluído: ")
            excluir_cliente(nome)
            print("Cliente excluído com sucesso!")
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida!")

menu()
