# Ex 5 - Introduïr un valor decimal (en €), seguidament demanar que introdueixi el IVA a aplicar-hi (4, 10 o 21%) i finalment mostrar
#        per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.
valor = float(input("Introdueix un valor en €: "))
iva_valid = [4, 10, 21]
iva = ''
while iva not in iva_valid:
    iva = int(input("Escull un IVA a aplicar (4, 10 o 21%): "))
    if iva not in iva_valid:
        print("Escull un valor d'IVA correcte!")
total = valor * (iva / 100)
print("Valor introduit: ", valor, "\nIVA demanat: ", iva, "\nTotal: ", total)