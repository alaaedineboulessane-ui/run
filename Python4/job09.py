def moyenne(a,b,c):
    moy = (a+b+c)/3
    if moy <= 20 and moy >= 15:
        return "Trés bon éleve"
    elif moy <= 14 and moy >= 11:
        return "Bon éleve"
    elif moy <= 10 and moy >= 8:
        return "éleve moyen"
    elif moy <= 7 and moy >= 0:
        return "éleve devant faire des efforts"
    return "Une des notes est soit supérieure à 20 ou négative"