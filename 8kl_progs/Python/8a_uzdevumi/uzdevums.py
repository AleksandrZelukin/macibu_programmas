# https://ppt-online.org/952713
aa = [1,4,16,23,14,96]

bb = aa[::-1]
print(bb)

dd =list(map(int,input().split()))
print(dd)
for i in range(len(dd)):
    if dd[i] % 2 ==0:
        print(dd[i],end=" ")




