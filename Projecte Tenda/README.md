# CRUD PRODUCTES
## Objectius
- Aprendre a utilitzar FastApi
- Aprendre a crear taules relacionals
- Llegir un csv amb python
- CRUD Python

## FEINA INDIVIDUAL
<b>1. Crear un entorn amb FastApi</b> <br>
Utilitzar el framework fastapi per crear una api rest
https://fastapi.tiangolo.com/

<b>2. Crear una bases de dades amb PostgreSQL per una botiga online de productes tecnològics.</b>
```
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE subcategory (
	subcategory_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	category_id INT NOT NULL,
	created_at TIMESTAMP,
	updated_at TIMESTAMP,
	FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE product (
	product_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description TEXT,
	company VARCHAR(255) NOT NULL,
	price DECIMAL(10,2) NOT NULL,
	units NUMERIC,
	subcategory_id INT NOT NULL,
	created_at TIMESTAMP,
	updated_at TIMESTAMP,
	FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
);
```
<b>3. Les funcionalitats que ens demanen el client:</b>
- CRUD Productes:
    - Ruta:  /product/
        Tipus de petició: Get
        Funcionament: Retorna una llista json amb tota la informació dels productes de la taula products
    - Ruta:  /product/{id}
Tipus de petició: Get
Funcionament: Retorna un objecte json amb la informació del producte que la id de la bases de dades coincideix amb la id que ens arribar per paràmetre.
    - Ruta:  /product/
Tipus de petició: Post
Funcionament: Permet afegir un nou producte a la BBDD
Retorna un objecte amb el missatge “S’ha afegit correctement”
    - Ruta:  /product/ 
            /product/{id}
Tipus de petició: Put
Funcionament: Permet modificar el camp d’un producte de la BBDD definit per la id que arribar per paràmetre. Retorna un objecte amb el missatge “S’ha modificat correctement”
    - Ruta:  /product/{id}
Tipus de petició: Delete
Funcionament: Permet eliminar un producte de la BBDD
Retorna un objecte amb el missatge “S’ha borrat correctament”
    - Ruta:  /productAll/
Tipus de petició: Get
Funcionament: Retorna una llista json de la següent informació del producte: nom de la categoria, nom de la subcategoria, nom del producte, marca del producte i el preu.

- Càrrega massiva de productes 
    - Ruta:  /loadProducts
Tipus de petició: Post
Funcionament: Servirà per fer una càrrega massiva de categories, subcategories i productes a les bases de dades a través d’un fitxer csv.