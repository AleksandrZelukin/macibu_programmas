#Produktu uzpirkšana pec iepriekš zināmu summu
#Saraksti
cenas = [1.40, 2, 1.37, 0.40, 2.70, 0.30]

nauda = float(input())

for k in cenas:
    if k <= nauda:
        print(k)
        nauda -= k

#Vardnicas
cenas = {"Piens":1.40,
         "Siers": 2,
         "Sviests": 1.37,
         "Konfekte": 0.40,
         "Biezpiens": 2.70,
         "Salvetes": 0.30}

nauda = float(input())
print("Ar lambda funkciju")
cenas_sorted = dict(sorted(cenas.items(), key=lambda s: s[::-1]))
for i,m in cenas_sorted.items():
    if m <= nauda:
        print(i, sep='/n')
        nauda -=m
print("bez lambda funciju")
for i,m in cenas.items():
    if m <= nauda:
        print(i, sep='/n')
        nauda -=m
