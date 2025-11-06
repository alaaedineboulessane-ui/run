valeur1 = int(input("Choisissez votre premiere valeur: "))
valeur2 = int(input("Choisissez votre deuxieme valeur: "))
if valeur1 > valeur2:
    print(str(valeur1) + "est supérieur à " + str(valeur2))
elif valeur1 < valeur2:
    print(str(valeur1) + "est inférieur à " + str(valeur2))
elif valeur1 == valeur2:
    print(str(valeur1) + " et " + str(valeur2) + " sont égaux ")