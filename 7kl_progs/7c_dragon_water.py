from random import shuffle
durvis = ['Dragon','Water','Empty']

rezultats = {}
while True:
    jautajums = input ('Spelejam? y/n\n')
    if jautajums == 'y':
        players = input('Tavs vards:  ')
        life = 1
        count = 0
        while True:
            izvele = int(input("Durvis numurs- "))
            if izvele > 3 :
                print('Durvis ar sadu numuru nekziste')
                continue
            shuffle(durvis)
            count +=100
            if durvis[izvele-1] == 'Dragon':
                print('Jūs zaude dzīvibi!')
                life -=1
            if durvis[izvele-1] == 'Water':
                print('Jūs ieguva dzīvibu!')
                life +=1
            else:
                print('Nekas nenotiek!')

            if life == 0:
                rezultats[players] = count
                print("Jūs zaude viss...", count)
                print(rezultats)
                break
    if jautajums == 'n':
        break


            

            