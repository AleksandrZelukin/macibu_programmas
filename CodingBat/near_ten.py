def near_ten(num):
    rem = num % 10
    if rem <= 2 and rem >= 0:
        return True
    elif rem >= 8 and rem <= 9:
        return True
    else:
        return False
        
        
a=17

print(near_ten(a))
