a = {"Ivars":"123","Olga":"123","Igors":"789"}

meginajums = 3
while meginajums > 0:
    vards = input("Login: ")
    parole = input("parole: ")
    if a.get(vards) != parole:
        print("Lietotājvārds vai parole nesakrīt!")
        meginajums -= 1
        print(f"Jūmas palikā {meginajums} meģinājums")
    else:
        print("OK!")
        break
        
