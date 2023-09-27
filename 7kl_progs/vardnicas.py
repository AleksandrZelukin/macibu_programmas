a= {}
while True:
    vards = input('Vārds:')
    atzimes = input('Atzīmes:')
    if vards == 'stop'and atzimes =='stop':
        break
    a[vards]=atzimes
    
    print(a)
    