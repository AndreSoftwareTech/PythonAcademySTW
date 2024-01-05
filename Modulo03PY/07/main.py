from conta import Conta

conta = Conta(input("Digite seu Nome:> "), 
float(input("Digite seu :> ")),
#atributo Saldo Conta
float(input("Digite seu Saldo Inicial:> ")),
#atributo limite Conta
float(input("Digite o limite da sua Conta:> ")))
conta.limite = 3500
print(conta)
