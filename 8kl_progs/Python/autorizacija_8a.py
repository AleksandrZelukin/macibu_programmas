a = {"Anna":"123","Ivars":"456","Anna":"792"}

meginajums = 3
while meginajums >0:
    atslega = input("login: ")
    vertiba = input("parole: ")
    if a.get(atslega) != vertiba:
        print("Lietotājvārds vai parole nesakrīt!")
        meginajums -= 1
        print(f"Tev palikā {meginajums} meģinājums")
    else:
        print("OK!")

