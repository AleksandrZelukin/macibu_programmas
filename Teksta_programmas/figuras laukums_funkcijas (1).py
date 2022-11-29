

while True:
    print("Nulle - iziet no programmas")
    a = input("Izvēleis figuru:\n1- trīsstūris\n2- aplis\n3- taisnstūris\n4- rombs\n5- trapece")
    
    if a=="1":
        print("trīsstūris")
        def triangle(a,b):
        return a*b/2
        x = float(input("pirmais katets= "))
        y = float(input("otrais katets= "))
        d = triangle(x,y)
        print("trisstūta laukums = ",d)
        
    if a=="2":
        print("aplis")

        r=float(input("r = "))
        #s=round(math.pi*r**2,2)
        print("apļa laukums ", r*r*3.14)
        #print ("apļa laukums  " ,s)
        #print ("apļa laukums %.2f " %(s))

    if a=="3":
        print("taisnstūris")
        b=float(input("puse a= "))
        c=float(input("puse b= "))
        d=b*c
        print("taisnstūra laukums = ",d)

    if a=="4":
        print("rombs")
        b=float(input("puse b= "))
        c=float(input("puse c= "))
        d=b*c
        print("romba laukums = ",d)

    if a=="5": 
        print("trapece")
        b=float(input("puse b= "))
        c=float(input("puse c= "))
        h=float(input("puse h= "))
        d=b+c/2*h
        print("trapeces laukums = ",d)          


    if a=="0":
        break
    
    if a=="6":
        continue

