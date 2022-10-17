# Izveidojam tukšu vardnicu
Capitals = dict()

# Aizpildim
Capitals['Latvija'] = 'Rīga'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Capitals['Igaunija'] = 'Tallinn'
Capitals['Polija'] = 'Varšava'

Countries = ['Latvija', 'Ukraine', 'USA', 'Igaunija', 'Polija']
print(Capitals)
dict_as_list = Capitals.items()
print(Capitals)
print(type(Capitals))
'''
for country in Countries:
    
    if country in Capitals:
        print('Galvaspilsēta ' + country + ': ' + Capitals[country])
    else:
        print('Sarakstā nav valsti ' + country)
'''
