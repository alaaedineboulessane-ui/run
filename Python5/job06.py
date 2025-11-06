l = [1,2,3,4,5]

def inversion(liste):
    element1 = l[0]
    element2 = l[len(liste)-1]
    l[0] = element2
    l[len(liste)-1] = element1
    return liste

print(inversion(l))
