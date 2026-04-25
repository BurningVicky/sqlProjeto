import sqlite3

def conectar():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT)")

    # vulnerável sem validação de entrada e sem hash de senha
    cursor.execute("INSERT INTO usuarios VALUES ('admin', '1234')")
    
    conn.commit()
    return conn

def login(conn, usuario, senha):
    cursor = conn.cursor()

    # vulnerável
    query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
    cursor.execute(query)

    return cursor.fetchone() is not None