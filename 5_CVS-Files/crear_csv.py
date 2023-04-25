"""This program shows how to create a CSV File using the CSV Library"""

import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "C:\\Users\\marti\\OneDrive\\Escritorio\\PythonAvanzado\\5_CVS-Files\\csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)

# archivo_abierto = open(ruta, "w")
# writer = csv.writer(archivo_abierto, delimiter=",")
# archivo_abierto.close()