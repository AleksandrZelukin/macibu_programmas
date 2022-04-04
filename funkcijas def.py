def tr (a,b,c):

    if a+b>c or a+c>b or b+c>a:
        return a+b+c
    else:
        print("trijsturis neeksiste")
    

a=int(input())
b=int(input())
x=int(input())
print(tr(a,b,x))
