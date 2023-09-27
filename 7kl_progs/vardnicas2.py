skola={}
skolniekus_skaits = int(input("Cik skolēnus klasē: "))
# izmantot cikls FOR
for i in range(skolniekus_skaits):
    vards = input("Skolnieka vārds: ")
    atzime = int(input("Skolnieka atzīme: "))

    skola[vards] = atzime

print(skola)
# izmantots cikls WHILE
while skolniekus_skaits > 0:
    vards = input("Skolnieka vārds: ")
    atzime = int(input("Skolnieka atzīme: "))

    skola[vards] = atzime
    skolniekus_skaits -=1
print(skola)