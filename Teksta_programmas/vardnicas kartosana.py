# Funkcija, kas atgriež vērtību “gads”:
def ageFunc(ele):
    return ele["vecums"]


#deklarējot studentu vārdnīcu sarakstu
studenti =[
{'vārds': "Atzīmēt","e -pasts":'[e -pasts aizsargāts]',"vecums": 28},
{'vārds': 'Džons',"e -pasts":'[e -pasts aizsargāts]',"vecums": 23},
{'vārds': 'Alberts',"e -pasts":'[e -pasts aizsargāts]',"vecums": 21},
{'vārds': "Kamerons","e -pasts":'[e -pasts aizsargāts]',"vecums": 27},
{'vārds': "Teilore","e -pasts":'[e -pasts aizsargāts]',"vecums": 25}
]
#saraksta kārtošana
studenti.sort(key=ageFunc)
#izdrukāt sakārtoto sarakstu
print(studenti)
