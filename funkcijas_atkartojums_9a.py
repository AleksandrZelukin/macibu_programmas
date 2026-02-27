def ss(a,b):
    s = a*b
    print(s)
def sa(a,b):
    s = a+b
    print(s)
def sd(a,b):
    s = a-b
    print(s)
def se(a,b):
    s = a/b
    print(s)
k = int(input("Ievadiet pirmo skaitli: "))
l = int(input("Ievadiet otro skaitli: "))
print("ko darisim?: a - reizinat, s - saskaitit, d - atņemt, e - dalīt")
n = input("Ievadiet darbību: ")
print(f"Jūs izvēlējāties: {n} un ar {k} un {l} rezultāts ir:")
if n == "a":
    ss(k,l)
elif n == "s":
    sa(k,l)
elif n == "d":
    sd(k,l)
elif n == "e":
    se(k,l)
    
