def time_to_text(nombre):
    if type(nombre) == float:
        return "Choisissez un nombre entier"
    elif nombre == 0:
        return "Choisissez un nombre positif"
    question = input("Vous voulez la conversion de minutes ou d'heures ? ")
    if question.lower() == "heure" or question.lower() == "heures":
        return str(nombre * 60) + " minutes" 
    elif question.lower() == "minutes" or question.lower() == "minute":
        minutes = 0
        if nombre < 60:
            return str(nombre) + " minutes"
        elif nombre >= 60:
            if nombre % 60 == 0:
                return str(nombre // 60) + " heures."
            return str(nombre // 60) + " heures et " + str(nombre % 60) + " minutes."

n = int(input("Choisissez votre valeur: "))
print(time_to_text(n))