for i in range (10):
    import random
    a = int(input("Uzmini skaitli no 1 lidz 6: "))
    n = random.randrange(1,6,1)
    if a>6 or a<1:
        break
    if a == n:
        print("Es uzvareju!")
    else:
        print("Dators izdoma skaitli:", n, "un uzvarei!")
