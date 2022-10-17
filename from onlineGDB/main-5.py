a=[34, 45, 53, 12, 68, 24]
b=["Red", "Blue", "orange", "Magenta"]
a.append(101)
c=a+b
print(a)

a.insert(1, 202)
print(a)

a.remove(53)
print(a)
del a[4]
print(a)
print(b)
print(c)