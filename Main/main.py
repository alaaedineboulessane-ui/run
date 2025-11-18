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