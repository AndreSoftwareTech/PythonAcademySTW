from crud import criar_Pessoa, criar_apartamento, criar_relatorio

def menu():

    var = 1
    while var !=0:
        
        print("Digite qual das opcoes deseja cadastrar")
        esc = int(input("1- Pessoa\n2- Quarto \n 3 Criar Relatorio \n >>> "))
        match esc:
            case 1:
                pessoa = {}
                pessoa["nome"]=str(input("Digite seu nome:> "))
                pessoa["cpf"]=int(input("Digite seu cpf:> "))
                pessoa["idade"]=int(input("Digite sua idade:> "))
                pessoa["telefone"]=int(input("Digite seu telefone:> "))
                criar_Pessoa(pessoa)
                

            case 2: 
                apartamento = {}
                apartamento["Numero"]=str(input("Digite O Numero do apartamento:> "))
                apartamento["Andar"]=str(input("Digite O Andar:> "))
                apartamento["Banheiro"]=int(input("Digite Quantos banheiros:> "))
                apartamento["Quartos"]=int(input("Digite quantos quartos :> "))
                apartamento["Comodos"]=int(input("Digite quantos comodos:> "))
                criar_apartamento(apartamento)
                

            case 3 :
                criar_relatorio()
            
        var = int(input("Digite o numero \n 0 - Sair\n 1 - Continuar \n >> "))

menu()