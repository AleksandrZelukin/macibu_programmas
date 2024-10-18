teksts = input("Uzrāksti kadu tekstu: ")
#Faila atveršana ierākstišanai
f = open("darbs_ar_tekstu_7b.txt","a", encoding="utf-8")
print(teksts,file=f)
f.close()
#Faila atveršana lasišānai
f = open("darbs_ar_tekstu_7b.txt","r", encoding="utf-8")
for i in f:
    print(i, end='')
    
f.close()