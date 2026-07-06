# ============================================================
# CAMADA MODEL (Modelo / Entidade)
# ------------------------------------------------------------
# Representa "o que" o sistema manipula: um Produto.
# Aqui NAO existe banco de dados, NAO existe menu, NAO existe SQL.
# E apenas a estrutura de dados com encapsulamento (mesmo conceito
# de @property que voce viu no Modulo 03 de Orientacao a Objetos).
# ============================================================


class Produto:
    def __init__(self, nome, preco, quantidade, id=None):
        # O "id" comeca como None porque quem gera o id e o banco de dados.
        # Quando lemos um produto do banco, preenchemos esse id.
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def __str__(self):
        # Define como o produto aparece quando usamos print(produto).
        return (
            f"[{self.__id}] {self.__nome} | "
            f"R$ {self.__preco:.2f} | "
            f"Estoque: {self.__quantidade}"
        )
