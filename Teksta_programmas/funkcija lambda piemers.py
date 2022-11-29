def sum(a,b):
    return a+b

print (sum(5,7))


lsum = lambda a,b: a+b
print(lsum(5,7))

def mana_summa (n):
    return lambda a: a+n


print(mana_summa(7)(5))


