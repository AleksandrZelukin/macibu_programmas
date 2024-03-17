a = int(input("Pirmais skatlis: "))
b = int(input("Otrais skaitlis: "))

izvele = input("Ko darīsim? (+,-,*,/)")

if izvele == "+":
    d = a+b
elif izvele =="-":
    d = a-b
elif izvele =="*":
    d = a*b
elif izvele =="/":
    d = a/b

print(d)
