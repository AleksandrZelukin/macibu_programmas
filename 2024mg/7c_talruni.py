t = {}

while True:
    vards = input("Vārds: ")
    if vards == "stop":
        break
    talrunis = input("talrunis: ")
    t[vards] = talrunis

for i in t.keys():
    print(i,t[i])