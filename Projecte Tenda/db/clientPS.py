import psycopg


def client():
    # Dades per establir connexió amb la BBDD
    conexio = """
            dbname = postgres
            user = user_postgres
            password = pass_postgres
            host = localhost
            port = 5433
            """

    try:
        # Si la connexió funciona, la retornem
        return psycopg.connect(conexio)

    except Exception as e:
        print(f"ERROR: {e}")
