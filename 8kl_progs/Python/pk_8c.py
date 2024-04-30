from datetime import datetime
pk = input("Ievadi personas kods: ")
if len(pk) == 12:
    print("Personas koda garums pareizs!")
    pk1 = list(pk)
    dd = pk1[0:2]
    mm = pk1[2:4]
    gg = pk1[4:6]    
    if pk1[7] == '1':
        gg.insert(0,"19")
    elif pk1[7] == '2':
        gg.insert(0,"20")
    else:
        print("Personas koda dati nav pareizi!")
    dzimsanas_date = (''.join(dd),''.join(mm),''.join(gg))
    date_kontrole=datetime.strptime((''.join(dzimsanas_date)), "%d%m%Y")
    print(date_kontrole)
else:
    print("Personas koda garums nav pareizs!")
    

