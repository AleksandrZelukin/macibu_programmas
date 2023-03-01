f = open("darbs_ar_failiem.txt","r") # Skātit fails
for s in f:
    print(s, end='')
f.close()

a = input("Ievādi teksts >>")
f = open("darbs_ar_failiem.txt","w") #Rākstit failā
print(a, file=f)
f.close()

f = open("darbs_ar_failiem.txt","r")
for s in f:
    print(s, end='')
f.close()

a = input("Ievādi teksts >>")
f = open("darbs_ar_failiem.txt","a") #Papīldināt fails
print(a, file=f)
f.close()

f = open("darbs_ar_failiem.txt","r")
for s in f:
    print(s, end='')
