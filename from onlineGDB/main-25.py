
while True:
    print("Lai noteikt laukums \ntaisnstura - 1\ntrijstura - 2\napla - 3")
    k=int(input())
    if k == 1:
        a = int(input("#taisnstura puse 1: "))  
        b = int(input("#taisnstura puse 2: ")) 
        s = a*b 
        print("#taisnstura laukums: ",s)

    elif k==2:
        a = int(input("#trijstura pamats: "))  
        b = int(input("#trijstura augstums: ")) 
        s = a*b/2
        print("#trijstura laukums: ",s)

    elif k==3:
        r=int(input("radius: "))
        from math import pi
        s=pi*r**2
        print("apla laukums: ",s)
    
    else:
        print("nepareizi dati!")
        break

