a = []

while True:
    jautajums = int(input("Vārds vai skaitlis? 1-vards, 2-skaitlis"))
    if jautajums == 1: 
        z = int(input("Izvēlēs poziciju: "))
        x = input("vārds: ")
        a.insert(z,x)
        print(a)

    elif jautajums == 2:
        z = int(input("Izvēlēs poziciju: "))
        x = int(input("skaitlis: "))
        a.insert(z,x)
        print(a)
    if jautajums == 0:
        break
        
