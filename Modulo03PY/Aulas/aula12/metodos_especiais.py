# ============================================================
# MODULO 03 - AULA 12: METODOS ESPECIAIS __repr__ E __eq__ [NOVO]
# ------------------------------------------------------------
# Objetivo: metodos especiais (dunder) personalizam comportamento:
#   __str__  -> texto amigavel (print)
#   __repr__ -> representacao tecnica (debug)
#   __eq__   -> comparacao de igualdade (==)
# ============================================================

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
