
a=list(map(int, input().split()))

b = int(input("Ko meklējam? "))

if b in a:
    print("Jā, ir")
    index = a.index(b)
    print(index)
else:
    print("Nē, nav")

c = a[::-1]
print(c)

#Определите, сколько в  списке
#элементов, которые больше двух своих соседей, и
#выведите количество таких элементов.
j = 0
k=[]
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        j+=1
        k.append(a[i])
print(j)
print(k)

