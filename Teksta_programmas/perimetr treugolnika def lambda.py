a=int(input())
b=int(input())
c=int(input())

if a+b>c and a+c>b and b+c>a:
    p=a+b+c
    print("trijsturis ekziste")

else:
    print("trijsturis neekziste")



def tr (a,b,c):

    if a+b>c and a+c>b and b+c>a:
        return a+b+c
    else:
        print("trijsturis neeksiste")
    

a=int(input())
b=int(input())
x=int(input())
print(tr(a,b,x))




d = lambda a,b,c:a+b+c
    
print("trijsturis neeksiste")




print(d(5,7,7))     
