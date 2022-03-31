a={}
a[3] = 'Trešdiena'
a[4] = 'Ceturtdiena'

a[1] = 'Pirmdiena'
a[6] = 'Sestdiena'
a[5] = 'Piektdiena'
a[2] = 'Otrdiena'
a[7] = 'Svētdiena'


for i in sorted(a):
    print(i,a[i])

del a[1]
a.pop(2)

for i in sorted(a):
    print(i,a[i])

