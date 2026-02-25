def tristuris(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return "Trijstūris ir derīgs"
    else:
        return "Trijstūris nav derīgs"

x = int(input("Ievadiet pirmo malu: "))
y = int(input("Ievadiet otro malu: "))
z = int(input("Ievadiet trešo malu: "))
print(tristuris(x, y, z))

def taisnsturis(a, b):
    return a * b

x = int(input("Ievadiet taisnstūra pirmo malu metru: "))
y = int(input("Ievadiet taisnstūra otro malu metru: "))
print("Taisnstūra laukums ir:", taisnsturis(x, y), "kvadrātmetri")

a = [12, 15, 10]
b = [20, 19, 76]
c = [30, 25, 40]
def saraksta_papildinasana(saraksts, elements):
    saraksts.append(elements)
    return saraksts

print(saraksta_papildinasana(a, 20))
print(saraksta_papildinasana(b, 30))
print(saraksta_papildinasana(c, 50))