
def triangle(a,b):
    return a*b/2

def aplis (a):
    return a**2*3.14

while True:
    print("Nulle - iziet no programmas")
    a = input("Izvēles figuru:\n1- trīsstūris\n2 - aplis\n3-taisnstūris\n")
    
    if a=="1":
        print("trisstūris")
        
        x = float(input("pirmais katets= "))
        y = float(input("otrais katets= "))
        d = triangle(x,y)
        print("trisstūta laukums = ",d)
    if a=='2':
        print("aplis")
        x=float(input("radius= "))
        s = aplis (x)
        #s=round(math.pi*r**2,2)
        #print("apļa laukums ", r*r*3.14)
        print ("apļa laukums  " ,s)
        #print ("apļa laukums %.2f " %(s))

    if a=='3':
        print("taisnstūris")
        b=float(input("puse a= "))
        c=float(input("puse b= "))
        d=b*c
        print("taisnstūra laukums = ",d)
                


    if a=="0":
        break
    
    if a=="4":
        continue

