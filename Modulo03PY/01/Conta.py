class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        print(f"Imprimindo variavel de referencia {self}")
        self.numero : int
        self.titular : str
        self.cpf : str
        self.saldo :float
        self.limite :float
