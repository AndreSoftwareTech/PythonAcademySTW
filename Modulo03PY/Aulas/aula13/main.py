# ============================================================
# MODULO 03 - AULA 13: MAIN (menu CRUD de clientes)
# ============================================================

from cliente import Cliente
from controller import cadastrar, listar, buscar_por_titular, remover

def menu():
    opcao = -1
    while opcao != 0:
        print("\n=== BANCO - CLIENTES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar por titular")
        print("4 - Remover")
        print("0 - Sair")
        opcao = int(input("Opcao >> "))

        if opcao == 1:
            c = Cliente(
                input("Titular >> "),
                input("Numero >> "),
                input("Saldo >> "),
                input("Limite >> "),
            )
            cadastrar(c)
            print("Cliente cadastrado!")
        elif opcao == 2:
            listar()
        elif opcao == 3:
            nome = input("Titular >> ")
            cliente = buscar_por_titular(nome)
            print(cliente if cliente else "Nao encontrado.")
        elif opcao == 4:
            remover(input("Titular a remover >> "))
            print("Removido (se existia).")
        elif opcao == 0:
            print("Ate logo!")

if __name__ == "__main__":
    menu()
