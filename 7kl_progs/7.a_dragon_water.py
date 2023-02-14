from random import shuffle
durvis = ['Dragon','Water','empty']
life = 4
count = 0

while True:
    choise = int(input("Durvju numurs: "))
    shuffle(durvis)
    count += 100
    if choise <4:
        if durvis[choise-1] == 'Dragon':
            print("Jūs zaudeja dzīvibu!")
            life -=3
        if durvis[choise-1] == 'Water':
            print("Jūs ieguva dzīvibu!")
            life +=1 
        else:
            print("Nekas nenotiek")
        if life ==0:
            print("Spēle beugusies. Jūsu konts: ",count) 
            break
    else:
        print("Durvis ar numuru", choise,"neekziste!")
    