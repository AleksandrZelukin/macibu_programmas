from random import shuffle
durvis = ['Dragon','Water','Empty']
life = 1
count = 0


while True:
    izvele = int(input("Durvis numurs- "))
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
        print("Jūs zaude viss...", count)
        break