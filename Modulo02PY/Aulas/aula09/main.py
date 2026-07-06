# ============================================================
# MODULO 02 - AULA 09: main.py (ponto de entrada)
# ------------------------------------------------------------
# Aqui IMPORTAMOS as funcoes do arquivo calculadora.py e
# montamos o menu. Execute este arquivo:  python main.py
# ============================================================

from calculadora import soma, subtracao, multiplicacao, divisao

def menu():
    opcao = -1
    while opcao != 0:
        print("\n1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        opcao = int(input("Escolha uma opcao >> "))

        if opcao == 0:
            print("Encerrando a calculadora...")
            continue

        if opcao not in (1, 2, 3, 4):
            print("Opcao invalida.")
            continue

        a = int(input("Primeiro numero >> "))
        b = int(input("Segundo numero >> "))

        if opcao == 1:
            print("Resultado:", soma(a, b))
        elif opcao == 2:
            print("Resultado:", subtracao(a, b))
        elif opcao == 3:
            print("Resultado:", multiplicacao(a, b))
        elif opcao == 4:
            print("Resultado:", divisao(a, b))

menu()
