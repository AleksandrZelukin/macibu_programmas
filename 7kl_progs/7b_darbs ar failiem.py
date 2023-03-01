f = open("7kl_progs/darbs_ar_failiem.txt","r") # Skātit fails
for s in f:
    print(s, end='')
f.close()

a = input("Ievādi teksts >>")
f = open("darbs_ar_failiem.txt","a") #Rākstit failā
print(a, file=f)


f.close()
f= open("darbs_ar_failiem.txt","r") # Skātit fails
for s in f:
    print(s, end='')
f.close()
