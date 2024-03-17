c ={}
''''
c["Rīga"]="Latvija"
c["Kauņa"]="Lietuva"
c["Ventspils"] = "Latvija"
c["Tallina"] = "Igaunija"
c["Palanga"] ="Lietuva"

for i in c.keys():
    print(c[i],i)

for i in c.items():
    print(i)
'''
while True:
    vards = input("Drauga vārds: ")
    talrunis = input("Tālruna numurs: ")
    if vards =="none" and talrunis=="none":
        for i in c.keys():
            print(c[i],i)
        break
    c[vards] = talrunis
    

