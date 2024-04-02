a = int(input("Pamats:  "))
h = int(input("Augstums:  "))
s = a*h

f = open("darbs_ar_failem_8b.txt","w",encoding="utf-8")

print(f"Tainsstūra ar platumu {a} un augstumu {h} platums ir {s}", file=f, end=";")

f.close()