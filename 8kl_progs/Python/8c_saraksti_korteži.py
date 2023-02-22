a = []
a.append(4)
a.append('D')
a.append(5)
a.append('E')
a.insert(1,2)
a.append('abba')
aa = input()
a.append(aa)
print(a)
a.remove('E') #dzēšanas pēc vertibas
print(a)
bb = a.pop(1) #dzešanas pēc indeksa
print(a)
bb = a.pop()
print(a)

b =tuple(a)
a = list(b)
print(b)
print(a)