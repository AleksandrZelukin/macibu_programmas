for i in range(10):
    import random
    n = random.randrange(1,6,1)
    a= int(input("Uzmini skaitli no 1 lidz 6:"))
    if a > 6:
        print("!")
        break
    if n == a:
        print("Dators uzmine skaitli ",n)
        print("uzvara!")
    else:
        print("Dators uzmine skaitli ",n)
        print("U-u-u-u!")