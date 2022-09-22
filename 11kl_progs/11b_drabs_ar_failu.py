book=dict()
print("print 'end' for exit\npress Enter for continue")

while True:
    a=(input())
    if a == "end":
        break
    a=input()
    b=input()
    book[a]=b
    
    print(book)
file = open("11b_drabs_ar_failu.txt", "a")

file.write(str(book))
file.write("\n")

file.close()
