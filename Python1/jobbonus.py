def verif(ch):
    if type(ch) == int:
        return "ça doit être une chaine de characteres"
    if ch == "":
        return "C'est vide"
    else:
        for i in range(len(ch)):
            if ch[i] == "e":
                return "oui"
    return "Il n y a pas de E"

print(verif("personne"))