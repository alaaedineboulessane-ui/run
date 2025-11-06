l = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def recup(liste):
    max = liste[0]
    min = liste[0]
    ind = 0
    indd = 0
    while ind <= len(liste):
        if max < liste[ind-1]:
            max = liste[ind-1]
            ind+=1
        else:
            ind+=1
    while indd <= len(liste):
        if min > liste[indd-1]:
            min = liste[indd-1]
            indd += 1
        else:
            indd +=1
    return max, min

print(recup(l))
