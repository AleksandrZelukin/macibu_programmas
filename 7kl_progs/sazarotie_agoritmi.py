while True:
    Aija = int(input("Aijai abolus : "))
    Vika = int(input("Vikas abolus: "))
    if Aija < Vika :
        print("Vikai vairāk abolus")
    elif Aija == Vika:
        print("Aija un Vika ir vienāds abolu daudzums")
    elif Aija == 0 or Vika == 0:
        break
    else:
        print("Aijai vairāk abolus")