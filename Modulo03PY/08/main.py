from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica


def menu():
    cond = 0 
    while cond == 0:
        
        var : int = int(input("Qual conta voce deseja acessar \n 1Pessoa Fisica\n 2Pessoa Juridica"))
       
        match var:
                case 1:
                        pf = PessoaFisica(
                        input("Digite o nome Do Titular >>"), 
                        input("Digite  o cpf do titular >>  "), 
                        float(input("DIgite o saldo inicial >>"))
                        )
                        print(pf)
                        pf.saldoInicial = float(input("Digite o valor incial>> "))
                        print(pf)

                        var = int(input("Voce deseja cadastrar um segundo titular \n1- sim \n2- nao"))

                        if var == 1:
                                pf.segundo_titular = input("Digite o segundo titular >>")
                                print(pf)
                case 2:
                        pj = PessoaJuridica(
                        input("Digite o nome Do Titular >>"), 
                        input("Digite  o cnpj do titular >>  "), 
                        float(input("DIgite o saldo inicial >>"))
                        )

                        print(pj)
                        pj.saldoInicial = float(input("Digite o valor incial>> "))
                        print(pj)

                        var = int(input("Voce deseja cadastrar um segundo titular \n1- sim \n2- nao"))

                        if var == 1:
                                pj.segundo_titular = input("Digite o segundo titular >>")
                                print(pj)
        cond = int(input("Digite 0 para continuar ou 1 para sair"))

menu()
