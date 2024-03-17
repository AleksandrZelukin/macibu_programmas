nauda = float(input("Karlim ir: "))
aboli = float(input("Aboli maksa: "))
svars = float(input("Karlis grib pirkt(kg) abolus: "))
maksa = aboli * svars
atlikums = nauda - maksa

if atlikums < 0:
    print("Karlim japieprasa mammai vel", atlikums*-1,"euro")
else:
    print("Karlim palika",round(atlikums,2),"EIRO")
