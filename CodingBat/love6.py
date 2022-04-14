def love6(a,b):
    if a==6 or b==6:
        return True
    if a+b ==6:
        return True
    if abs(a-b) ==6 or abs(b-a) ==6:
        return True



a=int(input())
b=int(input())

c = love6(a,b)

print(c)

