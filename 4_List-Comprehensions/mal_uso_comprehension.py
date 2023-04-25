"""This programs shows bad case scenarios for list comprehensions"""

# Caso 1
total = sum([num for num in range(100)])    # Creating a list that won't be used
# Correccion
total = sum(num for num in range(100))      # Same result without memory leak


# Caso 2
[print(element) for element in range(1)]    # No need to create a list
# Correccion
for element in range(10):                   # In this case, it's a bit better to display the elements in the conventional way
    print(element)
    

# Caso 3
lista_anidada = [[1, 2], [3, 4], [5, 6]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]   # A bit hard to read it using comprehension
print(valores_lista)

# Correccion
lista_anidada = [[1, 2], [3, 4], [5, 6]]
valores_lista = []
for elemento in lista_anidada:              # In this case, it's a bit better to display the elements in the conventional way
    for numero in elemento:
        valores_lista.append(numero)

print(valores_lista)