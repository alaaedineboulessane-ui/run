def triangle(hauteur):
    c  = ""
    for i in range(hauteur):
        if i == hauteur -1:
            c += " " * (hauteur - i)
            c += "/"
            c += "_" * 2 * i
            c += "\\"
            c += "\n"
        else:
            c += " " * (hauteur - i)
            c += "/"
            c += " " * 2 * i
            c += "\\"
            c += "\n"
    return c

print(triangle(5))

