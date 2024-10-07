'''
a = {}

a[1]=100
a[2]=200
a[3]=300

print(a)

del a[2]

print(a)
'''
d={}
print("Nospiediet stop, lai izietu!")
while True:
    a= input("Key: ")
    if a =="stop":
        b=a
        d[a]=b
        del d["stop"]
        print(d)
        break
    else:
        b= input("Value: ")
    d[a]=b
    print(d)
    '''
    if a =="stop":
        del d["stop"]
        print(d)
        break
    '''

vardnica = {}
while True:
    pilseta = input("Pilsēta: ")
    if pilseta == "none":
            break
    valsts = input("Valsts: ")
    vardnica[pilseta]=valsts
    if valsts == "none":
            break
    for key, value in vardnica.items():
        print (key,value)
