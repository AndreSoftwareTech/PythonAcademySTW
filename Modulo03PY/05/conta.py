class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular : str= titular
        self.numero : int = numero
        self.saldo : float= saldo
        self.limite : float = limite

    def extrato(self):
        print("O numero da conta {} do {} tem o saldo de {}".format(self.numero, self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
        