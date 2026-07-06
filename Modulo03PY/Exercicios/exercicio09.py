# ============================================================
# EXERCICIO 09 - "A FABRICA DE PRODUTOS"
# Base: Aula 09 (@classmethod fabrica + @staticmethod validador)
# ------------------------------------------------------------
# Contexto:
#   Nem todo metodo precisa de uma instancia pronta. As vezes a
#   classe fabrica objetos a partir de um texto, e outras vezes
#   so queremos validar um valor antes de criar qualquer coisa.
#
# Sua missao:
#   Crie a classe Produto com nome e preco. Depois implemente:
#     - @classmethod from_string(cls, texto): recebe "nome;preco"
#       (ex.: "Caneta;2.50") e devolve um Produto pronto.
#     - @staticmethod validar_preco(preco): retorna True se o preco
#       for >= 0, senao False.
#     - __str__: mostre "Nome - R$ X.XX"
#
# Regras (validando a Aula 09):
#   - Use @classmethod na fabrica e @staticmethod no validador.
#   - Crie um produto normal e outro via from_string().
#   - Teste validar_preco com um valor positivo e um negativo.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    @classmethod
    def from_string(cls, texto):
        nome, preco = texto.split(";")
        return cls(nome.strip(), preco.strip())

    @staticmethod
    def validar_preco(preco):
        return float(preco) >= 0

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


p1 = Produto("Caneta", 2.50)
p2 = Produto.from_string("Caderno;19.90")

print(p1)
print(p2)
print("Preco 10 valido?", Produto.validar_preco(10))
print("Preco -5 valido?", Produto.validar_preco(-5))
