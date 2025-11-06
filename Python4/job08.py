def fonction(type, saison):
    type1 = type.lower()
    saison1 = saison.lower()
    if type1 == "fruits" and saison1 == "hiver":
        return "Orange, mandarine et kiwi"
    elif type1 == "fruits" and saison1 == "été":
        return "Poire, fraise et cassis"
    elif type1 == "legume" and saison1 == "hiver":
        return "Carotte, topinambour et endive"
    elif type1 == "légume" and saison1 == "été":
        return "Artichaut, aubergine et navet"
    return "On n'a rien pour toi"