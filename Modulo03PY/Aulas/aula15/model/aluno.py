# ============================================================
# MODEL: classe Aluno com encapsulamento e serializacao
# ============================================================

class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = float(nota)

    @property
    def nome(self):
        return self.__nome

    @property
    def nota(self):
        return self.__nota

    @property
    def situacao(self):
        return "Aprovado" if self.__nota >= 7 else "Reprovado"

    def to_dict(self):
        return {"nome": self.__nome, "nota": self.__nota, "situacao": self.situacao}

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["nome"], dados["nota"])

    def __str__(self):
        return f"{self.nome} | Nota {self.nota:.1f} | {self.situacao}"
