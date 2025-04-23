a=[1,5,13,"Rīga","Latvija",3.6,100]
for i in a:
    if type(i) == str:
        print(i)
for i in a:
    if type(i) == float:
        print(i)
for i in a:
    if type(i) == int:
        print(i)

a = "taxi"
print(a)
b = list(a)
# print(b)
c=(b[::-1])
b = "".join(c)
print(b)

lat=["ā","ē","ī","ļ","ņ","š","ž","ķ",
     "ģ","č","ū","Ē","Ā","Ģ","Ķ","Č",
     "Ū","Ž","Š","Ļ","Ņ"]
d=0
a=input("Ievadi vārdu: ")
a1 = list(a)
for i in a1:
    if i in lat:
        d += 1
if d == 0:
    print(f"Vārdā {a} nav diakritisko zīmju")
else:
    print(f"Vārdā {a} ir {d} diakritiskās zīmes")