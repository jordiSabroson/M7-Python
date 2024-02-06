# Ex 7 - Demanar una paraula i detectar si és un palíndrom (que es llegeix igual del dret que del revés)
palindrom = input("Introdueix un palíndrom (o no...): ")
palindrom = palindrom.replace(" ", "")
if str(palindrom) == str(palindrom)[::-1]:
    print("ÉS PALÍNDROM!!")
else:
    print("No és palíndrom")
