a = int(input("Trijsturas a mala>>"))
b = int(input("Trijsturas b mala>>"))
c = int(input("Trijsturas c mala>>"))

perimetr=a+b+c
print(perimetr)

if a+b>c and c+b>a and c+a>b:
    print("Šis trijstūris ekziste!!!")
    f = open("Trijsuris.txt", "a",encoding="utf-8")
    print("Perimerts: {} cm".format(perimetr), "Trijstūris ar malam a:{}cm, b:{}cm, c:{}cm ekziste!".format(a, b, c),file=f )
    f.close()
else:
    print("Šis trijstūris neekziste!!!")


