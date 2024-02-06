# Ex 15 - Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. S’haura de demanar a 
# l’usuari que posi contactes (noms i edats). Si algun nom es repeteix no s'afegeix al diccionari
# (indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

diccionari_contactes = {}
while True:
    nom = input("Introdueix el nom del contacte (escriu 'stop' per acabar): ")
    
    if nom.lower() == 'stop':
        break
    
    if nom in diccionari_contactes:
        print(f"El contacte {nom} ja existeix, no es pot repetir un nom")
        continue
    
    edat = input(f"Introdueix l'edat d'en {nom}: ")
    diccionari_contactes[nom] = int(edat)
    
print("Diccionari de contactes final: ")
print(diccionari_contactes)