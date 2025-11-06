def verif(langage):
    casse = langage.lower()
    if casse == "javascript":
        return "Tu es un développeur web"
    elif casse == "python":
        return "Tu es un développeur IA"
    elif casse == "java":
        return "Tu es un développeur logiciel"
    elif casse == "reactjs":
        return "Tu es un développeur mobile"
    return "Un jour je serai le meilleur développeur"