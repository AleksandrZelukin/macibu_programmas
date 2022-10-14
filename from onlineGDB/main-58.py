bd = int(input()) # ja ir dzimšanas diena - 1
s = int(input()) # ātrums
if bd == 0:
    if s<=60:
        print("no soda nauda")
    if s>=61 or s<=80:
        print("sods 1 punkts")
    if s>= 81:
        print("sods 2 punkti")
        
if bd == 1:
    if s<=65:
        print("no soda nauda")
    if s>=66 or s<=80:
        print("sods 1 punkts")
    if s>= 81:
        print("sods 2 punkti")
        