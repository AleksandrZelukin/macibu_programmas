from random import shuffle
rez = dict()

while True:
    choice = input ('Spelejam? y/n\n')
    if choice == 'y':
        players = input('Tavs vards:  ')
        doors = ['dragon', 'water', 'empty', 'mikstūra']
        lives = 4
        score = 0
        penalty = 0
        while True:
            choice = int(input('Ievādi durvu numuru (1 - 4): '))
            shuffle(doors)
            score += 1
           
            if doors[choice - 1] == 'dragon' and penalty > 0 :
                print('Jūs cīnījāties ar pūķi un zaudējāt dzīvību.')
                lives -= 2
                penalti -= 1
                print('Tev palika', lives, 'dzīvēs!')
            elif doors[choice - 1] == 'dragon' and penalty == 0 :
                print('Jūs cīnījāties ar pūķi un zaudējāt dzīvību.')
                lives -= 1
                print('Tev palika', lives, 'dzīvēs!')

            elif doors[choice - 1] == 'water' and penalty > 0:
                print('Jūs dērāt dzīvo ūdeni un ieguvāt dzīvību.')
                lives += 1
                penalty -= 1
            elif doors[choice - 1] == 'water' and penalty == 0:
                print('Jūs dērāt dzīvo ūdeni un ieguvāt dzīvību.')
                lives += 0

                
            elif doors[choice - 1] == 'mikstūra':
                penalty += 1
                print ('sods', penalty, 'punkts')

            elif doors[choice - 1] == 'empty' and penalty > 0 :
                lives += 1
                penalty -= 1
                print('Tev palika', lives, 'dzīvēs!')
            elif doors[choice - 1] == 'empty' and penalty == 0:
                 lives += 1
                 
                 
            
                
            else:   
                print('Nekas nav noticis.')
            if lives == 0:
                rez[players]=score
                for key in rez:
                    print (key,rez[key])
                break

    if choice == 'n':
        print('Speles rezultati:')
        for key in rez:
                print(key,'nopelnija', rez[key], 'punktus')
        break
