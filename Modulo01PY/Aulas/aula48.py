cond = "sim"

while cond.lower() == "sim":
    var = int(input("Digite um número qualquer para teste: "))
    print(f"Número qualquer sendo impresso: {var}")

    cond = input("Você deseja continuar?\nDigite 'sim' para continuar ou 'nao' para sair: ")

print("Fora do While")

