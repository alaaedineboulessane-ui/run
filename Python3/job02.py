age = int(input("Quel âge avez vous ?"))
if age < 18:
    print("Tu ne peux pas voter")
elif age >= 18:
    print("Tu peux voter")