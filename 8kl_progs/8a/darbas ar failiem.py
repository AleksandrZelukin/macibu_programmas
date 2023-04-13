a = int(input())
b = int(input())
c = a+b
f = open("darbsArFailiem.txt","a")
print("{} + {} = {}".format(a,b,c),file=f)
print("{} + {} = {}".format(a,b,c))
f.close()