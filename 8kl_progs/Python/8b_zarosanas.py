a = int(input("Ievadi malu a: "))
b = int(input("Ievadi malu b: "))
c = int(input("Ievadi malu c: "))

if a+b>c and a+c>b and b+c>a:
    print("Trijsturis ekzistē!")

else:
    print("Trijsturis neekzistē!")