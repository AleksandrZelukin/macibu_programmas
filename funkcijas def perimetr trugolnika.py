def tr (a,b,c):

    if a+b>c and a+c>b and b+c>a:
        return a+b+c
    else:
        print("trijsturis neeksiste")
    

a=int(input())
b=int(input())
x=int(input())
print(tr(a,b,x))
