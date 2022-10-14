import math
def trisstur(a,b):
    return (a*b/2)
def aplis(r):
    return math.pi*a**2
def taisnsturis(a,b):
    return a*b
    
while True:
    f = input("Izvēles figuru: trīsstūris - 1, aplis - 2, tainsstūris - 3")
    
    if f == '1':
        print("trīsstūris")
        x = float(input("a= "))
        y = float(input("b= "))
        c = trisstur(x,y)
        print("trijstūra laukums ", c)
    
    if f == '2':
        print("aplis")
        a = float(input("a= "))
        c = aplis(a)
        print("apļa laukums ", c)
    
    if f == '3':
        print("tainsstūris")
        a = float(input("a= "))
        b = float(input("b= "))
        c = taisnsturis(a,b)
        print("tainsstūra laukums ", c)
    
    if f=='end':
        break


