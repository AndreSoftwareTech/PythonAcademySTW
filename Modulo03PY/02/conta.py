class Conta:
    titular : str
    numero : int
    saldo : float
    limite : float

    def teste(self):
        print(self.titular)

    def __str__(self):
        return f' { self.titular } - {self.numero} - {self.saldo} - {self.limite} '