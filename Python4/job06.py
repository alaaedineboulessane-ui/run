def verif(nombre):
    if nombre > 0:
        return "Nombre positif"
    elif nombre < 0:
        return "Nombre négatif"
    return "Nombre égal à 0"

print(verif(2))
print(verif(-2))
print(verif(0))