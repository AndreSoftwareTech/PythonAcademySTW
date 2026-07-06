# ============================================================
# CAMADA CONTROLLER (Controle / Orquestracao)
# ------------------------------------------------------------
# O Controller e a "ponte" entre a tela (View) e as regras (Service).
# Ele recebe dados ja lidos pela View, chama o Service e devolve uma
# RESPOSTA pronta para ser exibida (texto ou lista de produtos).
#
# Repare que aqui usamos try/except: se o Service levantar um erro de
# regra (ValueError), o Controller captura e transforma em uma mensagem
# amigavel, sem quebrar o programa.
# O Controller NAO usa input()/print() e NAO sabe nada de SQL.
# ============================================================

from service.produto_service import ProdutoService


class ProdutoController:
    def __init__(self):
        self.service = ProdutoService()

    def cadastrar(self, nome, preco, quantidade):
        try:
            produto = self.service.cadastrar(nome, preco, quantidade)
            return f"Produto cadastrado com sucesso! {produto}"
        except ValueError as erro:
            return f"Erro ao cadastrar: {erro}"

    def listar(self):
        # Devolve a lista de objetos Produto (quem formata e a View).
        return self.service.listar()

    def buscar(self, id):
        try:
            return self.service.buscar(id)
        except ValueError as erro:
            return f"Erro na busca: {erro}"

    def atualizar(self, id, nome, preco, quantidade):
        try:
            self.service.atualizar(id, nome, preco, quantidade)
            return "Produto atualizado com sucesso!"
        except ValueError as erro:
            return f"Erro ao atualizar: {erro}"

    def remover(self, id):
        try:
            self.service.remover(id)
            return "Produto removido com sucesso!"
        except ValueError as erro:
            return f"Erro ao remover: {erro}"
