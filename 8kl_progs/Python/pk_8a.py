from datetime import datetime
pk = input("Personas kods: ")
if  len(pk)==12:
    pk1 = list(pk)

    if pk[7] == "1":
        pk1.insert(4,"19")
    else:
        pk1.insert(4,"20")
    pk1 = pk1[0:7]

    pk2 = (''.join(pk1))
    try:
        datums = datetime.strptime(pk2, "%d%m%Y")
        print(datums)
    except:
        print("Personas kods nepareizs!")
else:
    print("Personas kods nav pareizs.")

