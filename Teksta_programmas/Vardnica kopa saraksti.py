a = {1,3,5,7,9,11}

b = {1,8,2,4,3}


b.add(7)
b.update([9,11,13,17])

print('a= ',a)
print('b= ',b)
c = a.intersection(b)
d = a.union(b)
print('starpiba starp a un b= ',c)
print('a un b apvienošana= ',d)

d.remove(13)
d.discard(13)
print(d)
