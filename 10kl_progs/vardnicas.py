
a = {}

a[1]=100
a[2]=200
a[3]=300

print(a)

del a[2]

print(a)

d={}
while True:
    a= input()
    b= input()
    d[a]=b
    print(d)
    if a =="stop":
        del d["stop"]
        print(d)
        break