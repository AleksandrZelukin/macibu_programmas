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
    pilseta = input("Pilsēta: ")
    valsts = input("valsts: ")
    if pilseta =="none" and valsts=="none":
        for i in c.keys():
            print(c[i],i)
        break
    c[pilseta] = valsts
    

