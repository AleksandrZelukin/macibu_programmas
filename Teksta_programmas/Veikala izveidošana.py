veikals=dict()
print("'saraksts'-skātit sarakstu\n'end'-iziet no programmas")

while True:
    a=(input())
    if a == "end":
        break
    elif a == "saraksts":
        print("nesakārtots saraksts: ",veikals)
        veikals_sorted = dict(sorted(veikals.items(), key=lambda s: s[::-1]))
        print("sakārtots saraksts: ", veikals_sorted)
    else:
        b=input()
    veikals[a]=b
    
    
