from random import shuffle
durvis = ['Dragon','Water','empty']
life = 2
count = 0

while True:
    choise = int(input("Durvju numurs: "))
    shuffle(durvis)
    count += 100
    if choise <4:
        if durvis[choise-1] == 'Dragon':
            life -= 1
            print("Dragon atņem dzīvibu","Palika dzīves: ",life)
            
        if durvis[choise-1] == 'Water':
            life +=1 
            print("Water dod tev 1 dzīvibu","Palika dzīves: ",life)
        
        if durvis[choise-1] == 'Empty':   
            print("Nekas nenotiek!")  
        
        if life == 0 :
            print("Spēle beigusies. Jūsu konts: ",count) 
            break
    else:
        print("Durvis ar numuru", choise,"neekziste!")
    