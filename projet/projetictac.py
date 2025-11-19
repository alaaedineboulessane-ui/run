import random

def tictac(choix):
    tab = ["X", "O"]
    signe = ""
    while choix != "X" or choix != "O"
        if choix == 1:
            signe = tab[0]
        elif choix == 2:
            signe = tab[1]
        else:
            signe = tab[random.randint(0,1)]
            return "Choix indisponible, choix aléatoire attribué" + signe
    return "Votre signe est " + signe

