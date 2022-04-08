import random
ver = 0
while (ver == 0):
        player = int(input("1 - akmens,\n2 - šķeres, \n3 - papirs.\n"))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
if player == 1:
        print("Jūs izvēlas akmens.")  
if player == 2:
        print("Jūs izvēlas šķeres.") 
if player == 3:
        print("Jūs izvēlas papirs.")  
comp = random.randint(1, 3)
if comp == 1:
        print("Dators izvēlas akmens.") 
if comp == 2:
        print("Dators izvēlas šķeres.")
if comp == 3:
        print("Dators izvēlas papirs.")
# определяем победителя
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2 
if player == 2 and comp == 1:
        win = 2  
if player == 2 and comp == 3:
        win = 1 
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("neizšķirts!")
if win == 1:
        print("Jūs uzvaretājs!")
if win == 2:
        print("Dators uzvaretājs!")
