l1 = int(input("Choissisez votre premiére longueur: "))
l2 = int(input("Choissisez votre deuxième longueur: "))
l3 = int(input("Choisissez votre troisième longueur: "))

if l1 > 0 and l2 > 0 and l3 > 0:
    if l1 == l2 == l3:
        print("Votre triangle est équilateral")
    elif l1 != l2 and l1 != l3:
        print("Votre triangle est rectangle")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        if l1 != l2 or l1 != l2 or l2 != l3:
            print("Votre triangle est réctangle isoscéle")
        else:
            print("Votre triangle est isoscéle")
else:
    print("Il y a une mesure qui est inférieure ou égale à 0 vous ne pouvez donc pas faire de triangle")