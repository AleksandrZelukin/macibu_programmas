
pwr1 = "qwerty"
meginajumi = 3
while meginajumi>0:
    pwr = input("Ievadi parole: ")
    if pwr != pwr1:
        print("Parole nepareiza")
        meginajumi -=1
        print("Tev palika",meginajumi, "meginajumus")
    else:
        print("Parole pareiza!")
        break
