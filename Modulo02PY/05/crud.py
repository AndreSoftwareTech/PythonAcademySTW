def criar_Pessoa(cliente):
    with open('cliente.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")

def criar_apartamento(cliente):
    with open('apartamento.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")



def criar_relatorio():
    pessoas = []
    apartamentos = []

    # Solicita o nome do cliente a ser pesquisado
    cliente_find = input("Digite o nome do cliente a ser pesquisado: ")

    # Lê o arquivo de pessoas e armazena os dados em uma lista
    with open('cliente.txt', 'r') as arquivo_pessoas:
        for linha in arquivo_pessoas:
            pessoa = eval(linha.strip())
            pessoas.append(pessoa)

    # Procura o cliente especificado
    cliente_encontrado = None
    for pessoa in pessoas:
        if pessoa['nome'] == cliente_find:
            cliente_encontrado = pessoa
            break

    if cliente_encontrado is None:
        print("Cliente não encontrado!")
        return


    # Solicita o número do apartamento a ser pesquisado
    numero_apartamento = input("Digite o número do apartamento a ser pesquisado: ")
    # Lê o arquivo de apartamentos e armazena os dados em uma lista
    with open('apartamento.txt', 'r') as arquivo_apartamentos:
        for linha in arquivo_apartamentos:
            apartamento = eval(linha.strip())
            apartamentos.append(apartamento)

    # Procura o apartamento especificado
    apartamento_encontrado = None
    for apartamento in apartamentos:
        if apartamento['Numero'] == numero_apartamento:
            apartamento_encontrado = apartamento
            break

    if apartamento_encontrado is None:
        print("Apartamento não encontrado!")
        return

    # Cria um terceiro arquivo e escreve as informações combinadas de pessoa e apartamento
    with open('relatorio.txt', 'w') as arquivo_relatorio:
        relatorio = {
            'Nome': cliente_encontrado['nome'],
            'CPF': cliente_encontrado['cpf'],
            'Apartamento': apartamento_encontrado['Numero'],
            'Andar': apartamento_encontrado['Andar']
        }
        arquivo_relatorio.write(str(relatorio) + '\n')

    print("Relatório criado com sucesso!")

# Chamada da função para criar o relatório

