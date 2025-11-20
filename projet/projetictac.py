import random
import time

def choix(reponse):
    tab = ["X", "O"]
    signe = ""
    if reponse == 1:
        return tab[0]
    elif reponse == 2:
        return tab[1]
    else:
        print("Vous avez choisi un mauvas chiffre, un signe aleatoire va être choisi")
        return tab[random.randint(0,1)]


def espace_vide(liste):
    verif = 0
    for i in range(len(liste)):
        if liste[i] == []:
            verif += 1 
    return verif

def victoire(liste):
    if liste[0] == liste[1] and liste[0] == liste[2] and liste[0] != [] and liste[1] != [] and liste[2] != []:
        return True
    elif liste[0] == liste[4] and liste[0] == liste[8] and liste[0] != [] and liste[4] != [] and liste[8] != []:
        return True
    elif liste[2] == liste[4] and liste[2] == liste[6] and liste[2] != [] and liste[4] != [] and liste[6] != []:
        return True
    elif liste[0] == liste[3] and liste[0] == liste[6] and liste[0] != [] and liste[3] != [] and liste[6] != []:
        return True
    elif liste[3] == liste[4] and liste[3] == liste[5] and liste[3] != [] and liste[4] != [] and liste[5] != []:
        return True
    elif liste[2] == liste[5] and liste[2] == liste[8] and liste[2] != [] and liste[5] != [] and liste[8] != []:
        return True
    elif liste[1] == liste[4] and liste[1] == liste[7] and liste[1] != [] and liste[4] != [] and liste[7] != []:
        return True
    elif liste[6] == liste[7] and liste[6] == liste[8] and liste[6] != [] and liste[7] != [] and liste[8] != []:
        return True
    return False
        

def tictac():
    action = ""
    ind = 1
    jeu = [[] for i in range(9)]
    reponse = int(input("Joueur 1 choissisez votre signe (1 pour le signe X, 2 pour le signe O): "))
    signe = choix(reponse)
    signe1 = "O" if signe == "X" else "X"
    ligne_haut = ["haut_gauche", "haut_centre", "haut_droite"]
    ligne_centre = ["centre_gauche", "centre_centre", "centre_droite"]
    ligne_bas = ["bas_gauche", "bas_centre", "bas_droite"]
    question = input("Voulez-vous jouer avec l'ia ? " )
    if question.lower() == "oui":
        print("L'ia vous remercie de l'avoir choisie pour jouer ! " + "\n" + "Démarrage de l'IA...")
        time.sleep(2)
    print("Voilà les placements possibles, il faut taper exactement ce qui est dit: " + "\n" + str(ligne_haut) + "\n" + str(ligne_centre) + "\n" + str(ligne_bas))
    print("Voilà le tableau: ")
    while espace_vide(jeu) != 0:
        while True:
            for i in range(0, 9, 3):
                print(jeu[i:i+3])
            debut = input("\n" + "Joueur numéro 1, jouez le tour numéro " + str(ind) + " ! Où voulez-vous placer votre signe ?: ")
            if debut in ligne_haut or debut in ligne_bas or debut in ligne_centre:
                action = "Joueur 1"
                ind += 1
                if debut == "haut_gauche" and jeu[0] == []:
                    jeu[0] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "haut_centre" and jeu[1] == []:
                    jeu[1] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "haut_droite" and jeu[2] == []:
                    jeu[2] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "centre_gauche" and jeu[3] == []:
                    jeu[3] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "centre_centre" and jeu[4] == []:
                    jeu[4] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "centre_droite" and jeu[5] == []:
                    jeu[5] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "bas_gauche" and jeu[6] == []:
                    jeu[6] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "bas_centre" and jeu[7] == []:
                    jeu[7] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
                elif debut == "bas_droite" and jeu[8] == []:
                    jeu[8] = signe
                    if victoire(jeu) == True:
                        for i in range(0, 9, 3):
                            print(jeu[i:i+3])
                        print("Vérification de la victoire...")
                        time.sleep(3)
                        return "Le " + action + " a gagné !"
                    break
            else:
                print("Vous avez fait un mauvais choix, la case est deja prise ou n'existe pas, veuillez réssayer")
        while True:
            if question.lower() == "oui":
                joke = ["L'IA analyse la situation...", "L'IA réfléchit intensément...", "L'IA calcule son prochain mouvement...", "L'IA cherche la faille dans votre stratégie...", "L'IA observe silencieusement le plateau...", "L'IA prépare une attaque sournoise...", "L'IA fait tourner ses circuits...", "L'IA simule plusieurs scénarios...", "L'IA prend une décision calculée...", "L'IA hésite... puis fait son choix.", "L'IA tente de vous impressionner...", "L'IA s’apprête à jouer un coup stratégique...", "L'IA analyse vos faiblesses...", "L'IA croit tenir la victoire...", "L'IA active son mode tactique...", "L'IA réfléchit plus vite que l'éclair...", "L'IA prépare un mouvement imprévisible...", "L'IA murmure : « Ce coup sera décisif... »", "L'IA effectue un scan tactique du plateau...", "L'IA applique une stratégie secrète..."]
                thinking = joke[random.randint(0,19)]
                action = "Intelligence Artificielle"
                reponse_ia = ia(jeu,signe1)
                if reponse_ia in ligne_haut or reponse_ia in ligne_bas or reponse_ia in ligne_centre:
                    print(thinking)
                    time.sleep(4)
                    if reponse_ia == "haut_gauche" and jeu[0] == []:
                        jeu[0] = signe1
                        print("Votre opposant a placé " + signe1 + "sur la case " + reponse_ia )
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "haut_centre" and jeu[1] == []:
                        jeu[1] = signe1
                        print("Votre opposant a placé " + signe1 + "sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "haut_droite" and jeu[2] == []:
                        jeu[2] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "centre_gauche" and jeu[3] == []:
                        jeu[3] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n" )
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "centre_centre" and jeu[4] == []:
                        jeu[4] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "centre_droite" and jeu[5] == []:
                        jeu[5] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "bas_gauche" and jeu[6] == []:
                        jeu[6] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "bas_centre" and jeu[7] == []:
                        jeu[7] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L'" + action + " a gagné !"
                        break
                    elif reponse_ia == "bas_droite" and jeu[8] == []:
                        jeu[8] = signe1
                        print("Votre opposant a placé " + signe1 + " sur la case " + reponse_ia + "\n")
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "L' " + action + " a gagné !"
                        break
            else:
                debut1 = input("Joueur numéro 2, jouez le tour numéro " + str(ind) + " ! Où voulez-vous placer votre signe ?: ")
                if debut1 in ligne_haut or debut1 in ligne_bas or debut1 in ligne_centre:
                    action = "Joueur 2"
                    if debut1 == "haut_gauche" and jeu[0] == []:
                        jeu[0] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "haut_centre" and jeu[1] == []:
                        jeu[1] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "haut_droite" and jeu[2] == []:
                        jeu[2] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "centre_gauche" and jeu[3] == []:
                        jeu[3] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "centre_centre" and jeu[4] == []:
                        jeu[4] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "centre_droite" and jeu[5] == []:
                        jeu[5] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "bas_gauche" and jeu[6] == []:
                        jeu[6] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "bas_centre" and jeu[7] == []:
                        jeu[7] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    elif debut1 == "bas_droite" and jeu[8] == []:
                        jeu[8] = signe1
                        if victoire(jeu) == True:
                            for i in range(0, 9, 3):
                                print(jeu[i:i+3])
                            print("Vérification de la victoire...")
                            time.sleep(3)
                            return "Le " + action + " a gagné !"
                        break
                    action = "Joueur 2"
                else:
                    print("Vous avez fait un mauvais choix, la case est deja prise ou n'existe pas, veuillez réssayer")
    return "Match nul ! Retentez !"


def ia(board,signe):
    ligne_haut = ["haut_gauche", "haut_centre", "haut_droite"]
    ligne_centre = ["centre_gauche", "centre_centre", "centre_droite"]
    ligne_bas = ["bas_gauche", "bas_centre", "bas_droite"]
    tableau = [ligne_haut, ligne_centre, ligne_bas]
    if board[0] == signe and board[1] == signe and board[2] == []:
        return ligne_haut[2]
    elif board[0] == signe and board[2] == signe and board[1] == []:
        return ligne_haut[1]
    elif board[1] == signe and board[2] == signe and board[0] == []:
        return ligne_haut[0]
    elif board[3] == signe and board[4] == signe and board[5] == []:
        return ligne_centre[2]
    elif board[3] == signe and board[5] == signe and board[4] == []:
        return ligne_centre[1]
    elif board[4] == signe and board[5] == signe and board[3] == []:
        return ligne_centre[0]
    elif board[6] == signe and board[7] == signe and board[8] == []:
        return ligne_bas[2]
    elif board[6] == signe and board[8] == signe and board[7] == []:
        return ligne_bas[1]
    elif board[7] == signe and board[8] == signe and board[6] == []:
        return ligne_bas[0]
    elif board[0] == signe and board[3] == signe and board[6] == []:
        return ligne_bas[0]
    elif board[0] == signe and board[6] == signe and board[3] == []:
        return ligne_centre[0]
    elif board[3] == signe and board[6] == signe and board[0] == []:
        return ligne_haut[0]
    elif board[1] == signe and board[4] == signe and board[7] == []:
        return ligne_bas[1]
    elif board[1] == signe and board[7] == signe and board[4] == []:
        return ligne_centre[1]
    elif board[4] == signe and board[7] == signe and board[1] == []:
        return ligne_haut[1]
    elif board[2] == signe and board[5] == signe and board[8] == []:
        return ligne_bas[2]
    elif board[2] == signe and board[8] == signe and board[5] == []:
        return ligne_centre[2]
    elif board[5] == signe and board[8] == signe and board[2] == []:
        return ligne_haut[2]
    elif board[0] == signe and board[4] == signe and board[8] == []:
        return ligne_bas[2]
    elif board[0] == signe and board[8] == signe and board[4] == []:
        return ligne_centre[1]
    elif board[4] == signe and board[8] == signe and board[0] == []:
        return ligne_haut[0]
    elif board[2] == signe and board[4] == signe and board[6] == []:
        return ligne_bas[0]
    elif board[2] == signe and board[6] == signe and board[4] == []:
        return ligne_centre[1]
    elif board[4] == signe and board[6] == signe and board[2] == []:
        return ligne_haut[2]
    ligne_choisie = random.randint(0,2)
    rand = random.randint(0,2)
    cible = tableau[ligne_choisie][rand]
    tableau[ligne_choisie].pop(rand)
    return cible
                


print(tictac())
