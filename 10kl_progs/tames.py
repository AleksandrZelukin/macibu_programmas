'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/#gridas-mainas-izmaksu-aprekinu-programma
Pasūtītājs Andris Ziediņš, remontē dzīvokļus un sagatavo tāmes. 
Andra draugs, kas ir programmētājs, 
izveidoja specifikāciju pēc Andra prasībām. 
Jūsu uzdevums ir uzrakstīt funkciju, 
kas no dotiem argumentiem aprēķina un atgriež Andrim derīgu rezultātu.
'''

import math
print("Cenas")
l = float(input("Lamināts(par paku),euro: "))
t = float(input("Tapetes(par rulli),euro: "))
k = float(input("Krāsa(par 1.litru),euro: "))

def remonts(garums, augstums, platums):
    return math.ceil(garums*platums/2.131), math.ceil((garums+platums)*augstums/10), math.ceil((garums*platums)*0.4)

x = int(input("garums: "))
y = float(input("augstums: "))
z = int(input("platums:"))


print(remonts(x,y,z))
t = remonts(x,y,z)

laminats = t[0]*l
tapetes = t[1]*t
krasa = t[2]*k

kopa = laminats+tapetes+krasa

print("Kopā jamāksā: ", round(kopa,2),"Euro")

'''
2.	Pie jums ir vērsies uzņēmums SIA Stabili podesti, ar vēlmi atvieglot materiālu sagatavošanu finiera podestu ražošanai. Podestus ražo gan standarta izmēros, gan pēc pasūtītāja izmēriem.
Jūs uzaicina uz ražotni iepazīties ar produkciju, un var novērot, ka podesti principā ir taisnstūra paralēlskaldņi, kas izveidoti no sešām finiera plāksnēm, kas savā starpā sastiprināti ar divpadsmit leņķveida līstēm, un stūros nostiprināti ar astoņiem stūra savienojumiem.
Uzņēmums vēlas automatizēt izlietoto materiālu uzskaiti un jums tiek uzticēts uzrakstīt kodu funkcijai, kas nosaka materiālu veidu un daudzumu dotā izmēra podestam.

'''