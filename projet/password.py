def verif(password):
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
        if not password[i] in abc:
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
    

print(verif("alad5in%aaaA"))