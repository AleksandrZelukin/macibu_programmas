books = {}
vards = input("Vārds>> ")
talrunis = input("Talrunis>> ")
f=open("talruna_gramata.txt","a")
books[vards]=talrunis

print(books, file=f)

f.close()