a = "Grāmata"
# print(a)
a1 = list(a)
# print(a1)
# a2 = a1[::-1]
# print(a2)
# a3 = " ".join(a2)
# print(a3)
# a4 = a3.upper()
# print(a4)
lat = ["ā","Ā","ē","Ē","ī","Ī","ķ","Ķ","ļ","Ļ","ņ","Ņ","š","Š","ū","Ū","ž","Ž"]
d = 0
for i in a1:
    if i in lat:
        d += 1
        print(f"Vārdā {a} ir {d} burtus ar diakritiskām zīmēm")
    else:
        print(f"Vārdā {a} nav diakritisko zīmju")
        break