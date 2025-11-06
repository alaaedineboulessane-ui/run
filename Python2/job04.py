n = int(input("Entrez un entier supérieur à 0 : "))
print("Voila la table de multiplication de " + str(n) + " : ")
for i in range(11):
    print(str(n) + " x " + str(i) + " = " + str(i * n))