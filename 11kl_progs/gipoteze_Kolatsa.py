a = int(input())

while True:
    if a//2==0:
        a = a*3+1
        print(a)

    elif a//2!=0:
        a = a/2
        print(a)
    if a==1:
        break