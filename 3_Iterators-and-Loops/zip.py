"""This program shows how the built-in Zip function works"""

nombres = ["Paco", "Emilio", "Javier"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo,end="\n\n")

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip,end="\n\n")

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)