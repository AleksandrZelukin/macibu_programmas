a = [34,45,12,23,4,56,12,73,45,16,23,56,]
b = int(input("Ko meklējam?"))



if b in a:
    print("Jā, ir!", b)
    index = a.index(b)
    print(index)

else:
    print("Nē, nav", b)

c = a[::-1]
print(a)
print(c)

j = 0
k = []
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        j+=1
        k.append(a[i])
print(j)
print(k)