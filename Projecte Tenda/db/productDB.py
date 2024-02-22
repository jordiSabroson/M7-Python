from db import clientPS
from model.Product import Product


def insert_product(product: Product):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO public.product(
                name, description, company, price, units, subcategory_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING product_id
        """, (
            product.name,
            product.description,
            product.company,
            product.price,
            product.units,
            product.subcategory_id
        ))

        id_insertat = cur.fetchone()[0]

        conn.commit()

        return {"id": id_insertat, "missatge": "producte insertat correctament"}

    except Exception as e:
        print(f'ERROR: {e}')

        conn.rollback()

    finally:
        conn.close()


def consulta():
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        data = cur.fetchone()

        return {"message": {data}}

    except Exception as e:
        print(f'ERROR: {e}')

        conn.rollback()

    finally:
        conn.close()
