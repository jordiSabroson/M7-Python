import psycopg

try:
    # String per a la connexió amb la base de dades postgres usant les dades del docker-compose.yml
    conexio = """
            dbname = postgres
            user = user_postgres
            password=pass_postgres
            host=localhost
            port=5433
            """

    # Guardem en una variable la connexió amb la BBDD
    conn = psycopg.connect(conexio)

    # El mètode cursor serveix per crear la connexió i que retorni un objecte
    cur = conn.cursor()

    # Manera de fer consultes dinàmiques a la bbdd
    # id = 1

    # El mètode execute() s’utilitza per enviar un sentència SQL a les bases de dades.
    # cur.execute(f"SELECT * FROM public.tiesto WHERE id={id}")

    # Pujar de manera iterativa i amb la id incremental, múltiples usuaris a la BBDD
    for count in range(10):
        cur.execute(f"""
                    INSERT INTO public.tiesto(id, NOM, edat, actiu, "desc")
                    VALUES({count}, 'FEDERIC', 22, true, 'molt eixerit')
                    """)

    print("S'ha afegit correctament")

    # El mètode commit() s’utilitza per fer efectius els canvis de la query.
    conn.commit()

    cur.execute("SELECT * FROM public.tiesto ORDER BY id ASC")

    # Així podem veure totes les dades de cada fila de la bbdd
    for i in cur:
        print(i)

    # el mètode fetchone() retorna un element de la bbdd
    # res = cur.fetchone()
    # print(res[1])

except Exception as e:
    print(f"ERROR: {e}")

    # El mètode rollback() s’utilitza per tirar endarrere els canvis de la query. Seria al revés del commit.
    conn.rollback()

finally:
    # El mètode close() tanca la connexió
    conn.close()
