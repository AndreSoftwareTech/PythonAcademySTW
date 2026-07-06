# ============================================================
# EXERCICIO 12 - "IGUAIS OU COINCIDENCIA?"
# Base: Aula 12 (__str__, __repr__, __eq__)
# ------------------------------------------------------------
# Contexto:
#   Metodos especiais (dunder) personalizam como objetos se
#   comportam: print usa __str__, repr() usa __repr__, e == usa __eq__.
#   Dois objetos diferentes podem ser "iguais" se seus dados forem.
#
# Sua missao:
#   Crie a classe Ponto com x e y. Implemente:
#     - __str__: texto amigavel, ex. "Ponto(3, 4)"
#     - __repr__: texto tecnico, ex. "Ponto(x=3, y=4)"
#     - __eq__: True se outro objeto for Ponto com mesmo x e y
#
# Regras (validando a Aula 12):
#   - Crie a, b com mesmas coordenadas e c com coordenadas diferentes.
#   - Imprima str, repr e compare a == b e a == c.
#
# Desafio logico:
#   Em __eq__, retorne False se outro NAO for instancia de Ponto.
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

    def __repr__(self):
        return f"Ponto(x={self.x}, y={self.y})"

    def __eq__(self, outro):
        if not isinstance(outro, Ponto):
            return False
        return self.x == outro.x and self.y == outro.y


a = Ponto(3, 4)
b = Ponto(3, 4)
c = Ponto(1, 2)

print("str:", a)
print("repr:", repr(a))
print("a == b?", a == b)
print("a == c?", a == c)
