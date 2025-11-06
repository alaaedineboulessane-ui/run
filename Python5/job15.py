l = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondir(liste):
    for i in range(len(liste)):
        liste[i] = int(liste[i])
    return liste

def min(liste):
    min = liste[0]
    indd = 0
    while indd <= len(liste):
        if min > liste[indd-1]:
            min = liste[indd-1]
            indd += 1
        else:
            indd +=1
    return min

def tri(liste):
    liste1 = []
    while liste != []:
        liste1.append(min(liste))
        liste.remove(min(liste))
    return liste1

liste1 = arrondir(l)

print(tri(liste1))