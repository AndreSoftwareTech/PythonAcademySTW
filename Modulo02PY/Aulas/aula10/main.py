# ============================================================
# MODULO 02 - AULA 10: main.py (menu do CRUD em memoria)
# ------------------------------------------------------------
# Importa as funcoes de tarefas.py e oferece um menu ao usuario.
# ============================================================

from tarefas import adicionar, listar, remover, quantidade

def menu():
    opcao = -1
    while opcao != 0:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa (por indice)")
        print("4 - Quantidade de tarefas")
        print("0 - Sair")
        opcao = int(input("Escolha uma opcao >> "))

        if opcao == 1:
            print(adicionar(input("Digite a tarefa >> ")))
        elif opcao == 2:
            print("Tarefas:", listar())
        elif opcao == 3:
            print(remover(int(input("Indice da tarefa >> "))))
        elif opcao == 4:
            print("Total de tarefas:", quantidade())
        elif opcao == 0:
            print("Ate logo!")
        else:
            print("Opcao invalida.")

menu()
