from datetime import datetime
pk = input("Personas kods: ")

if len(pk) == 12:
    print("pk garums OK!")
else:
    print("not OK!")

pk1 = list(pk)
milenium = pk1[7]
if milenium == "1":
    pk1.insert(4,"19")
if milenium == "2":
    pk1.insert(4,"20")
    
pk1 = pk1[0:7]
pk1 = (''.join(pk1))
try:
    datumu_parbaude = datetime.strptime(pk1, "%d%m%Y")
    print(datumu_parbaude)
except:
    print("Personas kods nepareizs!")