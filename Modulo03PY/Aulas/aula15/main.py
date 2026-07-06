# ============================================================
# MAIN: menu do mini-MVC (view + controller + model)
# Ponte de saida para o Modulo 04 (camadas + banco de dados).
# ============================================================

from controller.aluno_controller import cadastrar, listar, media_geral

def menu():
    opcao = -1
    while opcao != 0:
        print("\n=== ACADEMIA - MINI MVC ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Media geral")
        print("0 - Sair")
        opcao = int(input("Opcao >> "))

        if opcao == 1:
            print(cadastrar(input("Nome >> "), input("Nota >> ")))
        elif opcao == 2:
            alunos = listar()
            if not alunos:
                print("Nenhum aluno.")
            for a in alunos:
                print(a)
        elif opcao == 3:
            print(media_geral())
        elif opcao == 0:
            print("Encerrando...")

if __name__ == "__main__":
    menu()
