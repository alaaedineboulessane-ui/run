pair = ""
impair = ""
for i in range(1,31):
    if i % 2 == 0:
        pair += " " + str(i)
    if i % 2 != 0:
        impair += " "  + str(i) 
print("Voilà tous les nombres pairs allant de 1 à 31 :" + pair)
print("Et voilà tous les nombres impairs allant de 1 à 31 :" + impair)

#sans if 

pair1 = ""
impair1 = ""
for i in range(2,31,2):
    pair1 += " " + str(i) 
    impair1 += " " + str(i-1)

print("Voilà tous les nombres pairs allant de 1 à 31 :" + pair1)
print("Et voilà tous les nombres impairs allant de 1 à 31 :" + impair1)