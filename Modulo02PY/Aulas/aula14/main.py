# ============================================================
# MODULO 02 - AULA 14: main.py (CRUD com json)
# ------------------------------------------------------------
# Mesmo menu de hotel da aula 13, mas agora os dados sao salvos
# de forma estruturada e segura no arquivo hospedes.json.
# ============================================================

from controller import create, read, update, delete

def menu():
    opcao = -1
    while opcao != 0:
        print("\n===== HOTEL PYTHON (JSON) =====")
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
                novos_dados = {
                    "nome": input("Novo nome >> "),
                    "idade": input("Nova idade >> "),
                    "telefone": input("Novo telefone >> "),
                }
                if update(nome, novos_dados):
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
