#Trijstura laukuma noteikšana

a = int(input("Pirmais katets: "))
b = int(input("Otrais katets: "))

def tr(a,b):
    return (a*b)/2

s = tr(a,b)

print(s)


r = int(input("radius: "))
def circle(r, pi=3.14):
    return pi*r**2

print(circle(r,4))
print(circle(r))
