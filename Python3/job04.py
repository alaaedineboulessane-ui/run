nombre = " "
multiple3 = "Fizz"
multiple5 = "Buzz"
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        nombre += " " + multiple3 + multiple5
    elif i % 3  == 0 :
        nombre += " " + multiple3
    elif i % 5 == 0:
        nombre += " " + multiple5
    else:
        nombre += " " + str(i)
print(nombre)