# Ex 12 - Demanar 10 cops una paraula diferent a l’usuari. 
# Cada paraula que l’usuari introdueix es guardarà en una llista i es mostrarà per pantalla tota la llista ordenada alfabèticament.
llista = []
for i in range(1, 11):
    paraula = input("Introdueix una paraula ("+str(i)+"/10): ")
    llista.append(paraula)
    
llista.sort()
print(str(llista))