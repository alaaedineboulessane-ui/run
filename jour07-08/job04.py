def cesar(message, decalage):
    abc = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for caractere in message:
        index = abc.index(caractere)               
        indd = (index + decalage) % 26   
        resultat += abc[indd]            
    return resultat

print(cesar('aladin',4))