while True:
    a = int(input())
    if a<=0:
        print('nepareizi dati')
        break
    elif a<=3:
        print('zems')
    elif a<=6:
        print('vidējs')
    elif a<=8:
        print('augsts')
    elif a<=10:
        print('ļoti augsts')
    else:
        print ('nepareizi dati')
        break
        