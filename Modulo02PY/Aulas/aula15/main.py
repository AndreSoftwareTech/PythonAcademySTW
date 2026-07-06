# ============================================================
# MODULO 02 - AULA 15: main.py (projeto final do modulo)
# ------------------------------------------------------------
# Menu para cadastrar pessoas e apartamentos e, por fim, gerar
# um relatorio que RELACIONA uma pessoa com um apartamento.
# ============================================================

from controller import criar_pessoa, criar_apartamento, gerar_relatorio

def menu():
    opcao = -1
    while opcao != 0:
        print("\n===== HOTEL: CADASTRO E RELATORIO =====")
        print("1 - Cadastrar pessoa")
        print("2 - Cadastrar apartamento")
        print("3 - Gerar relatorio (pessoa + apartamento)")
        print("0 - Sair")
        opcao = int(input("Escolha uma opcao >> "))

        match opcao:
            case 1:
                nome = input("Nome >> ")
                cpf = input("CPF >> ")
                criar_pessoa(nome, cpf)
                print("Pessoa cadastrada!")
            case 2:
                numero = input("Numero do apartamento >> ")
                andar = input("Andar >> ")
                criar_apartamento(numero, andar)
                print("Apartamento cadastrado!")
            case 3:
                cpf = input("CPF da pessoa >> ")
                numero = input("Numero do apartamento >> ")
                print(gerar_relatorio(cpf, numero))
            case 0:
                print("Encerrando...")
            case _:
                print("Opcao invalida.")

menu()
