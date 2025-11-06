def mots_long(chiffre, str):
    points = ","
    liste = []
    for i in str:
        if i == points:
            str = str.replace(i," ")
    str = str.split()
    for n in str:
        if len(n) > chiffre:
            liste.append(n)
    return liste

print(mots_long(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance "))
