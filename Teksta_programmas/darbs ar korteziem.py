a = (45,19,23,67,45,78,49,27,18)

b = a[1]
c = a[2:4]
d = list(a)

print(type(d))
print(a)
d.remove(23)

print(d)

e = tuple(d)
print(e)