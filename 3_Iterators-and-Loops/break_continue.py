"""This program shows how the reserved keywords Break and Continue work"""

nombres = ["Paco", "Emilio", "Javier"]
for elemento in nombres:
    if elemento == "Emilio":
        break
    print(elemento)
    
print()

for elemento in nombres:
    if elemento == "Emilio":
        continue
    print(elemento)