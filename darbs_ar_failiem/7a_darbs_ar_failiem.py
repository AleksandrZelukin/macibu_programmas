#a = input("Ievādi vārds un talr.numurs >>")
a = {}
while True:
    vards = input("Vārds: ")
    talrunis = input("talrunis: ")
    if vards =="none" and talrunis=="none":
           break
    a[vards] = talrunis

    

f = open("7a_talruni.txt","a",encoding="utf-8") #Rākstit failā
print(a, file=f)
f.close()r