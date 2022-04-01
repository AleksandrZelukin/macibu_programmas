# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Latvia'] = 'Riga'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Latvia', 'France', 'USA', 'Estonia']

for country in Countries:
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if country in Capitals:
        print('Столица страны ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)

