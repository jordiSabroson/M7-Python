# Ex 9 - Posa un exemple d'una llista, d’una tupla i d’un diccionari i explicar les diferències.
tupla = ("hola", "saluts", "patata")
print("TUPLES: ")
print("Una tupla s'utilitza per emmagatzemar múltiples ítems en una única variable: " + str(tupla))
print("Les tuples estan ordenades i no es poden modificar.")

llista = ["adeu", "siau", "bonvent", "i barcanova"]
print("\nLLISTES: ")
print("Les llistes també s'utilitzen per emmagatzemar múltiples ítems en una única variable: " + str(llista))
print("Les llistes, a diferència de les tuples, es poden modificar")

diccionari = {
    "batua": "l'olla",
    "trosde": "quòniam",
    "gali": "fardeu"
}
print("\nDICCIONARIS: ")
print("Els diccionaris s'utilitzen per emmagatzemar dades amb el format key:value : " + str(diccionari))
print("Es poden modificar, però no permeten valors duplicats")
