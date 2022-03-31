a = {9:"fifa", 12:"Dina"}


a[1]='Pirmdiena'
a[2] = 'Otrdiena'
a[7] = 'Svētdiena'
a[3] = 'Trešdiena'

a[8] = 'Astotadiena'
a[8] = 'Liekasdiena'
a[2] = 'Marts'

del a[2]

a.pop(8)
for i in a:
    print(i,a[i])

print(a[7])


