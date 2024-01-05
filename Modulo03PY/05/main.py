from conta import Conta
v = "*"*20

print(v, "Menu conta 1", v)

conta = Conta(
            input("Digite Seu Nome >>"),
            int(input("Digite O numero da conta >>")),
            float(input("Digite o saldo da sua conta >>")),
            float(input("Digite o limite >>"))
              )

print(v,"Extrato conta 1", v)

conta.extrato()

conta.sacar(float(input("Digite o valor do saque >>")))
print(v,"Extrato Saque conta 1", v)
conta.extrato()

conta.depositar(float(input("Digite o valor do Deposito >>")))
print(v,"Extrato Deposito conta 1", v)
conta.extrato()

conta1 = Conta(
            input("Digite Seu Nome >>"),
            int(input("Digite O numero da conta >>")),
            float(input("Digite o saldo da sua conta >>")),
            float(input("Digite o limite >>"))
              )

print(v,"Extrato conta 2", v)

conta1.extrato()

conta1.sacar(float(input("Digite o valor do saque >>")))
print(v,"Extrato Saque conta 2", v)
conta1.extrato()

conta1.depositar(float(input("Digite o valor do Deposito >>")))
print(v,"Extrato Deposito conta 2", v)
conta1.extrato()

print(v,"Extrato transferencia", v)

conta1.transferir(float(input("Digite o valor da transferencia")), conta,  conta1)
print(v,"Extrato transeferencia conta 2", v)
conta1.extrato()

print(v,"Extrato transferencia conta 1", v)
conta.extrato()