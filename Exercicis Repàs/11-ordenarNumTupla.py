# Ex 11 - Demanar a l’usuari que introdueixi 10 números separats per un espai. A l’acabar, el programa els introduirà
# en una tupla i els ordenarà (major o menor, com vulgueu), mostrant per pantalla el contingut de la tupla.

input_nums = input("Introdueix 10 números separats per un espai: ")

numeros = [int(num) for num in input_nums.split()]

if len(numeros) != 10:
    print("Has d'introduïr 10 números!")
else:
    tuplaOrdenada = tuple(sorted(numeros))
    print("Tupla ordenada: " + str(tuplaOrdenada))
