while True:
#kvadrata perimetru
    a = input("izveles figuru: 1 = kvadrata")
    if a =="1":
        b= float(input("mala:"))
        print(b*4, "perimetru kvadrata: ")

#aretmitisko atzime
    s = float(input("pirma atzime: "))
    d = float(input("otra atzime: "))
    f = float(input("tresa atzime: "))
    n=s+d+f
    print(n/3, "perimetru kvadrata: ")

#Abolu    деньги = float(input("nauda: "))
    цена = float(input("centus par kg: "))
    яблоки = float(input("kg abolu: "))
    заплатит=цена*яблоки
    останется=nauda-jasamaksa
    print("jasamaksa: ", заплатит)
    print("mainīt: ", заплатит)


#vecaka

    Annai = int(input('vecaka annai:'))
    Marutai = int(input('vecaka Marutai:'))
    if Annai>Marutai:
        print('vecaka annai:', Annai)
    else:
        print('vecaka Marutai:', Marutai)