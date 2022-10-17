'''
Pļavā rotaļājas bērni un suņi. 
Zinot galvu un kāju kopējo skaitu (g un k), 
atrast, cik bērnu un cik suņu ir pļavā (b un s)
'''
g = int(input("Galvas: "))
k = int(input("Kājas: "))
x=k-(g*2) #"liekas" kajas
s=x/2 #suņu skaits

b=g-s #bernus skaits

print("suņus skaits: ", s)

print("bernus skaits: ", b)