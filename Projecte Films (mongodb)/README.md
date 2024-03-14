# PRÀCTICA 3 - CRUD + CONSULTES + MONGODB
### OBJECTIUS
- Aprendre a utilitzar FastApi
- Aprendre a fer consultes amb MongoDB
- CRUD Python
- Consultes query parameters

### FEINA INDIVIDUAL
<b>1. Crear un entorn amb FastApi</b>
<br>
Utilitzar el framework fastapi per crear una apirest
https://fastapi.tiangolo.com/

<b>2. Crear una bases de dades amb MongoDB i tingui una colecció que es digui films. Aquesta tindrà la següent estructura:</b>
<br>
```
{
	"title": “str”,
	"director": “str”,
	"year": int,
	"genre": “str”,
	"rating":number ,
	"country": “str”,
    "created_at": “date”,
    "update_at": “date”,
  }
```

<b>3. Les funcionalitats que ens demanen el client:</b>
- CRUD Films:
    - Ruta:  /films/<br>
    Tipus de petició: Get<br>
    Funcionament: Retorna un objecte json que contindrà “status”:1 i “data”: una llista d’objectes json amb tota la informació dels films.<br>
    En cas d’error retornarà un objecte json que contindrà “status” : -1 i “messatge”: missatge amb l’error que s’ha produït.
    - Ruta:  /film/{id}<br>
    Tipus de petició: Get<br>
    Funcionament: Retorna un objecte json que contindrà “status”:1 i “data”: un objecte json amb la informació del film que la id de la bases de dades coincideix amb la id que ens arribar per paràmetre.<br>
    En cas d’error retornarà un objecte json que contindrà “status” : -1 i “message”: missatge amb l’error que s’ha produït.
    - Ruta:  /film/<br>
    Tipus de petició: Post<br>
    Funcionament: Permet afegir un nou film a la BBDD<br>
    Retorna un objecte json que contindrà “status”:1 i “data”: un objecte json amb la informació del nou film que s’ha afegit amb la id.<br>
    En cas d’error retornarà un objecte que contindrà “status” : -1 i “message”: missatge amb l’error que s’ha produït.
    - Ruta:  /film/{id}<br>
    Tipus de petició: Put<br>
    Funcionament: Permet modificar qualsevol informació d’un film concret a la BBDD definit per la id que arriba per paràmetre.<br>
    Retorna un objecte json que contindrà “status”:1 i “message”: “El film s’ha actualitzat correctament”.<br>
    En cas d’error retornarà un objecte que contindrà status : -1 i “message”: missatge amb l’error que s’ha produït.
    - Ruta:  /film/{id}<br>
    Tipus de petició: Delete<br>
    Funcionament: Permet eliminar un producte de la BBDD<br>
    Retorna un objecte json que contindrà “status”:1 i “messatge”: “El film s’ha eliminat correctament”.<br>
    En cas d’error retornarà un objecte que contindrà status : -1 i “message”: missatge amb l’error que s’ha produït.
- Consultes avançades:
    - ?genre= (str)
        - valor genre=”Action” | ”Drama” | ”Romance” | ”Thriller” | ”Comedy” | ”Horror” | ”Documentary” | ”Animation”
        - Retorna una llista d’objectes json dels films segons el genre.
        - Exemple ruta amb query parameters: ?genre=Comedy
    - ?field=(str)&order=(str)
        - valor field= “title” | “director” | “year”
        - valor order: “asc” | “desc”
        - Retorna una llista json ordenada ascendent o descendent segons el camp de field.
        - Exemple ruta amb query parameters: ?field=title&orderby=asc
    - ?limit=(int)
        - Valor: 1 - 100
        - Retorna una objecte json amb: 
            - “row_count”: número total de registres 
            - “data”: una llista d’objectes json segons el límit definit en el query parameter.
        - Exemple ruta amb query parameters: ?limit=10
