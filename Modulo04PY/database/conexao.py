# ============================================================
# CAMADA DE CONEXAO (Infraestrutura / Banco de Dados)
# ------------------------------------------------------------
# Responsabilidade UNICA: saber como abrir uma conexao com o banco.
# Usamos SQLite, que ja vem instalado junto com o Python (modulo sqlite3)
# e guarda tudo em um unico arquivo (loja.db).
#
# Por que isolar a conexao em uma pasta/arquivo so dela?
#   - Se um dia trocarmos SQLite por MySQL ou PostgreSQL,
#     mudamos SOMENTE este arquivo, e o resto do sistema continua igual.
# ============================================================

import os
import sqlite3

# __file__ aponta para .../Modulo04PY/database/conexao.py
# Subimos DOIS niveis de pasta para guardar o loja.db na raiz do modulo
# (.../Modulo04PY/loja.db), nao importa de onde o programa foi executado.
PASTA_DATABASE = os.path.dirname(os.path.abspath(__file__))
PASTA_RAIZ = os.path.dirname(PASTA_DATABASE)
CAMINHO_BANCO = os.path.join(PASTA_RAIZ, "loja.db")


class Conexao:
    def __init__(self, banco=CAMINHO_BANCO):
        self.banco = banco

    def conectar(self):
        # Cria (na primeira vez) e abre o arquivo do banco de dados.
        conexao = sqlite3.connect(self.banco)
        # row_factory faz o SELECT devolver os dados acessiveis por nome
        # da coluna (ex.: linha["nome"]) em vez de so por posicao.
        conexao.row_factory = sqlite3.Row
        return conexao
