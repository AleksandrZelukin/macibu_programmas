file = open("dati.txt", "w")

book=dict()
print("print 'end' for exit\nprint Enter for continue")

while True:
    a=(input())
    if a == "end":
        break
    a=input()
    b=input()
    book[a]=b
    
    print(book)
file.write(str(book))    
file.close()
