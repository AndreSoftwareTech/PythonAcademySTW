# ============================================================
# CAMADA SERVICE (Regras de Negocio)
# ------------------------------------------------------------
# O Service e o "cerebro" das regras. Ele decide o que e valido
# ANTES de mandar salvar no banco. Exemplos de regra:
#   - nome nao pode ser vazio
#   - preco nao pode ser negativo
#   - quantidade nao pode ser negativa
#
# Quando um dado e invalido, "levantamos" um erro com raise ValueError.
# Quem chamou (o Controller) decide como mostrar esse erro ao usuario.
# O Service conversa com o DAO, mas NAO sabe nada de SQL nem de menu.
# ============================================================

from model.produto import Produto
from dao.produto_dao import ProdutoDAO


class ProdutoService:
    def __init__(self):
        self.dao = ProdutoDAO()

    def cadastrar(self, nome, preco, quantidade):
        self.__validar(nome, preco, quantidade)
        produto = Produto(nome=nome.strip(), preco=preco, quantidade=quantidade)
        return self.dao.inserir(produto)

    def listar(self):
        return self.dao.listar()

    def buscar(self, id):
        produto = self.dao.buscar_por_id(id)
        if produto is None:
            raise ValueError(f"Produto com id {id} nao encontrado.")
        return produto

    def atualizar(self, id, nome, preco, quantidade):
        # Garante que o produto existe antes de tentar atualizar.
        self.buscar(id)
        self.__validar(nome, preco, quantidade)
        produto = Produto(id=id, nome=nome.strip(), preco=preco, quantidade=quantidade)
        return self.dao.atualizar(produto)

    def remover(self, id):
        self.buscar(id)
        return self.dao.deletar(id)

    # ---------- Regras de validacao (uso interno) ----------
    def __validar(self, nome, preco, quantidade):
        if nome is None or nome.strip() == "":
            raise ValueError("O nome do produto nao pode ser vazio.")
        if preco < 0:
            raise ValueError("O preco nao pode ser negativo.")
        if quantidade < 0:
            raise ValueError("A quantidade nao pode ser negativa.")
