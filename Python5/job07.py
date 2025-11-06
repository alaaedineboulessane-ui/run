l = [8,24,48,2,16]

def multiple3(liste):
    indice = 0 
    for i in range(len(liste)):
        if liste[i] % 3 == 0:
            indice +=1
    return indice

print(multiple3(l))