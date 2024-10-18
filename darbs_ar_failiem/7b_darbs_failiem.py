f = open("7b_darbs_failem.txt","a")
c = {}
while True:
    vards = input("Drauga vārds: ")
    talrunis = input("Tālruna numurs: ")
    if vards =="none" and talrunis=="none":
        for i in c.keys():
            print(i,c[i],file=f)
        break
    c[vards] = talrunis


f.close()