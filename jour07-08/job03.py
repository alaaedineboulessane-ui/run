def diagonale(n):
    c = ""
    ind = n
    c += "+"
    for p in range(n):
        c+= "-"
    c+="+"
    c+="\n"
    for i in range(n):
        c += "|"
        for o in range(n):
            if o == ind-1:
                c += " "
            else:
                c += "#"
        ind -= 1
        c += "|"
        c += "\n"
    c += "+"
    for t in range(n):
        c+= "-"
    c+="+"
    c+="\n"
    return c


print(diagonale(20))