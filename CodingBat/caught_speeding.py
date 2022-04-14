def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed<= 65:
            return 0
        elif speed >=66 and speed <=85:
            return 1 
        elif speed >= 86:
            return 2
            
    else:
        if speed<= 60:
            return 0
        elif speed >=61 and speed <=80:
            return 1 
        elif speed >= 81:
            return 2
            
            
a = 82
b = False

print(caught_speeding(a,b))
