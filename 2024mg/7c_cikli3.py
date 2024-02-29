a = [48,17,3,2,7,19,24,4,2,9,5,17,7]
b = []
for i in a:
    if i<9:
        b.append(i)
print(a)
print(b)
c = [a[0],a[-1]]
print(f"Sarakstā a pirmais elements- {a[0]}, pedejais elements - {a[-1]}")
