f = open("10b_teksts.txt","r",encoding="utf-8")
for i in f:
    print(i)

f.close()

f = open("10b_teksts.txt","r",encoding="utf-8")

a = f.readlines()
print(a)

f.close()