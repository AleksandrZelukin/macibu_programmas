#import math

while True:
    print("Nulle - iziet no programmas")
    a = input("Izvēles figuru:\n1- trīsstūris\n2 - aplis\n3-taisnstūris\n")
    
    if a=="1":
        print("trisstūris")

        b = float(input("pirmais katets= "))
        c = float(input("otrais katets= "))
        d = b*c/2
        print("trisstūta laukums = ",d)
    if a=='2':
        print("aplis")

        r=float(input("r = "))
        #s=round(math.pi*r**2,2)
        print("apļa laukums ", r*r*3.14)
        #print ("apļa laukums  " ,s)
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

