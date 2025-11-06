def doublons(liste):
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat

def sort(liste):
    coups = 0
    tri = False
    while not tri:
        tri = True
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                coups += 1
                tri = False
    question = input("Voulez-vous supprimer les doublons dans la liste ? ")
    if question.lower() == "oui":
        return "Le nombre de coups est de " + str(coups) + " et voilà la liste triée sans doublons: " + str(doublons(liste))
    return "Le nombre de coups est de " + str(coups) + " et voilà la liste triée: " + str(liste)

print(sort([1,4,3,6,99,0,2,3,4,8,7,9,6,3,9,7,8,8,8,5,2,2,2,233,87,8,8,9,6,5,5,5,4,4,4]))