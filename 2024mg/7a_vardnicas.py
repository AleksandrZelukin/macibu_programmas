talruni = {}
'''
talruni["A"]= "678"
talruni["D"]="123"
talruni["B"]="100"

for k in talruni.keys():
    print(k,talruni[k])

for i in talruni.items():
    print(i)
'''
while True:
    vards = input("Vārds: ")
    talrunis = input("talrunis: ")
    
    talruni[vards] = talrunis
    print(talruni)
    if vards =="none" and talrunis=="none":
           break
