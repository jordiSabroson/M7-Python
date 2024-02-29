# Ex 8 - Desenvolupar un programa que primerament esculli aleatòriament un número entre 1 i 100. 
#        Després l’usuari haurà d’anar afegint un número fins que l’encerti. 
#        Cada vegada que l’usuari hi posi un número, caldrà indicar si és més petit o més gran.
#        Un cop l’encerti caldrà d’indicar que l’ha encertat i mostrar el número d’intents.
import random
num = random.randint(1, 100)
usuari = int(input("Endevina un número del 1 al 100: "))
while num != usuari:
    if num > usuari:
        print("El número secret és més GRAN")
        usuari = int(input("Introdueix el número: "))
    elif num < usuari:
        print("El número secret és més PETIT")
        usuari = int(input("Introdueix el número: "))
print("Has endevinat el número! Era el " + str(num))