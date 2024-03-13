from db import clientPS
from model.Product import Product
import pandas as pd


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

        # S'utilitza el pandas per llegir el fitxer csv
        csv_reader = pd.read_csv(file.file, header=0)

        # Amb el cursor, iterem per cada fila del csv i amb l'ajuda de funcions executem les ordres SQL
        with conn.cursor() as cur:
            for index, row in csv_reader.iterrows():
                fila = row.to_dict()
                category_id = updateCategory(
                    conn, fila["id_categoria"], fila["nom_categoria"])
                subcategory_id = updateSubcategory(
                    conn, fila["id_subcategoria"], fila["nom_subcategoria"], category_id)
                product_id = updateProduct(conn, fila["id_producto"], fila["nom_producto"],
                                           fila["descripcion_producto"], fila["companyia"], fila["precio"], fila["unidades"], subcategory_id)
        conn.commit()
        return {"message": "Càrrega massiva completada correctament", "state": 200}

    except Exception as e:
        print(f'ERROR: {e}')
        conn.rollback()
        return {"message": f"Error en la càrrega massiva: {str(e)}", "state": 500}
    finally:
        conn.close()


def updateCategory(conn, id, name):
    cur = conn.cursor()

    # Processar la categoria
    cur.execute("SELECT * FROM public.category WHERE category_id = %s", (id,))

    category_id = cur.fetchone()

    if category_id:
        # Si la categoria existeix, s'actualitza la seva informació
        cur.execute("""
        UPDATE public.category SET name = %s, updated_at = CURRENT_TIMESTAMP WHERE category_id = %s
        """, (name, id))
    else:
        # En canvi, si la categoria no existeix es fa un insert
        cur.execute("""
        INSERT INTO public.category (category_id, name, created_at, updated_at) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """, (id, name,))
    return id


def updateSubcategory(conn, id, name, category_id):
    cur = conn.cursor()

    cur.execute(
        "SELECT category_id FROM public.category WHERE category_id = %s", (category_id,))
    existing_category = cur.fetchone()

    if not existing_category:
        print(
            f"Error: No existe la categoría con el category_id {category_id}")
        return id

    cur.execute(
        "SELECT subcategory_id FROM public.subcategory WHERE subcategory_id = %s", (id,))

    subcategory_id = cur.fetchone()

    if subcategory_id:
        cur.execute("""
                UPDATE public.subcategory SET name = %s, category_id = %s, updated_at = CURRENT_TIMESTAMP WHERE subcategory_id = %s
        """, (name, category_id, id))
    else:
        cur.execute("""
        INSERT INTO public.subcategory (subcategory_id, name, category_id, created_at, updated_at) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """, (id, name, category_id,))
    return id


def updateProduct(conn, id, name, description, company, price, units, subcategory_id):
    cur = conn.cursor()

    cur.execute(
        "SELECT subcategory_id FROM public.subcategory WHERE subcategory_id = %s", (subcategory_id,))
    existing_subcategory = cur.fetchone()

    if not existing_subcategory:
        print(
            f"Error: No existe la subcategoría con el subcategory_id {subcategory_id}")
        return id

    cur.execute("""
            SELECT * FROM public.product WHERE product_id = %s
    """, (id,))
    product_id = cur.fetchone()

    if product_id:
        cur.execute("UPDATE public.product SET name = %s, description = %s, company = %s, price = %s, units = %s, subcategory_id = %s, updated_at = CURRENT_TIMESTAMP WHERE product_id = %s",
                    (name, description, company, price, units, subcategory_id, id))
    else:
        cur.execute("INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                    (id, name, description, company, price, units, subcategory_id))
    return id
