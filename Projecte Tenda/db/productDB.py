from db import clientPS


def consulta():
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute("select * from product")

        data = cur.fetchone()

        return f"consulta {data}"

    except Exception as e:
        print(f'ERROR: {e}')

        conn.rollback()

    finally:
        conn.close()
