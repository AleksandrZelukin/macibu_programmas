a=[1, 2, 3, 4]
b=["blue", "red", "orange"]

for i in a:
    print(i)
for k in b:
    print(k)

c = {
    "1": "Pirmdiena",
    "2": "Otrdiena",
    "3": "Trešdiena",
    "4": "Ceturdiena",
    "5": "Piektdiena",
    "6": "Sestdiena",
    "7": "Svētdiena"
}

print (c)
for m in c:
    print(m, '->', c[m])

for m in c.items():
    print(m)

for m in c.keys():
    print(m)

for m in c.values():
    print(m)

for m in sorted(c):
    print(m, c[m])



