a = input("Jūsu vārds>> ")

f = open("darbsArFailiem.txt","a",encoding="utf-8")
print(a,file=f)
f.close()