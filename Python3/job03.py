nombre = ""
ind = 0
for i in range(101):
    if ind == 26 or ind == 37 or ind == 88:
        ind+=1
    else:
        nombre += " " + str(ind)
        ind += 1
print(nombre)