import sqlite3
import hashlib
import re

def conectar():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT)")

    senha_hash = hashlib.sha256("1234".encode()).hexdigest()
    cursor.execute("INSERT INTO usuarios VALUES ('admin', ?)", (senha_hash,))
    
    conn.commit()
    return conn

def validar_entrada(texto):
    return re.match(r"^[a-zA-Z0-9_]+$", texto) is not None

def login(conn, usuario, senha):
    cursor = conn.cursor()

    if not validar_entrada(usuario) or not validar_entrada(senha):
        return False

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    cursor.execute(query, (usuario, senha_hash))

    return cursor.fetchone() is not None