users = {"user1" : "1234", "user2" : "1456"}
choice_count = 1
while choice_count < 4:
    print ("Welcome to this password system \nPlease input your username")
    choice = input ("")
    print ("Please enter your password")
    choice2 = input ("")
    if (choice in users) and (choice2 == users[choice]):
        print ("Access Granted")
        break
    else:
        print ("Access Denied.")
        choice_count += 1
        print("Jus izmanto ", choice_count - 1 ,"Meginajumus no 3 meģnājumus!")





