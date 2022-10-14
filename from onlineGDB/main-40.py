users = {"user1" : "1234", "user2" : "1456"}

print ("Welcome to this password system \nPlease input your username")

choice = input ("")

print ("Please enter your password")

choice2 = input ("")

if (choice in users) and (choice2 == users[choice]):
    print ("Access Granted")
else:
    print ("Access Denied.")
   
        

