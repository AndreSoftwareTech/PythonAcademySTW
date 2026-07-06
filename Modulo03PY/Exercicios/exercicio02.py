# ============================================================
# EXERCICIO 02 - "A CONTA QUE SE APRESENTA"
# Base: Aula 02 (Atributos, metodos e __str__)
# ------------------------------------------------------------
# Contexto:
#   Um objeto bancario nao e so uma caixa de numeros: ele precisa
#   SE COMUNICAR. O metodo __str__ e o cartao de visitas do objeto —
#   quando voce faz print(conta), e ele quem responde. Metodos comuns,
#   como extrato(), sao os "servicos" que o objeto oferece.
#
# Sua missao:
#   Complete a classe Conta com comportamento:
#     1) Declare os atributos da classe: titular, numero, saldo, limite.
#     2) Crie o metodo extrato(self) que imprima numero, titular e saldo formatado.
#     3) Crie __str__(self) retornando uma string resumida do titular e saldo.
#     4) Crie um objeto, chame extrato() e depois print(conta) para ver a diferenca.
#
# Regras (validando a Aula 02):
#   - __str__ deve RETORNAR uma string (return), nao usar print dentro dele.
#   - extrato() usa print — e uma acao; __str__ e uma representacao.
#   - Metodos de instancia recebem self como primeiro parametro.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Conta:
    titular: str
    numero: int
    saldo: float
    limite: float

    def extrato(self):
        print(f"Conta {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

    def __str__(self):
        return f"{self.titular} - {self.numero} - Saldo: R$ {self.saldo:.2f}"


conta = Conta()
conta.titular = "Lucas Ferreira"
conta.numero = 7788
conta.saldo = 3200.50
conta.limite = 1000.0

conta.extrato()
print(conta)
