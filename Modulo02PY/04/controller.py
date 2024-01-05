from datetime import datetime

def saudacao():
    hora = datetime.now(tz=None)

    if hora.hour >= 5 and hora.hour <13:
        print("Bom dia")
    if hora.hour >=13 and hora.hour <18:
        print("Boa tarde")
    else:
        print("Boa Noite")


def checkin(cliente):
    with open('hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")

def relatorio():
    with open('hotel.txt', 'r') as arquivo:
        print(arquivo.read())

def relatorioCliente(clienteFind):
        index = 0
        flag = 0
        arquivo = open('hotel.txt', 'r')

        for line in arquivo:
            index += 1

            if clienteFind == eval(line)['nome']:
                print(line)
                flag = 1

        if flag == 0:
            print("CLiente Nao encontrado ")
            
def update(cliente_find):
    flag = False  # Variável para indicar se o cliente foi encontrado

    with open('hotel.txt', 'r') as arquivo:
        lines = arquivo.readlines()

    with open('hotel.txt', 'w') as arquivo:
        for line in lines:
            if cliente_find in line:
                novo_nome = input("Digite o novo nome: ")
                nova_idade = input("Digite a nova idade: ")
                nova_linha = f"{{'nome': '{novo_nome}', 'idade': '{nova_idade}'}}\n"
                arquivo.write(nova_linha)
                flag = True  # Cliente encontrado e atualizado
            else:
                arquivo.write(line)

    if flag:
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado")

def delete(cliente_find):
    flag = False  # Variável para indicar se o cliente foi encontrado

    with open('hotel.txt', 'r') as arquivo:
        lines = arquivo.readlines()

    with open('hotel.txt', 'w') as arquivo:
        for line in lines:
            if cliente_find not in line:
                arquivo.write(line)
            else:
                flag = True  # Cliente encontrado e excluído

    if flag:
        print("Cliente deletado com sucesso!")
    else:
        print("Cliente não encontrado")


def main():
    cliente_find = input("Informe o nome do cliente a ser deletado: ")
    delete(cliente_find)


if __name__ == "__main__":
    main()

