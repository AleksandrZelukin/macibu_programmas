a = {"Ivars":"123","Olga":"456","Igors":"789"}

vards = input("Login: ")
parole = input("parole: ")

if a.get(vards) == parole:
    print("OK!")
else:
    print("Lietotājvārds vai parole nesakrīt!")