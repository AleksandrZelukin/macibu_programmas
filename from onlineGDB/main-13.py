# Izveidojam tukšu vardnicu
PhoneBook = dict()

# Aizpildim
PhoneBook['Olga'] = '+234567'
PhoneBook['Aivars'] = '123478'
PhoneBook['Osis'] = '2378745'
PhoneBook['Marija'] = '237844'
PhoneBook['Tatjana'] = '372549'


print(PhoneBook)

print(type(PhoneBook))

for key, value in PhoneBook.items():
    print(key, value)
    
for key in PhoneBook:
    print(key)
    
print(PhoneBook['Osis'])

a=input()
print(PhoneBook[a])




