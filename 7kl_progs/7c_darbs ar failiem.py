phonebook = {}

while True:
    menu = input("""
    =========================
    # Pievienot jaunu ierakstu - 1   #          
    # Rediģet ierakstu - 2               #
    # Dzest ierakstu - 3                   #  
    # Skatit visus ierakstus - 4        #     
    # Saglabat un Iziet - 5              #           
    =========================
    """)
    if menu == '1':   
        vards = input("Vārds: ")
        tlr_num = input("Tālrunis: ")
        phonebook[vards]=tlr_num

    if menu == '2':
        for key in phonebook:
            print(key, phonebook[key])

        vards = input("Vārds: ")
        tlr_num = input("Tālrunis: ")
        phonebook[vards]=tlr_num

    if menu == '3':
        vards = input("Vārds: ")
        del phonebook[vards]

    if menu == '4':
        for key in phonebook:
            print(key, phonebook[key])
    if menu == '5':
        f = open("7c_phonebook.txt","a")
        for key in phonebook:
            print(key, phonebook[key],file=f)
        f.close()
        break



#print(phonebook, file=f)

