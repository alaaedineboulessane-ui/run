def doublons(liste):
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat

l = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(doublons(l))
