saraksts = open("phonebook-2024.txt","w" )
phonebook = {}
while True:
    jautajums = input("""
    ievāds jaunu ierākstu(j) 
    dzēst ierāksu(d)
    skatit visu sarakstu(s) \n >>""")
    if jautajums == "j":  
        vards = input("Vārds: ")
        numurs = input("Talruna numurs: ")
        phonebook[vards]=numurs
        
    if jautajums == "d":
        vards = input("Vārds: ")
        del phonebook[vards]
        print(f"dalibnieks {vards} dzests no sarakstā")
    if jautajums == "s":
        for key, value in phonebook.items():
            print (key,value)
               
    if jautajums == "stop":
        break
        
for key, value in phonebook.items():
    print (key,value)
print(phonebook, file=saraksts)

saraksts.close()

saraksts = open("phonebook-2024.txt","r" )
phonebook = saraksts.readline()
print(phonebook)



saraksts.close()

