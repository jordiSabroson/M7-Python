# Ex 13 - Demanar a l’usuari posar 2 paraules. 
#         Afegir aquestes a una llista i mostrar per pantalla quantes vegades apareix cada lletra.
paraula1 = input("Introdueix una paraula: ")
paraula2 = input("Una altra paraula: ")
llista = [paraula1, paraula2]

contador = {}
for paraula in llista:
    for lletra in paraula:
        contador[lletra] = contador.get(lletra, 0) + 1
        
print("Cops que apareix cada lletra: ")
for lletra, count in contador.items():
    print(f"{lletra}: {count}")
