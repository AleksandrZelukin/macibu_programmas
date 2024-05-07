from datetime import datetime
pk = input("Ievadi personas kods: ")
if len(pk) == 12:
    pk1 = list(pk)
    if pk1[7] == '1':
        pk1.insert(4,"19")
    elif pk1[7] == '2':
        pk1.insert(4,"20")
    else:
        print("Personas koda dati nav pareizi!")
    pk1=pk1[0:7]
    try:
        date_kontrole=datetime.strptime((''.join(pk1)), "%d%m%Y")
        print(date_kontrole)
    except:
        print("Personas kods neekzistē")
else:
    print("Personas koda garums nav pareizs!")
  