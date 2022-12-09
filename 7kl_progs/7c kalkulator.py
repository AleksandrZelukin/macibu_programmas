while True:
    a = float(input("Pirmais skaitlis: "))
    b = float(input("Otrais skaitlis: "))

    print("Ko darīsim? * / - +")
    s = input("press end for exit!")

    if s == "*":
        print("Reizināšanas rezulāts: {} ".format(a*b))
    elif s == "/":
        print("Dališanas rezultāts: ",a/b)
    elif s == "-":
        print("Atņemšanas rezultāts: ",a-b)
    elif s == "+":
        print("Summa: ",a+b)
    elif s =="end":
        break