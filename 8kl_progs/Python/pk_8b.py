from datetime import datetime
pk = input("Personas kods: ")
'''
if len(pk) == 12:
    print("pk OK!")
else:
    print("not OK!") 
'''
pk1 = (''.join(list(pk[0:6])))
'''
dd = pk1[0:2]
mm = pk1[2:4]
yy = pk1[4:6]
print(dd,mm,yy)
'''

datumu_parbaude = datetime.strptime(pk1, "%d%m%y")
print(datumu_parbaude)