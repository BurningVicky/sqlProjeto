import app_vulneravel
import app_seguro

def test_sql_injection_vulneravel():
    conn = app_vulneravel.conectar()

    ataque = "' OR '1'='1"
    resultado = app_vulneravel.login(conn, ataque, ataque)

    assert resultado is True  # vulnerável


def test_sql_injection_seguro():
    conn = app_seguro.conectar()

    ataque = "' OR '1'='1"
    resultado = app_seguro.login(conn, ataque, ataque)

    assert resultado is False  # protegido