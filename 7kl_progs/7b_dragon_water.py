from random import shuffle
doors = ['Dragon','Water','Empty']
life = 2
count = 0
while True:
    choise = int(input("Dirvis numurs: "))
    if choise < 4 and choise > 0:
        shuffle(doors)
        count += 100
        if doors[choise-1] == 'Dragon':
            life -=2
            print('Jūs zaude dzīvibu! un atlikums ', life,"dzīves")
        if doors[choise-1] == 'Water':
            life +=1
            print('Jūs ieguva dzīvibu!un atlikums ', life,"dzīves")
        if doors[choise-1] == 'Empty':
            print('Nekas nenotiek!')
        if life <= 0:
            print('Jūs zaude viss...', count)
            break