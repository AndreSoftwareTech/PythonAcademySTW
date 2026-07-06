# ============================================================
# EXERCICIO 01 - "O MOLDE DA PRIMEIRA CONTA"
# Base: Aula 01 (Classes, self e __init__)
# ------------------------------------------------------------
# Contexto:
#   Antes de existir um app bancario, existe um MOLDE: a classe.
#   Cada conta aberta no mundo real e um objeto criado a partir
#   desse molde. O construtor __init__ e a linha de montagem onde
#   cada peca (atributo) e encaixada no objeto recém-nascido.
#
# Sua missao:
#   Crie a classe Conta do zero, passo a passo:
#     1) Defina a classe Conta com a palavra-chave class.
#     2) Crie o metodo __init__(self, numero, titular, cpf, saldo, limite).
#     3) Dentro do __init__, ATRIBUA cada parametro a self:
#          self.numero = int(numero)
#          self.titular = titular
#          self.cpf = cpf
#          self.saldo = float(saldo)
#          self.limite = float(limite)
#     4) Instancie UMA conta com dados fixos e imprima titular, numero e saldo.
#
# Regras (validando a Aula 01):
#   - Todo parametro do __init__ DEVE ser guardado em self.atributo.
#   - So anotar tipo (self.numero : int) NAO guarda valor — use atribuicao (=).
#   - self e sempre o primeiro parametro de metodos de instancia.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        print(f"Criando conta para {titular} (objeto: {self})")
        self.numero = int(numero)
        self.titular = titular
        self.cpf = cpf
        self.saldo = float(saldo)
        self.limite = float(limite)


conta = Conta("4521", "Marina Souza", "123.456.789-00", 1500.0, 500.0)

print("Titular:", conta.titular)
print("Numero:", conta.numero)
print("Saldo: R$", conta.saldo)
