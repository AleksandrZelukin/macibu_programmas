
phonebook=dict()

phonebook['Anna']='344567'
phonebook['Olegs']='456789'
phonebook['Aivars']='457890'
phonebook['Olga']='344567'
phonebook['Ainars']='456789'
phonebook['Aivarin']='457890'
phonebook['Annee']='344567'
phonebook['Antons']='456789'
phonebook['Aiva']='457890'
phonebook['Ant']='344567'
phonebook['Olejik']='456789'
phonebook['A']='457890'
print("Tavi draugi:")
for key in phonebook:
    print(key)
    

while True:
    f = input("meklēt tālruņa numuru - 1\nDzest ierakstu - 2\nPievienot ierakstu - 3\nIziet - 4\n")
    
    if f == '1':
        print('Ievadi vardu: ')
        a=input()
        print('Zvani: ',phonebook.get(a))
        
    
    if f == '2':
        print ('Ievadi vardu:  ')
        a=input()
        del phonebook[a]
        print('Ieraksts ', a, 'dzests!')
        
    if f == '3':
       print('Ievadi vardu:  ')
       a=input()
       print('Ievadi talruna numurs:  ')
       b=input()
       phonebook['a'] = b
        
    if f=='4':
        break   



