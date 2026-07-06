# ============================================================
# EXERCICIO 06 - "COFRE COM PORTEIRO"
# Base: Aula 06 (Encapsulamento: getters e setters)
# ------------------------------------------------------------
# Contexto:
#   Deixar o saldo bancario exposto e como deixar a porta do cofre
#   aberta. Encapsulamento usa atributos privados (__dois_underlines)
#   e metodos get/set que decidem QUEM pode ler ou alterar cada dado.
#
# Sua missao:
#   Proteja os dados de uma Conta:
#     1) No __init__, guarde titular, numero, saldo e limite com prefixo __.
#     2) Crie get_titular(), get_saldo(), get_limite() para leitura segura.
#     3) Crie set_titular(titular) — rejeita string vazia.
#     4) Crie set_saldo(saldo) — rejeita valores negativos.
#     5) Implemente __str__ usando os getters (nao acesse __ diretamente fora).
#     6) Teste leitura, alteracao valida e alteracao invalida.
#
# Regras (validando a Aula 06):
#   - Atributos privados: self.__nome (dois underscores).
#   - Fora da classe, use get_*/set_* — nunca conta.__saldo diretamente.
#   - Setters devem validar ANTES de alterar o valor interno.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = int(numero)
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        if titular.strip():
            self.__titular = titular
        else:
            print("Titular nao pode ser vazio.")

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = float(saldo)
        else:
            print("Saldo nao pode ser negativo.")

    def get_limite(self):
        return self.__limite

    def __str__(self):
        return f"{self.get_titular()} | Conta {self.__numero} | R$ {self.get_saldo():.2f}"


conta = Conta("Pedro Alves", "5566", 1200.0, 500.0)

print(conta)
print("Saldo via getter:", conta.get_saldo())

conta.set_saldo(1500.0)
conta.set_saldo(-100.0)      # deve rejeitar
conta.set_titular("")        # deve rejeitar
conta.set_titular("Pedro A. Alves")

print(conta)
