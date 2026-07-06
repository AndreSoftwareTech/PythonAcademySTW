# ============================================================
# MODULO 02 - AULA 13: main.py (menu do CRUD em arquivo)
# ------------------------------------------------------------
# Usa o match/case para montar o menu do hotel. Todos os dados
# ficam salvos no arquivo hotel.txt.
# ============================================================

from controller import saudacao, create, read, update, delete

def menu():
    saudacao()
    opcao = -1
    while opcao != 0:
        print("\n===== HOTEL PYTHON =====")
        print("1 - Cadastrar hospede")
        print("2 - Listar hospedes")
        print("3 - Atualizar hospede")
        print("4 - Remover hospede")
        print("0 - Sair")
        opcao = int(input("Escolha uma opcao >> "))

        match opcao:
            case 1:
                nome = input("Nome >> ")
                idade = input("Idade >> ")
                telefone = input("Telefone >> ")
                create(nome, idade, telefone)
                print("Hospede cadastrado!")
            case 2:
                for hospede in read():
                    print(hospede)
            case 3:
                nome = input("Nome do hospede a atualizar >> ")
                novo_nome = input("Novo nome >> ")
                nova_idade = input("Nova idade >> ")
                novo_telefone = input("Novo telefone >> ")
                if update(nome, novo_nome, nova_idade, novo_telefone):
                    print("Hospede atualizado!")
                else:
                    print("Hospede nao encontrado.")
            case 4:
                nome = input("Nome do hospede a remover >> ")
                if delete(nome):
                    print("Hospede removido!")
                else:
                    print("Hospede nao encontrado.")
            case 0:
                print("Encerrando...")
            case _:
                print("Opcao invalida.")

menu()
