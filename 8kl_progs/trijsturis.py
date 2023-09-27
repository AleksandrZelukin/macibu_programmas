a = int(input("Trijstura mala a: "))
b = int(input("Trijstura mala b: "))
c = int(input("Trijstura mala c: "))
f = open("trijsturis.txt","a",encoding="utf-8")
if a+b>c and b+c>a and a+c>b:
    print("Trijsturis ekszistē!")
    
    print("Trijsturis ar malam a = {},b = {},c = {} ekszistē!".format(a,b,c),file=f)
    
else:
    print("Trijsturis neekszistē!", file=f)

f.close()