def invers(ch):
    if type(ch) != str:
        return "Le type de l'argument doit être str"
    elif ch == "":
        return "Votre chaine de characteres est vide"
    hc = ""
    l = len(ch)
    for i in range (l):
        hc += ch[l-1-i]
    return hc

print(invers("aladin"))