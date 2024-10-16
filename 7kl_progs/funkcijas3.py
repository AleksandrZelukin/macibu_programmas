from math import pi
r = int(input("Ievadi radius: "))

def a(r):
    s = pi*r**2
    return s

x = a(r)

print("Apļa laukums ir: ", round(x,2))