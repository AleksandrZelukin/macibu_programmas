a = dict()

a[5] = "Piektdiena"
a[2] = "Otrdiena"
a[6] = "Sestdiena"
a[4] = "Ceturtdiena"
a[1] = "Pirmdiena"
a[3] = "Trešdiena"
a[7] = "Svētdiena"


print (a)

del a[7]

a.pop(6)

a[8] = "Astotdiena"
print(a)