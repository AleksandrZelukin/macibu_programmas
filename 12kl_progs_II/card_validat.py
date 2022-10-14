c=input("card number= ")
cc=len(list(c))
if cc==15 and c[0]=="3":
    print("AMEX")
elif cc==16 and c[0]=="5":
    print("MASTERCARD")
elif cc==13 or cc==16 and c[0]=="4":
    print("VISA")
else:
    print("NOT VALID CARD")