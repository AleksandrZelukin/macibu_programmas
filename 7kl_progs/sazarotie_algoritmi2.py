while True:

    Maija=int(input("Majas vēcums ir: "))
    Nika=int(input("Nikas vēcums ir: "))
    
    if Maija > Nika:
        print("Maija vecaka neka Nika")
    elif Maija == Nika:
        print("Maijas un Nikas vēcums ir vienāds!")
    else:
        print('Nika vēcaka neka Maija')
    if Maija ==0 or Nika ==0:
        break