"""This program shows how the for loop works along with the else conditional"""

lista_nombres = ["Paco", "Emilio", "Javier", "Ana"]

for nombre in lista_nombres:
    print(nombre)
else:
    print("Ciclo terminado")
    
print()

for nombre in lista_nombres:
    print(nombre)
    if nombre == 'Javier':
        break
else:
    print("Ciclo terminado")