a = {"Aija":123,"Ivars":456,"Olga":123}

vards = input("Login: ")
parole = input("parole: ")

#print(a.get(vards))

b = a.items()
#print(parole)
for key, value in b:
    if value == parole:
        print(key)