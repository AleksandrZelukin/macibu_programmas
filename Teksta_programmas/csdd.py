#rn=dict()
rn={}

while True:
    f=input("ievādit auto ipašnieka datus - 1\nsaraksta skats - 2\niziet no programmas - 0\n")

    if f == '1':
    
        print("Ievadi valsts numurs")
        a=input()

        print("Ipašnieks")
        b=input()

        rn[a]=b
        #rn.setdefault(a,b)

    if f== '2':
        
        for key in rn:
            print(key, rn[key])


    if f =='3':

        file = open('csdd.txt', 'w')
        for key, value in rn.items():
            file.write(f'{key}, {value}\n')
        file.close()
            
    if f == '0':
        break
        
