import csv

with open("datos.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila["nombre"])