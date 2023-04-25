"""This program shows what an argument and a parameter are."""

def calcular_area_cuadrado(lado):
    """Calcular el area de un cuadrado"""
    area = lado * lado
    return area

area_cuadrado = calcular_area_cuadrado(lado=5) # parametro(lado)=argumento(5)
print(area_cuadrado)