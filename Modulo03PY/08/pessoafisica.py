from conta import Conta

class PessoaFisica(Conta):
    __segundo_titular = " "
   
    def __init__(self, titular, cpf, saldoInicial):
        super().__init__("4545", "Pessoa Fisica")
        self.__titular = titular
        self.__cpf = cpf
        self.__saldoInicial = saldoInicial
    
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def saldoInicial(self):
        return self.__saldoInicial
    @saldoInicial.setter
    def saldoInicial(self, saldoInicial):
        if saldoInicial > 0:
            self.__saldoInicial = saldoInicial
        else:
            print("Valor invalido")
            
    def __str__(self):
        return  f' {super().__str__()} {self.titular} {self.cpf} {self.saldoInicial}' 