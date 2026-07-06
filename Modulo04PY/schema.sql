-- ============================================================
-- SCHEMA (Estrutura do Banco de Dados) - SQL puro
-- ------------------------------------------------------------
-- Este arquivo mostra, em SQL "cru", a mesma tabela que o codigo
-- cria automaticamente no arquivo produto_dao.py (metodo criar_tabela).
--
-- Serve para o aluno LER e ENTENDER o SQL de criacao (DDL),
-- separado da logica em Python. Voce pode inclusive abrir o
-- arquivo loja.db em um visualizador de SQLite e rodar estes
-- comandos manualmente.
-- ============================================================

CREATE TABLE IF NOT EXISTS produtos (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,  -- id gerado pelo banco
    nome       TEXT    NOT NULL,                    -- nome do produto
    preco      REAL    NOT NULL,                    -- preco (numero decimal)
    quantidade INTEGER NOT NULL                     -- quantidade em estoque
);

-- Exemplos de comandos SQL usados pela aplicacao (CRUD):

-- CREATE (inserir):
-- INSERT INTO produtos (nome, preco, quantidade) VALUES ('Caneta', 2.50, 100);

-- READ (consultar):
-- SELECT id, nome, preco, quantidade FROM produtos ORDER BY id;
-- SELECT id, nome, preco, quantidade FROM produtos WHERE id = 1;

-- UPDATE (atualizar):
-- UPDATE produtos SET nome = 'Caneta Azul', preco = 3.00, quantidade = 80 WHERE id = 1;

-- DELETE (remover):
-- DELETE FROM produtos WHERE id = 1;
