pk = input("Personas kods: ")
'''
if len(pk) == 12:
    print("pk OK!")
else:
    print("not OK!") 
'''
pk1 = list(pk)

dd = pk1[0:2]
mm = pk1[2:4]
yy = pk1[4:7]
print(dd,mm,yy)