import psycopg


def client():
    conexio = """
            dbname = postgres
            user = user_postgres
            password = pass_postgres
            host = localhost
            port = 5433
            """

    try:
        return psycopg.connect(conexio)

    except Exception as e:
        print(f"ERROR: {e}")
