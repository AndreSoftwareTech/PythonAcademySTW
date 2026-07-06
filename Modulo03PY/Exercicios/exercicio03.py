# ============================================================
# EXERCICIO 03 - "NASCIMENTO COMPLETO"
# Base: Aula 03 (Construtor completo)
# ------------------------------------------------------------
# Contexto:
#   Imagine abrir uma conta bancaria e o gerente dizer: "Pode deixar
#   o CPF em branco, voce preenche depois." Inaceitavel! Um construtor
#   completo garante que NENHUM objeto nasce incompleto ou invalido.
#
# Sua missao:
#   Refatore a classe Conta para nascer 100% pronta:
#     1) __init__ recebe: numero, titular, cpf, saldo, limite.
#     2) Atribua TODOS os campos a self no construtor.
#     3) Implemente __str__ mostrando titular, numero, CPF e saldo.
#     4) Crie duas contas diferentes e imprima ambas com print().
#
# Regras (validando a Aula 03):
#   - Nao crie atributos fora do __init__ depois da instancia.
#   - Converta numero para int e saldo/limite para float no construtor.
#   - Cada conta criada deve ter os cinco campos obrigatorios preenchidos.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        self.numero = int(numero)
        self.titular = titular
        self.cpf = cpf
        self.saldo = float(saldo)
        self.limite = float(limite)

    def __str__(self):
        return (
            f"{self.titular} | Conta {self.numero} | "
            f"CPF {self.cpf} | Saldo R$ {self.saldo:.2f}"
        )


conta_poupanca = Conta("1001", "Ana Costa", "111.222.333-44", 2500.0, 0.0)
conta_corrente = Conta("2002", "Tech Solutions LTDA", "12.345.678/0001-99", 50000.0, 10000.0)

print(conta_poupanca)
print(conta_corrente)
