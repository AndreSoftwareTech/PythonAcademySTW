# ============================================================
# EXERCICIO 14 - "LIVRO PERDIDO, LIVRO ENCONTRADO"
# Base: Aula 14 (Serializacao: to_dict / from_dict)
# ------------------------------------------------------------
# Contexto:
#   Serializar e transformar um objeto em dados "planos" (dict) que
#   podem ser salvos, enviados ou reconstruidos depois. E a ponte
#   entre OOP e persistencia — preparacao para sistemas maiores.
#
# Sua missao:
#   Crie a classe Livro(titulo, autor, paginas) com:
#     - to_dict() -> dicionario com as tres chaves
#     - @classmethod from_dict(cls, dados) -> novo Livro
#     - __str__ legivel para print
#   Demonstre o ciclo completo:
#     original -> to_dict -> from_dict -> restaurado
#   Compare se titulo, autor e paginas sao iguais nos dois objetos.
#
# Regras (validando a Aula 14):
#   - Nao altere os dados ao serializar (mesmos valores no dict).
#   - Mostre original, dict e restaurado na tela.
#
# Desafio logico:
#   Crie uma funcao clonar_livro(livro) que use to_dict + from_dict
#   e devolva uma COPIA independente (outro objeto na memoria).
# ============================================================

# --- GABARITO DO PROFESSOR ---
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


def clonar_livro(livro):
    return Livro.from_dict(livro.to_dict())


original = Livro("1984", "George Orwell", 328)
print("Original:", original)

dicionario = original.to_dict()
print("Como dict:", dicionario)

restaurado = Livro.from_dict(dicionario)
print("Restaurado:", restaurado)

iguais = (
    original.titulo == restaurado.titulo
    and original.autor == restaurado.autor
    and original.paginas == restaurado.paginas
)
print("Dados iguais?", iguais)

copia = clonar_livro(original)
print("Clone:", copia)
print("Original e clone sao o mesmo objeto?", original is copia)
