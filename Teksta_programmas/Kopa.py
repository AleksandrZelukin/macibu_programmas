a = set()
# https://foxford.ru/wiki/informatika/rabota-s-tekstovymi-faylami-v-python
b = {10,22,46,17}

#print (a)
#print (b)
a = {'pirmdiena', 'otrdiena', 'trešdiena',4,5,6,'svētdiena'}

a.add('cetrurdiena')
a.update(['piektdiena','sestdiena'])

print (a)

a.remove(4)
a.discard(5)

print(a)

for i in a:
    print(i)



