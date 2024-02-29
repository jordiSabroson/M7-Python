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


def getProductes():
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute("SELECT * FROM public.product")

        data = cur.fetchall()

        return data

    except Exception as e:
        print(f'ERROR: {e}')

        conn.rollback()

    finally:
        conn.close()


def getProductById(product: Product):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM public.product WHERE product_id = %s", (product.id))

        data = cur.fetchone()

        return {'id': data[0], 'name': data[1], 'description': data[2], 'company': data[3], 'price': data[4], 'unit': data[5]}

    except Exception as e:
        print(f'ERROR: {e}')

        conn.rollback()

    finally:
        conn.close()
