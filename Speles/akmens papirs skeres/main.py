import random
count1 = 0 
count2 = 0 
count3 = 0 

while True:
    player = int(input("1 - akmens,\n2 - šķeres, \n3 - papirs.\n0 - Iziet no spēles\n"))
    
    if player == 1:
            print("Jūs izvēlas akmens.")  
    if player == 2:
            print("Jūs izvēlas šķeres.") 
    if player == 3:
            print("Jūs izvēlas papirs.") 
    if player == 0:
        
        print("neizšķirts - ", count1, "Jūs uzvaretājs - ", count2, "Dators uzvaretājs - ", count3)
        
        counter = ["neizšķirts",count1,"Jūs uzvaretājs", count2, "Dators uzvaretājs", count3]
        for i in counter:
            print(i)
        break
    
    comp = random.randint(1, 3)
    if comp == 1:
            print("Dators izvēlas akmens.") 
    if comp == 2:
            print("Dators izvēlas šķeres.")
    if comp == 3:
            print("Dators izvēlas papirs.")
    
# определяем победителя
    if player == comp:
            print("neizšķirts!")
            count1 += 1
    if player == 1 and comp == 2:
            print("Jūs uzvaretājs!")
            count2 += 1
    if player == 1 and comp == 3:
            print("Dators uzvaretājs!")
            count3 += 1
    if player == 2 and comp == 1:
            print("Dators uzvaretājs!") 
            count3 += 1 
    if player == 2 and comp == 3:
            print("Jūs uzvaretājs!") 
            count2 += 1
    if player == 3 and comp == 1:
            print("Jūs uzvaretājs!")
            count2 += 1
    if player == 3 and comp == 2:
            print("Dators uzvaretājs!")
            count3 += 1
            
        
    
