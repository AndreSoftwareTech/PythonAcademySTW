# ============================================================
# CAMADA DAO (Data Access Object - Acesso a Dados)
# ------------------------------------------------------------
# Aqui, e SOMENTE aqui, escrevemos comandos SQL.
# O DAO traduz objetos Produto <-> linhas da tabela do banco.
#
# Repare que TODA consulta usa "?" no lugar dos valores. Isso se chama
# consulta parametrizada e evita o famoso "SQL Injection". NUNCA
# montamos SQL concatenando texto digitado pelo usuario.
#
# Os imports abaixo usam o nome da PASTA (pacote) de cada camada:
#   database.conexao  ->  pasta database, arquivo conexao.py
#   model.produto     ->  pasta model, arquivo produto.py
# ============================================================

from database.conexao import Conexao
from model.produto import Produto


class ProdutoDAO:
    def __init__(self):
        self.conexao = Conexao()

    # ---------- DDL: cria a estrutura da tabela (uma vez) ----------
    def criar_tabela(self):
        sql = """
            CREATE TABLE IF NOT EXISTS produtos (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                nome       TEXT    NOT NULL,
                preco      REAL    NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """
        conexao = self.conexao.conectar()
        conexao.execute(sql)
        conexao.commit()
        conexao.close()

    # ---------- CREATE: INSERT ----------
    def inserir(self, produto):
        sql = "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)"
        conexao = self.conexao.conectar()
        cursor = conexao.cursor()
        cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade))
        conexao.commit()
        # lastrowid = o id que o banco gerou para o registro recem-inserido.
        produto.id = cursor.lastrowid
        conexao.close()
        return produto

    # ---------- READ: SELECT (todos) ----------
    def listar(self):
        sql = "SELECT id, nome, preco, quantidade FROM produtos ORDER BY id"
        conexao = self.conexao.conectar()
        linhas = conexao.execute(sql).fetchall()
        conexao.close()
        # Transforma cada linha do banco em um objeto Produto.
        return [self.__linha_para_produto(linha) for linha in linhas]

    # ---------- READ: SELECT (um por id) ----------
    def buscar_por_id(self, id):
        sql = "SELECT id, nome, preco, quantidade FROM produtos WHERE id = ?"
        conexao = self.conexao.conectar()
        linha = conexao.execute(sql, (id,)).fetchone()
        conexao.close()
        if linha is None:
            return None
        return self.__linha_para_produto(linha)

    # ---------- UPDATE ----------
    def atualizar(self, produto):
        sql = "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?"
        conexao = self.conexao.conectar()
        cursor = conexao.cursor()
        cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade, produto.id))
        conexao.commit()
        # rowcount diz quantas linhas foram afetadas (0 = id nao existe).
        alterou = cursor.rowcount > 0
        conexao.close()
        return alterou

    # ---------- DELETE ----------
    def deletar(self, id):
        sql = "DELETE FROM produtos WHERE id = ?"
        conexao = self.conexao.conectar()
        cursor = conexao.cursor()
        cursor.execute(sql, (id,))
        conexao.commit()
        removeu = cursor.rowcount > 0
        conexao.close()
        return removeu

    # ---------- Auxiliar interno ----------
    def __linha_para_produto(self, linha):
        # Converte uma linha do banco (sqlite3.Row) em um objeto Produto.
        return Produto(
            id=linha["id"],
            nome=linha["nome"],
            preco=linha["preco"],
            quantidade=linha["quantidade"],
        )
