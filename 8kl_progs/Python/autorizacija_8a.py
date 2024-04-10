'''
a = {"Anna":"123","Ivars":"456"}

#b ={}
vards = input("login: ")
parole = input("parole: ")
a.get(vards)
parole = a.items()
for key, value in a:
    if value == parole:
        print(key)


'''
myDict = {"Anna": "123", "Ivars": "456"}

dict_items = myDict.items()
print("Given value is:")
myValue = input("parole: ")
print(myValue)
print("Parole pareiza:")
for key, value in dict_items:
    if value == myValue:
        print(key)



