from random import shuffle
doors = ['Dragon','Water','Empty']
life = 1
count = 0
players = dict()
while True:
    jautajums = input("Spelējam? (y/n)>>")
    if jautajums == "y":
        vards = input("Ka tev sauc? >>")
        count = 0
        while True:
            choise = int(input("Dirvis numurs: "))
            if choise < 4 and choise > 0:
                shuffle(doors)
                count += 100
            if doors[choise-1] == 'Dragon':
                life -=1
                print('Jūs zaude dzīvibu! un atlikums ', life,"dzīves")
            if doors[choise-1] == 'Water':
                life +=1
                print('Jūs ieguva dzīvibu!un atlikums ', life,"dzīves")
            if doors[choise-1] == 'Empty':
                print('Nekas nenotiek!')
            if life <= 0:
                players[vards]=count
                print('Jūs zaude viss...',players)
                break
    if jautajums == "n":
        print("Spēles kopiens:")
        for key in players:
            print(key, players[key])
        break        