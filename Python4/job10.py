def pair(nombre):
    if type(nombre) == float:
        return "Votre numéro doit être un entier"
    elif nombre < 0:
        return "Votre numéro doit être positif"
    elif nombre == 0:
        return "Choissisez un numéro plus grand ou égal à 1"
    if nombre % 2 == 0:
        return "Votre numéro est pair"
    return "Votre numéro est impair"

print(pair(4))