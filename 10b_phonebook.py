import json
phonebook = {}
while True:
    menu = input("""
    =====================================
    |Pievienot jaunu ierakstu - 1       | 
    |Skatit visus ierakstus - 2         |
    |Iziet - 3                          |
    =====================================
    """)
    if menu == '1':
        vards = input("Vārds: ")
        tlr_num = input("Tālrunis: ")    
        phonebook[vards]=tlr_num
        saraksts = str(phonebook)
        f = open("talruna_saraksts.txt",'a')  
        # json.dump(phonebook,f)
        # print(phonebook,file=f)
        print(saraksts)
        f.close() 

    if menu == '2':
        f = open("talruna_saraksts.txt",'r')
        for s in f:
            print(s, end='')
        f.close()

    if menu == '3':
        break