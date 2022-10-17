users = {"user1" : "1234", "user2" : "1456"}


print ("Welcome to this password system")
print ("Please input your username")



choice = input ("")



print ("Please enter your password")



choice2 = input ("")



if (choice in users) and (choice2 == users[choice]):
    print ("Access Granted")
else:
    print ("Access Denied. Should I create a new account now?")
    newaccount = input ("")
    if newaccount == "yes" or "Yes":
        print ("Creating new account...")
        print ("What should your username be?")
        newuser = input ("")
        print ("What should your password be?")
        newpass = input ("")
        users.update({newuser:newpass})
        
print(users)