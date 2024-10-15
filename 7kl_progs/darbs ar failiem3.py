a = int(input("Ievadi kvadrata malu: "))
perimetrs = a*4

f=open("perimetrs.txt","a")
print("Kvadrata perimetrs ar malu ",a,"ir: ",perimetrs,file=f )
f.close()

f=open("perimetrs.txt","r")
for s in f:
    print(s, end='')
f.close()