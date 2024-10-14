angle1 = int(input("Pirmais lenkis-->> "))
angle2 = int(input("Otrais lenkis-->> "))
angle3 = int(input("Trešais lenkis-->> "))

if angle1+angle2+angle3 == 180:
    f = open("trijsturis.txt","a",encoding="utf-8")
    print("Tas ir trijsturis, lenķi šādi: {}, {}, {}".format(angle1,angle2,angle3),file=f)
    f.close()
else:
    print("H-m-m, tas ir kaut kas nezinamais...")