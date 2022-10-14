'''
Programma trīsstūra un apļa laukuma atrašanu
10.b klases skolniekam palidzibai
'''
import math
while True:
    print("Nulle - iziet no programmas")
    f = input("Izvēles figuru: trīsstūris - 1, aplis - 2, taisnstūris - 3 ")
    list=["a",10,"b",20,"r",34,"c",23,"d",45]
    print("datu saraksts: ",list)
    if f == '1':
        print("trīsstūris")
        print("trijstūra laukums ", (list[1] * list[3])/2)
    if f=='2':
        print("aplis")
        s=math.pi*list[5]**2
        print ("apļa laukums  " ,s)
    if f == '3':
        print("taisnstūris")
        s=list[7]*list[9]
        print ("taisnstūra laukums  " ,s)
    
    
