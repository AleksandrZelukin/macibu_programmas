
N = int(input());
a = list(map(int,input().split()));

for i in a:
    if a[i]>a[i-1] and a[i]>a[1+1]:
        print(a[::1])
    #if a[i]<a[i-1] and a[i]<a[i+1]:
    #    print(a)