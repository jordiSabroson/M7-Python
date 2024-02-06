# Ex 10 - Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla 
# el mes corresponent al número indicat per l’usuari. 
mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

num = input("Introdueix un número entre el 0 i el 11: ")
print(str(mesos[int(num)]))