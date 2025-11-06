nombre = ""
for i in range(2, 1001):
    est_premier = True
    for n in range(2, int(i**0.5) + 1):
        if i % n == 0:
            est_premier = False
            break
    if est_premier:
        nombre += " " + str(i)

print(nombre)
