from random import shuffle
durvis = ['Dragon','Water','empty']
life = 2
count = 0
spele = {}
while True:
    jautajums = input("Sveiki! Spēlējam? (y/n)>> ")
    if jautajums == "y":
        vards = input("Tavs vārds>> ")

        while True:
            choise = int(input("Durvju numurs: "))
            shuffle(durvis)
            count += 100
            if choise <4:
                if durvis[choise-1] == 'Dragon':
                    life -= 2
                    print("Dragon atņem dzīvibu","Palika dzīves: ",life)
            
                if durvis[choise-1] == 'Water':
                    life +=1 
                    print("Water dod tev 1 dzīvibu","Palika dzīves: ",life)
        
                if durvis[choise-1] == 'Empty':   
                    print("Nekas nenotiek!")  
        
                if life <= 0 :
                    spele[vards] = count
                    print("Spēle beigusies") 
                    for key in spele:
                        print(key, spele[key])
                    break
            else:
                print("Durvis ar numuru", choise,"neekziste!")

    if jautajums == "n":
        print("Spēles kopiens:")
        for key in spele:
            print(key, spele[key])
        print("Spēles kopiens:")
        break
    