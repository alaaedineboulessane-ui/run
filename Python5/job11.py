l = [7,11,42,39,2]

def augment(liste):
    for i in range(len(liste)):
        liste[i] +=1
    return liste

print(augment(l))