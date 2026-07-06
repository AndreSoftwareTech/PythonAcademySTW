# ============================================================
# MAIN (Ponto de Entrada da Aplicacao)
# ------------------------------------------------------------
# E o arquivo que executamos:  python main.py
#
# Responsabilidades da main:
#   1) Preparar o banco (garantir que a tabela existe).
#   2) Iniciar o menu (a View), que dispara todo o fluxo.
#
# ESTRUTURA DE PASTAS (cada camada em seu proprio pacote):
#   Modulo04PY/
#     main.py                 <- voce esta aqui
#     view/menu.py            <- VIEW (tela: input/print)
#     controller/produto_controller.py  <- CONTROLLER (orquestra/erros)
#     service/produto_service.py         <- SERVICE (regras de negocio)
#     model/produto.py        <- MODEL (a classe Produto)
#     dao/produto_dao.py      <- DAO (comandos SQL)
#     database/conexao.py     <- CONEXAO (abre o SQLite)
#     loja.db                 <- arquivo do banco (criado sozinho)
#
# FLUXO COMPLETO de uma acao (ex.: cadastrar um produto):
#
#   main.py
#     -> view/menu.py ................ le os dados no teclado (input)
#        -> controller/produto_controller.py ... orquestra e trata erros
#           -> service/produto_service.py ....... aplica as regras
#              -> dao/produto_dao.py ............ monta e executa o SQL
#                 -> database/conexao.py ........ abre a conexao
#                    -> loja.db .................. dados salvos (SQLite)
#
# Cada pasta tem UMA responsabilidade. Isso deixa o sistema
# organizado, testavel e facil de manter/evoluir.
# ============================================================

from dao.produto_dao import ProdutoDAO
from view.menu import iniciar


def main():
    # Garante a estrutura do banco antes de abrir o menu.
    ProdutoDAO().criar_tabela()
    iniciar()


if __name__ == "__main__":
    main()
