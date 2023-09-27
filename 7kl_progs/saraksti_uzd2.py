a = [12,34,17,3,44,59,78,10,81,52,52,88,77]
b = int(input())
if b in a:
    print('Jā, ir!')
else:
    print("Nē, nav!")

c = a[::-1]
print(a[1:3])
print(a)

j = 0
k = []
for i in range(1,len(a)-1):
    if a[i-1]<a[i] and a[i]>a[i+1]:
        j +=1
        k.append(a[i])

print(j)
print(k)


