v = int(input())
d = int(input())

# v-0 avaļinājums v-1 strāda
# 6,0 - brīvdienas
# alarm '7:00' un '10:00'

if v==0:
    if d>=1 and d<=5:
        print("10:00")
    if d==0 or d==6:
        print("OFF")
    
if v==1:
    if d>=1 and d<=5:
        print("7:00")
    if d==0 or d==6:
        print("10:00")