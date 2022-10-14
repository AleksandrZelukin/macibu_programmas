def tr(a,b):
    return a*b/2
def apl(a):
    from math import pi
    return pi * a **2
def td(a,b):
    return a*b            
while True:
    f = input("Izvēles figuru: trīsstūris - 1\naplis - 2\ntainsstūris - 3\niziet no progrāmmas - end\n")
    if f == '1':
        print("trīsstūris")
        
        a = float(input("a= "))
        b = float(input("b= "))
        c=tr(a,b)
        
        print("trijstūra laukums ", c)
    if f == '2':
        print("aplis")
        a = float(input("radiuss= "))
        
        c=apl(a)
        print("apļa laukums ", c)
    if f == '3':
        print("tainsstūris")
        def td(a,b):
            return a*b
        a = float(input("a= "))
        b = float(input("b= "))
        c = td(a,b)
        print("tainsstūra laukums ", c)
    if f=='end':
        break



