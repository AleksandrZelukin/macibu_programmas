a = input("Ievadi vārdus: ")

a = list(a)

a= "".join(a)
# print(a)
b =("ā","Ā","ē","Ē","ī","Ī","ķ","Ķ","ļ","Ļ","ņ","Ņ","š","Š","ū","Ū","ž","Ž")
d= 0
v=[]
for i in a:
    if i in b:
        d += 1
        v.append(i)
if d > 0:
    # v="".join(v)
    v = list(v)
    print(f"Vārdā {a} ir {d} burtus ({v}) ar diakritiskām zīmēm")
else:
    print(f"Vārdā {a} nav diakritisko zīmju")  
