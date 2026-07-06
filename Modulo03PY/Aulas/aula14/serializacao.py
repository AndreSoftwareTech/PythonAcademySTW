# ============================================================
# MODULO 03 - AULA 14: SERIALIZACAO DE OBJETOS [NOVO]
# ------------------------------------------------------------
# Objetivo: transformar objetos Python em dados que podem ser
# salvos (dict/JSON) e reconstruir objetos a partir desses dados.
# Ponte entre OOP e persistencia (preparacao para Modulo 04).
# ============================================================

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "paginas": self.paginas}

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["titulo"], dados["autor"], dados["paginas"])

    def __str__(self):
        return f'"{self.titulo}" por {self.autor} ({self.paginas} pags)'

# Criar -> serializar -> desserializar -> objeto de volta
original = Livro("1984", "George Orwell", 328)
print("Original:", original)

dicionario = original.to_dict()
print("Como dict:", dicionario)

restaurado = Livro.from_dict(dicionario)
print("Restaurado:", restaurado)
print("Sao iguais?", original.titulo == restaurado.titulo)
