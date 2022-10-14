ves1 = int(input())
ves2 = int(input())

g = 1995

while ves1 > ves2:
    ves1 += -ves1*0.1
    g += 1 
    print(g, round(ves1,0) )
