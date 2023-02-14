from random import shuffle
doors = ['Dragon','Water','Empty']
life = 3
count = 0
while True:
    choise = int(input("Dirvis numurs: "))
    shuffle(doors)
    count += 100
    if doors[choise-1] == 'Dragon':
        life -=2
        print('Jūs zaude dzīvibu!')
    if doors[choise-1] == 'Water':
        life +=1
        print('Jūs ieguva dzīvibu!')
    else:
        print('Nekas nenotiek!')
    if life == 0:
        print('Jūs zaude viss...', count)
        break