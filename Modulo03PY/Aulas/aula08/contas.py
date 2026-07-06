# ============================================================
# MODULO 03 - AULA 08: HERANCA E super()
# ------------------------------------------------------------
# Objetivo: uma classe FILHA herda atributos e metodos da PAI.
# super() chama o construtor da classe pai. Aqui ContaBancaria e
# a base; PessoaFisica e PessoaJuridica sao especializacoes.
# ============================================================

class ContaBancaria:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        return f"Conta {self.numero} ({self.tipo})"

class PessoaFisica(ContaBancaria):
    def __init__(self, numero, titular, cpf, saldo):
        super().__init__(numero, "Pessoa Fisica")
        self.titular = titular
        self.cpf = cpf
        self.saldo = float(saldo)

    def __str__(self):
        return f"{super().__str__()} | {self.titular} | CPF {self.cpf} | R$ {self.saldo:.2f}"

class PessoaJuridica(ContaBancaria):
    def __init__(self, numero, razao_social, cnpj, saldo):
        super().__init__(numero, "Pessoa Juridica")
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.saldo = float(saldo)

    def __str__(self):
        return f"{super().__str__()} | {self.razao_social} | CNPJ {self.cnpj} | R$ {self.saldo:.2f}"
