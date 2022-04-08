veikals = {'Piens': 1.20,
          'Kefirs': 1.70,
          'Zivis': 2,
          'Siers': 4.20,
      	  'Sviests': 3.20,
          'Cepumi': 2,
          'Saldējums': 0.40,
          'Biezpiens': 2.50,
          'Jogurts': 1,
          'Salvetes': 0.4,
          'Maize': 1.20,
          'Torte': 5.50,
          'Risi':3.20,
          'Manna': 1.20}
nauda = float(input("Cik nauda tev ir? "))

for k, v in veikals.items():
    if v <=  nauda:        
    	print(k, sep='/n')
    	nauda -= v

nauda = float(input("Cik nauda tev ir? "))

sorted_preces = dict(sorted(veikals.items(), key=lambda x: x[::-1]))

for k, v in sorted_preces.items():
    if v <=  nauda:        
    	print(k, sep='/n')
    	nauda -= v

