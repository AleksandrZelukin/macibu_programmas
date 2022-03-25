import math
while True:
    print("Izvēles figuru:\n trījstūris - 1, aplis - 2 , tainsstūris - 3")
    f = input()
    if f == '1':
        print("trīsstūris")
        a = float(input("a = "))
        b = float(input("b = "))
        print("trijstūra laukums ", (a * b)/2)
    if f=='2':
        print("aplis")
        r=float(input("r = "))
        s=math.pi*r**2
        print ("apļa laukums  " ,s)
    if f=='3':
        print("tainsstūris")
        a = float(input("a = "))
        b = float(input("b = "))
        print("tainsstūra laukums ", (a * b))
    if f=='0':
        break


