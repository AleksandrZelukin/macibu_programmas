a = int(input("Tainsstūra pamats: "))
h = int(input("Tainsstūra augstums: "))
s = a*h 


f = open("tainsstura_platums_8a.txt","a",encoding="utf-8")
print(f"Tainsstūra platums ar pamatu {a} un augstumu {h} ir {s}")
print(f"Tainsstūra platums ar pamatu {a} un augstumu {h} ir {s}",file=f)
f.close()