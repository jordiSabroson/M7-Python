from db import clientPS
from model.Product import Product
import csv
from datetime import datetime
import codecs


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


def getProductById(id):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM public.product WHERE product_id = %s", (id,))
        data = cur.fetchone()

        if data:
            return {'id': data[0], 'name': data[1], 'description': data[2], 'company': data[3], 'price': data[4], 'unit': data[5]}
        else:
            print("No hi ha productes per l'ID seleccionat")
            return {"message": "Producte no trobat", "state": 404}

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
    finally:
        conn.close()


def modifyProduct(id, product: Product):
    try:
        conn = clientPS.client()
        cur = conn.cursor()

        cur.execute("""
        UPDATE public.product
        SET name = %s, description = %s, company = %s, price = %s, units = %s
        WHERE product_id = %s
        """, (
            product.name,
            product.description,
            product.company,
            product.price,
            product.units,
            id
        ))

        conn.commit()

        return {"message": "Producte actualitzat correctament", "state": 200}

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
        return {"message": f"Error al actualitzar el producte: {str(e)}", "state": 500}
    finally:
        conn.close()


def deleteProduct(id):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute("DELETE FROM public.product WHERE product_id = %s", (id,))
        conn.commit()
        return {"message": "Producte eliminat correctament", "state": 200}
    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
        return {"message": f"Error al eliminar el producte: {str(e)}", "state": 500}
    finally:
        conn.close()


def getAllProducts():
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        cur.execute("""
            SELECT c.name AS category_name, sc.name AS subcategory_name, p.name AS product_name, p.company AS product_company, p.price AS product_price
            FROM product p
            JOIN subcategory sc ON p.subcategory_id = sc.subcategory_id
            JOIN category c ON sc.category_id = c.category_id
        """)

        data = cur.fetchall()

        product_info_list = [
            {
                "category_name": row[0],
                "subcategory_name": row[1],
                "product_name": row[2],
                "product_company": row[3],
                "product_price": row[4]
            }
            for row in data
        ]

        return product_info_list

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
    finally:
        conn.close()


def loadProducts(file):
    try:
        conn = clientPS.client()
        cur = conn.cursor()
        csv_reader = csv.reader(codecs.iterdecode(
            file.file, 'utf-8'), delimiter=',')

        for row in csv_reader:
            category_name, subcategory_name, product_name = row

            # Procesar la categoría
            cur.execute("""
                SELECT category_id FROM public.category WHERE name = %s
            """, (category_name,))
            category_id = cur.fetchone()

            if category_id:
                # La categoría existe, realizar una actualización
                cur.execute("""
                    UPDATE public.category SET name = %s, updated_at = %s WHERE category_id = %s
                """, (category_name, datetime.now(), category_id))
            else:
                # La categoría no existe, realizar una inserción
                cur.execute("""
                    INSERT INTO public.category (name, created_at, updated_at) VALUES (%s, %s, %s)
                """, (category_name, datetime.now(), datetime.now()))

            # Subcategoria
            cur.execute("""
                    SELECT subcategory_id FROM public.subcategory WHERE name = %s
            """, (subcategory_name,))
            subcategory_id = cur.fetchone()

            if subcategory_id:
                cur.execute("""
                        UPDATE public.subcategory SET name = %s, updated_at = %s WHERE subcategory_id = %s
                """, (subcategory_name, datetime.now(), subcategory_id))
            else:
                cur.execute("""
                        INSERT INTO public.subcategory (name, created_at, updated_at) VALUES (%s, %s, %s)
                """, (subcategory_name, datetime.now(), datetime.now()))

            # Producte
            cur.execute("""
                    SELECT product_id FROM public.product WHERE name = %s
            """, (product_name,))
            product_id = cur.fetchone()

            if product_id:
                cur.execute("""
                        UPDATE public.product SET name = %s, updated_at = %s WHERE product_id = %s
                """, (product_name, datetime.now(), product_id))
            else:
                cur.execute("""
                        INSERT INTO public.product (name, created_at, updated_at) VALUES (%s, %s, %s)
                """, (product_name, datetime.now(), datetime.now()))

        conn.commit()
        return {"message": "Càrrega massiva completada correctament", "state": 200}

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
        return {"message": f"Error en la càrrega massiva: {str(e)}", "state": 500}
    finally:
        conn.close()
