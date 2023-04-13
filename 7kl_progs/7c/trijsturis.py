a = int(input("Trijstura mala a: "))
b = int(input("Trijstura mala b: "))
c = int(input("Trijstura mala c: "))

if a+b>c and b+c>a and a+c>b:
    f = open("trijsturis.txt","a")
    print("Trijsturis ar malam a= {},b = {}, c = {} ekzistē!".format(a,b,c),file=f)
    f.close()
    print("Dati ierakstiti datnē.")
else:
    print("Trijsturis neekzistē!")