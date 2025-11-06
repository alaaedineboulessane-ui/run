def forme(largeur, hauteur):
    c = ""
    for o in range(hauteur):
        c += "|"
        for i in range(largeur):
            if  o == 0 or o == hauteur-1:
                c += "-"
            else:
                c += " "
        c += "|"
        c += "\n"
    return c

print(forme(10,5))
        

    

