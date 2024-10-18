a = input("Uzrāksti kautko: ")


f = open("10b_teksts.txt","a",encoding="utf-8")
print(a, file=f)
print(f"'{a}' ir ierakstīts failā")
f.close()