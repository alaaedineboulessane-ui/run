l = [1,2,3,4,5]

def fonction(liste):
    return liste[1]

print(fonction(l))


def remplacement(liste):
    liste[3] = liste[2] + liste[4]
    return liste

print(remplacement(l))


def affiche(liste):
    return liste[len(liste)-1]

print(affiche(l))

