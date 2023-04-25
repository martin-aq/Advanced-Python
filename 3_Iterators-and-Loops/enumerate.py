"""This program shows how the built-in Enumerate function works"""

"""
enumerate(iterable, start=0)
"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = list(enumerate(nombres,start=5))
# print(nombres_enumerados,end="\n\n")

for indice, elemento in enumerate(nombres):
    print(indice, elemento)