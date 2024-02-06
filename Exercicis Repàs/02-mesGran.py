# Ex 2 - Demanar 2 valors numèrics i mostrar, per pantalla, la suma dels dos valors i quin és el més gran.
x = int(input("Introdueix un número: "))
y = int(input("Un altre número: "))
print("Suma: ", x + y)
mesGran = max(x, y)
print("El més gran és: ", mesGran)