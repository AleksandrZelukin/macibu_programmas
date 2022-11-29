a = dict()

a[5] = "Piektdiena"
a[2] = "Otrdiena"
a[6] = "Sestdiena"
a[4] = "Ceturtdiena"
a[1] = "Pirmdiena"
a[3] = "Trešdiena"
a[7] = "Svētdiena"


print (a)

for m in a:
    print(m, '->', a[m])

for m in a.items():
    print(m)

for m in a.keys():
    print(m)

for m in a.values():
    print(m)

for m in a:
    print (m,a[m])
    
for m in sorted(a):
    print(m, a[m])


