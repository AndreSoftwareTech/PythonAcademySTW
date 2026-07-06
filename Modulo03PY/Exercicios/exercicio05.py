# ============================================================
# EXERCICIO 05 - "CAIXA ELETRONICO COM REGRAS"
# Base: Aula 05 (Metodos de instancia)
# ------------------------------------------------------------
# Contexto:
#   Uma conta bancaria de verdade nao aceita deposito negativo nem
#   saque acima do saldo disponivel (saldo + limite). Metodos sao
#   as "portas de servico" do objeto: cada acao passa por regras
#   antes de alterar os dados internos.
#
# Sua missao:
#   Implemente a classe Conta com operacoes financeiras:
#     1) __init__(self, titular, numero, saldo, limite) com atribuicoes a self.
#     2) depositar(self, valor) — rejeita valores <= 0; soma ao saldo se valido.
#     3) sacar(self, valor) — rejeita valores <= 0; verifica saldo + limite.
#     4) extrato(self) — imprime resumo da conta.
#     5) Teste: deposito valido, saque valido, saque acima do permitido e deposito negativo.
#
# Regras (validando a Aula 05):
#   - Metodos alteram self.saldo — nunca variaveis soltas fora da classe.
#   - Valores invalidos devem exibir mensagem e retornar sem alterar o saldo.
#   - Saque so e permitido se self.saldo + self.limite >= valor.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = int(numero)
        self.saldo = float(saldo)
        self.limite = float(limite)

    def extrato(self):
        print(f"Conta {self.numero} | {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de deposito invalido.")
            return
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque invalido.")
            return
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente (mesmo com limite).")

    def __str__(self):
        return f"{self.titular} - Conta {self.numero} - R$ {self.saldo:.2f}"


conta = Conta("Juliana Rocha", "3344", 800.0, 200.0)

conta.extrato()
conta.depositar(500.0)
conta.sacar(300.0)
conta.sacar(1500.0)   # deve falhar: 800 + 500 - 300 = 1000, limite 200 -> max 1200
conta.depositar(-50)  # deve falhar
conta.extrato()
