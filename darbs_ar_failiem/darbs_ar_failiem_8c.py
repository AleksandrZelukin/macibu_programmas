a = int(input("Pamats: "))
h = int(input("Augstums: "))
s = a*h
f = open("darbs_ar_failiem_8c.txt","a",encoding="utf-8")

print(f"Taisnstūra platums ir {s}cm2",file=f)
f.close() 