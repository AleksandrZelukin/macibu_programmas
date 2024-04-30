from datetime import datetime
pk = input("Personas kods: ")
'''
if  len(pk)==12:
    print("Personas kods pareizs.")
else:
    print("Personas kods nav pareizs.")
'''
pk1 = list(pk[0:6])
diena = pk1[0:2]
meness = pk1[2:4]
gads = pk1[4:6]
#if pk[7] == "1":
#    a = 19
#else:
#    a = 20

#print(''.join(diena),''.join(meness),''.join(gads))
pk2 = (''.join(pk1))

datums = datetime.strptime(pk2, "%d%m%y")
print(datums)

    
