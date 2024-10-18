a = input("Pirkums un cena: ")

f = open("darbs_ar_failiem_8c.txt","a",encoding="utf-8")

print(a, file=f)
f.close()

for i in open("darbs_ar_failiem_8c.txt","r",encoding="utf-8"):
    print(i)