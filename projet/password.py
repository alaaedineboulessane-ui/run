def verif(password):
    majusc = 0
    minusc = 0
    long = len(password)
    if long < 8:
        return "Mot de passe trop court"
    for i in range(long):
        if password[i].isupper():
            majusc += 1
        if password[i].islower():
            minusc +=1
    if majusc == 0:
        return "Doit contenir au moins une lettre majuscule"
    if minusc == 0:
        return "Doit contenir au moins une lettre minuscule"
    