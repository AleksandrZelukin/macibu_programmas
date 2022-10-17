'''
Geometrisko figuru laukuma noteiksana
'''
a = int(input("Ievadi pirmu pusi: ")) #pirma puse

b = int(input("Ievadi otru pusi: ")) #otra puse


s = a*b #taisnstura laukums


print("Taisnstura laukums: ",s)

a = int(input("Ievadi trisstura pamats: ")) 

b = int(input("Ievadi trisstura augtumu: "))

c = a

s = c*b/2

print("Trisstura laukums: ",s)

r = int(input("Ievadi radius: "))

from math import pi

s = r**2*pi

print("Apla laukums: ",s)
