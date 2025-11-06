l = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def somme_intervalle(liste):
    somme = 1
    for i in range(len(liste)):
        if liste[i] >= 25 and liste[i] <= 90:
            somme *= liste[i]
    return somme

print(somme_intervalle(l))