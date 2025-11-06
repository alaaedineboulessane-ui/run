l = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def somme(liste):
    l = 0
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            l += liste[i]
    return l

print(somme(l))
    