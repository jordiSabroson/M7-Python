# Ex 6 - Posar entre 2 i 3 paraules. A l’executar el programa, mostrarà les paraules indicades per l’usuari, indicar quants caràcters
#       té i indicar el primer, i l’últim caràcter.
paraules = input("Introdueix entre 2 i 3 paraules: ")
numParaules = len(paraules.split())
c = 0
for i in range (0, len(paraules)):
    if (paraules[i] != ' '):
        c = c + 1
primeraLletra = paraules[0]
ultimaLletra = paraules[-1]
print("Paraules indicades: ", paraules, "\nNúmero de paraules: ", numParaules, "\nNúmero de caràcters: ", c, "\nPrimera lletra: ", primeraLletra, "\nÚltima lletra: ", ultimaLletra)
