SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        estoque INTEGER NOT NULL,
        preco FLOAT NOT NULL,
        categoria TEXT NOT NULL
)"""

SQL_INSERIR = """
    INSERT INTO produto(
        nome, descricao, estoque, preco, categoria)
    VALUES (?,?,?,?,?)
"""

SQL_EXCLUIR = """
    DELETE FROM produto
    WHERE id=?
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, descricao, estoque, preco, categoria
    FROM produto
    ORDER BY nome
"""