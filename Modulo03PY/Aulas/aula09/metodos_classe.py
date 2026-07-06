# ============================================================
# MODULO 03 - AULA 09: @classmethod E @staticmethod [NOVO]
# ------------------------------------------------------------
# Objetivo: nem todo metodo precisa de 'self' (instancia).
#   @classmethod -> recebe 'cls' (a classe); util para fabricas.
#   @staticmethod -> funcao utilitaria dentro da classe, sem self.
# ============================================================

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    @classmethod
    def from_string(cls, texto):
        # Fabrica: cria Produto a partir de "nome;preco"
        nome, preco = texto.split(";")
        return cls(nome.strip(), preco.strip())

    @staticmethod
    def validar_preco(preco):
        return float(preco) >= 0

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

# Demonstracao
p1 = Produto("Caneta", 2.50)
p2 = Produto.from_string("Caderno;19.90")

print(p1)
print(p2)
print("Preco 10 valido?", Produto.validar_preco(10))
print("Preco -5 valido?", Produto.validar_preco(-5))
