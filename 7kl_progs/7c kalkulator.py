a , b= float(input("Pirmais skaitlis: ")), float(input("Otrais skaitlis: "))
#b = float(input("Otrais skaitlis: "))

print("Ko darīsim? * / - +")



s = input()

if s == "*":
    print("Reizināšanas rezulāts: {} ".format(a*b))
elif s == "/":
    print("Dališanas rezultāts: ",a/b)
elif s == "-":
    print("Atņemšanas rezultāts: ",a-b)
elif s == "+":
    print("Summa: ",a+b)
