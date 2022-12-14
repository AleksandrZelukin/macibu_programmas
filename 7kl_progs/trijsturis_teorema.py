while True:
    h = input("Saksim stadat? (y/n)")
    if h =="y":
        a = input("Pirma mala: ")
        b = input("Otra mala: ")
        c = input("Treša mala: ")
        if a + b > c and a + c > b and b + c > a:
            print("trijsturis ekziste")
        else:
            print("trijsturis neekziste")
    if h =="n":
        break