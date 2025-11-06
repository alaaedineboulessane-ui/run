l = [4,8,9,2,7,99,5,0,2,5,8,48,8,825,]

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

print(tri(l))
