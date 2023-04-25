"""This program shows how the iter and next built-in methods work"""

numeros = [1,2,3]
iterador = iter(numeros)
print(iterador)

x = next(iterador)  # x = 1
print(x)
x = next(iterador)  # x = 2
print(x)
x = next(iterador)  # x = 3
print(x)
x = next(iterador)  # StopIteration error
print(x)