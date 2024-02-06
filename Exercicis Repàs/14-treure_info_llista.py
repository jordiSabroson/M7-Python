# Ex 14 - Cal buscar la informació que es demana de la següent list:
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Imprimir el segon element: " + str(areas_pis[1]))

print("Imprimir l’últim element: " + str(areas_pis[-1]))

print("Imprimir l’àrea de la terrassa: " + str(areas_pis[areas_pis.index("Terrassa") + 1]))

print("Imprimir del primer element al tercer element: " + str(areas_pis[:3]))

print("Imprimir del tercer element a l’últim: " + str(areas_pis[2:]))

area_hab1 = areas_pis[areas_pis.index("Habitació1") + 1]
area_hab2 = areas_pis[areas_pis.index("Habitació2") + 1]
print("Imprimir el total de l'àrea de les dues habitacions: " + str(area_hab1 + area_hab2))

index_lavabo = areas_pis.index("Lavabo")
nova_area_lavabo = 6.66
areas_pis[index_lavabo + 1] = nova_area_lavabo
print("Modificar l’àrea del lavabo i imprimir la nova list area: " + str(areas_pis))

areas_pis.append("Pati interior")
areas_pis.append(2.78)
print("Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area: " + str(areas_pis))

totes_areas = areas_pis[1::2]
print("Imprimir el total de l’àrea del pis: " + str(sum(totes_areas)))