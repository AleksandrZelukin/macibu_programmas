perimetrus_saraksts = []
while True:
    a_mala = int(input('a_mala>> '))
    b_mala = int(input('b_mala>> '))
    c_mala = int(input('c_mala>> '))
   
    if a_mala+b_mala>c_mala and a_mala+c_mala>b_mala and b_mala+c_mala>a_mala:
        print('Trijsturis ekziste, perimerts=')
        p = a_mala+b_mala+c_mala
    else:
        print('Trijstruris neekziste')
    perimetrus_saraksts.append(p)
    print(perimetrus_saraksts)