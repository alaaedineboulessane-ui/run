v1 = 1000   
v2 = 1



augmentation = int(input("de combien a augmenté le capital ?"))
rend = int(input("et combien de rendement ?"))
v1 += augmentation 
v2 = rend

baisse = v1 * 0.90
v2 -= 1
print(baisse,v2)
gain = "Le gain annuel est de " + str((v1*(v2/100)))


print(gain)