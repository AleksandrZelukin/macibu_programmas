#Гипотеза Коллатца
a = int(input())
count=0
while a>1:
    if a%2==0:
        a = a//2
        print(a)

    elif a%2!=0:
        a = 3*a+1
        print(a)
    count += 1    
print(f"{count} soļos")
