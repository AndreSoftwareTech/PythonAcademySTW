from cliente import Cliente

def cadastrar_cliente(cliente):
    with open('clientes.txt', 'a') as arquivo:
        arquivo.write(f"{cliente['Nome']},{cliente['Sobrenome']},{cliente['Idade']},{cliente['Telefone']}\n")

def listar_clientes():
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            cliente = {
                'Nome': dados[0],
                'Sobrenome': dados[1],
                'Idade': int(dados[2]),
                'Telefone': dados[3]
            }
            print(cliente)

def buscar_cliente(nome):
    encontrado = False
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            cliente = {
                'Nome': dados[0],
                'Sobrenome': dados[1],
                'Idade': int(dados[2]),
                'Telefone': dados[3]
            }
            if cliente['Nome'].lower() == nome.lower():
                print(cliente)
                encontrado = True
                break
    if not encontrado:
        print("Cliente não encontrado")

def atualizar_cliente(nome, atributo, novo_valor):
    clientes_atualizados = []
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            cliente = {
                'Nome': dados[0],
                'Sobrenome': dados[1],
                'Idade': int(dados[2]),
                'Telefone': dados[3]
            }
            if cliente['Nome'].lower() == nome.lower():
                cliente[atributo] = novo_valor
            clientes_atualizados.append(cliente)
    
    with open('clientes.txt', 'w') as arquivo:
        for cliente in clientes_atualizados:
            arquivo.write(f"{cliente['Nome']},{cliente['Sobrenome']},{cliente['Idade']},{cliente['Telefone']}\n")

def excluir_cliente(nome):
    clientes_restantes = []
    with open('clientes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            cliente = {
                'Nome': dados[0],
                'Sobrenome': dados[1],
                'Idade': int(dados[2]),
                'Telefone': dados[3]
            }
            if cliente['Nome'].lower() != nome.lower():
                clientes_restantes.append(cliente)
    
    with open('clientes.txt', 'w') as arquivo:
        for cliente in clientes_restantes:
            arquivo.write(f"{cliente['Nome']},{cliente['Sobrenome']},{cliente['Idade']},{cliente['Telefone']}\n")
