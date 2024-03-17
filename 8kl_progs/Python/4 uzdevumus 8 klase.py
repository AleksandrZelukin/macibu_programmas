'''
Programma pieprasa kvadrāta mālu a un izskaitļo perimetru (2.punkti)
Programma pieprasa Kārļa trīs atzīmes un izskaitļo vidējo aritmētisko. (2.punkti)
Kārlis noperka M kg abolu maksājot C centus par kg. Cik centus X ir jāsamaksa par pirkumu? Cik atlikuma centus S viņš dabūs no L eiro? (4.punkti)
Annai ir a gadi, bet Marutai - m gadi. Kas no viņam ir vecāka? (2.punkti)
Pļavā rotaļājas bērni un suņi. Zinot galvu un kāju kopējo skaitu (g un k), atrast, cik bērnu un cik suņu ir pļavā (b un s). (6.punkti)

#1 
a = int(input("Ievadiet kvadrata malu: "))
p=a*4
print("Kvadrata perimetrs ir:",p )

#2
a1 = int(input("Pirma atzime: "))
a2 = int(input("Otra atzime: "))
a3 = int(input("Tresa atzime: "))

v=(a1+a2+a3)/3

print("videja atzime ir:",v)

#3

L = int(input("Nauda kopa:"))
M = int(input("aboli kg:"))
C = float(input("cena par kilo: "))
x=L-(M*C)
print("atlikums:",x)
'''
#4
Anna = int(input("Annai:"))
Maruta = int(input("Marutai:"))
if Anna > Maruta:
    print("Anna ir vecāka par Maruta")
else:
    print("Maruta ir vecāka par Annu")
    

