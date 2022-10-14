a = int(input("Get coins:  "))


b = a // 25
c = (a - b * 25)//10
d = (a - b * 25 - c *10)//5
e = (a - b * 25 - c *10 - d * 5)//1
print("Quarter (25с)", b )
print("Disme (10с)", c)
print("Nickel (5с)", d )
print("Penny (1с)", e )
print("control:  ", b*25 + c*10 + d*5 + e)