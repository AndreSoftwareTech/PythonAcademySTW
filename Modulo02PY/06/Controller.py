from datetime import datetime

def saudacao():
    hora = datetime.now(tz=None)
    if hora.hour >= 5 and hora.hour < 13:
        print("Bom Dia")
    elif hora.hour >= 13 and hora.hour < 18:
        print("Boa Tarde")
    else:
        print("Boa Noite seus 17/05")
    

def Create(Abacate):
    with open('hotel.txt', 'a') as arquivo:
        arquivo.write(str(Abacate)+'\n')

def relatorioHospedes():
    with open('hotel.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        if conteudo:
            print(conteudo)
        else:
            print("Não há hóspedes cadastrados.")


def realotorioHospede(Cliente):
    index = 0
    flag= 0
    arquivo = open("hotel.txt", 'r')
    for line in arquivo:
        index += 1
        if Cliente == eval(line)["Nome"]:
            print(line)
            flag = 1
    if flag == 0:
        print("Cliente não encontrado")

def upcliente(cliente):
    encontrado = False
    linhas_atualizadas = []
    
    with open("hotel.txt", "r") as arquivo:
        for linha in arquivo:
            hospede = eval(linha)
            if hospede["Nome"] == cliente:
                print("Dados atuais do cliente:")
                print(linha)
                print("Digite as novas informações do cliente:")
                nome = input("Digite o novo nome do cliente: ").capitalize()
                sobrenome = input("Digite o novo sobrenome do cliente: ").capitalize()
                idade = int(input("Digite a nova idade do cliente: "))
                telefone = input("Digite o novo telefone do cliente: ")
                hospede["Nome"] = nome
                hospede["Sobrenome"] = sobrenome
                hospede["Idade"] = idade
                hospede["Telefone"] = telefone
                encontrado = True
            
            linhas_atualizadas.append(str(hospede))
    
    if encontrado:
        with open("hotel.txt", "w") as arquivo:
            arquivo.write("\n".join(linhas_atualizadas))
        print("Cliente atualizado")
    else:
        print("Cliente não encontrado")

def FazerCheckout(cliente):
    with open("hotel.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    encontrado = False
    with open("hotel.txt", "w") as arquivo:
        for linha in linhas:
            if cliente not in linha:
                arquivo.write(linha)
            else:
                encontrado = True

    if encontrado == True:
        print("Pessoa deletada")
    else:
        print("Cliente não encontrado")
