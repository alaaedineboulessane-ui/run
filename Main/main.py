#Ceci est un fichier qui va contenir toutes les fonctions que j'aurais crées


import hashlib
import json
import os
def verif(password):
    special = "!@#$%^&*"
    majusc = 0
    minusc = 0
    chiffre = 0
    spec = 0
    long = len(password)
    if long < 8:
        return "Mot de passe trop court"
    for i in range(long):
        if password[i].isupper():
            majusc += 1
        if password[i].islower():
            minusc +=1
        if password[i].isdigit():
            chiffre += 1
        if password[i] in special:
            spec += 1
    if majusc == 0:
        return "Doit contenir au moins une lettre majuscule"
    elif minusc == 0:
        return "Doit contenir au moins une lettre minuscule"
    elif chiffre == 0:
        return "Doit contenir au moins un chiffre"
    elif spec == 0:
        return "Doit contenir au moins un charactere special"
    return "Votre mot de passe est solide"
def cryptage(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()
def fichier(chiffre):
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            data = json.load(f)
    else:
        data = {"mots_de_passe": []}
    for i in range(chiffre):
        mdp = input(f"Entrez le mot de passe {i+1} : ")
        data["mots_de_passe"].append(mdp)
    data["mots_de_passe"] = list(set(data["mots_de_passe"]))
    for o in range(len(data["mots_de_passe"])):
        data["mots_de_passe"][o] = cryptage(data["mots_de_passe"][o])
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"{chiffre} mot(s) de passe ajouté(s) avec succès !")
def afficher_fichier():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data["mots_de_passe"]
    
    

import random

def choix(reponse):
    tab = ["X", "O"]
    signe = ""
    if reponse == 1:
        return tab[0]
    elif reponse == 2:
        return tab[1]
    else:
        return tab[random.randint(0,1)]


def espace_vide(liste):
    verif = 0
    for i in range(len(liste)):
        if liste[i] == []:
            verif += 1 
    return verif

def victoire(liste):
    if liste[0] == liste[1] and liste[0] == liste[2] and liste[0] != [] and liste[1] != [] and liste[2] != []:
        return True
    elif liste[0] == liste[4] and liste[0] == liste[8] and liste[0] != [] and liste[4] != [] and liste[8] != []:
        return True
    elif liste[2] == liste[4] and liste[2] == liste[6] and liste[2] != [] and liste[4] != [] and liste[6] != []:
        return True
    elif liste[0] == liste[3] and liste[0] == liste[6] and liste[0] != [] and liste[3] != [] and liste[6] != []:
        return True
    elif liste[3] == liste[4] and liste[3] == liste[5] and liste[3] != [] and liste[4] != [] and liste[5] != []:
        return True
    elif liste[2] == liste[5] and liste[2] == liste[8] and liste[2] != [] and liste[5] != [] and liste[8] != []:
        return True
    elif liste[1] == liste[4] and liste[1] == liste[7] and liste[1] != [] and liste[4] != [] and liste[7] != []:
        return True
    elif liste[6] == liste[7] and liste[6] == liste[8] and liste[6] != [] and liste[7] != [] and liste[8] != []:
        return True
    return False
        

def tictac(choix):
    action = ""
    ind = 1
    jeu = [[] for i in range(9)]
    reponse = int(input("Joueur 1 choissisez votre signe (1 pour le signe X, 2 pour le signe O): "))
    signe = choix(reponse)
    signe1 = "O" if signe == "X" else "X"
    ligne_haut = ["haut_gauche", "haut_centre", "haut_droite"]
    ligne_centre = ["centre_gauche", "centre_centre", "centre_droite"]
    ligne_bas = ["bas_gauche", "bas_centre", "bas_droite"]
    print("Voilà les placements possibles, il faut taper exactement ce qui est dit: " + "\n" + ligne_haut + "\n" + ligne_centre + "\n" + ligne_bas)
    while espace_vide(jeu) != 0:    
        debut = input("Joueur numéro 1, jouez le tour numéro " + str(ind) + " ! Où voulez-vous placer votre signe ?: ")
        if debut in ligne_haut or debut in ligne_bas or debut in ligne_centre:
            if debut == "haut_gauche" and jeu[0] == []:
                jeu[0] = signe
            elif debut == "haut_centre" and jeu[1] == []:
                jeu[1] = signe
            elif debut == "haut_droite" and jeu[2] == []:
                jeu[2] = signe
            elif debut == "centre_gauche" and jeu[3] == []:
                jeu[3] = signe
            elif debut == "centre_centre" and jeu[4] == []:
                jeu[4] = signe
            elif debut == "centre_droite" and jeu[5] == []:
                jeu[5] = signe
            elif debut == "bas_gauche" and jeu[6] == []:
                jeu[6] = signe
            elif debut == "bas_centre" and jeu[7] == []:
                jeu[7] = signe
            elif debut == "bas_droite" and jeu[8] == []:
                jeu[8] = signe
            action = "Joueur 1"
            if victoire(jeu) == True:
                for i in range(0, 9, 3):
                    print(jeu[i:i+3])
                return "Le " + action + " a gagné !"
        else:
            print("Vous avez fait un mauvais choix, la case est deja prise ou n'existe pas, veuillez réssayer")
        debut1 = input("Joueur numéro 2, jouez le tour numéro " + str(ind) + " ! Où voulez-vous placer votre signe ?: ")
        if debut1 in ligne_haut or debut1 in ligne_bas or debut1 in ligne_centre:
            if debut1 == "haut_gauche" and jeu[0] == []:
                jeu[0] = signe1
            elif debut1 == "haut_centre" and jeu[1] == []:
                jeu[1] = signe1
            elif debut1 == "haut_droite" and jeu[2] == []:
                jeu[2] = signe1
            elif debut1 == "centre_gauche" and jeu[3] == []:
                jeu[3] = signe1
            elif debut1 == "centre_centre" and jeu[4] == []:
                jeu[4] = signe1
            elif debut1 == "centre_droite" and jeu[5] == []:
                jeu[5] = signe1
            elif debut1 == "bas_gauche" and jeu[6] == []:
                jeu[6] = signe1
            elif debut1 == "bas_centre" and jeu[7] == []:
                jeu[7] = signe1
            elif debut1 == "bas_droite" and jeu[8] == []:
                jeu[8] = signe1
            action = "Joueur 2"
            if victoire(jeu) == True:
                for i in range(0, 9, 3):
                    print(jeu[i:i+3])
                return "Le " + action + " a gagné !"
        else:
            print("Vous avez fait un mauvais choix, la case est deja prise ou n'existe pas, veuillez réssayer")
        ind += 1
        for i in range(0, 9, 3):
            print(jeu[i:i+3])
    return "Match nul ! Retentez !"



                



