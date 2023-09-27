from random import shuffle
durvis = ['Spoks','empty','empty']
life = 1
count = 0
spele = {}
while True:
    jautajums = input("Sveiki! Spēlējam? (y/n)>> ")
    if jautajums == "y":
        vards = input("Tavs vārds>> ")

        while True:
            choise = int(input("Durvju numurs: "))
            shuffle(durvis)
            count += 1
            if choise <4:
                if durvis[choise-1] == 'Spoks':
                    life -= 1
                    print("Spoks atņem dzīvibu","Palika dzīves: ",life)
            
                if durvis[choise-1] == 'Empty':
                    life +=1 
                    print("Spoka nav","Palika dzīves: ",life)
        
                if durvis[choise-1] == 'Empty': 
                    life +=1  
                    print("Spoka nav","Palika dzīves: ",life) 
        
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
    
