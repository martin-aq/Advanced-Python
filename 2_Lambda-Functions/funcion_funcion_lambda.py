"""This program shows whether it is convenient to turn a function into 
   a lambda function
"""

# def separar_par_impar esta construida a partir de varias instrucciones, no apta para funcion lambda
def separar_par_impar(lista_numeros):
    """Separa numeros pares e impares"""
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# def calcular_area_cuadrado es una expresion sencilla, se puede transformar a funcion lambda
def calcular_area_cuadrado(lado):
    return lado ** 2


calcular_cuadrado = lambda lado: lado ** 2
print(calcular_cuadrado(2))