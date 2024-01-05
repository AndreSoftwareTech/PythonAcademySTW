from conta import Conta

class PessoaJuridica(Conta):
    __segundo_titular = " "
   
    def __init__(self, titular, cnpj, saldoInicial):
        super().__init__("3060", "Pessoa Juridica")
        self.__titular = titular
        self.__cnpj = cnpj
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
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj__cnpj):
        self.__cnpj = cnpj__cnpj

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
        return  f' {super().__str__()} {self.titular} {self.cnpj} {self.saldoInicial}' 