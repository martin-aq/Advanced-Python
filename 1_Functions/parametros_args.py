"""This program shows how *args works"""

def calcular_perimetro(*args):
    """Calcular el area de un cuadrado"""
    print(args)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = calcular_perimetro(1, 2, 3, 4)
print(perimetro)

triangulo = calcular_perimetro(1,2,3)
print(triangulo)