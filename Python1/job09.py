nom = "Pomme"
prix_unitaire = 1
quantite_en_stock = 20
print(" Chaque " + nom + " coute " + str(prix_unitaire) +" euros, et il y'en a " + str(quantite_en_stock))
quantite_en_stock -= int(input("Combien de " + nom + " voulez-vous acheter ?"))
print("Il reste maintenant " + str(quantite_en_stock) + str( nom))
print("Le prix de " + nom + "est monté de 10%")
prix_unitaire *= 1.10
print("Le prix est donc de " + str(prix_unitaire) + "euros")

