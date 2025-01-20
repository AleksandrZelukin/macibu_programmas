import random

print("""
      ==========
      Akmens - 1
      Šķēres - 2
      Papīrs - 3
      ==========
      """)

vardi = {1:"Akmens",2:"Šķēres",3:"Papīrs"}

speletajs = int(input("Jūsu izvēlē: "))
dators = random.randint(1,3)
print("Jūsu izvēļe: ",vardi[speletajs])
print("Datora izvēlē:",vardi[dators])

if speletajs == dators:
    print("spēles izloze")
elif speletajs == 1 and dators == 2 or speletajs == 2 and dators == 3 or speletajs == 3 and dators == 1:
    print("Jūs uzvāreja!") 
else:
    print("Dators uzvāreja!")
