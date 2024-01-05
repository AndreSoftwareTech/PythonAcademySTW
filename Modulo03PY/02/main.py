from conta import Conta


def teste(teste):
    print(teste)

usar = Conta()

usar.numero = 123
usar.titular = "Arcides"
usar.saldo = 1500.00
usar.limite = 3000.00

teste(usar.titular)